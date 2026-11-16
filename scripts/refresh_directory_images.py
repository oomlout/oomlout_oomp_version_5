"""Create small previews from full-detail hardware renders, reading sources only.

Requires Pillow. Usage: python scripts/refresh_directory_images.py --repositories C:/gh
"""
import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'oomp_hardware_screw_version_5', 'oomp_hardware_bolt_version_5'}


def refresh(repositories):
    config = json.loads((ROOT / 'data/directory_gallery.json').read_text(encoding='utf-8'))
    evidence = []
    for item in config['parts']:
        if item['repository'] not in ALLOWED:
            raise ValueError('Directory illustrations must come from the hardware catalogues')
        source = repositories / item['repository'] / 'parts' / item['part'] / config['source_image']
        destination = ROOT / 'presentation/images' / item['image']
        with Image.open(source) as original:
            preview = original.convert('RGB')
            preview.thumbnail((config['preview_size'], config['preview_size']), Image.Resampling.LANCZOS)
            preview.save(destination, optimize=True)
            evidence.append({'image': item['image'], 'repository': item['repository'],
                             'source': f"parts/{item['part']}/{config['source_image']}",
                             'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
                             'source_size': list(original.size), 'preview_size': list(preview.size)})
    (ROOT / 'presentation/images/gallery_sources.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repositories', type=Path, default=ROOT.parent)
    refresh(parser.parse_args().repositories)
