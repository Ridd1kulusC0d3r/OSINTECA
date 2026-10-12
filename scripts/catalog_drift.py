#!/usr/bin/env python3
"""Compare local OSINTECA resources with an explicitly supplied upstream JSON.

Read-only, standard-library tool: no network activity and no automatic imports.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_catalog(path: Path) -> dict[str, dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    resources = payload.get("resources")
    if not isinstance(resources, list):
        raise ValueError(f"{path}: expected an array named resources")
    by_id: dict[str, dict] = {}
    for item in resources:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            raise ValueError(f"{path}: each resource requires a string id")
        if item["id"] in by_id:
            raise ValueError(f"{path}: duplicate resource id: {item['id']}")
        by_id[item["id"]] = item
    return by_id


def compare(upstream: dict[str, dict], local: dict[str, dict]) -> dict:
    shared = sorted(upstream.keys() & local.keys())
    missing = sorted(upstream.keys() - local.keys())
    local_only = sorted(local.keys() - upstream.keys())
    url_conflicts = [
        {"id": key, "upstream": upstream[key].get("canonical_url"),
         "local": local[key].get("canonical_url")}
        for key in shared
        if upstream[key].get("canonical_url") != local[key].get("canonical_url")
    ]
    review_differences = [
        {"id": key,
         "fields": [
             field for field in ("status", "last_verified")
             if upstream[key].get(field) != local[key].get(field)
         ]}
        for key in shared
        if any(upstream[key].get(field) != local[key].get(field)
               for field in ("status", "last_verified"))
    ]
    return {
        "upstream_count": len(upstream),
        "local_count": len(local),
        "shared_ids": len(shared),
        "missing_from_local": missing,
        "local_only": local_only,
        "canonical_url_conflicts": url_conflicts,
        "review_metadata_differences": review_differences,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path, required=True,
                        help="Path to a locally checked-out OSINT4ALL data/resources.json")
    parser.add_argument("--local", type=Path,
                        default=Path(__file__).resolve().parents[1] / "data" / "resources.json")
    parser.add_argument("--strict", action="store_true",
                        help="Also fail if any entries or review metadata differ")
    args = parser.parse_args()
    result = compare(load_catalog(args.upstream), load_catalog(args.local))
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    has_conflicts = bool(result["canonical_url_conflicts"])
    has_drift = bool(
        result["missing_from_local"] or result["local_only"]
        or result["review_metadata_differences"]
    )
    return 1 if (has_conflicts or (args.strict and has_drift)) else 0


if __name__ == "__main__":
    raise SystemExit(main())
