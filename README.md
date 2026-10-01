# OSINTECA 🌍

> **The Open Source Intelligence Library · A Biblioteca Definitiva de OSINT**  
> Jurisdiction-aware · evidence-first · machine-readable · bilingual · AI-assisted with human validation

[![Language](https://img.shields.io/badge/language-English%20%7C%20Portugu%C3%AAs-0A66C2)](#languages)
[![Catalog](https://img.shields.io/badge/catalog-v0.3.2-blue)](data/resources.json)
[![Resources](https://img.shields.io/badge/resources-76-informational)](catalog/INDEX.generated.md)
[![Ethics](https://img.shields.io/badge/use-ethical%20%26%20lawful-success)](ETHICS.md)
[![AI Assisted](https://img.shields.io/badge/curation-AI--assisted-orange)](#ai-assisted-curation)

## OSINTECA mission / Missão

**One place for the analyst to start, pivot, validate and preserve.**  
**Um único ponto de entrada para descobrir fontes, escolher ferramentas, preservar evidência e produzir análise defensável.**

OSINTECA does not blindly mirror giant lists. It uses them as **upstream discovery ecosystems**, normalizes canonical sources, records provenance and tracks validation state.

### Fast decision router / Roteador rápido

| What you have / O que você tem | Start here / Comece aqui |
|---|---|
| Username / handle | [Target-input index](catalog/INPUTS.generated.md) → `username` |
| Email | [Target-input index](catalog/INPUTS.generated.md) → `email` |
| Phone number | [Target-input index](catalog/INPUTS.generated.md) → `phone-number` |
| Domain / IP / ASN | [CTI & OT](catalog/CTI-OT.md) + target-input index |
| Image / video | [IMINT & GEOINT](catalog/IMINT-GEOINT.md) |
| Location / coordinates | [IMINT & GEOINT](catalog/IMINT-GEOINT.md) |
| Company / organization | [Corporate & Financial](catalog/CORPORATE-FINANCIAL.md) |
| GitHub / code repository | [Code Repository OSINT](catalog/CODE-REPOSITORY-OSINT.md) |
| Public event / disputed claim | [Conflict Verification](catalog/CONFLICT-OSINT.md) + [Evidence Preservation](catalog/EVIDENCE-PRESERVATION.md) |
| Web page that may change | [Evidence Preservation](catalog/EVIDENCE-PRESERVATION.md) |
| Need automation / AI | [Agentic OSINT](catalog/AGENTIC-OSINT.md) + [AI-Assisted OSINT](catalog/AI-ASSISTED-OSINT.md) |
| Brazil-specific source | [Brazil country pack](countries/BR/README.md) |

### OSINTECA source mesh

**17 upstream ecosystems are registered** in [data/upstreams.json](data/upstreams.json), including OSINT4ALL, jivoi, Astrosp, OSINT Shifu, Trace Labs, Legendary OSINT, OSINT Brazuca, rawfilejson, My Ultimate OSINT Arsenal, OSINT Framework, Start.me OSINT4ALL, Bellingcat Toolkit, OSINT UI, Talkwalker and GitHub discovery surfaces.

See [docs/SOURCE-MESH.md](docs/SOURCE-MESH.md) for attribution and ingestion rules.

---

## What this repository is / O que este repositório é

**OSINTECA** is not meant to become the longest list of links on GitHub. It is being built as a **maintainable intelligence-resource atlas** that answers:

1. **Where does a source apply? / Onde se aplica?**
2. **Which intelligence discipline does it support? / Qual disciplina apoia?**
3. **What analytical task does it solve? / Qual tarefa resolve?**
4. **How current and trustworthy is the catalog entry? / Quão atual e confiável é a entrada?**
5. **How should evidence and provenance be preserved? / Como preservar evidência e proveniência?**

The canonical data source is [data/resources.json](data/resources.json). Markdown catalogs explain methodology and use; generated views come from the structured data.

---

## Start here / Comece aqui

| Need / Necessidade | Go to / Vá para |
|---|---|
| Find any structured resource | [Generated Resource Index](catalog/INDEX.generated.md) |
| Understand intelligence disciplines | [Intelligence Disciplines](docs/INTELLIGENCE-DISCIPLINES.md) |
| Search techniques and discovery | [Search & Discovery](catalog/SEARCH-DISCOVERY.md) |
| Start from a username/email/domain/image/etc. | [Tools by Target Input](catalog/INPUTS.generated.md) |
| GitHub / public code repositories | [Code Repository OSINT](catalog/CODE-REPOSITORY-OSINT.md) |
| Organize cases, evidence and hypotheses | [Investigation Workbenches](catalog/INVESTIGATION-WORKBENCHES.md) |
| Agent/MCP-assisted workflows | [Agentic OSINT](catalog/AGENTIC-OSINT.md) |
| Preserve web/media evidence | [Evidence Capture & Preservation](catalog/EVIDENCE-PRESERVATION.md) |
| People / usernames / email / phone | [People OSINT](catalog/PEOPLE-OSINT.md) |
| Missing-person methodology | [Missing Persons OSINT](catalog/MISSING-PERSONS-OSINT.md) |
| Social platforms | [SOCMINT](catalog/SOCMINT.md) |
| Image / geolocation / maps | [IMINT & GEOINT](catalog/IMINT-GEOINT.md) |
| Companies / ownership / finance | [Corporate & Financial OSINT](catalog/CORPORATE-FINANCIAL.md) |
| Aircraft / vessels / transport | [Transport / Maritime / Aviation](catalog/TRANSPORT-MARITIME-AVIATION.md) |
| Satellite / orbital / Earth observation | [Space & Satellite](catalog/SPACE-SATELLITE.md) |
| Cyber threat intelligence | [CTI & OT](catalog/CTI-OT.md) |
| Conflict verification | [Conflict OSINT](catalog/CONFLICT-OSINT.md) |
| Environment / deforestation | [Environmental OSINT](catalog/ENVIRONMENTAL-OSINT.md) |
| Academic / media / monitoring | [Academic, Media & Monitoring](catalog/ACADEMIC-MEDIA-MONITORING.md) |
| AI assistance | [AI-Assisted OSINT](catalog/AI-ASSISTED-OSINT.md) |
| Sources by country | [Country & Federation Atlas](countries/README.md) |
| Brazil | [Brazil Country Profile](countries/BR/README.md) |
| Upstream lists we learn from | [Upstream Reference Ecosystems](docs/UPSTREAM-SOURCES.md) |
| Project evolution | [Analyst-Centered Roadmap](docs/ANALYST-ROADMAP.md) |
| Add/correct a resource | [Contributing](CONTRIBUTING.md) |

---

## Analyst workflow / Fluxo do analista

OSINTECA is organized around an intelligence workflow rather than a random toolbox.

```text
Intelligence requirement
        ↓
Scope + red lines + jurisdiction
        ↓
Source mapping
        ↓
Collection
        ↓
Capture + provenance
        ↓
Normalization / entity candidates
        ↓
Verification + corroboration
        ↓
Hypotheses + alternatives
        ↓
Confidence assessment
        ↓
Intelligence product
        ↓
Feedback + revalidation
```

### Evidence language

Use explicit analytical labels:

| Label | Meaning |
|---|---|
| **Observed** | Directly visible in a source |
| **Claimed** | Asserted by a source |
| **Corroborated** | Supported by independent evidence |
| **Inferred** | Analytical conclusion derived from evidence |
| **Unresolved** | Plausible but insufficiently supported |

A username hit is a lead. A search result is a lead. An AI answer is not a source. Humanity did invent entire careers by forgetting these three sentences.

---

## Coverage map / Mapa de cobertura

### Core collection & intelligence disciplines

**OSINT · HUMINT · SIGINT · COMINT · ELINT · FISINT · GEOINT · IMINT · MASINT · TECHINT · CYBINT · CTI · MEDINT · FININT · DOMEX · WEBINT · DNINT · SOCMINT**

See [docs/INTELLIGENCE-DISCIPLINES.md](docs/INTELLIGENCE-DISCIPLINES.md) for definitions and overlap.

### Investigative domains tracked


### Jurisdiction model

```text
countries/<ISO-3166-1 alpha-2>/
├── README.md
├── federal.md
├── subnational/
└── sources/
```

Country packs should distinguish:

**national/federal · states/provinces/regions · municipal/local · courts · companies · property/land · procurement · elections/civic data · environment · transport · infrastructure · archives/media · privacy/legal constraints**

---

## Reference ecosystems incorporated

OSINTECA uses major lists as **upstream discovery ecosystems**, not as content to blindly mirror.

| Upstream | What it contributes |
|---|---|
| [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | Classical OSINT taxonomy: search, people, SOCMINT, domains, archives, imagery, academic research, geospatial, monitoring and CTI |
| [Astrosp/Awesome-OSINT-List](https://github.com/Astrosp/Awesome-OSINT-List) | Broad modern coverage: AI, identity resolution, media verification, metadata, vehicles, aviation, maritime, finance, blockchain, government/public records and training |
| [OSINT Shifu / awesome-osint-repos](https://github.com/osintshifu/awesome-osint-repos) | Repository-first catalogue, target-input model, emerging projects, agentic/MCP integrations and investigation workbenches |
| [Trace Labs repositories](https://github.com/orgs/tracelabs/repositories) | Missing-person methodology, passive research, evidence quality, analyst safety, VM/workstation, training and tooling-selection discipline |
| [Bellingcat Toolkit](https://bellingcat.gitbook.io/toolkit) | Verification-oriented investigation resources |
| [OSINT Framework](https://osintframework.com/) | Discovery-tree approach |
| [OSINT Brazuca](https://github.com/osintbrazuca/osint-brazuca) | Brazilian OSINT ecosystem |

Detailed provenance and import policy: [docs/UPSTREAM-SOURCES.md](docs/UPSTREAM-SOURCES.md).

---

## Trace Labs lessons adopted

From the current Trace Labs ecosystem OSINTECA now incorporates:

- people-centric and missing-person methodology;
- mission definition and stopping conditions;
- passive-research principle for sensitive cases;
- enumeration ≠ validation;
- threat-model thinking;
- evidence capture and archiving;
- analyst workstation as a reproducible environment;
- sanitized training/challenges;
- explicit tool-selection quality criteria.

Primary references:

- [Trace Labs OSINT VM](https://github.com/tracelabs/tlosint-vm)
- [Trace Labs Awesome OSINT](https://github.com/tracelabs/awesome-osint)
- [Trace Labs OSINT Field Manual](https://github.com/tracelabs/tofm)
- [Trace Labs Weekly OSINT Challenges](https://github.com/tracelabs/tracelabs-weekly-osint-challenges)

Historical material is retained as historical, not silently promoted as current.

---

## Evidence capture & preservation

Discovery without preservation is fragile.

OSINTECA now tracks tools and methods for:

**web archiving · screenshots · offline copies · public-media acquisition · frame extraction · OCR · document sanitization · metadata hygiene · archive access**

See [catalog/EVIDENCE-PRESERVATION.md](catalog/EVIDENCE-PRESERVATION.md).

Minimum provenance for an important finding:

- canonical URL;
- capture timestamp + timezone;
- original publication time if known;
- source/account/author;
- capture method;
- archive URL when available;
- relevant metadata;
- analyst observation;
- fact/claim/inference label;
- link to the intelligence requirement.

---

## AI-assisted curation

This repository is **AI-assisted** for classification, normalization, translation, deduplication and drafting.

AI assistance can introduce:

- stale links;
- incorrect descriptions;
- wrong jurisdiction tags;
- duplicate identities;
- hallucinated capabilities;
- incorrect access/licensing assumptions.

Therefore:

> **AI output is never treated as a source. New AI-assisted resource entries default to 🟡 Needs review.**

See [VALIDATION.md](VALIDATION.md) and [AI-Assisted OSINT](catalog/AI-ASSISTED-OSINT.md).

---

## Resource validation

| Marker | Machine status | Meaning |
|---|---|---|
| 🟢 | `verified` | URL and core capability manually checked |
| 🟡 | `needs-review` | Candidate/useful, not yet fully validated |
| 🟠 | `changed` | Important capability/ownership/access changed |
| 🔴 | `broken-unsafe` | Dead, compromised, misleading or unsuitable |
| ⚪ | `historical` | Kept for historical/learning context |

Selection policy: [docs/TOOL-SELECTION-POLICY.md](docs/TOOL-SELECTION-POLICY.md).

---

## Machine-readable architecture

```text
data/upstreams.json  → upstream provenance + curation decisions
        │
data/resources.json
        │
        ├── validated by scripts/validate_catalog.py
        │
        ├── taxonomy → data/taxonomies.json
        │
        ├── schema → schema/resource.schema.json
        │
        ├── input taxonomy → catalog/INPUTS.generated.md
        │
        └── generated view → catalog/INDEX.generated.md
```

The CI rejects malformed IDs, duplicate canonical URLs, invalid disciplines and malformed tags. Scheduled link health raises review signals without pretending every bot-blocked website is dead. A modest concession to reality.

---

## Current project maturity

| Layer | Status |
|---|---|
| Bilingual foundation | ✅ |
| Ethics / validation / contribution policy | ✅ |
| Machine-readable catalog | ✅ |
| Schema + taxonomy + CI | ✅ |
| Link health | ✅ |
| Trace Labs methodology integration | ✅ |
| jivoi + Astrosp + OSINT Shifu upstream mapping | ✅ |
| Evidence preservation layer | ✅ |
| Thematic catalogs | ✅ growing |
| Brazil country seed | ✅ |
| Brazil federal + 27 UFs | 🚧 |
| Evidence-first playbooks | 🚧 |
| GitHub Pages searchable UI | planned |
| Knowledge graph / case graph | planned |
| Change intelligence / monitoring | planned |
| Academy / challenges | planned |

Full plan: [docs/ANALYST-ROADMAP.md](docs/ANALYST-ROADMAP.md).

---

## Ethical and lawful use

Use OSINTECA for lawful, ethical and authorized research.

Do not use this catalog to facilitate:

- stalking or harassment;
- doxxing;
- coercion or discrimination;
- unauthorized access;
- targeting vulnerable people;
- physical harm;
- interference with active investigations.


See [ETHICS.md](ETHICS.md).

---

## Contributing

Corrections are as valuable as additions.

Every proposed resource should identify:

**canonical URL · jurisdiction · discipline · use case · source type · access model · languages · validation state · privacy/legal caveats**

Start with [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Languages

- **English** — primary global documentation language.
- **Português (pt-BR)** — first-class language for Brazil and the Lusophone community.

The machine-readable metadata uses stable canonical values; human-facing documentation may be bilingual or localized.

---

## Long-term model

```text
Resource ↔ Jurisdiction ↔ Discipline ↔ Use Case
    ↕
Entity ↔ Relationship ↔ Evidence
    ↕
 Case ↔ Hypothesis ↔ Assessment
```

The destination is an **open intelligence resource graph** where analysts can discover sources, understand applicability, preserve evidence, evaluate confidence and produce reproducible intelligence products.

## Disclaimer

OSINTECA is an educational and research index. Third-party resources can change, disappear, become paid, alter their terms, or simply be wrong. Inclusion is not endorsement. Responsibility for lawful and proportionate use remains with the analyst.

---

## Definitive upstream reference mesh

| Source | What OSINTECA learns from it |
|---|---|
| [OSINT4ALL](https://github.com/Ridd1kulusC0d3r/OSINT4ALL) | Owner-controlled structured foundation, taxonomy and validation |
| [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | Classical taxonomy and broad discovery |
| [Astrosp/Awesome-OSINT-List](https://github.com/Astrosp/Awesome-OSINT-List) | Modern surface coverage and gap discovery |
| [OSINT Shifu / awesome-osint-repos](https://github.com/osintshifu/awesome-osint-repos) | Repository-first model, target inputs, emerging projects and Agentic/MCP |
| [Trace Labs](https://github.com/orgs/tracelabs/repositories) | Tradecraft, evidence, missing-person methodology, workstation and training |
| [Legendary OSINT](https://github.com/K2SOsint/Legendary_OSINT) | Fraud, CTI, KYC/AML and specialist investigative domains |
| [rawfilejson/awesome-osint-arsenal](https://github.com/rawfilejson/awesome-osint-arsenal) | Broad arsenal and category gap discovery |
| [My Ultimate OSINT Arsenal](https://github.com/rashidwassan/My-Ultimate-OSINT-Arsenal) | Practical category-oriented discovery |
| [OSINT Brazuca](https://github.com/osintbrazuca/osint-brazuca) | Brazil-specific sources |
| [OSINT Framework](https://osintframework.com/) | Tree-style discovery |
| [Start.me OSINT4ALL](https://start.me/p/L1rEYQ/osint4all) | Web/bookmark discovery |
| [Bellingcat Toolkit](https://www.bellingcat.com/resources/2024/09/24/bellingcat-online-investigations-toolkit/) | Tool metadata: cost, difficulty, requirements, limitations, ethics and guides |
| [OSINT UI](https://docs.osint-ui.com/en) | Investigation graph, correlation, API and MCP ideas |
| [Talkwalker OSINT tools](https://www.talkwalker.com/blog/best-osint-tools) | Commercial/social-listening market view |
| [GitHub OSINT topic](https://github.com/topics/osint) | Emerging open-source project discovery |

> **Reference notice:** attribution is mandatory. Upstreams are discovery sources, not blanket verification. Canonical projects are preferred over mirrors and packaging forks.

<details>
<summary><strong>Master resource catalogue / Catálogo mestre (76 normalized resources)</strong></summary>

The structured source of truth is [data/resources.json](data/resources.json). This collapsed table keeps the repository homepage useful as a one-stop analyst entry point.

| Resource | Domain(s) | Target input(s) | Jurisdiction | Access | Validation |
|---|---|---|---|---|---|
| [ArchiveBox](https://github.com/ArchiveBox/ArchiveBox) | evidence-preservation, web-archives | url | GLOBAL | free | needs-review |
| [Astrosp Awesome OSINT List](https://github.com/Astrosp/Awesome-OSINT-List) | meta-index | — | GLOBAL | free | verified |
| [Awesome OSINT Repositories by OSINT Shifu](https://github.com/osintshifu/awesome-osint-repos) | meta-index, agentic-osint | no-fixed-input | GLOBAL | free | verified |
| [awesome-osint-arsenal](https://github.com/rawfilejson/awesome-osint-arsenal) | meta-index | — | GLOBAL | free | needs-review |
| [Bellingcat auto-archiver](https://github.com/bellingcat/auto-archiver) | evidence-preservation, web-archives | url | GLOBAL | free | needs-review |
| [Bellingcat Octosuite](https://github.com/bellingcat/octosuite) | code-repository-intelligence, identity-intelligence | username, repository-url | GLOBAL | free | verified |
| [Bellingcat Online Investigation Toolkit](https://bellingcat.gitbook.io/toolkit) | verification | — | GLOBAL | free | needs-review |
| [Carbon14](https://github.com/Lazza/Carbon14) | web-archives, web-research | — | GLOBAL | free | needs-review |
| [Censys Search](https://search.censys.io/) | cyber-infrastructure | ip-address, domain | GLOBAL | freemium | needs-review |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | change-intelligence, web-monitoring | url | GLOBAL | mixed | verified |
| [Copernicus Browser](https://browser.dataspace.copernicus.eu/) | satellite-osint, environmental-intelligence | — | GLOBAL | free | needs-review |
| [Dangerzone](https://github.com/freedomofpress/dangerzone) | analyst-safety, document-analysis | document, file | GLOBAL | free | needs-review |
| [ExifTool](https://exiftool.org/) | media-forensics | file, image, video | GLOBAL | free | needs-review |
| [FFmpeg](https://ffmpeg.org/) | media-forensics, media-preservation | audio, video, file | GLOBAL | free | needs-review |
| [Flowsint](https://github.com/reconurge/flowsint) | investigation-workbench, link-analysis, entity-resolution | name, organization-name | GLOBAL | free | needs-review |
| [FollowTheMoney](https://github.com/alephdata/followthemoney) | entity-resolution, corporate-intelligence, investigative-data | name, organization-name, dataset | GLOBAL | free | verified |
| [gallery-dl](https://github.com/mikf/gallery-dl) | media-preservation | — | GLOBAL | free | needs-review |
| [GHunt](https://github.com/mxrch/GHunt) | identity-intelligence | name | GLOBAL | free | needs-review |
| [GitFive](https://github.com/mxrch/GitFive) | code-repository-intelligence, identity-intelligence | name, username, repository-url | GLOBAL | free | needs-review |
| [Global Fishing Watch](https://globalfishingwatch.org/map/) | maritime-intelligence, environmental-intelligence | location | GLOBAL | free | needs-review |
| [Global Forest Watch](https://www.globalforestwatch.org/) | environmental-intelligence | — | GLOBAL | free | needs-review |
| [gowitness](https://github.com/sensepost/gowitness) | evidence-preservation, web-research | url | GLOBAL | free | needs-review |
| [Have I Been Pwned](https://haveibeenpwned.com/) | breach-exposure | — | GLOBAL | freemium | needs-review |
| [Holehe](https://github.com/megadose/holehe) | identity-intelligence | email | GLOBAL | free | needs-review |
| [HTTrack](https://www.httrack.com/) | web-archives, web-research | — | GLOBAL | free | needs-review |
| [ICIJ Datashare](https://github.com/ICIJ/datashare) | document-analysis, investigative-data | document, file, dataset | GLOBAL | free | verified |
| [Instaloader](https://github.com/instaloader/instaloader) | social-media-intelligence, media-preservation | name, username, image | GLOBAL | free | needs-review |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | threat-intelligence | domain, ip-address, file-hash, url | GLOBAL | free | needs-review |
| [Internet Archive CLI](https://github.com/jjjake/internetarchive) | evidence-preservation, web-archives | — | GLOBAL | free | needs-review |
| [Internet Archive Wayback Machine](https://web.archive.org/) | web-archives, web-research | url | GLOBAL | free | needs-review |
| [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | meta-index | — | GLOBAL | free | verified |
| [Maigret](https://github.com/soxoj/maigret) | identity-intelligence | username | GLOBAL | free | needs-review |
| [Maltego](https://www.maltego.com/) | entity-resolution, link-analysis | — | GLOBAL | freemium | needs-review |
| [MapBiomas Alerta](https://alerta.mapbiomas.org/) | environmental-intelligence | — | BR | free | needs-review |
| [Mapillary](https://www.mapillary.com/) | geospatial-analysis, street-level-imagery | location, coordinates, image | GLOBAL | free | needs-review |
| [MAT2](https://0xacab.org/jvoisin/mat2) | analyst-safety, metadata | — | GLOBAL | free | needs-review |
| [MISP](https://github.com/MISP/MISP) | threat-intelligence | domain, ip-address, file-hash | GLOBAL | free | needs-review |
| [Monolith](https://github.com/Y2Z/monolith) | evidence-preservation | — | GLOBAL | free | needs-review |
| [N2YO](https://www.n2yo.com/) | space-intelligence | — | GLOBAL | freemium | needs-review |
| [NASA Worldview](https://worldview.earthdata.nasa.gov/) | satellite-osint, environmental-intelligence | — | GLOBAL | free | needs-review |
| [OpenCorporates](https://opencorporates.com/) | corporate-intelligence | — | GLOBAL | freemium | needs-review |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | threat-intelligence | domain, ip-address, file-hash | GLOBAL | free | needs-review |
| [OpenRefine](https://github.com/OpenRefine/OpenRefine) | data-processing, document-analysis | dataset | GLOBAL | free | needs-review |
| [OpenSky Network](https://opensky-network.org/) | aviation-intelligence | aircraft-id, location | GLOBAL | freemium | needs-review |
| [OpenTrace](https://github.com/Gacut/OpenTrace) | investigation-workbench, evidence-preservation, link-analysis | name, url, document, image | GLOBAL | free | verified |
| [OSINT Brazuca](https://github.com/osintbrazuca/osint-brazuca) | regional-osint | — | BR | free | needs-review |
| [OSINT Framework](https://osintframework.com/) | meta-index | — | GLOBAL | free | needs-review |
| [PhoneInfoga](https://github.com/sundowndev/phoneinfoga) | identity-intelligence | phone-number | GLOBAL | free | needs-review |
| [QGIS](https://qgis.org/) | geospatial-analysis | dataset, coordinates, location | GLOBAL | free | needs-review |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | cyber-infrastructure | domain, ip-address, name, organization-name | GLOBAL | free | needs-review |
| [Safecast](https://safecast.org/) | radiological-monitoring, environmental-intelligence | location, coordinates | GLOBAL | free | needs-review |
| [SearXNG](https://github.com/searxng/searxng) | search-discovery | — | GLOBAL | free | needs-review |
| [Sherlock](https://github.com/sherlock-project/sherlock) | identity-intelligence | username | GLOBAL | free | needs-review |
| [Shodan](https://www.shodan.io/) | cyber-infrastructure | ip-address, domain | GLOBAL | freemium | needs-review |
| [SingleFile](https://github.com/gildas-lormeau/SingleFile) | evidence-preservation, web-archives | url | GLOBAL | free | needs-review |
| [sn0int](https://github.com/kpcyrd/sn0int) | osint-framework, cyber-infrastructure | — | GLOBAL | free | needs-review |
| [Social Analyzer](https://github.com/qeeqbox/social-analyzer) | social-media-intelligence, identity-intelligence | name, username | GLOBAL | free | needs-review |
| [Space-Track.org](https://www.space-track.org/) | space-intelligence | aircraft-id | GLOBAL | account | needs-review |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | cyber-infrastructure | domain, ip-address, username, email | GLOBAL | free | needs-review |
| [TerraBrasilis](https://terrabrasilis.dpi.inpe.br/) | environmental-intelligence | — | BR | free | needs-review |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | document-analysis, media-forensics | image, document | GLOBAL | free | needs-review |
| [theHarvester](https://github.com/laramies/theHarvester) | cyber-infrastructure, search-discovery | domain | GLOBAL | free | needs-review |
| [Timesketch](https://github.com/google/timesketch) | timeline-analysis, investigation-workbench | event-data | GLOBAL | free | needs-review |
| [Trace Labs Awesome OSINT](https://github.com/tracelabs/awesome-osint) | missing-persons-osint, meta-index | — | GLOBAL | free | verified |
| [Trace Labs Gumshoe](https://github.com/tracelabs/gumshoe) | investigation-methodology, link-analysis | — | GLOBAL | free | historical |
| [Trace Labs OSINT Field Manual](https://github.com/tracelabs/tofm) | missing-persons-osint, investigation-methodology | — | GLOBAL | free | verified |
| [Trace Labs OSINT Live](https://github.com/tracelabs/tlosint-live) | investigation-environment | — | GLOBAL | free | historical |
| [Trace Labs OSINT VM](https://github.com/tracelabs/tlosint-vm) | investigation-environment, missing-persons-osint | — | GLOBAL | free | verified |
| [Trace Labs Search Party CTF Writeups](https://github.com/tracelabs/searchparty-ctf-writeups) | missing-persons-osint, osint-training | — | GLOBAL | free | historical |
| [Trace Labs Weekly OSINT Challenges](https://github.com/tracelabs/tracelabs-weekly-osint-challenges) | osint-training, investigation-methodology | — | GLOBAL | free | verified |
| [UseOSINT Skills](https://github.com/UseOSINT/Skills) | agentic-osint, investigation-methodology | no-fixed-input | GLOBAL | free | verified |
| [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | satellite-osint | — | GLOBAL | account | needs-review |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | identity-intelligence | username | GLOBAL | free | needs-review |
| [WiGLE](https://wigle.net/) | wireless-intelligence, geospatial-analysis | — | GLOBAL | account | needs-review |
| [World Intel MCP](https://github.com/marc-shade/world-intel-mcp) | agentic-osint, situational-awareness, monitoring | keyword, location, event-data | GLOBAL | free | needs-review |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | media-preservation | — | GLOBAL | free | needs-review |

</details>

## Analyst evolution / Evolução do analista

The OSINTECA maturity path is:

```text
Foundations
   ↓
Source evaluation
   ↓
Evidence preservation
   ↓
Verification & corroboration
   ↓
Target-input pivoting
   ↓
Domain specialization
   ↓
Entity resolution & graph reasoning
   ↓
Change intelligence
   ↓
AI-assisted analysis with provenance
   ↓
Review, teaching & community contribution
```

Full path: [docs/ANALYST-ROADMAP.md](docs/ANALYST-ROADMAP.md)  
Repository evolution: [ROADMAP.md](ROADMAP.md)

