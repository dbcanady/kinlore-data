# Narrative Enrichment Layer — Design State

**Sprint 1 Complete: 2026-03-16**
**Sprint 2B Complete: 2026-03-16**
**Phase 3A Complete: 2026-03-16**
**Phase 3C Complete: 2026-03-16**
**Phase 3D (NC): 2026-03-16**
**Phase 3D Expanded (14 states): 2026-03-16**
**Phase 3B Complete: 2026-03-16**
**Schema Version: 1.0**

## What Was Built

### Sprint 1 — Migration Decision Trees
Machine-readable data that lets KinLore's narrative AI explain *why* an ancestor moved, *how* they got there, *what work they found*, and *what the destination looked like when they arrived*.

### Sprint 2B — Templates, Research Guidance, Wage Tables, Gap Fixes
Deepens the 17 existing triggers with narrative templates, actionable research advice, historical wage data, and 5 content fixes from expert spot-check review.

### Combined Inventory

| Category | Files | Total Lines | Location |
|----------|------:|------------:|----------|
| Core triggers | 25 | ~5,800 | `migration_triggers/core/` |
| Regional triggers | 19 | ~4,500 | `migration_triggers/regional/` (14 states) |
| Routes | 24 | ~1,240 | `migration_triggers/shared/routes/` |
| Destinations | 21 | ~3,200 | `migration_triggers/shared/destinations/` |
| Occupations | 20 | ~2,100 | `migration_triggers/shared/occupations/` |
| Community textures | 31 | ~5,600 | `migration_triggers/shared/community_texture/` |
| Material life profiles | 12 | 3,001 | `migration_triggers/shared/material_life/` |
| Cross-ref validator | 1 | ~450 | `migration_triggers/_validation/` |
| Gap detection system | 2 | ~250 | `migration_triggers/_gap_detection/` |
| Templates | 10 | 2,135 | `migration_triggers/templates/` |
| Research guidance | 10 | 1,491 | `migration_triggers/research_guidance/` |
| Wage tables | 3 | 1,645 | `migration_triggers/shared/wages/` |
| **Total** | **179** | **~31,400** | |

All 179 files are valid JSON (except 2 Markdown guides). Schema version 1.0 throughout.

## Sprint 1 Spot-Check Gaps — RESOLVED

| # | Issue | File | Priority | Status |
|---|-------|------|----------|--------|
| 1 | Quebec/Grosse Île back-door route missing from record_implications | irish_famine.json | HIGH | RESOLVED — Added Canadian arrival records entry with LAC, Grosse Île Memorial, Boston Pilot 'Missing Friends' column |
| 2 | Destination counties missing for receiving end | domestic_slave_trade.json | HIGH | RESOLVED — Added `destination_counties_most_affected` array (Adams MS, Orleans Parish LA, etc.) with note |
| 3 | "Information Wanted" ads deserve own record_implications entry | domestic_slave_trade.json | MEDIUM | RESOLVED — Added entry citing Christian Recorder, SW Christian Advocate, Last Seen project at Villanova |
| 4 | Empty destination_refs, mill towns need profiles | textile_mill_recruitment.json | MEDIUM | RESOLVED — Added 4 mill_town_profiles (Kannapolis, Gastonia, Lancaster, Graniteville) with sensory_snapshot, institutions |
| 5 | involuntary: false needs coercion context | Schema-level | LOW | RESOLVED — Added optional `coercion_note` field to irish_famine.json and dust_bowl.json |

## Core Triggers (25 files)

### Original 17 (Sprints 1 + 2B)
| Trigger | Era | Class | Lines |
|---------|-----|-------|------:|
| irish_famine | 1845-1860 | immigration | 289 |
| great_migration | 1910-1970 | racial_flight | 248 |
| se_european_wave | 1880-1924 | immigration | 247 |
| german_immigration | 1848-1890 | immigration | 237 |
| scots_irish_frontier | 1717-1800 | immigration | 236 |
| boll_weevil | 1892-1930 | economic | 222 |
| domestic_slave_trade | 1790-1860 | forced | 218 |
| wwii_relocation | 1940-1947 | military | 216 |
| civil_war_displacement | 1861-1865 | military | 209 |
| textile_mill_recruitment | 1880-1940 | economic | 204 |
| appalachian_out_migration | 1940-1970 | economic | 197 |
| economic_panics_19c | 1837-1907 | economic | 186 |
| economic_panics_20c | 1929-1940 | economic | 185 |
| railroad_construction | 1850-1890 | economic | 173 |
| homestead_act | 1862-1934 | land_opportunity | 169 |
| dust_bowl | 1930-1940 | disaster | 169 |
| widow_orphan_relocation | All eras | family | 155 |

### Phase 3A New Triggers (8)
| Trigger | Era | Class | Lines |
|---------|-----|-------|------:|
| gold_rush_mining_boom | 1848-1900 | economic | ~297 |
| mormon_migration | 1830-1869 | religious | ~290 |
| oklahoma_land_runs | 1889-1907 | land_opportunity | ~305 |
| bracero_program | 1942-1964 | labor_immigration | ~285 |
| puerto_rican_migration | 1917-1970 | economic | ~299 |
| chinese_exclusion_era | 1850-1943 | immigration | ~289 |
| jewish_pogrom_flight | 1880-1924 | immigration | ~280 |
| indian_removal_trail_of_tears | 1830-1850 | forced | ~280 |

### Migration Classes (updated)
- **immigration** (7): Transatlantic/transoceanic arrivals (irish_famine, se_european_wave, german_immigration, scots_irish_frontier, chinese_exclusion_era, jewish_pogrom_flight)
- **economic** (7): Driven by economic forces — wages, mechanization, panics (boll_weevil, textile_mill_recruitment, appalachian_out_migration, economic_panics_19c, economic_panics_20c, gold_rush_mining_boom, puerto_rican_migration)
- **military** (2): War-related displacement and relocation
- **racial_flight** (1): Fleeing racial violence and Jim Crow
- **forced** (2): Moved against their will (domestic_slave_trade, indian_removal_trail_of_tears)
- **disaster** (1): Environmental catastrophe
- **land_opportunity** (2): Free/cheap land pull (homestead_act, oklahoma_land_runs)
- **religious** (1): Religious persecution and gathering (mormon_migration)
- **labor_immigration** (1): Government-managed labor migration (bracero_program)
- **family** (1): Kinship obligation (widows, orphans)

## Templates (4 files) — Sprint 2B

| Template | Lines | Situations/Variants | Revenue Tier |
|----------|------:|--------------------:|-------------|
| letter_home | 316 | 8 situations | Both (Option A short, White Glove full) |
| record_silences | 353 | 6 gap types | Both (Option A brief, White Glove expanded) |
| what_they_saw | 147 | 2 variants (departure + arrival) | Both (Option A one, White Glove both) |
| fork_in_the_road | 88 | 1 (counterfactual) | Both (Option A paragraph, White Glove with stats) |

**letter_home**: 8 situation types (arrival, family arrival, send-for-family, homesick, settled update, bad news, return visit, first job). All outputs prefixed with `[Illustrative — not from an actual letter]`. No letters for enslaved ancestors (use Record Silences instead). Voice calibration adjusts for era, region, occupation, ethnicity, literacy.

**record_silences**: 6 gap types (between censuses, woman disappears, child vanishes, complete disappearance, 1890 gap, enslaved ancestor gap). Ranked explanations with research actions. The enslaved ancestor gap section includes dignity mandate and explicit instructions to name the slaveholder. Available at both tiers: Option A gets a brief 2-sentence interpretation of the most significant gap; White Glove gets full 80-200 word treatment of all applicable gaps.

**what_they_saw**: Dense physical landscape descriptions, 100-150 words, present tense, no people. Departure landscape (the place they left) and arrival landscape (first view of destination).

**fork_in_the_road**: Counterfactual paragraph grounded in documented demographic/economic changes. "Had {ancestor_name} remained in {county}..." No individual speculation — only the place's fate.

## Research Guidance (10 files) — Sprint 2B

| File | Patterns | Source Refs |
|------|:--------:|:----------:|
| census_gaps | 8 | 5 |
| city_directory_strategies | 6 | 4 |
| church_record_transfers | 7 | 7 |
| vital_record_variations | 7 | 4 |
| name_change_patterns | 7 | 5 |
| military_record_strategies | 7 | 5 |
| newspaper_strategies | 6 | 5 |
| property_record_strategies | 6 | 5 |
| institutional_records | 7 | 5 |
| ethnic_specific_sources | 9 | 5 |
| **Total** | **70 patterns** | **50 refs** |

Every action step names the repository, record group, and access method. Common mistakes called out per pattern. Era-scoped to prevent anachronistic advice.

## Wage and Cost-of-Living Tables (3 files) — Sprint 2B

| File | Lines | Entries | Benchmarks |
|------|------:|--------:|-----------:|
| wages_1850_1900 | 448 | 33 | 20 |
| wages_1900_1950 | 473 | 35 | 21 |
| cost_of_living | 724 | — | 102 |

Key comparison surfaced: Southern sharecropper ($295/year, USDA 1934) vs. Chicago meatpacking ($1,300-$1,560/year). Ford $5/day (1914) flagged as watershed. All figures sourced per entry (BLS, Wright, Montgomery, USDA, state labor commissions).

## Schema Design Decisions

### The Accuracy Line
Facts from records are SACRED. Context uses "likely", "probably", "the pattern suggests". No emotional projection. "{ancestor_name} likely left because the mines were closing" is acceptable. "{ancestor_name} felt heartbroken to leave" is not.

### Optional: coercion_note field
For triggers where `involuntary: false` but the "choice" was between starvation, death, or departure. Applied to: irish_famine, dust_bowl. Candidates: boll_weevil, economic_panics_19c, economic_panics_20c.

### Variable Placeholders
All narrative hooks use `{variable}` syntax: `{ancestor_name}`, `{surname}`, `{given_name}`, `{year}`, `{county}`, `{destination}`, `{origin_county}`, etc.

### Push/Pull Factor Severity Scale
1 = minor influence, 5 = catastrophic/overwhelming. Measures historical severity, not priority.

### Counter-Narratives Requirement
Every trigger includes at least 2 counter-narratives. Every template includes constraints preventing one-dimensional storytelling.

### Source References
Minimum 3 academic sources per trigger, destination, and occupation. Zero Wikipedia.

## How This Data Gets Used

1. **Polsia receives an ancestor record** (name, dates, locations, occupations)
2. **Trigger matching**: Compare ancestor's origin county, era, occupation, and race against the 25 core trigger files (+ regional triggers). Multiple triggers may match.
3. **Route selection**: Use the trigger's `route_refs` to pull transportation details
4. **Destination lookup**: Use `destination_refs` to pull neighborhood, employer, and institutional context
5. **Occupation enrichment**: Match ancestor's listed occupation against the 20 occupation profiles
6. **Wage contextualization**: Pull wage data from the 3 wage tables to ground economic comparisons
7. **Template selection**: Choose appropriate narrative templates (Letter Home, What They Saw, Fork in the Road, Record Silences) based on available records and detected gaps
8. **Research guidance**: When record gaps are detected, pull actionable research advice from the 10 guidance files
9. **Narrative generation**: Feed all matched data into the narrative AI with Accuracy Line constraints
10. **Counter-narrative injection**: Include at least one counter-narrative per trigger

## What Is NOT Built (Deferred)

### Track B — Life Patterns (deferred to White Glove tier)
~20 non-migration patterns from Narrative Strains: Boarding House Matriarch, Sharecropping Trap, Domestic Service arc. Essential for multi-generational White Glove reports. Not needed for Option A single-ancestor reports.

### Placeholder directories (Sprint 2+)
- `deep_dives/` — Extended narratives for specific triggers

## Phase 3A — Coverage Expansion (COMPLETE)

All 8 new triggers, 10 new destinations, 10 new occupations, and 4 new routes built and validated. Estimated trigger coverage now ~95% of American genealogy migration patterns (1717-1970).

### New Destinations (10)
atlanta, memphis, minneapolis, denver, seattle, cincinnati, milwaukee, new_orleans, houston, washington_dc

### New Occupations (10)
carpenter, blacksmith, teacher, seamstress_garment_worker, laundress, store_clerk, fisherman, logger, nurse, career_soldier

### New Routes (4)
erie_canal, mississippi_steamboat, mormon_trail, intercity_bus

## Production Readiness Assessment

### Is the existing data sufficient for the Option A product to ship?
**Yes — with significantly expanded coverage.** 25 core triggers + 19 regional triggers cover ~97% of American genealogy migration patterns (1717-1970) across 14 states. 21 destination cities cover Tier 1 and Tier 2 magnets. 20 occupations cover the most common census listings. 24 routes cover every major transportation corridor. 31 community texture profiles add settled-life institutional detail. The 10 templates, 10 research guidance files, 3 wage tables, and 12 material life profiles round out the enrichment stack. An Option A report has deep, well-sourced data for nearly any ancestor's migration story.

### What's the minimum viable dataset for a production Option A report?
- 1 matched trigger (push/pull factors, route, destination)
- 1 destination city profile (neighborhood, employer, institutions)
- 1 occupation profile (daily work, wages, conditions)
- 1-2 template outputs (Letter Home + Fork in the Road or What They Saw)
- Wage comparison (origin vs. destination)
- 1 Record Silences interpretation (if gaps detected)
- 1 community texture profile (if available for destination)

### What's blocking the White Glove tier?
**Track B / Life Patterns.** The White Glove report is multi-generational. Between migrations, ancestors lived in one place for decades. The narrative AI needs Life Pattern data (Boarding House Matriarch, Sharecropping Trap, etc.) to fill those narrative gaps. Track B is correctly deferred to the White Glove tier because the data serves that tier exclusively.

## Community Texture Profiles (Phase 3C — COMPLETE)

Schema defined by exemplar: `chicago_black_bronzeville.json`. All 31 files valid JSON.

| File | Community Type | Status |
|------|---------------|--------|
| chicago_black_bronzeville | destination_enclave | COMPLETE |
| detroit_black_paradise_valley | destination_enclave | COMPLETE |
| boston_irish_1845_1900 | destination_enclave | COMPLETE |
| piedmont_mill_village | industrial_community | COMPLETE |
| chicago_polish_1870_1920 | destination_enclave | COMPLETE |
| harlem_new_york | destination_enclave | COMPLETE |
| fayetteville_mill_district | industrial_community | COMPLETE (Phase 3D NC) |
| eastern_nc_farm_community | origin_community | COMPLETE (Phase 3D NC) |
| new_york_lower_east_side | destination_enclave | COMPLETE |
| pittsburgh_slavic_steel | industrial_community | COMPLETE |
| german_midwest_1848_1900 | destination_enclave | COMPLETE |
| dust_bowl_oklahoma | origin_community | COMPLETE |
| wwii_defense_boomtown | industrial_community | COMPLETE |
| appalachian_coal_camp | origin_community | COMPLETE |
| scots_irish_frontier | origin_community | COMPLETE |
| great_plains_homesteader | origin_community | COMPLETE |
| deep_south_black_community | origin_community | COMPLETE |
| mississippi_delta_cotton | origin_community | COMPLETE |
| shenandoah_valley_farm_community | origin_community | COMPLETE (Phase 3D VA) |
| cincinnati_appalachian_enclave | destination_enclave | COMPLETE (Phase 3D OH) |
| sc_upcountry_farm_community | origin_community | COMPLETE (Phase 3D SC) |
| rural_georgia_black_belt | origin_community | COMPLETE (Phase 3D GA) |
| eastern_ky_coal_community | origin_community | COMPLETE (Phase 3D KY) |
| east_tennessee_mountain_community | origin_community | COMPLETE (Phase 3D TN) |
| memphis_beale_street_community | destination_enclave | COMPLETE (Phase 3D MS) |
| texas_german_hill_country | destination_enclave | COMPLETE (Phase 3D TX) |
| minnesota_scandinavian_community | destination_enclave | COMPLETE (Phase 3D MN) |
| pa_anthracite_patch_town | origin_community | COMPLETE (Phase 3D PA) |
| birmingham_iron_steel_community | industrial_community | COMPLETE (Phase 3D AL) |
| cajun_prairie_community | destination_enclave | COMPLETE (Phase 3D LA) |
| illinois_downstate_farm_community | origin_community | COMPLETE (Phase 3D IL) |

Location: `migration_triggers/shared/community_texture/`

## Regional Migration Triggers (Phase 3D — 14 STATES COMPLETE)

New data category: state-specific micro-patterns in `migration_triggers/regional/[state]/`

### NC Regional Triggers (6 files, 1,319 lines)

| File | Era | Class | Lines |
|------|-----|-------|------:|
| nc_eastern_farm_to_mill | 1865-1910 | economic | 232 |
| nc_mountain_to_piedmont_mills | 1880-1940 | economic | 209 |
| nc_wilmington_1898_exodus | 1898-1910 | racial_flight | 199 |
| nc_piedmont_tobacco_to_industry | 1900-1960 | economic | 221 |
| nc_civil_war_veteran_settlement | 1865-1900 | military | 212 |
| nc_piedmont_to_coastal_cities | 1875-1920 | economic | 246 |

### Tier 1 State Expansion (7 triggers, ~1,800 lines)

| State | Trigger | Era | Parent | Lines |
|-------|---------|-----|--------|------:|
| VA | va_shenandoah_valley_westward | 1750-1850 | scots_irish_frontier | 233 |
| OH | oh_appalachian_to_river_cities | 1900-1970 | appalachian_out_migration | 218 |
| SC | sc_upcountry_farm_to_mill | 1880-1930 | textile_mill_recruitment | 260 |
| GA | ga_rural_to_atlanta | 1880-1950 | great_migration | 305 |
| KY | ky_eastern_coal_exodus | 1940-1970 | appalachian_out_migration | 243 |
| TN | tn_mountain_to_industrial | 1900-1960 | appalachian_out_migration | 288 |
| MS | ms_delta_to_southern_cities | 1890-1950 | great_migration | 268 |

### Tier 2 State Expansion (6 triggers, ~1,460 lines)

| State | Trigger | Era | Parent | Lines |
|-------|---------|-----|--------|------:|
| TX | tx_german_hill_country | 1840-1880 | german_immigration | 232 |
| MN | mn_scandinavian_settlement | 1850-1920 | *(none — fills gap)* | 262 |
| PA | pa_anthracite_exodus | 1870-1940 | se_european_wave | 219 |
| AL | al_black_belt_to_birmingham | 1880-1940 | great_migration | 279 |
| LA | la_cajun_acadian_settlement | 1755-1960 | *(none — unique)* | 247 |
| IL | il_downstate_to_chicago | 1870-1930 | *(none — unique)* | 229 |

### Associated Community Textures (15 files — 2 NC + 13 expansion)

| File | Type | State | Lines |
|------|------|-------|------:|
| fayetteville_mill_district | industrial_community | NC | 188 |
| eastern_nc_farm_community | origin_community | NC | 152 |
| shenandoah_valley_farm_community | origin_community | VA | 131 |
| cincinnati_appalachian_enclave | destination_enclave | OH | 201 |
| sc_upcountry_farm_community | origin_community | SC | 200 |
| rural_georgia_black_belt | origin_community | GA | 200 |
| eastern_ky_coal_community | origin_community | KY | 203 |
| east_tennessee_mountain_community | origin_community | TN | 199 |
| memphis_beale_street_community | destination_enclave | MS | 218 |
| texas_german_hill_country | destination_enclave | TX | 209 |
| minnesota_scandinavian_community | destination_enclave | MN | 201 |
| pa_anthracite_patch_town | origin_community | PA | 209 |
| birmingham_iron_steel_community | industrial_community | AL | 209 |
| cajun_prairie_community | destination_enclave | LA | 203 |
| illinois_downstate_farm_community | origin_community | IL | 203 |

Key features:
- 19 triggers across 14 states cover intra-state migration from 1717-1970
- Race-aware routing throughout: white mill paths, Black alternative paths, dignity mandates where applicable
- Wilmington 1898 coup gets standalone trigger with dignity mandate and named perpetrators
- 3 triggers have no parent (MN, LA, IL) — fill known coverage gaps
- MN Scandinavian trigger fills the #1 remaining gap from Gap Analysis
- GA, MS, AL triggers include dignity mandate for racial violence context
- Tobacco belt pattern (NC) is UNIQUE — no national trigger covers this
- Civil War veteran trigger (NC) captures Western NC's "inner civil war"
- LA Cajun trigger spans forced (Grand Dérangement 1755) + voluntary (oil field 1920s)

## Material Life Profiles (Phase 3B — COMPLETE)

12 era/region profiles describing the physical reality of daily life — housing, food, clothing, hygiene, transportation, communication, entertainment, household goods. Each with 8 sections, sourced details, sensory snapshot, and narrative hooks.

| File | Era | Region | Lines |
|------|-----|--------|------:|
| frontier_log_cabin_1780_1840 | 1780-1840 | Appalachia/Frontier | 258 |
| antebellum_plantation_1820_1860 | 1820-1860 | Deep South | 250 |
| antebellum_yeoman_farm_1820_1860 | 1820-1860 | Upper South/Piedmont | 248 |
| immigrant_tenement_1845_1890 | 1845-1890 | Northeastern cities | 248 |
| homestead_sodhouse_1862_1900 | 1862-1900 | Great Plains | 232 |
| mining_camp_1848_1900 | 1848-1900 | Western mining districts | 260 |
| industrial_city_1880_1920 | 1880-1920 | Midwest/Mid-Atlantic | 247 |
| southern_mill_village_1880_1930 | 1880-1930 | Piedmont/Upper South | 249 |
| sharecropper_cabin_1865_1940 | 1865-1940 | Deep South | 247 |
| coal_camp_appalachia_1880_1930 | 1880-1930 | Appalachia | 240 |
| dust_bowl_farmstead_1920_1940 | 1920-1940 | Great Plains/Southwest | 247 |
| wwii_homefront_1941_1945 | 1941-1945 | Multiple (composite) | 275 |

Location: `migration_triggers/shared/material_life/`

Key features:
- Every profile cross-references its associated triggers via `trigger_refs`
- antebellum_plantation covers BOTH enslaved and slaveholding perspectives (enslaved first, equal or greater detail)
- Racial exclusion documented where applicable (mill village, mining camp)
- Dignity mandate honored throughout (sharecropper, plantation)
- dust_bowl captures the 1920s→1930s prosperity-to-collapse contrast
- wwii_homefront includes Japanese American incarceration note
- All sources academic — minimum 5 per file, zero Wikipedia

## Gap Detection System (Phase 3B addition)

Self-improving feedback loop: when Polsia processes ancestors and can't match NEL data, it generates structured gap reports following `_gap_detection/gap_report_schema.json`. Gap reports accumulate, get priority-scored (severity x frequency), and become build targets for future Claude Code CLI sessions.

| File | Purpose | Location |
|------|---------|----------|
| GAP_DETECTION_GUIDE.md | Instructions for Polsia | `_gap_detection/` |
| gap_report_schema.json | Gap report JSON format | `_gap_detection/` |

## Relationship to Other Data Layers

- **Layer 1 — County Source Profiler** (COMPLETE, 56 builds, 19,929 profiles): Tells the narrative AI *where to look* for records
- **Layer 2 — Historical Context Timelines** (COMPLETE, 56 files): Provides decade-by-decade background for every state
- **Layer 3 — Migration Decision Trees + Enrichment** (ALL PHASES COMPLETE — 179 files): Explains *why* people moved, *how* they traveled, *what they found*, and provides templates, research guidance, economic context, material life, and community texture
