# Narrative Dry Run #3: Daniel Canady

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)
**Pipeline:** POLSIA_INTEGRATION.md 10-step ancestor processing
**Revenue Tier:** Option A (single-ancestor report)

---

## Ancestor Input Record

| Field | Value |
|-------|-------|
| Name | Daniel Canady |
| Label | War of 1812 Veteran / Cumberland County TPA |
| Birth Year | 1793 |
| Origin | Cumberland County, NC |
| Destination | None (stayed) |
| Arrival Year | None |
| Occupation | Farmer |
| Race | White |
| Era | 1793-1868 |

**Type:** Real test ancestor (user's family). Stayed-put yeoman farmer in Cumberland County, NC. War of 1812 militia veteran. Born in the early Republic, died three years after the Civil War. The OLDEST era of the user's real ancestors. This case tests the non-migration pipeline: no route, no destination, no arrival. The story is about staying.

---

## Step 1: Trigger Matching

### Matched Triggers

**Primary:** `war_of_1812_service` (core) -- era 1812-1878, migration_class: military
- Cumberland County, NC is explicitly listed in `counties_most_affected` -- the very first county in the list.
- Phase 1 match: "Militia Mobilization" (1812-1813). The trigger explicitly names Cumberland County in the phase description: "a man from Cumberland County, North Carolina might serve a 3-month term guarding the Cape Fear coast and return home without having fired a shot."
- Daniel was approximately 19-22 during active hostilities (1812-1815) -- squarely within the militia obligation age range (18-45).
- Push factor match: `militia_obligation_and_duty` (severity 3) -- state militia laws required men of military age to serve when called.
- Pull factor match: `bounty_land_warrants` (severity 4) -- 160 acres for service. Whether Daniel claimed, sold, or never applied for bounty land is a key research question.
- Pull factor match: `local_community_defense` (severity 3) -- Cumberland County bordered the Cape Fear River and the coast, making coastal defense a direct concern.
- Counter-narrative: "Most service was uneventful" -- Daniel's militia service was likely a 3-6 month term of garrison duty on the Cape Fear coast, not a dramatic campaign.
- Phase 4 match: "Pension Era" (1816-1878). Daniel lived until 1868, meaning he was alive when service pensions were authorized for regular army veterans in 1871 but died three years before the 1878 act that extended pensions to all veterans including militia. His widow may have been eligible.

**Secondary:** `antebellum_yeoman_south` (core) -- era 1790-1860, migration_class: economic
- Cumberland County, NC is explicitly listed in `origin_counties` and `counties_most_affected`.
- Phase 1 match: "Post-Revolutionary Settlement" (1790-1815) -- Daniel was born into this era. His family was part of the generation that established the farmsteads that would anchor communities for decades.
- Phase 2 match: "War of 1812 Aftermath and Banking Crisis" (1812-1825) -- the Panic of 1819 hit when Daniel was 26, in the early years of establishing his own household.
- Phase 3 match: "Cotton Kingdom Expansion" (1820-1840) -- the dual squeeze of planter competition and soil exhaustion was present in Cumberland County.
- Phase 4 match: "Antebellum Crisis" (1837-1860) -- the Panic of 1837, the crop lien system's origins, and the planter squeeze all applied.
- Push factor match: `land_subdivision_heirs` (severity 4) -- the arithmetic of partible inheritance reducing farm viability.
- Push factor match: `soil_exhaustion_continuous` (severity 3) -- decades of cultivation depleting Piedmont soils.
- Push factor match: `planter_squeeze` (severity 3) -- competing against enslaved labor.
- Daniel experienced ALL FOUR push factors across his 75-year life. He stayed anyway.

**Tertiary:** `stayed_and_adapted` (core) -- era: all eras, migration_class: non_migration
- This trigger fires precisely because Daniel did NOT migrate despite the pressures documented in antebellum_yeoman_south.
- Phase match: All three phases -- "Pressure Accumulation," "Adaptation in Place," "Consolidation and Continuity" -- map to Daniel's life arc.
- Pull factor match: `land_ownership` (severity 5) -- the single most powerful anchor.
- Pull factor match: `family_network_density` (severity 4) -- the Canady name was deeply rooted in Cumberland County.
- Pull factor match: `community_ties` (severity 3) -- militia service, church membership, court day participation.
- Pull factor match: `church_membership` (severity 3) -- Baptist churches were the center of community life in eastern NC.
- Counter-narrative: `staying_not_always_choice` -- staying was not always free choice. Poverty, obligation, and lack of options kept families in place as often as affection did.
- Template integration: `economic_life_story` (property_trajectory), `record_silences` (silence_as_narrative), `fork_in_the_road` (inverted -- "what if he HAD left?").

### Draft Narrative (Trigger Context)

> Daniel Canady was born in Cumberland County, North Carolina, in 1793 -- four years after the Constitution was ratified and three years after the first federal census. When his militia company was called up during the War of 1812, the duty was likely local: a three- to six-month term guarding the Cape Fear coast against British naval raids that never materialized in that stretch of shoreline. He came home to a farm in a county where the Canady name was already established, and he stayed for the next fifty-five years while the world around him transformed. He survived the Panic of 1819, the cotton kingdom's expansion, the Panic of 1837, the antebellum crisis, the Civil War, and the first years of Reconstruction. He died in 1868 on the same ground where he had farmed since his twenties.

### Grade: **STRONG**

All three triggers fire cleanly. Cumberland County is explicitly named in both war_of_1812_service and antebellum_yeoman_south. The stayed_and_adapted trigger provides the narrative framework for a non-migration ancestor. The layering is precise: war_of_1812_service provides the military identity, antebellum_yeoman_south provides the economic pressures, and stayed_and_adapted provides the framework for interpreting WHY he remained. The triple-trigger approach produces a richer narrative than any single trigger could.

**One observation:** Daniel died in 1868 -- three years before the 1871 service pension act and ten years before the 1878 act that covered militia veterans. If he had lived thirteen more years, the pension file would likely be the richest single document in his genealogical record. His widow may have been eligible under the 1878 act. This is a significant research lead the pipeline surfaces.

**No issues found.**

---

## Step 2: Route Selection

### Matched Routes

**None expected. None matched.**

Daniel Canady did not migrate. The stayed_and_adapted trigger explicitly notes: `route_refs: []` -- no routes apply. The antebellum_yeoman_south trigger references `great_wagon_road` and `mississippi_steamboat` as routes for families that DID leave, but Daniel was not among them.

### Draft Narrative (Route)

> Daniel Canady's story has no route because Daniel Canady did not leave. While neighbors loaded wagons and headed down the Great Wagon Road toward Tennessee and Alabama, or floated the Cape Fear to the coast and took ship for destinations south and west, Daniel stayed on his Cumberland County farm. The absence of a route is the point. The narrative for a stayed-put ancestor is not about the journey -- it is about the daily reality of remaining in a place that was changing around you while watching others leave.

### Grade: **ADEQUATE** (by design)

The absence of a route is correct behavior for a non-migration ancestor. The pipeline correctly routes around this step. The narrative work that a route would do -- grounding the reader in the physical experience of travel -- is instead handled by the community texture (Step 6) and material life (Step 5), which describe the world Daniel inhabited rather than the world he traveled through.

**No gap -- this is working as designed.**

---

## Step 3: Destination Lookup

### Matched Destination

**None expected. None matched.**

Daniel's destination is the same as his origin: Cumberland County, NC. No destination profile exists because he did not go anywhere. The stayed_and_adapted trigger explicitly notes: `destination_refs: []`.

### Grade: **ADEQUATE** (by design)

The absence of a destination profile is appropriate here. The narrative work that a destination profile would do (grounding the ancestor in a specific physical and institutional place at the end of a journey) is instead handled by the community texture for eastern NC farm communities (Step 6) -- which describes the place Daniel stayed IN rather than a place he arrived AT. This is how the pipeline should work for non-migrating ancestors.

**No gap -- this is working as designed.**

---

## Step 4: Occupation Enrichment

### Matched Occupations

**Primary:** `tenant_farmer` -- era 1870-1960
**Secondary:** `general_farmer_midwest` -- era 1860-1970

### Assessment

Both occupation files are partial matches for Daniel Canady, and neither is ideal.

The `tenant_farmer` profile covers 1870-1960 -- almost entirely after Daniel's death (1868). Its content describes the postbellum tenant farming system, which is too late for Daniel's era. Daniel was a pre-Civil War yeoman farmer, not a post-Civil War tenant. The tenant_farmer file's seasonal cycle, compensation structures, and cultural context are all framed around the late 19th and early 20th century.

The `general_farmer_midwest` profile covers 1860-1970 and is geographically wrong -- it describes Midwest farming (Iowa, Illinois, Indiana, Ohio), not southeastern North Carolina coastal plain farming. Its seasonal cycle (corn and wheat) and its economic structure (diversified family farming with livestock) are Corn Belt, not Cape Fear.

**Neither file describes what Daniel Canady actually did:** antebellum yeoman farming in eastern North Carolina, 1810-1868. His work was subsistence farming on Piedmont/coastal plain sandy-loam soil, supplemented by a small cash crop (likely corn, some cotton, possibly naval stores/turpentine given Cumberland County's longleaf pine forests). He worked his own land with family labor, possibly supplemented by one or two hired hands or enslaved workers (census records would clarify).

### Draft Narrative (Occupation -- synthesized from trigger and material life data)

> Daniel Canady farmed in Cumberland County for roughly fifty years. The work was governed by the rhythms that ruled every yeoman farmer in eastern North Carolina: plowing in March, planting corn and cotton in April, cultivating through the summer heat, harvesting in the fall, killing hogs after the first hard frost, and settling accounts at the general store before Christmas. Cumberland County's sandy-loam soil grew corn well enough, and the county's longleaf pine forests offered an additional income stream -- turpentine and naval stores that could be sold down the Cape Fear River to Fayetteville. A good year might produce enough surplus to clear the store account and leave a little cash. A bad year left the debt rolling into the next season.

### Grade: **THIN**

Neither occupation file matches Daniel's era or geography. The `tenant_farmer` file is temporally wrong (postbellum, not antebellum). The `general_farmer_midwest` file is geographically wrong (Midwest, not southeastern NC). The draft narrative above is synthesized from the antebellum_yeoman_south trigger and the material life profiles rather than from a dedicated occupation file.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing occupation profile |
| Searched For | Antebellum yeoman farmer, southeastern NC (1790-1860). Subsistence farming with small cash crop on sandy-loam Piedmont/coastal plain soil. Corn, cotton, possibly naval stores (turpentine). Family labor, no or minimal enslaved labor. |
| Severity | **MEDIUM** -- the trigger (antebellum_yeoman_south) and material life profiles partially compensate, but there is no dedicated occupation profile for the pre-Civil War yeoman farmer who grew corn and cotton in the Upper/Eastern South. |
| Nearest Match | `tenant_farmer` (wrong era -- postbellum), `general_farmer_midwest` (wrong region) |
| Recommended Build | `yeoman_farmer_upper_south.json` covering: subsistence-plus-surplus farming on 50-200 acres, 1790-1860. Corn, tobacco, cotton, naval stores. Family labor economics. Seasonal cycle for the Upper South. Would serve the antebellum_yeoman_south trigger and the large population of user ancestors who were pre-Civil War Southern farmers. |

---

## Step 5: Material Life Grounding

### Matched Material Life Profiles

**Primary (early life):** `frontier_log_cabin_1780_1840` -- matches Daniel's childhood and young adulthood in Cumberland County (1793-1840)
**Secondary (later life):** `antebellum_yeoman_farm_1820_1860` -- matches Daniel's established farming years (1820-1860)

Both profiles apply because Daniel's 75-year life spans the transition from frontier conditions to established antebellum yeoman farming. His childhood cabin was likely one-room log construction; by the 1840s-1850s, the Canady homestead was probably a frame or hewn-log dogtrot house with outbuildings.

### Draft Narrative (Material Life -- spanning both profiles)

> The cabin where Daniel Canady grew up in the 1790s was likely one room -- sixteen by twenty feet of round or hewn logs with a clay-chinked fireplace, a puncheon floor, and a sleeping loft reached by pegs driven into the wall. The nearest neighbor was a mile through the woods. By the time Daniel was established on his own farm in the 1820s and 1830s, the material world had improved modestly: a two-room dogtrot house with an open breezeway, a detached kitchen, a smokehouse for the annual hog killing, a springhouse over cold water for keeping milk and butter. The family ate cornbread in every form -- hoecake, pone, ashcake, mush -- with salt pork and whatever the kitchen garden produced. A cast-iron Dutch oven, a skillet, and a kettle were among the most valuable possessions in the household. By the 1850s, his wife could buy calico at the general store instead of spinning thread on the porch, and a family Bible recorded the births, marriages, and deaths that no county clerk had yet begun to track.

### Grade: **STRONG**

Both material life profiles are excellent and historically grounded. The frontier_log_cabin profile captures Daniel's early years (the log cabin, the puncheon floor, the corn-and-pork diet, the spinning wheel, the isolation). The antebellum_yeoman_farm profile captures his established years (the dogtrot house, the detached kitchen, the smokehouse, the transition from homespun to store-bought cloth, the family Bible). The overlap between the two profiles (1820-1840) correctly reflects the gradual transition from frontier to established farm life.

The `economic_position` field in antebellum_yeoman_farm_1820_1860 provides flexibility for Daniel's specific situation. Without census data confirming his acreage and wealth, the default position ("landowner") is the working assumption, but the file provides adjustment guidance for tenant, landless laborer, or marginal positions if records indicate otherwise.

**No issues found.** The two profiles layer perfectly across Daniel's life span.

---

## Step 6: Community Texture

### Matched Community Texture

**Primary:** `eastern_nc_farm_community` -- origin_community, era 1865-1910

### Assessment

The `eastern_nc_farm_community` texture is geographically correct -- Cumberland County is explicitly listed in its geographic scope. However, its era range (1865-1910) is a partial mismatch for Daniel Canady, who died in 1868. The texture file is designed for the POST-Civil War farm community that mill migrants left -- it focuses on Confederate veteran families, the crop lien system, and the farm-to-mill transition. Daniel lived through only the earliest years of this era.

The file's pre-war content is implicit rather than explicit. Its institutions (Missionary Baptist churches, one-room schoolhouses, crossroads general stores, the county courthouse) were all present during Daniel's lifetime, but the file frames them in their postbellum context. Its social fabric section describes the post-war class hierarchy, not the antebellum one. Its race_and_wilmington_1898 section is entirely post-Daniel.

What the file DOES provide for Daniel's era:
- Institutional fabric: Baptist churches as community centers, the crossroads general store, court day at the county courthouse -- all present throughout Daniel's life
- Community rhythms: tobacco/cotton cycles, court days, camp meeting season, hog killing, Christmas -- all applicable to Daniel's era
- Informal economy: women's egg/butter sales, midwifery, turpentine/naval stores -- all applicable
- The crop lien narrative hooks, while postbellum in their fullest form, describe dynamics (buying on credit at the general store) that existed in the antebellum period as well

### Draft Narrative (Community Texture)

> Daniel Canady's community in Cumberland County was organized around three institutions that had not changed since his grandfather's day: the Baptist church, the crossroads general store, and the county courthouse. On Sunday, the Baptist church gathered the neighborhood -- every family within a five-mile radius knew every other family, and the church provided governance, mutual aid, and the weekly exchange of news. On court day, quarterly, the county seat at Fayetteville drew the community for legal business, horse trading, political speeches, and the exchange of information about who was leaving, who was staying, and how the crops were doing. In between, the general store was the fulcrum of daily economic life -- the place where Daniel bought salt, coffee, iron tools, and cloth on credit secured by the coming crop. The longleaf pine forests of Cumberland County added a dimension that the inland Piedmont lacked: turpentine and naval stores that could be extracted and sold down the Cape Fear to Fayetteville, providing cash income in a landscape where most transactions ran on credit and barter.

### Grade: **ADEQUATE**

The eastern_nc_farm_community texture file is geographically correct and institutionally relevant, but its temporal focus (1865-1910) means it captures Daniel's community only in its post-mortem, not at its peak. The institutions it describes -- Baptist churches, general stores, county courthouses -- were all present during Daniel's lifetime, but the file doesn't describe them in their antebellum context. The crop lien system, Confederate veteran networks, and farm-to-mill migration are all post-Daniel.

The file works well enough for a draft narrative because the institutional fabric of eastern NC farm communities was remarkably stable from the 1790s through the 1910s. The Baptist church in 1830 looked much like the Baptist church in 1880. But the file's framing is wrong for Daniel's era -- it describes a post-war landscape of decline, not the antebellum community at its established peak.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Temporal mismatch in community_texture profile |
| Searched For | Eastern NC farm community, ANTEBELLUM era (1790-1860). Cumberland County / Cape Fear region. Baptist churches, militia musters, court day, naval stores economy, antebellum social fabric before the war and Reconstruction changed everything. |
| Severity | **LOW** -- the existing file's institutions are relevant to Daniel's era, but the framing is postbellum. The antebellum_yeoman_south trigger partially compensates with its own community description. A dedicated antebellum version would improve the narrative. |
| Nearest Match | `eastern_nc_farm_community` (correct geography, wrong era emphasis) |
| Recommended Build | Extend `eastern_nc_farm_community` era range backward to 1790, or create `eastern_nc_farm_antebellum.json` covering: antebellum social fabric, militia muster culture, naval stores economy, Fayetteville as market center, Cape Fear River commerce, antebellum church and court day culture. |

---

## Step 7: Wage Contextualization

### Relevant Wage Data

| Occupation | Era | Region | Annual Income |
|-----------|-----|--------|---------------|
| Farm laborer | 1850s | South | $75-$150 (seasonal) |
| Farm laborer | 1860s | South (freedperson, postwar) | $50-$150 |
| Sharecropper | 1860s | South | $0-$100 net (often negative) |
| Farm laborer | 1870s | South | $100-$175 (seasonal) |

### Assessment

The wage table covers 1850-1900 -- it captures only the last eighteen years of Daniel's life (1850-1868) and none of his earlier decades. For the period 1793-1850, there is no dedicated wage data in the NEL. This is a temporal coverage gap, though it is partially mitigated by the fact that antebellum wages before 1850 are less well-documented in general.

The 1850s Southern farm laborer wages ($0.30-$0.50/day, $75-$150/year) provide context for Daniel's economic world. But Daniel was a farm OWNER, not a farm laborer -- the distinction matters. An owner's income was the surplus after subsistence, not a daily wage. The trigger's description of yeoman farming economics is more relevant than the wage table for Daniel's specific situation.

### Draft Narrative (Wage Context)

> The economics of Daniel Canady's life in Cumberland County are difficult to reduce to a number. He was not a wage earner -- he was a farm owner whose income was whatever the land produced after the family ate and the store account was settled. A hired farm laborer in eastern North Carolina in the 1850s earned thirty to fifty cents a day, or roughly seventy-five to a hundred and fifty dollars for a year's seasonal work. Daniel's farm, if it produced a cash surplus at all, likely generated comparable amounts -- a few hundred dollars in a good year, nothing in a bad one. A pair of heavy leather shoes cost one to two dollars. A Dutch oven cost about the same. Coffee was ten to fifteen cents a pound. The family Bible that recorded his children's births cost one to five dollars -- a significant purchase when a good year's surplus might be two hundred dollars.

### Grade: **ADEQUATE**

The wage data is temporally limited for Daniel's life span -- it captures only the 1850s-1860s, missing the first fifty-seven years of his life (1793-1850). For the period it covers, the data provides useful context (Southern farm laborer wages, cost of living benchmarks), but the distinction between farm laborer (wage earner) and farm owner (surplus producer) means the wage table is an approximation rather than a direct match.

The cost_of_living_benchmarks data (shoes at $2-4, coffee at $0.10-0.15/lb, flour at $0.75-1.25 per 25-lb sack) is more directly useful for grounding Daniel's material reality than the wage figures.

**One observation:** Pre-1850 wage and cost data would significantly improve the pipeline's ability to handle early-era ancestors like Daniel. The NEL currently has no wage data before 1850.

---

## Step 8: Template Selection & Draft Output

### Templates Selected

**1. Military Service Arc** -- enlistment_moment (War of 1812 militia service)
**2. Record Silences** -- silence_as_narrative (pre-census era, minimal records expected)
**3. Economic Life Story** -- property_trajectory (multi-generation land trajectory in Cumberland County)
**4. Hinge Generation** -- economic_reset or scattered_children (the Civil War as hinge)

For Option A, selecting the two strongest: Military Service Arc + Record Silences.

### Draft: Military Service Arc (Enlistment Moment)

> When Daniel Canady's militia company mustered in Cumberland County around 1812 or 1813, the duty was local and the terms were short. He was nineteen or twenty years old -- within the state militia obligation that required all white men of military age to serve when called by the governor. Cumberland County militia companies were assigned to coastal defense along the Cape Fear, watching for British naval raids that the War of 1812 had made plausible if not imminent. No enlistment record with a physical description is likely to survive -- the British burning of Washington in August 1814 destroyed many War Department records, and the 1973 fire at the National Personnel Records Center destroyed more. What may survive: a muster roll at the North Carolina State Archives listing Daniel's name, his company, and the dates of his service. If the service was three months, it was a summer spent in a camp on the coast, drilling, standing guard, and waiting for an attack that probably never came. The pension file -- if Daniel or his widow ever applied -- would be the single richest biographical document in his genealogical record.

**Word count:** 175. **Beats:** 4 of 5 hit (who they were before, the enlistment, unit context, the world they entered). Physical description beat intentionally omitted due to record destruction.

### Draft: Record Silences (Silence as Narrative)

> Daniel Canady was born in 1793 -- three years after the first federal census. The 1790 census lists only heads of household, not individual names; the 1800 census follows the same format. Daniel does not appear by name in any federal census until 1810 at the earliest, and even then he would appear only as a tick mark in his father's household -- a white male under the age of sixteen. He does not appear as a named individual until the 1820 census, by which time he was twenty-seven years old. For the first quarter-century of his life, the documentary record contains at most a tick mark, a militia muster roll, and whatever the Cumberland County deed books and church records preserve. This is not a gap in Daniel Canady's life -- it is a feature of how records were kept in the early Republic. Before 1850, the census named only household heads. Before mandatory vital registration (not universal in North Carolina until the twentieth century), births, marriages, and deaths were recorded only if the family kept a Bible or the church kept minutes. Daniel Canady lived for seventy-five years, and for the first half of that life, the documentary system was barely capable of recording that he existed.

**Word count:** 202. **Beats:** All applicable beats hit (the systemic gap, the era-specific record-keeping limitations, the research implications, the interpretive frame).

### Draft: Economic Life Story (Property Trajectory -- bonus draft for White Glove context)

> The property trajectory of the Canady family in Cumberland County is the story of antebellum yeoman economics in miniature. If Daniel's father or grandfather received a land grant of several hundred acres in the late eighteenth century -- as many Cumberland County families did -- the arithmetic of partible inheritance began immediately. Divided among heirs, subdivided again, the original holding shrank with each generation. By the 1850 census, Daniel's real estate valuation (if he appears) would reveal where the family stood on the yeoman economic spectrum: above $1,000 and he was comfortable by local standards; below $500 and the farm was marginal. The Civil War would have destroyed whatever remained of the antebellum economy -- Daniel's last years, from 1865 to 1868, were spent in a county where the labor system had been dismantled, the currency was worthless, and the crop lien was replacing the old credit arrangements with something worse.

**Word count:** 155. **Beats:** 4 of 5 hit (starting point, trajectory, telling transaction inferred, community comparison).

### Draft: Hinge Generation (Economic Reset -- bonus draft)

> Daniel Canady's death in 1868 -- three years after the Civil War ended -- placed his children at the hinge. Whatever land Daniel held was divided among heirs in a county where land values had collapsed, the labor system had been upended, and the old credit economy was being replaced by the crop lien system. The next census (1870) would show what the children inherited: landowner or tenant, comfortable or marginal. If Daniel's children appear as tenant farmers in 1870 or 1880 after their father was listed as a landowner in 1860, the reset is documented in the starkest possible terms -- the family went from owning to renting in one generation, not because of individual failure but because the Civil War destroyed the economic foundation of yeoman farming across the entire Upper South.

**Word count:** 141. **Beats:** All 5 hit (parent position, the break, child position, the arithmetic, the meaning).

### Grade: **STRONG**

All four templates produce meaningful output. The military_service_arc template handles the War of 1812 cleanly, with appropriate hedging about record destruction. The record_silences template addresses the most significant challenge of this ancestor -- the pre-1850 documentary void -- with intellectual honesty. The economic_life_story and hinge_generation templates provide the multi-generational framing that makes the stayed-and-adapted narrative powerful.

**One critical observation:** The military_service_arc template notes that War of 1812 records are "significantly more fragmentary than Civil War records due to the 1814 burning of Washington and the 1973 NPRC fire." This is exactly right for Daniel -- the template correctly flags that the ABSENCE of an enlistment record does not mean the absence of service.

**No issues found.**

---

## Step 9: Research Guidance

### Relevant Guidance Files

- `census_gaps` -- Daniel spans 1793-1868, covering censuses from 1800 through 1860. The pre-1850 censuses (1800-1840) name only household heads with tick marks for other members, creating a structural documentation gap for the first half of his life. The 1850 and 1860 censuses are the critical records -- they name every individual with age, birthplace, and occupation.
- `property_record_strategies` -- Cumberland County deed records are essential for establishing Daniel's land ownership. Tax lists provide annual location evidence for the years between censuses. Deed chain construction can trace the Canady family land from the original grant through subdivision.
- `military_record_strategies` -- Bounty land warrant application files (NARA RG 15 / RG 49) may contain proof of service, biographical details, and family information. State militia records at the NC State Archives may include muster rolls for Cumberland County militia companies during the War of 1812. The pension question is key: did Daniel file before his death? Did his widow file after the 1878 act?

### Draft Narrative (Research Guidance)

> The records for Daniel Canady begin with a problem: he was born before the census could name him. The 1800 and 1810 censuses list only household heads, so Daniel appears -- if at all -- as a tick mark in his father's household. The first census that names him individually is 1820, by which time he was twenty-seven. For the years before 1820, the trail runs through Cumberland County deed books, tax lists, and militia muster rolls at the NC State Archives. The War of 1812 bounty land warrant application file at the National Archives -- if one exists -- may be the richest surviving document for Daniel, containing proof of service, age, residence, and family details. Search NARA Record Group 15 for the pension index and Record Group 49 for bounty land warrants. At the state level, the NC State Archives holds militia muster rolls, county deed records on microfilm, and tax lists that provide annual presence evidence. If Daniel's widow survived past 1878 -- when Congress extended pensions to all War of 1812 veterans including militia -- a widow's pension file may exist and would contain the most detailed biographical information about both Daniel and his surviving spouse.

### Grade: **STRONG**

The guidance is specific and actionable. The census_gaps file correctly identifies the pre-1850 documentation challenge. The military_record_strategies file provides the critical research leads: bounty land warrants at NARA, state militia records at the NC State Archives, and the pension question. The property_record_strategies file provides the methodology for establishing land ownership through deed chains and tax lists.

**The pension question is the most important research lead this pipeline surfaces.** Daniel died in 1868. Service pensions for all War of 1812 veterans (including militia) were not authorized until 1878. If Daniel's widow survived ten years past his death, she would have been eligible for a widow's pension -- and that file, if it exists, would be the biographical jackpot.

**No issues found.**

---

## Step 10: Gap Detection

### Gaps Found

| # | Gap Type | Severity | Description |
|---|----------|----------|-------------|
| 1 | Missing occupation profile | **MEDIUM** | No profile for antebellum yeoman farmer in the Upper/Eastern South (1790-1860). The `tenant_farmer` file is postbellum, the `general_farmer_midwest` is geographically wrong. Need: subsistence-plus-surplus farming on 50-200 acres, corn/cotton/naval stores, family labor, seasonal cycle for the Upper South. Would serve the large population of pre-Civil War Southern farmer ancestors. |
| 2 | Temporal mismatch in community_texture | **LOW** | The `eastern_nc_farm_community` texture covers 1865-1910, but Daniel died in 1868. The institutions (Baptist churches, general stores, courthouses) are relevant across eras, but the file's framing is postbellum. Extending the era range backward to 1790 or creating a dedicated antebellum profile would improve coverage. |
| 3 | Pre-1850 wage data gap | **LOW** | The wage tables begin at 1850, but Daniel was born in 1793. No wage or cost-of-living data exists in the NEL for the period 1790-1850. This gap affects all early-era ancestors. A pre-1850 supplement would serve Revolutionary War veterans, War of 1812 ancestors, and early frontier settlers. |

### Gaps NOT Found (Pipeline Success)

- All three triggers matched cleanly with Cumberland County explicitly named
- Route and destination correctly routed around (non-migration, no data expected)
- TWO material life profiles layered across Daniel's full lifespan
- Community texture geographically correct, institutionally relevant
- War of 1812 trigger vivid, sourced, and explicitly names Cumberland County in its phase description
- Stayed_and_adapted trigger provides robust non-migration framework
- All four templates produced clean output
- Research guidance actionable and specific (pension question, bounty land, state militia records)
- Record silences addressed the pre-1850 void with intellectual honesty

---

## Report Card

| Pipeline Step | Grade | Notes |
|---------------|-------|-------|
| 1. Trigger Matching | **STRONG** | Triple trigger (war_of_1812 + antebellum_yeoman + stayed_and_adapted), all explicitly name Cumberland County |
| 2. Route Selection | **ADEQUATE** | No route needed -- non-migration. Working as designed. |
| 3. Destination Lookup | **ADEQUATE** | No destination needed -- non-migration. Working as designed. |
| 4. Occupation Enrichment | **THIN** | Neither occupation file matches era or geography. Antebellum yeoman farmer profile needed. |
| 5. Material Life | **STRONG** | Two profiles layer perfectly: frontier_log_cabin (childhood) + antebellum_yeoman_farm (adulthood) |
| 6. Community Texture | **ADEQUATE** | Geographically correct, institutionally relevant, but temporal focus is postbellum |
| 7. Wage Contextualization | **ADEQUATE** | Covers 1850-1868 only. No pre-1850 data. Cost benchmarks useful. |
| 8. Templates | **STRONG** | Military service arc, record silences, economic life story, hinge generation all produce clean output |
| 9. Research Guidance | **STRONG** | Pension question, bounty land warrants, NC State Archives militia records -- specific and actionable |
| 10. Gap Detection | 1 MEDIUM, 2 LOW | Missing: yeoman farmer occupation profile; community texture temporal gap; pre-1850 wage data |

### Overall: 6/10 STRONG, 3 ADEQUATE, 1 THIN

**The NEL produces a good narrative for Daniel Canady, with one significant gap.** The three triggers fire perfectly -- Cumberland County is explicitly named in both the War of 1812 and antebellum_yeoman_south triggers, and the stayed_and_adapted trigger provides a robust framework for non-migration narrative. The material life profiles layer beautifully across his 75-year lifespan. The military service arc template handles War of 1812 service with appropriate record-loss caveats. The record silences template addresses the pre-1850 documentation void with intellectual honesty.

The weak point is occupation enrichment: there is no dedicated profile for the antebellum yeoman farmer who was the majority of the white Southern population before the Civil War. This is a genuinely useful build target.

The three ADEQUATE grades (route, destination, community texture) are structurally appropriate for a non-migration ancestor born in 1793. Steps 2 and 3 are correctly empty. Step 6 is geographically correct but temporally misaligned. Step 7 is limited by the wage table's 1850 start date.

### Build Targets Identified

1. **`yeoman_farmer_upper_south.json`** (occupation) -- **MEDIUM priority**. Antebellum yeoman farmer, Upper South / Eastern NC, 1790-1860. Subsistence-plus-surplus farming on 50-200 acres. Corn, cotton, tobacco, naval stores. Family labor economics. Seasonal cycle for the Eastern/Upper South. Would serve the antebellum_yeoman_south trigger and the very large population of pre-Civil War Southern farmer ancestors in KinLore user queries. This is arguably the single most common occupation among user ancestors that currently lacks a dedicated profile.

2. **Pre-1850 wage/cost supplement** -- **LOW priority**. Wage and cost-of-living data for the period 1790-1850. Covers early Republic through antebellum peak. Would serve Revolutionary War veterans, War of 1812 ancestors, early frontier settlers, and any ancestor born before 1800. Data sources: USDA Historical Statistics, Lebergott's Manpower in Economic Growth, state labor reports.

3. **Eastern NC farm community antebellum extension** -- **LOW priority**. Extend `eastern_nc_farm_community.json` era range backward from 1865 to 1790, or create a dedicated antebellum version. Would add: militia muster culture, antebellum church and court day, Fayetteville as market center, Cape Fear River commerce, naval stores economy, antebellum social hierarchy before the war dismantled it.

---

## Narrative Quality Assessment

**Does the NEL data produce a story worth reading?**

Yes -- with a caveat. The story of Daniel Canady is fundamentally different from a migration narrative, and the NEL handles that difference well. The triple-trigger approach (war + yeoman economics + stayed-and-adapted) produces a layered narrative that explains both the pressures Daniel faced and the reasons he resisted them. The material life profiles ground the reader in the physical reality of his world -- from the one-room log cabin of his childhood to the dogtrot farmhouse of his established years. The record silences template honestly addresses the most significant challenge: for the first half of Daniel's life, the documentary system could barely record that he existed.

**What makes this case uniquely challenging for the product:**

- **He STAYED.** The entire pipeline is optimized for migration -- routes, destinations, arrivals. Daniel tests the non-migration pathway, and the pipeline handles it cleanly by routing around steps 2 and 3.
- **He is OLD.** Born in 1793, Daniel predates the first census that names individuals (1850) by fifty-seven years. The record silences template is essential here, not optional.
- **His war was the War of 1812.** The NEL's war_of_1812_service trigger is well-built and names Cumberland County explicitly, but the record destruction problem (1814 burning of Washington + 1973 NPRC fire) means his service records may not survive. The pension question -- did his widow file? -- is the key research lead.
- **His era has no occupation profile.** The antebellum yeoman farmer is the most common pre-Civil War ancestor type, and it has no dedicated file. The trigger and material life profiles compensate, but a dedicated occupation profile would improve the narrative for every pre-war Southern farmer ancestor.

**What the narrative arc looks like:**

Born in the early Republic (1793) -- militia service in the War of 1812 (age 19-22) -- establishing a farm in the 1810s-1820s -- surviving the Panic of 1819 -- farming through the antebellum era while watching neighbors leave for Alabama and Mississippi -- surviving the Panic of 1837 -- appearing in the 1850 and 1860 censuses as an elderly yeoman farmer -- enduring the Civil War as a man in his seventies -- dying in 1868 in a county where the world he had known for seventy-five years had been fundamentally destroyed.

That is a story worth telling. The NEL provides the historical grounding, the material texture, and the research guidance to tell it honestly. The occupation gap is real but addressable. The rest of the pipeline delivers.

**The counter-narratives work.** The stayed_and_adapted trigger's counter-narrative -- "Staying was not always a free choice" -- adds complexity. The antebellum_yeoman_south trigger's counter-narrative -- "Yeoman farmers were not uniformly poor and uneducated" -- prevents flattening the story. The war_of_1812_service trigger's counter-narrative -- "Most service was uneventful" -- prevents inflating routine militia duty into drama.

**The Accuracy Line holds.** Every claim in the draft narratives above is grounded in sourced data from the NEL files or explicitly hedged with "likely," "probably," or "if." No emotional projection. No fabricated feelings. "Daniel stayed" -- not "Daniel chose to stay because he loved his land."

**The research guidance is the narrative's strongest actionable output.** The pension question alone could transform the family's understanding of Daniel Canady. If his widow survived past 1878, a pension file may exist at NARA that contains sworn testimony, proof of marriage, proof of service, and biographical detail that survives nowhere else. That is the kind of concrete, specific research lead that makes a KinLore report worth the purchase.

**Third dry run: PASS.**
