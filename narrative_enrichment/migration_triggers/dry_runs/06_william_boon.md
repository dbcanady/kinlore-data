# Narrative Dry Run #6: William Boon

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)
**Pipeline:** POLSIA_INTEGRATION.md 10-step ancestor processing
**Revenue Tier:** Option A (single-ancestor report)

---

## Ancestor Input Record

| Field | Value |
|-------|-------|
| Name | William Boon |
| Birth Year | 1830 |
| Origin | Nash County, NC |
| Destination | None (stayed -- died in war) |
| Arrival Year | None |
| Occupation | Turpentine laborer / farmer |
| Race | White |
| Era | 1830-1862 |

**Type:** Real test ancestor (user's family). Civil War KIA. This ancestor tests what the NEL does with a TRUNCATED LIFE -- a man who lived only 32 years and was killed in action during the Civil War. There is no destination, no arrival, no postwar life. The story gets cut off. The hinge_generation template matters here because his death IS the hinge -- his children's lives diverge because their father was killed. Nash County sits in eastern NC's turpentine belt -- longleaf pine country where naval stores (turpentine, rosin, tar, pitch) were the cash economy alongside subsistence farming.

---

## Step 1: Trigger Matching

### Matched Triggers

**Primary:** `civil_war_service` (core) -- era 1861-1870, migration_class: military
- Nash County, NC is **explicitly listed** in `counties_most_affected` -- one of only 15 counties named.
- Phase match: Phase 1, "Volunteer Rush" (1861-1862). William was killed in action during this early period, meaning he likely enlisted in the initial volunteer surge after Fort Sumter.
- Push factor match: `state_and_local_social_pressure` (severity 4) -- "communities organized public rallies, published lists of enlistees, and pressured men of military age to volunteer." In a Nash County crossroads community, not enlisting was not an option.
- Push factor match: `defense_of_home_community` (severity 4) -- "For men in border states and areas threatened by invasion, enlistment was directly linked to community defense." Eastern NC was invaded by Union forces in early 1862 (Burnside Expedition), making this personal for Nash County men.
- Counter-narrative match: `not_all_soldiers_were_willing` -- worth noting for completeness, but at Phase 1, most enlistments were volunteer.
- Template ref: The trigger explicitly activates the `military_service_arc` template.
- Material life ref: Points to `antebellum_yeoman_farm_1820_1860` -- the world William left.
- Community texture ref: Points to `eastern_nc_farm_community` -- Nash County is explicitly named.

**Secondary:** `antebellum_yeoman_south` (core) -- era 1790-1860, migration_class: economic
- Nash County, NC is **explicitly listed** in both `origin_counties` and `counties_most_affected`.
- Phase match: Phase 4, "Antebellum Crisis" (1837-1860). William's entire adult life (1830-1862) falls within the period of yeoman economic squeeze.
- Push factor match: `land_subdivision_heirs` (severity 4) -- the relentless subdivision of farms across generations. By the 1850s, Nash County farms were being divided into parcels too small to sustain a family.
- Push factor match: `soil_exhaustion_continuous` (severity 3) -- Nash County's sandy coastal plain soils were never suited to continuous cultivation. The longleaf pine barrens that produced turpentine were not prime farmland.
- Push factor match: `crop_lien_origins` (severity 2) -- the general store ledger as economic chain.
- Push factor match: `planter_squeeze` (severity 3) -- Nash County had a planter class with enslaved labor; non-slaveholding yeoman families like William's competed at a structural disadvantage.
- William's occupation as "turpentine laborer / farmer" fits the antebellum yeoman profile perfectly -- a man working seasonal turpentine extraction because farming alone did not pay.
- This trigger's `what_happened_to_those_who_stayed` section is directly relevant: "Families that did not migrate faced the continued pressure of subdivision, soil exhaustion, and economic marginalization." William stayed. Then the war came.

### Draft Narrative (Trigger Context)

> By 1860, William Boon's Nash County was a landscape of shrinking farms and thinning pines. The land that earlier generations had cleared from longleaf pine barrens was sandy, acidic, and never productive the way Piedmont red clay could be. The farms had been subdivided among heirs until a man's share might not feed his family through winter. Turpentine work -- chipping boxes into the trunks of longleaf pines and collecting the gum for distillation into spirits of turpentine and rosin -- supplemented what the farm could not provide. It was brutal, low-status work in a landscape of cut stumps and fire-blackened barrens, but it was cash income in a county where cash was scarce.
>
> When the war came in 1861, Nash County sent its men. The community pressure to enlist was overwhelming -- neighbors who had known William Boon all his life watched to see who volunteered and who did not. By early 1862, the war was not distant: Union forces under Ambrose Burnside were invading the eastern NC coast, taking New Bern in March 1862 and threatening the entire coastal plain. For a Nash County man, the war was not in Virginia. It was at the back door.

### Grade: **STRONG**

Both triggers fire cleanly. Nash County is explicitly named in both. The dual-trigger approach layers perfectly: the antebellum yeoman trigger establishes the economic world William lived in (shrinking farms, turpentine labor, planter squeeze), and the civil_war_service trigger narrates the moment that world was shattered. The push factors from both triggers reinforce each other -- the same economic pressures that were slowly grinding yeoman families down were then accelerated by war.

**Key observation:** This is NOT a migration story. William did not go anywhere voluntarily. He was mobilized. The antebellum_yeoman_south trigger normally describes families who left Nash County; William stayed and then was pulled into war. This inverts the normal pipeline flow -- there is no destination, no route selection, no arrival narrative. The pipeline must adapt.

---

## Step 2: Route Selection

### Matched Route

**None.** William Boon did not migrate. His movement was military -- from Nash County to wherever his regiment was assigned, on foot and by rail according to military orders. The civil_war_service trigger's transportation section covers this:
- Railroad: "Railroads were the primary means of moving troops to and between theaters."
- On foot: "Infantry soldiers marched. The daily march was the defining physical experience of Civil War service: 10-20 miles per day carrying 40-60 pounds of equipment."

There are no route files in the NEL for military movement because military movement is not migration -- it follows orders, not economic logic.

### Grade: **ADEQUATE** (by design)

The absence of a route match is correct behavior. This is not a migration story. The civil_war_service trigger's own transportation section provides the necessary context for military movement. The pipeline correctly recognizes that route files apply to voluntary movement, not military mobilization.

**No gap. Working as designed.**

---

## Step 3: Destination Lookup

### Matched Destination

**None.** William Boon had no destination. He did not migrate to a city, a homestead, or a new community. He was mobilized to wherever his unit was sent, and he was killed there. The destination fields in the civil_war_service trigger list military destinations (state rendezvous camps, Washington DC, Richmond, Chattanooga-Atlanta corridor, Vicksburg) -- but these are theaters of war, not settlement destinations.

For a Nash County Confederate soldier, the probable military destinations were:
- A state rendezvous camp (Camp Mangum in Raleigh is specifically named in the trigger)
- The Eastern Theater -- Virginia campaigns (Washington-Richmond corridor)
- Possibly eastern NC defense (against the Burnside Expedition)

Without knowing William's specific unit, we cannot determine his exact military route.

### Grade: **ADEQUATE** (by design)

Same as Route Selection: the absence is correct. The pipeline does not need a destination file for a KIA soldier. The narrative destination is a battlefield, documented in the CMSR and unit history, not in a destination profile.

**No gap. Working as designed.**

---

## Step 4: Occupation Enrichment

### Matched Occupation

`tenant_farmer` -- era 1870-1960

This is the closest available match, but it is **temporally misaligned**. The tenant_farmer file covers 1870-1960 (post-Civil War tenant farming), while William Boon lived 1830-1862 (antebellum). The tenant farming system described in the file -- with its formalized crop sharing, AAA programs, and mechanization pressures -- is the POSTWAR system. William's world was the antebellum precursor: subsistence farming on subdivided land, supplemented by turpentine labor.

The file's daily_work section ("Rented and farmed land owned by someone else. Unlike sharecroppers, tenant farmers typically owned their own tools, mules, and seed") is partially applicable to William if he was renting rather than owning. The economics section's description of cash rent vs. crop share arrangements applies to the antebellum period as well, though in a less formalized way.

### Turpentine Laborer -- KNOWN GAP

William's primary cash-earning occupation -- turpentine laborer -- is **not in the NEL occupation files**. This is a known gap from Priority 6 in the roadmap. The eastern_nc_farm_community texture file acknowledges this: "Turpentine and naval stores: in the southeastern counties (Bladen, Columbus, Robeson), turpentine extraction from longleaf pine was a seasonal cash-earning activity, especially for Black workers." But Nash County was also turpentine country, and the community texture's mention is a one-sentence note, not an occupation profile.

What a turpentine_laborer occupation file would need to cover:
- The work itself: boxing pines (cutting a V-shaped cavity in the trunk to collect gum), scraping and collecting crude turpentine, hauling barrels to the distillery
- The economics: piece-rate pay per barrel, seasonal cycle (March-November), relationship to farm labor
- The hazards: exposure to turpentine fumes, burns from distillery work, rattlesnakes in the piney woods, fire danger
- The social status: turpentine work was low-status -- below farming, associated with both poor whites and enslaved/free Black workers
- The record trail: naval stores production records, distillery ledgers, census occupation listings

### Draft Narrative (Occupation)

> The census might list William Boon as "farmer," but the census was taken in June, and in June a Nash County man was probably in the pine barrens. Turpentine extraction -- chipping boxes into the trunks of longleaf pines, scraping the gum that oozed from the cuts, hauling barrels of crude turpentine to the nearest distillery -- was the cash economy of eastern North Carolina's pine belt. The work was seasonal (March through November), paid by the barrel, and ranked below farming in the community's social hierarchy. But it was cash money, and for a man whose farm share was too small to feed a family, the pine woods offered what the exhausted soil could not.
>
> Whether William owned his land or rented it, the economic reality was similar: a small parcel of sandy coastal plain soil, a garden, a few hogs running in the woods, and turpentine work to make up the difference. The 1850 census for Nash County would show his household composition and the value of his real estate -- if any. The agricultural schedule would document what he grew and what livestock he kept. These records, combined with the turpentine production data that the distillery might have recorded, would outline the economic life of a man who worked two marginal occupations and never accumulated enough to leave.

### Grade: **THIN**

The tenant_farmer file is temporally wrong for William (post-Civil War vs. antebellum). The turpentine_laborer occupation is a documented gap. The narrative relies heavily on the antebellum_yeoman_south trigger's economic context and the eastern_nc_farm_community texture rather than a dedicated occupation profile. The draft above is plausible and historically grounded, but it is drawing from general context, not from a specific occupation file.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing occupation profile |
| Searched For | turpentine_laborer / naval_stores_worker -- the occupation of extracting turpentine, rosin, tar, and pitch from longleaf pine forests in eastern NC, SC, and GA |
| Severity | **MEDIUM** -- the narrative can be constructed from the community texture and trigger context, but there is no dedicated occupation file covering the work, the economics, the hazards, or the record trail |
| Nearest Match | None. The tenant_farmer file is the wrong era and the wrong industry. |
| Recommended Build | `turpentine_laborer.json` covering: boxing pines, scraping gum, distillery work, piece-rate economics, seasonal cycle, social status hierarchy, racial composition (both white and Black workers), naval stores production records, longleaf pine ecology, relationship to farming, the transition from natural-growth harvesting to destructive extraction. Would serve NC, SC, and GA ancestors in the pine belt. |

---

## Step 5: Material Life Grounding

### Matched Material Life Profile

`antebellum_yeoman_farm_1820_1860` -- matches William's origin (Nash County, NC) and era (1830-1862) exactly.

This is the strongest match of any file in the pipeline. William Boon IS the person this material life profile was written for: a non-slaveholding white yeoman farmer in the Upper South, 50-200 acres (or less), subsistence farming with a small cash component, 1820-1860.

The `economic_position` field is critical here. William could be:
- **Landowner**: "The ancestor owned their land, worked it themselves, and appeared in deed books and tax rolls."
- **Tenant**: "The ancestor worked someone else's land for a share of the crop or a cash rent. They do NOT appear in deed records."
- **Landless laborer**: "The ancestor owned no land and worked for daily wages on others' farms."
- **Marginal**: "The ancestor existed at the margins of the yeoman economy -- a squatter on unpatented land, a widow farming a dower tract, or a family on less than 20 acres of exhausted soil."

Without checking William's actual census records, we cannot determine his exact position. But the occupation "turpentine laborer / farmer" suggests either **tenant** or **marginal** -- a man supplementing inadequate farming with wage labor in the pine woods. Landowners generally did not do turpentine work; they hired it out or leased their timber.

### Draft Narrative (Material Life)

> The house William Boon's family lived in was likely a log or frame structure of two rooms with a sleeping loft -- the dogtrot plan common in eastern North Carolina's coastal plain. If the family owned it, it sat on stone piers over the sandy soil, with a detached kitchen and a smokehouse out back. If they rented, the house belonged to the landlord, and the quality depended on the landlord's inclination to maintain it. Either way, the material world was the same: cast-iron pots over a hearth fire, cornbread at every meal, salt pork from the November hog killing, a kitchen garden of beans and sweet potatoes, and a spinning wheel that was gathering dust as store-bought calico replaced homespun.
>
> Saturday evening meant heated water in the washpot. Sunday morning meant the Baptist church. The general store ledger at the crossroads recorded the family's year in credit entries: seed corn and coffee in March, calico cloth in April, quinine in July, salt for the hog killing in November. Each entry marked "on account" -- against a crop that had not been harvested yet and a turpentine season that had not ended. The family Bible, if they had one, recorded the births. In Nash County in the 1850s, a family's entire material wealth -- everything that would appear in an estate inventory -- might amount to less than the value of two good mules.

### Grade: **STRONG**

The antebellum_yeoman_farm_1820_1860 material life profile is the right file for the right ancestor. Every detail in the profile applies directly to William Boon's Nash County world: the dogtrot house, the detached kitchen, the iron cookware, the hog killing, the general store credit system, the kitchen garden, the homespun-to-store-bought transition. The sensory snapshot ("Woodsmoke hangs low over the farmstead in the early chill...") could be William's farmstead.

The `economic_position` framework adds critical flexibility -- the narrative can adjust for whether William owned or rented, and the adjustment changes the story meaningfully (a landowner who left property to be divided vs. a tenant who left nothing but children).

**No issues found with the file itself. The gap is in the occupation profile, not the material life.**

---

## Step 6: Community Texture

### Matched Community Texture

**Origin:** `eastern_nc_farm_community` -- origin_community, era 1865-1910

This file is designed for the community William Boon lived in. Nash County is within the geographic scope ("Eastern North Carolina coastal plain farm country -- Wayne, Johnston, Sampson, Duplin, Harnett, Cumberland, Robeson, Bladen, Columbus, Lenoir, Greene, Pitt counties"). Nash County is not explicitly listed in the location.geographic_scope (an oversight -- it lists counties further south and east), but the community described IS Nash County's community.

**However, the era is slightly misaligned.** The file covers 1865-1910 (post-Civil War), while William lived 1830-1862 (antebellum). The institutions described -- Missionary Baptist churches, crossroads general stores, Confederate memorial associations -- existed in both periods (except the memorial associations, which are postwar). The crop lien system described in the file had its antebellum origins in the credit economy William knew. The community rhythms (tobacco cycle, cotton cycle, court days, camp meeting, hog killing) are identical for both the antebellum and postbellum periods.

The file's most powerful element for William's narrative: the `informal_economy` section lists "Turpentine and naval stores: in the southeastern counties (Bladen, Columbus, Robeson), turpentine extraction from longleaf pine was a seasonal cash-earning activity." This confirms turpentine as part of the eastern NC farm community's economic texture.

The `Confederate memorial associations and veterans' groups` institution is poignantly relevant: William would never be a member because he was killed. But his widow and children would interact with these organizations -- they defined the community's post-war identity.

### Draft Narrative (Community Texture)

> Nash County's community life revolved around three points on the map: the Baptist church, the crossroads general store, and the county courthouse in Nashville. On Sunday, William Boon's family gathered with neighbors at the Missionary Baptist church nearest their farm -- the building that served as meetinghouse, social hub, and moral court for the surrounding five-mile radius. The church minutes recorded who joined, who was dismissed, and who was disciplined. On court day, the entire community converged on the county seat for legal business, horse trading, and political talk. On ordinary days, the general store was where the community happened -- men on the porch, a ledger on the counter, news carried by peddlers and circuit riders.
>
> Camp meeting in late August was the one week that felt like abundance -- families camping on the grounds, cooking over open fires, singing and preaching and visiting cousins from adjacent counties. By September, the cotton was ready and the turpentine season was winding down, and the community settled back into the rhythms that had governed eastern NC farm life for three generations. In this world, everyone knew William Boon. When he enlisted, everyone knew that too.

### Grade: **STRONG** (with caveats)

The eastern_nc_farm_community texture is deeply detailed and directly applicable to William's world. The Missionary Baptist church, the crossroads store, the crop lien system, the court day rhythm -- these are the institutions and rhythms of his life. The file's treatment of race and the Wilmington 1898 context is postwar and does not apply to William's antebellum period, but the core community structures are continuous across the war.

**Two caveats:**
1. Nash County is not explicitly listed in the geographic_scope (an oversight in the file -- it lists neighboring counties but not Nash).
2. The era range (1865-1910) starts after William's death. The file is designed for the community his family lived in after he was killed, not the one he knew. The overlap is substantial, but the antebellum community had different institutions (militia musters, slave-hiring markets, different political structures).

### GAP IDENTIFIED (minor)

| Field | Value |
|-------|-------|
| Gap Type | Geographic scope oversight |
| Description | Nash County is not listed in the eastern_nc_farm_community file's geographic_scope field, despite being squarely within the region described and being explicitly listed in both the civil_war_service and antebellum_yeoman_south trigger files. |
| Severity | **LOW** -- the file clearly covers Nash County's type of community; the county name is simply missing from the list. |
| Fix | Add "Nash" to the geographic_scope counties list in eastern_nc_farm_community.json |

---

## Step 7: Wage Contextualization

### Relevant Wage Data

| Occupation | Era | Region | Annual Income |
|-----------|-----|--------|---------------|
| Farm laborer | 1850s | South | $75-$150 (seasonal) |
| Farm laborer | 1860s (postwar) | South | $50-$150 |
| Sharecropper | 1860s | South | $0-$100 net (often negative) |
| General laborer | 1860s | Northeast | $250-$400 |

The wages_by_occupation_1850_1900 table provides the Southern farm laborer data that frames William's economic life. At $0.30-$0.50 per day and $75-$150 per year (seasonal), Southern farm labor in the 1850s was subsistence-level. The context note is critical: "Enslaved labor dominated Southern agriculture; free white farm laborers earned subsistence wages."

Turpentine laborer wages are NOT in the wage table (consistent with the missing occupation file). Historical sources suggest turpentine workers in the antebellum period earned comparable or slightly higher daily rates than farm laborers ($0.50-$0.75/day), but the work was seasonal and piece-rate (payment per barrel of crude turpentine collected).

The most important wage comparison for William's story is not a destination comparison (he never migrated) but a **military comparison**: a Confederate private's pay was $11/month in 1861 ($132/year) -- roughly equivalent to what a farm laborer earned, but the military pay was steady and nominally guaranteed (though the Confederate government frequently fell behind on pay).

### Draft Narrative (Wage Context)

> William Boon's economic life can be framed in a single comparison. A farm laborer in Nash County in the 1850s earned $0.30 to $0.50 per day -- $75 to $150 for a full year of seasonal work. Turpentine extraction might have added another $50 to $100 in cash, paid by the barrel at the distillery. A Confederate private's pay was $11 per month -- $132 per year, comparable to what Nash County farm labor paid, but theoretically steady. For a man with a family and no land, the arithmetic of enlistment was not purely patriotic. The army paid, fed, and clothed you. The farm might not.
>
> But the arithmetic had a variable the ledger could not capture: the probability of dying. Approximately one in four Confederate soldiers was killed or died of disease. The $11-a-month wages were paid against those odds.

### Grade: **ADEQUATE**

The wage table provides the farm laborer data needed to ground William's economic life. The missing turpentine laborer wages are a gap (consistent with the missing occupation file), but the farm laborer data covers his farming income. The military pay comparison is drawn from the civil_war_service trigger, not from the wage table -- the table does not include military pay as an occupation. This is a reasonable omission (military pay is a trigger-level detail, not a wage-table occupation), but it means the narrative AI must synthesize across files.

### GAP IDENTIFIED (minor)

| Field | Value |
|-------|-------|
| Gap Type | Missing wage data |
| Description | No wage data for turpentine laborers in the 1850s South. Also, no military pay data in the wage table (military pay is covered in the trigger file but not cross-referenced in the wage table). |
| Severity | **LOW** -- turpentine wages are part of the larger turpentine_laborer occupation gap; military pay is available from the trigger file. |
| Fix | Include in the recommended turpentine_laborer.json occupation build. |

---

## Step 8: Template Selection & Draft Output

### Templates Selected

**1. Military Service Arc** -- wound_capture_death situation (William was KIA -- this is the critical event)
**2. Hinge Generation** -- scattered_children situation (William's death IS the hinge)
**3. Record Silences** -- family_aftermath_overlay (what happened to the family after William was killed)

This is where the TRUNCATED LIFE problem becomes acute. The standard pipeline assumes a life arc: trigger --> route --> destination --> occupation --> settlement --> aging --> death. William's story is: trigger --> enlistment --> killed. The arc is cut short. The templates must handle this truncation.

### Assessment: Does the military_service_arc template handle KIA?

**Yes.** The `wound_capture_death` situation explicitly covers death in service:
- "Death in service (combat, disease, or accident), or any combination. This is often the most documented moment of an ancestor's entire life."
- Structural beats include: "For death: cause as stated in the record. Disease death should be treated with the same documentary precision and narrative gravity as combat death."
- "'Died of chronic diarrhea, General Hospital No. 9, Richmond, March 14, 1863' is a complete and devastating sentence. Do not elaborate."
- The file includes burial location guidance: "Soldiers who died in service were buried in national cemeteries, regimental burial grounds, or local churchyards."

The template also includes the `pension_and_aftermath` situation, which applies to William's **widow**, not William himself: "The widow's pension variant: when the veteran died, the widow's application reveals her own circumstances -- her age, her economic condition, whether she remarried."

For Confederate soldiers specifically: "Confederate veterans were excluded from federal pensions" and "Confederate pensions were administered by individual states." William's widow would have applied for a NC Confederate pension -- the state archives hold these records.

### Draft: Military Service Arc (wound_capture_death)

> William Boon enlisted in Nash County -- probably at a muster in Nashville or at a crossroads church where the company was being organized, in 1861 or early 1862. His Compiled Military Service Record, if it survives in NARA Record Group 109, would document his enlistment date, his unit assignment, his rank (almost certainly private), and every bimonthly muster roll that recorded whether he was present, absent sick, or on detached service.
>
> The muster rolls end with a final notation: killed in action. The CMSR records the date and, sometimes, the place. The unit history identifies the engagement. But the record says only what it says -- a date, a place, a notation. William Boon was 32 years old. He had been alive for less time than many of his neighbors' fences had been standing.
>
> If the place of burial is documented -- a regimental burial ground, a hospital cemetery, a field burial near the engagement site -- it may still be identifiable. If not, he lies in soil that has long since absorbed the wooden markers that Confederate burial details used when they had time to bury their dead. Confederate soldiers killed in Virginia were frequently buried by their comrades in shallow graves near the battlefield. The graves are documented in some unit histories; many were never found.

**Word count:** 210. **Beats:** Event, aftermath, burial (3 of 6 applicable -- no hospital, no POW, no pension for William himself).

### Draft: Hinge Generation (scattered_children)

> The hinge is a date: the date William Boon was killed. Before that date, the household existed -- William, his wife, their children, however many there were, in a Nash County house or cabin, farming and working turpentine. After that date, the household had to survive without its primary earner. The 1860 census shows the intact household. The 1870 census -- if the family can be located -- shows the aftermath.
>
> The children's locations in the 1870 census tell the story. If they are all in one place -- the widow's household or a grandparent's household in Nash County -- the family network held. If they are scattered across different counties, the household could not hold together and the children were absorbed by relatives, bound out as apprentices, or put to work on other farms. If some children cannot be found in 1870 at all, the silence is its own data.
>
> For families like William Boon's -- non-slaveholding white yeomen who lost their primary earner to the war -- the generational reset was steep. The father had been a farmer and turpentine laborer with perhaps a small parcel of land or a tenancy. The children, fatherless in a devastated postwar economy, likely started as laborers, tenant farmers, or sharecroppers. The $800 or $1,200 in real estate that a yeoman family might have held in 1860 became zero or near-zero in 1870 -- not because the land was taken, but because the war destroyed property values, the labor system that supported them, and the man who worked them.

**Word count:** 251. **Beats:** All 5 hit (anchor, break, scatter, pattern, trace).

### Draft: Record Silences / Family Aftermath Overlay

> William Boon's records end with his death. But the records for the people who survived him continue -- and they tell the economic story of his death more clearly than any military record.
>
> If William's widow filed a Confederate pension application with the State of North Carolina -- and the NC State Archives holds these records -- the application would document her age, her economic condition, her children's names and ages, and her own struggle to survive without the family's primary earner. Confederate widows' pensions in North Carolina were small ($30-$60 per year by the time the system was established in the 1880s-1890s), and the application had to demonstrate both the veteran's service and the widow's continued unmarried status. If she remarried, the pension was forfeited.
>
> The critical question is not what happened to William -- the military record answers that. The critical question is what happened to his family. Did the widow hold the farm or tenancy? Was she taken in by her parents or siblings? Were the children bound out or apprenticed? Did the family stay in Nash County or disperse? The 1870 census is the first document that can answer these questions. The Confederate pension application, if it exists, is the second.

**Word count:** 207.

### Grade: **STRONG**

All three templates fire appropriately for this ancestor. The military_service_arc handles KIA cleanly -- the wound_capture_death situation was designed for exactly this case. The hinge_generation template's scattered_children situation maps perfectly onto a family that lost its primary earner to war. The record_silences family_aftermath_overlay centers the right question: not "what happened to William?" but "what happened to everyone he left behind?"

**One critical observation:** The military_service_arc template does not have a specific beat for "young death" or "life cut short." The template assumes the narrative moves through enlistment --> service --> wound/capture/death --> pension --> veteran_in_community. For William, the arc terminates at step 3. The template handles this gracefully (each situation is independent), but there is no explicit guidance for what to do when the LIFE is the truncated element, not just the military career. The hinge_generation template fills this gap -- it picks up where the military arc drops off.

---

## Step 9: Research Guidance

### Relevant Guidance Files

- `census_gaps` -- William spans 1830-1862, covering censuses from 1840 through 1860. He was killed before the 1870 census. The 1850 census (the first to name all individuals) and the 1860 census are the critical documents for his civilian life. The 1870 census is critical for his FAMILY's aftermath.
- `military_record_strategies` -- The `civil_war_pension_files` pattern is directly applicable, specifically the widow's pension section: "the widow's file often contains the most family information because she had to prove the marriage and identify all children." However, this pattern describes FEDERAL (Union) pensions. William was Confederate. The guidance correctly notes: "For Confederate pensions, contact the state archives for the state where the veteran applied." NC Confederate pension records are at the NC State Archives.

### Draft Narrative (Research Guidance)

> The records that document William Boon's life fall into two categories: the civilian records before the war, and the military records of the war itself.
>
> For the civilian life: the 1850 federal census is the first to list William by name, with age, occupation, birthplace, and household composition. The 1860 census provides the same data a decade later, along with the agricultural schedule showing crop production, livestock, and farm value. Nash County deed records would show whether William owned property; tax lists would show his relative economic position. Baptist church minutes from the congregation nearest his farm may document membership. These records are at the Nash County courthouse and on FamilySearch microfilm.
>
> For the military life: search the National Park Service Soldiers and Sailors Database for William Boon's unit and rank. Then request the Compiled Military Service Record from NARA (Record Group 109, Confederate records). The CMSR will establish enlistment date, unit assignment, and the circumstances of death as documented on the final muster roll or casualty report. North Carolina's state adjutant general records -- published as a multi-volume roster of NC troops -- list every Confederate soldier from the state with service details.
>
> For the family aftermath: the NC Confederate Pension application, if the widow filed one, is at the NC State Archives. It would document the widow's name, the children, and the family's economic condition decades after William's death. The 1870 census is the first document that shows the household after William's death.

### Grade: **STRONG**

Both guidance files provide specific, actionable research advice. The census_gaps file's treatment of the 1850 and 1860 censuses as anchor documents is exactly right. The military_record_strategies file's pension section applies to William's widow (adjusted for Confederate state pensions rather than federal pensions). The NC State Archives as the repository for Confederate pension records is correctly identified.

**One important addition the guidance should surface:** The North Carolina Troops series (published by the NC Office of Archives and History) provides detailed unit histories for every NC regiment, including rosters with individual soldiers' service records. This is the single most useful published source for NC Confederate soldiers and is not mentioned in the military_record_strategies guidance file, which focuses on federal records.

---

## Step 10: Gap Detection

### Gaps Found

| # | Gap Type | Severity | Description |
|---|----------|----------|-------------|
| 1 | Missing occupation profile | **MEDIUM** | No profile for turpentine laborer / naval stores worker. This is the primary cash-earning occupation for William Boon and for thousands of eastern NC residents (both white and Black) from the colonial era through the early 20th century. The gap affects the daily-life narrative, the wage comparison, and the record guidance for turpentine production records. |
| 2 | Missing wage data | **LOW** | No wage data for turpentine laborers in the 1850s South. Part of the larger turpentine_laborer occupation gap. Historical rates were approximately $0.50-$0.75/day, paid by the barrel. |
| 3 | Geographic scope oversight | **LOW** | Nash County not listed in the eastern_nc_farm_community geographic_scope field, despite being within the region and being named in both the civil_war_service and antebellum_yeoman_south trigger files. |
| 4 | Template gap -- truncated life | **LOW** | No explicit pipeline guidance for what to do when the ancestor's life is so short (32 years, killed in action) that the standard life-arc model does not apply. The existing templates handle this through situation independence (military_service_arc) and generational bridging (hinge_generation), but there is no explicit guidance document for the "short life" case. |

### Gaps NOT Found (Pipeline Success)

- Primary trigger (civil_war_service) matched with Nash County explicitly listed ✓
- Secondary trigger (antebellum_yeoman_south) matched with Nash County explicitly listed ✓
- Route correctly routed around (military mobilization, not migration) ✓
- Destination correctly routed around (KIA, no settlement destination) ✓
- Material life (antebellum_yeoman_farm) perfect era and region match ✓
- Community texture (eastern_nc_farm_community) deeply relevant ✓
- Military_service_arc template handles KIA cleanly ✓
- Hinge_generation template handles the family aftermath ✓
- Record_silences family_aftermath_overlay centers the widow's story ✓
- Research guidance provides actionable paths for both civilian and military records ✓
- Wage data covers farm laborer comparisons ✓

---

## Report Card

| Pipeline Step | Grade | Notes |
|---------------|-------|-------|
| 1. Trigger Matching | **STRONG** | Dual triggers (civil_war_service + antebellum_yeoman_south), Nash County explicitly named in both |
| 2. Route Selection | **ADEQUATE** | No route needed -- military mobilization, not migration. Working as designed. |
| 3. Destination Lookup | **ADEQUATE** | No destination needed -- KIA, no settlement. Working as designed. |
| 4. Occupation Enrichment | **THIN** | tenant_farmer file is wrong era; turpentine_laborer is a known missing profile |
| 5. Material Life | **STRONG** | antebellum_yeoman_farm_1820_1860 is the perfect match for this ancestor |
| 6. Community Texture | **STRONG** | eastern_nc_farm_community deeply relevant (minor: Nash County not in scope list) |
| 7. Wage Contextualization | **ADEQUATE** | Farm laborer wages correct; turpentine wages missing; military pay from trigger file |
| 8. Templates | **STRONG** | Military_service_arc + hinge_generation + record_silences overlay all fire correctly |
| 9. Research Guidance | **STRONG** | Census + military record strategies both actionable; NC Confederate pensions correctly identified |
| 10. Gap Detection | 1 MEDIUM, 3 LOW | Missing: turpentine_laborer occupation; wage data; Nash County in texture scope; truncated-life guidance |

### Overall: 6/10 STRONG, 2 ADEQUATE, 1 THIN, 1 N/A

**The NEL produces a good narrative for William Boon, but the TRUNCATED LIFE exposes structural assumptions in the pipeline.** The triggers, material life, community texture, templates, and research guidance all work well. The pipeline correctly adapts to a non-migration case (no route, no destination). But the occupation gap (turpentine laborer) leaves a meaningful hole in the daily-life narrative, and the pipeline has no explicit guidance for handling a life that ends at 32.

The most important finding from this dry run: **the hinge_generation template is the star of this narrative.** For a KIA ancestor, the military_service_arc handles the death, but the hinge_generation handles the MEANING of the death -- what it did to the family, how the children's lives diverged, whether the household survived. This is the template that turns a short, blunt military record into a family story.

### Build Targets Identified

1. **`turpentine_laborer.json`** (occupation) -- MEDIUM priority. Covers boxing pines, scraping gum, distillery work, piece-rate economics, seasonal cycle, social status, racial composition, naval stores production records, longleaf pine ecology, and the transition from natural-growth harvesting to destructive extraction. Would serve NC, SC, and GA pine belt ancestors across two centuries. This is the same gap identified in Priority 6 of the roadmap.
2. **Nash County added to eastern_nc_farm_community scope** -- LOW priority, 30-second fix. Add "Nash" to the geographic_scope counties list.
3. **Truncated-life pipeline note** -- LOW priority. Add a note to POLSIA_INTEGRATION.md acknowledging that some ancestors die young and the standard life-arc model does not apply. Guidance: lean on hinge_generation for the family aftermath and record_silences for the documentary void. The military_service_arc's situation independence already handles the military narrative cleanly.

---

## Narrative Quality Assessment

**Does the NEL data produce a story worth reading?**

Yes, but it is a different kind of story. This is not a migration arc, not a rags-to-riches trajectory, not a long life lived across changing eras. It is a 32-year life that ends on a battlefield, and the story continues through the people who survived.

**What makes this case important for the product:**

- It tests the NEL's ability to handle ABSENCE -- no destination, no route, no postwar life, no pension for the veteran himself. The pipeline must produce a narrative from what is NOT there.
- It proves the hinge_generation template's value. Without this template, William's story would be a military record and a blank page. With it, the story continues through his children -- where they went, what they became, whether the family held together. The death is not the end of the narrative; it is the beginning of the hinge.
- It proves the record_silences family_aftermath_overlay's value. The overlay's widow_survival and children_scatter situations are exactly what this case needs. The widow's Confederate pension application, if it exists, may be the richest document about this family -- and it was filed by someone other than the ancestor.
- It validates the pipeline's ability to route around missing components. Steps 2 and 3 (route and destination) correctly return ADEQUATE/by design rather than flagging false gaps. The pipeline recognizes that a KIA soldier does not need a destination profile.

**What could be stronger:**

- A turpentine_laborer occupation file would give the daily-life narrative the kind of specific, sourced detail that makes KinLore reports vivid. Right now, the turpentine work is mentioned but not profiled.
- The military_service_arc template could benefit from a brief note on handling very short service periods (enlistment to KIA in less than two years) and soldiers killed before any pension claim was possible.
- The community texture file should list Nash County in its geographic scope.

**The Accuracy Line holds.** The draft narrative paragraphs above use "likely," "probably," and "if" throughout. No emotions are projected onto William Boon. No heroism is ascribed. The military death is stated as a record notation, not a dramatic scene. The turpentine work is described as an economic calculation, not a character trait. The hinge_generation treatment asks where the children ended up, not how they felt about losing their father. The records speak; the narrative presents what they say.

**What this dry run reveals about the NEL as a product:**

The NEL was designed primarily for MIGRATION stories -- people who went somewhere. William Boon went nowhere. He was born in Nash County, lived in Nash County, enlisted in Nash County, and was killed somewhere else before he could come back. The pipeline handles this non-migration case well enough -- but the ENERGY of the narrative shifts from the ancestor to the family. William's story is short and blunt. His family's story is long and complex. The NEL's templates (hinge_generation, record_silences, military_service_arc) together produce that family story from what are, individually, very spare records.

The lesson: KinLore is not always telling the story of the ancestor. Sometimes it is telling the story of what the ancestor's life -- and death -- did to everyone around them.

**Sixth dry run: PASS.**
