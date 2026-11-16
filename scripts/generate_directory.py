"""Build the public directory from the verified repository inventory."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESCRIPTIONS = {
    'oomlout_oomp_version_5': ('OOMP core', 'Shared identifiers, metadata and documentation utilities; this directory.'),
    'oomp_bearing_version_5': ('Bearings', 'Bearing catalogue project; GitHub reports 0 KiB and no root README was available at audit time.'),
    'oomp_mechanical_version_5': ('Mechanical parts', 'Shaft couplers, magnets and timing pulleys with models and drawings.'),
    'oomp_electronic_version_5': ('Electronic components', 'Component records, package drawings, KiCad assets and source metadata.'),
    'oomp_electronic_breakout_version_5': ('Electronic breakouts', 'Breakout boards, pin layouts and mounting geometry.'),
    'oomp_electronic_project_version_5': ('Electronic projects', 'Board projects, component matching, interactive explorers and production outputs.'),
    'oomp_hardware_bolt_version_5': ('Bolts, nuts and washers', 'Hardware variants, dimensional drawings, models and supplier records.'),
    'oomp_hardware_screw_version_5': ('Screws', 'Screw families and sizes, drawings and generated models.'),
    'oomp_electrical_extension_lead_uk_socket_6_outlet_pro_elec_2068_version_5': ('UK six-outlet extension lead', 'Pro Elec 2068 extension-lead records and associated assets.'),
    'oomp_electronic_verison_5_pretty': ('Electronics visual browser', 'A compact, illustrated electronics catalogue. The published name spells version as verison.'),
    'oomp_electronic_version_5_only_yaml': ('Electronics YAML export', 'Lightweight metadata and thumbnails; GitHub reports 0 KiB and no root README was available at audit time.'),
    'oomp_hardware_bolt_version_5_only_yaml': ('Bolts YAML export', 'Lightweight hardware metadata and thumbnails.'),
    'oomp_hardware_screw_version_5_only_yaml': ('Screws YAML export', 'Lightweight screw metadata and thumbnails.'),
}


def generate():
    inventory = json.loads((ROOT / 'data/repositories.json').read_text(encoding='utf-8'))
    rows = inventory['repositories']
    gallery = json.loads((ROOT / 'data/directory_gallery.json').read_text(encoding='utf-8'))['parts']
    gallery_names = []
    gallery_images = []
    for item in gallery:
        url = f'https://github.com/oomlout/{item["repository"]}/tree/main/parts/{item["part"]}/'
        image = f'presentation/images/{item["image"]}'
        gallery_names.append(f'[{item["label"]}]({url})')
        gallery_images.append(f'[![Full-detail CAD render: {item["detail"]}]({image})]({image})')
    lines = ['# OOMP version 5', '', '## Summary', '',
             'OOMP is a collection of reusable part records for electronics, hardware and mechanical projects. Each catalogue brings together part identifiers, structured metadata and available drawings, models or reference files. Start here to find the right repository, then choose an exact part in its catalogue.', '',
             '| ' + ' | '.join(gallery_names) + ' |',
             '| ' + ' | '.join(['---'] * len(gallery)) + ' |',
             '| ' + ' | '.join(gallery_images) + ' |', '',
             'Full-detail catalogue renders, reduced for this page. The two M3 screws are 10 mm long; the set screw is M6 × 25 mm with a fully threaded hex head. Click a name for its part record or an image for a larger preview. Illustrations are not to a common scale.', '',
             '## Details', '', 'Choose a full catalogue for source data and available assets, the visual browser for quick discovery, or a YAML export for lightweight data use. Files and completeness vary by repository.', '',
             f'Repositories checked on {inventory["checked"]}. The list includes GitHub projects absent from this computer and preserves their published names.', '']
    lines += ['Repositories are sorted by their full repository name/code. Lightweight `_only_yaml` exports sit beside their source catalogue.', '']
    for row in sorted(rows, key=lambda r: r['name'].casefold()):
        label, description = DESCRIPTIONS[row['name']]
        lines += [f'- [{row["name"]}]({row["url"]}) — **{label}.** {description}', '']
    lines += ['## Using the catalogues', '',
              '1. Open the repository for the component family you need.',
              '2. Follow its catalogue or `parts/` folders to the exact variant.',
              '3. Check the full OOMP ID and source metadata before using its available files. Model formats, drawings and supplier references vary by part.', '',
              'For local setup and modifications, see the [generator guide](README_GENERATOR.md). Maintainers can use the [documentation standard and repository audit](presentation/README.md).']
    (ROOT / 'README.md').write_text('\n'.join(lines) + '\n', encoding='utf-8', newline='\n')
    # A YAML sequence remains machine-readable as the inventory grows.
    (ROOT / 'data/oomp_repo_list.yaml').write_text('\n'.join('- ' + row['url'] for row in sorted(rows, key=lambda r: r['name'])) + '\n', encoding='utf-8', newline='\n')


if __name__ == '__main__':
    generate()
