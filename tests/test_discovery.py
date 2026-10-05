import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from discovery import contribution_evidence, public_record_is_safe  # noqa: E402
from language_audit import aggregate_file_touches, language_for_path  # noqa: E402
from visuals import generate, languages_visual, matrix  # noqa: E402


class DiscoveryTests(unittest.TestCase):
    def test_ownership_and_contribution_filter(self):
        self.assertTrue(contribution_evidence('gopeto222',0,0))
        self.assertTrue(contribution_evidence('AstroByte-Development',1,0))
        self.assertTrue(contribution_evidence('other',0,1))
        self.assertFalse(contribution_evidence('AstroByte-Development',0,0))

    def test_private_record_cannot_publish_url(self):
        self.assertFalse(public_record_is_safe({'visibility':'private','repository':'owner/private'}))
        self.assertTrue(public_record_is_safe({'visibility':'private','repository':None}))

    def test_inventory_and_svg(self):
        data=json.loads((ROOT/'data/projects.json').read_text())
        projects=data['projects']
        self.assertEqual(len(projects),20)
        self.assertEqual(len({p['id'] for p in projects}),20)
        self.assertTrue(all(public_record_is_safe(p) for p in projects))
        self.assertEqual(matrix(projects,'en',True).count('class="missing"'),0)
        self.assertEqual(len(generate(projects)),78)

    def test_language_snapshot(self):
        data=json.loads((ROOT/'data/languages.json').read_text())
        self.assertGreater(data['commitsAnalyzed'],0)
        self.assertIn('Lua',data['languages'])
        self.assertIn('source-file touches',data['measurement'].lower())
        self.assertIn('LUA',languages_visual(data,'en',False))

    def test_language_aggregation_uses_authored_file_touches(self):
        commits=[
            {'parents':[{}], 'files':[{'filename':'src/a.lua'},{'filename':'src/b.ts'},{'filename':'vendor/c.lua'}]},
            {'parents':[{}], 'files':[{'filename':'src/a.lua'}]},
            {'parents':[{},{}], 'files':[{'filename':'src/merged.py'}]},
        ]
        self.assertEqual(aggregate_file_touches(commits),{'Lua':2,'TypeScript':1})
        self.assertIsNone(language_for_path('node_modules/x.js'))


if __name__=='__main__':unittest.main()
