# OSINTECA Source Mesh

OSINTECA is designed as a **single analyst entry point** fed by many upstream ecosystems. The goal is not to republish their work verbatim. The goal is to discover, normalize, attribute, validate and maintain useful resources in one canonical model.

## Ingestion policy

```text
Upstream ecosystem
      ↓
discover candidates
      ↓
canonical-source check
      ↓
deduplicate / merge identities
      ↓
classify by input + domain + jurisdiction
      ↓
record provenance
      ↓
needs-review
      ↓
human validation
      ↓
verified
```

## Primary upstreams

| Upstream | OSINTECA role |
|---|---|
| OSINT4ALL | Owner-controlled structured foundation migrated into OSINTECA |
| jivoi/awesome-osint | Classical OSINT taxonomy and broad discovery |
| Astrosp/Awesome-OSINT-List | Modern surface-area and gap discovery |
| OSINT Shifu / awesome-osint-repos | Repository-first catalogue, target-input model, emerging projects, AI/MCP |
| Trace Labs | Tradecraft, missing-person methodology, analyst workstation, evidence and training |
| K2SOsint / Legendary OSINT | Specialist fraud, CTI, KYC/AML and investigative domains |
| rawfilejson / awesome-osint-arsenal | Broad arsenal and category gap discovery |
| rashidwassan / My Ultimate OSINT Arsenal | Practical category-oriented discovery |
| OSINT Brazuca | Brazil-specific sources and regional context |
| OSINT Framework | Tree-style discovery model |
| Start.me OSINT4ALL | Web/bookmark discovery board |
| Bellingcat Toolkit | Tool-selection metadata: cost, difficulty, requirements, limitations, ethics and guides |
| OSINT UI | Investigation graph, correlation, API and MCP workflow ideas |
| Talkwalker OSINT overview | Commercial/social-listening market perspective |
| GitHub topic: osint | Continuous emerging-project discovery |
| jivoi + osintshifu profiles | Maintainer ecosystem watch |

Machine-readable registry: [../data/upstreams.json](../data/upstreams.json).

## Attribution rule

Every imported or normalized item should keep its canonical URL and, when known, an `upstream_refs` value. Lists and articles are discovery sources, not evidence that a child tool is safe, current or correct.

## Why this matters

A giant copied list becomes stale immediately. A provenance-aware source mesh lets OSINTECA answer four more useful questions:

1. Where did this resource come from?
2. Is the canonical project still alive?
3. What problem does it solve?
4. Has a human actually validated it?
