# KinLore Data Repository

County-level genealogical source profiles for all US states and territories. This data feeds the KinLore.ai narrative generation agent.

## Stats
- **56 builds** (50 states + DC + Puerto Rico + US Virgin Islands + American Samoa + Guam + Northern Mariana Islands)
- **3,234 jurisdictions** profiled
- **19,929 source profiles** created
- **56/56 GOLD_STANDARD** validated (8/8 checks passed for every build)
- **Schema version:** 3.1

## Directory Structure

```
data/
  {state_name}/              # lowercase, underscores for spaces
    manifest.json            # schema_version, county counts, batch list
    rundown_00_statewide.json  # state-level repositories and resources
    rundown_01_*.json        # county batch (flat JSON array)
    rundown_02_*.json        # ...
    ...
validation/
  validation_{ST}_v1.1.json  # 8-check validation report per state
```

## Schema (v3.1)

### County Metadata (15 fields)
state, county, fips_code, formed_year, parent_county, grandparent_county, county_seat, is_burned_county, record_losses, jurisdictional_notes, research_tips, online_land_records_url, online_land_records_earliest_year, online_land_records_scope, heritage_book

### Source Profile (13 fields)
state, county, record_type, source_name, repository, access_method, url, year_start, year_end, coverage_notes, survival_notes, kinlore_priority, programmatic_access

### Priority Scale (1-3)
- **1** = Check first. Free, digitized, indexed. (20-30% of sources)
- **2** = Moderate value. Digitized or well-documented. (50-60%)
- **3** = Supplementary. In-person, fragmentary. (15-25%)

### Batch File Format
Batch files are **flat JSON arrays** (not wrapped in objects):
```json
[
  { "county_metadata": { ... }, "source_profiles": [ ... ] },
  { "county_metadata": { ... }, "source_profiles": [ ... ] }
]
```

### Statewide File Format
Statewide files are **dict objects** with categorized sources:
```json
{
  "scope": "statewide",
  "state": "XX",
  "categories": {
    "core_repositories": [ ... ],
    "familysearch_collections": [ ... ],
    ...
  }
}
```

## For Polsia Engineering Agent

Each state directory is a self-contained migration unit. To migrate a state:
1. Read `manifest.json` for county count and batch file list
2. Read `rundown_00_statewide.json` for state-level resources
3. Read all `rundown_01_*.json` through `rundown_XX_*.json` for county data
4. Create migration file and import into Neon Postgres

All data has been validated against Census Bureau FIPS codes. Every county name and FIPS code matches federal reference data.
