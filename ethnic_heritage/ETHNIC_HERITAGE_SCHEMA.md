# Ethnic Heritage Profile Schema — Layer 5

## Purpose
When Polsia identifies an ancestor's ethnic/cultural heritage from records (surname, church denomination, immigration port, settlement area, etc.), it loads the matching heritage profile to enrich the narrative with culturally-specific context that goes far beyond geography alone.

## File Location
`/home/dbcanady/kinlore-data/ethnic_heritage/{profile_id}.json`

## Usage by Polsia
1. Identify ancestor's likely heritage from available clues (surname, denomination, settlement pattern, origin records)
2. Load matching heritage profile(s) — an ancestor may match multiple (e.g., `scots_irish` + `quaker`)
3. Weave heritage-specific context into narrative using `{variable}` placeholder hooks
4. Cross-reference with Layer 3 triggers, Layer 4 regional data, and life patterns

---

## JSON Schema (v1.0)

Every file MUST include these top-level fields:

```json
{
  "_schema_version": "1.0",
  "_last_updated": "2026-03-20",
  "_purpose": "Ethnic heritage profile for [group] — provides cultural context for narrative generation",

  "profile_id": "string — matches filename without .json",
  "display_name": "string — human-readable name",
  "group_category": "string — one of: colonial_british, germanic, irish, scandinavian, southern_eastern_european, slavic_baltic, african_american, french_acadian, asian_american, latin_american, other",
  "alternate_terms": ["array of other names this group is known by"],
  "identification_clues": {
    "surname_patterns": ["common surname types or specific surnames that signal this heritage"],
    "denomination_signals": ["church affiliations that strongly suggest this group"],
    "settlement_signals": ["geographic areas where this group concentrated"],
    "record_signals": ["record types or features that identify this group — e.g., parish records in Norwegian, naturalization from specific ports"],
    "occupation_signals": ["occupations strongly associated with this group"]
  }
}
```

### Required Sections (all profiles)

#### 1. immigration_overview
```json
{
  "immigration_overview": {
    "primary_period": "date range string",
    "peak_decades": ["1850s", "1860s"],
    "waves": [
      {
        "wave_name": "string",
        "period": "date range",
        "origin_regions": ["specific regions, not just country"],
        "push_factors": ["why they left — be specific"],
        "pull_factors": ["why America — be specific"],
        "estimated_numbers": "string with source qualifier",
        "primary_ports_of_entry": ["specific ports"],
        "typical_journey": "narrative description of the voyage/travel"
      }
    ],
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```
- Minimum 1 wave, most groups have 2-4
- Push/pull factors must be historically specific, not generic
- Port of entry matters enormously for record-finding

#### 2. settlement_patterns
```json
{
  "settlement_patterns": {
    "primary_destinations": [
      {
        "region": "string",
        "period": "date range",
        "why": "specific reason for this destination",
        "community_character": "what the settlement looked like"
      }
    ],
    "chain_migration_networks": ["description of how networks operated"],
    "clustering_factors": ["why they clustered — church, language, land agents, kin"],
    "secondary_migration": ["later moves within the US"],
    "urban_vs_rural": "description of settlement preference and why",
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```
- Connect to Layer 4 regional clusters where possible
- Include specific place names, not just states

#### 3. church_and_records
```json
{
  "church_and_records": {
    "primary_denominations": [
      {
        "denomination": "string",
        "record_types_kept": ["baptism, marriage, burial, communion, confirmation, etc."],
        "record_language": "language(s) used in records",
        "typical_record_detail": "what level of family detail these records contain",
        "genealogical_value": "high/medium/low with explanation"
      }
    ],
    "civil_record_interaction": "how church records relate to civil records for this group",
    "language_transition_timeline": [
      {
        "period": "date range",
        "language": "language used",
        "context": "when/why the shift happened"
      }
    ],
    "key_repositories": ["where to find these records today"],
    "record_survival_notes": "what survived, what didn't, and why",
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```
- This section is CRITICAL for genealogical utility
- Be specific about what records contain (do they name parents? godparents? birthplace?)
- Language of records matters for research strategy

#### 4. naming_conventions
```json
{
  "naming_conventions": {
    "surname_patterns": [
      {
        "pattern": "description of the pattern",
        "examples": ["example names"],
        "genealogical_implication": "what this means for research"
      }
    ],
    "given_name_traditions": [
      {
        "tradition": "description",
        "examples": ["names"],
        "era": "when this was practiced"
      }
    ],
    "americanization_patterns": [
      {
        "original": "original form or pattern",
        "americanized": "what it became",
        "when": "typical period of change",
        "how": "process — was it gradual? at naturalization? at school?"
      }
    ],
    "common_name_traps": ["specific pitfalls researchers encounter"],
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```
- Name changes are one of the biggest genealogical challenges
- Include SPECIFIC examples, not just abstract patterns

#### 5. occupational_patterns
```json
{
  "occupational_patterns": {
    "by_era": [
      {
        "era": "date range",
        "common_occupations": ["list"],
        "why": "what drove this group to these occupations",
        "economic_position": "where they sat in the economic hierarchy"
      }
    ],
    "occupational_clustering": ["specific industries or trades dominated by this group"],
    "economic_mobility_trajectory": "narrative description of how economic position changed over generations",
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```

#### 6. cultural_markers
```json
{
  "cultural_markers": {
    "foodways": ["food traditions that identify this group and appear in narrative"],
    "holidays_and_traditions": ["cultural celebrations, their timing, and significance"],
    "social_organizations": ["fraternal orders, mutual aid societies, cultural clubs"],
    "material_culture": ["distinctive housing, clothing, tools, artifacts"],
    "music_and_arts": ["musical traditions, artistic expressions"],
    "language_markers": ["distinctive words, phrases, accent features that appear in records or narrative"],
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```

#### 7. intermarriage_patterns
```json
{
  "intermarriage_patterns": {
    "endogamy_period": "how long this group primarily married within itself",
    "endogamy_factors": ["what reinforced in-group marriage — language, religion, geography, family pressure"],
    "common_intermarriage_groups": ["which other groups they commonly married when endogamy broke down"],
    "transition_timeline": "when and why intermarriage became common",
    "genealogical_implications": "what intermarriage means for research strategy",
    "narrative_hooks": ["hooks with {variable} placeholders"]
  }
}
```

#### 8. genealogical_pitfalls
```json
{
  "genealogical_pitfalls": {
    "common_traps": [
      {
        "trap": "description of the pitfall",
        "why_it_happens": "explanation",
        "how_to_avoid": "research strategy"
      }
    ],
    "record_gaps": [
      {
        "gap": "what's missing",
        "period": "when",
        "workaround": "alternative sources"
      }
    ],
    "name_change_patterns": ["specific patterns beyond what's in naming_conventions"],
    "research_tips": ["actionable advice for this specific group"]
  }
}
```

#### 9. nel_cross_references
```json
{
  "nel_cross_references": {
    "trigger_refs": ["Layer 3 trigger IDs relevant to this group"],
    "community_texture_refs": ["Layer 3 community texture IDs"],
    "material_life_refs": ["Layer 3 material life IDs"],
    "life_pattern_refs": ["Layer 3 life pattern IDs"],
    "regional_landscape_refs": ["Layer 4 cluster IDs where this group concentrated"],
    "other_heritage_refs": ["other ethnic heritage profiles that commonly overlap"]
  }
}
```

#### 10. source_references
```json
{
  "source_references": ["Chicago-style citations, 5+ per file, NO Wikipedia"]
}
```

### Additional Required Section (specific profiles only)

#### dignity_mandate (REQUIRED for: enslaved_african_american, free_black_antebellum, reconstruction_jim_crow, great_migration, native_american, chinese, japanese, mexican_tejano, and any profile involving forced migration or systematic oppression)
```json
{
  "dignity_mandate": {
    "applies": true,
    "guidance": "specific guidance for narrating this group's experience with dignity",
    "language_notes": ["terms to use", "terms to avoid"],
    "framing_principles": ["how to frame difficult history"]
  }
}
```

---

## Content Standards

- **Line count**: 200-400 lines per file (substantial, not stub)
- **The Accuracy Line**: Facts from records are SACRED. Context uses "likely", "probably", "typically"
- **{variable} placeholders**: `{ancestor_name}`, `{surname}`, `{year}`, `{county}`, `{state}`, `{denomination}`, `{occupation}`
- **Sources**: 5+ Chicago-style citations per file. NO Wikipedia. Use primary scholarly sources.
- **Specificity over generality**: "Arrived at Castle Garden in the 1850s" beats "Came to America"
- **Narrative utility**: Every fact should help Polsia write a better story. If it doesn't serve narrative, cut it.
- **No stereotyping**: Cultural patterns are statistical tendencies, not universals. Use "commonly", "often", "many" — never "all" or "always"

## Index File
`ETHNIC_HERITAGE_INDEX.json` — lookup table mapping identification clues to profile IDs, similar to Layer 4's REGIONAL_LANDSCAPE_INDEX.json.
