"""Install the shared renderer in an explicitly selected local catalogue.

Usage: python scripts/install_documentation.py C:/gh/oomp_mechanical_version_5
Existing root README is preserved once as README_GENERATOR.md. No commit or push.
"""
import argparse
import ast
import json
from pathlib import Path
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_directory import DESCRIPTIONS, ROOT


def install(project):
    project = Path(project).resolve()
    if project == ROOT or project.name not in DESCRIPTIONS:
        raise ValueError('Select a known downstream OOMP version 5 repository')
    if not (project / '.git').exists():
        raise ValueError('Expected an existing Git checkout')
    guide = project / 'README_GENERATOR.md'
    if not guide.exists():
        old = (project / 'README.md').read_text(encoding='utf-8') if (project / 'README.md').exists() else ''
        guide.write_text('# Generator and maintenance guide\n\nRun `python action_documentation.py` after generating the catalogue to refresh its documentation. Requires Python and PyYAML. Edit `documentation.json` for the public introduction.\n\n[OOMP documentation standard](https://github.com/oomlout/oomlout_oomp_version_5/blob/main/presentation/README.md)\n\n' + old, encoding='utf-8')
    label, summary = DESCRIPTIONS[project.name]
    config_path = project / 'documentation.json'
    if not config_path.exists():
        config = {'title': 'OOMP ' + label.lower(), 'summary': summary,
                  'part_pages': not project.name.endswith(('_only_yaml', '_pretty'))}
        if project.name.endswith('_only_yaml'):
            config['summary'] = 'A lightweight catalogue of part metadata and preview thumbnails. Use the full source repository for models, drawings and generation code.'
            config['source_repository'] = 'https://github.com/oomlout/' + project.name.removesuffix('_only_yaml')
        if project.name.endswith('_pretty'):
            config['browse'] = 'catalogue/'
            config['source_repository'] = 'https://github.com/oomlout/oomp_electronic_version_5'
        if project.name == 'oomp_bearing_version_5':
            config['summary'] = 'A developing catalogue for bearing records and associated CAD assets. No generated part records are present in this checkout yet.'
        config_path.write_text(json.dumps(config, indent=2) + '\n', encoding='utf-8')
    shutil.copyfile(ROOT / 'oomp_documentation.py', project / 'oomp_documentation.py')
    (project / 'action_documentation.py').write_text('"""Refresh documentation from existing assets without rebuilding parts."""\nfrom pathlib import Path\nfrom oomp_documentation import generate\n\ndef main(**kwargs):\n    return generate(Path(__file__).resolve().parent)\n\nif __name__ == "__main__":\n    print(main())\n', encoding='utf-8')
    working = project / 'working.py'
    if working.exists():
        source = working.read_text(encoding='utf-8')
        run = next((node for node in ast.parse(source).body if isinstance(node, ast.FunctionDef) and node.name == 'run'), None)
        if run and 'action_documentation.main(' not in source:
            lines = source.splitlines(keepends=True)
            lines.insert(run.end_lineno, '\n    # Refresh documentation after the existing asset pipeline.\n    if kwargs.get("run_documentation", True):\n        import action_documentation\n        action_documentation.main()\n')
            working.write_text(''.join(lines), encoding='utf-8', newline='\n')
    for filename, needle, destination in (
        ('working_only_yaml.py', '    return result\n', 'output'),
        ('generate_pretty_repository.py', '    return stats\n', 'output_root'),
    ):
        exporter = project / filename
        if not exporter.exists():
            continue
        source = exporter.read_text(encoding='utf-8')
        if 'from oomp_documentation import generate' in source:
            continue
        if source.count(needle) != 1:
            raise ValueError(f'Inspect the changed exporter before installing: {exporter}')
        hook = (f'    # Refresh installed export documentation after publishing assets.\n'
                f'    if ({destination} / "documentation.json").is_file():\n'
                f'        from oomp_documentation import generate as generate_documentation\n'
                f'        generate_documentation({destination})\n')
        exporter.write_text(source.replace(needle, hook + needle), encoding='utf-8', newline='\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    install(parser.parse_args().project)
