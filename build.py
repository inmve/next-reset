#!/usr/bin/env python3
"""Build the static website and the separate, README-only repository draft."""
from pathlib import Path
from datetime import datetime, timezone
from html import escape
from urllib.parse import urlparse
import json
import hashlib
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'public'
config = json.loads((ROOT / 'site.config.json').read_text())
data = json.loads((ROOT / 'data/events.json').read_text())
strings = json.loads((ROOT / f"locales/{config['locale']}.json").read_text())
now = datetime.now(timezone.utc)
today = now.date().isoformat()
design = int(config['design'])
pelican_design = int(config.get('pelicanDesign', design))
if design not in range(1, 6):
    raise ValueError('Design must be between 1 and 5')
if pelican_design not in range(1, 6):
    raise ValueError('Pelican design must be between 1 and 5')
def t(key, **values):
    return strings[key].format(**values)
def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))
def date_label(value):
    date = timestamp(value if 'T' in value else value + 'T12:00:00Z')
    return date.strftime('%B ') + str(date.day) + (f', {date.year}' if date.year != now.year else '')
def url(value, github=False):
    parsed = urlparse(value)
    if parsed.scheme != 'https' or not parsed.netloc or parsed.username or parsed.password:
        raise ValueError(f'Expected a public HTTPS URL: {value}')
    if github and (parsed.netloc != 'github.com' or len(parsed.path.strip('/').split('/')) != 2):
        raise ValueError('Repository links must point to an owner/repository on github.com')
    return escape(value, quote=True)
for key in ('updatesRepository', 'sourceRepository', 'siteUrl'):
    if config.get(key): url(config[key], github=key != 'siteUrl')
missing = [key for key in ('updatesRepository', 'sourceRepository', 'siteUrl') if not config.get(key)]
if '--release' in sys.argv and missing:
    raise SystemExit('Public addresses still needed: ' + ', '.join(missing))
OUT.mkdir(exist_ok=True)
cards, records, rows, active = [], [], [], []
for provider in data['providers']:
    events = sorted((event for event in data['events'] if event['provider'] == provider['id']), key=lambda event: timestamp(event['announcedAt']), reverse=True)
    if not events: raise ValueError('Missing provider events')
    event = events[0]
    if event['status'] not in ('announced', 'confirmed_completed', 'banked_available'): raise ValueError('Unsupported event status')
    banked = event['status'] == 'banked_available'
    announced = event['status'] == 'announced'
    riding = announced or banked
    expected = event.get('expectedDate')
    overdue = announced and expected and expected < today
    source = url(event['source'])
    confirmation = timestamp(event['announcedAt'])
    age = max(0, (now - confirmation).days)
    q = min(age / 30, 1)
    red = f'rgb({round(196 - 96*q)},{round(76 - 47*q)},{round(77 - 35*q)})'
    if banked:
        label = t('bankedReset')
        shown_date = t('bankedReset')
        scope = t('bankedDetails', date=date_label(event['announcedAt']))
        row_state = 'banked reset available · use when you choose'
    elif announced:
        label = t('confirmationPending' if overdue else 'announcedForToday' if expected == today else 'announced')
        shown_date = date_label(expected) if expected else t('dateUnknown')
        scope = t('awaitingScope' if overdue else 'todayTimeUnknown' if expected == today else 'expectedTimeUnknown')
        row_state = f"reset expected **{expected}**" if expected else 'reset announced · date not specified'
        if overdue: row_state += ' · confirmation pending'
        else: active.append(provider['name'])
    else:
        label = t('lastConfirmed')
        shown_date = date_label(event['announcedAt'])
        scope = t('daysSince', days=age)
        if event.get('scopeLabelKey'): scope += ' | ' + t(event['scopeLabelKey'])
        row_state = f"last confirmed reset **{confirmation.date().isoformat()}**"
        if event.get('scopeLabelKey'): row_state += ' · ' + t(event['scopeLabelKey'])
    pose = 'cycling' if riding else provider['pose']
    svg = (ROOT / f'assets/pelicans/pelican-{pelican_design:02}-{pose}.svg').read_text()
    svg = re.sub(r'(<title[^>]*>).*?(</title>)', lambda match:match[1]+escape(t(pose+'Title'))+match[2], svg)
    svg = re.sub(r'(<desc[^>]*>).*?(</desc>)', lambda match:match[1]+escape(t(pose+'Description'))+match[2], svg)
    readme_illustration = ''
    if config.get('siteUrl'):
        root_tag = re.match(r'<svg\b[^>]*>', svg).group()
        inner_svg = re.sub(r'^<svg\b[^>]*>|</svg>\s*$', '', svg)
        metadata = ''.join(re.findall(r'<(?:title|desc)\b[^>]*>.*?</(?:title|desc)>', inner_svg))
        art = re.sub(r'<(?:title|desc)\b[^>]*>.*?</(?:title|desc)>', '', inner_svg)
        still_art = re.sub(r'<animate(?:Transform|Motion)?\b[^>]*/>', '', art)
        background = '<rect width="320" height="240" rx="12" fill="#f5f6f0"/>'
        if riding:
            motion_style = '<style>.readme-still{display:none}@media(prefers-reduced-motion:reduce){.readme-motion{display:none}.readme-still{display:inline}}</style>'
            readme_art = motion_style + '<g class="readme-motion">' + art + '</g><g class="readme-still">' + still_art + '</g>'
        else:
            readme_art = still_art
        readme_svg = root_tag + metadata + background + readme_art + '</svg>'
        readme_svg = '\n'.join(line.rstrip() for line in readme_svg.splitlines()) + '\n'
        image_path = f'readme/{provider["id"]}.svg'
        (OUT / 'readme').mkdir(exist_ok=True)
        (OUT / image_path).write_text(readme_svg)
        image_version = hashlib.sha256(readme_svg.encode()).hexdigest()[:12]
        image_url = url(config['siteUrl'].rstrip('/') + '/' + image_path + '?v=' + image_version)
        caption = escape(t('enjoyTheRide' if riding else 'waitingNote'))
        readme_illustration = f'\n\n<p><img src="{image_url}" width="180" height="135" alt="{escape(t(pose+"Title"), quote=True)}"><br><em>{caption}</em></p>'
    # Static first paint; only the announced bicycle starts moving after motion preferences are read.
    if riding: svg = svg.replace('repeatCount="indefinite"', 'repeatCount="indefinite" begin="indefinite"')
    svg = re.sub(r'([pmcb]0[1-5])-', rf'\1-{provider["id"]}-', svg)
    for before, after in {'#263e39':'var(--bird-ink)', '#98b3a0':'var(--bird-sage)', '#d89958':'var(--bird-gold)', '#f3efe2':'var(--bird-cream)'}.items(): svg = svg.replace(before, after)
    source_text = t('sourceOn', date=date_label(event['announcedAt'])) if event.get('announcementPrecision') == 'day' else t('sourceAt', date=confirmation.strftime('%b %d, %H:%M'))
    note = ('<p class="banked-help">' + escape(t('bankedDate')) + '</p>' if banked else '') + '<p class="pelican-note">' + escape(t('enjoyTheRide' if riding else 'waitingNote')) + '</p>'
    cards.append(f'''<article class="provider {'announced' if riding else 'waiting'}" data-provider="{provider['id']}" style="--wait:{red}">
<div class="provider-details"><h2 class="provider-name">{escape(provider['name'])}<span>{escape(provider['company'])}</span></h2>
<p class="scope">{escape(scope)}</p><p class="when">{escape(shown_date)}</p>
<a class="source" href="{source}" target="_blank" rel="noopener noreferrer">{escape(source_text)}</a></div>
<div class="bird-stage"><div class="bird">{svg}</div></div>{note}</article>''')
    records.append({**provider, 'announced':announced, 'banked':banked, 'expectedDate':expected, 'confirmedAt':event['announcedAt'], 'source':event['source'], 'scopeLabelKey':event.get('scopeLabelKey'), 'author':event.get('author', provider['company'])})
    if not banked: rows.append(f"## {provider['name']} / {provider['company']}\n\n{row_state[0].upper() + row_state[1:]} · [announcement]({event['source']})")
today_plans = [record for record in records if record['announced'] and record['expectedDate'] == today]
dated_plans = sorted((record for record in records if record['announced'] and record['expectedDate'] and record['expectedDate'] > today), key=lambda record:record['expectedDate'])
undated_plans = [record for record in records if record['announced'] and not record['expectedDate']]
completed_today = [record['name'] for record in records if not record['announced'] and not record['banked'] and timestamp(record['confirmedAt']).date().isoformat() == today]
if today_plans:
    heading = t('plannedToday' if len(today_plans) == 1 else 'plannedTodayPlural', providers=', '.join(record['name'] for record in today_plans))
elif completed_today:
    heading = t('completedToday', providers=', '.join(completed_today))
elif dated_plans:
    next_date = dated_plans[0]['expectedDate']
    next_plans = [record for record in dated_plans if record['expectedDate'] == next_date]
    heading = t('plannedForDate' if len(next_plans) == 1 else 'plannedForDatePlural', providers=', '.join(record['name'] for record in next_plans), when=date_label(next_date))
elif undated_plans:
    heading = t('plannedUndated' if len(undated_plans) == 1 else 'plannedUndatedPlural', providers=', '.join(record['name'] for record in undated_plans))
else:
    heading = t('noResetsToday')
proof_record = (today_plans or [record for record in records if record['name'] in completed_today] or dated_plans or undated_plans or [None])[0]
proof_text = t('basedOnPost', author=proof_record['author'], date=timestamp(proof_record['confirmedAt']).strftime('%b %d, %H:%M')) if proof_record else ''
values = {key:escape(value) for key,value in strings.items()}
values.update({
    'nextResetQuestion':escape(t('nextResetQuestion')).replace(escape(t('nextResetTerm')), '<mark>'+escape(t('nextResetTerm'))+'</mark>'),
    'lang':config['locale'], 'design':str(design), 'brand':escape(config['name']),
    'styleVersion':hashlib.sha256((ROOT/'src/style.css').read_bytes()).hexdigest()[:12],
    'scriptVersion':hashlib.sha256((ROOT/'src/site.js').read_bytes()).hexdigest()[:12],
    'pageTitle':escape(t('statusPageTitle', status=t('siteTitle'), date=today)),
    'homeLabel':escape(t('homeLabel', name=config['name'])),
    'heading':'<br>'.join(escape(line) for line in heading.split('|')),
    'proofText':escape(proof_text), 'proofUrl':url(proof_record['source']) if proof_record else '#providers',
    'proofHidden':'' if proof_record else 'hidden', 'noProofHidden':'hidden' if proof_record else '',
    'actionUrl':url(config['updatesRepository'],True) if config.get('updatesRepository') else '#providers',
    'actionLabel':escape(t('githubUpdates' if config.get('updatesRepository') else 'seeUpdates')),
    'cards':'\n'.join(cards), 'navigation':'', 'sourceLink':'', 'subscription':'<p class="subscription-note">'+escape(t('watchHelp'))+'</p>', 'canonical':'',
    'snapshot':escape(t('snapshotLabel', date=timestamp(data['snapshotAt']).strftime('%b %d, %Y · %H:%M'))),
    'state':json.dumps({'strings':strings,'cards':records,'config':config},ensure_ascii=False).replace('<','\\u003c')
})
if config.get('sourceRepository'):
    values['sourceLink'] = f'<a href="{url(config["authorUrl"])}">{escape(t("madeBy", author=config["authorName"]))}</a><a href="{url(config["sourceRepository"].rstrip("/")+"/issues")}">{escape(t("feedback"))}</a>'
if config.get('siteUrl'):
    values['canonical'] = f'<link rel="canonical" href="{url(config["siteUrl"])}"><meta property="og:url" content="{url(config["siteUrl"])}">'
page = re.sub(r'\{\{(\w+)\}\}', lambda match:values[match[1]], (ROOT/'src/page.html').read_text())
(OUT/'index.html').write_text(page)
for file in ('style.css','site.js'): shutil.copy(ROOT/'src'/file, OUT/file)
shutil.copy(ROOT/'data/events.json', OUT/'events.json')
(OUT/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="12" fill="#f6e8da"/><path d="M31 15A13 13 0 1 0 32 24" fill="none" stroke="#344a3c" stroke-width="3" stroke-linecap="round"/></svg>')
readme_title = (', '.join(active) + (' reset is upcoming' if len(active)==1 else ' resets are upcoming')) if active else 'No need to rush'
site_link = f"{t('checkWebsite')} — [{config['name']}]({config['siteUrl']})." if config.get('siteUrl') else f"{t('checkWebsite')} — {t('websiteComingSoon')}."
readme = '# Free AI Coding' + '\n\n## ' + t('notificationsHeading') + '\n\n' + t('resetNotifications') + '\n\n## Limit resets\n\n' + '\n\n'.join(row.replace('## ', '### ', 1) for row in rows) + '\n\n' + site_link + '\n'
(ROOT/'minimal-README.md').write_text(readme)
print('Built public/index.html and minimal-README.md. ' + ('Addresses pending: '+', '.join(missing) if missing else 'All public addresses configured.'))
