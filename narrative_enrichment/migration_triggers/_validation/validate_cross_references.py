#!/usr/bin/env python3
"""
KinLore Narrative Enrichment Layer — Cross-Reference Validation Script
======================================================================
Validates that all 150+ JSON files in the migration_triggers tree wire
together correctly: file counts, cross-references, schema consistency,
source quality, narrative hook variables, and integration stress tests.

Standalone Python 3 script — no external dependencies beyond the
standard library.

Usage:
    python3 validate_cross_references.py

Author: KinLore.ai / Polsia
Date:   2026-03-16
"""

import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# ── Configuration ──────────────────────────────────────────────────────

BASE = Path("/home/dbcanady/kinlore-data/narrative_enrichment/migration_triggers")
NEL_BASE = Path("/home/dbcanady/kinlore-data/narrative_enrichment")

DIRS = {
    "core":              BASE / "core",
    "regional_nc":       BASE / "regional" / "nc",
    "regional_va":       BASE / "regional" / "va",
    "regional_oh":       BASE / "regional" / "oh",
    "regional_sc":       BASE / "regional" / "sc",
    "regional_ga":       BASE / "regional" / "ga",
    "regional_ky":       BASE / "regional" / "ky",
    "regional_tn":       BASE / "regional" / "tn",
    "regional_ms":       BASE / "regional" / "ms",
    "regional_tx":       BASE / "regional" / "tx",
    "regional_mn":       BASE / "regional" / "mn",
    "regional_pa":       BASE / "regional" / "pa",
    "regional_al":       BASE / "regional" / "al",
    "regional_la":       BASE / "regional" / "la",
    "regional_il":       BASE / "regional" / "il",
    "destinations":      BASE / "shared" / "destinations",
    "occupations":       BASE / "shared" / "occupations",
    "routes":            BASE / "shared" / "routes",
    "community_texture": BASE / "shared" / "community_texture",
    "material_life":     BASE / "shared" / "material_life",
    "wages":             BASE / "shared" / "wages",
    "templates":         BASE / "templates",
    "research_guidance": BASE / "research_guidance",
    "validation":        BASE / "_validation",
    "life_patterns":     NEL_BASE / "life_patterns",
}

EXPECTED_COUNTS = {
    "core":              32,
    "regional_nc":       6,
    "regional_va":       1,
    "regional_oh":       1,
    "regional_sc":       1,
    "regional_ga":       1,
    "regional_ky":       1,
    "regional_tn":       1,
    "regional_ms":       1,
    "regional_tx":       1,
    "regional_mn":       1,
    "regional_pa":       1,
    "regional_al":       1,
    "regional_la":       1,
    "regional_il":       1,
    "destinations":      82,
    "occupations":       27,
    "routes":            25,
    "community_texture": 33,
    "material_life":     20,
    "wages":             3,
    "templates":         11,
    "research_guidance": 10,
    "life_patterns":     23,
}

# Files in life_patterns/ that are metadata, not content patterns
LIFE_PATTERN_META_FILES = {"CHAIN_LINK_INDEX"}

# Required fields by file type
REQUIRED_TRIGGER_FIELDS = [
    "migration_id", "display_name", "era", "migration_class",
    "involuntary", "push_factors", "pull_factors",
    "record_implications", "counter_narratives", "source_references",
]

REQUIRED_DESTINATION_FIELDS = [
    "destination_id", "display_name", "neighborhoods",
    "major_employers", "source_references",
]

REQUIRED_OCCUPATION_FIELDS = [
    "occupation_id", "display_name", "what_they_did",
    "economics", "working_conditions", "records_generated",
    "source_references",
]

REQUIRED_ROUTE_FIELDS = [
    "route_id", "display_name", "route_type",
    "segments", "source_references",
]

REQUIRED_MATERIAL_LIFE_FIELDS = [
    "material_life_id", "display_name", "era", "region",
    "population", "trigger_refs", "sections",
    "sensory_snapshot", "narrative_hooks", "source_references",
]

REQUIRED_COMMUNITY_TEXTURE_FIELDS = [
    "institutions", "social_fabric", "narrative_hooks",
    "counter_narratives", "source_references",
]

REQUIRED_LIFE_PATTERN_FIELDS = [
    "pattern_id", "display_name", "short_description",
    "era_range", "regions", "population", "pattern_class",
    "lifecycle_phases", "entry_conditions", "exit_conditions",
    "chain_examples", "daily_life", "economic_trajectory",
    "family_dynamics", "record_signatures", "narrative_hooks",
    "counter_narratives", "source_references",
]

VALID_PATTERN_CLASSES = {
    "economic_arc", "family_dynamic", "community_pattern",
    "occupational_lifecycle", "social_transformation",
}

# Variable pattern for narrative hooks
VARIABLE_RE = re.compile(r"\{[a-z_]+\}")

# ── Counters & Reporting ──────────────────────────────────────────────

class Report:
    """Tracks pass/warn/fail counts and stores messages."""

    def __init__(self):
        self.passed = 0
        self.warnings = 0
        self.failed = 0
        self.messages = []
        self._section = ""

    def section(self, title: str):
        self._section = title
        self.messages.append(f"\n{'=' * 60}")
        self.messages.append(f"=== {title} ===")
        self.messages.append(f"{'=' * 60}")

    def subsection(self, title: str):
        self.messages.append(f"\n--- {title} ---")

    def ok(self, msg: str):
        self.passed += 1
        self.messages.append(f"  [PASS] {msg}")

    def warn(self, msg: str):
        self.warnings += 1
        self.messages.append(f"  [WARN] {msg}")

    def fail(self, msg: str):
        self.failed += 1
        self.messages.append(f"  [FAIL] {msg}")

    def info(self, msg: str):
        self.messages.append(f"  [INFO] {msg}")

    def blank(self):
        self.messages.append("")

    @property
    def total(self):
        return self.passed + self.warnings + self.failed

    def print_all(self):
        for m in self.messages:
            print(m)

    def print_summary(self):
        print(f"\n{'=' * 60}")
        print("=== SUMMARY ===")
        print(f"{'=' * 60}")
        print(f"  Total checks:  {self.total}")
        print(f"  Passed:        {self.passed}")
        print(f"  Warnings:      {self.warnings}")
        print(f"  Failed:        {self.failed}")
        pct = (self.passed / self.total * 100) if self.total else 0
        print(f"  Pass rate:     {pct:.1f}%")
        if self.failed == 0 and self.warnings == 0:
            print("\n  RESULT: ALL CLEAR — every cross-reference validates.")
        elif self.failed == 0:
            print(f"\n  RESULT: PASS with {self.warnings} warning(s) — no hard failures.")
        else:
            print(f"\n  RESULT: {self.failed} FAILURE(s) require attention.")


# ── Helpers ───────────────────────────────────────────────────────────

def load_json(path: Path) -> dict | list | None:
    """Load a JSON file, returning None on parse failure."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as exc:
        return None


def json_files_in(directory: Path) -> list[Path]:
    """Return sorted list of .json files in a directory."""
    if not directory.is_dir():
        return []
    return sorted(p for p in directory.iterdir() if p.suffix == ".json")


def stem_set(directory: Path) -> set[str]:
    """Return set of file stems (no extension) in a directory."""
    return {p.stem for p in json_files_in(directory)}


def collect_all_strings(obj, accumulator: list):
    """Recursively collect all string values from a JSON object."""
    if isinstance(obj, str):
        accumulator.append(obj)
    elif isinstance(obj, list):
        for item in obj:
            collect_all_strings(item, accumulator)
    elif isinstance(obj, dict):
        for v in obj.values():
            collect_all_strings(v, accumulator)


def count_source_refs(data: dict) -> int:
    """Count source_references in a data dict, handling both list-of-str
    and list-of-dict formats."""
    refs = data.get("source_references", [])
    if isinstance(refs, list):
        return len(refs)
    return 0


def has_wikipedia(data: dict) -> list[str]:
    """Return list of source references that mention Wikipedia."""
    refs = data.get("source_references", [])
    hits = []
    for ref in refs:
        text = ""
        if isinstance(ref, str):
            text = ref
        elif isinstance(ref, dict):
            text = json.dumps(ref)
        if "wikipedia" in text.lower():
            hits.append(text[:120])
    return hits


def extract_destination_ids(dest_refs) -> list[str]:
    """Extract destination IDs from the various destination_refs formats.
    Can be:
      - list of strings:  ["chicago", "detroit"]
      - list of dicts:    [{"destination_id": "boston_ma", ...}, ...]
    """
    ids = []
    if not isinstance(dest_refs, list):
        return ids
    for item in dest_refs:
        if isinstance(item, str):
            ids.append(item)
        elif isinstance(item, dict):
            did = item.get("destination_id", "")
            if did:
                ids.append(did)
    return ids


def extract_route_refs(data: dict) -> list[str]:
    """Extract route_refs from trigger transportation block."""
    transport = data.get("transportation", {})
    if isinstance(transport, dict):
        refs = transport.get("route_refs", [])
        if isinstance(refs, list):
            return [r for r in refs if isinstance(r, str)]
    return []


# ── Part 1: File Inventory ───────────────────────────────────────────

def check_file_inventory(report: Report):
    report.section("FILE INVENTORY")

    total_found = 0
    for key, expected in EXPECTED_COUNTS.items():
        d = DIRS[key]
        files = json_files_in(d)
        actual = len(files)
        total_found += actual

        if actual == expected:
            report.ok(f"{key}: {actual} files (expected {expected})")
        elif actual > expected:
            report.warn(f"{key}: {actual} files (expected {expected}) — {actual - expected} extra")
        else:
            report.fail(f"{key}: {actual} files (expected {expected}) — {expected - actual} missing")

    # Validation dir itself (stress_tests.json — not counted in the 120 content files)
    val_files = json_files_in(DIRS["validation"])
    report.info(f"_validation: {len(val_files)} file(s) (stress_tests.json — not counted in content total)")

    content_total = sum(EXPECTED_COUNTS.values())
    report.info(f"Expected content files: {content_total}")
    report.info(f"Found content files:    {total_found}")

    # Grand total including validation
    grand = total_found + len(val_files)
    report.info(f"Grand total (all JSON): {grand}")


# ── Part 2a: Trigger → Route references ─────────────────────────────

def check_trigger_route_refs(report: Report):
    report.subsection("Trigger -> Route References")

    route_stems = stem_set(DIRS["routes"])
    trigger_dirs = [("core", DIRS["core"])] + [(k, DIRS[k]) for k in DIRS if k.startswith("regional_")]

    for label, d in trigger_dirs:
        for fp in json_files_in(d):
            data = load_json(fp)
            if data is None:
                report.fail(f"{label}/{fp.name}: could not parse JSON")
                continue

            route_refs = extract_route_refs(data)
            if not route_refs:
                report.info(f"{label}/{fp.name}: no route_refs (empty or absent)")
                continue

            for rid in route_refs:
                if rid in route_stems:
                    report.ok(f"{label}/{fp.name} -> routes/{rid}.json")
                else:
                    report.fail(f"{label}/{fp.name} -> routes/{rid}.json  NOT FOUND")


# ── Part 2b: Trigger → Destination references ───────────────────────

def check_trigger_destination_refs(report: Report):
    report.subsection("Trigger -> Destination References")

    dest_stems = stem_set(DIRS["destinations"])

    # Build a lookup of alternate_ids from destination files so we can
    # match destination_refs like "boston_ma" to file "boston.json"
    alt_id_map = {}  # alternate_id -> file stem
    for fp in json_files_in(DIRS["destinations"]):
        dd = load_json(fp)
        if dd and isinstance(dd, dict):
            for alt in dd.get("alternate_ids", []):
                alt_id_map[alt] = fp.stem

    trigger_dirs = [("core", DIRS["core"])] + [(k, DIRS[k]) for k in DIRS if k.startswith("regional_")]

    for label, d in trigger_dirs:
        for fp in json_files_in(d):
            data = load_json(fp)
            if data is None:
                report.fail(f"{label}/{fp.name}: could not parse JSON")
                continue

            dest_refs = data.get("destination_refs", [])
            dest_ids = extract_destination_ids(dest_refs)

            if not dest_ids:
                report.info(f"{label}/{fp.name}: no destination_refs")
                continue

            for did in dest_ids:
                if did in dest_stems:
                    report.ok(f"{label}/{fp.name} -> destinations/{did}.json")
                elif did in alt_id_map:
                    report.ok(f"{label}/{fp.name} -> destinations/{alt_id_map[did]}.json (via alternate_id '{did}')")
                else:
                    # Not necessarily a failure — some triggers reference
                    # destinations that don't have full profiles yet.
                    report.warn(f"{label}/{fp.name} -> destinations/{did}.json  NOT FOUND (no profile yet)")


# ── Part 2c: Community Texture → Trigger references ─────────────────

def check_community_trigger_refs(report: Report):
    report.subsection("Community Texture -> Trigger References")

    trigger_stems = stem_set(DIRS["core"])
    regional_stems = set()
    for k in DIRS:
        if k.startswith("regional_"):
            regional_stems |= stem_set(DIRS[k])
    all_trigger_stems = trigger_stems | regional_stems

    for fp in json_files_in(DIRS["community_texture"]):
        data = load_json(fp)
        if data is None:
            report.fail(f"community_texture/{fp.name}: could not parse JSON")
            continue

        trefs = data.get("trigger_refs", [])
        if not trefs:
            report.info(f"community_texture/{fp.name}: no trigger_refs")
            continue

        for tref in trefs:
            if tref in all_trigger_stems:
                report.ok(f"community_texture/{fp.name} -> trigger {tref}")
            else:
                # Some community textures reference trigger IDs that use
                # different naming conventions (e.g. "german_immigration_1848"
                # vs. file "german_immigration.json"). These are conceptual
                # refs that may not map 1:1 to filenames.
                report.warn(f"community_texture/{fp.name} -> trigger '{tref}'  "
                            f"NOT FOUND as core or regional file")


# ── Part 2d: Schema Consistency ──────────────────────────────────────

def check_schema_consistency(report: Report):
    report.subsection("Schema Consistency — _schema_version and _last_updated")

    all_dirs = [
        ("core",              DIRS["core"]),
        ("regional/nc",       DIRS["regional_nc"]),
        ("destinations",      DIRS["destinations"]),
        ("occupations",       DIRS["occupations"]),
        ("routes",            DIRS["routes"]),
        ("community_texture", DIRS["community_texture"]),
        ("material_life",     DIRS["material_life"]),
        ("wages",             DIRS["wages"]),
        ("templates",         DIRS["templates"]),
        ("research_guidance", DIRS["research_guidance"]),
        ("life_patterns",     DIRS["life_patterns"]),
    ]

    for label, d in all_dirs:
        for fp in json_files_in(d):
            # Skip metadata files in life_patterns
            if label == "life_patterns" and fp.stem in LIFE_PATTERN_META_FILES:
                report.info(f"{label}/{fp.name}: metadata file — skipping schema check")
                continue

            data = load_json(fp)
            if data is None:
                report.fail(f"{label}/{fp.name}: INVALID JSON — could not parse")
                continue

            # _schema_version
            sv = data.get("_schema_version")
            if sv == "1.0":
                report.ok(f"{label}/{fp.name}: _schema_version = '1.0'")
            elif sv is None:
                report.fail(f"{label}/{fp.name}: MISSING _schema_version")
            else:
                report.fail(f"{label}/{fp.name}: _schema_version = '{sv}' (expected '1.0')")

            # _last_updated
            lu = data.get("_last_updated")
            if lu:
                report.ok(f"{label}/{fp.name}: _last_updated = '{lu}'")
            else:
                report.fail(f"{label}/{fp.name}: MISSING _last_updated")


def check_required_fields(report: Report):
    report.subsection("Schema Consistency — Required Fields by Type")

    checks = [
        ("core",              DIRS["core"],         REQUIRED_TRIGGER_FIELDS,             "trigger"),
        ("regional/nc",       DIRS["regional_nc"],  REQUIRED_TRIGGER_FIELDS,             "trigger"),
        ("destinations",      DIRS["destinations"], REQUIRED_DESTINATION_FIELDS,          "destination"),
        ("occupations",       DIRS["occupations"],  REQUIRED_OCCUPATION_FIELDS,           "occupation"),
        ("routes",            DIRS["routes"],       REQUIRED_ROUTE_FIELDS,                "route"),
        ("community_texture", DIRS["community_texture"], REQUIRED_COMMUNITY_TEXTURE_FIELDS, "community_texture"),
        ("material_life",     DIRS["material_life"],     REQUIRED_MATERIAL_LIFE_FIELDS,      "material_life"),
        ("life_patterns",     DIRS["life_patterns"],     REQUIRED_LIFE_PATTERN_FIELDS,       "life_pattern"),
    ]

    for label, d, required, ftype in checks:
        for fp in json_files_in(d):
            # Skip metadata files in life_patterns
            if label == "life_patterns" and fp.stem in LIFE_PATTERN_META_FILES:
                continue

            data = load_json(fp)
            if data is None:
                continue  # Already flagged above

            missing = [f for f in required if f not in data]
            if not missing:
                report.ok(f"{label}/{fp.name}: all {len(required)} required {ftype} fields present")
            else:
                report.fail(f"{label}/{fp.name}: MISSING required {ftype} fields: {missing}")

            # Life pattern-specific validations
            if ftype == "life_pattern":
                # Validate pattern_class
                pc = data.get("pattern_class", "")
                if pc in VALID_PATTERN_CLASSES:
                    report.ok(f"{label}/{fp.name}: valid pattern_class '{pc}'")
                else:
                    report.fail(f"{label}/{fp.name}: invalid pattern_class '{pc}' "
                                f"(expected one of {sorted(VALID_PATTERN_CLASSES)})")

                # Validate lifecycle_phases has 3-5 entries
                phases = data.get("lifecycle_phases", [])
                if isinstance(phases, list) and 3 <= len(phases) <= 5:
                    report.ok(f"{label}/{fp.name}: {len(phases)} lifecycle_phases (3-5 expected)")
                elif isinstance(phases, list):
                    report.warn(f"{label}/{fp.name}: {len(phases)} lifecycle_phases (3-5 expected)")
                else:
                    report.fail(f"{label}/{fp.name}: lifecycle_phases is not a list")


# ── Part 2e: Source Reference Quality ────────────────────────────────

def check_source_quality(report: Report):
    report.subsection("Source Reference Quality")

    all_dirs = [
        ("core",              DIRS["core"]),
        ("regional/nc",       DIRS["regional_nc"]),
        ("destinations",      DIRS["destinations"]),
        ("occupations",       DIRS["occupations"]),
        ("routes",            DIRS["routes"]),
        ("community_texture", DIRS["community_texture"]),
        ("material_life",     DIRS["material_life"]),
        ("templates",         DIRS["templates"]),
        ("research_guidance", DIRS["research_guidance"]),
        ("wages",             DIRS["wages"]),
        ("life_patterns",     DIRS["life_patterns"]),
    ]

    for label, d in all_dirs:
        for fp in json_files_in(d):
            # Skip metadata files in life_patterns
            if label == "life_patterns" and fp.stem in LIFE_PATTERN_META_FILES:
                continue

            data = load_json(fp)
            if data is None:
                continue

            count = count_source_refs(data)
            if count >= 3:
                report.ok(f"{label}/{fp.name}: {count} source references")
            elif count > 0:
                report.warn(f"{label}/{fp.name}: only {count} source reference(s) (< 3)")
            else:
                # Some file types (templates, wages, research_guidance)
                # may store sources differently — warn, don't fail.
                if label in ("templates", "research_guidance", "wages"):
                    # Check for alternate source fields
                    alt_keys = ["data_source", "sources", "data_sources"]
                    has_alt = any(k in data for k in alt_keys)
                    if has_alt:
                        report.ok(f"{label}/{fp.name}: sources present via alternate field")
                    else:
                        report.warn(f"{label}/{fp.name}: no source_references found")
                else:
                    report.warn(f"{label}/{fp.name}: no source_references array found")

            # Wikipedia check
            wiki_hits = has_wikipedia(data)
            if wiki_hits:
                for hit in wiki_hits:
                    report.fail(f"{label}/{fp.name}: source references Wikipedia: {hit}")
            # (no PASS message for the negative case to avoid clutter)


# ── Part 2f: Narrative Hook Variable Syntax ──────────────────────────

def check_narrative_hooks(report: Report):
    report.subsection("Narrative Hook Variable Syntax")

    all_dirs = [
        ("core",              DIRS["core"]),
        ("regional/nc",       DIRS["regional_nc"]),
        ("destinations",      DIRS["destinations"]),
        ("occupations",       DIRS["occupations"]),
        ("routes",            DIRS["routes"]),
        ("community_texture", DIRS["community_texture"]),
        ("material_life",     DIRS["material_life"]),
        ("templates",         DIRS["templates"]),
        ("life_patterns",     DIRS["life_patterns"]),
    ]

    for label, d in all_dirs:
        for fp in json_files_in(d):
            # Skip metadata files in life_patterns
            if label == "life_patterns" and fp.stem in LIFE_PATTERN_META_FILES:
                continue

            data = load_json(fp)
            if data is None:
                continue

            all_strs = []
            collect_all_strings(data, all_strs)

            hooks_with_vars = []
            for s in all_strs:
                matches = VARIABLE_RE.findall(s)
                if matches:
                    hooks_with_vars.append((s[:80], matches))

            if hooks_with_vars:
                unique_vars = set()
                for _, matches in hooks_with_vars:
                    unique_vars.update(matches)
                report.ok(f"{label}/{fp.name}: {len(hooks_with_vars)} narrative hook(s) "
                          f"with variables: {sorted(unique_vars)[:5]}{'...' if len(unique_vars) > 5 else ''}")
            else:
                # Templates may use structural beats instead of
                # inline {variable} hooks
                if label == "templates":
                    # Check for "variables" key in template variants
                    has_var_list = False
                    if isinstance(data, dict):
                        for v in data.get("variants", []):
                            if isinstance(v, dict) and v.get("variables"):
                                has_var_list = True
                                break
                    if has_var_list:
                        report.ok(f"{label}/{fp.name}: template uses 'variables' lists in variants")
                    else:
                        report.warn(f"{label}/{fp.name}: no narrative hooks with {{variable}} syntax found")
                else:
                    report.warn(f"{label}/{fp.name}: no narrative hooks with {{variable}} syntax found")


# ── Part 3: Integration Stress Tests ─────────────────────────────────

# Test ancestor definitions
TEST_ANCESTORS = [
    {
        "name": "Patrick O'Brien",
        "label": "Irish Famine Immigrant",
        "birth_year": 1830,
        "origin": "County Cork, Ireland",
        "destination": "Boston, MA",
        "arrival_year": 1848,
        "occupation": "laborer",
        "race": None,
        "era": "1845-1860",
        "trigger_keywords": ["irish", "famine"],
        "expected_triggers": ["irish_famine"],
        "expected_routes": ["atlantic_crossing_famine", "atlantic_crossing_steerage"],
        "expected_dest_ids": ["boston", "boston_ma"],
        "expected_occupations": ["railroad_laborer", "general_farmer_midwest"],
        "expected_textures": ["boston_irish_1845_1900"],
        "expected_templates": ["what_they_saw", "letter_home"],
        "expected_guidance": ["census_gaps", "name_change_patterns", "church_record_transfers"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "Ella Mae Johnson",
        "label": "Great Migration",
        "birth_year": 1915,
        "origin": "Bolivar County, MS",
        "destination": "Chicago, IL",
        "arrival_year": 1938,
        "occupation": "domestic servant / meatpacking worker",
        "race": "Black",
        "era": "1910-1970",
        "trigger_keywords": ["great_migration"],
        "expected_triggers": ["great_migration", "boll_weevil"],
        "expected_routes": ["illinois_central"],
        "expected_dest_ids": ["chicago"],
        "expected_occupations": ["domestic_servant", "meatpacking_worker"],
        "expected_textures": ["chicago_black_bronzeville", "mississippi_delta_cotton", "deep_south_black_community"],
        "expected_templates": ["what_they_saw", "fork_in_the_road"],
        "expected_guidance": ["census_gaps", "city_directory_strategies", "church_record_transfers"],
        "expected_wages": ["wages_by_occupation_1900_1950"],
    },
    {
        "name": "Anders Olsen",
        "label": "Mormon Handcart",
        "birth_year": 1840,
        "origin": "Norway",
        "destination": "Salt Lake City, UT",
        "arrival_year": 1856,
        "occupation": "farmer",
        "race": None,
        "era": "1830-1869",
        "trigger_keywords": ["mormon"],
        "expected_triggers": ["mormon_migration"],
        "expected_routes": ["mormon_trail", "atlantic_crossing_steerage"],
        "expected_dest_ids": ["salt_lake_city_ut"],
        "expected_occupations": ["general_farmer_midwest"],
        "expected_textures": [],
        "expected_templates": ["what_they_saw", "letter_home"],
        "expected_guidance": ["census_gaps", "church_record_transfers"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "Wong Ah Sing",
        "label": "Chinese Railroad Worker",
        "birth_year": 1845,
        "origin": "Guangdong, China",
        "destination": "Portland, OR",
        "arrival_year": 1865,
        "occupation": "railroad laborer / laundry",
        "race": "Chinese",
        "era": "1850-1943",
        "trigger_keywords": ["chinese"],
        "expected_triggers": ["chinese_exclusion_era", "railroad_construction"],
        "expected_routes": ["pacific_crossing"],
        "expected_dest_ids": ["portland_or", "san_francisco_chinatown_ca", "san_francisco"],
        "expected_occupations": ["railroad_laborer", "laundress"],
        "expected_textures": [],
        "expected_templates": ["what_they_saw", "record_silences"],
        "expected_guidance": ["name_change_patterns", "ethnic_specific_sources"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "James Henry Canady",
        "label": "NC Farm to Mill",
        "birth_year": 1870,
        "origin": "Wayne County, NC",
        "destination": "Cumberland County, NC",
        "arrival_year": 1895,
        "occupation": "cotton mill operative",
        "race": "white",
        "era": "1865-1910",
        "trigger_keywords": ["nc_eastern", "textile_mill", "farm_to_mill"],
        "expected_triggers": ["nc_eastern_farm_to_mill", "textile_mill_recruitment"],
        "expected_routes": [],
        "expected_dest_ids": ["fayetteville_mill_district"],
        "expected_occupations": ["textile_mill_hand", "tenant_farmer"],
        "expected_textures": ["eastern_nc_farm_community", "fayetteville_mill_district", "piedmont_mill_village"],
        "expected_templates": ["what_they_saw", "fork_in_the_road"],
        "expected_guidance": ["census_gaps", "church_record_transfers", "property_record_strategies", "military_record_strategies"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "Sarah Goldstein",
        "label": "Jewish Pogrom Flight",
        "birth_year": 1890,
        "origin": "Minsk, Russia",
        "destination": "New York City (Lower East Side)",
        "arrival_year": 1905,
        "occupation": "garment worker",
        "race": None,
        "era": "1880-1924",
        "trigger_keywords": ["jewish", "pogrom"],
        "expected_triggers": ["jewish_pogrom_flight", "se_european_wave"],
        "expected_routes": ["atlantic_crossing_steerage"],
        "expected_dest_ids": ["nyc_lower_east_side", "new_york_city"],
        "expected_occupations": ["seamstress_garment_worker"],
        "expected_textures": ["new_york_lower_east_side"],
        "expected_templates": ["what_they_saw", "letter_home"],
        "expected_guidance": ["name_change_patterns", "ethnic_specific_sources", "census_gaps"],
        "expected_wages": ["wages_by_occupation_1900_1950"],
    },
    # ── Phase 3E Real Test Ancestors ──────────────────────────────────
    # These 5 ancestors are from the user's actual family research.
    # Pre-3E scores: Abel Bass 62% | William Boon 31% | Daniel Canady 50%
    #                Young Autry 25% | George Knauss 80%
    {
        "name": "Abel Bass",
        "label": "Civil War POW / Sampson County Yeoman",
        "birth_year": 1816,
        "origin": "Sampson County, NC",
        "destination": None,
        "arrival_year": None,
        "occupation": "farmer",
        "race": "white",
        "era": "1816-1905",
        "trigger_keywords": ["civil_war", "yeoman", "stayed"],
        "expected_triggers": ["civil_war_service", "antebellum_yeoman_south", "stayed_and_adapted"],
        "expected_routes": [],
        "expected_dest_ids": [],
        "expected_occupations": ["tenant_farmer", "general_farmer_midwest"],
        "expected_textures": ["eastern_nc_farm_community"],
        "expected_templates": ["military_service_arc", "record_silences", "economic_life_story", "hinge_generation"],
        "expected_guidance": ["census_gaps", "property_record_strategies", "military_record_strategies"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "William Boon",
        "label": "Civil War KIA / Nash County Turpentine Belt",
        "birth_year": 1830,
        "origin": "Nash County, NC",
        "destination": None,
        "arrival_year": None,
        "occupation": "turpentine laborer / farmer",
        "race": "white",
        "era": "1830-1862",
        "trigger_keywords": ["civil_war", "yeoman"],
        "expected_triggers": ["civil_war_service", "antebellum_yeoman_south"],
        "expected_routes": [],
        "expected_dest_ids": [],
        "expected_occupations": ["tenant_farmer"],
        "expected_textures": ["eastern_nc_farm_community"],
        "expected_templates": ["military_service_arc", "record_silences", "hinge_generation"],
        "expected_guidance": ["census_gaps", "military_record_strategies"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "Daniel Canady",
        "label": "War of 1812 Veteran / Cumberland County TPA",
        "birth_year": 1793,
        "origin": "Cumberland County, NC",
        "destination": None,
        "arrival_year": None,
        "occupation": "farmer",
        "race": "white",
        "era": "1793-1868",
        "trigger_keywords": ["war_of_1812", "yeoman", "stayed"],
        "expected_triggers": ["war_of_1812_service", "antebellum_yeoman_south", "stayed_and_adapted"],
        "expected_routes": [],
        "expected_dest_ids": [],
        "expected_occupations": ["tenant_farmer", "general_farmer_midwest"],
        "expected_textures": ["eastern_nc_farm_community"],
        "expected_templates": ["military_service_arc", "record_silences", "economic_life_story", "hinge_generation"],
        "expected_guidance": ["census_gaps", "property_record_strategies", "military_record_strategies"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "Young Autry",
        "label": "Pre-1850 Sampson County / Minimal Records",
        "birth_year": 1790,
        "origin": "Sampson County, NC",
        "destination": None,
        "arrival_year": None,
        "occupation": "farmer",
        "race": "white",
        "era": "1790-1850",
        "trigger_keywords": ["yeoman", "stayed"],
        "expected_triggers": ["antebellum_yeoman_south", "stayed_and_adapted"],
        "expected_routes": [],
        "expected_dest_ids": [],
        "expected_occupations": ["tenant_farmer", "general_farmer_midwest"],
        "expected_textures": ["eastern_nc_farm_community"],
        "expected_templates": ["record_silences", "hinge_generation"],
        "expected_guidance": ["census_gaps", "property_record_strategies"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
    {
        "name": "George Knauss",
        "label": "PA Dutch Younger-Son Diaspora to Pike County/North Dakota",
        "birth_year": 1840,
        "origin": "Northampton County, PA",
        "destination": "Nelson County, ND",
        "arrival_year": 1900,
        "occupation": "farmer / laborer",
        "race": "white",
        "era": "1840-1936",
        "trigger_keywords": ["homestead", "german", "economic"],
        "expected_triggers": ["homestead_act", "german_immigration", "economic_panics_19c"],
        "expected_routes": ["northern_pacific"],
        "expected_dest_ids": [],
        "expected_occupations": ["general_farmer_midwest"],
        "expected_textures": ["great_plains_homesteader", "pa_anthracite_patch_town", "german_midwest_1848_1900"],
        "expected_templates": ["what_they_saw", "fork_in_the_road", "economic_life_story", "hinge_generation"],
        "expected_guidance": ["census_gaps", "property_record_strategies"],
        "expected_wages": ["wages_by_occupation_1850_1900"],
    },
]

PIPELINE_COMPONENTS = [
    "triggers", "route", "destination", "occupation",
    "community_texture", "template", "research_guidance", "wage_data",
]


def run_stress_test(ancestor: dict, report: Report,
                    trigger_data_cache: dict,
                    dest_stems: set, dest_alt_map: dict,
                    occ_stems: set, route_stems: set,
                    texture_stems: set, template_stems: set,
                    guidance_stems: set, wage_stems: set):
    """Run a single ancestor through the pipeline and report coverage."""

    report.subsection(f"Test Ancestor: {ancestor['name']} ({ancestor['label']})")

    coverage = {}
    gaps = []

    # 1. Which trigger(s) match
    matched_triggers = []
    for tid in ancestor["expected_triggers"]:
        core_path = DIRS["core"] / f"{tid}.json"
        nc_path = DIRS["regional_nc"] / f"{tid}.json"
        if core_path.exists():
            matched_triggers.append(f"core/{tid}.json")
        elif nc_path.exists():
            matched_triggers.append(f"regional/nc/{tid}.json")
        else:
            gaps.append(f"No trigger file for '{tid}'")

    if matched_triggers:
        report.ok(f"Triggers: {', '.join(matched_triggers)}")
        coverage["triggers"] = True
    else:
        report.fail(f"No matching triggers found")
        coverage["triggers"] = False

    # 2. Which route(s) exist
    matched_routes = []
    missing_routes = []
    for rid in ancestor["expected_routes"]:
        if rid in route_stems:
            matched_routes.append(f"routes/{rid}.json")
        else:
            missing_routes.append(rid)

    if matched_routes:
        report.ok(f"Routes: {', '.join(matched_routes)}")
        coverage["route"] = True
    elif not ancestor["expected_routes"]:
        report.info(f"Routes: none expected (intra-regional migration)")
        coverage["route"] = True  # No route expected, so no gap
    else:
        report.warn(f"Routes: missing {missing_routes}")
        coverage["route"] = False

    if missing_routes:
        for r in missing_routes:
            gaps.append(f"No route profile for '{r}'")

    # 3. Which destination(s) exist
    matched_dests = []
    missing_dests = []
    for did in ancestor["expected_dest_ids"]:
        if did in dest_stems:
            matched_dests.append(f"destinations/{did}.json")
        elif did in dest_alt_map:
            matched_dests.append(f"destinations/{dest_alt_map[did]}.json (via alt_id '{did}')")
        else:
            missing_dests.append(did)

    if matched_dests:
        report.ok(f"Destinations: {', '.join(matched_dests)}")
        coverage["destination"] = True
    else:
        report.warn(f"Destinations: no matching profiles found")
        coverage["destination"] = False

    if missing_dests:
        for md in missing_dests:
            gaps.append(f"No destination profile for '{md}'")

    # 4. Which occupation(s) match
    matched_occs = []
    missing_occs = []
    for oid in ancestor["expected_occupations"]:
        if oid in occ_stems:
            matched_occs.append(f"occupations/{oid}.json")
        else:
            missing_occs.append(oid)

    if matched_occs:
        report.ok(f"Occupations: {', '.join(matched_occs)}")
        coverage["occupation"] = True
    else:
        report.warn(f"Occupations: no matching profiles found")
        coverage["occupation"] = False

    if missing_occs:
        for mo in missing_occs:
            gaps.append(f"No occupation profile for '{mo}'")

    # 5. Which community texture(s) apply
    matched_tex = []
    missing_tex = []
    for tid in ancestor["expected_textures"]:
        if tid in texture_stems:
            matched_tex.append(f"community_texture/{tid}.json")
        else:
            missing_tex.append(tid)

    if matched_tex:
        report.ok(f"Community textures: {', '.join(matched_tex)}")
        coverage["community_texture"] = True
    elif not ancestor["expected_textures"]:
        report.warn(f"Community textures: none expected (gap in coverage)")
        coverage["community_texture"] = False
        gaps.append("No community texture profile expected for this migration pattern")
    else:
        report.warn(f"Community textures: missing {missing_tex}")
        coverage["community_texture"] = len(matched_tex) > 0

    if missing_tex:
        for mt in missing_tex:
            gaps.append(f"No community texture profile for '{mt}'")

    # 6. Which template(s) would be selected
    matched_tmpl = []
    missing_tmpl = []
    for tid in ancestor["expected_templates"]:
        if tid in template_stems:
            matched_tmpl.append(f"templates/{tid}.json")
        else:
            missing_tmpl.append(tid)

    if matched_tmpl:
        report.ok(f"Templates: {', '.join(matched_tmpl)}")
        coverage["template"] = True
    else:
        report.warn(f"Templates: no matching templates found")
        coverage["template"] = False

    if missing_tmpl:
        for mt in missing_tmpl:
            gaps.append(f"No template for '{mt}'")

    # 7. Which research guidance files would be relevant
    matched_guid = []
    missing_guid = []
    for gid in ancestor["expected_guidance"]:
        if gid in guidance_stems:
            matched_guid.append(f"research_guidance/{gid}.json")
        else:
            missing_guid.append(gid)

    if matched_guid:
        report.ok(f"Research guidance: {', '.join(matched_guid)}")
        coverage["research_guidance"] = True
    else:
        report.warn(f"Research guidance: no matching guidance found")
        coverage["research_guidance"] = False

    if missing_guid:
        for mg in missing_guid:
            gaps.append(f"No research guidance for '{mg}'")

    # 8. Wage data
    matched_wages = []
    missing_wages = []
    for wid in ancestor["expected_wages"]:
        if wid in wage_stems:
            matched_wages.append(f"wages/{wid}.json")
        else:
            missing_wages.append(wid)

    if matched_wages:
        report.ok(f"Wage data: {', '.join(matched_wages)}")
        coverage["wage_data"] = True
    else:
        report.warn(f"Wage data: no matching wage tables found")
        coverage["wage_data"] = False

    if missing_wages:
        for mw in missing_wages:
            gaps.append(f"No wage table for '{mw}'")

    # Coverage score
    covered = sum(1 for v in coverage.values() if v)
    total = len(PIPELINE_COMPONENTS)
    pct = covered / total * 100

    report.blank()
    report.info(f"COVERAGE SCORE: {covered}/{total} = {pct:.0f}%")

    if gaps:
        report.info(f"GAPS ({len(gaps)}):")
        for g in gaps:
            report.info(f"  - {g}")
    else:
        report.info("GAPS: none — full pipeline coverage")


def run_stress_tests(report: Report):
    report.section("INTEGRATION STRESS TESTS")

    # Pre-compute lookup sets
    dest_stems = stem_set(DIRS["destinations"])
    occ_stems = stem_set(DIRS["occupations"])
    route_stems = stem_set(DIRS["routes"])
    texture_stems = stem_set(DIRS["community_texture"])
    template_stems = stem_set(DIRS["templates"])
    guidance_stems = stem_set(DIRS["research_guidance"])
    wage_stems = stem_set(DIRS["wages"])

    # Build alternate ID map for destinations
    dest_alt_map = {}
    for fp in json_files_in(DIRS["destinations"]):
        dd = load_json(fp)
        if dd and isinstance(dd, dict):
            for alt in dd.get("alternate_ids", []):
                dest_alt_map[alt] = fp.stem

    trigger_data_cache = {}

    for ancestor in TEST_ANCESTORS:
        run_stress_test(
            ancestor, report, trigger_data_cache,
            dest_stems, dest_alt_map,
            occ_stems, route_stems,
            texture_stems, template_stems,
            guidance_stems, wage_stems,
        )


# ── Part 3b: Life Pattern Cross-Reference Validation ─────────────────

def check_life_pattern_cross_refs(report: Report):
    """Validate that Life Pattern entry/exit conditions reference
    existing triggers and patterns, and that material_life_refs,
    community_texture_refs, and trigger_refs resolve."""
    report.subsection("Life Pattern Cross-References")

    # Build lookup sets
    trigger_stems = stem_set(DIRS["core"])
    regional_stems = set()
    for k in DIRS:
        if k.startswith("regional_"):
            regional_stems |= stem_set(DIRS[k])
    all_trigger_stems = trigger_stems | regional_stems

    # Also build set of migration_ids from trigger files (some differ from filename)
    trigger_migration_ids = set()
    trigger_dirs = [("core", DIRS["core"])] + [(k, DIRS[k]) for k in DIRS if k.startswith("regional_")]
    for label, d in trigger_dirs:
        for fp in json_files_in(d):
            data = load_json(fp)
            if data and isinstance(data, dict):
                mid = data.get("migration_id", "")
                if mid:
                    trigger_migration_ids.add(mid)
            trigger_migration_ids.add(fp.stem)

    all_trigger_ids = all_trigger_stems | trigger_migration_ids

    material_life_stems = stem_set(DIRS["material_life"])
    community_texture_stems = stem_set(DIRS["community_texture"])

    # Also build material_life_ids from file contents
    material_life_ids = set()
    for fp in json_files_in(DIRS["material_life"]):
        data = load_json(fp)
        if data and isinstance(data, dict):
            mlid = data.get("material_life_id", "")
            if mlid:
                material_life_ids.add(mlid)
        material_life_ids.add(fp.stem)

    all_ml_ids = material_life_stems | material_life_ids

    # Build set of pattern_ids
    pattern_ids = set()
    for fp in json_files_in(DIRS["life_patterns"]):
        if fp.stem in LIFE_PATTERN_META_FILES:
            continue
        data = load_json(fp)
        if data and isinstance(data, dict):
            pid = data.get("pattern_id", "")
            if pid:
                pattern_ids.add(pid)
        pattern_ids.add(fp.stem)

    # Validate each life pattern
    for fp in json_files_in(DIRS["life_patterns"]):
        if fp.stem in LIFE_PATTERN_META_FILES:
            continue

        data = load_json(fp)
        if data is None:
            report.fail(f"life_patterns/{fp.name}: could not parse JSON")
            continue

        fname = f"life_patterns/{fp.name}"

        # Check entry_conditions.fed_by_triggers
        entry_conditions = data.get("entry_conditions", [])
        for ec in entry_conditions:
            if not isinstance(ec, dict):
                continue
            ec_id = ec.get("condition_id", "?")
            for tref in ec.get("fed_by_triggers", []):
                if tref in all_trigger_ids:
                    report.ok(f"{fname} entry '{ec_id}' -> trigger '{tref}'")
                else:
                    report.fail(f"{fname} entry '{ec_id}' -> trigger '{tref}' NOT FOUND")
            for pref in ec.get("fed_by_patterns", []):
                if pref in pattern_ids:
                    report.ok(f"{fname} entry '{ec_id}' -> pattern '{pref}'")
                else:
                    report.fail(f"{fname} entry '{ec_id}' -> pattern '{pref}' NOT FOUND")

        # Check exit_conditions.activates_triggers and activates_patterns
        exit_conditions = data.get("exit_conditions", [])
        for xc in exit_conditions:
            if not isinstance(xc, dict):
                continue
            xc_id = xc.get("condition_id", "?")
            for tref in xc.get("activates_triggers", []):
                if tref in all_trigger_ids:
                    report.ok(f"{fname} exit '{xc_id}' -> trigger '{tref}'")
                else:
                    report.fail(f"{fname} exit '{xc_id}' -> trigger '{tref}' NOT FOUND")
            for pref in xc.get("activates_patterns", []):
                if pref in pattern_ids:
                    report.ok(f"{fname} exit '{xc_id}' -> pattern '{pref}'")
                else:
                    report.fail(f"{fname} exit '{xc_id}' -> pattern '{pref}' NOT FOUND")

            # Validate severity is 1-5
            sev = xc.get("severity")
            if isinstance(sev, int) and 1 <= sev <= 5:
                report.ok(f"{fname} exit '{xc_id}': severity {sev} (valid 1-5)")
            elif sev is not None:
                report.warn(f"{fname} exit '{xc_id}': severity {sev} (expected 1-5)")

            # Validate generation_lag
            valid_lags = {"same_generation", "next_generation", "two_generations"}
            lag = xc.get("generation_lag", "")
            if lag in valid_lags:
                report.ok(f"{fname} exit '{xc_id}': generation_lag '{lag}' valid")
            elif lag:
                report.warn(f"{fname} exit '{xc_id}': generation_lag '{lag}' "
                            f"not in {sorted(valid_lags)}")

        # Check trigger_refs
        for tref in data.get("trigger_refs", []):
            if tref in all_trigger_ids:
                report.ok(f"{fname} trigger_ref '{tref}'")
            else:
                report.warn(f"{fname} trigger_ref '{tref}' NOT FOUND")

        # Check material_life_refs
        for mlref in data.get("material_life_refs", []):
            if mlref in all_ml_ids:
                report.ok(f"{fname} material_life_ref '{mlref}'")
            else:
                report.warn(f"{fname} material_life_ref '{mlref}' NOT FOUND")

        # Check community_texture_refs
        for ctref in data.get("community_texture_refs", []):
            if ctref in community_texture_stems:
                report.ok(f"{fname} community_texture_ref '{ctref}'")
            else:
                report.warn(f"{fname} community_texture_ref '{ctref}' NOT FOUND")


# ── Part 4: Era Overlap Validation ────────────────────────────────────

def parse_era(era_str: str) -> tuple[int | None, int | None]:
    """Parse an era string like '1910-1970' into (start, end) integers.
    Returns (None, None) for unparseable or 'All eras'-style values."""
    if not era_str or not isinstance(era_str, str):
        return (None, None)
    m = re.match(r"(\d{4})\s*[-–]\s*(\d{4})", era_str)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    return (None, None)


def eras_overlap(start_a: int, end_a: int, start_b: int, end_b: int) -> bool:
    """Return True if two era ranges overlap."""
    return start_a <= end_b and start_b <= end_a


def check_era_overlaps(report: Report):
    """Validate that trigger eras align with material_life eras.
    For each material_life trigger_ref, check that the eras overlap."""
    report.section("ERA OVERLAP VALIDATION")

    # Load all trigger eras (core + regional)
    trigger_eras = {}  # trigger_id -> (start, end)
    trigger_dirs = [("core", DIRS["core"])] + [(k, DIRS[k]) for k in DIRS if k.startswith("regional_")]
    for label, d in trigger_dirs:
        for fp in json_files_in(d):
            data = load_json(fp)
            if data is None:
                continue
            tid = data.get("migration_id", fp.stem)
            era_str = data.get("era", "")
            start, end = parse_era(era_str)
            if start is not None:
                trigger_eras[tid] = (start, end)
            # Also store by file stem if different
            if fp.stem not in trigger_eras and start is not None:
                trigger_eras[fp.stem] = (start, end)

    # Load all material_life files and check trigger_refs
    for fp in json_files_in(DIRS["material_life"]):
        data = load_json(fp)
        if data is None:
            report.fail(f"material_life/{fp.name}: could not parse JSON")
            continue

        ml_era_str = data.get("era", "")
        ml_start, ml_end = parse_era(ml_era_str)
        if ml_start is None:
            report.warn(f"material_life/{fp.name}: unparseable era '{ml_era_str}' — skipping overlap check")
            continue

        trigger_refs = data.get("trigger_refs", [])
        if not trigger_refs:
            report.info(f"material_life/{fp.name}: no trigger_refs to validate")
            continue

        for tref in trigger_refs:
            if tref not in trigger_eras:
                # Trigger has unparseable era (e.g., "All eras") or doesn't exist
                report.info(f"material_life/{fp.name} -> {tref}: trigger era not parseable or trigger not found — skipping")
                continue

            t_start, t_end = trigger_eras[tref]
            if eras_overlap(ml_start, ml_end, t_start, t_end):
                report.ok(f"material_life/{fp.name} [{ml_era_str}] <-> {tref} [{t_start}-{t_end}]: eras overlap")
            else:
                report.warn(f"material_life/{fp.name} [{ml_era_str}] <-> {tref} [{t_start}-{t_end}]: "
                            f"NO era overlap — potential temporal mismatch")


# ── Part 5: Content Depth Checks ─────────────────────────────────────

def check_content_depth(report: Report):
    """Validate that key content fields are substantive, not placeholder-thin."""
    report.section("CONTENT DEPTH CHECKS")

    # ── Trigger depth (core + regional) ──────────────────────────────
    report.subsection("Trigger Content Depth")
    trigger_dirs = [("core", DIRS["core"])] + [(k, DIRS[k]) for k in DIRS if k.startswith("regional_")]
    for label, d in trigger_dirs:
        for fp in json_files_in(d):
            data = load_json(fp)
            if data is None:
                continue

            fname = f"{label}/{fp.name}"

            # push_factors: at least 2
            pf = data.get("push_factors", [])
            pf_count = len(pf) if isinstance(pf, list) else 0
            if pf_count >= 2:
                report.ok(f"{fname}: {pf_count} push_factors")
            else:
                report.warn(f"{fname}: only {pf_count} push_factor(s) (minimum 2)")

            # pull_factors: at least 1
            plf = data.get("pull_factors", [])
            plf_count = len(plf) if isinstance(plf, list) else 0
            if plf_count >= 1:
                report.ok(f"{fname}: {plf_count} pull_factor(s)")
            else:
                report.warn(f"{fname}: only {plf_count} pull_factor(s) (minimum 1)")

            # counter_narratives: at least 2
            cn = data.get("counter_narratives", [])
            cn_count = len(cn) if isinstance(cn, list) else 0
            if cn_count >= 2:
                report.ok(f"{fname}: {cn_count} counter_narratives")
            else:
                report.warn(f"{fname}: only {cn_count} counter_narrative(s) (minimum 2)")

            # record_implications: list with at least 3 entries, or dict with at least 2 keys
            ri = data.get("record_implications")
            if isinstance(ri, list):
                ri_count = len(ri)
                if ri_count >= 3:
                    report.ok(f"{fname}: {ri_count} record_implications entries")
                else:
                    report.warn(f"{fname}: only {ri_count} record_implications entries (minimum 3)")
            elif isinstance(ri, dict):
                ri_count = len(ri)
                if ri_count >= 2:
                    report.ok(f"{fname}: {ri_count} record_implications keys")
                else:
                    report.warn(f"{fname}: only {ri_count} record_implications key(s) (minimum 2)")
            else:
                report.warn(f"{fname}: record_implications missing or unexpected type")

    # ── Destination depth ────────────────────────────────────────────
    report.subsection("Destination Content Depth")
    for fp in json_files_in(DIRS["destinations"]):
        data = load_json(fp)
        if data is None:
            continue
        fname = f"destinations/{fp.name}"

        # neighborhoods: at least 2
        nb = data.get("neighborhoods", [])
        nb_count = len(nb) if isinstance(nb, list) else 0
        if nb_count >= 2:
            report.ok(f"{fname}: {nb_count} neighborhoods")
        else:
            report.warn(f"{fname}: only {nb_count} neighborhood(s) (minimum 2)")

        # major_employers: at least 2
        me = data.get("major_employers", [])
        me_count = len(me) if isinstance(me, list) else 0
        if me_count >= 2:
            report.ok(f"{fname}: {me_count} major_employers")
        else:
            report.warn(f"{fname}: only {me_count} major_employer(s) (minimum 2)")

    # ── Occupation depth ─────────────────────────────────────────────
    report.subsection("Occupation Content Depth")
    for fp in json_files_in(DIRS["occupations"]):
        data = load_json(fp)
        if data is None:
            continue
        fname = f"occupations/{fp.name}"

        # counter_narratives: at least 2
        cn = data.get("counter_narratives", [])
        cn_count = len(cn) if isinstance(cn, list) else 0
        if cn_count >= 2:
            report.ok(f"{fname}: {cn_count} counter_narratives")
        else:
            report.warn(f"{fname}: only {cn_count} counter_narrative(s) (minimum 2)")

    # ── Material life section depth ──────────────────────────────────
    report.subsection("Material Life Section Depth")
    for fp in json_files_in(DIRS["material_life"]):
        data = load_json(fp)
        if data is None:
            continue
        fname = f"material_life/{fp.name}"

        sections = data.get("sections", {})
        if not isinstance(sections, dict):
            report.warn(f"{fname}: 'sections' is not a dict — cannot check depth")
            continue

        for sec_name, sec_data in sections.items():
            if not isinstance(sec_data, dict):
                continue
            details = sec_data.get("details", [])
            detail_count = len(details) if isinstance(details, list) else 0
            if detail_count >= 2:
                report.ok(f"{fname} -> {sec_name}: {detail_count} detail items")
            else:
                report.warn(f"{fname} -> {sec_name}: only {detail_count} detail item(s) (minimum 2)")

    # ── Life pattern content depth ───────────────────────────────────
    report.subsection("Life Pattern Content Depth")
    for fp in json_files_in(DIRS["life_patterns"]):
        if fp.stem in LIFE_PATTERN_META_FILES:
            continue
        data = load_json(fp)
        if data is None:
            continue
        fname = f"life_patterns/{fp.name}"

        # entry_conditions: at least 1
        ec = data.get("entry_conditions", [])
        ec_count = len(ec) if isinstance(ec, list) else 0
        if ec_count >= 1:
            report.ok(f"{fname}: {ec_count} entry_conditions")
        else:
            report.warn(f"{fname}: no entry_conditions (minimum 1)")

        # exit_conditions: at least 1
        xc = data.get("exit_conditions", [])
        xc_count = len(xc) if isinstance(xc, list) else 0
        if xc_count >= 1:
            report.ok(f"{fname}: {xc_count} exit_conditions")
        else:
            report.warn(f"{fname}: no exit_conditions (minimum 1)")

        # counter_narratives: at least 2
        cn = data.get("counter_narratives", [])
        cn_count = len(cn) if isinstance(cn, list) else 0
        if cn_count >= 2:
            report.ok(f"{fname}: {cn_count} counter_narratives")
        else:
            report.warn(f"{fname}: only {cn_count} counter_narrative(s) (minimum 2)")

        # chain_examples: at least 2
        ce = data.get("chain_examples", [])
        ce_count = len(ce) if isinstance(ce, list) else 0
        if ce_count >= 2:
            report.ok(f"{fname}: {ce_count} chain_examples")
        else:
            report.warn(f"{fname}: only {ce_count} chain_example(s) (minimum 2)")

        # daily_life.details: at least 2
        dl = data.get("daily_life", {})
        if isinstance(dl, dict):
            dl_details = dl.get("details", [])
            dl_count = len(dl_details) if isinstance(dl_details, list) else 0
            if dl_count >= 2:
                report.ok(f"{fname} daily_life: {dl_count} detail items")
            else:
                report.warn(f"{fname} daily_life: only {dl_count} detail item(s) (minimum 2)")


# ── Part 6: Source Reference Depth ───────────────────────────────────

def check_source_depth(report: Report):
    """Validate that source_references entries contain enough detail
    to be verifiable — not just placeholder stubs."""
    report.section("SOURCE REFERENCE DEPTH")

    all_dirs = [
        ("core",              DIRS["core"]),
        ("destinations",      DIRS["destinations"]),
        ("occupations",       DIRS["occupations"]),
        ("routes",            DIRS["routes"]),
        ("community_texture", DIRS["community_texture"]),
        ("material_life",     DIRS["material_life"]),
        ("life_patterns",     DIRS["life_patterns"]),
    ]
    # Include regional dirs
    for k in sorted(DIRS.keys()):
        if k.startswith("regional_"):
            all_dirs.append((k, DIRS[k]))

    for label, d in all_dirs:
        for fp in json_files_in(d):
            # Skip metadata files in life_patterns
            if label == "life_patterns" and fp.stem in LIFE_PATTERN_META_FILES:
                continue

            data = load_json(fp)
            if data is None:
                continue

            refs = data.get("source_references", [])
            if not isinstance(refs, list) or not refs:
                continue  # Already checked in source quality section

            fname = f"{label}/{fp.name}"
            vague_refs = []

            for i, ref in enumerate(refs):
                if isinstance(ref, str):
                    if len(ref) < 20:
                        vague_refs.append(f"  ref[{i}]: \"{ref}\" ({len(ref)} chars)")
                elif isinstance(ref, dict):
                    has_author = bool(ref.get("author"))
                    has_title = bool(ref.get("title"))
                    # Also accept 'citation' field (full citation string format)
                    has_citation = bool(ref.get("citation"))
                    if not has_author and not has_title and not has_citation:
                        snippet = json.dumps(ref)[:80]
                        vague_refs.append(f"  ref[{i}]: missing author, title, and citation: {snippet}")

            if vague_refs:
                report.warn(f"{fname}: {len(vague_refs)} vague source reference(s):")
                for vr in vague_refs:
                    report.info(vr)
            else:
                report.ok(f"{fname}: all {len(refs)} source references have adequate detail")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    report = Report()

    print("KinLore Narrative Enrichment Layer — Cross-Reference Validation")
    print(f"Base directory: {BASE}")
    print(f"{'=' * 60}")

    if not BASE.is_dir():
        print(f"ERROR: Base directory does not exist: {BASE}")
        sys.exit(1)

    # Part 1
    check_file_inventory(report)

    # Part 2: Cross-Reference Validation
    report.section("CROSS-REFERENCE VALIDATION")
    check_trigger_route_refs(report)
    check_trigger_destination_refs(report)
    check_community_trigger_refs(report)

    # Part 3b: Life Pattern Cross-References
    report.section("LIFE PATTERN CROSS-REFERENCES")
    check_life_pattern_cross_refs(report)

    # Part 2 continued: Schema Consistency
    report.section("SCHEMA CONSISTENCY")
    check_schema_consistency(report)
    check_required_fields(report)

    # Part 2 continued: Source Quality
    report.section("SOURCE QUALITY")
    check_source_quality(report)

    # Part 2 continued: Narrative Hooks
    report.section("NARRATIVE HOOK VARIABLES")
    check_narrative_hooks(report)

    # Part 4: Era Overlap Validation
    check_era_overlaps(report)

    # Part 5: Content Depth Checks
    check_content_depth(report)

    # Part 6: Source Reference Depth
    check_source_depth(report)

    # Part 7: Integration Stress Tests
    run_stress_tests(report)

    # Print everything
    report.print_all()
    report.print_summary()

    # Exit code
    sys.exit(1 if report.failed > 0 else 0)


if __name__ == "__main__":
    main()
