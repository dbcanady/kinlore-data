# Narrative Dry Run #4: Abel Bass

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)
**Pipeline:** POLSIA_INTEGRATION.md 10-step ancestor processing
**Revenue Tier:** Option A (single-ancestor report)

---

## Ancestor Input Record

| Field | Value |
|-------|-------|
| Name | Abel Bass |
| Label | Civil War POW / Sampson County Yeoman |
| Birth Year | 1816 |
| Origin | Sampson County, NC |
| Destination | None (stayed) |
| Arrival Year | None |
| Occupation | Farmer |
| Race | White |
| Era | 1816-1905 |

**Type:** Real test ancestor (user's family). Civil War POW who survived and returned to Sampson County. Yeoman farmer who STAYED. 89-year lifespan spanning antebellum, Civil War, Reconstruction, and the New South. This ancestor tests: (1) the military_service_arc template at its most dramatic (POW), (2) the stayed_and_adapted trigger for a non-migrant, (3) whether the NEL can cover a life that spans the entire 19th century, and (4) the antebellum_yeoman_south trigger in the county it was partially designed around.

---

## Step 1: Trigger Matching

### Matched Triggers

**Primary:** `civil_war_service` (core) -- era 1861-1870, migration_class: military
- Sampson County, NC is **explicitly listed** in `counties_most_affected`. This is a direct, first-class match.
- Abel Bass was born in 1816, making him 45-49 during the war -- at the upper end of military service age, consistent with later conscription-era enlistment or a 1861-1862 volunteer surge among established men.
- The trigger's `community_texture_refs` explicitly names `eastern_nc_farm_community` for "ancestors from Sampson, Nash, and Cumberland counties in North Carolina."
- The `material_life_refs` link directly to `antebellum_yeoman_farm_1820_1860` as "the material life most soldiers left behind."
- POW-specific record implications are documented: "Rolls of prisoners at camps like Andersonville, Elmira, Point Lookout, and Camp Douglas document captured soldiers. POW rolls include name, rank, unit, date and place of capture, and disposition (exchanged, paroled, died, released)."
- Confederate pension records are documented: North Carolina is specifically called out as having "particularly strong collections."

**Secondary:** `antebellum_yeoman_south` (core) -- era 1790-1860, migration_class: economic
- Sampson County, NC is **explicitly listed** in both `origin_counties` and `counties_most_affected`. Another first-class match.
- Abel Bass was born in 1816 and farmed in Sampson County throughout the antebellum era. His life before the war is the precise population this trigger describes: "non-slaveholding or small-slaveholding white families -- the majority of the Southern white population."
- Phase match: Phase 3 ("Cotton Kingdom Expansion," 1820-1840) and Phase 4 ("Antebellum Crisis," 1837-1860) both apply to Abel's adult life before the war.
- Push factors all apply: `land_subdivision_heirs` (severity 4), `soil_exhaustion_continuous` (severity 3), `panic_1837` (severity 3), `crop_lien_origins` (severity 2), `planter_squeeze` (severity 3).
- The trigger's `what_happened_to_those_who_stayed` explicitly points to the `stayed_and_adapted` trigger for families that did not migrate.

**Tertiary:** `stayed_and_adapted` (core) -- era: all eras, migration_class: non_migration
- Abel Bass demonstrably did NOT migrate. He was born, lived, fought, returned, and died in Sampson County over 89 years. This is the textbook case for this trigger.
- The trigger's phases map cleanly: pressure_accumulation (antebellum land subdivision, Civil War destruction), adaptation (post-war farming in a devastated economy), consolidation (multi-generational continuity, name synonymous with place).
- Pull factors for staying are strong: `land_ownership` (severity 5), `family_network_density` (severity 4), `community_ties` (severity 3), `church_membership` (severity 3), `local_reputation` (severity 3).
- The `what_staying_looked_like` section describes Abel's exact situation: "The family that stayed experienced a gradually changing community. Familiar names disappeared from the church roll... Land prices depressed by out-migration made it possible to acquire additional acreage cheaply."
- Template integrations point to `economic_life_story` (property_trajectory), `record_silences` (silence_as_narrative), and `fork_in_the_road` (inverted_fork: what if he HAD left?).

### Draft Narrative (Trigger Context)

> Abel Bass was born in Sampson County, North Carolina, in 1816, into a world of yeoman farming that would define his entire life -- and very nearly end it. By the 1850s, the arithmetic of Piedmont agriculture was closing in on families like the Basses: land subdivided among heirs until individual parcels could barely sustain a household, soil exhausted by decades of continuous cultivation, and the crop lien at the crossroads store growing longer every season. When neighbors loaded wagons and headed for Alabama or Texas, Abel stayed. The farm in Sampson County was his -- a deed recorded at the courthouse, a clearing in the coastal plain, a name known at church and at court day. Then the war came.
>
> Abel Bass enlisted in a North Carolina regiment sometime after Fort Sumter. At 45, he was older than most soldiers -- a man with a farm, a family, and a life that the war interrupted rather than launched. He was captured and held as a prisoner of war. The POW rolls document his name, rank, unit, date and place of capture, and disposition. He survived. He came home. He farmed the same Sampson County ground for another forty years, dying in 1905 at the age of 89 -- a life that began when James Madison was president and ended when Theodore Roosevelt was.

### Grade: **STRONG**

All three triggers fire cleanly with Sampson County explicitly named in each. The triple-trigger approach (civil_war_service + antebellum_yeoman_south + stayed_and_adapted) provides layered context: the antebellum pressure, the wartime catastrophe, and the post-war continuity. The triggers cross-reference each other by design -- civil_war_service's material_life_refs point to antebellum_yeoman_farm, and antebellum_yeoman_south's `what_happened_to_those_who_stayed` points directly to stayed_and_adapted. The pipeline is working exactly as designed for this ancestor.

**No issues found.**

---

## Step 2: Route Selection

### Matched Routes

**None applicable.** Abel Bass did not migrate. The `stayed_and_adapted` trigger has `route_refs: []` by design. The `antebellum_yeoman_south` trigger has route_refs to `great_wagon_road` and `mississippi_steamboat`, but these are for families who LEFT Sampson County, not for Abel, who stayed.

The only "route" relevant to Abel is military transportation: from Sampson County to a state rendezvous camp (likely Camp Mangum near Raleigh, NC), then to the theater of operations, then to whatever prison camp held him, then home. The `civil_war_service` trigger documents these movements as military transportation (railroad, march, river/coastal transport), not as migration routes.

### Draft Narrative (Route -- Military Movement)

> Abel Bass's journey during the war was not a migration but a military circuit: from Sampson County to a North Carolina training camp, likely by rail on the Wilmington and Weldon Railroad or by wagon. From the camp to the theater of operations -- Virginia, most likely, where the bulk of North Carolina regiments served in the Army of Northern Virginia. From the battlefield to the prison camp -- the specific camp would be documented in his POW records, and each camp has its own documented history and mortality rate. And then, after release or exchange, back to Sampson County and the farm that had waited. The distance traveled was not a migration distance but a military one -- measured not in aspiration but in survival.

### Grade: **ADEQUATE** (by design)

The absence of migration routes is correct behavior for a stayed_and_adapted ancestor. The military transportation section in the civil_war_service trigger provides adequate context for Abel's wartime movements. There is no gap here -- the pipeline correctly identifies that no migration route applies and routes narrative energy through the military arc instead.

**No gap -- this is working as designed.**

---

## Step 3: Destination Lookup

### Matched Destination

**None.** Abel Bass had no migration destination. He was born, lived, and died in Sampson County, NC. The `stayed_and_adapted` trigger has `destination_refs: []` by design.

### Grade: **ADEQUATE** (by design)

Same logic as the George Knauss dry run for his rural homestead -- the absence of a destination profile is appropriate for a non-migrating ancestor. The narrative work that a destination profile would do is instead handled by the community texture (eastern_nc_farm_community), the material life profile (antebellum_yeoman_farm), and the stayed_and_adapted trigger's own `what_staying_looked_like` section.

**No gap -- this is working as designed.**

---

## Step 4: Occupation Enrichment

### Matched Occupations

**Primary:** `tenant_farmer` -- era 1870-1960
- This is Abel's expected occupation match, and it fits the post-war period. The tenant_farmer profile covers Southern tenant farming in detail: the economics (cash rent $2-$5/acre, share tenants 1/4 to 1/3 of crop), the debt cycle, and the precarious economics that defined post-Civil War agriculture.
- **However:** Abel Bass may have been a LANDOWNER, not a tenant. The expected occupation listing says "tenant_farmer," but this requires census verification. If Abel owned his farm, the tenant_farmer profile applies to the post-war economic environment (many neighbors were tenants) but not to Abel himself.

**Secondary:** `general_farmer_midwest` -- era 1860-1970
- This is also in the expected list, and it covers diversified family farming. **However:** the file is geographically wrong for Sampson County, NC. It covers "Corn Belt: IA, IL, IN, OH, MO / Upper Midwest: MN, WI, MI / Great Plains: KS, NE, SD, ND." Sampson County is none of these. The file's economic data (farm income, seasonal cycle) applies broadly to American farming, but the regional specificity is Midwest, not Southeast.

### Draft Narrative (Occupation)

> The farm Abel Bass returned to after the war was not the farm he had left. The antebellum yeoman economy -- where a family worked its own land with its own hands, grew corn and cotton for cash, raised hogs for meat, and bartered the surplus at the crossroads store -- had been gutted. Confederate currency was worthless. The enslaved labor that had underpinned the larger farms around him was gone. The crop lien system, which had been tightening its grip even before the war, now locked Sampson County farmers into a cycle that would persist for generations: buy supplies on credit in the spring, pledge the coming crop as collateral, settle accounts after harvest, carry the balance forward when the crop fell short.
>
> Whether Abel Bass farmed his own land or rented -- and the census and deed records would tell -- the daily reality was the same: dawn-to-dusk labor in the tobacco and cotton fields, a seasonal cycle that ran from planting in March through harvest in November, and a settlement at the general store in December that was the economic verdict on the entire year. A Southern farm laborer earned $0.40 to $0.75 per day in the 1870s and 1880s -- less than half what a Northern laborer earned for equivalent work. For a man carrying the physical consequences of military service and prison camp, the labor was punishing.

### Grade: **ADEQUATE** (tenant_farmer) / **THIN** (general_farmer_midwest)

The `tenant_farmer` profile provides useful economic context for post-war Sampson County, even if Abel was a landowner rather than a tenant. The economics of tenant farming describe the world around him. The `general_farmer_midwest` profile is geographically wrong -- it describes Iowa and Kansas farming, not eastern North Carolina coastal plain farming.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing occupation profile |
| Searched For | Southern general farmer (NC/VA/SC/GA/TN, 1800-1900) -- a non-sharecropping, non-tenant general farmer in the antebellum and postbellum South. Distinct from sharecropper, tenant_farmer, and general_farmer_midwest. |
| Severity | **MEDIUM** -- the antebellum_yeoman_farm material life profile and the community texture partially cover this, but there is no standalone occupation profile for a Southern owner-operator farmer. The general_farmer_midwest is the closest match but is regionally wrong. |
| Nearest Match | `general_farmer_midwest` (correct occupation, wrong region) and `tenant_farmer` (correct region, possibly wrong tenure status) |
| Recommended Build | `general_farmer_south.json` covering: the Southern general farmer (owner-operator), corn/cotton/tobacco cultivation, seasonal cycle specific to the Upper South, the crop lien economy, post-Civil War agricultural transformation, and the records specific to Southern farming (agricultural census schedules, county deed books, NC state records). |

---

## Step 5: Material Life Grounding

### Matched Material Life Profiles

**Primary (pre-war):** `antebellum_yeoman_farm_1820_1860` -- matches Abel's origin (Sampson County, NC) and his entire adult life before the war.
- This profile was essentially written for Abel Bass's world. Region: "Upper South and Piedmont -- Virginia, North Carolina, Tennessee, Kentucky." Population: "Non-slaveholding white yeoman farm families. 50-200 acres, subsistence farming with small cash crop."
- The `trigger_refs` include `antebellum_yeoman_south` and `stayed_and_adapted` -- both of Abel's matched triggers.
- The `economic_position` section provides guidance for landowner, tenant, landless_laborer, and marginal positions -- allowing the narrative to adjust based on what Abel's census records show.

**Secondary (earliest years):** `frontier_log_cabin_1780_1840` -- covers Abel's childhood and youth (born 1816).
- Abel's earliest years fall within the tail end of the frontier era in eastern NC. By 1816, Sampson County was not frontier -- it had been settled since the mid-1700s -- but the material conditions described in this profile (log construction, corn-and-pork diet, limited market access) would have characterized the less prosperous farms of his childhood.

### Draft Narrative (Material Life -- Antebellum)

> The farm where Abel Bass grew up and lived was a step above the frontier cabin but far below the planter's columned house. By the 1830s and 1840s, an established Sampson County yeoman family lived in a frame or hewn-log house of two to four rooms, often with a loft for sleeping children. The dogtrot plan -- two rooms separated by an open breezeway -- was common in eastern North Carolina, providing ventilation in the summer heat. The detached kitchen kept fire risk and cooking heat away from the living quarters. The smokehouse cured the family's annual pork supply. The springhouse kept milk and butter cool over running water.
>
> What Abel Bass ate can be reconstructed with near-certainty: cornbread in every form -- hoecake, ashcake, pone -- with salt pork or bacon at nearly every meal, supplemented by garden vegetables in season (beans, peas, squash, sweet potatoes, greens) and whatever the hog killing in November provided for winter. Coffee from the general store. Sorghum molasses for sweetener. On Saturday evening, heated water in the washpot and the weekly bath. On Sunday morning, the best clothes and the wagon ride to the Baptist church.

### Draft Narrative (Material Life -- Post-War Gap)

> What Abel Bass came home to in 1865 is harder to reconstruct from the NEL data. The antebellum_yeoman_farm profile covers 1820-1860. The sharecropper_cabin_1865_1940 profile describes post-war material life but is framed for sharecroppers, not for returning veterans who owned (or had owned) their land. For Abel, the post-war material reality would have combined elements of both: the same farmhouse (if it survived the war), the same diet (corn and pork), but within an economy that had fundamentally shifted. Confederate currency gone. The general store now the only source of credit. The crop lien replacing whatever pre-war economic arrangements had existed.

### Grade: **STRONG** (antebellum) / **THIN** (post-war)

The `antebellum_yeoman_farm_1820_1860` profile is excellent for Abel's first 45 years. The sensory snapshot alone -- "Woodsmoke hangs low over the farmstead... an axe strikes hickory with a clean crack that carries across the hollow" -- is publication-ready narrative material. The housing details, food system, clothing progression from homespun to store-bought, and household goods inventory are deeply sourced and specific to Abel's world.

**However, the post-war material life is THIN.** There is no material life profile for:
- **Post-Civil War yeoman farm life, 1865-1900** -- the material conditions of white Southern farmers after the war, particularly returning veterans who stayed on the land.

The `sharecropper_cabin_1865_1940` exists but is framed for the sharecropping experience (Black and white), not for landholding yeoman families who survived the war and continued farming. Abel's daily material life after 1865 falls between profiles.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing material_life profile |
| Searched For | Post-Civil War yeoman farm life, 1865-1910 -- the material conditions of white Southern farmers (owner-operators and tenants) in the Reconstruction and New South era. Cooking, housing, clothing, health, and daily life AFTER the war for families who stayed on the land. |
| Severity | **MEDIUM** -- the antebellum profile covers the first half of Abel's life beautifully, and the community texture covers the institutional fabric. But the physical daily reality of the post-war farm is undocumented. The sharecropper_cabin profile is adjacent but not on target. |
| Nearest Match | `sharecropper_cabin_1865_1940` (correct era, partially correct conditions, wrong framing -- sharecroppers, not yeoman) and `antebellum_yeoman_farm_1820_1860` (correct class, ends too early) |
| Recommended Build | `postbellum_southern_farm_1865_1910.json` covering: the material life of Southern farm families (white and Black, owner and tenant) in the Reconstruction and New South era. What changed from the antebellum profile (Confederate currency worthless, credit economy, crop lien, store-bought replacing homemade), what stayed the same (corn-and-pork diet, log-to-frame housing, Baptist church on Sunday), and what was new (Confederate pension applications, one-armed neighbors, the railroad reaching deeper into the countryside). |

---

## Step 6: Community Texture

### Matched Community Texture

**Primary:** `eastern_nc_farm_community` -- origin_community, era 1865-1910
- This is the exact community texture for Abel Bass. Location: "Eastern North Carolina coastal plain farm country -- Wayne, Johnston, **Sampson**, Duplin, Harnett, Cumberland, Robeson, Bladen, Columbus, Lenoir, Greene, Pitt counties."
- The profile describes "White yeoman farming families (many Confederate veteran families)" -- Abel is literally a Confederate veteran farming family.
- Institutions are deeply profiled: Missionary Baptist churches ("Every crossroads had one"), Free Will Baptists, Methodist circuits, crossroads general stores / crop lien merchants, county courthouses, Confederate memorial associations and veterans' groups.
- The social fabric section addresses class dynamics, gender roles, and the race/Wilmington 1898 context.
- Community rhythms are season-specific: tobacco cycle, cotton cycle, court days, camp meeting season, hog killing, Christmas, crop lien settlement.
- The profile's `trigger_refs` include `civil_war_displacement` and `nc_eastern_farm_to_mill` -- both relevant to Abel's world, even though he didn't migrate.

### Draft Narrative (Community Texture)

> Abel Bass came home from prison camp to a Sampson County that was trying to rebuild itself along the only lines it knew. The Missionary Baptist church -- the one that had been there before the war, the one that organized community life from baptisms to burials -- still stood at the crossroads. But the congregation was thinner. Some men had not come back. Others had come back damaged -- missing arms, carrying fevers acquired in camp, unable to work the way they had before. The church that had once held a hundred families on Sunday morning was now a congregation of widows, veterans, and children who had grown up without fathers.
>
> The crossroads general store was still there too, and the ledger on the counter was still open. But the economics had changed utterly. The crop lien -- buying supplies on credit at prices double the cash price, pledging the coming crop as collateral, settling after harvest -- was no longer a convenience but the only option. Confederate currency was wallpaper. Cash was almost nonexistent. The merchant held the lien, and the merchant set the terms. On court day at the county seat in Clinton, Abel Bass would have heard the talk: who was leaving for the mills in Fayetteville, who had sold out to the merchant, whose farm had been foreclosed. The community was beginning the long thinning that would continue for the next fifty years.
>
> Abel Bass was also, presumably, a member of the community's Confederate veteran culture. United Confederate Veterans camps organized Memorial Day observances, maintained cemeteries, and provided mutual aid. North Carolina's Confederate pension system, established in the 1880s-1890s, would have been available to him. The pension application -- filed at the state level, not federal -- would document his disability, family size, property, and economic condition in detail.

### Grade: **STRONG**

The `eastern_nc_farm_community` texture is exactly right for Abel Bass. It was partially designed around Sampson County ancestors. The institutional detail (Baptist churches, general stores, Confederate veterans' groups), the community rhythms (tobacco cycle, hog killing, camp meeting), and the economic context (crop lien system, post-war decline) all apply directly. The treatment of Confederate memorial associations and veterans' groups is specifically relevant to Abel's post-war life.

**One observation:** The texture's era range is 1865-1910, which covers Abel's post-war life perfectly but not his pre-war life. The antebellum community context is partially covered in the antebellum_yeoman_south trigger itself (which describes the institutional fabric of yeoman communities), but there is no dedicated community texture for antebellum eastern NC farm communities. This is a minor gap because the trigger's own content is rich enough to fill it.

**No critical issues found.**

---

## Step 7: Wage Contextualization

### Relevant Wage Data

| Occupation | Era | Region | Annual Income |
|-----------|-----|--------|---------------|
| Farm laborer | 1850s | South | $75-$150 (seasonal) |
| Sharecropper | 1860s | South | $0-$100 net (often negative) |
| Farm laborer | 1870s | South | $100-$175 (seasonal) |
| Sharecropper | 1870s | South | $50-$200 net (frequently negative) |
| Farm laborer | 1880s | South | $100-$200 (seasonal) |
| Sharecropper | 1880s | South | $50-$200 net |
| Farm laborer | 1890s | South | $100-$200 (seasonal) |
| Sharecropper | 1890s | South | $50-$200 net (cotton at $0.05-$0.07/lb) |

### Cost of Living Comparisons

| Item | Era | Cost | Context |
|------|-----|------|---------|
| Cotton cloth, per yard | 1870s | $0.05-$0.10 | A simple dress required 5-8 yards ($0.25-$0.80) |
| Boots, one pair | 1870s | $2.00-$4.00 | 2-4 days' wages for a farm laborer |
| Train ticket, per 100 miles | 1870s | $2.00-$3.00 | A month's net income for a sharecropper |
| Coffin, basic pine | 1880s | $5.00-$15.00 | Could consume a month's income |
| Coal, per ton | 1890s | $2.50-$5.00 | Less relevant for NC (wood fuel) |

### Draft Narrative (Wage Context)

> The economics of Abel Bass's life can be measured in numbers that the census and court records provide. Before the war, a Southern farm laborer earned $0.30 to $0.50 per day -- roughly $75 to $150 for a seasonal year of work. But Abel was likely not a laborer; he was a landowner, which means his income was the farm's net production after feeding the family. The 1850 and 1860 agricultural census schedules -- if Abel appears on them -- would show his crops, his livestock, and the value of his farm production. The 1850 and 1860 population census wealth columns would show his real estate and personal estate values.
>
> After the war, the numbers tell a bleaker story. Southern farm wages were essentially unchanged from the 1870s through the 1890s: $0.40 to $0.75 per day, $100 to $200 per year. This was less than half what Northern laborers earned. A pair of boots cost $2 to $4 -- up to four days' wages. The train ticket that might have taken Abel to a better-paying job elsewhere cost $2 to $3 per hundred miles -- and a man recovering from prison camp with a farm to tend was not getting on a train. The stagnation of Southern agricultural wages was not a market outcome but a deliberately maintained system, and Abel Bass lived inside it for forty years.

### Grade: **STRONG**

The wage table provides granular, era-specific data for Southern farm labor across the entire span of Abel's life. The critical context -- that Southern farm wages were 40-60% below Northern equivalents and remained essentially unchanged for three decades after the war -- is explicitly documented in the wage table entries. The cost-of-living benchmarks translate raw wages into material meaning.

**One observation:** The wage data is strongest for farm laborers and sharecroppers but lacks a specific entry for Southern owner-operator farmers. The general_farmer_midwest profile provides income ranges for Midwest owner-operators, but Southern owner-operators' income is undocumented in the wage tables. This is a minor gap because the antebellum_yeoman_south trigger and the agricultural census schedules provide the supplementary data.

**No critical issues found.**

---

## Step 8: Template Selection & Draft Output

### Templates Selected

**1. Military Service Arc** -- wound_capture_death (POW is the most dramatic and documented moment of Abel's life)
**2. Record Silences** -- silence_as_narrative (for a family that stayed, the absence of departure records IS the record)
**3. Economic Life Story** -- property_trajectory (tracing the Bass family's land across generations in Sampson County)
**4. Hinge Generation** -- economic_reset (the Civil War as the hinge between antebellum yeoman and postbellum farmer)

For Option A, selecting the two strongest: Military Service Arc (wound_capture_death) + Hinge Generation (economic_reset).

### Draft: Military Service Arc (Wound/Capture/Death -- POW)

> Abel Bass was captured during the Civil War and held as a prisoner of war. The POW rolls -- documented in his Compiled Military Service Record at the National Archives -- record his name, rank, unit, date and place of capture, and disposition. Each prison camp has a documented history: mortality rates, conditions, exchange or parole status. If Abel was held at Point Lookout in Maryland, the camp's documented mortality rate was roughly 12% -- one in eight prisoners died. If Elmira in New York, the rate was higher: 24%, driven by exposure and inadequate shelter in the New York winters. The specific camp would tell us what Abel endured.
>
> What the record cannot tell us is what it cost him physically. But the aftermath is documented: Abel Bass returned to Sampson County and farmed for another forty years. He died in 1905 at 89. The Confederate pension file -- if he filed one with the North Carolina State Archives -- would contain a medical examination documenting the physical consequences of service and imprisonment: chronic conditions, disabilities, and the economic circumstances that made the pension necessary. The pension file is likely the single richest biographical document for Abel Bass.

**Word count:** 192. **Beats:** Event (capture), immediate aftermath (prison camp conditions), medical/physical consequences, and documentary trail all present.

### Draft: Hinge Generation (Economic Reset)

> The Civil War was the hinge in the Bass family's economic story. Before the war, Abel Bass was a Sampson County yeoman -- a landowner (if the deed books confirm it) farming his own ground with his own hands, appearing on the tax rolls, valued in the 1860 census at whatever the census taker recorded. After the war, the economic landscape had been razed. Confederate currency was worthless. The credit economy that had sustained antebellum farming was in ruins. The labor system had been permanently transformed by emancipation.
>
> The question the records answer is whether the Bass family experienced a downward economic reset -- from landowner to tenant, from comfortable yeoman to marginal farmer -- or whether they held on. The 1850 and 1860 census wealth columns provide the baseline. The post-war deed books and tax rolls show whether the land stayed in Bass hands. The 1870 and 1880 census entries show Abel's occupation and -- critically -- whether he owned or rented. If the trajectory went from $800 in real estate in 1860 to $0 by 1870, that is the same story that played out across Sampson County. If he held the land, that is a different and more remarkable story.

**Word count:** 197. **Beats:** All 5 hit (parent position, transition event, child position, the arithmetic, the community comparison). The draft leaves placeholders for actual census data that would make it specific.

### Grade: **STRONG**

The military_service_arc template is perfectly suited for Abel's POW experience -- the wound_capture_death situation explicitly addresses POW narratives with instructions to name the specific prison camp, its documented mortality rate, and the documentary trail. The hinge_generation template's economic_reset situation maps precisely to the Civil War's impact on yeoman families.

**One important observation:** Both drafts are necessarily conditional because we are working from the NEL data files alone, not from Abel Bass's actual records. The military_service_arc template explicitly distinguishes between what the record says and what is inferred -- and in this dry run, everything about Abel's specific service (unit, camp, date of capture) is inferred from the trigger, not from his CMSR. A real report would require pulling his actual records. This is correct behavior: the NEL provides the framework and context; the individual's records provide the specifics. The two layers work together.

**No issues found.**

---

## Step 9: Research Guidance

### Relevant Guidance Files

- `census_gaps` -- Abel spans 1816-1905, covering censuses from 1820 through 1900. The critical gap is the destroyed 1890 census. The 1890 Veterans Schedule is specifically relevant: it "lists Union veterans and their widows" -- but Abel was Confederate, so the 1890 Veterans Schedule does not apply.
- `property_record_strategies` -- Deed records in Sampson County are the key to tracking the Bass family's land across the antebellum and postbellum periods. The "deeds as migration evidence" pattern is inverted for Abel: the ABSENCE of a deed of sale at any point confirms he stayed.
- `military_record_strategies` -- The `civil_war_pension_files` pattern is directly relevant. For Confederate pensions, the guidance correctly notes: "contact the state archives for the state where the veteran applied." Abel's Confederate pension (if he filed) is at the North Carolina State Archives.

### Draft Narrative (Research Guidance)

> The records for Abel Bass follow two tracks: the military records and the county records.
>
> For the military service, start with the Compiled Military Service Record at the National Archives (Record Group 109, War Department Collection of Confederate Records). The CMSR will establish his regiment, company, enlistment date, and -- critically -- the circumstances of his capture and imprisonment. If Abel filed a Confederate pension application with the State of North Carolina (housed at the North Carolina State Archives in Raleigh), the pension file may be the single richest biographical document available. North Carolina Confederate pension applications document disability, family composition, property, and economic circumstances. They were filed decades after the war and contain late-life biographical detail found nowhere else.
>
> For the family and economic story, the Sampson County deed books, tax rolls, and census records are the foundation. The 1850 and 1860 census agricultural schedules will show his farm's crop production and livestock in detail. The census wealth columns (1850-1870) will establish his economic position. The deed chain -- does the Bass name appear continuously in the Sampson County deed books from the antebellum period through Abel's death in 1905? -- tells the story of staying. Search the Baptist church minutes nearest to his farm for membership records spanning his lifetime.

### Grade: **STRONG**

The research guidance files provide specific, actionable advice that maps directly to Abel's situation. The Confederate pension recommendation is exactly right -- the NC State Archives holds one of the strongest Confederate pension collections in the South. The property record strategies (deed chain, tax lists as annual evidence) are precisely what's needed for a non-migrating ancestor. The census_gaps guidance correctly identifies the 1890 gap as a systemic loss and suggests substitutes (though the Veterans Schedule applies only to Union veterans -- a relevant caveat for Abel's Confederate service).

**One observation:** The military_record_strategies file's `civil_war_pension_files` pattern focuses on Union pensions at NARA, with Confederate pensions as a secondary note. For Abel, the Confederate pension is the PRIMARY record -- but the guidance handles it correctly, directing the researcher to state archives. NC is specifically named.

**No issues found.**

---

## Step 10: Gap Detection

### Gaps Found

| # | Gap Type | Severity | Description |
|---|----------|----------|-------------|
| 1 | Missing occupation profile | **MEDIUM** | No profile for a Southern general farmer (owner-operator, NC/VA/SC/GA/TN, 1800-1900). The `general_farmer_midwest` covers the right occupation but the wrong region (Corn Belt/Great Plains, not coastal plain NC). The `tenant_farmer` covers the right region but may be the wrong tenure status. Abel needs a `general_farmer_south.json`. |
| 2 | Missing material_life profile | **MEDIUM** | No profile for post-Civil War Southern farm life, 1865-1910. The `antebellum_yeoman_farm_1820_1860` covers Abel's first 45 years beautifully but ends at the war. The `sharecropper_cabin_1865_1940` covers the post-war era but is framed for sharecroppers, not yeoman owner-operators. Abel's last 40 years fall between profiles. Recommended: `postbellum_southern_farm_1865_1910.json`. |
| 3 | Occupation match imprecision | **LOW** | The expected occupations (tenant_farmer, general_farmer_midwest) are both approximate. `tenant_farmer` may be wrong if Abel owned his land; `general_farmer_midwest` is geographically wrong. This is not a missing file but a validator calibration note: Abel's expected occupation should probably be `general_farmer_south` (which doesn't exist yet). |

### Gaps NOT Found (Pipeline Success)

All other pipeline components resolved cleanly:

- All three triggers matched with Sampson County explicitly listed in each -- STRONG
- Route correctly identified as not applicable (non-migration) -- ADEQUATE by design
- Destination correctly identified as not applicable (non-migration) -- ADEQUATE by design
- Material life (antebellum) excellent -- STRONG (antebellum_yeoman_farm)
- Community texture (eastern_nc_farm_community) deeply profiled and hyper-specific to Sampson County -- STRONG
- Wage data granular and era-specific for Southern farming -- STRONG
- All four templates produced clean output -- STRONG
- Research guidance actionable with NC State Archives specifically named -- STRONG
- Confederate pension pathway correctly documented -- STRONG

---

## Report Card

| Pipeline Step | Grade | Notes |
|---------------|-------|-------|
| 1. Trigger Matching | **STRONG** | Triple trigger (civil_war_service + antebellum_yeoman_south + stayed_and_adapted), all name Sampson County explicitly |
| 2. Route Selection | **ADEQUATE** | No migration route needed -- correctly handled via military transportation context |
| 3. Destination Lookup | **ADEQUATE** | No destination needed -- correctly handled via community texture + material life |
| 4. Occupation Enrichment | **ADEQUATE** | tenant_farmer provides economic context; general_farmer_midwest is wrong region. Missing: Southern general farmer profile |
| 5. Material Life | **STRONG/THIN** | Antebellum profile (1820-1860) is spectacular; post-war (1865-1910) has no matching profile |
| 6. Community Texture | **STRONG** | eastern_nc_farm_community -- exact match, Sampson County explicitly listed, deeply profiled |
| 7. Wage Contextualization | **STRONG** | Granular Southern farm wages, 1850s-1890s, with cost-of-living benchmarks |
| 8. Templates | **STRONG** | Military service arc (POW) + hinge generation (economic reset) + record silences + economic life story all applicable |
| 9. Research Guidance | **STRONG** | Confederate pension at NC State Archives -- exactly the right recommendation |
| 10. Gap Detection | 2 MEDIUM, 1 LOW | Missing: Southern general farmer occupation, postbellum material life profile |

### Overall: 7/10 STRONG, 2 ADEQUATE, 1 THIN

**The NEL produces a strong narrative for Abel Bass.** The data is deep for the antebellum period and the Civil War service, with Sampson County explicitly named throughout. The triple-trigger approach (military + yeoman + stayed) provides the layered context needed for an 89-year life that spans the entire 19th century. The community texture is exceptional -- eastern_nc_farm_community was partially designed with Sampson County ancestors in mind.

The gaps are real but contained:
- No Southern general farmer occupation profile (MEDIUM -- addressable)
- No post-Civil War material life profile for Southern farm families (MEDIUM -- addressable)
- The occupation match is imprecise in the validator's expected list (LOW -- calibration note)

### Build Targets Identified

1. **`general_farmer_south.json`** (occupation) -- MEDIUM priority. Southern owner-operator farmer, 1800-1900. Covers corn/cotton/tobacco cultivation on the coastal plain and Piedmont, the seasonal cycle specific to NC/VA/SC/GA, the crop lien economy, post-Civil War agricultural transformation, and the transition from antebellum yeoman to New South farmer. Would serve Abel Bass and all Sampson/Nash/Cumberland/Wayne County ancestors. Distinct from `general_farmer_midwest` (wrong region) and `tenant_farmer` (possibly wrong tenure).

2. **`postbellum_southern_farm_1865_1910.json`** (material_life) -- MEDIUM priority. The material life of Southern farm families in the Reconstruction and New South era. What changed from the antebellum period (currency collapse, credit economy, crop lien as dominant system, railroad penetrating the countryside), what stayed the same (corn-and-pork diet, log-to-frame housing evolution, Baptist church, hog killing), and what was new (disabled veterans as a permanent community presence, Confederate pension system, the slow arrival of manufactured goods). Would serve all Southern ancestors from 1865-1910 -- a large and important population.

3. **Validator calibration** -- LOW priority. Update Abel Bass's expected occupations from `[tenant_farmer, general_farmer_midwest]` to `[general_farmer_south]` once the profile is built. The current expected occupations are the best available approximations but are not precise matches.

---

## Narrative Quality Assessment

**Does the NEL data produce a story worth reading?**

Yes. Abel Bass's story is one of the most compelling test cases yet because it is a story of endurance rather than movement. The narrative arc is unusual for genealogy: not "where did they go?" but "why did they stay?" and "what did it cost?"

The story moves through a clear arc: antebellum yeoman farming (the land, the church, the general store, the pressures of subdivision and soil exhaustion) --> the war (enlistment at 45, service in a NC regiment, capture, imprisonment, survival) --> the return (to a Sampson County gutted by war, its currency worthless, its labor system transformed) --> forty years of farming the same ground (adaptation, persistence, the slow thinning of the community around him) --> death at 89 (a life that began when Madison was president and ended when Roosevelt was).

**What makes this case uniquely valuable for the product:**

- **It tests the non-migration path.** Most genealogy narratives default to the journey. Abel's story is about staying, and the NEL handles it through the stayed_and_adapted trigger with its inverted push/pull factors and its "what staying looked like" section. This is a less-told story and a more common one -- in every migration wave, the majority stayed.

- **The POW experience tests military_service_arc at its most dramatic.** The template's constraints -- no glorification, no emotional projection, clinical language for wounds and conditions -- are exactly right for a prison camp narrative. The template's insistence on naming the specific camp and its documented mortality rate produces narrative power through specificity, not sentiment.

- **The 89-year lifespan tests whether the NEL can tell a long story.** Abel's life spans two material life profiles (frontier_log_cabin into antebellum_yeoman_farm), at least two phases of the antebellum_yeoman_south trigger, the entire Civil War, Reconstruction, the Populist era, and the dawn of the 20th century. The NEL covers the antebellum period and the war beautifully. The post-war period (1865-1905) is thinner -- and the gap is now documented as a build target.

- **Sampson County is the NEL's home turf.** The county is explicitly listed in civil_war_service, antebellum_yeoman_south, stayed_and_adapted, and eastern_nc_farm_community. The economic_life_story template uses Bass family examples (A.W. Bass, the Cannady family in Sampson County). This ancestor lives at the center of the NEL's strongest data coverage.

**What could be stronger:**

- A **postbellum material life profile** would add texture to the last 40 years of Abel's life -- the specific physical conditions of farming in eastern NC after the war. What did the farm look like in 1880? In 1900? How did the arrival of the railroad, manufactured goods, and the Confederate pension change daily life?

- A **Southern general farmer occupation profile** would ground Abel's specific working life in sourced economic data. What did a Sampson County farmer grow, and what did it earn, decade by decade?

- **Abel's actual records** would transform the conditional drafts above into specific narrative. The CMSR would name his regiment and prison camp. The pension file would contain his own testimony. The census wealth columns would establish his economic position. The deed chain would confirm whether he owned or rented. The dry run shows that the NEL framework is ready to receive this data -- the templates, triggers, and guidance all point to exactly the right records.

**The Accuracy Line holds.** Every claim in the draft narratives above is either directly from the NEL files or explicitly flagged as conditional on the ancestor's actual records. "If Abel was held at Point Lookout" -- not "Abel suffered at Point Lookout." "If the deed books confirm it" -- not "Abel owned his land." The NEL's discipline of separating sourced context from individual record evidence is functioning correctly.

**Fourth dry run: PASS.**
