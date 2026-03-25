# Narrative Enrichment Layer -- Polsia Integration Guide

**Version: 1.2**
**Schema Version: 1.0 (all data files)**
**Last Updated: 2026-03-25**
**Total Files: 338 (333 JSON + 2 guides + 1 validator + 2 schema docs) | Total Lines: ~55,000**

This document governs how Polsia processes ancestor records through the Narrative Enrichment Layer (NEL). Read this FIRST. It tells you what exists, how to use it, and what rules you must follow.

---

## 1. What This Repository Contains

333 JSON data files (plus 2 Markdown guides, 1 Python validator, and 2 schema docs) organized by function:

```
migration_triggers/
  core/                     32 core migration triggers
  regional/                 14 state directories with 19 regional triggers
    nc/                      6 NC regional triggers
    va/                      1 (Shenandoah Valley westward)
    oh/                      1 (Appalachian to river cities)
    sc/                      1 (Upcountry farm to mill)
    ga/                      1 (Rural to Atlanta)
    ky/                      1 (Eastern coal exodus)
    tn/                      1 (Mountain to industrial)
    ms/                      1 (Delta to southern cities)
    tx/                      1 (German Hill Country)
    mn/                      1 (Scandinavian settlement)
    pa/                      1 (Anthracite exodus)
    al/                      1 (Black Belt to Birmingham)
    la/                      1 (Cajun/Acadian settlement)
    il/                      1 (Downstate to Chicago)
  shared/
    destinations/           82 destination city profiles
    occupations/            27 occupation profiles
    routes/                 25 transportation route files
    community_texture/      33 community texture profiles
    material_life/          19 material life era/region profiles
    wages/                   3 wage and cost-of-living tables
  templates/                11 narrative templates (22 situations + 5 audience profiles)
  research_guidance/        10 research guidance files (70 patterns, 50 source refs)
  _validation/               1 cross-reference validator
  _gap_detection/            2 files (guide + schema)
  dry_runs/                  9 files (8 ancestor dry runs + analysis)

life_patterns/              22 Life Pattern files (settled-life arcs between migrations)
                             Schema: life_patterns/LIFE_PATTERN_SCHEMA.md

ethnic_heritage/            46 ethnic heritage profiles (cultural context by ancestry group)
                             1 index: ETHNIC_HERITAGE_INDEX.json
                             Schema: ethnic_heritage/ETHNIC_HERITAGE_SCHEMA.md
```

**Coverage:** ~97% of American genealogy migration patterns, 1717-1970. 32 core triggers + 19 regional triggers span 9 migration classes: immigration, economic, military, racial_flight, forced, disaster, land_opportunity, religious, labor_immigration, and family. Regional triggers cover 14 states with hyper-local intra-state migration patterns. 22 Life Patterns cover the settled-life arcs that unfold BETWEEN migrations — what happened while people stayed. Life Patterns connect to triggers through chain-link architecture (entry/exit conditions), enabling continuous multi-generational narrative chaining. 46 Ethnic Heritage profiles provide culturally-specific context for 11 heritage group categories (colonial British, Germanic, Irish, Scandinavian, Southern/Eastern European, Slavic/Baltic, African American, French/Acadian, Asian American, Latin American, and other), enriching narratives with immigration waves, naming conventions, church records, occupational patterns, and cultural markers.

For the full inventory with line counts, file lists, and build history, see `DESIGN_STATE.md`.

---

## 2. The Ancestor Processing Pipeline

**Input:** An ancestor record containing: name, dates (birth, marriage, death), locations (origin, destination), occupation, race/ethnicity, and any known record gaps.

Process the ancestor through all 12 steps below. Steps 1-11 gather data. Step 12 is mandatory reporting.

### Step 1: Trigger Matching

Compare the ancestor's origin county, era, occupation, ethnicity, and race against:
- 32 core triggers in `core/` (national-level migration patterns)
- 19 regional triggers in `regional/[state]/` (state-level micro-patterns across 14 states)

Multiple triggers may match. Rank by era overlap and geographic specificity. Regional triggers supplement (not replace) national triggers -- they provide finer-grained push factors for intra-state movement.

Each trigger contains: push/pull factors with severity scores (1-5), affected counties, era range, route references, destination references, occupation references, counter-narratives, record implications, and narrative hooks.

### Step 2: Ethnic Heritage Matching

After trigger matching (and ideally after identifying the ancestor's surname, origin, denomination, and settlement area), match the ancestor against the 46 ethnic heritage profiles in `ethnic_heritage/`.

**When to use:** Apply ethnic heritage matching to EVERY ancestor. Most ancestors will match at least one heritage profile. Some will match multiple (e.g., a Scots-Irish Quaker in the Shenandoah Valley matches both `scots_irish` and `quaker`).

**How to match:** Use the `identification_clues` fields in each profile (or consult `ETHNIC_HERITAGE_INDEX.json` for a consolidated lookup table). Match on:

- **surname_patterns** — Does the ancestor's surname match known patterns? (e.g., Mc/Mac patronymics signal Scots-Irish; -ski/-wicz signal Polish)
- **denomination_signals** — Does the ancestor's church affiliation signal a specific heritage? (e.g., Lutheran + German surname = likely Germanic heritage)
- **settlement_signals** — Was the ancestor in a known heritage concentration area? (e.g., Shenandoah Valley = Scots-Irish or German Colonial)
- **record_signals** — Do the available records contain heritage markers? (e.g., parish records in Norwegian, naturalization from specific ports)
- **occupation_signals** — Does the ancestor's occupation signal a specific heritage? (e.g., linen weaver = Scots-Irish; turpentine laborer in NC = likely African American)

A single strong signal (surname + denomination match) is sufficient. Two or more weak signals from different clue categories also warrant a match.

**What each profile provides:**
- Immigration overview with specific waves, push/pull factors, ports of entry, and journey descriptions
- Settlement patterns with chain migration networks and clustering factors
- Church and records guidance (denominations, record languages, key repositories, survival notes)
- Naming conventions with Americanization patterns and common research traps
- Occupational patterns by era with economic mobility trajectory
- Cultural markers (foodways, traditions, social organizations, material culture)
- Intermarriage patterns and genealogical pitfalls
- Cross-references to triggers, community textures, material life profiles, life patterns, and regional landscape clusters

**How ethnic heritage interacts with other layers:** Ethnic heritage profiles provide the cultural WHY that enriches every other pipeline step:

- **Triggers (Step 1):** Heritage profiles explain why a specific ethnic group was susceptible to a given trigger. A `german_colonial` profile explains why German settlers in the Shenandoah responded differently to the `scots_irish_frontier` trigger than their Scots-Irish neighbors.
- **Routes (Step 3):** Heritage profiles name the ports of entry and typical journey patterns that connect to route files.
- **Destinations (Step 4):** Heritage settlement patterns explain WHY an ancestor ended up in a specific destination and what community awaited them.
- **Occupations (Step 5):** Heritage occupational clustering explains industry concentration patterns that supplement individual occupation profiles.
- **Life Patterns (Step 7):** Heritage intermarriage timelines and economic mobility arcs add cultural depth to settled-life patterns.
- **Community Texture (Step 8):** Heritage profiles name the churches, fraternal orders, and mutual aid societies that appear in community texture profiles — and explain their cultural significance.
- **Templates (Step 10):** Heritage naming conventions feed directly into the `naming_as_evidence` template. Heritage immigration waves enrich `letter_home` and `what_they_saw` templates.

Each profile's `nel_cross_references` section contains explicit links to related triggers, community textures, material life profiles, life patterns, and regional landscape clusters. Use these cross-references to pull heritage-specific context into every narrative layer.

### Step 3: Route Selection

Use the matched trigger's `route_refs` to pull transportation details from `shared/routes/`. 25 route files cover: overland trails, railroads, steamboats, canals, ocean crossings, intercity bus, and Pacific routes.

Select the route that best matches the ancestor's origin-to-destination geography and era. If the trigger references multiple routes, prefer the one whose era range most closely aligns with the ancestor's travel year.

### Step 4: Destination Lookup

Match the ancestor's destination city or county against the 82 destination profiles in `shared/destinations/`. Each profile contains: neighborhoods, major employers by era, institutions (churches, schools, mutual aid), housing stock, and a sensory snapshot.

If no exact city match exists, check `alternate_ids` within existing profiles. Some profiles cover broader metro areas.

### Step 5: Occupation Enrichment

Match the ancestor's listed occupation against 27 occupation profiles in `shared/occupations/`. Census occupation titles vary wildly across decades -- match on the closest equivalent. Each profile contains: daily work description, wages by era, working conditions, career trajectory, health risks, and narrative hooks.

### Step 6: Material Life Grounding

Match the ancestor's era + region against the 19 material life profiles in `shared/material_life/`. These provide the physical reality of daily existence: housing, food, clothing, hygiene, transportation, communication, entertainment, and household goods.

Multiple profiles may apply if the ancestor lived across eras or moved between regions. Each profile cross-references its associated triggers via `trigger_refs`.

### Step 7: Life Pattern Matching

If the ancestor STAYED in one place for an extended period (roughly a decade or more between migrations), match them against the 22 Life Pattern files in `life_patterns/`. Life Patterns describe what happened while people lived in one place — the economic arcs, family dynamics, community patterns, and occupational lifecycles that unfolded between migrations.

**When to match:** A Life Pattern applies when the ancestor's records show continuous residence in the same county or community across multiple census years, OR when the ancestor matches a known settled-life pattern (sharecropping, company-town life, homesteading, etc.) regardless of explicit census evidence.

**How to match:** Compare the ancestor's era, region, race/ethnicity, occupation, and economic trajectory against the `population`, `era_range`, `regions`, and `pattern_class` fields. Multiple Life Patterns may apply (e.g., a family might experience `yeoman_farming_stability` followed by `appalachian_subsistence_squeeze` across generations).

Each Life Pattern contains:
- **Lifecycle phases** (3-5 phases): The arc of the pattern over time, each with description, record signatures, and a narrative hook
- **Entry conditions**: What prior event feeds into this pattern — references existing triggers and other Life Patterns via `fed_by_triggers` and `fed_by_patterns`
- **Exit conditions**: What this pattern produces that becomes the next generation's push factor — references triggers via `activates_triggers` and other patterns via `activates_patterns`
- **Chain examples**: Concrete multi-generational chains showing the pattern in context
- **Daily life, economic trajectory, family dynamics**: Sourced content sections for narrative enrichment
- **Record signatures, cultural markers, counter-narratives**: Standard NEL content fields

**Chain-link architecture:** Entry and exit conditions are the connective tissue of multi-generational narratives. When processing a White Glove multi-generational report, use the chain-link fields to connect triggers and Life Patterns across generations:

```
trigger → life_pattern → trigger → life_pattern
```

For example: `scots_irish_frontier` (trigger) → `yeoman_farming_stability` (life pattern) → `civil_war_displacement` (trigger) → `sharecropping_trap` (life pattern) → `great_migration` (trigger).

Match entry conditions by checking if the ancestor's PRIOR trigger match appears in the Life Pattern's `fed_by_triggers` array. Match exit conditions by checking if the ancestor's NEXT migration matches any `activates_triggers` in the current Life Pattern's exit conditions. The `generation_lag` field indicates whether the exit activates in the same generation, next generation, or two generations later.

**Pattern classes:**

| Class | Description |
|-------|-------------|
| `economic_arc` | Patterns defined by economic trajectory — accumulation, stability, decline, or trap |
| `family_dynamic` | Patterns defined by how family structure changes over time |
| `community_pattern` | Patterns defined by how communities form, sustain, or dissolve |
| `occupational_lifecycle` | Patterns defined by a specific occupation's arc over a career |
| `social_transformation` | Patterns defined by large-scale social or structural change experienced while staying |

### Step 8: Community Texture

Match the ancestor's settled community against the 33 community texture profiles in `shared/community_texture/`. These provide institutional fabric: churches (denomination, founding date), schools, fraternal orders, newspapers, mutual aid societies, and social geography.

Three types: `destination_enclave` (ethnic/racial community at destination), `industrial_community` (company town, mill village), `origin_community` (the place they left).

### Step 9: Wage Contextualization

Pull wage and cost-of-living data from the 3 files in `shared/wages/`:
- `wages_1850_1900.json` -- 33 occupation entries, 20 benchmarks
- `wages_1900_1950.json` -- 35 occupation entries, 21 benchmarks
- `cost_of_living.json` -- 102 benchmarks across eras

Always present wages in context. "A mill operative's $1/day" means nothing without "when a pound of flour cost 3 cents." Every wage comparison must pair the wage with a contemporary cost benchmark from `cost_of_living.json`.

### Step 10: Template Selection

Choose narrative templates from the 10 in `templates/` based on what the ancestor's records reveal:

| Template | Use When | Situations |
|----------|----------|-----------|
| `letter_home` | Migration stories | 8 (arrival, family arrival, send-for-family, homesick, settled update, bad news, return visit, first job) |
| `what_they_saw` | Departure/arrival landscapes needed | 2 (departure + arrival) |
| `fork_in_the_road` | Counterfactual enrichment | 1 ("Had they stayed...") |
| `record_silences` | Record gaps detected | 6 gap types |
| `military_service_arc` | Veteran ancestors | 5 (enlistment to community return) |
| `document_deep_read` | Single rich document exists | 3 (source contradiction, paper trail, deep read) |
| `economic_life_story` | Economic trajectory or remarriage | 3 (economic failure, remarriage economics, status transformation) |
| `naming_as_evidence` | Naming patterns reveal connections | 3 |
| `convergence` | Multiple family lines meet | 3 (White Glove primarily) |
| `audience_adapter` | Output needs audience adjustment | 5 audience profiles |

Template constraints:
- `letter_home`: All outputs prefixed with `[Illustrative -- not from an actual letter]`. No letters for enslaved ancestors (use `record_silences` instead).
- `audience_adapter`: Modifies OTHER template outputs for specific audiences. It is a post-processor, not standalone.
- `convergence`: White Glove exclusive.

### Step 11: Research Guidance

When record gaps are detected, pull actionable research advice from the 10 files in `research_guidance/`. Files cover: census gaps, city directories, church records, vital records, name changes, military records, newspapers, property records, institutional records, and ethnic-specific sources.

Every action step names the repository, record group, and access method. Common mistakes are called out per pattern. Advice is era-scoped to prevent anachronistic suggestions.

### Step 12: Gap Detection (MANDATORY)

After completing the pipeline, check what COULD NOT be matched. This step runs after EVERY ancestor, regardless of how complete the matches were.

Follow `_gap_detection/GAP_DETECTION_GUIDE.md` to generate structured gap reports per `_gap_detection/gap_report_schema.json`. Append to `gap_reports.jsonl`.

Gap severity levels:
- **HIGH** -- No trigger match at all. Narrative has almost no historical context.
- **MEDIUM** -- Trigger matched but missing a key dimension (destination, occupation, route).
- **LOW** -- Existing data covers it approximately. A dedicated file would improve quality.

Build thresholds: HIGH + frequency >= 3 = BUILD NOW. Any severity + frequency >= 10 = BUILD NOW.

Do not let gaps block narrative generation. Generate the best narrative with available data, then report the gap.

---

## 3. The Accuracy Line

These constraints are non-negotiable. They govern every word of output.

**Facts from records are SACRED.** Context uses "likely", "probably", "the pattern suggests." Never upgrade contextual inference to factual certainty.

**No emotional projection.** Acceptable: "{ancestor_name} likely left because the mines were closing." Unacceptable: "{ancestor_name} felt heartbroken to leave." The records do not contain feelings. Do not fabricate them.

**Counter-narratives are required.** Every trigger includes at least 2 counter-narratives. Every template includes constraints preventing one-dimensional storytelling. Not every Irish immigrant was fleeing famine. Not every Great Migration participant was fleeing violence. State the dominant pattern, then state the exceptions.

**Confidence levels must be explicit.** Use "suggests" and "is consistent with." Never use "proves." The phrase "the records show" is reserved for direct documentary evidence.

**Source standards:** Minimum 3 academic sources per trigger, destination, and occupation. Zero Wikipedia. All wage figures cite their source (BLS, state labor commissions, USDA, published monographs).

---

## 4. Revenue Tier Handling

Two tiers. Different depth, same accuracy standard.

**Option A (single-ancestor report):**
- One matched trigger, one template output per applicable category
- 80-150 words per template situation
- Briefer treatment of material life, community texture, and wage context
- Record Silences: brief 2-sentence interpretation of the most significant gap

**White Glove (multi-generational report):**
- All matched triggers AND Life Patterns across the family, full template treatment
- 100-250 words per situation, all applicable situations rendered
- `convergence` template and `audience_adapter` gift_recipient profile are White Glove exclusive
- Record Silences: full 80-200 word treatment of all applicable gaps
- **Chain-link narrative threading**: Use Life Pattern entry/exit conditions to connect generations. For each ancestor in the family line, check whether the previous ancestor's trigger or Life Pattern exit conditions feed into the current ancestor's Life Pattern entry conditions. Build the narrative chain explicitly: "The conditions that held the {family_name} family in {county} for {number} decades were the same conditions that eventually propelled the next generation toward {destination_city}." The `chain_examples` field in each Life Pattern provides concrete models.

**NEVER reference dollar amounts ($29, $99) in narrative output.** Use "Option A" and "White Glove" as internal tier labels only. These labels do not appear in customer-facing text.

---

## 5. Race-Aware Routing

Several triggers and community textures include race-specific routing logic. This is not optional -- it reflects documented historical reality.

**African American ancestors:**
- `textile_mill_recruitment` routes to racial exclusion note (Black workers were barred from most Piedmont mills until the 1960s)
- NC regional triggers route to alternative migration paths (Black farm workers had different destination options than white workers)
- `great_migration` and `boll_weevil` have race as primary driver
- `deep_south_black_community` and `mississippi_delta_cotton` community textures provide origin-community institutional detail

**Forced and violent triggers carry a dignity mandate:**
- `domestic_slave_trade` -- Enslaved people are named as people, not property. Slaveholders are named. Economic language ("sold", "traded") is used without euphemism but with dignity.
- `indian_removal_trail_of_tears` -- Forced removal is stated as forced removal. Tribal sovereignty acknowledged. Cherokee, Choctaw, Chickasaw, Creek, and Seminole nations are named specifically.
- `nc_wilmington_1898_exodus` -- The 1898 coup is described as a coup. Perpetrators are named. The narrative does not "both sides" a massacre.

**Enslaved ancestor gaps in `record_silences`:**
- The enslaved ancestor gap type includes specific handling instructions
- Slaveholders must be named when known -- they are the access point to records
- The absence of records IS the story. Do not paper over it.

---

## 6. Gap Detection (Mandatory Step)

Full instructions: `_gap_detection/GAP_DETECTION_GUIDE.md`
Report schema: `_gap_detection/gap_report_schema.json`
Output file: `_gap_detection/gap_reports.jsonl` (JSON Lines format, one object per line)

Key rules:

1. Run gap detection after EVERY ancestor processing run. No exceptions.
2. Generate one structured gap report per the schema. Include ancestor context (era, origin, destination, occupation, ethnicity, race).
3. Be specific in the `searched_for` field. "Missing occupation" is useless. "Missing occupation profile for 'tanner' (ancestor in Pennsylvania, 1850-1880)" is actionable.
4. Deduplicate before appending. If the same `gap_type` + `searched_for` exists, increment frequency rather than creating a duplicate.
5. Include `nearest_match` -- the closest existing file. This tells future builders what schema to follow.
6. Known gaps are listed in the Gap Detection Guide. Do not re-report them unless frequency tracking requires it.

The gap detection system is the NEL's self-improvement mechanism. Gap reports accumulate, get priority-scored (severity x frequency), and become build targets for Claude Code CLI sessions. Every ancestor that hits a gap teaches the system what to build next.

---

## 7. Variable Placeholder Syntax

All narrative hooks in triggers, templates, and profiles use `{variable}` placeholders. Replace these with actual ancestor data before generating output.

Standard variables:
- `{ancestor_name}` -- Full name
- `{surname}` -- Family name only
- `{given_name}` -- First name only
- `{year}` -- Relevant year (context-dependent)
- `{county}` -- County name
- `{origin_county}` -- County of origin
- `{destination}` -- Destination city or county
- `{occupation}` -- Occupation as listed in records

Any `{variable}` remaining in output text is a bug. Every placeholder must resolve to a value or be removed (with the surrounding sentence rewritten) before the narrative reaches the customer.

---

## 8. Schema Reference

- **Schema version:** 1.0 throughout all 333 JSON files
- **Data format:** JSON (all data files). Markdown (guide documents only).
- **Push/pull factor severity scale:** 1 = minor influence, 5 = catastrophic/overwhelming. Measures historical severity, not build priority. Also used for Life Pattern exit condition severity.
- **Priority scale (County Source Profiler, Layer 1):** 1-3 (NOT 1-5). Do not confuse with push/pull severity.
- **Era ranges:** Expressed as `"era_start"` / `"era_end"` integers (years) within each trigger and profile. Life Patterns use `"era_range"` string format (e.g., "1865-1940").
- **Route references:** Triggers contain `route_refs` arrays pointing to filenames in `shared/routes/`.
- **Destination references:** Triggers contain `destination_refs` arrays pointing to filenames in `shared/destinations/`.
- **Cross-references:** Material life profiles contain `trigger_refs`. Community textures contain `associated_triggers`. Life Patterns contain `trigger_refs`, `material_life_refs`, and `community_texture_refs`. These are bidirectional pointers for validation.
- **Chain-link references (Life Patterns only):** `entry_conditions[].fed_by_triggers` and `entry_conditions[].fed_by_patterns` link backward; `exit_conditions[].activates_triggers` and `exit_conditions[].activates_patterns` link forward. These are the connective tissue for multi-generational narratives.
- **Life Pattern classes:** `economic_arc`, `family_dynamic`, `community_pattern`, `occupational_lifecycle`, `social_transformation`
- **Life Pattern schema:** Full schema definition at `life_patterns/LIFE_PATTERN_SCHEMA.md`
- **Ethnic Heritage profiles:** 46 profiles in `ethnic_heritage/` covering 11 group categories. Each profile contains `identification_clues` (surname, denomination, settlement, record, and occupation signals), `nel_cross_references` linking to triggers, community textures, material life, life patterns, and regional landscape clusters. Index at `ethnic_heritage/ETHNIC_HERITAGE_INDEX.json`. Schema at `ethnic_heritage/ETHNIC_HERITAGE_SCHEMA.md`.

Full schema details, file-by-file inventory, and build history: `DESIGN_STATE.md`
Roadmap and phase planning: `NEL_ROADMAP.md`
