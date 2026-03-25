# Narrative Dry Run #8: Wong Ah Sing

**Date:** 2026-03-18
**Author:** Claude Code CLI (Opus 4.6)
**Pipeline:** POLSIA_INTEGRATION.md 10-step ancestor processing
**Revenue Tier:** Option A (single-ancestor report)

---

## Ancestor Input Record

| Field | Value |
|-------|-------|
| Name | Wong Ah Sing |
| Birth Year | 1845 |
| Origin | Guangdong, China |
| Destination | Portland, OR |
| Arrival Year | ~1865 |
| Occupation | Railroad laborer / laundry |
| Race | Chinese |
| Era | 1850-1943 |

**Type:** Synthetic test ancestor -- Chinese immigration pipeline. Guangdong to Portland via Pacific crossing. Tests race-aware routing, Pacific crossing route, exclusion era triggers, railroad construction context, and record silences for Chinese Americans. This ancestor has the most complex identity documentation challenges of any test case: his name may not be his birth name, his records were created by a system designed to exclude him, and the 1906 San Francisco earthquake destroyed the municipal records that might have anchored his identity.

---

## Step 1: Trigger Matching

### Matched Triggers

**Primary:** `chinese_exclusion_era` (core) -- era 1850-1943, migration_class: immigration
- Wong Ah Sing's origin (Guangdong, China) is the source region for the vast majority of Chinese immigrants. The trigger explicitly names "Guangdong Province, China (Taishan/Toisan, Xinhui, Kaiping, Enping -- the 'Sze Yup' or Four Counties)" as the primary origin.
- Phase match: Gold Mountain and Railroad Era (1850-1882), peak years 1852-1870. Wong's ~1865 arrival places him squarely in the peak of this phase -- the year the Central Pacific began hiring Chinese labor.
- Portland, OR is explicitly listed in the phase's `primary_destinations` and `counties_most_affected` (Multnomah OR).
- Wong arrives 17 years before the Chinese Exclusion Act (1882) but will live through it. His story spans all three phases: Gold Mountain arrival, exclusion, and extended exclusion.
- Push factors match: Taiping Rebellion (severity 5) -- the deadliest civil war in human history was ravaging Guangdong Province during Wong's youth. Opium Wars aftermath (severity 4) and Guangdong famine/overpopulation (severity 4) compound the crisis.
- Pull factors match: Gold Mountain mythology + railroad labor demand -- the Central Pacific began hiring Chinese workers in 1865, the exact year of Wong's arrival.
- The coercion_note is critical: "After 1882, Chinese immigration was not freely chosen in any meaningful sense." Wong arrived before exclusion but lived under it for 61 years.

**Secondary:** `railroad_construction` (core) -- era 1850-1890, migration_class: economic
- Phase 2 (Transcontinental Construction, 1863-1869) matches Wong's arrival year precisely. "The Central Pacific built east from Sacramento using predominantly Chinese labor, eventually employing over 12,000 Chinese workers."
- Wong's listed occupation (railroad laborer) maps directly to this trigger.
- The trigger explicitly documents the racial wage gap: "Chinese workers on the Central Pacific were paid less than Irish workers for the same work and were required to buy their own food."
- Counter-narrative on erasure: "Despite building the most difficult sections of the transcontinental railroad through the Sierra Nevada, Chinese workers were excluded from the famous completion photograph at Promontory Summit."

### Draft Narrative (Trigger Context)

> In 1865, the year Wong Ah Sing crossed the Pacific, the Taiping Rebellion had killed an estimated twenty to thirty million people in China, and the Pearl River Delta around Guangdong was a landscape of famine, clan warfare, and economic collapse. The Cantonese called California "Gam Saan" -- Gold Mountain -- and the credit-ticket system managed by the Six Companies advanced passage money to young men who could not have afforded it, recouping the debt from their American wages. Wong arrived at the precise moment when the Central Pacific Railroad was transforming Gold Mountain from a mythology into a labor contract: the company was hiring every Chinese man it could find to blast tunnels through the Sierra Nevada, build trestles across canyons, and lay track in conditions that killed hundreds.
>
> What Wong could not have known in 1865 was that the country he had entered would spend the next seventeen years debating whether to let him stay, and then sixty-one years after that making certain that no one like him could follow.

### Grade: **STRONG**

Both triggers fire cleanly and layer effectively. The chinese_exclusion_era trigger is one of the most detailed and historically grounded files in the entire NEL -- its treatment of the credit-ticket system, the Six Companies, the push factors from Guangdong, and the three-phase timeline provides rich narrative material. The railroad_construction trigger adds the labor context. The two triggers together tell the story of Wong's arrival: Guangdong's catastrophe pushed him out, and the Central Pacific's insatiable demand for labor pulled him in.

**No issues found.**

---

## Step 2: Route Selection

### Matched Routes

**Primary:** `pacific_crossing` -- sea_route, era 1850-1943
- This is the correct route for Wong's 1865 arrival. The route covers Hong Kong/Canton to San Francisco, 8,000 miles of open Pacific.
- Travel time: 30-50 days by sailing ship (1860s), 18-21 days by steamship.
- Cost: $40-$60 via credit-ticket system, repaid from wages at high interest.
- Conditions are vivid: "Steerage passengers were packed into the lower holds of ships, sleeping in tiered wooden bunks with no more than eighteen inches between them. The air below decks was thick with the smell of cooking rice, bilge water, and the sickness of men who had never seen the ocean before."

**Noted but not applicable:** `pacific_crossing_angel_island` -- era 1910-1940
- Angel Island opened in 1910, 45 years after Wong's arrival. He would NOT have been processed through Angel Island. However, if Wong was still alive and in Portland when the Geary Act (1892) required Certificates of Identity, he would have interacted with the exclusion bureaucracy at a later date.

**Expected but wrong match:** `southern_pacific` -- railroad, era 1876-1996
- The Southern Pacific route file describes the Sunset Route from New Orleans to Los Angeles/San Francisco. This is a Gulf South to California corridor -- it has nothing to do with a Chinese immigrant traveling from San Francisco to Portland. The expected match is incorrect.
- The actual Portland route from San Francisco would have been coastal steamship (Pacific Mail Steamship Company) or, after the 1880s, overland rail. There is no dedicated "San Francisco to Portland" route file in the NEL.

### Draft Narrative (Route)

> In 1865, Wong Ah Sing likely boarded a sailing ship in Hong Kong or Canton bound for San Francisco -- eight thousand miles of open Pacific, six to eight weeks in steerage, in the hold of a vessel where the air was a mix of cooking rice, bilge water, and the sickness of men who had never been to sea. The credit-ticket system had paid his passage, and the debt would be waiting at the other end. Steerage passengers slept in tiered wooden bunks with eighteen inches between them. Food was rice and dried fish, served twice a day. Fresh water was rationed. When the ship entered the Golden Gate, Chinese passengers were separated from white passengers and held aboard for customs inspection. In 1865 there was no Angel Island, no Chinese Exclusion Act -- just the Pacific Mail wharf and the offices of the Six Companies, which would determine his first bed and his first job.

### Grade: **STRONG** (pacific_crossing) / **BROKEN** (southern_pacific expected match)

The pacific_crossing route file is vivid, specific, and historically grounded. It provides the sensory detail -- the eighteen-inch bunks, the rice and salt fish, the separation at the Golden Gate -- that makes the narrative real. The pacific_crossing_angel_island file is correctly identified but inapplicable (Wong arrives 45 years before Angel Island opens).

### GAP IDENTIFIED (Expected Route Error)

| Field | Value |
|-------|-------|
| Gap Type | Expected route mismatch |
| Description | The expected route `southern_pacific` describes a New Orleans-to-California corridor used primarily by Black migrants and Dust Bowl refugees in the 1920s-1940s. It has no relevance to a Chinese immigrant traveling from San Francisco to Portland in the 1860s-1880s. |
| Severity | **LOW** -- affects validator expectations, not narrative quality |
| Fix | Remove southern_pacific from Wong Ah Sing's expected_routes. The actual secondary route would be Pacific coastal steamship (San Francisco to Portland) or, after 1887, the Southern Pacific's Oregon line. Neither has a dedicated route file. |

### GAP IDENTIFIED (Missing Route)

| Field | Value |
|-------|-------|
| Gap Type | Missing route file |
| Description | No route file covers the San Francisco-to-Portland coastal corridor. Chinese workers moved between San Francisco and Portland via Pacific Mail Steamship Company coastal steamers and later by rail. This was a major internal Chinese American migration corridor. |
| Severity | **MEDIUM** -- the pacific_crossing gets Wong to San Francisco, but there is no route file for the secondary leg to Portland. The Portland destination file mentions coastal shipping ties to San Francisco but there is no standalone route. |
| Recommended Build | `pacific_coastal_steamer.json` covering the San Francisco-Portland-Seattle coastal route used by Chinese workers, salmon cannery laborers, and lumber industry workers, 1860s-1920s. |

---

## Step 3: Destination Lookup

### Matched Destinations

**Primary:** `portland_or` -- peak immigration era 1850-1960
- The Old Town / Chinatown neighborhood entry (era 1870-1950) is directly relevant.
- Character: "Portland's Chinatown was the second-largest on the West Coast after San Francisco. Centered on Second Avenue and the surrounding blocks, it was a dense enclave of boarding houses, shops, temples, and association halls serving Chinese workers employed in canneries, railroads, and lumber."
- Key institutions: Chinese Consolidated Benevolent Association (Portland chapter), Kam Wah Chung & Co., tong headquarters, labor contractors' offices.
- Employer match: Railroads (Northern Pacific, Union Pacific, Southern Pacific, era 1870-1960) -- "Chinese workers built much of the Oregon rail network in the 1870s-1880s."
- Employer match: Canneries (Columbia River Salmon, era 1870-1940) -- "Chinese workers -- called 'China gangs' -- performed the repetitive, fast-paced work of cutting, cleaning, and canning fish."
- Anti-immigrant reception: "Chinese expulsion attempts (1886) -- mobs attempted to drive Chinese residents from Portland and several Oregon towns."
- Narrative hook: "Portland's Chinatown was the second-largest on the West Coast -- if {ancestor_name} was Chinese and came to Oregon, Second Avenue was home base: a few blocks of Cantonese signs and familiar food in a city that made clear, through law and custom, that those few blocks were all that was on offer."

**Secondary:** `san_francisco_chinatown_ca` -- bachelor society peak 1870-1940
- This would be Wong's port of entry and possibly his first American address before moving to Portland.
- The file is extraordinarily detailed: Grant Avenue, Stockton Street, Portsmouth Square, Ross Alley, the Six Companies, Tin How Temple, Chinese Hospital, Cameron House.
- The laundry work employer entry is directly relevant: "The Chinese laundry was the iconic Chinese American small business -- by 1880, Chinese men operated hundreds of laundries across San Francisco."
- Yick Wo v. Hopkins (1886) originated in San Francisco's discriminatory enforcement of laundry licensing.

**Tertiary:** `san_francisco` -- general city destination
- The Chinatown neighborhood entry overlaps with the dedicated san_francisco_chinatown_ca file but adds the broader city context: Angel Island processing, the Workingmen's Party anti-Chinese rallies, the 1906 earthquake.

### Draft Narrative (Destination)

> When Wong Ah Sing reached Portland -- likely after first passing through San Francisco's Chinatown, where the Six Companies assigned housing and employment to new arrivals -- he entered a community that was the second-largest Chinatown on the West Coast. Portland's Chinese quarter centered on Second Avenue: boarding houses where men slept in shifts, a Chinese Consolidated Benevolent Association office that functioned as an informal government, labor contractors' offices that dispatched workers to railroad construction, salmon canneries on the Columbia River, and lumber camps throughout the Oregon interior. Beneath the streets, an extensive network of underground passages connected basements and provided shelter. Like every West Coast Chinatown, Portland's was a bachelor society -- the Page Act of 1875 and the Exclusion Act of 1882 ensured that the men who built Oregon's railroads and packed its salmon could not bring wives or form families.

### Grade: **STRONG**

The Portland destination file is excellent for this ancestor. The Old Town / Chinatown neighborhood is directly profiled with era-appropriate institutions, employers, and anti-immigrant reception data. The san_francisco_chinatown_ca file adds depth for the likely first American stop. The cannery employer entry -- including the "Iron Chink" machine named for its intended purpose of replacing Chinese workers -- provides narrative material that is unflinching and historically grounded.

**No issues found.**

---

## Step 4: Occupation Enrichment

### Matched Occupations

**Primary (arrival):** `railroad_laborer` -- era 1865-1960
- Directly applicable. Daily work: "Built and maintained railroad track. Construction laborers graded roadbed, laid ties, spiked rails, and built bridges and culverts."
- Wages (1860s, Chinese): $0.75-$1.00/day, vs. $1.50-$2.50/day for white workers -- "The wage gap was pure racial discrimination codified into company policy."
- The cultural_context section explicitly addresses the racial stratification: "Chinese laborers built the Central Pacific through the Sierra Nevada; Irish workers built the Union Pacific across the Plains."
- Records generated: Railroad company payroll records, Chinese Exclusion Act case files at NARA.
- Records disrupted: "Mobile workforce rarely appears in county census records. Chinese workers systematically excluded from many local records."

**Secondary (post-railroad):** `laundress` -- era 1850-1940
- The laundress file exists but is framed primarily around Black women in the postbellum South and, secondarily, Chinese laundrymen. The regions section mentions "Western mining and railroad towns: CA, CO, NV, MT (Chinese laundrymen)" but the detailed daily_work description focuses on the physical process of washing by hand -- which is shared across demographics.
- The counter-narrative section is relevant: "Chinese laundrymen on the West Coast were often entrepreneurs who owned their businesses, employed workers, and accumulated capital."
- **However, the file is named "laundress" (feminine) and its detailed framing is around women's work.** A Chinese laundry operator in Portland was a fundamentally different occupation: a male-dominated small business providing a commercial service, not domestic labor. The economics, autonomy, and social meaning were different.

### Draft Narrative (Occupation)

> The Central Pacific paid Chinese workers like Wong Ah Sing seventy-five cents to one dollar per day -- thirty to fifty percent less than the white laborers doing identical work on the same grade. Chinese workers provided their own food (rice and dried fish purchased through Chinese contractors) and lived in camps apart from the rest of the workforce. The work itself was brutal: blasting tunnels through Sierra Nevada granite with black powder, building snow sheds against avalanches, laying track in conditions that killed hundreds. After the transcontinental railroad was completed in 1869, the twelve thousand Chinese workers who had built the most dangerous sections were scattered into whatever employment would have them -- and the Chinese Exclusion Act of 1882 ensured that the scattering would be permanent.
>
> The laundry was the fallback. When every other door was closed, a Chinese man could open a laundry: the work required no English, minimal capital -- a washtub, an iron, a rented room -- and no permission from employers who would not hire Chinese workers for anything else. In Portland's Chinatown, the laundry was not just labor. It was a survival strategy that became a community institution: the one business that white Portland could not take away because white Portland did not want to do the work.

### Grade: **STRONG** (railroad_laborer) / **ADEQUATE** (laundress)

The railroad_laborer file is well-suited for this ancestor. The racial wage differential, the working conditions, and the records implications are all directly applicable. The file's explicit treatment of Chinese labor on the Central Pacific, including the wage discrimination data from Chang's *Ghosts of Gold Mountain*, provides sourced narrative material.

The laundress file is a partial match. Its counter-narrative section acknowledges Chinese laundrymen as entrepreneurs, but the file's core framing is around women's domestic labor -- washboards, lye soap, boiled water. A Chinese laundry operation in Portland was a commercial business, not domestic work. The file works but requires narrative adjustment.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing occupation profile |
| Description | No dedicated occupation file for "Chinese laundryman" or "Chinese laundry operator" as a distinct occupation. The laundress file covers the physical work but not the specific economics, social meaning, and legal context of the Chinese laundry as a male-dominated small business, niche occupation created by exclusion, and subject of landmark civil rights litigation (Yick Wo v. Hopkins, 1886). |
| Severity | **MEDIUM** -- the laundress file and san_francisco_chinatown_ca destination file (which has a laundry work employer entry) together provide enough material, but a dedicated file would be stronger. |
| Recommended Build | `chinese_laundryman.json` covering: the laundry as exclusion-era survival strategy, Yick Wo v. Hopkins, one-man operations, the dispersal of Chinese laundries into small towns nationwide, the economics ($30-$60/month after expenses), the social isolation of running a laundry alone in a town with no other Chinese residents, the laundry as path to merchant status (and therefore legal protection under the Exclusion Act). |

---

## Step 5: Material Life Grounding

### Matched Material Life Profile

`mining_camp_1848_1900` -- the closest era and region match available.

This is a partial match. The mining camp profile covers Western mining districts during the era Wong was active, and it explicitly includes Chinese miners as a distinct population with a `chinese_miner` economic position in the `economic_position` field:

- Position guidance: "Critical adjustment required. The ancestor was Chinese and lived under conditions of legal exclusion, residential segregation, and constant threat of violence. Material life was in Chinatown -- communal bunkhouses, Chinese restaurants, separate stores and temples."
- Narrative hook: "{ancestor_name} worked the margins of the {county} diggings -- confined by law, custom, and threat of violence to claims the white miners had abandoned, living in Chinatown at the edge of camp."

The housing section includes "Chinese camp housing" -- communal bunkhouses, Six Companies dormitories, segregation to the edge of camp. The food section includes "Chinese restaurants and cookhouses" -- serving both Chinese and American food at prices below Anglo establishments. The clothing section includes Chinese traditional clothing -- loose cotton tunics, cloth shoes, the queue. The health section includes Chinese herbal medicine.

### Draft Narrative (Material Life)

> The material life of a Chinese railroad worker in the 1860s was the material life of the camp: a bunk in a communal bunkhouse operated by a Chinese labor contractor, shared with dozens of men from the same Sze Yup districts in Guangdong. The Chinese workers bought and prepared their own food -- rice, dried fish, salted vegetables, and tea, ordered through Chinese merchants -- while white workers received company-provided meals. This arrangement was not a cultural preference; it was a wage structure designed to extract labor at lower cost. Chinese workers wore loose cotton tunics and trousers, cloth shoes, and the queue -- the long braided pigtail mandated by Qing dynasty law and targeted by anti-Chinese mobs as a form of assault. When Wong Ah Sing later settled in Portland's Chinatown, the material world was the same in miniature: a room in a boarding house on Second Avenue, a bunk shared with other men, meals at a Chinese restaurant that served better food at lower prices than any Anglo competitor, and the joss house where incense smoke and Cantonese prayer offered the closest thing to home that ten thousand miles allowed.

### Grade: **ADEQUATE**

The mining_camp_1848_1900 profile works for this ancestor because it explicitly includes Chinese workers as a profiled population. The `chinese_miner` economic position, the Chinese camp housing detail, the food and clothing descriptions, and the herbal medicine section all provide usable material. The sensory snapshot -- "Downstream, the Chinatown begins -- low-roofed buildings, a red-painted joss house, the smell of cooking oil and incense" -- is directly applicable.

**However, this is a mining camp profile, not a railroad construction camp or urban Chinatown profile.** Wong's material life had three distinct phases: railroad construction camp (1865-1869), possible mining work (1870s), and Portland Chinatown (1870s-1943). The mining camp profile covers the middle phase but not the first or third. There is no material life profile for:
- **Railroad construction camp life** (temporary camps along the right-of-way, distinct from mining camps)
- **Urban Chinatown bachelor society** (Portland/San Francisco, 1870-1940) -- the boarding houses, SRO rooms, bachelor apartments, Chinese restaurants, tong headquarters, and joss houses that defined daily life for Chinese men in American cities for six decades.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing material_life profile |
| Description | No profile for urban Chinatown bachelor society life (1870-1940). Wong Ah Sing spent most of his American life not in a mining camp but in Portland's Chinatown -- a boarding house room, bachelor meals, the Six Companies social structure, the material world of exclusion-era urban Chinese America. The mining_camp profile provides some transferable detail (Chinese camp housing, Chinese restaurants) but does not cover the SRO room, the tong meeting hall, the remittance office, the herbal doctor's shop, or the density and isolation of urban Chinatown life. |
| Severity | **HIGH** -- this is the dominant material reality for the majority of Chinese American ancestors from 1870 to 1940. Any Chinese American ancestor who lived in San Francisco, Portland, Seattle, New York, or any other Chinatown needs this profile. |
| Recommended Build | `chinatown_bachelor_society_1870_1940.json` covering: SRO rooms and boarding houses, bachelor cooking and Chinese restaurants, remittance to Guangdong, the joss house, the tong, the herbal medicine shop, Chinese New Year, the material poverty and social density of twelve-block enclaves, the gender ratio (27:1 by 1890), and the daily experience of legal exclusion made physical. |

---

## Step 6: Community Texture

### Matched Community Textures

**Expected:** `new_york_lower_east_side` -- destination_enclave, era 1880-1920.

This is the wrong community texture for a Portland-bound Chinese immigrant. The new_york_lower_east_side profile covers the Lower East Side tenement district -- "Eastern European Jewish (dominant numerically), Southern Italian, Chinese (Cantonese, primarily from Taishan/Toisan), plus smaller Irish, German, and Greek communities." While it does include Chinese residents as part of the LES ethnic mix (Mott, Pell, and Doyers Streets), the file's focus is overwhelmingly Jewish and Italian. It describes a New York neighborhood, not a West Coast Chinatown. Wong Ah Sing never went to New York.

**Actual search result:** No community texture profile exists for any Chinatown community anywhere. There is no:
- `portland_chinatown.json`
- `san_francisco_chinatown.json`
- `chinese_bachelor_society.json`
- Any community texture for Chinese Americans in any location

The 31 community texture profiles cover: Black communities (8 profiles), European immigrant communities (9 profiles), Appalachian/rural Southern white communities (7 profiles), frontier/homesteader communities (3 profiles), WWII boomtowns (1 profile), and specific regional communities (3 profiles). Zero cover Chinese American communities.

### Draft Narrative (Community Texture -- improvised from destination and trigger data)

> Portland's Chinatown was a city within a city -- or more precisely, a village within a city. The Chinese Consolidated Benevolent Association functioned as the community's unofficial government, mediating disputes, organizing collective defense against anti-Chinese agitation, and managing the labor contracts that dispatched workers to railroad construction, salmon canneries, and lumber camps. Within the CCBA, district associations organized by region of origin in Guangdong -- Sze Yup men in one group, Sam Yup in another -- replicated the village structures that the Pacific crossing had shattered. The tongs controlled gambling, labor contracting, and the underground economy. The joss house on Second Avenue offered Taoist and Buddhist worship. The herbalist dispensed remedies from a pharmacopoeia ten thousand miles and three thousand years from Oregon. And on the streets around Second Avenue, Wong Ah Sing lived in a world that was simultaneously the most crowded and the most isolated in Portland -- a few blocks where Cantonese was spoken and familiar food was served, surrounded by a city and a legal system that wanted him gone.

### Grade: **BROKEN**

This is the most significant gap the dry run has exposed. The expected community texture (new_york_lower_east_side) is completely wrong for this ancestor -- it describes the wrong city, the wrong coast, and the wrong primary ethnic group. No community texture exists for any Chinese American community. The narrative above was improvised entirely from the portland_or destination file and the chinese_exclusion_era trigger, not from a dedicated community texture profile.

The absence is severe because the community texture profiles are designed to provide the institutional, social, and cultural fabric of daily life -- the churches, the mutual aid organizations, the gathering places, the social hierarchies, the seasonal rhythms, and the informal economy. For Chinese Americans, this fabric was extraordinarily dense and well-documented: the Six Companies, the district associations, the tongs, the joss houses, Chinese New Year, the herbal medicine tradition, the remittance economy, the bachelor society's social world. None of this is captured in a community texture file.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing community_texture profile |
| Description | No community texture profile exists for any Chinese American community. This is a complete coverage gap for an entire ethnic group. Wong Ah Sing's daily social world -- the Six Companies, district associations, tongs, joss houses, Chinese restaurants, herbal medicine, bachelor society social structures, Chinese New Year, the remittance economy -- is undocumented in the community texture layer. |
| Severity | **CRITICAL** -- this is not a single missing file but a complete ethnic coverage gap. Every Chinese American ancestor in the NEL pipeline will hit this same wall. |
| Recommended Build | At minimum two files: `west_coast_chinatown_bachelor_society.json` (covering SF/Portland/Seattle Chinatowns, 1860-1940) and `chinatown_post_exclusion.json` (covering the transition from bachelor society to family community, 1943-1970). A New York Chinatown file would be a third priority. |

---

## Step 7: Wage Contextualization

### Relevant Wage Data

| Occupation | Era | Region | Annual Income |
|-----------|-----|--------|---------------|
| Railroad construction laborer (Chinese) | 1860s | West | $200-$300 |
| Railroad construction laborer (white) | 1860s | West | $350-$600 |
| General laborer (mining camps) | 1850s | West | $300-$800 |
| Railroad construction laborer | 1880s | West | $300-$500 |

The wage table explicitly documents the racial wage gap on the transcontinental railroad:
- Chinese workers: $0.75-$1.00/day ($200-$300/year)
- White workers: $1.50-$2.50/day ($350-$600/year)
- Context: "Chinese workers on the Central Pacific earned 30-50% less than white laborers doing identical work. They provided their own food and lived in camps. The wage gap was pure racial discrimination codified into company policy."

The san_francisco_chinatown_ca destination file provides supplementary wage data for post-railroad occupations:
- Chinese laundry operator: $30-$60/month ($360-$720/year) after expenses
- Chinese cigar maker: $8-$12/week ($400-$600/year)
- Chinese restaurant worker: $5-$10/week plus meals

### Draft Narrative (Wage Context)

> The arithmetic of Wong Ah Sing's labor was written in two columns. A Chinese railroad worker on the Central Pacific earned seventy-five cents to one dollar per day -- two hundred to three hundred dollars per year. A white worker doing identical work on the same grade earned a dollar fifty to two fifty per day. The gap was not a market outcome. It was company policy, and every Chinese worker knew it. From those wages, Wong paid for his own food -- rice, dried fish, and tea, purchased through Chinese contractors at camp -- while white workers received company-provided meals. After the railroad was completed and the Chinese Exclusion Act closed the door behind him, a laundry in Portland might earn thirty to sixty dollars per month -- enough to live on, enough to send remittances to a family in Guangdong he might never see again, but earned at the cost of sixteen-hour days over boiling water and a hot iron in a one-man shop.

### Grade: **STRONG**

The wage table provides the critical data point: the racial wage differential on the transcontinental railroad, sourced to Gordon Chang's *Ghosts of Gold Mountain* (2019). This is the economic engine of the narrative -- not just what Wong earned, but what white workers earned for identical work. The comparison is damning and documented.

The supplementary wage data from the destination files (laundry operator income) fills the post-railroad gap adequately, though it is embedded in destination files rather than in the wage table itself.

**One observation:** The wage table does not include a standalone entry for "Chinese laundryman" or "Chinese laundry operator" as a distinct occupation with wages. The laundry income data comes from the san_francisco_chinatown_ca destination file's employer section, not from the wage table. A wage entry for Chinese laundry work would strengthen the pipeline.

---

## Step 8: Template Selection & Draft Output

### Templates Selected

**1. What They Saw** -- departure_landscape (Option A gets one variant)
**2. Record Silences** -- silence_as_narrative approach (this ancestor's defining narrative challenge)

### Draft: What They Saw (Departure Landscape -- Guangdong Province, China)

> Guangdong Province, China, 1865. The Pearl River Delta spreads south from Canton to the sea -- alluvial flats, terraced rice paddies climbing the low hills, the river carrying silt and commerce to the trading ports. In the Sze Yup districts, the villages are clusters of grey brick and tile behind earthen walls. The fields are small -- a family's rice paddies may total a single acre, subdivided beyond the threshold of subsistence by the same generational arithmetic that drove Pennsylvania Dutch farmers off their land. Twenty years of rebellion have scoured the countryside: burned villages, untended fields, and young men who are either dead, conscripted, or gone. The port at Hong Kong, ceded to the British after the Opium Wars, is where the ships leave for Gold Mountain. The smell is river mud, night soil, and the charcoal smoke of ten thousand cooking fires.

**Word count:** 141. **Beats:** All 5 hit (framing, topography, agricultural landscape, built environment, sensory close).

### Draft: Record Silences (Silence as Narrative -- What the Record Chose to See)

> The records that survive for Wong Ah Sing were not created to document his life. They were created to control it. The Chinese Exclusion Act (1882) and the Geary Act (1892) built a bureaucratic apparatus designed to regulate, restrict, and ultimately eliminate the Chinese presence in America -- and in doing so, they produced the most detailed immigration case files of any ethnic group. If Wong Ah Sing has a surviving record at NARA, it is a file created by the system that wanted him gone: a photograph taken for a Certificate of Identity, a list of interrogation questions about a village ten thousand miles away, a physical description recorded so that immigration officials could identify him if he tried to leave and return.
>
> The records that were NOT created tell the other half of the story. Wong Ah Sing's birth name may not be the name he used in America -- transliteration from Cantonese to English was inconsistent, and the same man might appear as "Wong Ah Sing," "Ah Sing Wong," "Wong Sing," or "A. S. Wong" across different records. No birth certificate exists; Guangdong Province in 1845 did not issue them. No marriage record exists in Oregon, because the Page Act of 1875 and the Exclusion Act ensured that the woman Wong might have married could not cross the Pacific to join him. The 1906 San Francisco earthquake destroyed the municipal records that might have established his legal presence. The silence in Wong Ah Sing's record is not a gap in research. It is the archive working as designed: documenting exclusion, not existence.

**Word count:** 254. **Approach:** "What the Record Chose to See" from the silence_as_narrative gap type.

### Grade: **STRONG**

The what_they_saw template produces clean output for Guangdong Province. The challenge is that this is the first departure landscape set OUTSIDE the United States -- all previous dry runs departed from American counties. The template's variables ({county}, {state}, {decade}) assume American geography. Despite this, the structural beats transfer well: framing, topography, agricultural landscape, built environment, sensory close all work for a Chinese origin.

The record_silences template is exceptionally well-suited for this ancestor. The silence_as_narrative gap type, with its "what_the_record_chose" approach, is precisely what Wong Ah Sing's case demands. The template's interpretive frame -- "the silence is not a gap in research; it is the archive working as designed" -- becomes even more powerful when the archive was explicitly designed to exclude. The chinese_exclusion_era trigger's record_implications section provides the specific records (Exclusion case files, Certificates of Identity, Angel Island interrogations) and the specific absences (paper son identities, destroyed San Francisco records, transliteration inconsistencies) that make the silence concrete rather than abstract.

### GAP IDENTIFIED (Template Variable)

| Field | Value |
|-------|-------|
| Gap Type | Template variable assumption |
| Description | The what_they_saw template's variables ({county}, {state}, {decade}) assume American geography. For Chinese, European, and other immigrant ancestors, the departure landscape is in another country. The template works but the variables need internationalization for immigrant departure scenes. |
| Severity | **LOW** -- the template's structural beats are universal; only the variable names are America-centric. |
| Fix | Add a note to the template that for immigrant ancestors, {county} and {state} map to {region} and {country}. No structural change needed. |

---

## Step 9: Research Guidance

### Relevant Guidance Files

**1. `name_change_patterns`** -- pattern_id: immigration_anglicization
- Directly applicable but insufficient. The file covers European name anglicization (O'Suilleabhain to Sullivan, Schwarz to Black) and debunks the Ellis Island myth. It does NOT address the specific challenges of Chinese name transliteration: Cantonese romanization inconsistencies, surname-first vs. given-name-first ordering, the loss of tonal distinctions in English, and the paper son system's deliberate identity substitution.

**2. `ethnic_specific_sources`** -- pattern_id: chinese_exclusion_case_files
- Excellent. This is exactly the right guidance for Wong Ah Sing. The section covers:
  - Chinese Exclusion Act case files at NARA (San Bruno for SF arrivals, Seattle for Pacific NW arrivals)
  - Angel Island Immigration Station records
  - Certificates of Identity and Certificates of Residence (Geary Act, 1892)
  - Chinese Historical Society of America resources
  - The paper son identity challenge

### Draft Narrative (Research Guidance)

> The most detailed record that may survive for Wong Ah Sing is, paradoxically, a product of the system that tried to exclude him. Chinese Exclusion Act case files at the National Archives -- held at NARA San Bruno for San Francisco arrivals and NARA Seattle for Pacific Northwest cases -- include photographs, physical descriptions, interrogation transcripts, and supporting documents. If Wong was in the United States when the Geary Act took effect in 1892, he was required to obtain a Certificate of Identity -- effectively an internal passport with a photograph, one of the few photographic records of ordinary Chinese Americans in the 19th century. Search the National Archives Catalog (catalog.archives.gov) for "Chinese Exclusion" and the name "Wong Ah Sing" or variants (Ah Sing Wong, Wong Sing, A. S. Wong). The Chinese Historical Society of America (chsa.org) in San Francisco holds community records, photographs, and oral histories. Portland's Chinese Consolidated Benevolent Association may hold membership records organized by district association, including names, villages of origin, and arrival dates that no American government document recorded.
>
> A critical research caution: the name "Wong Ah Sing" may not be his birth name. Cantonese-to-English transliteration was inconsistent, and the paper son system meant that some Chinese Americans adopted entirely different surnames to enter the country. Family oral history is the essential starting point for distinguishing the documented name from the actual name.

### Grade: **STRONG**

The ethnic_specific_sources guidance for Chinese Exclusion case files is one of the strongest entries in the research guidance collection. Its action steps are specific, actionable, and historically informed. The name_change_patterns file is applicable but needs supplementation -- it covers European anglicization well but does not address the Chinese-specific challenges of Cantonese transliteration, surname ordering, or paper son identity substitution.

### GAP IDENTIFIED

| Field | Value |
|-------|-------|
| Gap Type | Missing research guidance pattern |
| Description | The name_change_patterns file has no pattern for Chinese name transliteration challenges: Cantonese romanization inconsistency, surname-first vs. given-name-first ordering, the loss of tonal distinctions, Wade-Giles vs. Pinyin vs. informal romanization systems, and paper son identity substitution. These are distinct from European anglicization patterns and warrant a dedicated pattern. |
| Severity | **MEDIUM** -- the ethnic_specific_sources file partially covers this through the paper son discussion, but the name_change_patterns file is the logical home for search strategy guidance on Chinese names. |
| Recommended Build | Add a pattern_id `chinese_name_transliteration` to name_change_patterns.json covering: Cantonese romanization systems, surname-first convention, common surname confusion (Wong/Wang/Huang are all the same character), given name ordering (Ah Sing / Sing Ah / A.S.), and the paper son identity overlay. |

---

## Step 10: Gap Detection

### Gaps Found

| # | Gap Type | Severity | Description |
|---|----------|----------|-------------|
| 1 | Missing community_texture | **CRITICAL** | No community texture profile exists for any Chinese American community. This is a complete ethnic coverage gap affecting every Chinese American ancestor. |
| 2 | Missing material_life profile | **HIGH** | No profile for urban Chinatown bachelor society life (1870-1940). The mining_camp profile provides partial coverage through its chinese_miner position, but the dominant material reality for Chinese Americans -- the SRO room, the bachelor boarding house, the twelve-block enclave -- is undocumented. |
| 3 | Missing occupation profile | **MEDIUM** | No dedicated profile for "Chinese laundryman" -- a distinct occupation created by exclusion, subject to landmark litigation, and central to the Chinese American experience. The laundress file is a partial match but misframed. |
| 4 | Missing route file | **MEDIUM** | No route file covers the San Francisco-Portland coastal corridor, a major Chinese American internal migration route. |
| 5 | Missing research guidance pattern | **MEDIUM** | No pattern in name_change_patterns for Chinese name transliteration challenges. |
| 6 | Expected route mismatch | **LOW** | southern_pacific listed as expected route but describes a Gulf South-to-California corridor irrelevant to this ancestor. |
| 7 | Expected community texture mismatch | **LOW** | new_york_lower_east_side listed as expected texture but describes a New York neighborhood irrelevant to a Portland-bound Chinese immigrant. |
| 8 | Template variable assumption | **LOW** | what_they_saw template variables assume American geography; immigrant departure landscapes need internationalized variables. |

### Gaps NOT Found (Pipeline Success)

Despite the significant gaps, several pipeline components resolved well:
- Both triggers (chinese_exclusion_era + railroad_construction) matched cleanly with deep, sourced detail -- the chinese_exclusion_era trigger is one of the best files in the NEL
- Pacific crossing route vivid and historically grounded -- vivid enough to carry the narrative alone
- Portland destination (Old Town/Chinatown) directly profiled with era-appropriate institutions and employers
- Railroad laborer occupation file detailed with explicit Chinese wage data
- Wage table documents the racial wage differential with sourced data
- Record silences template + silence_as_narrative gap type perfectly suited for Chinese American record challenges
- Chinese Exclusion case file research guidance specific and actionable

---

## Report Card

| Pipeline Step | Grade | Notes |
|---------------|-------|-------|
| 1. Trigger Matching | **STRONG** | Dual triggers (chinese_exclusion_era + railroad_construction), both deeply relevant with sourced detail |
| 2. Route Selection | **STRONG/BROKEN** | pacific_crossing excellent; southern_pacific expected match is wrong; SF-to-Portland route missing |
| 3. Destination Lookup | **STRONG** | Portland/Old Town Chinatown directly profiled; SF Chinatown adds depth |
| 4. Occupation Enrichment | **STRONG/ADEQUATE** | railroad_laborer excellent; laundress file is a partial, misframed match |
| 5. Material Life | **ADEQUATE** | mining_camp_1848_1900 has chinese_miner position; no urban Chinatown bachelor society profile |
| 6. Community Texture | **BROKEN** | No Chinese American community texture exists anywhere in the NEL -- complete ethnic gap |
| 7. Wage Contextualization | **STRONG** | Racial wage differential on Central Pacific documented and sourced |
| 8. Templates | **STRONG** | What They Saw works for Guangdong; Record Silences is perfectly suited |
| 9. Research Guidance | **STRONG** | Chinese Exclusion case files guidance is excellent; name transliteration pattern missing |
| 10. Gap Detection | 2 CRITICAL/HIGH, 3 MEDIUM, 3 LOW | Most gaps of any dry run -- complete Chinese American community/material life coverage missing |

### Overall: 5/10 STRONG, 2 ADEQUATE, 1 THIN, 2 BROKEN

**The NEL produces a partial narrative for Wong Ah Sing -- strong in places, fatally thin in others.** The trigger files, the Pacific crossing route, the Portland destination, and the record silences template are excellent. But the pipeline collapses at community texture and material life -- the two layers that are supposed to ground the ancestor in daily lived experience. Without a Chinese American community texture or a bachelor society material life profile, the narrative has no social fabric. The reader learns about the Pacific crossing, the railroad, and the exclusion bureaucracy, but not about what Wong Ah Sing's daily life looked like: the boarding house room, the laundry, the joss house, the remittance office, the chess game in the park.

This is the worst-performing dry run of the series, and it exposes the NEL's most significant ethnic coverage gap.

### Build Targets Identified

1. **`west_coast_chinatown_bachelor_society.json`** (community_texture) -- **CRITICAL** priority. Covers San Francisco, Portland, and Seattle Chinatowns, 1860-1940. Six Companies/CCBA structure, district associations, tongs, joss houses (Tin How Temple, others), Chinese restaurants as social institutions, herbal medicine, Chinese opera, Chinese New Year, the remittance economy, bachelor society social dynamics, the gender ratio (27:1), anti-Chinese violence and community defense, the "bachelor apartment" and SRO room, the Chinese laundry as community institution, Yick Wo v. Hopkins and legal resistance. This is the single highest-priority build target identified by any dry run.

2. **`chinatown_bachelor_society_1870_1940.json`** (material_life) -- **HIGH** priority. The physical daily life of a Chinese man in a West Coast Chinatown: SRO rooms (6x8 feet, triple bunks, $2-$5/month), Chinese restaurant meals (25-50 cents), bachelor cooking (rice pot, tea kettle, dried fish), the remittance table at the district association, the herbal medicine cabinet, Chinese clothing in an American city (transition from traditional to Western dress), the smell of incense and cooking oil, the sound of Cantonese and mahjong tiles. Sensory detail for the world that exclusion built.

3. **`chinese_laundryman.json`** (occupation) -- **MEDIUM** priority. Distinct from laundress: male-dominated, commercial business, exclusion-era survival strategy, Yick Wo v. Hopkins, one-man operations in small towns, path to merchant status, the economics of washing and ironing in a rented room, dispersal nationwide, social isolation. Would serve Chinese American ancestors from 1870 through 1940.

4. **`pacific_coastal_steamer.json`** (route) -- **MEDIUM** priority. San Francisco-Portland-Seattle coastal shipping route, 1860s-1920s. Pacific Mail Steamship Company coastal service, Chinese worker movement between West Coast Chinatowns, salmon cannery seasonal labor migration. Would serve Chinese, Japanese, and general Pacific Northwest migration narratives.

5. **`chinese_name_transliteration`** (research guidance pattern) -- **MEDIUM** priority. Add to name_change_patterns.json: Cantonese romanization inconsistency, surname-first convention, common surname confusion (Wong/Wang/Huang), given name ordering, paper son identity overlay, and search strategies for Chinese names across American records.

---

## Narrative Quality Assessment

**Does the NEL data produce a story worth reading?**

Partially. The narrative has a powerful skeleton but missing flesh.

**What works:**
- The triggers tell a devastating and well-sourced story of push (Taiping Rebellion, famine, Opium Wars) and pull (Gold Mountain, railroad labor demand) followed by betrayal (Chinese Exclusion Act)
- The Pacific crossing route is visceral -- the steerage hold, the rice and salt fish, the separation at the Golden Gate
- The Portland destination file's Old Town/Chinatown neighborhood, the cannery employer entry ("Iron Chink" machine), and the anti-immigrant reception data provide real, unflinching detail
- The wage data makes the racial discrimination concrete: 75 cents for Chinese workers, $1.50-$2.50 for white workers doing identical work
- The record_silences template is arguably MORE powerful for this ancestor than for any other -- the silence_as_narrative approach, combined with the chinese_exclusion_era trigger's record_implications section, produces the most intellectually honest narrative in the series. The records were created by the system of exclusion; the absence of records reflects the exclusion's intent
- The research guidance for Chinese Exclusion case files at NARA is specific and actionable

**What fails:**
- There is no social fabric. The community texture layer -- which for Ella Mae Johnson provided Bronzeville's churches, newspapers, and cultural institutions, and for George Knauss provided the Great Plains homesteader's Grange halls and circuit riders -- is completely absent for Wong Ah Sing. The reader learns that he lived in Portland's Chinatown but has no texture for what Chinatown felt like from the inside
- There is no material daily life. The mining camp profile's chinese_miner position provides fragments, but there is no dedicated profile for the SRO room, the one-man laundry, the bachelor's rice pot, or the remittance letter. The physical world of exclusion-era Chinese America is undocumented in the material life layer
- The occupation pipeline partially fails. Railroad laborer works, but the transition to laundry work -- the defining post-exclusion occupation -- is served by a file framed around Black women's domestic labor, not Chinese men's commercial enterprise

**The Accuracy Line holds.** Every claim in the draft narratives above is grounded in sourced data from the NEL files. The chinese_exclusion_era trigger's source references (Erika Lee, Ronald Takaki, Him Mark Lai, Gordon Chang) are first-rate scholarship. No emotional projection. No fabricated feelings. "Wong could not have known" -- not "Wong dreamed of freedom."

**The dignity mandate holds.** The narrative does not reduce Wong to victimhood. The counter-narratives in the chinese_exclusion_era trigger (Chinese merchants were substantial and influential; Chinese Americans fought exclusion through the courts and sometimes won; the bachelor society was manufactured by law, not by cultural preference) provide the complexity that prevents a flat victimization story. Wong Ah Sing is not a passive object of exclusion. He is a man who crossed eight thousand miles of ocean, built a railroad through the Sierra Nevada, survived the closing of the door behind him, and found a way to make a living in a country that had decided it did not want him.

**What this dry run proves:** The NEL's Chinese American pipeline is half-built. The top of the pipeline (triggers, routes, destinations, wages, research guidance) is strong. The middle of the pipeline (community texture, material life, occupation) has critical gaps. The bottom of the pipeline (templates, especially record_silences) is excellent. The fix is not conceptual -- it is content: three to five new JSON files would bring Wong Ah Sing's narrative to the same quality level as Ella Mae Johnson's or George Knauss's.

**Eighth dry run: CONDITIONAL PASS.** The pipeline produces a publishable narrative, but it is notably thinner than what the NEL delivers for Black, European, or homesteader ancestors. The gaps are addressable and should be prioritized.
