"""Build the public directory from the verified repository inventory."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DESCRIPTIONS = {
    'oomp_tool_version_5': (
        'Workshop tools and stationery',
        'Tools used in OOBB part holder v5, with holder layouts, dimension drawings, editable OpenSCAD models and Blender renders of photographed tools.',
    ),
    'oomp_three_d_printer_version_5': ('3D printers and supplies', 'Printer models, filament spools, compatible spares and automatic material systems with OOMP inventory labels and sourced specifications.'),
    'oomp_motor_version_5': ('Motors, pumps and fans', '17 NEMA 17 stepper, N20 and TT gearmotor, JT-500 pump and computer-fan records, with dimensioned drawings, editable SCAD, STL/GLB models and studio renders.'),
    'oomlout_oomp_version_5': ('OOMP core', 'Shared identifiers, metadata and documentation utilities; this directory.'),
    'oomp_bearing_version_5': ('Bearings', '339 single-row, flanged and double-row bearing records with dimensioned A4 drawings, GLB models, studio renders and series navigation.'),
    'oomp_mechanical_version_5': ('Mechanical parts', 'Shaft couplers, magnets and timing pulleys with models and drawings.'),
    'oomp_electronic_version_5': ('Electronic components', 'Component records, package drawings, KiCad assets and source metadata.'),
    'oomp_electronic_breakout_version_5': ('Electronic breakouts', 'Breakout boards, pin layouts and mounting geometry.'),
    'oomp_electronic_project_version_5': ('Electronic projects', 'Board projects, component matching, interactive explorers and production outputs.'),
    'oomp_hardware_bolt_version_5': ('Bolts, nuts and washers', 'Hardware variants, dimensional drawings, models and supplier records.'),
    'oomp_hardware_spacer_standoff_version_5': ('Spacers and standoffs', 'White nylon M3-M6 clearance spacers and M2.5-M6 tapped-to-tapped, stud-to-tapped and stud-to-stud hex standoffs, with dimensioned drawings, editable CAD and Blender studio renders.'),
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
    samples = json.loads((ROOT / 'data/directory_samples.json').read_text(encoding='utf-8'))
    by_name = {row['name']: row for row in rows}
    for row in rows:
        if row.get('parent') and (row['parent'] not in by_name or by_name[row['parent']].get('parent')):
            raise ValueError(f'Variant must name a main repository: {row["name"]}')
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
    if inventory.get('local_additions_note'):
        lines += [inventory['local_additions_note'], '']
    lines += ['Main repositories are sorted by their full repository name/code. Alternative browsers and YAML-only exports are linked beneath their main repository.', '',
              '| Repository | What it provides | Sample |', '| --- | --- | --- |']
    for row in sorted((row for row in rows if not row.get('parent')), key=lambda r: r['name'].casefold()):
        label, description = DESCRIPTIONS[row['name']]
        repository = f'[{row["name"]}]({row["url"]})'
        variants = sorted((variant for variant in rows if variant.get('parent') == row['name']), key=lambda r: r['variant_label'])
        if variants:
            repository += '<br><sub>Variants: ' + ' · '.join(f'[{v["variant_label"]}]({v["url"]})' for v in variants) + '</sub>'
        sample = samples.get(row['name'])
        if sample:
            picture = f'<img src="{escape(sample["image"], quote=True)}" alt="{escape(sample["label"], quote=True)}" width="140">'
            preview = f'[{picture}]({sample["target"]})<br>{sample["label"]}'
            if sample.get('credit'):
                preview += '<br>' + sample['credit']
        else:
            preview = 'No sample published yet.'
        lines.append(f'| {repository} | **{label}.** {description} | {preview} |')
    lines.append('')
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
