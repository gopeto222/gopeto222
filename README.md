<p align="right"><strong>English</strong> · <a href="README.bg.md">Български</a></p>

<img src="assets/brand/hero.svg" alt="Georgi Kanchev — software developer, AstroByte Development" width="100%">

<p align="center"><strong>Full-stack systems · FiveM infrastructure · Developer tools · Automation</strong></p>

I build software that connects interfaces, server logic, and operational workflows. My current work includes local code analysis, FiveM resources, and web administration tools. I favor explicit trust boundaries, maintainable modules, and reviewable changes.

<p align="center"><a href="#selected-work">Work</a> · <a href="#engineering-focus">Engineering</a> · <a href="#technology">Technology</a> · <a href="#github-activity">Activity</a> · <a href="#contact">Contact</a></p>

## Selected work

### AstroByte CodeGuard · developer tool

**Problem.** A scan result is useful only when a developer can inspect the evidence and safely evaluate a proposed fix.

**Solution.** A local Rust scanner and CLI feed a Tauri 2 desktop application with React and TypeScript. The app presents findings and source context, and offers optional fixes through OpenAI or Anthropic. A proposed change is shown as a diff and requires explicit approval before it is applied. Fix history supports verification and guarded revert.

**Architecture.** `project → Rust scanner → findings → optional AI proposal → diff review → apply → verification`.

**My contribution.** Personal repository under my account. **Status.** Active private development; source and build are not public. The description is based on the repository's README and project structure, not a public release claim.

<img src="assets/architecture/codeguard.svg" alt="CodeGuard architecture: local project, Rust scanner, findings, optional AI proposal, review and verification" width="100%">

### FiveM systems · resource development

I maintain Lua resources and server customizations in personal repositories and have authored commits in selected AstroByte Development organization repositories. The verified work spans business registry, DMV, document and vehicle related resources. Organization work is collaborative and private; these descriptions identify the domain without publishing private source or attributing others' commits to me.

**Engineering focus.** Client and server boundaries, persistent data, and resource integration. Individual security or performance properties should be judged per resource; I do not claim every resource implements every pattern.

<img src="assets/architecture/fivem.svg" alt="FiveM resource architecture: client, server resource and persistent database" width="100%">

### Web administration · private project

A personal TypeScript repository is described as a FiveM server rules website with a Discord administration panel. It is private, so this portfolio does not link to its source or claim a deployed demo. My public profile also describes experience with backend, databases and Discord integrations; specific implementations remain unlisted until they can be shared.

## Engineering focus

| Domain | What I work on |
| --- | --- |
| Developer tools | Local analysis, evidence-rich findings, guarded AI assisted edits |
| FiveM | Lua resources, Qbox ecosystem integrations, client/server workflows |
| Web systems | TypeScript interfaces and administration workflows |
| Operations | Automation, Git workflows and maintainable delivery |

## Technology

**Verified in inspected repositories:** Rust, Lua, TypeScript, React, Tauri 2, Python, OpenAI and Anthropic integrations. The CodeGuard desktop app targets macOS; its current frontend is Tauri/React, not SwiftUI.

**From my existing profile and private FiveM work:** JavaScript, Node.js, MySQL, Qbox, `ox_lib`, `ox_target`, `ox_inventory`, and `oxmysql`. These are experience areas, not claims that every showcased project uses them.

## GitHub activity

<img src="assets/metrics/activity.svg" alt="Public GitHub contribution calendar metrics for the most recent 12 months" width="100%">

The graphic uses GitHub's public contribution calendar for this account. Contributions include activity other than commits. It does not reveal private repositories or measure hours worked. The workflow refreshes the graphic daily; a date on the card shows when it was generated. [Metric method](docs/metrics.md).

## Contact

For developer tools, FiveM systems, and web administration work, [contact me through GitHub](https://github.com/gopeto222). Other contact channels will be added when a public address is available.

<sub>AstroByte Development · Georgi Kanchev</sub>
