import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
QUOTE = 'we’ll reset usage limits for all paid users across codex and ChatGPT work'
SOURCE = 'https://x.com/thsottiaux/status/2103637477760311522'


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('assets', 'src', 'locales', 'data'):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copy(ROOT / 'build.py', self.root / 'build.py')
        self.config = json.loads((ROOT / 'site.config.json').read_text())
        self.config['providerRepositories'] = {
            p: f'https://github.com/inmve/{p}-reset-alerts'
            for p in ('codex', 'claude', 'grok')
        }
        self.data = json.loads((ROOT / 'data/events.json').read_text())
        self.data['events'] = [e for e in self.data['events'] if e['provider'] != 'codex'] + [{
            'id': 'codex-test', 'provider': 'codex', 'status': 'announced',
            'type': 'usage_reset', 'announcedAt': '2026-09-26T00:07:00Z',
            'source': SOURCE, 'author': '@thsottiaux', 'quote': QUOTE,
            'scopeLabelKey': 'codexPaidScope', 'expectedDate': None,
        }]

    def build(self, success=True):
        (self.root / 'site.config.json').write_text(json.dumps(self.config))
        (self.root / 'data/events.json').write_text(json.dumps(self.data))
        result = subprocess.run([sys.executable, 'build.py', '--release'],
                                cwd=self.root, capture_output=True, text=True)
        if success:
            self.assertEqual(result.returncode, 0, result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def test_quote_and_subscription_are_visible_without_javascript(self):
        self.build()
        page = (self.root / 'public/index.html').read_text()
        self.assertIn('<blockquote>', page)
        self.assertIn(QUOTE, page)
        self.assertIn(SOURCE, page)
        self.assertIn('Completion has not been confirmed', page)
        for repo in self.config['providerRepositories'].values():
            self.assertIn(f'href="{repo}"', page)

    def test_feeds_are_separate_and_include_subscription_and_source(self):
        self.build()
        for provider in ('codex', 'claude', 'grok'):
            readme = (self.root / f'notifications/{provider}/README.md').read_text()
            self.assertIn('Watch → Custom → Releases', readme)
            event = max((e for e in self.data['events'] if e['provider'] == provider), key=lambda e: e['announcedAt'])
            self.assertIn(event['source'], readme)
            self.assertNotIn('### ' + ('Claude Code' if provider == 'codex' else 'Codex'), readme)
        codex = (self.root / 'notifications/codex/README.md').read_text()
        self.assertIn('> ' + QUOTE, codex)
        self.assertIn('Reset announced', codex)
        self.assertIn('Completion has not been confirmed', codex)
        combined = (self.root / 'minimal-README.md').read_text()
        self.assertIn('Claude Code', combined)
        self.assertIn('Banked reset', combined)

    def test_no_pending_announcement_is_not_a_claim_that_no_reset_happened(self):
        event = self.data['events'][-1]
        event['status'] = 'confirmed_completed'
        event.pop('quote')
        self.build()
        readme = (self.root / 'notifications/codex/README.md').read_text()
        self.assertIn('No newer reset announcement is recorded', readme)
        self.assertIn('Last recorded reset confirmation', readme)

    def test_quote_is_escaped_and_russian_copy_is_translated(self):
        self.data['events'][-1]['quote'] = '<script>alert(1)</script> & source'
        self.config['locale'] = 'ru'
        self.build()
        page = (self.root / 'public/index.html').read_text()
        self.assertIn('&lt;script&gt;', page)
        self.assertNotIn('<script>alert(1)</script>', page)
        self.assertIn('Подписаться на следующий сброс', page)
        self.assertIn('Завершение сброса пока не подтверждено', page)

    def test_announced_cards_quote_their_source_and_link_their_own_feed(self):
        import re
        self.build()
        page = (self.root / 'public/index.html').read_text()
        for provider in ('codex', 'claude', 'grok'):
            card = re.search(r'<article[^>]*data-provider="' + provider + r'".*?</article>', page, re.S).group()
            self.assertIn(self.config['providerRepositories'][provider], card)
            if provider in ('codex', 'claude'):
                event = max((e for e in self.data['events'] if e['provider'] == provider), key=lambda e: e['announcedAt'])
                self.assertIn('<blockquote>', card)
                self.assertIn(event['quote'], card)
                self.assertIn(event['source'], card)

    def test_release_requires_all_provider_repository_urls(self):
        del self.config['providerRepositories']['codex']
        result = self.build(success=False)
        self.assertIn('codex', result.stderr + result.stdout)


if __name__ == '__main__':
    unittest.main()
