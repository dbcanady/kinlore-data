# Narrative Enrichment Layer — Design State

**Sprint 1 Complete: 2026-03-16**
**Schema Version: 1.0**

## What Was Built

Sprint 1 delivers the **Migration Decision Trees** — machine-readable data that lets KinLore's narrative AI explain *why* an ancestor moved, *how* they got there, *what work they found*, and *what the destination looked like when they arrived*.

### Inventory

| Category | Files | Total Lines | Location |
|----------|------:|------------:|----------|
| Core triggers | 17 | 3,495 | `migration_triggers/core/` |
| Routes | 8 | 429 | `migration_triggers/shared/routes/` |
| Destinations | 11 | 1,494 | `migration_triggers/shared/destinations/` |
| Occupations | 10 | 1,035 | `migration_triggers/shared/occupations/` |
| Stress tests | 1 (7 tests) | 211 | `migration_triggers/_validation/` |
| **Total** | **47** | **6,664** | |

All 47 files are valid JSON. Schema version 1.0 throughout.

## Core Triggers (17 files)

Each trigger entry documents a specific historical migration pattern with phases, push/pull factors (severity 1-5), transportation details with route_refs, chain migration patterns with gender_pattern, destination_refs, record implications for genealogical research, counter-narratives, and academic source references.

| Trigger | Era | Class | Lines |
|---------|-----|-------|------:|
| irish_famine | 1845-1860 | immigration | 283 |
| great_migration | 1910-1970 | racial_flight | 248 |
| se_european_wave | 1880-1924 | immigration | 247 |
| german_immigration | 1848-1890 | immigration | 237 |
| scots_irish_frontier | 1717-1800 | immigration | 236 |
| boll_weevil | 1892-1930 | economic | 222 |
| wwii_relocation | 1940-1947 | military | 216 |
| civil_war_displacement | 1861-1865 | military | 209 |
| domestic_slave_trade | 1790-1860 | forced | 200 |
| appalachian_out_migration | 1940-1970 | economic | 197 |
| economic_panics_19c | 1837-1907 | economic | 186 |
| economic_panics_20c | 1929-1940 | economic | 185 |
| railroad_construction | 1850-1890 | economic | 173 |
| homestead_act | 1862-1934 | land_opportunity | 169 |
| dust_bowl | 1930-1940 | disaster | 168 |
| textile_mill_recruitment | 1880-1940 | economic | 164 |
| widow_orphan_relocation | All eras | family | 155 |

### Migration Classes
- **immigration** (4): Transatlantic/transoceanic arrivals
- **economic** (5): Driven by economic forces — wages, mechanization, panics
- **military** (2): War-related displacement and relocation
- **racial_flight** (1): Fleeing racial violence and Jim Crow
- **forced** (1): Enslaved people moved against their will
- **disaster** (1): Environmental catastrophe
- **land_opportunity** (1): Free/cheap land pull
- **family** (1): Kinship obligation (widows, orphans)

## Routes (8 files)

| Route | Type | Era |
|-------|------|-----|
| illinois_central | railroad | 1856-1970 |
| pennsylvania_railroad | railroad | 1846-1968 |
| louisville_nashville | railroad | 1859-1982 |
| southern_pacific | railroad | 1876-1996 |
| route_66 | highway | 1926-1985 |
| great_wagon_road | wagon_road | 1740-1810 |
| atlantic_crossing_famine | sea_route | 1845-1855 |
| atlantic_crossing_steerage | sea_route | 1855-1924 |

## Destinations (11 files)

Chicago, Detroit, New York City, Philadelphia, Pittsburgh, Los Angeles, Cleveland, St. Louis, San Francisco, Baltimore, Boston.

Each profile includes neighborhoods (3-4 per city with ethnic group, era, character), major employers (3-4 with wages and working conditions), churches and mutual aid societies (2-3 with records available), housing patterns, anti-immigrant reception, and source references. 103 total narrative hooks with {variable} placeholders.

## Occupations (10 files)

Sharecropper, tenant farmer, meatpacking worker, coal miner, textile mill hand, railroad laborer, steelworker, domestic servant, auto worker, general farmer (Midwest).

Each profile includes daily work description, seasonal cycle, economics with real historical wage data, working conditions, why they left, records generated (with research tips), census clues, cultural context, and counter-narratives.

## Stress Tests (7 scenarios)

| Test | Ancestor | Trigger | Result |
|------|----------|---------|--------|
| #1 | James Edward Harris | great_migration | PASS |
| #2 | Bridget Connolly | irish_famine | PASS |
| #3 | Elmer Dawson | dust_bowl | PASS |
| #4 | Sarah Whitfield | appalachian_out_migration | PASS |
| #5 (stretch) | Solomon | domestic_slave_trade | PASS |
| #6 (stretch) | Robert McBride | scots_irish_frontier | PASS |
| #7 (stretch) | Mary Thompson | widow_orphan_relocation | PASS |

Each stress test takes a fictional ancestor profile, maps it against a specific trigger file, and generates a 200-350 word sample narrative using only data present in the trigger, route, and destination files. All narratives respect the Accuracy Line.

## Schema Design Decisions

### The Accuracy Line
Facts from records are SACRED. Context uses "likely", "probably", "the pattern suggests". No emotional projection. "{ancestor_name} likely left because the mines were closing" is acceptable. "{ancestor_name} felt heartbroken to leave" is not.

### Variable Placeholders
All narrative hooks use `{variable}` syntax: `{ancestor_name}`, `{surname}`, `{given_name}`, `{year}`, `{county}`, `{destination}`, `{origin_county}`, etc. The narrative AI populates these from the ancestor's actual records.

### Push/Pull Factor Severity Scale
1 = minor influence, 5 = catastrophic/overwhelming. This is NOT a priority scale — it measures historical severity of the force acting on the population.

### Counter-Narratives Requirement
Every trigger must include at least 2 counter-narratives — facts that complicate the default story. This prevents the narrative AI from producing one-dimensional accounts.

### Source References
Minimum 3 academic sources per trigger, destination, and occupation. Zero Wikipedia. All references are published books or journal articles from recognized historians.

## What Is NOT Built (Deferred)

### Track B — Life Patterns (deferred to $99 tier)
The Narrative Strains document (~100 patterns) contains ~20 non-migration patterns: Boarding House Matriarch, Sharecropping Trap, Domestic Service arc. These are "Life Patterns" — what happened between migrations. Essential for multi-generational $99 reports. Not needed for single-ancestor $29 reports.

### Placeholder directories (Sprint 2+)
- `deep_dives/` — Extended narratives for specific triggers
- `templates/` — Narrative generation templates
- `research_guidance/` — User-facing research tips
- `shared/wages/` — Historical wage comparison tables

## How This Data Gets Used

1. **Polsia receives an ancestor record** (name, dates, locations, occupations)
2. **Trigger matching**: Compare ancestor's origin county, era, occupation, and race against the 17 trigger files. Multiple triggers may match.
3. **Route selection**: Use the trigger's `route_refs` to pull transportation details
4. **Destination lookup**: Use the trigger's `destination_refs` to pull neighborhood, employer, and institutional context
5. **Occupation enrichment**: Match ancestor's listed occupation against the 10 occupation profiles for daily life detail
6. **Narrative generation**: Feed matched trigger data + route + destination + occupation into the narrative AI with the Accuracy Line constraints
7. **Counter-narrative injection**: Include at least one counter-narrative per trigger to prevent one-dimensional storytelling

## Relationship to Other Data Layers

- **Layer 1 — County Source Profiler** (COMPLETE, 56 builds, 19,929 profiles): Tells the narrative AI *where to look* for records in each county
- **Layer 2 — Historical Context Timelines** (COMPLETE, 56 files): Provides decade-by-decade background for every state
- **Layer 3 — Migration Decision Trees** (THIS SPRINT): Explains *why* people moved, *how* they traveled, *what they found*
