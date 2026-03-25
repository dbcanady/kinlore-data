# NEL Gap Detection Guide

**For: Polsia / KinLore Narrative AI**
**Version: 1.0**
**Last Updated: 2026-03-16**

## Purpose

This guide tells the narrative AI how to detect and report gaps in the Narrative Enrichment Layer (NEL) data. When processing an ancestor record, the AI should attempt to match against every data category. When no match is found, a **structured gap report** is generated so the data layer can be expanded to cover the missing pattern.

**This is how the NEL gets smarter over time.** Every ancestor that hits a gap teaches us what to build next.

---

## How Gap Detection Works

### Step 1: Match Attempt

When processing an ancestor record, attempt matches in this order:

1. **Trigger matching** — Compare ancestor's origin county, era, occupation, ethnicity, and race against:
   - 25 core triggers in `core/`
   - 6 NC regional triggers in `regional/nc/` (expand as more states are built)

2. **Destination lookup** — Match ancestor's destination against 21 destination profiles in `shared/destinations/`

3. **Occupation lookup** — Match ancestor's listed occupation against 20 occupation profiles in `shared/occupations/`

4. **Route selection** — Use matched trigger's `route_refs` to pull from 24 route files in `shared/routes/`

5. **Material life lookup** — Match ancestor's era + region against 12 material life profiles in `shared/material_life/`

6. **Community texture lookup** — Match ancestor's settled community against 18 community texture profiles in `shared/community_texture/`

7. **Wage lookup** — Match ancestor's occupation + era against 3 wage tables in `shared/wages/`

8. **Template selection** — Select appropriate templates from 10 templates in `templates/`

9. **Research guidance** — When record gaps detected, match against 10 guidance files in `research_guidance/`

### Step 2: Gap Detection

A gap exists when ANY of the following occur:

| Condition | Gap Type | Severity |
|-----------|----------|----------|
| No trigger matches the ancestor's migration pattern at all | `missing_trigger` | HIGH |
| Trigger matches but destination city has no profile | `missing_destination` | MEDIUM |
| Ancestor's occupation has no profile | `missing_occupation` | MEDIUM |
| Trigger references a route that has no file | `missing_route` | MEDIUM |
| No material life profile covers the ancestor's era + region | `missing_material_life` | LOW |
| No community texture covers the ancestor's settled community | `missing_community_texture` | LOW |
| National trigger matches but a state-specific pattern exists that isn't covered | `missing_regional_trigger` | LOW |
| Ancestor's occupation/era falls outside wage table coverage | `missing_wage_data` | LOW |

**HIGH** = The narrative AI has almost no historical context for this ancestor. The report will be significantly weaker.
**MEDIUM** = The narrative AI has some context but is missing a key dimension (work life, destination detail, journey description).
**LOW** = The narrative AI can work around this gap using adjacent data, but a dedicated file would improve the narrative.

### Step 3: Gap Reporting

When a gap is detected, generate a structured gap report following the schema in `gap_report_schema.json`.

**Output format:** JSON Lines (one JSON object per line) appended to `gap_reports.jsonl`.

**Key fields:**
- `gap_type` — Which data category is missing
- `severity` — How badly the narrative suffers
- `searched_for` — What the AI looked for (specific enough to act on)
- `nearest_match` — The closest existing file, if any
- `suggested_file` — A proposed filename for the missing data
- `frequency_note` — How many times this gap has been seen

### Step 4: Deduplication

Before adding a new gap to the report file, check if the same `gap_type` + `searched_for` combination already exists. If so, increment the frequency count rather than creating a duplicate entry.

---

## Priority Scoring for Build Targets

Gap reports accumulate into a prioritized build queue:

| Priority | Criteria | Action |
|----------|----------|--------|
| **BUILD NOW** | HIGH severity + frequency >= 3, OR any severity + frequency >= 10 | Create the missing file immediately |
| **BUILD SOON** | MEDIUM severity + frequency >= 5, OR HIGH severity + frequency >= 1 | Queue for next build session |
| **DEFER** | LOW severity + frequency < 10 | Track but don't build yet |

---

## Known Gaps (as of 2026-03-16)

These are gaps we already know about from cross-reference validation and coverage analysis. They are future build targets, not errors:

### Trigger Gaps (candidates for future core triggers)
- Scandinavian Immigration (1850-1920) — Norwegian, Swedish, Finnish settlement in Upper Midwest
- Vietnamese Refugee Resettlement (1975-1985) — Southeast Asian refugee communities
- Great Migration Return (1970-present) — Reverse migration from North to South

### Destination Gaps (cities that triggers reference but have no profile)
- San Francisco, Los Angeles, Baltimore, Richmond, Nashville, Louisville, Indianapolis, Kansas City, Omaha, Salt Lake City, El Paso, San Antonio

### Occupation Gaps (common census occupations without profiles)
- tanner, cooper, wheelwright, printer, baker, butcher, mason/bricklayer, painter, tailor, barber, hotel keeper, druggist, miller

### Regional Trigger Gaps (state-specific patterns not yet built)
- VA: Shenandoah Valley → Kentucky/Tennessee
- OH: Ohio River Valley crossings (KY/WV → OH industrial cities)
- TX: German Hill Country settlement patterns
- MN: Scandinavian clustering patterns
- PA: Coal region internal migration

---

## Feedback Loop Architecture

```
┌─────────────────────────────────────────────────────┐
│  Polsia processes ancestor record                    │
│  ↓                                                   │
│  Matches against NEL data (triggers, destinations,   │
│  occupations, routes, material_life, community       │
│  texture, wages, templates, research_guidance)       │
│  ↓                                                   │
│  Gaps detected? → Generate gap_report (JSON)         │
│  ↓                                                   │
│  gap_reports.jsonl accumulates in repository          │
└─────────────┬───────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────┐
│  Review cycle (manual or automated)                  │
│  ↓                                                   │
│  Priority scoring: severity × frequency              │
│  ↓                                                   │
│  BUILD NOW targets → Claude Code CLI session         │
│  ↓                                                   │
│  New files built, validated, pushed to GitHub         │
└─────────────┬───────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────┐
│  Polsia pulls updated NEL from GitHub                │
│  ↓                                                   │
│  Previously-gapped ancestors now have matches        │
│  ↓                                                   │
│  Fewer gaps → Better narratives → Smarter system     │
└─────────────────────────────────────────────────────┘
```

---

## Integration Notes for Polsia

1. **Read this guide** as part of your NEL context when processing ancestor records.
2. **Read `gap_report_schema.json`** for the exact output format.
3. **Do not let gaps block narrative generation.** Generate the best narrative you can with available data, then report the gap separately.
4. **The `nearest_match` field is critical.** It tells Claude Code CLI what existing file to use as a starting point or schema reference when building the missing file.
5. **Be specific in `searched_for`.** "Missing occupation" is useless. "Missing occupation profile for 'tanner' (ancestor in Pennsylvania, 1850-1880)" is actionable.
6. **Report gaps even when you can work around them.** A LOW severity gap seen 50 times is a high-priority build target.
