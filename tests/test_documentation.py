import json
from pathlib import Path
import tempfile
import unittest
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from install_documentation import install

from oomp_documentation import generate, managed, START


class DocumentationTests(unittest.TestCase):
    def test_install_retains_setup_and_wires_build_once(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / 'oomp_mechanical_version_5'
            root.mkdir()
            (root / '.git').mkdir()
            (root / 'README.md').write_text('Original setup instructions.')
            (root / 'working.py').write_text('def run(**kwargs):\n    print("assets")\n\nif __name__ == "__main__":\n    run()\n')
            install(root)
            install(root)
            self.assertIn('Original setup instructions.', (root / 'README_GENERATOR.md').read_text())
            self.assertEqual(1, (root / 'working.py').read_text().count('action_documentation.main()'))
            compile((root / 'working.py').read_text(), 'working.py', 'exec')

    def test_generation_preserves_notes_and_is_repeatable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'documentation.json').write_text(json.dumps({'title': 'Test', 'summary': 'Test parts.'}))
            part = root / 'parts' / 'test_part'
            part.mkdir(parents=True)
            (part / 'working.yaml').write_text('name: "A | B"\ntaxonomy_1: hardware\nnotes: "```"\n')
            (part / 'README.md').write_text('Hand-written [notes](working.yaml).\n')
            generate(root)
            first = (part / 'README.md').read_bytes()
            generate(root)
            self.assertEqual(first, (part / 'README.md').read_bytes())
            rendered = first.decode()
            self.assertIn('A &#124; B', rendered)
            self.assertIn('````yaml', rendered)
            self.assertIn('Hand-written [notes](working.yaml).', rendered)
            self.assertNotIn('![', rendered)

    def test_mirror_does_not_add_part_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'documentation.json').write_text(json.dumps({'title': 'Mirror', 'summary': 'Metadata.', 'part_pages': False}))
            part = root / 'parts' / 'test_part'
            part.mkdir(parents=True)
            (part / 'working.yaml').write_text('id: test_part\n')
            generate(root)
            self.assertEqual(['working.yaml'], [p.name for p in part.iterdir()])

    def test_broken_markers_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'README.md'
            path.write_text(START)
            with self.assertRaises(ValueError):
                managed(path, 'replacement')
            self.assertEqual(START, path.read_text())


if __name__ == '__main__':
    unittest.main()
