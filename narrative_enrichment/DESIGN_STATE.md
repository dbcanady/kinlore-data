# Narrative Enrichment Layer — Design State

**Sprint 1 Complete: 2026-03-16**
**Sprint 2B Complete: 2026-03-16**
**Schema Version: 1.0**

## What Was Built

### Sprint 1 — Migration Decision Trees
Machine-readable data that lets KinLore's narrative AI explain *why* an ancestor moved, *how* they got there, *what work they found*, and *what the destination looked like when they arrived*.

### Sprint 2B — Templates, Research Guidance, Wage Tables, Gap Fixes
Deepens the 17 existing triggers with narrative templates, actionable research advice, historical wage data, and 5 content fixes from expert spot-check review.

### Combined Inventory

| Category | Files | Total Lines | Location |
|----------|------:|------------:|----------|
| Core triggers | 17 | 3,575 | `migration_triggers/core/` |
| Routes | 8 | 429 | `migration_triggers/shared/routes/` |
| Destinations | 11 | 1,494 | `migration_triggers/shared/destinations/` |
| Occupations | 10 | 1,035 | `migration_triggers/shared/occupations/` |
| Stress tests | 1 (7 tests) | 211 | `migration_triggers/_validation/` |
| **Templates** | **4** | **870** | `migration_triggers/templates/` |
| **Research guidance** | **10** | **1,469** | `migration_triggers/research_guidance/` |
| **Wage tables** | **3** | **1,645** | `migration_triggers/shared/wages/` |
| **Total** | **64** | **10,713** | |

All 64 files are valid JSON. Schema version 1.0 throughout.

## Sprint 1 Spot-Check Gaps — RESOLVED

| # | Issue | File | Priority | Status |
|---|-------|------|----------|--------|
| 1 | Quebec/Grosse Île back-door route missing from record_implications | irish_famine.json | HIGH | RESOLVED — Added Canadian arrival records entry with LAC, Grosse Île Memorial, Boston Pilot 'Missing Friends' column |
| 2 | Destination counties missing for receiving end | domestic_slave_trade.json | HIGH | RESOLVED — Added `destination_counties_most_affected` array (Adams MS, Orleans Parish LA, etc.) with note |
| 3 | "Information Wanted" ads deserve own record_implications entry | domestic_slave_trade.json | MEDIUM | RESOLVED — Added entry citing Christian Recorder, SW Christian Advocate, Last Seen project at Villanova |
| 4 | Empty destination_refs, mill towns need profiles | textile_mill_recruitment.json | MEDIUM | RESOLVED — Added 4 mill_town_profiles (Kannapolis, Gastonia, Lancaster, Graniteville) with sensory_snapshot, institutions |
| 5 | involuntary: false needs coercion context | Schema-level | LOW | RESOLVED — Added optional `coercion_note` field to irish_famine.json and dust_bowl.json |

## Core Triggers (17 files)

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

### Migration Classes
- **immigration** (4): Transatlantic/transoceanic arrivals
- **economic** (5): Driven by economic forces — wages, mechanization, panics
- **military** (2): War-related displacement and relocation
- **racial_flight** (1): Fleeing racial violence and Jim Crow
- **forced** (1): Enslaved people moved against their will
- **disaster** (1): Environmental catastrophe
- **land_opportunity** (1): Free/cheap land pull
- **family** (1): Kinship obligation (widows, orphans)

## Templates (4 files) — Sprint 2B

| Template | Lines | Situations/Variants | Revenue Tier |
|----------|------:|--------------------:|-------------|
| letter_home | 283 | 7 situations | Both ($29 short, $99 full) |
| record_silences | 352 | 6 gap types | Both ($29 brief, $99 expanded) |
| what_they_saw | 147 | 2 variants (departure + arrival) | Both ($29 one, $99 both) |
| fork_in_the_road | 88 | 1 (counterfactual) | Both ($29 paragraph, $99 with stats) |

**letter_home**: 7 situation types (arrival, family arrival, send-for-family, homesick, settled update, bad news, return visit). All outputs prefixed with `[Illustrative — not from an actual letter]`. No letters for enslaved ancestors (use Record Silences instead). Voice calibration adjusts for era, region, occupation, ethnicity, literacy.

**record_silences**: 6 gap types (between censuses, woman disappears, child vanishes, complete disappearance, 1890 gap, enslaved ancestor gap). Ranked explanations with research actions. The enslaved ancestor gap section includes dignity mandate and explicit instructions to name the slaveholder.

**what_they_saw**: Dense physical landscape descriptions, 100-150 words, present tense, no people. Departure landscape (the place they left) and arrival landscape (first view of destination).

**fork_in_the_road**: Counterfactual paragraph grounded in documented demographic/economic changes. "Had {ancestor_name} remained in {county}..." No individual speculation — only the place's fate.

## Research Guidance (10 files) — Sprint 2B

| File | Patterns | Source Refs |
|------|:--------:|:----------:|
| census_gaps | 8 | 5 |
| city_directory_strategies | 6 | 4 |
| church_record_transfers | 6 | 5 |
| vital_record_variations | 7 | 4 |
| name_change_patterns | 7 | 5 |
| military_record_strategies | 7 | 5 |
| newspaper_strategies | 6 | 5 |
| property_record_strategies | 6 | 5 |
| institutional_records | 7 | 5 |
| ethnic_specific_sources | 9 | 5 |
| **Total** | **69 patterns** | **48 refs** |

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
2. **Trigger matching**: Compare ancestor's origin county, era, occupation, and race against the 17 trigger files. Multiple triggers may match.
3. **Route selection**: Use the trigger's `route_refs` to pull transportation details
4. **Destination lookup**: Use `destination_refs` to pull neighborhood, employer, and institutional context
5. **Occupation enrichment**: Match ancestor's listed occupation against the 10 occupation profiles
6. **Wage contextualization**: Pull wage data from the 3 wage tables to ground economic comparisons
7. **Template selection**: Choose appropriate narrative templates (Letter Home, What They Saw, Fork in the Road, Record Silences) based on available records and detected gaps
8. **Research guidance**: When record gaps are detected, pull actionable research advice from the 10 guidance files
9. **Narrative generation**: Feed all matched data into the narrative AI with Accuracy Line constraints
10. **Counter-narrative injection**: Include at least one counter-narrative per trigger

## What Is NOT Built (Deferred)

### Track B — Life Patterns (deferred to $99 tier)
~20 non-migration patterns from Narrative Strains: Boarding House Matriarch, Sharecropping Trap, Domestic Service arc. Essential for multi-generational $99 reports. Not needed for $29 single-ancestor reports.

### Placeholder directories (Sprint 2+)
- `deep_dives/` — Extended narratives for specific triggers

### Sprint 2A — New triggers (not yet scheduled)
Adding triggers beyond the initial 17. Candidates: Gold Rush, Mormon migration, Oklahoma Land Run, Bracero Program, Puerto Rican migration, Vietnamese refugee resettlement.

## Sprint 2A Readiness Assessment

### Is the existing data sufficient for the $29 product to ship?
**Yes.** The 17 triggers cover the most common migration patterns in American genealogy (1717-1970). The 11 destination cities are the primary magnets. The 10 occupations are the jobs ancestors held. The 4 templates generate the speculative/interpretive content. The 10 research guidance files handle record gaps. The 3 wage tables ground economic context. A $29 report centered on one ancestor's migration story has everything it needs.

### What's the minimum viable dataset for a production $29 report?
- 1 matched trigger (push/pull factors, route, destination)
- 1 destination city profile (neighborhood, employer, institutions)
- 1 occupation profile (daily work, wages, conditions)
- 1-2 template outputs (Letter Home + Fork in the Road or What They Saw)
- Wage comparison (origin vs. destination)
- 1 Record Silences interpretation (if gaps detected)

### What's blocking the $99 tier?
**Track B / Life Patterns.** The $99 report is multi-generational. Between migrations, ancestors lived in one place for decades. The narrative AI needs Life Pattern data (Boarding House Matriarch, Sharecropping Trap, etc.) to fill those narrative gaps. Track B is correctly deferred to the $99 revenue tier because the data serves that tier exclusively.

## Relationship to Other Data Layers

- **Layer 1 — County Source Profiler** (COMPLETE, 56 builds, 19,929 profiles): Tells the narrative AI *where to look* for records
- **Layer 2 — Historical Context Timelines** (COMPLETE, 56 files): Provides decade-by-decade background for every state
- **Layer 3 — Migration Decision Trees + Enrichment** (SPRINTS 1 + 2B COMPLETE): Explains *why* people moved, *how* they traveled, *what they found*, and provides templates, research guidance, and economic context
