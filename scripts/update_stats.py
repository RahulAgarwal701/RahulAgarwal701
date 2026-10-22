"""Cache original anuraghazra/github-readme-stats cards; retain last good cards on failure."""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import os
import sys
import xml.etree.ElementTree as ET

OWNER = os.environ.get('PROFILE_USERNAME', 'RahulAgarwal701')
BASE = 'https://github-readme-stats.vercel.app/api'
COMMON = {
    'username': OWNER, 'bg_color': '0B111B', 'title_color': '8FE6CA',
    'text_color': '9BAFC5', 'icon_color': '9CC8FF', 'border_color': '26374B',
    'border_radius': '14', 'disable_animations': 'true',
}
CARDS = {
    'stats.svg': ('', {'show_icons': 'true', 'hide_rank': 'true', 'card_width': '495'}),
    'languages.svg': ('/top-langs/', {'layout': 'compact', 'langs_count': '6', 'card_width': '495'}),
}

def validate_card(data):
    if len(data) > 2_000_000:
        raise ValueError('Unexpected card size')
    root = ET.fromstring(data)
    if root.tag != '{http://www.w3.org/2000/svg}svg':
        raise ValueError('Response is not SVG')
    content = ' '.join(root.itertext()).lower()
    if any(s in content for s in ['something went wrong', 'rate limit', 'could not resolve', 'bad credentials', 'maximum retries', 'user not found', 'error fetching', 'no languages data']):
        raise ValueError('Provider returned an error card')
    if any(node.tag.rsplit('}',1)[-1] in ('script','foreignObject') for node in root.iter()):
        raise ValueError('Unexpected active SVG content')

def main():
    failed = False
    directory = Path('profile')
    directory.mkdir(exist_ok=True)
    for name, (endpoint, extra) in CARDS.items():
        try:
            url = BASE + endpoint + '?' + urlencode(COMMON | extra)
            req = Request(url, headers={'User-Agent': 'Rahul-profile-stats'})
            with urlopen(req, timeout=45) as response:
                data = response.read(2_000_001)
            validate_card(data)
            target = directory / name
            temporary = target.with_suffix('.tmp')
            temporary.write_bytes(data)
            temporary.replace(target)
            print(f'Updated {name}')
        except Exception as exc:
            failed = True
            print(f'::warning::{name}: {exc}; kept the existing card.')
    return 1 if failed else 0

if __name__ == '__main__':
    sys.exit(main())
