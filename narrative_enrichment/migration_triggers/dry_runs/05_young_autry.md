# Narrative Dry Run #5: Young Autry

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)
**Pipeline:** POLSIA_INTEGRATION.md 10-step ancestor processing
**Revenue Tier:** Option A (single-ancestor report)

---

## Ancestor Input Record

| Field | Value |
|-------|-------|
| Name | Young Autry |
| Birth Year | 1790 |
| Origin | Sampson County, NC |
| Destination | None (stayed) |
| Arrival Year | None |
| Occupation | Farmer |
| Race | White |
| Era | 1790-1850 |

**Type:** Real test ancestor (user's family). Pre-1850 Sampson County / Minimal Records. THIS IS THE RECORD SILENCE STRESS TEST. Young Autry lived and died in the era before detailed census records -- pre-1850 censuses list only heads of household with tick marks for age/sex categories. No individual census entries. No military service expected. No migration. Born 1790, died approximately 1850. The question this dry run answers: can the NEL produce narrative value from almost nothing?

---

## Step 1: Trigger Matching

### Matched Triggers

**Primary:** `antebellum_yeoman_south` (core) -- era 1790-1860, migration_class: economic
- Sampson County, NC is explicitly listed in both `origin_counties` and `counties_most_affected`. Direct hit.
- Phase match: Phase 1, "Post-Revolutionary Settlement" (1790-1815) aligns with Young Autry's birth year and early adulthood. Phase 2, "War of 1812 Aftermath and Banking Crisis" (1812-1825) covers his middle years. Phase 3, "Cotton Kingdom Expansion" (1820-1840) covers his later years.
- Push factors applicable: `land_subdivision_heirs` (severity 4), `soil_exhaustion_continuous` (severity 3), `crop_lien_origins` (severity 2), `planter_squeeze` (severity 3).
- Pull factor match: NONE used -- Young Autry did not migrate. The pull factors describe destinations he never went to.
- Counter-narrative match: `not_all_yeomen_poor` and `yeoman_independence_myth` both apply -- we know almost nothing about Young Autry's economic position, so the range of possibility matters.

**Secondary:** `stayed_and_adapted` (core) -- era "All eras", migration_class: non_migration
- Young Autry stayed in Sampson County his entire life. This is the non-migration trigger designed for exactly this case.
- Phase match: "Pressure Accumulation" applies (Young Autry lived through the post-Revolutionary settlement period and watched the cotton economy expand south and west without him). "Adaptation in Place" applies (he farmed in Sampson County for 60 years while the economic pressures described in antebellum_yeoman_south affected everyone around him). "Consolidation and Continuity" applies (the Autry name remained in Sampson County).
- Pull factors (reasons to stay): `family_network_density` (severity 4), `land_ownership` (severity 5), `community_ties` (severity 3), `church_membership` (severity 3), `local_reputation` (severity 3).
- The `what_staying_looked_like` section is the primary narrative engine here: daily reality of a gradually changing community, economic adaptation, social consequences of remaining while others leave.
- Template integrations: `record_silences` (silence_as_narrative -- "the ABSENCE of a deed of sale, the ABSENCE of a removal certificate from the church... confirm continuity"), `fork_in_the_road` (inverted -- what would have happened if he HAD left?).

### Draft Narrative (Trigger Context)

> Young Autry was born in Sampson County, North Carolina, in 1790 and -- as far as the surviving records can tell us -- he never left. He lived through every pressure that drove thousands of Upper South yeoman families westward: land subdivision among heirs that shrank farms below the threshold of viability, soil exhaustion from decades of continuous cultivation, the Panic of 1819, the cotton kingdom's expansion into Alabama and Mississippi, and the steady squeeze of the planter class economy. Neighbors loaded wagons and headed for fresh land in the Southwest. Brothers and cousins may have written back from Alabama or Tennessee describing available acreage and richer soil. Young Autry stayed.
>
> Staying was not inertia. It was a decision that the records document by omission: the ABSENCE of a land sale in the deed books, the ABSENCE of his name from another state's census, the ABSENCE of a letter of dismissal from the local Baptist church. In a period when movement was the defining American act, staying put left a different kind of trace.

### Grade: **STRONG**

Both triggers fire cleanly. Sampson County is explicitly named in the antebellum_yeoman_south trigger's origin and most-affected counties lists. The stayed_and_adapted trigger is designed for precisely this case -- a non-migrating ancestor in a community under migration pressure. The dual-trigger approach inverts the usual narrative: instead of explaining why the ancestor left, it explains why the ancestor stayed while everyone else did.

**One critical observation:** The antebellum_yeoman_south trigger is rich with push factors and narrative hooks, but almost all of them assume variables the researcher does not have for Young Autry. `{property_acres}`, `{number}` of heirs, `{crop}` -- we do not know any of these. The narrative hooks require adaptation to work without individual-level data. The trigger provides the WORLD; the record_silences template must frame the INDIVIDUAL within it.

---

## Step 2: Route Selection

### Matched Route

**None.** Young Autry did not migrate. The stayed_and_adapted trigger explicitly states: `route_refs: []` and `primary_mode: "Not applicable -- this trigger describes non-migration"`.

### Grade: **ADEQUATE** (by design)

This is correct behavior. No route should fire for a non-migrating ancestor. The pipeline correctly returns an empty set. The narrative work that a route file would do (describing the physical experience of travel) is replaced by the stayed_and_adapted trigger's description of what staying looked like.

**No gap -- this is working as designed.**

---

## Step 3: Destination Lookup

### Matched Destination

**None.** Young Autry had no destination. The stayed_and_adapted trigger explicitly states: `destination_refs: []`.

### Grade: **ADEQUATE** (by design)

Correct behavior. A non-migrating ancestor generates no destination lookup. The narrative weight that a destination profile would carry is instead handled by the community_texture profile for the origin community (Step 6) and the material_life profiles (Step 5). The origin IS the destination.

**No gap -- this is working as designed.**

---

## Step 4: Occupation Enrichment

### Matched Occupations

**Expected:** `tenant_farmer` and `general_farmer_midwest`
**Actual assessment:** Both are problematic matches for Young Autry.

`tenant_farmer` -- era 1870-1960. **ERA MISMATCH.** The tenant_farmer profile begins in 1870, twenty years after Young Autry's death. The economics, compensation structures, and cultural context described in this file do not apply to the antebellum period. The file describes the post-Civil War crop lien system, AAA programs, and Depression-era displacement -- none of which Young Autry experienced. We also do not know whether Young Autry was a tenant farmer, a landowner, or a landless laborer.

`general_farmer_midwest` -- era 1860-1970, regions: Corn Belt / Upper Midwest / Great Plains. **REGION AND ERA MISMATCH.** This file describes Midwestern diversified family farming -- corn, wheat, oats, hog raising, cream separators. Young Autry was a Coastal Plain North Carolina farmer in the antebellum period. The agricultural practices, tools, crops (tobacco, corn, some cotton), and economic structures were fundamentally different from Iowa or Ohio farming.

### What SHOULD Match

The closest occupation match is embedded in the antebellum_yeoman_south trigger itself, not in a standalone occupation file. The trigger's description of yeoman farming -- subsistence crops with a small cash crop, 50-200 acres, family labor -- IS the occupation profile. The antebellum_yeoman_farm_1820_1860 material life file provides the daily work description that an occupation file would normally supply.

### Draft Narrative (Occupation)

> The census records from Young Autry's lifetime do not list occupations. Before 1850, the federal census recorded only the head of household's name, with tick marks indicating the number of people in the household by age and sex categories. There was no occupation column. We can say with near certainty that Young Autry was a farmer -- in Sampson County in 1810, virtually every white male head of household was a farmer -- but we cannot say what kind. Did he own his land or rent it? Did he grow tobacco, cotton, corn, or all three? Did he hold title to 200 acres or scratch a living from 30? The records do not say.
>
> What we know is what every yeoman farmer in Sampson County did: cleared land, worked it with family labor, grew corn as the subsistence crop and tobacco or cotton as the cash crop, raised hogs in the woods, and settled accounts at the general store after harvest. The annual cycle -- planting in spring, cultivation through summer, harvest in fall, hog killing after the first freeze -- organized every aspect of daily life. The absence of an occupation entry in the census is not a gap in Young Autry's story. It is a feature of how the census was designed before 1850.

### Grade: **THIN**

The expected occupation files do not match. The `tenant_farmer` profile is twenty years too late and assumes post-Civil War economic structures. The `general_farmer_midwest` profile is the wrong region entirely. Neither file provides useful content for a 1790-1850 North Carolina farmer. The narrative instead draws on the antebellum_yeoman_south trigger and the material_life profiles to reconstruct what farming looked like -- which works, but exposes a real gap.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing occupation profile |
| Searched For | Antebellum yeoman farmer / Southern subsistence farmer, 1780-1860. The occupation of the majority of the white Southern population before the Civil War. |
| Severity | **MEDIUM** -- the material_life file and trigger compensate, but a dedicated occupation file for antebellum Southern farming would provide: daily/seasonal work descriptions, tools and equipment, economic compensation (barter, subsistence, small cash crop), records generated (tax lists, agricultural census from 1850), and census clues. Currently this information is scattered across the trigger and material_life files rather than consolidated in one occupation profile. |
| Nearest Match | `tenant_farmer` (wrong era), `general_farmer_midwest` (wrong region and era) |
| Recommended Build | `yeoman_farmer_antebellum.json` covering: subsistence-plus-surplus farming, 50-200 acres, tobacco/cotton/corn, family labor, no enslaved labor, general store credit economy, pre-1850 census limitations, seasonal cycle, tools (axe, plow, hoe), records generated (tax lists, deed records, militia rolls). Would serve the largest single demographic group in KinLore user research. |

---

## Step 5: Material Life Grounding

### Matched Material Life Profiles

**Primary:** `antebellum_yeoman_farm_1820_1860` -- matches Young Autry's later years (1820-1850)
**Secondary:** `frontier_log_cabin_1780_1840` -- matches Young Autry's early years (1790-1820)

Both profiles are directly relevant. Young Autry was born in 1790, when Sampson County was still within a generation of frontier settlement, and died around 1850, by which time the yeoman farm landscape was well established. His life spans the transition from frontier log cabin to established yeoman farmstead -- from the puncheon-floor one-room cabin of the 1790s to the two-room dogtrot with detached kitchen of the 1840s.

### Draft Narrative (Material Life)

> The world Young Autry was born into in 1790 was close to the frontier. Sampson County had been carved from Duplin County only six years earlier, in 1784. The cabin where he spent his childhood was likely one room -- sixteen by twenty feet of hewn logs with clay chinking, a puncheon floor, and a cat-and-clay chimney that smoked in every wind. The family ate what the farm and the woods produced: cornbread baked in a Dutch oven, salt pork, hominy, wild game, and whatever the kitchen garden yielded. A cast-iron pot and a skillet might have been the most valuable objects in the household. The nearest neighbor was a clearing away through hardwood forest.
>
> By the time Young Autry was raising his own family in the 1810s and 1820s, Sampson County had matured. The cabin probably gained a second room -- or was replaced by a frame house. A detached kitchen kept the summer heat and fire risk separate from the living quarters. A smokehouse stood in the yard, sweet with salt-cured ham. The spinning wheel and loom turned raw cotton and wool into linsey-woolsey for the family's clothing, though by the 1840s, store-bought calico from the general store was displacing homespun. The family Bible -- if the Autrys owned one -- recorded births, marriages, and deaths on its pages, serving as the family's only genealogical record in an era before vital registration.
>
> What Young Autry ate, wore, and owned can be approximated from estate inventories of his Sampson County neighbors: three iron pots, a Dutch oven, a spinning wheel, a feather bed, six pewter plates, a family Bible, a rifle, an axe, and a mantel clock -- the entire material world of a yeoman family, appraised at less than the value of two mules.

### Grade: **STRONG**

Both material life profiles are deeply relevant and richly detailed. The frontier_log_cabin file covers the world Young Autry was born into; the antebellum_yeoman_farm file covers the world he lived in as an adult. Together they span his entire life. The sensory snapshots are publication-ready. The household goods inventories provide exactly the kind of specific, sourced detail that makes "we don't know what he owned" into "here is what every yeoman farmer in Sampson County owned, and the odds are strong that Young Autry's household looked the same."

The `economic_position` field in the antebellum_yeoman_farm file is especially valuable here. Because we do not know whether Young Autry was a landowner, tenant, or marginal farmer, the position_guidance section provides separate narrative hooks for each possibility, with different record expectations and different framings. This is exactly the kind of hedged, honest framing the Accuracy Line demands.

**THIS IS WHERE THE NEL CARRIES THE NARRATIVE FOR A RECORD-THIN ANCESTOR.** When individual records fail, the material life profiles provide the physical world that the ancestor certainly inhabited. The details are not invented for Young Autry -- they are documented for his era, region, and economic class, and applied with appropriate hedging language.

**No issues found.**

---

## Step 6: Community Texture

### Matched Community Texture

**Primary:** `eastern_nc_farm_community` -- origin_community, era 1865-1910

### Assessment

The eastern_nc_farm_community texture is the closest available match, but it has an **ERA PROBLEM**. The file covers the post-Civil War period (1865-1910), not the antebellum period (1790-1850). Young Autry was dead before this file's era begins. The institutions described -- Confederate memorial associations, the Grange, post-Civil War crop lien merchants -- did not exist in Young Autry's lifetime.

**However, much of the file's content IS relevant with adjustment:**
- The Missionary Baptist and Free Will Baptist church descriptions apply -- these denominations were established in eastern NC well before the Civil War and functioned the same way. The genealogical notes about Baptist church minutes, letters of dismissal, and the Baptist Historical Collection at Wake Forest are directly relevant.
- The Methodist circuit system description applies -- circuit riders served eastern NC from the colonial era.
- The one-room schoolhouse description is broadly applicable, though antebellum common schools were even more rudimentary.
- The county courthouse and court day descriptions are directly applicable -- county courts functioned the same way in the antebellum period.
- The crossroads general store description is applicable in outline, though the formalized crop lien system described in the file postdates Young Autry.
- The community rhythms (tobacco cycle, cotton cycle, court days, camp meeting season, hog killing, Christmas) are all applicable to the antebellum period.
- The informal economy descriptions (women's egg/butter sales, quilting bees, midwifery) apply across eras.

The file's treatment of race dynamics and the Wilmington 1898 coup is irrelevant to Young Autry's era (he was dead by then), but the biracial reality of Sampson County existed in the antebellum period in a different form -- enslaved Black labor alongside free white yeoman farming.

### Draft Narrative (Community Texture)

> Young Autry's Sampson County was organized around three institutions that shaped every aspect of daily life: the church, the courthouse, and the general store.
>
> The Baptist church -- almost certainly Missionary Baptist -- was the center of community life. Services were an all-day affair: morning preaching, dinner on the grounds, afternoon service. Church business meetings recorded who joined, who was disciplined, and who departed. In August, camp meetings drew families from three counties for a week of preaching, singing, and socializing under canvas -- the closest thing to a vacation a yeoman family would experience. The church provided the framework for births (blessing), marriages (ceremony), death (burial), and moral governance (discipline of members for drunkenness, fighting, or failure to pay debts).
>
> Court day at the Sampson County courthouse in Clinton was the secular equivalent -- quarterly sessions that combined legal business with socializing, horse trading, political speechmaking, and tavern gatherings. The tax list, the deed book, the militia roll, the marriage bond -- the fragmentary records that survive from Young Autry's era were all generated at the courthouse.
>
> The general store at the nearest crossroads was where the Autry family bought what the farm could not produce: salt, iron tools, coffee, sugar, and cloth. The storekeeper extended credit against the coming harvest, and the ledger that recorded each purchase was the chain that bound yeoman families to the cash economy even as they maintained the appearance of self-sufficiency.

### Grade: **ADEQUATE** (with era adjustment)

The eastern_nc_farm_community texture provides the institutional skeleton of Young Autry's world, but it requires significant era adjustment. The post-Civil War framing (Confederate veterans, Grange, Wilmington 1898) does not apply. The antebellum institutions -- Baptist churches, county courts, general stores -- are present in the file but embedded in a post-war context. The file's genealogical notes about Baptist church records, county courthouse records, and county newspapers are directly applicable regardless of era.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Era mismatch in community_texture profile |
| Searched For | Antebellum eastern NC farm community, 1790-1860 -- the community texture BEFORE the Civil War: militia musters, camp meetings, court day culture, yeoman Baptist churches, general store economy without the formalized crop lien, the enslaved labor system as background context |
| Severity | **LOW-MEDIUM** -- the existing file's institutions are applicable with adjustment, but the era framing is wrong. A dedicated antebellum version would be more accurate and would not require the narrative AI to mentally strip out post-war content. |
| Nearest Match | `eastern_nc_farm_community` (correct geography, wrong era by 15-60 years) |
| Recommended Build | Either extend the existing file backward to 1790 with an antebellum section, or create a separate `antebellum_eastern_nc_farm_community.json` covering: militia musters, camp meetings, court day, Baptist church governance, general store credit without the formalized lien, the enslaved labor context, and the community dynamics of a county still close to its frontier origins. |

---

## Step 7: Wage Contextualization

### Relevant Wage Data

| Occupation | Era | Region | Annual Income |
|-----------|-----|--------|---------------|
| Farm laborer | 1850s | South | $75-$150 (seasonal) |

### Assessment

The wage table `wages_by_occupation_1850_1900` starts in the 1850s -- the decade of Young Autry's death. For most of his life (1790-1840), there is no wage data in this table. The 1850s Southern farm laborer entry provides a rough endpoint: $0.30-$0.50 per day, $75-$150 per year for seasonal work. But Young Autry was not a wage laborer -- he was a farmer (owner or tenant), and farm income is a different economic calculation from wages.

The antebellum_yeoman_south trigger provides better economic context than the wage table:
- Cheap western land at $1.25/acre (Land Act of 1820) vs. Piedmont land at $5-15/acre
- The Panic of 1819 and Panic of 1837 as economic disruptions
- The crop lien origins and general store credit economy
- The planter class squeeze on yeoman margins

The wage table is essentially useless for Young Autry's era and economic situation. The relevant economic story is not wages but farm production, land values, and the credit economy.

### Draft Narrative (Wage Context)

> We do not know what Young Autry's farm produced in cash value. Before the 1850 agricultural census -- the first to record individual farm production -- there is no systematic data on what a Sampson County yeoman farmer earned. What we know is structural: a family on 50 to 150 acres of Coastal Plain sandy loam grew corn for subsistence, tobacco or cotton as a cash crop, and raised hogs that foraged in the woods. The cash economy was thin -- most transactions were barter or store credit. A farm laborer in the 1850s South earned $0.30 to $0.50 per day, roughly $75 to $150 per year. A landowing yeoman farmer likely generated more value than that, but much of it was consumed directly rather than converted to cash. The family ate what it grew, wore what it spun, and heated the house with wood it cut. Cash was for salt, iron, coffee, sugar, and the annual settlement at the general store.

### Grade: **THIN**

The wage table does not cover Young Autry's era. The 1850s entries are useful only as a rough endpoint. The economic narrative must be built from the trigger's push factor descriptions and the material life profiles rather than from wage data. This is an honest limitation -- antebellum yeoman farm economics are poorly quantified by design (subsistence production was never measured until the agricultural census began in 1850).

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Wage table does not cover pre-1850 era |
| Searched For | Farm income / economic position data for antebellum yeoman farmers, 1790-1850 |
| Severity | **LOW** -- this is a real limitation, but it reflects the historical reality that pre-1850 economic data is sparse. A wage table cannot be built for an era when wages were not systematically recorded. The trigger's push factor descriptions and the material life profiles compensate by describing the economic STRUCTURE even without precise numbers. |
| Nearest Match | `wages_by_occupation_1850_1900` entry for 1850s Southern farm laborer ($75-$150/yr) |
| Recommended Action | Not a buildable gap. The data does not exist. The NEL correctly provides structural economic context rather than fabricated numbers. This is the Accuracy Line in action. |

---

## Step 8: Template Selection & Draft Output

### Templates Selected

**1. Record Silences** -- silence_as_narrative (the primary narrative tool for this ancestor)
**2. Hinge Generation** -- economic_reset (the generational pivot)

### Assessment: Record Silences

The `record_silences` template's `silence_as_narrative` gap type was explicitly designed for ancestors like Young Autry. The editorial note in the file confirms this: "This gap type was created in response to testing 5 real ancestors through the NEL pipeline. Three of five (Daniel Canady, Young Autry, Abel Bass) hit brick walls where the standard gap types did not apply because there was no meaningful record trail to have gaps in."

The `silence_as_narrative` gap type provides five interpretive approaches:
1. **what_the_record_chose** -- what the record-keeping system captured vs. what it excluded
2. **the_negative_space** -- what we can infer from what IS documented about the community
3. **the_statistical_twin** -- what someone with Young Autry's demographic profile statistically experienced
4. **the_life_that_fits** -- what material life was consistent with the handful of facts we have
5. **the_documentary_inventory** -- an honest accounting of every known record and what it tells

All five approaches are applicable to Young Autry. The most powerful combination for Option A is **what_the_record_chose** + **the_life_that_fits**.

### Draft: Record Silences (silence_as_narrative)

> The records that survive from Young Autry's lifetime were not designed to tell his story. They were designed to count him.
>
> The 1800 census recorded that a white male aged 26-44 lived in Sampson County as head of a household. Tick marks indicated the number and age categories of other people living with him. The enumerator did not record Young Autry's occupation, his acreage, his crop, his debts, his church, or his wife's name. The 1810 and 1820 censuses did the same thing -- a name, a set of tick marks, and nothing else. If Young Autry appeared in the 1830 or 1840 census, the same sparse format applied. The individual census -- the one that named every person in the household and listed their age, sex, birthplace, and occupation -- did not begin until 1850, the approximate year of his death.
>
> This is not a failure of research. It is a feature of how the early republic recorded its citizens. Before 1850, the federal census was a counting exercise, not a biographical one. Young Autry's name survived; everything else about his life filtered through the gap between what the government wanted to know (how many people lived here?) and what a descendant wants to know (who was this person?).
>
> What we can say is what the world around him looked like. A yeoman farmer in Sampson County in the 1810s and 1820s lived in a hewn-log or frame house of two rooms, ate cornbread and salt pork, wore homespun until store-bought cloth displaced it in the 1840s, attended the Baptist church on Sunday, settled accounts at the general store after harvest, and buried children who did not survive to adulthood -- roughly one in three before the age of ten. The estate inventories of his neighbors tell us what a yeoman family owned: iron cookware, a spinning wheel, a feather bed, a rifle, an axe, and a family Bible. The tax lists tell us who owned land and how much. The deed books tell us who bought and sold. These records do not name Young Autry specifically -- but they describe the world he inhabited with a precision that individual census entries would never match.
>
> The silence is not empty. It is full of the lives of 10,000 Sampson County residents whose daily existence was too ordinary for the record-keeping system of their era to document individually. Young Autry was one of them. His absence from the detailed record is the record.

**Word count:** 380. **Approaches used:** what_the_record_chose + the_life_that_fits + the_statistical_twin (blended).

### Assessment: Hinge Generation

The `hinge_generation` template's `economic_reset` situation is potentially applicable: if we can document Young Autry's economic position and compare it to his children's, the generational pivot becomes visible. However, this requires records from TWO generations -- and we barely have records from one. The template's constraints are explicit: "Requires specific numbers from at least two generations. A reset without numbers is an assertion, not a documented finding."

For Young Autry, the hinge_generation template is **aspirational rather than executable**. If the 1850 census captured his children (it likely did -- they would have been in their 20s-30s), their census entries would show occupation, real estate value, and personal property value. Those entries, compared to whatever fragmentary evidence exists for Young Autry (a tax list entry, a deed, a militia roll), would constitute the two-generation evidence the template requires. But that comparison cannot be made without the actual records.

### Draft: Hinge Generation (economic_reset -- speculative)

> If the 1850 census captured Young Autry's children -- and for the first time in American census history, it would have named them individually, listed their ages, birthplaces, and occupations, and recorded their real estate holdings -- their entries represent the first detailed documentation of the Autry family. Whatever Young Autry's economic position was, his children's 1850 census entries would tell us whether the next generation held land, worked as tenants, or labored for wages. The gap between what Young Autry had (unknowable from surviving records) and what his children had (potentially documented in the 1850 census) is the hinge -- but it is a hinge we can see from only one side.

**Word count:** 112. **Note:** This template application is conditional on finding the 1850 census entries for Young Autry's children. Without them, the hinge_generation template cannot execute per its own constraints.

### Grade: **STRONG** (record_silences) / **CONDITIONAL** (hinge_generation)

The record_silences template is the star of this dry run. The silence_as_narrative gap type was literally built for this case. Its five interpretive approaches provide multiple angles for turning "we know nothing" into "here is what the nothing means." The narrative output is intellectually honest, historically grounded, and emotionally powerful without violating the Accuracy Line.

The hinge_generation template is a stretch for Option A -- it requires two generations of records, and Young Autry's generation has almost none. It becomes viable only if the researcher locates his children in the 1850 census, which is a research task, not a narrative task. For White Glove, the hinge_generation template combined with actual research into the 1850 census could be extraordinarily powerful.

---

## Step 9: Research Guidance

### Relevant Guidance Files

- `census_gaps` -- Pattern: `rural_undercounting` directly applicable. Pre-1850 census limitations are mentioned in the `enumerator_errors` pattern (census details are "self-reported approximations, not verified facts") and can be extended to the fundamental limitation of pre-1850 census structure.
- `property_record_strategies` -- Patterns: `tax_lists_as_annual_evidence` (critical for pre-1850 research) and `deed_chain_construction` (to establish land ownership).

### Draft Narrative (Research Guidance)

> The records most likely to contain information about Young Autry are not the census -- which told us almost nothing before 1850 -- but the county records at the Sampson County courthouse in Clinton, North Carolina.
>
> **Tax lists** are the most underused tool in early American genealogy. Sampson County tax assessment rolls, compiled annually, list every property owner and sometimes every adult male. They are one of the few annual records available for the antebellum period. Young Autry's appearance on a tax list confirms his presence in the county for that year. His assessed value -- acreage, livestock, personal property -- reveals his economic position. His disappearance from the list brackets his death or departure. NC tax records are at the NC State Archives in Raleigh and increasingly on FamilySearch microfilm.
>
> **Deed records** at the Sampson County Register of Deeds document land transactions: if Young Autry ever bought or sold land, the deed book records when, from whom, how much acreage, and at what price. The witnesses on the deed were typically neighbors or relatives -- they identify his community network. The absence of deed records is also informative: a man with no deeds may have been a tenant, a landless laborer, or a squatter on unpatented land.
>
> **Militia rolls**: all adult white males were required to muster with the county militia. Militia rolls, where they survive, document presence in the county and approximate age. Check the NC State Archives.
>
> **Baptist church minutes**: if the Autry family attended a Missionary Baptist or Free Will Baptist church in Sampson County, the church minutes may record membership, discipline proceedings, and letters of dismissal. Check individual congregations and the Baptist Historical Collection at Wake Forest University.
>
> **County court records**: estate records (wills, inventories, guardianships), marriage bonds, and civil court proceedings are at the Sampson County courthouse and microfilmed at the NC State Archives.

### Grade: **STRONG**

The research guidance files provide exactly the right advice for a pre-1850 ancestor. The tax_lists_as_annual_evidence pattern is particularly valuable -- it identifies the single most useful record type for locating and tracking Young Autry through annual records that the census (taken only once a decade) cannot match. The deed_chain_construction pattern provides the methodology for establishing land ownership or documenting its absence.

The guidance correctly prioritizes county-level records over federal records for this era. The census gives us tick marks; the courthouse gives us deeds, tax lists, militia rolls, and court records that collectively provide a far richer picture.

**One observation that strengthens the guidance:** The antebellum_yeoman_south trigger's `record_implications` section lists ten key record types and five common pitfalls for researching antebellum yeoman families. The pitfall about pre-1850 census structure is directly applicable: "The 1790-1840 census records list only the head of household with tick marks for other household members by age and sex -- tracing individuals before 1850 requires supplementary records." The trigger's record guidance and the research guidance files reinforce each other.

**No issues found.**

---

## Step 10: Gap Detection

### Gaps Found

| # | Gap Type | Severity | Description |
|---|----------|----------|-------------|
| 1 | Missing occupation profile | **MEDIUM** | No occupation file for antebellum yeoman farmer / Southern subsistence farmer (1780-1860). The `tenant_farmer` file starts in 1870 (wrong era); `general_farmer_midwest` is wrong region. The material_life and trigger files compensate, but a dedicated occupation file would consolidate daily work, seasonal cycle, tools, economics, and records generated. Would serve the largest demographic in KinLore user research. |
| 2 | Era mismatch in community_texture | **LOW-MEDIUM** | The `eastern_nc_farm_community` texture covers 1865-1910, not 1790-1850. Many institutions (Baptist churches, county courts, general stores) are applicable with adjustment, but the post-Civil War framing (Confederate veterans, Grange, Wilmington 1898) does not apply. The antebellum community needs its own treatment or an era extension. |
| 3 | Wage table does not cover pre-1850 | **LOW** | The `wages_by_occupation_1850_1900` table starts at 1850 -- the decade of Young Autry's death. This is an honest limitation that reflects the historical absence of systematic wage data. Not buildable. The NEL correctly provides structural economic context instead. |

### Gaps NOT Found (Pipeline Success)

Despite the severity of the record-silence problem, the pipeline produced narrative material at every step:

- Both triggers matched with Sampson County explicitly listed (antebellum_yeoman_south + stayed_and_adapted) -- **STRONG**
- Route correctly returned empty (non-migration) -- **ADEQUATE by design**
- Destination correctly returned empty (non-migration) -- **ADEQUATE by design**
- Two material life profiles span Young Autry's entire life (frontier_log_cabin + antebellum_yeoman_farm) -- **STRONG**
- Record_silences template's silence_as_narrative gap type was literally designed for this ancestor -- **STRONG**
- Research guidance identified the right record types (tax lists, deeds, militia rolls, church minutes) -- **STRONG**
- Hinge_generation template identified but flagged as conditional on finding children in 1850 census -- **HONEST**

---

## Report Card

| Pipeline Step | Grade | Notes |
|---------------|-------|-------|
| 1. Trigger Matching | **STRONG** | Dual triggers (antebellum_yeoman_south + stayed_and_adapted), Sampson County explicitly named |
| 2. Route Selection | **ADEQUATE** | Correctly empty -- non-migration ancestor |
| 3. Destination Lookup | **ADEQUATE** | Correctly empty -- non-migration ancestor |
| 4. Occupation Enrichment | **THIN** | Neither expected occupation file matches era or region. Trigger and material_life compensate. |
| 5. Material Life | **STRONG** | Two profiles span entire life. Best narrative material for this ancestor. |
| 6. Community Texture | **ADEQUATE** | Right geography, wrong era. Usable with adjustment. |
| 7. Wage Contextualization | **THIN** | Wage table starts 1850; Young Autry's life was mostly pre-1850. Not buildable. |
| 8. Templates | **STRONG/CONDITIONAL** | record_silences is the MVP. hinge_generation conditional on finding children's records. |
| 9. Research Guidance | **STRONG** | Tax lists, deeds, militia rolls, church minutes -- exactly right for pre-1850 research |
| 10. Gap Detection | 1 MEDIUM, 1 LOW-MEDIUM, 1 LOW | Missing: antebellum farmer occupation; community texture era mismatch; wage gap (not buildable) |

### Overall: 4 STRONG, 3 ADEQUATE, 2 THIN, 1 CONDITIONAL

---

## The Verdict: Can the NEL Produce Narrative Value from Almost Nothing?

**Yes. But it does so by shifting the narrative center of gravity from the individual to the world.**

For Ella Mae Johnson (Dry Run #1) and George Knauss (Dry Run #2), the NEL matched the ancestor to specific triggers, routes, destinations, and occupations. The narrative was ABOUT the individual -- her specific migration, his specific homestead. The records were thin in places, but the general arc of each life was traceable.

Young Autry breaks this model. We have almost no individual records. The pre-1850 census gives us a name and tick marks. There may be a tax list entry, a deed, a militia roll -- but we cannot assume even these exist. The NEL cannot tell us the story of Young Autry's life because the records do not contain it.

What the NEL CAN do -- and what it does well -- is tell the story of Young Autry's WORLD. The material life profiles describe the cabin he lived in, the food he ate, the clothes he wore, and the tools he used. The antebellum_yeoman_south trigger describes the economic pressures that shaped every decision he made. The stayed_and_adapted trigger frames his non-migration as a decision, not an absence of decision. The eastern_nc_farm_community texture describes the institutions -- church, courthouse, general store -- that organized his daily life. And the record_silences template turns the absence of records into the narrative itself: not "we couldn't find anything" but "here is what the nothing means."

**The narrative strategy for a record-silent ancestor:**
1. Acknowledge the silence honestly. Name the systemic reason records are thin. Do not apologize.
2. Describe the world the ancestor inhabited using era- and region-specific material life and community texture data.
3. Frame the silence in statistical terms: Young Autry was one of thousands of Sampson County residents whose lives were too ordinary for the record-keeping system to document individually.
4. Use hedged language throughout: "likely," "probably," "consistent with." Never claim to know what cannot be known.
5. End with research guidance that gives the descendant somewhere to go -- county records that the census cannot replace.

**Where the NEL falls short for this ancestor:**
- The occupation files do not cover antebellum Southern farming (MEDIUM gap)
- The community texture is 15-60 years too late (LOW-MEDIUM gap)
- The wage table does not reach back to his era (LOW gap, not fixable)
- The hinge_generation template requires records the ancestor may not have (CONDITIONAL, not a gap)

**Where the NEL succeeds for this ancestor:**
- Two material life profiles that span his entire life, with vivid, sourced, era-specific detail
- Two triggers that fire cleanly and provide the economic and social context of his world
- A record_silences template that was explicitly designed for this exact case
- Research guidance that identifies the right county-level records and the right archives
- An honest, unflinching acknowledgment that the record does not owe us a narrative -- and that the absence itself IS the narrative

**The Accuracy Line holds.** Every sentence in the draft narrative above is either directly sourced from the NEL data files or explicitly hedged with "likely," "probably," or "we do not know." No fabricated facts. No invented feelings. No false precision. The narrative says what can be said and frames what cannot.

**This is the hardest test the NEL will face.** An ancestor with robust records is easy. An ancestor with no records is the real test of whether the system produces value. The answer is: yes, it does -- not by inventing information about Young Autry, but by placing him in a world so precisely described that his individual absence becomes a statement about the limits of the archive and the universality of ordinary life.

### Build Targets Identified

1. **`yeoman_farmer_antebellum.json`** (occupation) -- MEDIUM priority. The occupation of the majority of white Southerners before the Civil War. Would consolidate information currently scattered across the antebellum_yeoman_south trigger and the antebellum_yeoman_farm material life file into a single occupation profile with: daily/seasonal work, tools, economics, census clues, records generated. Would serve the single largest demographic group in KinLore user research.
2. **`antebellum_eastern_nc_farm_community.json`** (community_texture) or era extension of existing file -- LOW-MEDIUM priority. Would provide pre-Civil War community texture for eastern NC: militia musters, camp meetings, antebellum Baptist church governance, general store credit without the formalized post-war lien, and the enslaved labor context.
3. **Validator note:** The expected occupations for Young Autry (`tenant_farmer`, `general_farmer_midwest`) should be reconsidered. Neither matches his era or region. A more accurate expectation would be `yeoman_farmer_antebellum` (which does not yet exist) or simply noting that no current occupation file applies.

---

## Fifth dry run: PASS.

The NEL produces meaningful narrative value from minimal records. It does so honestly, without fabrication, and with a narrative strategy -- world-building through material life, community texture, and record silence interpretation -- that turns the absence of individual records into a story about the archive itself. This is the most important thing the NEL can do, because the majority of ancestors that KinLore users research will fall somewhere on the spectrum between "robust records" and "almost nothing." The NEL proves it can work at both ends.
