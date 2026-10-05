# Maintaining the profile

The two READMEs and the SVG assets in `assets/generated/` are generated. Edit the source data and Python components, then rebuild both languages together.

## Sources

- `data/profile.json`: bilingual case-study copy, featured order, contact destination.
- `data/projects.json`: the public, verified project inventory and attribution. Private source URLs and repository slugs must never be added here.
- `data/visuals.json`: visual manifest. A screenshot entry requires a real, reviewed capture, its source project, a descriptive alt, and a safe public asset path. Diagrams are identified separately.
- `data/languages.json`: dated, contribution-aware file-touch snapshot. See [discovery.md](discovery.md) for its limits.
- `data/activity.json`: public GitHub contribution calendar, refreshed by the scheduled workflow.
- `scripts/theme.py`: color and typography tokens; `scripts/portfolio/`: composition modules.

## Rebuild and check

```sh
python3 scripts/visuals.py
python3 scripts/build_readmes.py
python3 scripts/metrics.py --validate
python3 -m unittest discover -s tests -v
python3 scripts/qa.py
```

`scripts/discovery.py` refreshes only an ignored local audit file using authenticated GitHub CLI access. Review its evidence before changing public records. The scheduled GitHub Action refreshes public activity only; its token cannot validate private project authorship or update the language snapshot.

GitHub renders profile README Markdown with restricted HTML and static SVG images. The language control therefore links between `README.md` and `README.bg.md`; it does not rely on JavaScript. Desktop and mobile images are delivered with `<picture>` and media queries. All generated SVGs have text alternatives and avoid external fonts, scripts, and animations.

Before publishing new screenshots, inspect every pixel and metadata for private data, user information, endpoints, credentials, and third-party branding. Document the capture and verify the asset is actually from the featured project. If no safe capture exists, use a labeled diagram.
