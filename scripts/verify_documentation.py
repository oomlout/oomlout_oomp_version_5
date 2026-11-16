"""Check local links in generated OOMP blocks, excluding retained legacy notes."""
import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from oomp_documentation import START, END


def verify(project):
    pages = [project / 'README.md', *(project / 'parts').glob('*/README.md')]
    failures = []
    checked = 0
    for page in pages:
        if not page.is_file():
            continue
        content = page.read_text(encoding='utf-8')
        if START not in content:
            continue
        content = content.split(START, 1)[1].split(END, 1)[0]
        content = re.sub(r'(?ms)^(`{3,})[^\n]*\n.*?^\1\s*$', '', content)
        for target in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in target or target.startswith('#'):
                continue
            checked += 1
            if not (page.parent / unquote(target.split('#', 1)[0])).exists():
                failures.append(f'{page}: {target}')
    return checked, failures


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    checked, failures = verify(parser.parse_args().project)
    print(f'Checked {checked} generated local links; {len(failures)} failures')
    for failure in failures:
        print(failure)
    raise SystemExit(bool(failures))
