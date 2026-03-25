# KinLore NEL Phase 4: Life Patterns with Chain-Link Architecture

**Version**: 1.0
**Date**: 2026-03-18
**Status**: Schema Design + Selection Complete — Ready for Build

---

## Purpose

Life Patterns are the Phase 4 layer of the Narrative Enrichment Layer. They describe **what happened while people STAYED** — the settled-life arcs, economic trajectories, family dynamics, and community patterns that unfolded between migrations, typically spanning one to three generations in a single place.

Triggers describe why people MOVED. Life Patterns describe how people LIVED.

A White Glove report spanning four generations should be able to chain:
**trigger → life_pattern → trigger → life_pattern** through the chain-link fields, producing a continuous narrative arc across centuries.

---

## Table of Contents

1. [Full Strain Classification (All 100)](#1-full-strain-classification-all-100)
2. [Life Pattern JSON Schema](#2-life-pattern-json-schema)
3. [Schema Field Reference](#3-schema-field-reference)
4. [Build Plan (~22 Selected Life Patterns)](#4-build-plan-22-selected-life-patterns)
5. [Exemplar Reference](#5-exemplar-reference)
6. [Build Instructions for Parallel Agents](#6-build-instructions-for-parallel-agents)

---

## 1. Full Strain Classification (All 100)

Each of the 100 narrative strains from `NARRATIVE_STRAINS.md` is classified as one of:

- **TRIGGER_DUPLICATE** — Already covered by an existing NEL core or regional trigger
- **TRIGGER_CANDIDATE** — A migration pattern not yet covered that could become a future trigger
- **LIFE_PATTERN** — A settled-life, family-arc, or economic-trajectory pattern that happens BETWEEN migrations (Phase 4 targets)

### Category 1: Land & Homestead Migrations

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 1 | The Tidewater-to-Piedmont Drift | TRIGGER_CANDIDATE | Colonial-era migration not yet covered; could pair with scots_irish_frontier |
| 2 | The Great Wagon Road Scots-Irish Stream | TRIGGER_DUPLICATE | Covered by `core/scots_irish_frontier.json` |
| 3 | The Kentucky Dark and Bloody Ground | TRIGGER_CANDIDATE | Trans-Appalachian migration through Cumberland Gap; related to scots_irish_frontier but distinct enough for a future trigger |
| 4 | The Northwest Territory Yankee Plow | TRIGGER_CANDIDATE | Yankee westward migration to Ohio not covered by existing triggers |
| 5 | The Southern Yeoman's Alabama Fever | TRIGGER_DUPLICATE | Partially covered by `core/antebellum_yeoman_south.json` |
| 6 | The Texas Empresario Gamble | TRIGGER_CANDIDATE | Pre-annexation Texas migration; partially covered by regional/tx triggers |
| 7 | The Oregon Trail Family Wagon | TRIGGER_CANDIDATE | Overland trail migration not yet in NEL |
| 8 | The Homestead Act Prairie Claim | TRIGGER_DUPLICATE | Covered by `core/homestead_act.json` |
| 9 | The Oklahoma Land Run Dash | TRIGGER_DUPLICATE | Covered by `core/oklahoma_land_runs.json` |
| 10 | The Cutover Timber-Land Settler | TRIGGER_CANDIDATE | Great Lakes cutover settlement; niche but documentable |

### Category 2: Agricultural Crises

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 11 | The Boll Weevil Exodus | TRIGGER_DUPLICATE | Covered by `core/boll_weevil.json` |
| 12 | The Dust Bowl Okie Migration | TRIGGER_DUPLICATE | Covered by `core/dust_bowl.json` |
| 13 | The Tobacco Road Soil Exhaustion | LIFE_PATTERN | Multi-generational decline arc; what happened to families farming exhausted soil before they moved |
| 14 | The Post-Civil War Southern Sharecropping Trap | **LIFE_PATTERN** | **Exemplar file.** The iconic "stayed" pattern — decades trapped in a single place by economic coercion |
| 15 | The Grasshopper Plague Retreat | TRIGGER_CANDIDATE | Short-duration disaster migration; could be a trigger |
| 16 | The Great Plains Wheat Boom and Bust | LIFE_PATTERN | Boom-bust economic arc on the plains — a lifecycle of expansion, overextension, and collapse |
| 17 | The Appalachian Subsistence Squeeze | LIFE_PATTERN | Multi-generational farm subdivision arc; the slow squeeze before out-migration |
| 18 | The Delta Cotton Mechanization Displacement | TRIGGER_CANDIDATE | Overlaps with great_migration but the mechanization angle is distinct |
| 19 | The New England Farm Abandonment | LIFE_PATTERN | Multi-generational decline and departure arc for Yankee hill farms |
| 20 | The Bracero and Migrant Farm Circuit | TRIGGER_DUPLICATE | Covered by `core/bracero_program.json` |

### Category 3: Industrial Pulls

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 21 | The New England Mill Girl Pipeline | LIFE_PATTERN | Occupational lifecycle for young women in the mill system — entry, work, exit |
| 22 | The Anthracite Patch Town Cage | LIFE_PATTERN | Multi-generational company-town lifecycle — arrival, entrapment, exit or stagnation |
| 23 | The Pittsburgh/Birmingham Steel Furnace Pull | LIFE_PATTERN | The immigrant steelworker family arc across two or three generations |
| 24 | The Detroit Auto Assembly Line | LIFE_PATTERN | The assembly-line family arc — arrival, factory life, neighborhood formation, second-generation divergence |
| 25 | The Lowell-to-Lawrence Immigrant Mill Succession | LIFE_PATTERN | Multi-ethnic occupational succession pattern in a single industry |
| 26 | The Colorado/Montana Hard-Rock Mining Magnet | TRIGGER_CANDIDATE | Mining migration pattern; related to gold_rush_mining_boom |
| 27 | The Railroad Section-Gang Trail | TRIGGER_DUPLICATE | Covered by `core/railroad_construction.json` |
| 28 | The Appalachian-to-Ohio Factory Pipeline | TRIGGER_DUPLICATE | Covered by `core/appalachian_out_migration.json` and `regional/oh/oh_appalachian_to_river_cities.json` |
| 29 | The West Virginia Coal Camp Company Town | LIFE_PATTERN | The coal-camp lifecycle — arrival, company-town existence, mine closure, community death |
| 30 | The Pullman Porter Network | LIFE_PATTERN | Occupational lifecycle with unique information-network role; feeds into great_migration |

### Category 4: The Great Migration & Racial Violence

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 31 | The First Great Migration: Mississippi to Chicago | TRIGGER_DUPLICATE | Covered by `core/great_migration.json` (Phase 1) |
| 32 | The Second Great Migration: South to Everywhere | TRIGGER_DUPLICATE | Covered by `core/great_migration.json` (Phase 2) |
| 33 | Lynching Flight: The Terror That Moved Families | TRIGGER_CANDIDATE | Specific racial-terror trigger distinct from great_migration; high priority for future trigger |
| 34 | Sundown Town Exclusion and Rerouting | LIFE_PATTERN | Not a migration but a structural constraint shaping where settled life could happen |
| 35 | The Tulsa/Rosewood/East St. Louis Massacre Diaspora | TRIGGER_CANDIDATE | Massacre-driven displacement; specific enough for future trigger |
| 36 | The Exoduster Movement to Kansas | TRIGGER_CANDIDATE | Distinct pre-Great-Migration Black westward movement |
| 37 | The South Carolina Sea Island Isolation and Persistence | LIFE_PATTERN | Classic persistence/staying pattern — Gullah/Geechee community lifecycle |

### Category 5: Immigration Waves

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 38 | The Irish Famine Flood | TRIGGER_DUPLICATE | Covered by `core/irish_famine.json` |
| 39 | The German Forty-Eighter Intellectual Migration | TRIGGER_DUPLICATE | Covered by `core/german_immigration.json` |
| 40 | The Scandinavian Prairie Settlement | LIFE_PATTERN | Post-migration settlement lifecycle — the first generation's arc from arrival to established farm community |
| 41 | The Southern Italian Sojourner Pattern | TRIGGER_DUPLICATE | Covered by `core/se_european_wave.json` |
| 42 | The Eastern European Jewish Flight from Pogroms | TRIGGER_DUPLICATE | Covered by `core/jewish_pogrom_flight.json` |
| 43 | The Chinese Exclusion and Survival | TRIGGER_DUPLICATE | Covered by `core/chinese_exclusion_era.json` |
| 44 | The Volga German Resettlement | TRIGGER_CANDIDATE | Distinct enough for a future trigger; community-transplant pattern |
| 45 | The Quebec Petit-Canadien Mill Migration | TRIGGER_CANDIDATE | Not yet in NEL; significant for New England genealogy |
| 46 | The Polish Partition Diaspora | LIFE_PATTERN | The immigrant parish lifecycle — arrival, institution-building, upward mobility, assimilation |
| 47 | The Mexican Revolution Refugee Wave | TRIGGER_CANDIDATE | Distinct from bracero_program; refugee pattern |
| 48 | The Greek Kafenion-to-Diner Chain | LIFE_PATTERN | Immigrant entrepreneurial lifecycle — arrival, wage work, business ownership, community formation |

### Category 6: Forced Displacements

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 49 | The Trail of Tears: Cherokee Removal | TRIGGER_DUPLICATE | Covered by `core/indian_removal_trail_of_tears.json` |
| 50 | The Five Tribes Removal Cascade | TRIGGER_DUPLICATE | Covered by `core/indian_removal_trail_of_tears.json` (broader scope) |
| 51 | The Enslaved Family Sale and Separation | TRIGGER_DUPLICATE | Covered by `core/domestic_slave_trade.json` |
| 52 | Japanese American Internment | TRIGGER_DUPLICATE | Covered by `core/wwii_relocation.json` |
| 53 | The Reservoir Flood Displacement | TRIGGER_CANDIDATE | TVA/dam displacement pattern; distinct from any existing trigger |
| 54 | The Freedmen's Bureau Relocation and Family Reunification | TRIGGER_DUPLICATE | Covered by `core/reconstruction_era.json` |
| 55 | The Dakota War Exile and Internment | TRIGGER_CANDIDATE | Specific Indigenous displacement not in current NEL |
| 56 | The Acadian Expulsion and Cajun Resettlement | TRIGGER_DUPLICATE | Partially covered by `regional/la/la_cajun_acadian_settlement.json` |
| 57 | The Navajo Long Walk | TRIGGER_CANDIDATE | Specific Indigenous displacement not in current NEL |
| 58 | The Urban Renewal "Negro Removal" | TRIGGER_CANDIDATE | Mid-20th century forced displacement; high priority for future trigger |

### Category 7: War & Military

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 59 | The Civil War Widow's Reconstruction | LIFE_PATTERN | Post-loss family restructuring pattern; what happened after the soldier didn't come home |
| 60 | The WWI Draft Registration and Home-Front Reshuffling | LIFE_PATTERN | Wartime family disruption and adaptation lifecycle |
| 61 | The WWII Defense Migration | TRIGGER_DUPLICATE | Partially covered by `core/gi_bill_migration.json` and material_life/wwii_homefront |
| 62 | The GI Bill Suburban Transformation | TRIGGER_DUPLICATE | Covered by `core/gi_bill_migration.json` |
| 63 | The Civil War Border-State Refugee Crisis | TRIGGER_DUPLICATE | Covered by `core/civil_war_displacement.json` |
| 64 | The Korean and Vietnam War Military Family Circuit | LIFE_PATTERN | The military-family lifecycle — enlistment, base life, deployment, homecoming, settlement |

### Category 8: Economic Panics & Depressions

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 65 | The Panic of 1837 and Westward Acceleration | TRIGGER_DUPLICATE | Covered by `core/economic_panics_19c.json` |
| 66 | The Long Depression of 1873 and Industrial Displacement | TRIGGER_DUPLICATE | Covered by `core/economic_panics_19c.json` |
| 67 | The Panic of 1893 and the Populist Exodus | TRIGGER_DUPLICATE | Covered by `core/economic_panics_19c.json` |
| 68 | The Great Depression Family Survival Strategies | LIFE_PATTERN | Depression survival lifecycle — the family strategies that kept people in place |

### Category 9: Natural Disasters

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 69 | The Galveston Hurricane Exodus (1900) | TRIGGER_CANDIDATE | Single-event disaster trigger |
| 70 | The San Francisco Earthquake and Chinatown Destruction (1906) | TRIGGER_CANDIDATE | Single-event disaster trigger |
| 71 | The 1927 Mississippi Flood and Delta Displacement | TRIGGER_CANDIDATE | Single-event disaster trigger with racial dimensions |
| 72 | The 1930s Ohio River Flood Displacement | TRIGGER_CANDIDATE | Regional disaster trigger |
| 73 | The Johnstown Flood Family Obliteration (1889) | TRIGGER_CANDIDATE | Single-event disaster trigger |
| 74 | The 1906 and 1928 Florida Hurricane Migrations | TRIGGER_CANDIDATE | Regional disaster trigger |
| 75 | The Great Peshtigo Fire and Cutover Devastation (1871) | TRIGGER_CANDIDATE | Single-event disaster trigger |

### Category 10: Social & Religious Movements

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 76 | The Mormon Trek and Gathering | TRIGGER_DUPLICATE | Covered by `core/mormon_migration.json` |
| 77 | The Amish and Mennonite Persistence Pattern | LIFE_PATTERN | The "daughter colony" lifecycle — community growth, fission, replanting |
| 78 | The Utopian Colony Experiment | LIFE_PATTERN | The commune lifecycle — founding, flourishing, dissolution, dispersal |
| 79 | The Shaker Gathering and Dissolution | TRIGGER_CANDIDATE | Niche religious migration; too small for a life pattern |
| 80 | The Back-to-Africa Emigration Movement | TRIGGER_CANDIDATE | Emigration pattern distinct from anything in NEL |

### Category 11: Women's & Family Patterns

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 81 | The Widow's Relocation to Town | LIFE_PATTERN | The widow's economic arc — loss, relocation, survival, rebuilding |
| 82 | The Orphan Train Resettlement | TRIGGER_CANDIDATE | Forced child placement pattern; distinct from migration triggers |
| 83 | The Boarding House Matriarch Economy | LIFE_PATTERN | Women's economic lifecycle — the boarding house as survival and community institution |
| 84 | The Domestic Service Migration | LIFE_PATTERN | Women's occupational lifecycle — entry into service, accumulation, marriage/exit |
| 85 | The Mail-Order Bride and Picture-Bride Pattern | TRIGGER_CANDIDATE | Spousal migration pattern; niche |
| 86 | The Prostitution and Red-Light District Survival Economy | LIFE_PATTERN | Women's survival economy in frontier/industrial communities; high sensitivity |
| 87 | The Indentured Servant Family Formation | LIFE_PATTERN | Colonial-era lifecycle — indenture, service, freedom, land acquisition |

### Category 12: Resource Booms & Busts

| # | Strain Name | Classification | Notes |
|---|------------|----------------|-------|
| 88 | The California Gold Rush Forty-Niner | TRIGGER_DUPLICATE | Covered by `core/gold_rush_mining_boom.json` |
| 89 | The Comstock Lode Silver Bonanza | TRIGGER_CANDIDATE | Specific mining migration; related to gold_rush_mining_boom |
| 90 | The Black Hills Gold Rush and Lakota Dispossession | TRIGGER_CANDIDATE | Mining migration with Indigenous dispossession dimension |
| 91 | The Pennsylvania Oil Boom Pioneer | LIFE_PATTERN | Resource boom-bust lifecycle — the arc of a family riding the boom |
| 92 | The Klondike and Alaska Gold Rush | TRIGGER_CANDIDATE | Specific mining migration |
| 93 | The Spindletop Oil Boom and Texas Gusher Culture | LIFE_PATTERN | Oil-field nomadic lifecycle — the family that followed the drill bit |
| 94 | The Appalachian Timber Boom and Bust | LIFE_PATTERN | The lifecycle of a mountain community before, during, and after timber extraction |
| 95 | The Lead and Zinc Mining Towns of the Tri-State | LIFE_PATTERN | Multi-generational mining-town lifecycle including environmental contamination |
| 96 | The Michigan Copper Country Rise and Fall | LIFE_PATTERN | Multi-ethnic mining-community lifecycle from boom through decline |
| 97 | The Colorado Silver Crash Displacement | TRIGGER_CANDIDATE | Single-event economic displacement trigger |
| 98 | The Southern Turpentine and Naval Stores Circuit | LIFE_PATTERN | Exploitative extractive-labor lifecycle — peonage, isolation, depletion |
| 99 | The Anthracite-to-Bituminous Coal Family Migration | TRIGGER_CANDIDATE | Inter-coalfield migration pattern |
| 100 | The Great Lakes Iron Range Family Arc | LIFE_PATTERN | Multi-ethnic industrial community lifecycle from boom through mechanization |

### Classification Summary

| Classification | Count | Notes |
|----------------|------:|-------|
| TRIGGER_DUPLICATE | 35 | Already covered by existing NEL triggers |
| TRIGGER_CANDIDATE | 27 | Future trigger candidates (not Phase 4 scope) |
| LIFE_PATTERN | 38 | Phase 4 targets — settled-life patterns between migrations |

---

## 2. Life Pattern JSON Schema

### Schema Version: 1.0

```json
{
  "_schema_version": "1.0",
  "_last_updated": "2026-03-18",
  "_purpose": "string — one-sentence description of what this Life Pattern captures",

  "pattern_id": "string — snake_case unique identifier",
  "display_name": "string — human-readable name",
  "short_description": "string — 2-3 sentence summary of the pattern",
  "era_range": "string — e.g., '1865-1940'",
  "regions": ["array of region strings"],
  "population": "string — who experiences this pattern, with demographic detail",
  "pattern_class": "string — one of: economic_arc | family_dynamic | community_pattern | occupational_lifecycle | social_transformation",

  "lifecycle_phases": [
    {
      "phase_id": "string — snake_case identifier",
      "phase_name": "string — display name for the phase",
      "era": "string — date range for this phase",
      "description": "string — 3-5 sentences describing what happens in this phase",
      "record_signatures": ["array of strings — what specific records this phase generates"],
      "narrative_hook": "string — with {variable} placeholders"
    }
  ],

  "entry_conditions": [
    {
      "condition_id": "string — snake_case identifier",
      "description": "string — what prior event or state feeds into this pattern",
      "fed_by_triggers": ["array of migration_id strings from existing triggers"],
      "fed_by_patterns": ["array of pattern_id strings from other Life Patterns"],
      "typical_generation_position": "string — first | second | third+"
    }
  ],

  "exit_conditions": [
    {
      "condition_id": "string — snake_case identifier",
      "description": "string — what this pattern produces that becomes the next generation's push factor or entry condition",
      "activates_triggers": ["array of migration_id strings"],
      "activates_patterns": ["array of pattern_id strings"],
      "generation_lag": "string — same_generation | next_generation | two_generations",
      "severity": "integer 1-5 — same scale as trigger push factors"
    }
  ],

  "chain_examples": [
    "string — concrete multi-generational chain example",
    "string — another chain example"
  ],

  "daily_life": {
    "narrative": "string — 4-6 sentences describing a typical day/week/year in this pattern",
    "details": [
      {
        "item": "string — aspect name",
        "description": "string — 2-4 sentences of sourced detail",
        "source": "string — citation"
      }
    ]
  },

  "economic_trajectory": {
    "narrative": "string — 3-5 sentences describing the financial arc",
    "trajectory_type": "string — accumulating | stable | declining | trapped | volatile",
    "details": [
      {
        "item": "string — aspect name",
        "description": "string — 2-4 sentences of sourced detail",
        "source": "string — citation"
      }
    ]
  },

  "family_dynamics": {
    "narrative": "string — 3-5 sentences describing how this pattern shaped family structure",
    "details": [
      {
        "item": "string — aspect name",
        "description": "string — 2-4 sentences of sourced detail",
        "source": "string — citation"
      }
    ]
  },

  "record_signatures": [
    {
      "record_type": "string — name of the record type",
      "description": "string — what it contains and where to find it",
      "genealogical_value": "string — what a researcher can extract from it"
    }
  ],

  "cultural_markers": [
    {
      "marker": "string — the visible sign",
      "description": "string — how it appears in records and family memory"
    }
  ],

  "narrative_hooks": [
    "string with {variable} placeholders — reusable narrative sentences",
    "string with {variable} placeholders"
  ],

  "counter_narratives": [
    {
      "myth": "string — the common misconception",
      "reality": "string — the documented truth",
      "source": "string — citation"
    }
  ],

  "source_references": [
    "string — full citation in Chicago style"
  ],

  "material_life_refs": ["array of material_life_id strings"],
  "community_texture_refs": ["array of community_id strings"],
  "trigger_refs": ["array of migration_id strings — contextually related triggers"]
}
```

---

## 3. Schema Field Reference

### Identity Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pattern_id` | string | YES | Unique snake_case identifier. Convention: descriptive name without dates (e.g., `sharecropping_trap`, `yeoman_farming_stability`) |
| `display_name` | string | YES | Human-readable name for reports and UI |
| `short_description` | string | YES | 2-3 sentence summary. Must distinguish this from triggers — focus on what happens while staying, not on moving |
| `era_range` | string | YES | Date range, e.g., "1865-1940". May span multiple generations |
| `regions` | array | YES | Geographic regions where this pattern occurs |
| `population` | string | YES | Detailed demographic description — race, class, occupation, family structure |
| `pattern_class` | string | YES | One of five classes (see below) |

### Pattern Classes

| Class | Description | Example |
|-------|-------------|---------|
| `economic_arc` | Patterns defined by an economic trajectory — accumulation, stability, decline, or trap | sharecropping_trap, wheat_boom_bust |
| `family_dynamic` | Patterns defined by how family structure changes over time | civil_war_widows_arc, military_family_circuit |
| `community_pattern` | Patterns defined by how communities form, sustain, or dissolve | immigrant_parish_lifecycle, company_town_lifecycle |
| `occupational_lifecycle` | Patterns defined by a specific occupation's arc over a career or generation | mill_girl_pipeline, pullman_porter_network |
| `social_transformation` | Patterns defined by large-scale social or structural change experienced while staying | depression_survival_strategies, sundown_town_exclusion |

### Lifecycle Phases (CRITICAL — the structural core)

Each Life Pattern MUST have 3-5 phases that describe the arc of the pattern over time. This is the key structural difference from triggers, which have push/pull factors.

**Phase structure:**
- `phase_id`: snake_case identifier (e.g., `entry_and_establishment`)
- `phase_name`: Display name (e.g., `Entry and Establishment`)
- `era`: Date range for this phase within the overall pattern era
- `description`: 3-5 sentences describing what happens, what changes, what records are generated
- `record_signatures`: Array of specific record types generated during this phase
- `narrative_hook`: Reusable sentence with `{variable}` placeholders

### Chain-Link Fields (REQUIRED — the architectural innovation)

These fields are REQUIRED on every Life Pattern. They are what makes the chain-link architecture work.

**Entry Conditions** — What feeds INTO this pattern:
- `condition_id`: Unique identifier for this entry path
- `description`: What prior event or state creates the conditions for entering this pattern
- `fed_by_triggers`: Array of `migration_id` values from existing triggers
- `fed_by_patterns`: Array of `pattern_id` values from other Life Patterns
- `typical_generation_position`: Which generation typically enters — "first" (the person who migrated), "second" (their children), "third+" (grandchildren and later)

**Exit Conditions** — What this pattern PRODUCES:
- `condition_id`: Unique identifier for this exit path
- `description`: What this pattern creates that becomes the next generation's push factor or entry condition
- `activates_triggers`: Array of `migration_id` values from triggers this exit feeds into
- `activates_patterns`: Array of `pattern_id` values from Life Patterns this exit feeds into
- `generation_lag`: How long before the exit activates — "same_generation", "next_generation", "two_generations"
- `severity`: 1-5 scale (same as trigger push factors). 1=minor nudge, 5=catastrophic/unavoidable

**Chain Examples** — 2-3 concrete multi-generational chains showing the pattern in context:
```
"scots_irish_frontier → yeoman_farming_stability → civil_war_displacement → sharecropping_trap → great_migration"
```

### Content Fields

**daily_life**: Object with narrative + sourced details. What a typical day/week/year looked like for people living this pattern. Must include material details a narrative writer can use.

**economic_trajectory**: Object with narrative + trajectory_type + sourced details. The financial arc — accumulating, stable, declining, trapped, or volatile. Must include specific dollar amounts, property values, or wage rates where available.

**family_dynamics**: Object with narrative + sourced details. How this pattern shaped family structure, gender roles, child-rearing, inheritance, and intergenerational relationships.

**record_signatures**: Array of objects describing what specific records this Life Pattern generates. Life Pattern records are DIFFERENT from trigger records — a Life Pattern might generate property tax rolls, school records, church membership over decades, not migration records. Each record signature includes:
- `record_type`: Name of the record
- `description`: What it contains and where to find it
- `genealogical_value`: What a researcher can extract

**cultural_markers**: Array of objects describing visible signs in records and family memory — naming patterns, religious affiliation, material possessions, food traditions, speech patterns.

### Standard NEL Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `narrative_hooks` | array of strings | YES | 4-6 reusable narrative sentences with `{variable}` placeholders |
| `counter_narratives` | array of objects | YES | Myths vs. documented reality with citations |
| `source_references` | array of strings | YES | Full citations in Chicago style, 3-5 sources |
| `material_life_refs` | array of strings | YES | IDs of related material_life profiles |
| `community_texture_refs` | array of strings | YES | IDs of related community_texture files |
| `trigger_refs` | array of strings | YES | IDs of contextually related triggers |
| `_schema_version` | string | YES | Always "1.0" |
| `_last_updated` | string | YES | ISO date |

---

## 4. Build Plan (22 Selected Life Patterns)

### Selection Criteria Applied

From the 38 strains classified as LIFE_PATTERN, the following 22 were selected based on:
1. **Frequency** — How commonly a KinLore customer would encounter this pattern
2. **Narrative value** — How much it enriches a White Glove report
3. **Existing NEL support** — Whether triggers, material_life, and community_texture already partially cover it
4. **Diversity** — Geographic and temporal spread across the selection
5. **Chain-link density** — How many connections it makes to existing triggers and other patterns

### The 22 Selected Life Patterns

#### Priority 1 — Build First (7 patterns)
These have the densest chain-link connections and the highest customer encounter frequency.

| # | pattern_id | Display Name | Era | Class | Source Strain(s) | Entry Chains | Exit Chains | Priority |
|---|-----------|-------------|-----|-------|------------------|-------------|-------------|----------|
| 1 | `sharecropping_trap` | The Sharecropping Trap | 1865-1940 | economic_arc | #14 | reconstruction_era, domestic_slave_trade, civil_war_displacement | great_migration, boll_weevil, textile_mill_recruitment | **1** |
| 2 | `yeoman_farming_stability` | Yeoman Farming Stability | 1780-1860 | economic_arc | #5, #13 | scots_irish_frontier, homestead_act | antebellum_yeoman_south, civil_war_displacement, economic_panics_19c | **1** |
| 3 | `appalachian_subsistence_squeeze` | The Appalachian Subsistence Squeeze | 1880-1940 | economic_arc | #17 | scots_irish_frontier, yeoman_farming_stability | appalachian_out_migration, coal_camp_lifecycle | **1** |
| 4 | `immigrant_parish_lifecycle` | The Immigrant Parish Lifecycle | 1850-1940 | community_pattern | #46, #25, #41 | irish_famine, se_european_wave, german_immigration | gi_bill_migration, depression_survival_strategies | **1** |
| 5 | `company_town_lifecycle` | The Company Town Lifecycle | 1870-1950 | community_pattern | #22, #29 | appalachian_out_migration, railroad_construction, se_european_wave | appalachian_subsistence_squeeze, great_migration | **1** |
| 6 | `depression_survival_strategies` | Great Depression Family Survival | 1929-1941 | social_transformation | #68 | economic_panics_20c, wheat_boom_bust | gi_bill_migration, dust_bowl, great_migration | **1** |
| 7 | `civil_war_widows_arc` | The Civil War Widow's Arc | 1861-1900 | family_dynamic | #59 | civil_war_service, civil_war_displacement | widow_orphan_relocation, yeoman_farming_stability (decline) | **1** |

#### Priority 2 — Build Second (9 patterns)
High customer frequency and strong chain-link connections; depend on Priority 1 patterns for cross-referencing.

| # | pattern_id | Display Name | Era | Class | Source Strain(s) | Entry Chains | Exit Chains | Priority |
|---|-----------|-------------|-----|-------|------------------|-------------|-------------|----------|
| 8 | `steel_city_immigrant_arc` | The Steel City Immigrant Arc | 1870-1940 | occupational_lifecycle | #23 | se_european_wave, irish_famine | gi_bill_migration, depression_survival_strategies | **2** |
| 9 | `auto_city_family_arc` | The Auto City Family Arc | 1910-1945 | occupational_lifecycle | #24 | great_migration, appalachian_out_migration, se_european_wave | gi_bill_migration, depression_survival_strategies | **2** |
| 10 | `pullman_porter_network` | The Pullman Porter Network | 1867-1960 | occupational_lifecycle | #30 | reconstruction_era, great_migration | great_migration (information accelerant) | **2** |
| 11 | `scandinavian_homestead_arc` | The Scandinavian Homestead Arc | 1860-1920 | community_pattern | #40 | homestead_act | wheat_boom_bust, appalachian_subsistence_squeeze (parallel) | **2** |
| 12 | `new_england_farm_decline` | New England Farm Decline | 1830-1900 | economic_arc | #19 | (colonial settlement) | homestead_act, textile_mill_recruitment, mill_girl_pipeline | **2** |
| 13 | `sundown_town_exclusion` | Sundown Town Exclusion | 1890-1968 | social_transformation | #34 | great_migration, reconstruction_era | great_migration (rerouting effect) | **2** |
| 14 | `tobacco_soil_exhaustion` | Tobacco Road Soil Exhaustion | 1780-1860 | economic_arc | #13 | (colonial settlement) | antebellum_yeoman_south, domestic_slave_trade | **2** |
| 15 | `boarding_house_matriarch` | The Boarding House Matriarch Economy | 1840-1930 | family_dynamic | #83 | irish_famine, se_european_wave, widow_orphan_relocation | immigrant_parish_lifecycle | **2** |
| 16 | `wwi_homefront_disruption` | WWI Home-Front Disruption | 1917-1920 | family_dynamic | #60 | war_of_1812_service (generational echo) | depression_survival_strategies, great_migration | **2** |

#### Priority 3 — Build Last (6 patterns)
Important for completeness and niche customer scenarios; lower encounter frequency but high narrative value.

| # | pattern_id | Display Name | Era | Class | Source Strain(s) | Entry Chains | Exit Chains | Priority |
|---|-----------|-------------|-----|-------|------------------|-------------|-------------|----------|
| 17 | `wheat_boom_bust` | The Great Plains Wheat Boom and Bust | 1914-1932 | economic_arc | #16 | homestead_act, scandinavian_homestead_arc | dust_bowl, depression_survival_strategies | **3** |
| 18 | `mill_girl_pipeline` | The Mill Girl Pipeline | 1820-1860 | occupational_lifecycle | #21 | new_england_farm_decline | immigrant_parish_lifecycle (ethnic succession) | **3** |
| 19 | `gullah_geechee_persistence` | Gullah/Geechee Persistence | 1670s-1950s | community_pattern | #37 | domestic_slave_trade | (modern displacement by development) | **3** |
| 20 | `military_family_circuit` | The Military Family Circuit | 1950-1975 | family_dynamic | #64 | civil_war_service (tradition), gi_bill_migration | gi_bill_migration (second use) | **3** |
| 21 | `oil_field_nomad` | The Oil-Field Nomad Family | 1901-1940 | occupational_lifecycle | #91, #93 | economic_panics_20c, homestead_act (failed) | gi_bill_migration, depression_survival_strategies | **3** |
| 22 | `indentured_servant_formation` | Indentured Servant Family Formation | 1620-1780 | economic_arc | #87 | (transatlantic passage) | yeoman_farming_stability, scots_irish_frontier | **3** |

### Patterns Deferred (16 LIFE_PATTERN strains not selected)

These 16 were classified as LIFE_PATTERN but are deferred to a future build cycle. Reasons: lower customer frequency, high sensitivity requiring special handling, or significant overlap with selected patterns.

| # | Strain | Reason Deferred |
|---|--------|----------------|
| #21/18 | Mill Girl Pipeline (variant) | Covered by #18 above |
| #25 | Immigrant Mill Succession | Overlaps with immigrant_parish_lifecycle |
| #34 | Sundown Town (variant) | Selected above |
| #48 | Greek Kafenion-to-Diner Chain | Niche ethnic pattern; could be future community_texture |
| #77 | Amish Persistence | Niche religious pattern; well-documented elsewhere |
| #78 | Utopian Colony | Very niche; low customer frequency |
| #81 | Widow's Relocation | Overlaps significantly with civil_war_widows_arc |
| #84 | Domestic Service Migration | Overlaps with boarding_house_matriarch; could be future occupational_lifecycle |
| #86 | Red-Light District Economy | High sensitivity; requires special dignity handling; deferred |
| #87 | Indentured Servant (variant) | Selected above |
| #91 | PA Oil Boom | Folded into oil_field_nomad |
| #94 | Appalachian Timber | Overlaps with appalachian_subsistence_squeeze |
| #95 | Tri-State Mining | Overlaps with company_town_lifecycle |
| #96 | Michigan Copper Country | Overlaps with company_town_lifecycle; could be future regional |
| #98 | Turpentine Circuit | Overlaps with sharecropping_trap (peonage); could be future trigger |
| #100 | Iron Range Arc | Overlaps with company_town_lifecycle; could be future regional |

---

## 5. Exemplar Reference

The full exemplar file is written to:
```
/home/dbcanady/kinlore-data/narrative_enrichment/life_patterns/sharecropping_trap.json
```

This exemplar demonstrates every field in the schema with production-quality content. All subsequent Life Pattern builds should use it as their structural template.

Key characteristics of the exemplar:
- **4 lifecycle phases** spanning 1865-1940 (Entry/Contract, Entrenchment, Breaking Point, Exit or Persistence)
- **3 entry conditions** (from emancipation, from antebellum tenancy, from failed Reconstruction land ownership)
- **4 exit conditions** (Great Migration, boll weevil displacement, textile mill recruitment, mechanization displacement)
- **3 chain examples** showing multi-generational paths
- **Full content sections** (daily_life, economic_trajectory, family_dynamics) each with narrative + 3-4 sourced details
- **5 record signatures** specific to the pattern (not migration records — crop lien ledgers, agricultural schedules, etc.)
- **4 cultural markers**
- **6 narrative hooks** with {variable} placeholders
- **3 counter-narratives** with sourced corrections
- **Cross-references** to 3 material_life files, 3 community_texture files, and 5 triggers

---

## 6. Build Instructions for Parallel Agents

### For Each Life Pattern Build

1. **Read this schema document** as your sole structural reference.
2. **Read the exemplar** (`sharecropping_trap.json`) as your content template.
3. **Read the source strain(s)** from `NARRATIVE_STRAINS.md` (strain numbers listed in the Build Plan).
4. **Read the referenced material_life and community_texture files** for cross-referencing.
5. **Build the JSON file** following the schema exactly.
6. **Validate** that all cross-references (trigger_refs, material_life_refs, community_texture_refs, fed_by_triggers, activates_triggers) reference files that actually exist.

### Content Standards

- **Target length**: 200-250 lines of JSON (similar to material_life files in depth)
- **Lifecycle phases**: 3-5 phases, each with 3-5 sentences of description
- **The Accuracy Line**: Facts from records are SACRED. Context uses "likely," "probably," "typically."
- **Sourced details**: Every detail in daily_life, economic_trajectory, and family_dynamics must have a source citation
- **Chain-link completeness**: Every entry_condition must reference at least one existing trigger or pattern. Every exit_condition must reference at least one trigger or pattern.
- **Narrative hooks**: 4-6 hooks per file, each with at least one {variable} placeholder
- **Counter-narratives**: 2-4 per file, correcting common genealogical or historical misconceptions
- **Variable placeholders**: Use the standard NEL variables: `{ancestor_name}`, `{origin_county}`, `{destination_city}`, `{year}`, `{decade}`, `{state}`, `{pronoun_subject}`, `{pronoun_object}`, `{pronoun_possessive}`

### File Naming Convention

```
/home/dbcanady/kinlore-data/narrative_enrichment/life_patterns/{pattern_id}.json
```

All files go in the `life_patterns/` directory (not in `migration_triggers/`).

### Cross-Reference Integrity

When referencing triggers, use the exact `migration_id` from the trigger file. When referencing material_life, use the exact `material_life_id`. When referencing community_texture, use the exact filename without `.json`. When referencing other Life Patterns, use the exact `pattern_id`.

Existing trigger migration_ids available for cross-referencing:
```
antebellum_yeoman_south, appalachian_out_migration, boll_weevil, bracero_program,
chinese_exclusion_era, civil_war_displacement, civil_war_service, domestic_slave_trade,
dust_bowl, economic_panics_19c, economic_panics_20c, german_immigration,
gi_bill_migration, gilded_age_labor_conflict, gold_rush_mining_boom, great_migration,
homestead_act, indian_removal_trail_of_tears, irish_famine, jewish_pogrom_flight,
mormon_migration, oklahoma_land_runs, puerto_rican_migration, railroad_construction,
reconstruction_era, scots_irish_frontier, se_european_wave, stayed_and_adapted,
textile_mill_recruitment, war_of_1812_service, widow_orphan_relocation, wwii_relocation
```

Existing material_life_ids available:
```
antebellum_plantation_1820_1860, antebellum_yeoman_farm_1820_1860,
chinatown_bachelor_society_1870_1940, coal_camp_appalachia_1880_1930,
dust_bowl_farmstead_1920_1940, free_black_community_1790_1865,
frontier_log_cabin_1780_1840, great_depression_urban_1929_1941,
great_migration_urban_1920_1960, homestead_sodhouse_1862_1900,
immigrant_tenement_1845_1890, industrial_city_1880_1920,
mining_camp_1848_1900, postbellum_southern_farm_1865_1910,
postwar_suburban_1945_1970, railroad_section_hand_camp_1870_1920,
sharecropper_cabin_1865_1940, small_town_merchant_1830_1920,
southern_mill_village_1880_1930, wwii_homefront_1941_1945
```

Existing community_texture files available (use filename without .json):
```
appalachian_coal_camp, birmingham_iron_steel_community, boston_irish_1845_1900,
cajun_prairie_community, chicago_black_bronzeville, chicago_polish_1870_1920,
cincinnati_appalachian_enclave, deep_south_black_community, detroit_black_paradise_valley,
dust_bowl_oklahoma, east_tennessee_mountain_community, eastern_ky_coal_community,
eastern_nc_farm_community, fayetteville_mill_district, german_midwest_1848_1900,
great_plains_homesteader, harlem_new_york, illinois_downstate_farm_community,
memphis_beale_street_community, minnesota_scandinavian_community,
mississippi_delta_cotton, new_york_lower_east_side, pa_anthracite_patch_town,
pa_dutch_lehigh_valley, piedmont_mill_village, pittsburgh_slavic_steel,
rural_georgia_black_belt, sc_upcountry_farm_community, scots_irish_frontier,
shenandoah_valley_farm_community, texas_german_hill_country,
west_coast_chinatown_bachelor_society, wwii_defense_boomtown
```

---

*This document is the sole reference for Phase 4 Life Pattern builds. No additional design documents are needed. Build agents should read this document, the exemplar, and the relevant source strain(s) before beginning each file.*
