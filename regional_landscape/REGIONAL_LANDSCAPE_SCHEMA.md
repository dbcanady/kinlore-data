# KinLore Layer 4: Regional Landscape Profiles — Schema & Architecture

**Version**: 1.0
**Date**: 2026-03-19
**Status**: Schema Complete — SE NC Coastal Plain Pilot Under Construction

---

## Purpose

Regional Landscape Profiles are the Layer 4 enrichment data for the KinLore Narrative Enrichment Layer. They describe **what a specific place looked, felt, and functioned like** at specific points in time — the physical geography, economic rhythms, transportation networks, information channels, migration pathways, record survival, and seasonal calendars that grounded an ancestor's life in a real, tangible place.

Layer 3 (NEL) answers: *Why did they move, how, and what did they find?*
Layer 4 answers: *What did the land look and feel like where they lived?*

A KinLore narrative without Layer 4 says: "The family farmed in eastern North Carolina."
A KinLore narrative WITH Layer 4 says: "The family farmed sandy loam on the Neuse River plain, where the longleaf pine had been cut back just far enough to plant tobacco rows that ran to the tree line, and the nearest newspaper was a two-day wagon ride away in Goldsboro."

---

## Architecture: Separate Layer, Graceful Fallback

Layer 4 is an **independent, optional enrichment layer** — not embedded inside the NEL.

```
/home/dbcanady/kinlore-data/
    data/                          ← Layer 1: County Source Profiler
    enrichment/historical_context/ ← Layer 2: Historical Context Timelines
    narrative_enrichment/          ← Layer 3: NEL (triggers, patterns, templates)
    regional_landscape/            ← Layer 4: Regional Landscape Profiles (THIS)
```

**The rule:** Polsia checks the county-to-region index. If the ancestor's county has a cluster → load and use the profiles. If not → skip this step entirely. The narrative is always solid from Layers 1-3; Layer 4 is bonus depth.

This is like satellite imagery resolution — high-res where it's been built, standard resolution everywhere else. Both work. One is richer.

---

## Directory Structure

```
regional_landscape/
    REGIONAL_LANDSCAPE_SCHEMA.md          # This document
    REGIONAL_LANDSCAPE_INDEX.json         # County-to-region lookup
    _validation/
        validate_regional_landscape.py    # Standalone validator
    {cluster_id}/                         # One directory per regional cluster
        county_landscape/                 # 1 file per county — physical geography
            {county}.json
        local_economy/                    # 1 file per cluster — economic eras
            {cluster_id}_economy.json
        road_connectivity/                # 1 file per cluster — transportation
            {cluster_id}_roads.json
        information_landscape/            # 1 file per cluster — how news traveled
            {cluster_id}_information.json
        micro_migration/                  # 1 file per cluster — county-to-county chains
            {cluster_id}_migration_networks.json
        courthouse_atlas/                 # 1 file per county — records survival
            {county}.json
        seasonal_calendar/                # 1 file per cluster — month-by-month rhythms
            {cluster_id}_seasons.json
        cultural_markers/                 # 1 file per cluster — denomination, naming, foodways
            {cluster_id}_culture.json
        hidden_history/                   # 1 file per cluster — events that explain record gaps
            {cluster_id}_hidden.json
```

### File Granularity

**Per-county files** (physical facts that differ by county):
- County Landscape Profiles — geography, soil, waterways, sensory snapshots
- Courthouse & Records Survival Atlas — fires, floods, what survived

**Per-cluster files** (regional patterns shared across counties):
- Local Economy Timelines — decade-by-decade economic snapshots
- Road & Connectivity Networks — transportation infrastructure
- Information Landscape Profiles — newspapers, literacy, communication
- Micro-Migration Network Maps — county-to-county chains
- Seasonal Calendar Profiles — month-by-month rhythms

For a 9-county cluster, this yields **25 files** (9 + 1 + 1 + 1 + 1 + 9 + 1 + 1 + 1).

### Naming Conventions

- Cluster directories: `{region}_{state}_{descriptor}` in snake_case (e.g., `se_nc_coastal_plain`)
- County files: `{county_name_lowercase}.json` (e.g., `wayne.json`)
- Regional files: `{cluster_id}_{type}.json` (e.g., `se_nc_coastal_plain_economy.json`)
- Index: `REGIONAL_LANDSCAPE_INDEX.json` (caps for metadata)

---

## The 7 Profile Types

### Type 1: County Landscape Profile

**Purpose:** Physical geography, topography, soil, vegetation, waterways, and sensory details by era. What the land looked, smelled, and sounded like.

**Granularity:** One file per county.
**Path:** `{cluster}/county_landscape/{county}.json`
**Target length:** 130-160 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `county_landscape_id` | string | `{state_lc}_{county_lc}` (e.g., `nc_wayne`) |
| `display_name` | string | Human-readable name |
| `county` | string | County name |
| `state` | string | State abbreviation |
| `fips_code` | string | FIPS code |
| `cluster_ref` | string | Cluster ID |
| `physical_geography` | object | Physiographic province, elevation, terrain, soil types, waterways, vegetation eras |
| `sensory_snapshots` | array | 3+ vivid era-specific snapshots (4-6 sentences each) |
| `landscape_changes` | array | Major changes to the physical landscape with narrative impact |
| `narrative_hooks` | array | 4+ hooks with `{variable}` placeholders |
| `source_references` | array | 5+ Chicago-style citations |
| `nel_cross_references` | object | trigger_refs, material_life_refs, community_texture_refs, life_pattern_refs |

**Sensory snapshots are the key output.** These are the paragraphs a narrative writer drops into the story to ground the ancestor in a real place. Each must specify era, season, and include sight, sound, smell, and temperature details.

### Type 2: Local Economy Timeline

**Purpose:** Decade-by-decade economic snapshots — employers, infrastructure, crops, wages, turning points.

**Granularity:** One file per cluster.
**Path:** `{cluster}/local_economy/{cluster_id}_economy.json`
**Target length:** 300-400 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `economy_id` | string | `{cluster_id}_economy` |
| `display_name` | string | Human-readable name |
| `cluster_ref` | string | Cluster ID |
| `era_range` | string | Overall era range |
| `economic_eras` | array | 6-8 era objects with county_specifics, infrastructure, employers, wages |
| `economic_turning_points` | array | 5+ specific events with year and impact |
| `narrative_hooks` | array | 6+ hooks with `{variable}` placeholders |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | trigger_refs, material_life_refs, wage_table_refs |

### Type 3: Road & Connectivity Network

**Purpose:** Transportation infrastructure by era. Travel times, road conditions, railroad timeline, isolation.

**Granularity:** One file per cluster.
**Path:** `{cluster}/road_connectivity/{cluster_id}_roads.json`
**Target length:** 200-280 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `connectivity_id` | string | `{cluster_id}_roads` |
| `transportation_eras` | array | 4-5 eras with travel_times, key_routes, isolation_index |
| `railroad_timeline` | array | Railroad entries with stations and impact |
| `narrative_hooks` | array | 5+ hooks |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | route_refs |

### Type 4: Information Landscape Profile

**Purpose:** How news and information reached people — newspapers, literacy, telegraph, mail, oral networks.

**Granularity:** One file per cluster.
**Path:** `{cluster}/information_landscape/{cluster_id}_information.json`
**Target length:** 180-250 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `information_id` | string | `{cluster_id}_information` |
| `information_eras` | array | 3-4 eras with literacy_context, newspapers, mail_service, telegraph/telephone, oral_networks |
| `narrative_hooks` | array | 5+ hooks |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | community_texture_refs, research_guidance_refs |

**Newspapers must include:** name, county, years published, frequency, genealogical value, and survival_status (where microfilm/digital copies exist).

### Type 5: Micro-Migration Network Map

**Purpose:** Documented county-to-county migration chains, settlement clustering, chain migration evidence.

**Granularity:** One file per cluster.
**Path:** `{cluster}/micro_migration/{cluster_id}_migration_networks.json`
**Target length:** 200-300 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `migration_network_id` | string | `{cluster_id}_migration_networks` |
| `migration_corridors` | array | Documented corridors with evidence and chain_mechanics |
| `internal_movement_patterns` | array | Intra-cluster movement |
| `settlement_clusters` | array | Documented clusters at destinations |
| `narrative_hooks` | array | 5+ hooks |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | trigger_refs, destination_refs, community_texture_refs |

### Type 6: Courthouse & Records Survival Atlas

**Purpose:** What records survived, what burned, what flooded. Substitute sources. Narrative impact of record losses.

**Granularity:** One file per county.
**Path:** `{cluster}/courthouse_atlas/{county}.json`
**Target length:** 80-120 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `courthouse_atlas_id` | string | `{state_lc}_{county_lc}_courthouse` |
| `courthouse_history` | object | Current and previous courthouses |
| `record_losses` | array | Each loss with date, cause, records destroyed/survived, narrative_impact |
| `record_survival_summary` | object | Per-record-type: deeds, wills, marriages, court minutes, vital records |
| `substitute_sources` | array | Alternative sources with repository and genealogical value |
| `narrative_hooks` | array | 4+ hooks |
| `source_references` | array | 3+ citations |
| `nel_cross_references` | object | layer1_county_profile_ref, research_guidance_refs, template_refs |

### Type 7: Seasonal Calendar Profile

**Purpose:** Month-by-month activity rhythms — agriculture, social/civic life, economics, weather.

**Granularity:** One file per cluster.
**Path:** `{cluster}/seasonal_calendar/{cluster_id}_seasons.json`
**Target length:** 300-400 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `seasonal_calendar_id` | string | `{cluster_id}_seasons` |
| `primary_economy` | string | What drove the seasonal rhythm |
| `calendar_eras` | array | 2-3 era objects, each with all 12 months |
| `narrative_hooks` | array | 6+ hooks |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | material_life_refs, occupation_refs |

Each month entry includes: agricultural, social_civic, economic, weather_conditions, and a narrative_hook.

### Type 8: Cultural Marker Profile

**Purpose:** Regional cultural fingerprints that appear in records and family memory — church denomination as origin indicator, naming conventions, food traditions, dialect markers, social hierarchies, material culture. These let Polsia interpret *cultural evidence* to locate an ancestor geographically and socially, not just by dates and places.

**Granularity:** One file per cluster.
**Path:** `{cluster}/cultural_markers/{cluster_id}_culture.json`
**Target length:** 200-300 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `cultural_markers_id` | string | `{cluster_id}_culture` |
| `display_name` | string | Human-readable name |
| `cluster_ref` | string | Cluster ID |
| `era_range` | string | Overall era range |
| `denomination_map` | array | Church denominations → origin/class/race indicators with genealogical significance |
| `naming_conventions` | array | Given name patterns, surname clustering, naming-as-evidence patterns |
| `foodways` | array | Regional food traditions that appear as cultural markers (barbecue style, crop-specific diet, etc.) |
| `dialect_markers` | array | Speech patterns that appear in written records (depositions, letters) |
| `social_hierarchies` | array | Class/occupation/race stratification specific to this region |
| `material_culture` | array | Physical objects, housing styles, clothing that distinguish this region |
| `cultural_calendar` | array | Distinctive regional traditions tied to calendar (revival season, camp meetings, holidays) |
| `narrative_hooks` | array | 6+ hooks with `{variable}` placeholders |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | community_texture_refs, material_life_refs, template_refs |

**Key output:** The denomination_map and naming_conventions are the most genealogically powerful fields. A Free Will Baptist affiliation places an ancestor in the eastern NC coastal plain. A "Young" given name signals a youngest-son naming tradition common in SE NC. These are interpretive tools that transform raw record data into narrative specificity.

### Type 9: Hidden History Overlay

**Purpose:** Events, systems, and patterns that explain record gaps, reframe ancestor narratives, or reveal stories the records don't tell directly. These are the "the absence of records IS the story" moments — courthouse fires (cross-referenced from courthouse atlas), racial violence, forced displacement, underground networks, epidemic disease, wartime destruction, and legal systems that erased people from the record.

**Granularity:** One file per cluster.
**Path:** `{cluster}/hidden_history/{cluster_id}_hidden.json`
**Target length:** 200-350 lines.

**Required fields:**

| Field | Type | Description |
|-------|------|-------------|
| `hidden_history_id` | string | `{cluster_id}_hidden` |
| `display_name` | string | Human-readable name |
| `cluster_ref` | string | Cluster ID |
| `era_range` | string | Overall era range |
| `hidden_events` | array | Specific events that altered records or narratives (wars, coups, epidemics, fires) |
| `systemic_erasures` | array | Ongoing systems that kept people out of records (illiteracy, racial exclusion, peonage, legal barriers) |
| `underground_networks` | array | Hidden or semi-hidden activity that left oblique record traces (Underground Railroad, moonshine, labor organizing) |
| `reframing_narratives` | array | Common genealogical assumptions about this region that the evidence contradicts |
| `record_gap_explanations` | array | Specific date ranges/counties where records disappear and WHY |
| `dignity_notes` | array | Guidance for narrating sensitive events (forced labor, racial violence, epidemic disease) with accuracy and dignity |
| `narrative_hooks` | array | 6+ hooks with `{variable}` placeholders |
| `source_references` | array | 5+ citations |
| `nel_cross_references` | object | trigger_refs, template_refs (especially record_silences), research_guidance_refs |

**The dignity mandate applies.** Hidden history events involving racial violence, forced labor, or epidemic disease must be narrated with factual accuracy and human dignity. The same standards from the NEL's forced/violent triggers (domestic_slave_trade, trail_of_tears, wilmington_1898) apply here.

---

## Integration with Polsia

Layer 4 adds a lookup step to the Polsia pipeline, between Material Life Grounding (Step 5) and Life Pattern Matching (Step 6):

1. Look up the ancestor's county in `REGIONAL_LANDSCAPE_INDEX.json → county_to_region[state][county]`
2. If found: load the cluster's profiles and use them for narrative enrichment
3. If not found: skip — the narrative proceeds with Layers 1-3

**Revenue tier handling:**
- **Option A:** 1-2 sensory snapshots, most relevant economic era, brief seasonal context
- **White Glove:** Full landscape profile across all eras, multiple sensory snapshots, complete micro-migration data, full courthouse atlas for record silence interpretation

---

## Cross-Referencing

Regional Landscape files reference NEL files (one-way):
- `trigger_refs` → migration_id strings from triggers
- `material_life_refs` → material_life_id strings
- `community_texture_refs` → community texture filenames
- `life_pattern_refs` → pattern_id strings
- `route_refs` → route_id strings
- `research_guidance_refs` → research guidance filenames
- `layer1_county_profile_ref` → pointer to Layer 1 county source profiler

**NEL files do NOT back-reference Layer 4.** The index is the bridge.

---

## Content Standards

- **The Accuracy Line:** Facts from records are SACRED. Context uses "likely", "probably."
- **Sources:** Minimum 3 per courthouse atlas file, minimum 5 per all other file types. Zero Wikipedia.
- **Narrative hooks:** Every file must have 4+ hooks with `{variable}` placeholders using standard NEL variables.
- **Sensory detail:** County landscape sensory snapshots must include sight, sound, smell, and temperature.
- **Variable placeholders:** Standard NEL variables: `{ancestor_name}`, `{surname}`, `{year}`, `{county}`, `{origin_county}`, `{destination}`, `{occupation}`, `{pronoun_subject}`, `{pronoun_object}`, `{pronoun_possessive}`, `{decade}`, `{state}`.

---

## Coverage Strategy

Layer 4 does not attempt universal coverage. It builds depth where it matters most:

**Tier 1:** User testing ground and personal interest (SE NC Coastal Plain)
**Tier 2:** High-frequency genealogy regions (Appalachian coal country, Mississippi Delta, Great Plains homestead belt, NY/NJ immigrant corridor, Great Migration destination cities)
**Tier 3:** Gap-detection driven (when 3+ ancestors hit an uncovered region)
**Tier 4:** May never need coverage (existing NEL is sufficient)

Each new cluster adds entries to `REGIONAL_LANDSCAPE_INDEX.json` and follows the same 7-type schema.

---

*This document is the sole reference for Layer 4 Regional Landscape Profile builds. Build agents should read this document and the exemplar files before beginning each cluster.*
