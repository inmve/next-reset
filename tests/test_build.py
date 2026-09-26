import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('assets', 'src', 'locales', 'data'):
            shutil.copytree(ROOT / name, self.root / name)
        shutil.copy(ROOT / 'build.py', self.root / 'build.py')
        self.data = json.loads((self.root / 'data/events.json').read_text())
        self.config = json.loads((ROOT / 'site.config.json').read_text())

    def build(self, success=True):
        (self.root / 'site.config.json').write_text(json.dumps(self.config))
        (self.root / 'data/events.json').write_text(json.dumps(self.data))
        result = subprocess.run([sys.executable, 'build.py', '--release'], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode == 0, success, result.stderr + result.stdout)
        return result

    def test_site_contains_two_sourced_feeds_and_history(self):
        self.build()
        page = (self.root / 'public/index.html').read_text()
        self.assertIn('recent resets', page)
        self.assertIn('confirmed on announcement day', page)
        self.assertIn('Resets all propagated', page)
        for provider in ('codex', 'claude'):
            self.assertIn(f'data-provider="{provider}"', page)
            self.assertIn(self.config['providerRepositories'][provider], page)
        self.assertNotIn('data-provider="grok"', page)

    def test_exported_feeds_share_sourced_events(self):
        self.build()
        for provider in ('codex', 'claude'):
            readme = (self.root / f'notifications/{provider}/README.md').read_text()
            self.assertIn('Watch → Custom → Releases', readme)
            self.assertIn('## recent resets', readme)
            exported = json.loads((self.root / f'notifications/{provider}/data/events.json').read_text())
            expected = sorted((event for event in self.data['events'] if event['provider'] == provider), key=lambda event: (event.get('confirmedAt') or event.get('availableAt') or event.get('announcedAt'))['value'][:10], reverse=True)
            self.assertEqual({e['id'] for e in exported['events']}, {e['id'] for e in expected})
            self.assertEqual(exported['provider']['id'], provider)
            self.assertEqual(exported['schemaVersion'], 2)
            self.assertNotIn('grok-reset-alerts', readme)

    def test_unknown_occurrence_does_not_become_exact_reset_delay(self):
        self.build()
        readme = (self.root / 'notifications/codex/README.md').read_text()
        self.assertIn('confirmed on announcement day', readme)
        self.assertNotIn('hours from announcement to reset', readme)

    def test_quote_is_escaped_and_russian_copy_is_translated(self):
        codex = next(e for e in self.data['events'] if e['id'] == 'codex-paid-users-reset-2026-09-26')
        (codex['confirmedAt'] or codex['announcedAt'])['sources'][0]['quote'] = '<script>alert(1)</script>'
        self.config['locale'] = 'ru'
        self.build()
        page = (self.root / 'public/index.html').read_text()
        self.assertIn('&lt;script&gt;', page)
        self.assertNotIn('<script>alert(1)</script>', page)
        self.assertIn('недавние сбросы', page)

    def test_release_requires_both_feed_urls(self):
        del self.config['providerRepositories']['codex']
        result = self.build(success=False)
        self.assertIn('codex', result.stderr + result.stdout)

if __name__ == '__main__':
    unittest.main()
