# Narrative Dry Run Analysis — All 8 Ancestors

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)

---

## Scoreboard

| # | Ancestor | Type | Profile | Score | Verdict |
|---|----------|------|---------|-------|---------|
| 1 | Ella Mae Johnson | Synthetic | Great Migration, Black, MS→Chicago | 9/10 STRONG | **PASS** |
| 2 | George Knauss | Real | PA Dutch→ND homesteader | 8/10 STRONG | **PASS** |
| 3 | Daniel Canady | Real | War of 1812 vet, Cumberland Co. NC, stayed | 6/10 STRONG | **PASS** |
| 4 | Abel Bass | Real | Civil War POW, Sampson Co. NC, stayed | 7/10 STRONG | **PASS** |
| 5 | Young Autry | Real | Pre-1850, minimal records, stayed | 4/10 STRONG | **PASS** |
| 6 | William Boon | Real | Civil War KIA, Nash Co. NC, 32-year life | 6/10 STRONG | **PASS** |
| 7 | Sarah Goldstein | Synthetic | Jewish pogrom, Russia→NYC LES | 7/10 STRONG | **PASS** |
| 8 | Wong Ah Sing | Synthetic | Chinese railroad worker→Portland | 5/10 STRONG | **CONDITIONAL PASS** |

**8/8 PASS** (1 conditional). The NEL produces usable narrative for every test case.

---

## Pattern Analysis

### Where the NEL is Strongest

**Migration stories with clear economic logic:** Ella Mae Johnson (9/10) and George Knauss (8/10) scored highest because the full pipeline fires — trigger → route → destination → occupation → wage comparison. When someone MOVED, the NEL has deep, layered data at every step.

**Dual/triple trigger layering:** Every ancestor matched 2-3 triggers, and the layering always added depth without repetition. The great_migration + boll_weevil pairing for Ella Mae and the homestead_act + german_immigration + economic_panics pairing for George both produced richer narrative than any single trigger would.

**Templates as narrative architecture:** The hinge_generation and record_silences templates were the MVPs for the stayed-put NC ancestors. When individual records are thin, these templates provide structured ways to narrate absence, family disruption, and generational change.

### Where the NEL is Weakest

**Stayed-put Southern ancestors (the user's own family):** Daniel Canady (6/10), Abel Bass (7/10), Young Autry (4/10), and William Boon (6/10) all scored lower — not because the triggers failed, but because the supporting data (occupation, material life, community texture) has gaps for antebellum Southern yeoman farmers. Four of five real ancestors hit the same wall.

**Chinese American coverage:** Wong Ah Sing (5/10, conditional) exposed the NEL's most significant ethnic gap. Zero Chinese community texture profiles exist. No Chinatown material life. No Chinese laundryman occupation. The triggers and routes are strong, but the middle of the pipeline (daily life, community, occupation) has critical holes.

**Pre-1850 ancestors:** Young Autry's 4/10 is the floor. The NEL can still produce narrative value by shifting from individual to world-level storytelling, but the material life and community texture files need antebellum extensions.

---

## Consolidated Gap Inventory

### CRITICAL (blocks narrative quality for a major demographic)

| Gap | Affected Ancestors | Source |
|-----|-------------------|--------|
| No Chinese American community texture (Chinatown bachelor society) | Wong Ah Sing | DR#8 |

### HIGH (significant narrative hole)

| Gap | Affected Ancestors | Source |
|-----|-------------------|--------|
| No Chinatown bachelor society material life (1870-1940) | Wong Ah Sing | DR#8 |

### MEDIUM (degrades narrative, workaround exists)

| Gap | Affected Ancestors | Source |
|-----|-------------------|--------|
| No antebellum yeoman farmer occupation (1780-1860) | Daniel, Abel, Young Autry, William | DR#3,4,5,6 |
| No Great Migration urban material life (1920-1960) | Ella Mae (+ any Black urban ancestor) | DR#1 |
| No postbellum Southern farm material life (1865-1910) | Abel Bass (+ any Reconstruction-era ancestor) | DR#4 |
| No PA Dutch / Lehigh Valley community texture | George Knauss | DR#2 |
| No turpentine laborer occupation | William Boon | DR#6 |
| No Chinese laundryman occupation | Wong Ah Sing | DR#8 |
| No SF-to-Portland coastal route | Wong Ah Sing | DR#8 |

### LOW (minor, easily fixable)

| Gap | Affected Ancestors | Source |
|-----|-------------------|--------|
| Validator: erie_canal anachronistic for 1900 | George Knauss | DR#2 |
| Validator: new_york_lower_east_side wrong for Chinese ancestor | Wong Ah Sing | DR#8 |
| Validator: southern_pacific wrong for Wong Ah Sing | Wong Ah Sing | DR#8 |
| Community texture: eastern_nc_farm_community covers 1865-1910, not antebellum | Daniel, Young Autry | DR#3,5 |
| Community texture: Nash County missing from geographic_scope | William Boon | DR#6 |
| Wage table: no garment worker entry (data exists in occupation file) | Sarah Goldstein | DR#7 |
| Wage table: no pre-1850 data (may not be fixable) | Daniel, Young Autry | DR#3,5 |
| Jewish-specific material life layer (Sabbath, kosher, cheder) | Sarah Goldstein | DR#7 |

---

## Prioritized Build Targets

### Tier 1 — Fixes the Most Ancestors (build these next)

| # | File | Type | Priority | Ancestors Fixed | Effort |
|---|------|------|----------|----------------|--------|
| 1 | `yeoman_farmer_antebellum.json` | occupation | **MEDIUM** | Daniel, Abel, Young Autry, William (4 of 5 real ancestors) | ~250 lines |
| 2 | `postbellum_southern_farm_1865_1910.json` | material_life | **MEDIUM** | Abel, Daniel, William's family (Reconstruction era) | ~250 lines |
| 3 | `great_migration_urban_1920_1960.json` | material_life | **MEDIUM** | Ella Mae + any Black urban ancestor | ~250 lines |

### Tier 2 — Fills Ethnic Coverage Gaps

| # | File | Type | Priority | Ancestors Fixed | Effort |
|---|------|------|----------|----------------|--------|
| 4 | `west_coast_chinatown_bachelor_society.json` | community_texture | **CRITICAL** | Wong Ah Sing + any Chinese ancestor | ~200 lines |
| 5 | `chinatown_bachelor_society_1870_1940.json` | material_life | **HIGH** | Wong Ah Sing + any Chinese ancestor | ~250 lines |
| 6 | `chinese_laundryman.json` | occupation | **MEDIUM** | Wong Ah Sing | ~150 lines |

### Tier 3 — Targeted Fills

| # | File | Type | Priority | Ancestors Fixed | Effort |
|---|------|------|----------|----------------|--------|
| 7 | `turpentine_laborer.json` | occupation | **MEDIUM** | William Boon + NC turpentine belt ancestors | ~150 lines |
| 8 | `pa_dutch_lehigh_valley.json` | community_texture | **MEDIUM** | George Knauss | ~200 lines |
| 9 | `pacific_coastal_steamer.json` | route | **MEDIUM** | Wong Ah Sing | ~80 lines |

### Tier 4 — Quick Fixes (< 30 minutes total)

| # | Fix | Type |
|---|-----|------|
| 10 | Add Nash County to eastern_nc_farm_community geographic_scope | content fix |
| 11 | Extend eastern_nc_farm_community era back to antebellum | content fix |
| 12 | Add garment worker entry to wages_1900_1950 table | content fix |
| 13 | Fix validator: remove erie_canal from George Knauss expected_routes | validator fix |
| 14 | Fix validator: correct Wong Ah Sing expected textures and routes | validator fix |
| 15 | Add Chinese name transliteration patterns to name_change_patterns.json | content addition |

---

## What the Dry Runs Proved

### 1. The data layer works.
All 8 ancestors produced usable narrative. Even Young Autry — the hardest case, with almost no individual records — generated a publication-quality narrative by shifting from "here is what we know about this person" to "here is what the silence means."

### 2. Migration stories are the product's sweet spot.
Ella Mae Johnson (9/10) and George Knauss (8/10) — the two ancestors who actually MOVED — scored highest. The full pipeline fires: trigger → route → destination → occupation → wage comparison → community texture. This is what Option A was designed for.

### 3. Stayed-put ancestors need more support.
The user's own family (4 NC yeoman farmers who never left) consistently scored 4-7/10. The triggers fire fine, but the occupation, material life, and community texture files have antebellum gaps. Three builds (yeoman_farmer_antebellum + postbellum_southern_farm + eastern_nc_farm_community antebellum extension) would raise all four scores by 1-2 points.

### 4. Chinese American coverage is the biggest ethnic gap.
Wong Ah Sing's conditional pass (5/10) is the only case where the pipeline structurally fails. Three new files (Chinatown texture + material life + laundryman occupation) would bring it to parity. This matters for product credibility — if KinLore can narrate Irish, Jewish, Black, and German ancestors but not Chinese, that's a visible hole.

### 5. The Accuracy Line held across all 8 runs.
No draft narrative fabricated facts, projected emotions, or upgraded inference to certainty. Every claim was grounded in sourced NEL data. The counter-narratives prevented one-dimensional storytelling. The system works as designed.

### 6. Templates are more important than triggers for stayed-put ancestors.
For the NC yeoman farmers, the triggers provide context but the templates (record_silences, hinge_generation, economic_life_story, military_service_arc) provide the narrative structure. The templates are what turn "he was a farmer who stayed" into a story.

---

## Recommended Next Action

**Build Tier 1 (items 1-3) + Tier 4 quick fixes (items 10-15).** This raises the floor for the user's own family (4 of 5 real ancestors improved) and fills the most-common-ancestor occupation gap. Total effort: ~750 lines of new content + 6 small edits. One session.

Then build Tier 2 (items 4-6) for Chinese American coverage. This is a credibility issue, not just a coverage issue.

Tier 3 can wait — those are targeted fills for specific ancestors.
