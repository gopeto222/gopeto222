# Project discovery and attribution

The public inventory was audited on 2026-10-05 from the authenticated `gopeto222` account. The audit enumerated accessible personal, organization, collaborator, public, private and archived repositories, then checked commits authored by `gopeto222` on accessible branches and authored pull requests. The exact source inventory is stored only in an ignored local file. `scripts/discovery.py` can repeat the metadata audit with an authenticated GitHub CLI; it writes only to that ignored file.

The public `data/projects.json` contains 20 records: eight personal repositories (including this profile), eleven AstroByte Development repositories with observed authored commits, and one private repository under another developer's account with 44 observed authored commits. Five accessible AstroByte Development repositories had no observed authored commits or authored pull requests and were excluded. These are **observed** counts, not a claim that every branch or historical identity was accessible. A repository may contain third-party assets, and an initial import commit does not prove original authorship of all imported files. Therefore, organization and collaborative projects are labeled as contributions rather than sole creations.

Private repository slugs, URLs, source text, internal endpoints and customer details do not appear in the public inventory. Descriptive names are used in the project matrix. The five featured systems were selected for technical depth and available documentation; every verified repository remains in the matrix. ServerDeck was not found among accessible repositories, so no ServerDeck project or architecture was invented.

## Language snapshot

`data/languages.json` is a local authenticated audit of source-file touches in authored, non-merge commits on accessible branches. It excludes common generated/vendor paths and does not store source or private repository names. A file changed in two commits counts twice. The metric reflects changed files, **not authored lines, code ownership, proficiency, or whole-repository language volume**. It can overrepresent imports or repeated changes; the chart is labeled accordingly. The public GitHub Actions token cannot read these private repositories, so automation regenerates its visual from the committed snapshot but does not silently present it as live private data.

## Reference comparison

The detailed audit and final comparison are in [reference-audit.md](reference-audit.md). The redesign uses a distinct graphite and cyan visual system, five sourced case studies, a grouped archive of all 20 verified records, an integrated language control, responsive compositions, contribution-aware measurements, and explicit role labels. Generated diagrams are labeled as diagrams. The source audit found no suitable product captures in the selected private repositories or local CodeGuard checkout; no screenshot was invented or taken from another product.
