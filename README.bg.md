<!-- Generated from data/profile.json and data/projects.json by scripts/build_readmes.py. -->

<a href="README.md" title="Към английската версия"><picture><source media="(max-width: 650px)" srcset="assets/generated/hero-bg-mobile.svg"><img src="assets/generated/hero-bg.svg" alt="Към английската версия; AstroByte engineering portfolio" width="100%"></picture></a>

<p align="center"><a href="#featured">Основни системи</a> · <a href="#archive">Всички проекти</a> · <a href="#technology">Технологии</a> · <a href="#activity">Активност</a> · <a href="#contact">Контакт</a></p>

Разработвам локални инструменти, уеб приложения за администрация и FiveM системи. По-долу личните проекти са разграничени от установения принос в обща работа.

<a id="engineering"></a>
<img src="assets/generated/chapter-engineering-bg.svg" alt="Инженерен профил" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/command-bg-mobile.svg"><img src="assets/generated/command-bg.svg" alt="Инженерен профил dashboard with verified domains and practice" width="100%"></picture>

<a id="featured"></a>
<img src="assets/generated/chapter-featured-bg.svg" alt="Основни системи" width="100%">

Подбраните проекти са описани според проверените хранилища. Частният код остава частен.

### AstroByte CodeGuard

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-codeguard-bg-mobile.svg"><img src="assets/generated/feature-codeguard-bg.svg" alt="Системна схема за AstroByte CodeGuard" width="100%"></picture>

<sub>Проверена системна схема; не е кадър от приложението.</sub>

- **Проблем:** Находките се нуждаят от контекст, а предложените поправки — от преглед и възможност за връщане.
- **Система:** Rust скенер и CLI с macOS интерфейс чрез Tauri 2 и React. Предложенията от OpenAI или Anthropic са незадължителни и се показват като diff преди изрично одобрение.
- **Моят принос:** Личен проект с установени авторски commit-и.
- **Инженерно решение:** Локално сканиране, ограничен и редактиран AI контекст, ключове в Keychain и връщане след проверка за конфликти.
- **Статус:** Частна разработка; не се твърди публичен релийз.
- **Технологии:** Rust · Tauri 2 · React · TypeScript · OpenAI · Anthropic


### Платформа за правила

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-rules-bg-mobile.svg"><img src="assets/generated/feature-rules-bg.svg" alt="Системна схема за Платформа за правила" width="100%"></picture>

<sub>Проверена системна схема; не е кадър от приложението.</sub>

- **Проблем:** Правилата имат нужда от удобен публичен изглед и контролиран редакторски процес.
- **Система:** Next.js, React, TypeScript, PostgreSQL и Prisma с Discord OAuth администрация, чернови, версии и одитни записи.
- **Моят принос:** Личен проект с установени авторски commit-и.
- **Инженерно решение:** Сървърни проверки на достъпа и проследим път от чернова до публикуване.
- **Статус:** Частен код; не се твърди публично демо.
- **Технологии:** Next.js · React · TypeScript · PostgreSQL · Prisma


### DMV таблет

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-dmv-bg-mobile.svg"><img src="assets/generated/feature-dmv-bg.svg" alt="Системна схема за DMV таблет" width="100%"></picture>

<sub>Проверена системна схема; не е кадър от приложението.</sub>

- **Проблем:** Регистрацията на превозни средства изисква процес в играта с постоянни записи и проследима история.
- **Система:** FiveM NUI таблет, Lua код за клиент и сървър, Qbox и MySQL. Документацията описва регистрация, история на номерата, QR проверка и локализация.
- **Моят принос:** Има авторски commit-и, включително промяна по релийз; проектът е организационен.
- **Инженерно решение:** Системата свързва клиентския интерфейс със сървърна логика и постоянни данни.
- **Статус:** Частен организационен код.
- **Технологии:** Lua · Qbox · MySQL · NUI


### Бизнес регистър

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-registry-bg-mobile.svg"><img src="assets/generated/feature-registry-bg.svg" alt="Системна схема за Бизнес регистър" width="100%"></picture>

<sub>Проверена системна схема; не е кадър от приложението.</sub>

- **Проблем:** Бизнес записите и документите изискват подреден процес със сървърни проверки.
- **Система:** Qbox ресурс с таблет интерфейс, MySQL записи, локализация и журнал, описани в хранилището.
- **Моят принос:** Установен е авторски първоначален commit. Това не доказва еднолична собственост върху по-късните промени.
- **Инженерно решение:** Сървърната валидация защитава записите, а журналът прави промените проследими.
- **Статус:** Частен организационен код.
- **Технологии:** Lua · Qbox · MySQL


### Съвместна FiveM инфраструктура

<picture><source media="(max-width: 650px)" srcset="assets/generated/feature-collaboration-bg-mobile.svg"><img src="assets/generated/feature-collaboration-bg.svg" alt="Системна схема за Съвместна FiveM инфраструктура" width="100%"></picture>

<sub>Проверена системна схема; не е кадър от приложението.</sub>

- **Проблем:** Споделената FiveM система изисква координирани промени по ресурси и данни.
- **Система:** В достъпната история се вижда работа по Lua и TypeScript ресурси и промяна по базата данни в частно споделено хранилище.
- **Моят принос:** Установени са 44 авторски commit-а в достъпните клонове. Цялата система не се приписва на един човек.
- **Инженерно решение:** Портфолиото обозначава системата като съвместна и ограничава твърденията до установената работа.
- **Статус:** Частен съвместен код.
- **Технологии:** Lua · TypeScript · Vue


<a id="archive"></a>
<img src="assets/generated/chapter-archive-bg.svg" alt="Всички проекти" width="100%">

20 проверени проекта от 25 достъпни хранилища. 5 организационни хранилища са изключени, защото не е установен авторски принос. Личните, организационните и съвместните проекти са обозначени отделно. [Метод на одита](docs/discovery.md).

#### Инструменти

<picture><source media="(max-width: 650px)" srcset="assets/generated/archive-tools-bg-mobile.svg"><img src="assets/generated/archive-tools-bg.svg" alt="Инструменти project inventory with role and availability" width="100%"></picture>

#### Инженерни процеси

<picture><source media="(max-width: 650px)" srcset="assets/generated/archive-operations-bg-mobile.svg"><img src="assets/generated/archive-operations-bg.svg" alt="Инженерни процеси project inventory with role and availability" width="100%"></picture>

#### FiveM системи

<picture><source media="(max-width: 650px)" srcset="assets/generated/archive-fivem-bg-mobile.svg"><img src="assets/generated/archive-fivem-bg.svg" alt="FiveM системи project inventory with role and availability" width="100%"></picture>

#### Уеб системи

<picture><source media="(max-width: 650px)" srcset="assets/generated/archive-web-bg-mobile.svg"><img src="assets/generated/archive-web-bg.svg" alt="Уеб системи project inventory with role and availability" width="100%"></picture>

[Публичен код: хранилището на този профил](https://github.com/gopeto222/gopeto222).

<a id="fivem"></a>
<img src="assets/generated/chapter-fivem-bg.svg" alt="FiveM инженерство" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/fivem-bg-mobile.svg"><img src="assets/generated/fivem-bg.svg" alt="FiveM схема на клиент, сървър и постоянни данни" width="100%"></picture>

Това е модел от документираните ресурси, а не твърдение, че всеки проект използва всички компоненти. DMV и регистърът по-горе са конкретни примери.

<a id="technology"></a>
<img src="assets/generated/chapter-technology-bg.svg" alt="Технологии" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/technology-bg-mobile.svg"><img src="assets/generated/technology-bg.svg" alt="Групи технологии от проверените проекти" width="100%"></picture>

<a id="architecture"></a>
<img src="assets/generated/chapter-architecture-bg.svg" alt="Архитектура" width="100%">

Схемите показват документирани компоненти и важни граници. Незадължителните интеграции са обозначени.

#### AstroByte CodeGuard

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-codeguard-bg-mobile.svg"><img src="assets/generated/architecture-codeguard-bg.svg" alt="AstroByte CodeGuard architecture diagram" width="100%"></picture>

#### Платформа за правила

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-rules-bg-mobile.svg"><img src="assets/generated/architecture-rules-bg.svg" alt="Платформа за правила architecture diagram" width="100%"></picture>

#### DMV таблет

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-dmv-bg-mobile.svg"><img src="assets/generated/architecture-dmv-bg.svg" alt="DMV таблет architecture diagram" width="100%"></picture>

<details><summary>Още архитектурни схеми</summary>

#### Бизнес регистър

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-registry-bg-mobile.svg"><img src="assets/generated/architecture-registry-bg.svg" alt="Бизнес регистър architecture diagram" width="100%"></picture>

#### Съвместна FiveM инфраструктура

<picture><source media="(max-width: 650px)" srcset="assets/generated/architecture-collaboration-bg-mobile.svg"><img src="assets/generated/architecture-collaboration-bg.svg" alt="Съвместна FiveM инфраструктура architecture diagram" width="100%"></picture>

</details>

<a id="activity"></a>
<img src="assets/generated/chapter-activity-bg.svg" alt="Активност" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/metrics/activity-bg-mobile.svg"><img src="assets/metrics/activity-bg.svg" alt="Публичен календар на GitHub приносите и поредици" width="100%"></picture>

Картата се генерира от публичния календар на GitHub. Броят не измерва часове, собственост върху код или влияние на проекта. [Метод](docs/metrics.md).

<picture><source media="(max-width: 650px)" srcset="assets/generated/languages-bg-mobile.svg"><img src="assets/generated/languages-bg.svg" alt="Променени файлове в авторски commit-и без merge" width="100%"></picture>

Езиковата активност е датирана извадка от промени по файлове в авторски commit-и. Тя не измерва умения. [Ограничения](docs/discovery.md).

<a id="practice"></a>
<img src="assets/generated/chapter-practice-bg.svg" alt="Как разработвам" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/practice-bg-mobile.svg"><img src="assets/generated/practice-bg.svg" alt="Инженерни решения за сигурност, производителност, архитектура и доставка" width="100%"></picture>

Това са примери от конкретни проекти, а не твърдение, че всяко хранилище има еднакви защити.

<a id="services"></a>
<img src="assets/generated/chapter-services-bg.svg" alt="Съвместна работа" width="100%">

<picture><source media="(max-width: 650px)" srcset="assets/generated/services-bg-mobile.svg"><img src="assets/generated/services-bg.svg" alt="Области на работа с потвърден опит" width="100%"></picture>

<a id="contact"></a>
<img src="assets/generated/chapter-contact-bg.svg" alt="Контакт" width="100%">

Имате идея за инструмент, платформа или система? Нека започнем с конкретния проблем и разговор в GitHub.

<a href="https://github.com/gopeto222" title="Свържете се с Георги в GitHub"><picture><source media="(max-width: 650px)" srcset="assets/generated/contact-bg-mobile.svg"><img src="assets/generated/contact-bg.svg" alt="Contact @gopeto222 on GitHub" width="100%"></picture></a>

<sub>AstroByte Development · Георги Канчев · <a href="README.md">Към английската версия</a></sub>
