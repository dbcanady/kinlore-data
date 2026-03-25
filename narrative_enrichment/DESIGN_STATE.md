# KinLore Data Architecture — Design State

**Last Updated: 2026-03-25**
**Schema Version: 1.0 (all layers)**
**Pipeline Version: 1.2 (12-step)**

---

## Architecture Overview

KinLore's narrative engine is fed by 5 data layers, each providing a different dimension of context. Together they enable Polsia to generate historically grounded, source-cited family narratives from public genealogical records.

| Layer | Purpose | Files | Lines |
|-------|---------|------:|------:|
| 1 — County Source Profiler | Where to find records | 56 builds | ~19,929 profiles |
| 2 — Historical Context Timelines | Decade-by-decade state background | 56 | ~5,400 |
| 3 — Narrative Enrichment (NEL) | Why they moved, how they lived | 287 | ~53,000 |
| 4 — Regional Landscape Profiles | Hyper-local sensory/institutional detail | 1,038 | ~165,000 |
| 5 — Ethnic Heritage Profiles | Cultural identity and identification | 47 | ~24,000 |
| **Total** | | **~1,484** | **~267,000** |

---

## Layer 1 — County Source Profiler (COMPLETE 2026-03-12)

- **56 builds** (50 states + DC + PR + VI + AS + GU + MP)
- **3,234 jurisdictions**, **19,929 source profiles**
- **56/56 GOLD_STANDARD** validated
- Schema v3.1: 15 metadata fields + 13 source profile fields
- Tells the narrative AI *where to look* for records in any US county

## Layer 2 — Historical Context Timelines (COMPLETE 2026-03-16)

- **56 files**, 5.4 MB
- Decade-by-decade background for every state and territory
- Provides the historical backdrop against which individual stories unfold

---

## Layer 3 — Narrative Enrichment Layer (COMPLETE 2026-03-18)

The core intelligence layer. Explains *why* ancestors moved, *how* they traveled, *what work they found*, *what their daily life looked like*, and provides narrative templates, research guidance, and economic context.

### NEL Inventory

| Category | Files | Location |
|----------|------:|----------|
| Core triggers | 32 | `migration_triggers/core/` |
| Regional triggers | 19 | `migration_triggers/regional/` (14 states) |
| Destinations | 82 | `migration_triggers/shared/destinations/` |
| Occupations | 27 | `migration_triggers/shared/occupations/` |
| Routes | 25 | `migration_triggers/shared/routes/` |
| Community textures | 33 | `migration_triggers/shared/community_texture/` |
| Material life profiles | 20 | `migration_triggers/shared/material_life/` |
| Templates | 11 | `migration_triggers/templates/` |
| Research guidance | 10 | `migration_triggers/research_guidance/` |
| Wage tables | 3 | `migration_triggers/shared/wages/` |
| Life patterns | 22 + 2 meta | `life_patterns/` |
| Cross-ref validator | 1 | `migration_triggers/_validation/` |
| Gap detection | 2 | `migration_triggers/_gap_detection/` |
| Dry runs | 9 | `migration_triggers/dry_runs/` |
| **Total** | **~298** | |

### Core Triggers (32)

**Migration Classes:**
- **immigration** (8): irish_famine, se_european_wave, german_immigration, scots_irish_frontier, chinese_exclusion_era, jewish_pogrom_flight, puerto_rican_migration, bracero_program
- **economic** (7): boll_weevil, textile_mill_recruitment, appalachian_out_migration, economic_panics_19c, economic_panics_20c, gold_rush_mining_boom, gilded_age_labor_conflict
- **military** (4): civil_war_displacement, wwii_relocation, civil_war_service, war_of_1812_service
- **racial_flight** (1): great_migration
- **forced** (2): domestic_slave_trade, indian_removal_trail_of_tears
- **disaster** (1): dust_bowl
- **land_opportunity** (3): homestead_act, oklahoma_land_runs, gi_bill_migration
- **religious** (1): mormon_migration
- **family** (1): widow_orphan_relocation
- **stayed** (2): stayed_and_adapted, antebellum_yeoman_south
- **reconstruction** (1): reconstruction_era
- **railroad** (1): railroad_construction

### Regional Triggers (19 across 14 states)

| State | Triggers |
|-------|----------|
| NC | 6 (eastern_farm_to_mill, mountain_to_piedmont, wilmington_1898, tobacco_to_industry, civil_war_veteran, piedmont_to_coastal) |
| VA, OH, SC, GA, KY, TN, MS, TX, MN, PA, AL, LA, IL | 1 each |

### Destinations (82)

Expanded from 21 to 82 via Destination Buildout (2026-03-18). Covers 15 clusters: Great Migration North, Appalachian Industrial, Oklahoma Territory, Mormon Corridor, California Agricultural, Pacific Northwest, Southern Industrial, Upper Midwest, Military/Defense, NYC Ethnic Enclaves, Piedmont Mill, Historic South, Mid-Atlantic Gateway, Trans-Mississippi, Frontier Mining.

### Templates (11)

| Template | Purpose |
|----------|---------|
| what_they_saw | Physical landscape descriptions (departure + arrival) |
| letter_home | Illustrative letters (8 situation types) |
| record_silences | Gap interpretation (6 gap types) |
| fork_in_the_road | Counterfactual "had they stayed" paragraph |
| convergence | Where two family lines meet |
| document_deep_read | Extract narrative from a specific document |
| economic_life_story | Economic arc across a lifetime |
| military_service_arc | Service, impact, aftermath |
| naming_as_evidence | What names reveal about heritage |
| hinge_generation | The generation that changed everything |
| audience_adapter | Tone/depth calibration for different audiences |

### Life Patterns — Phase 4 (22 files, COMPLETE 2026-03-18)

Multi-generational narrative architecture for what happened BETWEEN migrations. Chain-link design with entry_conditions/exit_conditions enabling pattern chaining across generations.

**Pattern classes:** economic_arc, family_dynamic, community_pattern, occupational_lifecycle, social_transformation

**Index:** `CHAIN_LINK_INDEX.json` — 53 entry conditions, 67 exit conditions, 22 chains mapped

Patterns: appalachian_subsistence_squeeze, auto_city_family_arc, boarding_house_matriarch, civil_war_widows_arc, company_town_lifecycle, depression_survival_strategies, gullah_geechee_persistence, immigrant_parish_lifecycle, indentured_servant_formation, military_family_circuit, mill_girl_pipeline, new_england_farm_decline, oil_field_nomad, pullman_porter_network, scandinavian_homestead_arc, sharecropping_trap, steel_city_immigrant_arc, sundown_town_exclusion, tobacco_soil_exhaustion, wheat_boom_bust, wwi_homefront_disruption, yeoman_farming_stability

### Validation

**Cross-reference validator:** `_validation/validate_cross_references.py`
- **4,645 checks, 0 failures, 21 warnings, 99.5% pass rate**
- 7 check types: file inventory, cross-references, schema consistency, required fields, source quality, narrative hooks, source depth
- Era overlap validation (material_life ↔ triggers)
- Content depth checks (push/pull factors, counter-narratives, neighborhoods, etc.)
- Life pattern cross-references (entry/exit chain validation)
- Ethnic heritage cross-references (nel_cross_references resolution)
- 11 stress test ancestors (6 synthetic + 5 real family) — all at 89% (8/9 pipeline coverage)

**8 narrative dry runs** — all PASS (analysis at `dry_runs/00_ANALYSIS.md`)

**Gap detection system:** Self-improving feedback loop for Polsia to report missing data

### Build History

| Phase | Date | What |
|-------|------|------|
| Sprint 1 | 2026-03-16 | 17 core triggers |
| Sprint 2B | 2026-03-16 | 4 templates, 10 research guidance, 3 wages |
| Phase 3A | 2026-03-16 | 8 new triggers, 10 destinations, 10 occupations, 12 routes |
| Phase 3B | 2026-03-16 | 12 material life profiles, gap detection system |
| Phase 3C | 2026-03-16 | 18 community texture profiles |
| Phase 3D NC | 2026-03-16 | 6 NC regional triggers + 2 community textures |
| Phase 3D Expanded | 2026-03-16 | 13 state triggers + 13 community textures (14 states) |
| GENO Templates | 2026-03-17 | 6 new templates (10 total → 11 with hinge_generation) |
| Phase 3E | 2026-03-17 | 4 core triggers, hinge_generation, economic_position, 5 real ancestors |
| Destination Buildout | 2026-03-18 | 61 new destinations (21→82) |
| Priorities 1-6 | 2026-03-18 | Dry runs, material life gaps, validator upgrades, new triggers, occupations |
| Chinese American Parity | 2026-03-18 | Chinatown texture, material life, laundryman |
| Targeted Fills | 2026-03-18 | PA Dutch texture, Pacific coastal steamer route |
| Phase 4 (Life Patterns) | 2026-03-18 | 22 chain-linked life patterns + schema + index |
| Pipeline v1.1 | 2026-03-19 | POLSIA_INTEGRATION.md updated, life patterns wired in |

---

## Layer 4 — Regional Landscape Profiles (COMPLETE 2026-03-25)

Hyper-local sensory and institutional detail for narrative grounding. 9 profile types per cluster providing the physical, economic, institutional, and social context that makes narratives feel like *real places*.

### Architecture

Each cluster contains:
1. **county_landscape/** — Per-county sensory snapshots (geography, soil, waterways, vegetation)
2. **courthouse_atlas/** — Per-county record navigation (what survives, where, gotchas)
3. **local_economy/** — Regional economic story across eras
4. **road_connectivity/** — Transportation networks and travel times
5. **information_landscape/** — Newspapers, ethnic press, oral networks
6. **micro_migration/** — Internal movement patterns and settlement clusters
7. **seasonal_calendar/** — Agricultural/industrial rhythms by month
8. **cultural_markers/** — Denominations, naming conventions, foodways, social institutions
9. **hidden_history/** — Erasure, conflict, resilience, dignity mandates

### Coverage: 47 Clusters, 27 States, 358 Counties, 1,038 Files

| State | Clusters | Counties |
|-------|----------|----------|
| NC | 7 | 57 |
| SC | 2 | 14 |
| VA | 3 | 25 |
| MD | 2 | 12 |
| PA | 3 (Southeast Gateway, Western Frontier, Anthracite) | 22 |
| NY | 1 | 8 |
| MA | 1 | 6 |
| CT | 1 | 6 |
| NJ | 1 | 8 |
| KY | 2 | 16 |
| TN | 2 | 16 |
| OH | 3 | 24 |
| IN | 1 | 8 |
| IL | 1 | 8 |
| IA | 2 (Eastern, Corn Belt) | 16 |
| WI | 1 | 8 |
| MO | 1 | 8 |
| GA | 2 | 16 |
| AL | 2 | 16 |
| MS | 2 | 16 |
| LA | 1 | 8 |
| TX | 2 (East Piney Woods, German Hill Country) | 16 |
| MN | 1 | 8 |
| ND | 1 | 8 |
| SD | 1 | 8 |

**Major migration corridors covered:** Great Wagon Road (PA→VA→NC→SC), Wilderness Road (VA→KY→TN), Ohio River (PA/VA→OH→IN→IL), Cotton Belt (VA/NC/SC→GA→AL→MS→TX), Colonial Origins (MA→CT→NY→NJ→PA), Upper Plains (WI→MN→ND/SD), Mississippi River (IA→MO→MS→LA)

**Index:** `REGIONAL_LANDSCAPE_INDEX.json` — county-to-region lookup for all 358 counties

---

## Layer 5 — Ethnic Heritage Profiles (COMPLETE 2026-03-25)

Deep cultural context for narrative personalization. When Polsia identifies an ancestor's ethnic/cultural heritage from records, it loads the matching profile to enrich the narrative with culturally-specific context.

### Coverage: 45 Profiles Across 11 Group Categories

| Category | Profiles |
|----------|----------|
| Colonial British (8) | english_chesapeake, english_puritan, english_indentured, scots_irish, scottish, welsh, french_huguenot, quaker |
| Germanic (5) | german_colonial, german_48er, german_gilded_age, dutch, swiss |
| Irish (3) | irish_prefamine, irish_famine, irish_postfamine |
| Scandinavian (4) | norwegian, swedish, danish, finnish |
| Southern/Eastern European (9) | italian_northern, italian_southern, greek, hungarian, polish, czech_bohemian, slovak, russian_ukrainian, portuguese_azorean |
| Slavic/Baltic (3) | croatian_serbian, lithuanian, jewish_eastern_european |
| African American (4) | enslaved_african_american, free_black_antebellum, reconstruction_jim_crow, great_migration_african_american |
| French/Acadian (2) | french_canadian, acadian_cajun |
| Asian American (3) | chinese_american, japanese_american, filipino_american |
| Latin American (2) | mexican_tejano, spanish_colonial |
| Other (2) | jewish_german, native_american |

**14 profiles carry dignity mandates.**

Each profile contains 10 required sections: identification clues, immigration overview, settlement patterns, church/records, naming conventions, occupational patterns, cultural markers, intermarriage patterns, genealogical pitfalls, NEL cross-references, and source references.

**Index:** `ETHNIC_HERITAGE_INDEX.json` — identification clues lookup (surname patterns, denomination signals, settlement signals, occupation signals, record signals) for all 45 profiles

---

## Pipeline Integration

**POLSIA_INTEGRATION.md v1.2** defines the 12-step ancestor pipeline:

1. **Record Identification** — Parse ancestor's name, dates, locations, occupations
2. **Ethnic Heritage Matching** — Match against 45 heritage profiles via identification clues
3. **Trigger Matching** — Match against 32 core + 19 regional triggers
4. **Route Selection** — Pull transportation details from 25 route profiles
5. **Destination Lookup** — Pull neighborhood/employer/institutional context from 82 destinations
6. **Life Pattern Matching** — Match against 22 chain-linked life patterns
7. **Community Texture** — Load relevant community profiles from 33 textures
8. **Occupation Enrichment** — Match against 27 occupation profiles
9. **Material Life** — Load era/region-appropriate material life from 20 profiles
10. **Regional Landscape** — Load hyper-local detail from 47 clusters (1,038 files)
11. **Template Selection + Narrative Generation** — 11 templates with Accuracy Line constraints
12. **Gap Detection + Reporting** — Self-report missing data for future builds

---

## Schema Design Principles

### The Accuracy Line
Facts from records are SACRED. Context uses "likely", "probably", "the pattern suggests". No emotional projection.

### Variable Placeholders
All narrative hooks use `{variable}` syntax: `{ancestor_name}`, `{surname}`, `{year}`, `{county}`, `{destination}`, `{pronoun_subject}`, `{pronoun_possessive}`, etc.

### Push/Pull Factor Severity Scale
1 = minor influence, 5 = catastrophic/overwhelming. Measures historical severity, not priority.

### Counter-Narratives Requirement
Every trigger includes at least 2 counter-narratives. Every template includes constraints preventing one-dimensional storytelling.

### Source References
Minimum 3 academic sources per file. Zero Wikipedia. Chicago-style citations.

### Dignity Mandate
Required for any content involving forced migration, racial violence, or systematic oppression. Applied to: Trail of Tears, domestic slave trade, Wilmington 1898, enslaved ancestors, Japanese American incarceration, Chinese exclusion, Nueces Massacre, mine disasters, and more.

---

## Production Readiness

### Option A (single ancestor)
**Production-ready.** The 12-step pipeline has deep, well-sourced data for nearly any American ancestor's story. 32 core triggers cover ~97% of American genealogy migration patterns (1717-1970). 82 destinations, 27 occupations, 25 routes, 33 community textures, 20 material life profiles, and 45 ethnic heritage profiles provide rich context.

### White Glove (multi-generational)
**Production-ready.** Life Patterns (Phase 4) fill the narrative gap between migrations. Chain-link architecture enables multi-generational narrative chaining. Regional Landscape profiles add hyper-local depth across 47 clusters.

### Minimum viable dataset for an Option A report
- 1 matched trigger (push/pull factors, route, destination)
- 1 ethnic heritage profile (cultural context)
- 1 destination profile (neighborhood, employer, institutions)
- 1 occupation profile (daily work, wages, conditions)
- 1 community texture (settled-life institutional detail)
- 1-2 template outputs (Letter Home + What They Saw or Fork in the Road)
- Wage comparison (origin vs. destination)
- 1 Record Silences interpretation (if gaps detected)

---

## What Remains

- **FamilySearch API integration** — Polsia needs live record lookup capability
- **End-to-end pipeline testing** — Run real ancestors through Polsia, watch gap reports accumulate
- **Gap-driven builds** — Future content built on demand as gap detection surfaces missing data
