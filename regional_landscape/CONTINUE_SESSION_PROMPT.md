Continue the KinLore Layer 4 (Regional Landscape) project. Check memory files for full state.

**Session completed 2026-03-19:** Layer 4 architecture designed, schema finalized (9 profile types), SE NC + Piedmont fully built, Western Mountains + Lumbee core files built. NEL chain-link index + validator + POLSIA_INTEGRATION updated.

**REMOTE CONTROL MODE: ON.** Work autonomously. Auto-accept. Build aggressively in parallel. Report status at milestones.

---

## THE PLAN — Work in this order:

### Phase 1: Finish NC (make it a fortress)

**1A. Complete Western NC Mountains** (~24 files)
- 11 county landscapes (Buncombe, Madison, Yancey, Watauga, Ashe, Cherokee, Swain, Jackson, Haywood, Mitchell, Avery)
- 11 courthouse atlases (same counties)
- Roads & connectivity (1 file)
- Information landscape (1 file)
- Seasonal calendar (1 file)
- Core files ALREADY BUILT: economy, cultural markers, hidden history, micro-migration

**1B. Complete Lumbee Corridor** (~16 files)
- 5 county landscapes (Robeson, Scotland, Hoke, Columbus, Bladen)
- 5 courthouse atlases (same counties)
- Local economy (1 file)
- Roads & connectivity (1 file)
- Information landscape (1 file)
- Seasonal calendar (1 file)
- NOTE: Lumbee dignity mandate applies throughout. See hidden_history file for guidance.
- Core files ALREADY BUILT: cultural markers, hidden history, micro-migration

**1C. Build NE NC Tidewater/Albemarle** (full ~25-file cluster)
- Counties: Bertie, Hertford, Chowan, Perquimans, Pasquotank, Gates, Currituck, Dare, Tyrrell, Washington, Martin (11 counties)
- Character: Colonial first-settlement (oldest English in America), plantation rice/tobacco, maritime fishing, Outer Banks, isolated Black communities
- Key stories: Lost Colony connection, Blackbeard, colonial plantation slavery, maritime economy, Freedmen's Colony on Roanoke Island (Civil War), isolation and persistence

**1D. Build NC Sandhills/Upper Cape Fear** (full ~25-file cluster)
- Counties: Moore, Harnett, Hoke, Scotland, Richmond, Anson, Montgomery (7 counties)
- Character: Scottish Highland settlement (Gaelic spoken into 19th century), Flora MacDonald, turpentine/lumber, Fort Bragg military impact (1918+), distinctive sandhills ecology
- Key stories: Highland Scots diaspora, Camp Mackall (WWII airborne), Long Street Church (oldest Scottish Presbyterian), sandhills as ecological barrier

**1E. Build Lower Cape Fear/Wilmington** (full ~25-file cluster)
- Counties: New Hanover, Brunswick, Pender, Columbus, Bladen (5 counties)
- Character: Port city, rice culture, 1898 coup (ONLY successful armed overthrow of US government), distinct from inland coastal plain
- Key stories: Wilmington 1898 (already an NEL trigger), rice plantation slavery, Wilmington as largest NC city pre-Civil War, blockade running, Cape Fear River trade

### Phase 2: Adjacent States (SC & VA)

**2A. Build SC Piedmont/Upcountry** (new cluster)
- Counties: Greenville, Spartanburg, Anderson, Laurens, Oconee, Pickens, Cherokee, York (~8 counties)
- Character: Continuation of the NC mill belt across the state line. Same companies, same families, same hierarchy. 1934 strike violence (Honea Path). Connects directly to Piedmont NC cluster.
- Already has NEL regional trigger: sc_upcountry_farm_to_mill

**2B. Build Virginia Tidewater** (new cluster — HIGHEST NATIONAL ROI)
- Counties: James City, York, Henrico, Charles City, Surry, Elizabeth City, Gloucester, Isle of Wight (~8 counties)
- Character: Colonial origin for MILLIONS of Americans. Jamestown. Plantation tobacco. Enslaved labor from 1619. Colonial gentry families. MOST-TRACED ancestry in the US.
- Key stories: 1619 arrival of first enslaved Africans, Bacon's Rebellion (1676), colonial tobacco economy, indentured servitude transition to slavery

**2C. Build Shenandoah Valley, VA** (new cluster)
- Counties: Augusta, Rockingham, Shenandoah, Frederick, Page, Warren (~6 counties)
- Character: Scots-Irish highway via Great Wagon Road. German settlement. Breadbasket of the Confederacy. Sheridan's Burning (1864). Gateway to Appalachian migration.
- Already has NEL regional trigger: va_shenandoah_valley_westward

### Phase 3: User's Family Territory (ND & MN — different perspective)

**3A. Build Great Plains Homestead Belt — ND** (new cluster)
- Counties: Nelson, Walsh, Pembina, Grand Forks, Traill, Cass, Steele, Griggs (~8 counties)
- Character: Homestead Act country. Scandinavian/German-Russian settlement. Wheat boom and bust. Dust Bowl. EXTREME isolation — different from anything in the South.
- User's ancestor George Knauss ended up in Nelson County, ND
- Key stories: Bonanza farms, railroad towns, Norwegian/Swedish/Icelandic enclaves, -40° winters, the proving-up process

**3B. Build Minnesota Scandinavian Belt** (new cluster)
- Counties: Otter Tail, Stearns, Kandiyohi, Meeker, Wright, Douglas (~6 counties)
- Character: Scandinavian homestead arc. Norwegian/Swedish Lutheran communities. Lake country. Already has NEL regional trigger: mn_scandinavian_settlement
- Key stories: Ole Rolvaag's "Giants in the Earth" territory, grasshopper plagues, Dakota War of 1862, immigrant church records in Norwegian/Swedish

### Phase 4: Infrastructure

**4A. Build Layer 4 Validator** — `_validation/validate_regional_landscape.py`
- Inventory check per cluster
- Schema validation per profile type
- Cross-reference validation (all NEL refs resolve)
- FIPS code validation against Layer 1
- Index integrity (every county in index has files)
- Narrative hook variable check
- Source reference check

**4B. Update POLSIA_INTEGRATION.md** — add Layer 4 lookup step (Step 5.5 between Material Life and Life Pattern Matching)

**4C. Update DESIGN_STATE.md and NEL_ROADMAP.md** — document Layer 4

---

## Key Reference Files
- Schema: `/home/dbcanady/kinlore-data/regional_landscape/REGIONAL_LANDSCAPE_SCHEMA.md`
- Index: `/home/dbcanady/kinlore-data/regional_landscape/REGIONAL_LANDSCAPE_INDEX.json`
- NEL integration: `/home/dbcanady/kinlore-data/narrative_enrichment/POLSIA_INTEGRATION.md`
- High-ROI list: memory file `layer4_high_roi_regions.md`
- SE NC exemplars: `/home/dbcanady/kinlore-data/regional_landscape/se_nc_coastal_plain/` (complete cluster — use as template)

## Build Patterns
- Use parallel agents (5+ at a time) for maximum throughput
- County landscapes + courthouse atlases = per-county files (1 each per county)
- Economy + roads + info + micro-migration + seasonal + cultural markers + hidden history = per-cluster files (1 each)
- Validate with `python3 -c "import json; json.load(open('file.json'))"` after each batch
- All files: schema v1.0, zero Wikipedia, {variable} placeholder syntax, NEL cross-references

The user goes by "Kilgore Trout" and prefers autonomous operation. Start with Phase 1A (Western NC Mountains remaining files) and work straight through the plan.
