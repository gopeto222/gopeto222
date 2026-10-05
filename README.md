<p align="right"><strong>EN</strong> · <a href="README.bg.md">БГ</a></p>

<picture><source media="(max-width: 650px)" srcset="assets/generated/hero-en-mobile.svg"><img src="assets/generated/hero-en.svg" alt="Georgi Kanchev — software engineer building developer tools, FiveM systems and web platforms" width="100%"></picture>

<p align="center"><a href="#command-center">Command center</a> · <a href="#featured-systems">Featured systems</a> · <a href="#all-projects">All projects</a> · <a href="#architecture">Architecture</a> · <a href="#activity">Activity</a> · <a href="#contact">Contact</a></p>

<a id="command-center"></a>
<img src="assets/generated/section-02-en.svg" alt="02 — Developer command center" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/command-en-mobile.svg"><img src="assets/generated/command-en.svg" alt="Current focus, core languages and engineering priorities" width="100%"></picture>

I work across local developer tooling, FiveM server resources, and web administration. The technologies below are grounded in inspected repositories; the project inventory distinguishes personal work from collaborative contributions.

<a id="featured-systems"></a>
<img src="assets/generated/section-03-en.svg" alt="03 — Featured systems" width="100%">

### AstroByte CodeGuard · local code intelligence

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-codeguard-en-mobile.svg"><img src="assets/generated/feature-codeguard-en.svg" alt="CodeGuard scanner dashboard showing analysis, findings, AI fix review and safe revert" width="100%"></picture>

**Problem → solution.** Code findings need evidence and fixes need a controlled review path. CodeGuard combines a Rust scanner and CLI with a macOS Tauri 2 / React desktop app. It presents source context and findings, then optionally requests a proposal from OpenAI or Anthropic. The app shows a diff, requires explicit approval, verifies the result, and keeps guarded fix history.

**My contribution:** personal repository with authored activity. **Engineering decisions:** local scanning, bounded and redacted AI context, credential storage in macOS Keychain, project-scoped source access, and conflict-aware revert are documented in the repository. **Status:** private development; no public source or release link.

### Rules administration platform · full-stack product

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-rules-en-mobile.svg"><img src="assets/generated/feature-rules-en.svg" alt="Rules platform dashboard showing draft publishing, access control, revisions and audit logging" width="100%"></picture>

**Problem → solution.** Server rules need a public reading experience and a controlled editorial workflow. The private personal project uses Next.js, React, TypeScript, PostgreSQL and Prisma. Its repository documents Discord OAuth administration, drafts and publishing, revision history, server-side access checks, and an audit log.

**My contribution:** personal repository with authored commits. **Status:** private; no demo is claimed.

### DMV tablet · FiveM workflow

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-dmv-en-mobile.svg"><img src="assets/generated/feature-dmv-en.svg" alt="DMV system dashboard showing registration, plate history, verification and localization" width="100%"></picture>

**Project:** a private AstroByte Development Qbox resource with a FiveM NUI tablet, Lua client/server code, vehicle registration records and MySQL persistence. Its README documents registration, plate history, QR verification, and localization.

**My contribution:** authored commits are present, including a release change. This is an **organization project**; the full system is not attributed to me alone. **Status:** private source.

### Business registry · FiveM records

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-registry-en-mobile.svg"><img src="assets/generated/feature-registry-en.svg" alt="Business registry dashboard showing records, documents, server validation and activity logging" width="100%"></picture>

**Project:** a private AstroByte Development Qbox resource for business records and documents. The repository README describes server-side validation, MySQL activity logs, localization and a tablet interface.

**My contribution:** an authored initial repository commit is visible. It establishes contribution, not sole ownership of every later change. **Status:** private source.

### Collaborative FiveM server infrastructure

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-collaboration-en-mobile.svg"><img src="assets/generated/feature-collaboration-en.svg" alt="Collaborative FiveM infrastructure dashboard showing shared resource and database work" width="100%"></picture>

**Project:** a shared private FiveM repository under another developer's account. **My contribution:** 44 authored commits were observed on accessible branches during the audit, including a database change. This is a **collaborative project**; the visual describes the shared system and does not claim its full implementation as mine. **Status:** private source.

<a id="all-projects"></a>
<img src="assets/generated/section-04-en.svg" alt="04 — All projects" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/matrix-en-mobile.svg"><img src="assets/generated/matrix-en.svg" alt="Matrix of 20 verified personal and collaborative project records, with category, stack, role and visibility" width="100%"></picture>

The matrix is generated from [the public-safe project inventory](data/projects.json). It includes all 20 accessible repositories with personal ownership or observed authored contributions, including this profile. Five additional organization repositories were reviewed and excluded because no authored contribution was established. Private entries use descriptive labels and omit repository URLs. A commit proves an authored change; it does not prove sole authorship of the project. [Discovery method and limits](docs/discovery.md).

<a id="how-i-build"></a>
<img src="assets/generated/section-05-en.svg" alt="05 — How I build" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/engineering-en-mobile.svg"><img src="assets/generated/engineering-en.svg" alt="Engineering principles covering security, performance, architecture and delivery" width="100%"></picture>

The strongest evidence is in the systems themselves: CodeGuard's explicit diff review and guarded revert; the rules platform's server-side access control, revision history and audit log; and the Qbox registry's server validation. These are project-specific decisions, not a claim that every repository implements the same safeguards.

<a id="technology"></a>
<img src="assets/generated/section-06-en.svg" alt="06 — Technology" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/technology-en-mobile.svg"><img src="assets/generated/technology-en.svg" alt="Technology map for systems, web, data, desktop and AI, and delivery" width="100%"></picture>

Language activity uses **source-file touches in authored, non-merge commits** across accessible personal and contributed repositories. A file touched in two commits counts twice. It does not measure code ownership or proficiency, and it includes no private source text. The snapshot is refreshed only during an authenticated audit; the public workflow cannot access private repositories. [Method](docs/discovery.md).

<picture><source media="(max-width: 650px)" srcset="assets/generated/languages-en-mobile.svg"><img src="assets/generated/languages-en.svg" alt="Language activity based on source-file touches in authored commits" width="100%"></picture>

<a id="architecture"></a>
<img src="assets/generated/section-07-en.svg" alt="07 — Architecture" width="100%">

These are high-level maps of components confirmed by repository documentation or structure. Optional and internal paths are intentionally simplified.

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-codeguard-en-mobile.svg"><img src="assets/generated/architecture-codeguard-en.svg" alt="CodeGuard: local project to Rust scanner, findings, optional AI proposal and review" width="100%"></picture>

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-rules-en-mobile.svg"><img src="assets/generated/architecture-rules-en.svg" alt="Rules platform: browser, Next.js, Discord authentication, editor and PostgreSQL" width="100%"></picture>

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-dmv-en-mobile.svg"><img src="assets/generated/architecture-dmv-en.svg" alt="DMV: player, NUI tablet, Lua server, Qbox and MySQL" width="100%"></picture>

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-collaboration-en-mobile.svg"><img src="assets/generated/architecture-collaboration-en.svg" alt="Collaborative FiveM system: client, server resources, shared workflow and persistence" width="100%"></picture>

<a id="activity"></a>
<img src="assets/generated/section-08-en.svg" alt="08 — Activity" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/metrics/activity-en-mobile.svg"><img src="assets/metrics/activity-en.svg" alt="Public GitHub contribution counts, active days, streaks and daily calendar" width="100%"></picture>

The card refreshes from GitHub's contribution calendar. Contributions are not equivalent to commits, hours or project ownership. The date on the card shows when it was generated. [Metric method](docs/metrics.md).

<a id="about"></a>
<img src="assets/generated/section-09-en.svg" alt="09 — About" width="100%">

I build at the boundary between product interfaces and systems work: a scanner with guarded AI proposals, administrative workflows with explicit permissions, and FiveM resources connected to server logic and persistent data. I use Git, tests and documentation to make those systems easier to change and recover.

<a id="contact"></a>
<img src="assets/generated/section-10-en.svg" alt="10 — Contact" width="100%">

For developer tools, FiveM systems, or full-stack administration work, [contact me on GitHub](https://github.com/gopeto222). Email, website and Discord links will appear here when public contact details are available.

<sub>AstroByte Development · Georgi Kanchev · <a href="README.bg.md">Българска версия</a></sub>
