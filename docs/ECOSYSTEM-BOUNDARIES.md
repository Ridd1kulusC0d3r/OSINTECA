# OSINTECA and OSINT4ALL: catalog ownership

## Finding (12 October 2026)

A comparison of the two repos' checked-in `data/resources.json` files found:

| Metric | Observed |
|---|---:|
| OSINT4ALL resources | 90 |
| OSINTECA resources | 76 |
| Shared resource IDs | 76 |
| Only in OSINT4ALL | 14 |
| Only in OSINTECA | 0 |
| Conflicting `canonical_url` values among shared IDs | 0 |

All 76 OSINTECA IDs were also present in OSINT4ALL at inspection time. That is **100% shared identity**, not proof that the two files are byte-identical. Many metadata fields differ, including review state and added dates, and the sources must not be silently overwritten.

## Recommended division of responsibility

**OSINT4ALL**: canonical stewardship of resource identities, provenance, verification, jurisdiction, lifecycle and normalized metadata.

**OSINTECA**: human-oriented analyst library, explanations, annotated reading paths, methodological guides and search experiences **built from an identified catalog snapshot**.

**OSINTList**: quick link directory. It is not an additional catalog authority.

**The-Pensieve-OSINT**: analyst memory, investigative routing and repeatable decision support, not an independent copy of the same resource records.

These are recommendations for future governance; this PR does not change upstream repositories.

## Local, read-only drift check

With both repositories checked out as siblings:

```bash
cd OSINTECA
python scripts/catalog_drift.py --upstream ../OSINT4ALL/data/resources.json
```

The command reports shared IDs, missing entries, local-only entries, URL conflicts and differences in review metadata. By default it only exits nonzero for conflicting URLs or invalid input. Use `--strict` in an intentional migration gate to reject all drift.

This script **does not fetch, merge, import or overwrite** any catalog, and CI uses synthetic inputs rather than live network access.

## Migration procedure

1. Designate a versioned OSINT4ALL JSON snapshot and record its commit SHA.
2. Review all 14 upstream-only entries for taxonomy/compatibility rather than copying them blindly.
3. Compare `status` and `last_verified` per shared ID; never elevate a verification status automatically.
4. Preserve OSINTECA-only commentary in a separate annotation layer keyed by canonical resource ID.
5. Generate OSINTECA views from the pinned snapshot plus annotations.
6. Add tests for ID stability, links, schema changes and provenance before deleting any duplicated data.

## Evidence vs inference

The numerical overlap is verified on the inspected files, but **no conclusion about operating production sites or external URL health is implied**. A shared URL is not evidence of ownership, operational reliability or permission to collect from a service.
