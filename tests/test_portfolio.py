import json
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from portfolio.build import generate
from portfolio.readme import render
from portfolio.svg import document, text
from qa import validate_projects, validate_readmes, validate_svg
from theme import BACKGROUND_0, TEXT_PRIMARY, TEXT_SECONDARY


def contrast(a, b):
    def luminance(value):
        channels=[int(value[i:i+2],16)/255 for i in (1,3,5)]
        linear=[c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4 for c in channels]
        return .2126*linear[0]+.7152*linear[1]+.0722*linear[2]
    x,y=sorted((luminance(a),luminance(b)),reverse=True)
    return (x+.05)/(y+.05)


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory=json.loads((ROOT/'data/projects.json').read_text())
        cls.profile=json.loads((ROOT/'data/profile.json').read_text())
        cls.visuals=json.loads((ROOT/'data/visuals.json').read_text())

    def test_project_model_and_authorship(self):
        validate_projects(self.inventory,self.profile,self.visuals)
        self.assertEqual(len(self.inventory['projects']),20)
        self.assertEqual(sum(p['ownership']=='organization' for p in self.inventory['projects']),11)

    def test_rejects_unverified_and_private_urls(self):
        original=self.inventory['projects'][0]
        bad=dict(original,repositoryUrl='https://github.com/example/private')
        data=dict(self.inventory,projects=[bad,*self.inventory['projects'][1:]])
        with self.assertRaisesRegex(ValueError,'Private URL'):
            validate_projects(data,self.profile,self.visuals)
        bad=dict(original,verified=False)
        data=dict(self.inventory,projects=[bad,*self.inventory['projects'][1:]])
        with self.assertRaisesRegex(ValueError,'Unverified'):
            validate_projects(data,self.profile,self.visuals)

    def test_unknown_featured_reference(self):
        profile=json.loads(json.dumps(self.profile))
        profile['caseStudies']['codeguard']['projectId']='missing'
        with self.assertRaisesRegex(ValueError,'Featured'):
            validate_projects(self.inventory,profile,self.visuals)

    def test_svg_escaping_and_unicode(self):
        svg=document(300,100,'Тест & <safe>','A "quote" & more',
                     text(20,40,'Български & <Rust>',20),BACKGROUND_0)
        ET.fromstring(svg)
        self.assertIn('Български &amp; &lt;Rust&gt;',svg)
        self.assertIn('Тест &amp; &lt;safe&gt;',svg)

    def test_svg_rejects_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'bad.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><title>x</title><desc>x</desc><g id="a"/><g id="a"/></svg>')
            with self.assertRaisesRegex(ValueError,'duplicate SVG ID'):
                validate_svg(path)

    def test_readme_parity_and_asset_references(self):
        refs=validate_readmes()
        self.assertGreater(len(refs),100)
        en=render('en',self.profile,self.inventory)
        bg=render('bg',self.profile,self.inventory)
        self.assertEqual(en,(ROOT/'README.md').read_text())
        self.assertEqual(bg,(ROOT/'README.bg.md').read_text())
        self.assertEqual(en.count('<details>'),bg.count('<details>'))

    def test_generated_output_is_deterministic(self):
        first={path.name:path.read_bytes() for path in generate()}
        second={path.name:path.read_bytes() for path in generate()}
        self.assertEqual(first,second)

    def test_all_svg_text_starts_inside_viewbox(self):
        for path in (ROOT/'assets/generated').glob('*.svg'):
            root=ET.parse(path).getroot()
            _,_,width,height=[float(x) for x in root.attrib['viewBox'].split()]
            for node in root.iter('{http://www.w3.org/2000/svg}text'):
                self.assertGreaterEqual(float(node.attrib['x']),0,path.name)
                self.assertLessEqual(float(node.attrib['x']),width,path.name)
                self.assertGreaterEqual(float(node.attrib['y']),0,path.name)
                self.assertLessEqual(float(node.attrib['y']),height,path.name)

    def test_core_text_contrast(self):
        self.assertGreaterEqual(contrast(TEXT_PRIMARY,BACKGROUND_0),7)
        self.assertGreaterEqual(contrast(TEXT_SECONDARY,BACKGROUND_0),4.5)

    def test_no_unverified_technologies_in_map(self):
        observed={t for p in self.inventory['projects'] for t in p['technologies']}
        svg=(ROOT/'assets/generated/technology-en.svg').read_text()
        for technology in ('Swift','SwiftUI','ServerDeck','Gemini','Ollama'):
            if technology not in observed:
                self.assertNotIn('>'+technology+'<',svg)


if __name__=='__main__':
    unittest.main()
