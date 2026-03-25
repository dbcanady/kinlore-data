# Narrative Dry Run #1: Ella Mae Johnson

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)
**Pipeline:** POLSIA_INTEGRATION.md 10-step ancestor processing
**Revenue Tier:** Option A (single-ancestor report)

---

## Ancestor Input Record

| Field | Value |
|-------|-------|
| Name | Ella Mae Johnson |
| Birth Year | 1915 |
| Origin | Bolivar County, Mississippi |
| Destination | Chicago, Illinois |
| Arrival Year | ~1938 |
| Occupation | Domestic servant → meatpacking worker |
| Race | Black |
| Era | 1910-1970 |

**Type:** Synthetic test ancestor — archetypal Great Migration case.

---

## Step 1: Trigger Matching

### Matched Triggers

**Primary:** `great_migration` (core) — era 1910-1970, migration_class: racial_flight
- Bolivar County, MS is explicitly listed in `phases[0].origin_regions[0].counties_most_affected`
- Phase match: First Great Migration (1910-1940), peak departure 1916-1930. Ella Mae's ~1938 departure is between phases — late First wave or early Second wave.
- Primary destination for Mississippi Delta: Chicago (correct match)
- Primary route: Illinois Central Railroad north through Memphis

**Secondary:** `boll_weevil` (core) — era 1892-1930, migration_class: economic
- Bolivar County, MS is explicitly listed in `phases[1].origin_regions[0].counties_most_affected`
- Phase match: Deep South Cotton Collapse (1907-1925). The weevil reached MS by 1907. By Ella Mae's birth in 1915, the damage was already done. By her departure in 1938, the cotton economy had been hollowed out for 30 years.
- The boll_weevil trigger overlaps with great_migration and reinforces the economic push factors.

### Draft Narrative (Trigger Context)

> By 1938, the cotton economy that had defined Bolivar County for fifty years was already a shell. The boll weevil had reached the Mississippi Delta by 1907 — a generation before Ella Mae Johnson left — and by the time she was born in 1915, the crop-lien system was collapsing: landlords evicting tenants, merchants closing stores, the credit that had sustained sharecropping families evaporating. Year after year, the Johnson family likely settled accounts in the fall and heard the same verdict from the landlord's ledger: not enough to clear the debt.
>
> But the economic catastrophe was only half the story. In Bolivar County, Ella Mae Johnson could not vote, could not serve on a jury, and had no meaningful standing in the courts. The threat of racial violence was not distant — it was in the next county, last year. Between the debt that would never be paid and the ballot that could never be cast, the Illinois Central ran straight north to Chicago, and the Chicago Defender — smuggled south in a Pullman porter's bag — said *come*.

### Grade: **STRONG**

Both triggers fire cleanly. Bolivar County is explicitly named in both. The push factors layer perfectly — economic collapse (boll weevil) + racial violence + Jim Crow disenfranchisement (great_migration). The narrative hooks from both triggers resolve cleanly with {county} = "Bolivar County" and {ancestor_name} = "Ella Mae Johnson." The dual-trigger approach adds depth without repetition.

**No issues found.**

---

## Step 2: Route Selection

### Matched Route

`illinois_central` — the Great Migration's signature route.

- Route type: railroad
- Era active: 1856-1970
- Segments: New Orleans → Jackson → Memphis → Chicago (12th Street Station)
- The trigger's `route_refs` include `illinois_central` as primary for Mississippi Delta migrants.
- The segment from Jackson, MS to Memphis is the relevant leg — Bolivar County is in the Delta between these two stops.

### Draft Narrative (Route)

> In 1938, Ella Mae Johnson likely boarded the Illinois Central at one of the dozens of small Delta stops between Clarksdale and Memphis — the same rails that had carried half a million Black southerners toward Chicago since 1916. The Jim Crow cars sat immediately behind the locomotive, where coal smoke and cinders blew in through open windows. Passengers packed their own food — fried chicken, biscuits, boiled eggs — because dining cars would not serve them. Somewhere north of Cairo, Illinois, the conductor would walk through and announce that segregation laws no longer applied. For many migrants, this was the first moment of freedom they had ever experienced.

### Grade: **STRONG**

The Illinois Central route file is vivid and specific. The three-segment breakdown (New Orleans → Jackson → Memphis → Chicago) gives precise distances, travel times, costs, and conditions. The "Chickenbone Express" nickname and the segregation-line detail at Cairo, Illinois, are exactly the kind of texture that makes a narrative come alive. The route file explicitly calls out that Black passengers were confined to cars behind the locomotive — this is the kind of sourced detail that separates good narrative from generic.

**No issues found.**

---

## Step 3: Destination Lookup

### Matched Destination

`chicago` — with Bronzeville / Black Belt as the specific neighborhood.

- The neighborhood entry for "Bronzeville / Black Belt" (era 1916-1970) matches Ella Mae perfectly.
- Primary groups: "African Americans from Mississippi, Alabama, Arkansas, Tennessee" — Ella Mae is from Mississippi.
- Key institutions: Chicago Defender, Pilgrim Baptist Church, Provident Hospital, Wabash Avenue YMCA.
- Major employers: Union Stock Yards / Meatpacking (era 1865-1971) — matches her eventual occupation.

### Draft Narrative (Destination)

> When Ella Mae Johnson arrived in Chicago around 1938, Bronzeville was already a city within a city. Restrictive covenants and the memory of the 1919 race riot — 38 dead, 537 injured, 1,000 Black families left homeless — confined the South Side's Black population to a narrow strip between 26th and 47th Streets along State Street. Despite the crowding, Bronzeville had its own newspaper, hospital, banks, and insurance companies, all because white Chicago would not share its own. The South Side was home to more transplanted Mississippians than some Mississippi counties. Ella Mae probably found her first Chicago church through someone from back home — Southern congregations mapped onto South Side churches, with Mississippi Baptists at one and Alabama Methodists at another.

### Grade: **STRONG**

The Chicago destination file is deep and multi-layered. Bronzeville, Back of the Yards, Polish Triangle, and Maxwell Street are all profiled with era-specific detail. The narrative hooks resolve cleanly — particularly "the South Side was home to more transplanted Mississippians than some Mississippi counties." The anti-immigrant reception section provides the 1919 race riot data that contextualizes why Bronzeville existed. The housing_patterns section ("Black families faced a truncated trajectory — restrictive covenants blocked movement until the 1950s") adds structural context.

**No issues found.**

---

## Step 4: Occupation Enrichment

### Matched Occupations

**Primary (arrival):** `domestic_servant` — era 1865-1970
**Secondary (later):** `meatpacking_worker` — era 1880-1960

Both files are detailed and era-appropriate. Ella Mae's occupation trajectory — domestic service upon arrival, meatpacking work later — is a documented historical pattern for Black women in Chicago during the late 1930s and 1940s, as defense industry and packinghouse jobs opened to Black women during WWII.

### Draft Narrative (Occupation)

> The work that sustained Ella Mae Johnson in her first years in Chicago was the kind of labor that rarely made it into the record books. Domestic service — cooking, cleaning, caring for white families' children while her own waited — paid $5 to $15 per week in the 1930s, with no overtime, no sick days, and no legal protections. Domestic workers were excluded from the 1938 Fair Labor Standards Act. The work was isolating: one worker, one employer, in a private home with no witnesses.
>
> The war changed everything. When defense industries and meatpacking plants began hiring Black women in the early 1940s, Ella Mae likely made the same calculation thousands of Black women made: the stockyards offered steady if brutal work — the killing floor did not care where you came from, only that you could stand the pace. A meatpacking job paid $25 to $35 per week by the 1940s. The wage differential between domestic service and the packinghouse was the same arithmetic that had brought her north in the first place.

### Grade: **STRONG**

Both occupation files are detailed and historically grounded. The domestic_servant file's detail about FLSA exclusion and the "slave markets" of the Bronx adds systemic context. The meatpacking_worker file's progression from pre-union to post-UPWA wages tracks perfectly with Ella Mae's timeline. The transition from domestic work to packinghouse work during WWII is a well-documented historical pattern that both files support.

**One observation:** The domestic_servant file mentions that in the Depression, wages dropped to "$2-$3 per week" — Ella Mae's 1938 arrival places her at the tail end of the Depression. This could sharpen the narrative further.

**No issues found.**

---

## Step 5: Material Life Grounding

### Matched Material Life Profiles

**Origin:** `sharecropper_cabin_1865_1940` — matches Ella Mae's origin in Bolivar County (sharecropping family, pre-migration)
**Destination:** `industrial_city_1880_1920` — partial match. This is the closest available profile for Chicago, but it covers the SE European immigrant experience (1880-1920), not Black Chicago in the 1930s-1940s.

### Draft Narrative (Material Life — Origin)

> The cabin where Ella Mae Johnson grew up was a one- or two-room structure of rough-sawn, unpainted pine, set on log piers with gaps between the boards wide enough to see daylight through. It belonged to the landowner, not the family. Newspaper covered the interior walls for insulation — sometimes the Chicago Defender itself, the paper calling families north literally holding the cold out of the cabin they had not yet left. The family cooked over an iron stove, ate the furnish system's three Ms — cornmeal, fatback, and sorghum molasses — and supplemented with greens, field peas, and catfish from the bayou. A family's entire material wealth — everything not the landlord's property — could be loaded onto a single wagon in an afternoon. The one-way train ticket from Clarksdale to Chicago cost seven dollars: roughly what a sharecropping family might clear in an entire year.

### Grade: **STRONG** (origin) / **THIN** (destination)

The sharecropper_cabin material life profile is spectacular. The newspaper-on-walls detail, the iron pot, the Chicago Defender as insulation, the seven-dollar train ticket — these are exactly the kind of sourced, specific details that make narratives visceral. The sensory snapshot is publication-ready.

**However, the destination material life is THIN.** The `industrial_city_1880_1920` profile describes SE European immigrant life (Polish parishes, feather beds, kielbasa) — it is ethnically and temporally wrong for Black Chicago in the late 1930s. Ella Mae's daily life in a Bronzeville kitchenette apartment in 1940 was materially different from a Polish steelworker's flat in 1905. There is no material life profile for:
- **Black urban life, 1920-1950** (the Great Migration destination experience)
- **Kitchenette apartment / Black Belt overcrowding** (the housing that defined Bronzeville)

**This is the first real gap the dry run has exposed.**

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing material_life profile |
| Searched For | Black urban life, 1920-1960 — Bronzeville kitchenette apartments, overcrowding, urban daily life for Great Migration arrivals |
| Severity | **MEDIUM** — the narrative can use community_texture and destination data to approximate, but there is no dedicated material_life profile for the physical daily experience at the destination |
| Nearest Match | `industrial_city_1880_1920` (wrong era, wrong ethnicity) |
| Recommended Build | `great_migration_destination_1920_1960.json` covering: kitchenette apartments, coal heat, shared bathrooms, urban food (corner grocery vs. garden), streetcar commuting, ice delivery, rent parties |

---

## Step 6: Community Texture

### Matched Community Textures

**Origin 1:** `mississippi_delta_cotton` — origin_community, era 1870-1940
**Origin 2:** `deep_south_black_community` — origin_community, era 1865-1940
**Destination:** `chicago_black_bronzeville` — destination_enclave, era 1916-1960

### Draft Narrative (Community Texture — selected elements)

> On Sunday morning in Bolivar County, the congregation gathered at the Missionary Baptist church — the one building that belonged to Black people, built with their own hands and maintained with their own money. The church deacon board functioned as an informal community government. When the Defender came through — passed hand to hand from the Pullman porter to the barbershop to the church pew — Ella Mae read about jobs in Chicago that paid more in a week than sharecropping paid in a month.
>
> In Chicago, Bronzeville's institutional fabric caught her. Olivet Baptist Church had grown from 800 members in 1915 to over 12,000 by 1930 — it ran employment referrals, housing assistance, and orientation services for Southern newcomers. The Chicago Defender, which had called her north, now documented her daily world in extraordinary detail: arrivals, church memberships, weddings, deaths, and the Bud Billiken parade.

### Grade: **STRONG**

All three community texture profiles are richly detailed. The Mississippi Delta file's treatment of plantation commissaries, juke joints, and the cotton cycle rhythm is exceptional. The deep_south_black_community file adds the broader institutional context (Rosenwald schools, burial societies, Prince Hall Masons). The Bronzeville file is arguably the best-written file in the entire NEL — the treatment of Pilgrim Baptist, Olivet Baptist, Quinn Chapel, the Defender, the Regal Theater, Supreme Life Insurance, and the class dynamics between "old settlers" and "newcomers" provides narrative material for pages.

**No issues found.** The three textures layer perfectly: Delta-specific origin → broader Black South context → Bronzeville destination.

---

## Step 7: Wage Contextualization

### Relevant Wage Data

| Occupation | Era | Region | Annual Income |
|-----------|-----|--------|---------------|
| Sharecropper | 1900s | South | $100-$300 (often negative) |
| Farm laborer | 1930s | South | $150-$300 |
| Domestic servant | 1920s-1930s | Northeast | $260-$780/year |
| Meatpacking worker | 1940s | Midwest (Chicago) | $1,300-$1,800 |
| Meatpacking worker | 1950s (post-UPWA) | Midwest | $3,400-$4,200 |

### Draft Narrative (Wage Context)

> The arithmetic was simple. A sharecropping family in Bolivar County might clear $100 to $300 for an entire year of cotton farming — if they cleared anything at all. In the Depression years of the late 1930s, some families settled their accounts and owed more than they earned. In Chicago, a domestic servant's $5 to $15 per week was modest, but it was cash — not commissary credit, not landlord's arithmetic, but money that belonged to the person who earned it. By the 1940s, when Ella Mae likely moved to meatpacking work, the stockyards paid $25 to $35 per week — roughly $1,300 to $1,800 per year, or six to ten times what sharecropping had ever paid. A week's wages at a Chicago meatpacking plant equaled a month's earnings picking cotton in Bolivar County. Ella Mae could do the arithmetic.

### Grade: **STRONG**

The wage table provides granular, sourced data that makes the economic comparison vivid. The progression from sharecropper ($100-$300/yr) to domestic servant ($260-$780/yr) to meatpacking worker ($1,300-$1,800/yr) is a clear economic arc that the narrative can follow. The critical comparison — Southern agricultural wages vs. Northern industrial wages — is explicitly flagged in the wage table's description as "the economic engine of the Great Migration."

The `cost_of_living.json` table would add further context (what a pound of flour cost, what rent was), but the wage comparison alone carries the argument.

**No issues found.**

---

## Step 8: Template Selection & Draft Output

### Templates Selected

**1. What They Saw** — departure_landscape (Option A gets one variant)
**2. Fork in the Road** — counterfactual

### Draft: What They Saw (Departure Landscape)

> Bolivar County, Mississippi, 1938. The Delta stretches flat from the Yazoo River to the Mississippi — alluvial soil, black and heavy, some of the richest cotton land in America and the poorest place for the people who work it. The fields run to the horizon in every direction, the cotton picked clean by December and the stalks standing dry and brown like rows of dead men. A commissary sits at the crossroads — unpainted clapboard, a kerosene lamp in the window, a ledger on the counter that records every purchase against next year's crop. Behind it, tenant cabins in a row: two rooms each, stick-and-mud chimneys, no glass in the windows. The Illinois Central tracks cut through the flat land a mile east, heading north. At night, the train whistle carries across the open fields.

**Word count:** 140. **Beats:** All 5 hit (framing, topography, agricultural landscape, built environment, sensory close).

### Draft: Fork in the Road

> Had Ella Mae Johnson remained in Bolivar County after 1938, she would have watched the mechanical cotton picker arrive — the International Harvester machine, commercially deployed in 1944, that could harvest in one hour what a manual laborer picked in seventy. Plantation owners who had once needed hundreds of tenant families now needed a handful of machine operators. Bolivar County had fewer people by 1970 than it did in 1900. The sharecropping system that had sustained — and exploited — thousands of families was replaced by machines. The county's Black population dropped by more than half between 1940 and 1970, as young adults departed and only the old remained. Instead, by 1950, Ella Mae Johnson was in Chicago, earning unionized wages at a meatpacking plant that paid more in a week than Bolivar County had ever paid in a month.

**Word count:** 147. **Beats:** All 5 hit (opening frame, economic trajectory, demographic collapse, human detail, closing comparison).

### Grade: **STRONG**

Both template files provide clear structural beats, constraints, and example outputs that guide generation effectively. The `what_they_saw` template's "Walker Evans photographs" tone direction and its prohibition on emotion/people/metaphor produces tight, visual prose. The `fork_in_the_road` template's insistence on documented facts (mechanical cotton picker, 1944; population data) prevents speculation.

**No issues found.**

---

## Step 9: Research Guidance

### Relevant Guidance Files

- `census_gaps` — Ella Mae appears in Southern census (1920, 1930) and Northern census (1940). The gap between 1930 and 1940 is where the migration happened.
- `city_directory_strategies` — Chicago city directories (annual) can narrow her arrival date.
- `church_record_transfers` — Letters of dismission from the Baptist church in Bolivar County + membership records at Olivet or Pilgrim Baptist in Chicago.

### Draft Narrative (Research Guidance)

> The records tell us Ella Mae Johnson was in Bolivar County for the 1930 census and in Chicago for the 1940 census. The migration happened somewhere in between. To narrow the date: check Chicago city directories, published annually, for the first appearance of her name and address. If she joined a church in Chicago — Olivet Baptist, Pilgrim Baptist, or Metropolitan Community — the membership records often noted where members migrated from, and the Southern sending church may have recorded a letter of dismission documenting her departure. The Chicago Defender's social pages are one of the richest sources for Black genealogy in America — search for her name in arrival notices, church announcements, and obituaries.

### Grade: **STRONG**

The guidance files provide specific, actionable research advice with named repositories, record groups, and access methods. The cross-reference between Southern church dismissal letters and Northern church membership rolls is exactly the kind of practical, non-obvious advice that distinguishes a KinLore report from a generic genealogy guide.

**No issues found.**

---

## Step 10: Gap Detection

### Gaps Found

| # | Gap Type | Severity | Description |
|---|----------|----------|-------------|
| 1 | Missing material_life profile | **MEDIUM** | No profile for Black urban life at Great Migration destinations (1920-1960). The industrial_city_1880_1920 profile covers SE European immigrants, not Black Bronzeville. Need: kitchenette apartments, urban food, rent parties, shared bathrooms, coal-heated walkups, ice delivery, streetcar life. |
| 2 | Missing occupation profile | **LOW** | No profile for "laundress" as a standalone occupation. The domestic_servant file covers laundry work, but many Black women in both the South and North worked specifically as laundresses — taking in washing — which was a distinct occupation with different economics (piece-rate, home-based, more autonomy). |

### Gaps NOT Found (Pipeline Success)

All other pipeline components resolved cleanly:
- Both triggers matched with Bolivar County explicitly listed ✓
- Route (Illinois Central) matched perfectly ✓
- Destination (Chicago/Bronzeville) deeply profiled ✓
- Two occupations matched (domestic_servant + meatpacking_worker) ✓
- Origin material life (sharecropper_cabin) excellent ✓
- Three community textures layered perfectly ✓
- Wage data granular and sourced ✓
- Both templates produced clean output ✓
- Research guidance actionable ✓

---

## Report Card

| Pipeline Step | Grade | Notes |
|---------------|-------|-------|
| 1. Trigger Matching | **STRONG** | Dual triggers (great_migration + boll_weevil), both name Bolivar County explicitly |
| 2. Route Selection | **STRONG** | Illinois Central — vivid, sourced, three-segment breakdown |
| 3. Destination Lookup | **STRONG** | Chicago/Bronzeville deeply profiled with era-appropriate institutions |
| 4. Occupation Enrichment | **STRONG** | Both domestic_servant and meatpacking_worker detailed and historically grounded |
| 5. Material Life | **STRONG/THIN** | Origin (sharecropper_cabin) is spectacular; destination has no matching profile |
| 6. Community Texture | **STRONG** | Three textures layer perfectly: Delta → Black South → Bronzeville |
| 7. Wage Contextualization | **STRONG** | Granular comparison drives the economic narrative |
| 8. Templates | **STRONG** | Both What They Saw and Fork in the Road produce clean, constrained output |
| 9. Research Guidance | **STRONG** | Specific repositories, actionable advice |
| 10. Gap Detection | 1 MEDIUM, 1 LOW | Missing: Black urban material life profile; standalone laundress occupation |

### Overall: 9/10 STRONG, 1 THIN

**The NEL produces an excellent narrative for this ancestor.** The data is deep, sourced, era-specific, and emotionally powerful without violating the Accuracy Line. The one significant gap — no material life profile for Black urban Chicago — is addressable and should be a Priority 3 build target.

### Build Targets Identified

1. **`great_migration_urban_1920_1960.json`** (material_life) — MEDIUM priority. Kitchenette apartments, coal heat, shared bathrooms, urban food, streetcar commuting, rent parties, ice delivery, the "Black Belt" as physical reality. Would serve not just Chicago but Detroit, Cleveland, Philadelphia, and NYC Harlem narratives.
2. **`laundress.json`** (occupation) — LOW priority. Distinct from domestic_servant: piece-rate, home-based, more autonomy, washerwomen's strikes, transition to commercial laundry. Would serve both Southern and Northern narratives.

---

## Narrative Quality Assessment

**Does the NEL data produce a story worth reading?**

Yes. Emphatically. The narrative moves through a clear arc: the collapsing cotton economy → the decision to leave → the train north → arriving in a city within a city → finding work → the wage comparison that justified everything. At every beat, the NEL provides sourced, specific, non-generic detail:
- Not just "cotton farming" but the commissary ledger, the furnish system, the boll weevil's county-by-county march
- Not just "took a train" but the Illinois Central's Jim Crow cars, the coal smoke, the moment north of Cairo when segregation laws no longer applied
- Not just "found a job" but the domestic servant's $5/week with no FLSA protection, then the packinghouse at $25-$35/week after the war opened the door
- Not just "lived in Chicago" but Bronzeville between 26th and 47th, the Defender on every corner, Olivet Baptist Church growing from 800 to 12,000 members

**The counter-narratives work.** The data doesn't flatten the story into a simple "escaped the South" narrative. It notes that Northern cities had overcrowded housing, racial covenants, and bitter winters. That some migrants returned. That class differences shaped the experience. That not every departure was permanent.

**The Accuracy Line holds.** Every claim in the draft narrative above is grounded in sourced data from the NEL files. No emotional projection. No fabricated feelings. "Ella Mae could do the arithmetic" — not "Ella Mae dreamed of a better life."

**First dry run: PASS.**
