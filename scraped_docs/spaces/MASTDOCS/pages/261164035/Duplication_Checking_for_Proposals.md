---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals"
date_accessed: "2026-03-11T11:33:40.322357"
---

<!-- CHUNK 1 START -->
The [JWST Duplicate Observations Policy](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-general-science-policies/jwst-duplicate-observations-policy) requires proposers for new JWST observing time to justify observations that duplicate any existing or planned observations in other programs. This article describes tools and strategies for identifying and understanding potential duplications. It is the proposer's responsibility to determine if matching observations are genuine duplicates according to the policy.
**On this page...**
* 1[Tools for Identifying Duplicate Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-ToolsforIdentifyingDuplicateObservations)
* 1.1[JWST Duplicate Observation Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-JWSTDuplicateObservationSearch)
* 1.2[Alternative tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-Alternativetools)
* 2[Search Strategies](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-SearchStrategies)
* 2.1[Moving Target Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-MovingTargMovingTargetSearch)
* 2.2[Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-Caveats)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations"} -->
MAST provides tools to discover existing and planned JWST observations that match attributes of those you may be planning for an observing proposal. The information from these searches will help you determine if your observation would be a genuine duplication. This article describes the [JWST Duplicate Observation Search](https://mast.stsci.edu/duplication/#/search), which is optimized for this purpose, and mentions other possible approaches. Later sections of this article summarize strategies for effective searches, as well as caveats that apply to the range of available tools.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "JWST Duplicate Observation Search"} -->
This [custom tool](https://mast.stsci.edu/duplication/#/search), shown in Fig. 1, allows you to compare the parameters of your intended observations with existing or planned observations in the JWST program database. Any matches the tool finds are potential duplicates that require some careful analysis to determine if they are genuine. Detailed comparisons are best done with the program specifications in the APT files of accepted programs with similar observations, but this can be a lengthy and tedious process. This tool will help you identify observations where a potential duplication exists.
Unlike most other MAST tools, this search does not return links to data. Rather, it returns metadata of executed or approved observations.
The search interface (Fig. 1) is similar to other MAST Mission web applications. Use the boxes and pull-down menus to specify the parameters of potential observations, and then execute the search to see if your observations match any that exist in the JWST program database.  
![Interface for JWST Duplicate Observations tool](https://outerspace.stsci.edu/download/attachments/261164035/window_jwst_dupUI.png?version=1&modificationDate=1724329548262&api=v2)
**Figure 1 —** Interface for searching for JWST Observations that match the parameters of your intended observations. Many [elements](https://outerspace.stsci.edu/display/MASTDOCS/Components) of the interface are similar to those in other MAST Mission search interfaces. Various elements of the interface (_numbered boxes_) are described in the text.
To use the tool, enter a fixed target by name or coordinates (_**box 1**_) and specify the search parameters (**_box 2_**) to align with your intended configuration. Then specify additional constraints (_**box 3**_). You may specify more or fewer output fields in the search results (_**box 4**_). See [Moving Target Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-MovingTarg) for strategies to find observations of Solar System targets.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "JWST Duplicate Observation Search", "Header 3": "Search parameters"} -->
The constraint fields provide the means to specify the observing configuration that matches your intended observation.
![](https://outerspace.stsci.edu/download/attachments/261164035/dialog_objCoord.png?version=1&modificationDate=1723136354505&api=v2)
**Object/Coordinates** : Specify the name or coordinates plus the search radius for a fixed target or field of interest, or upload a list of targets/coordinates. These elements and their function are described on the [Target Name Search](https://outerspace.stsci.edu/display/MASTDOCS/Target+Name+Search+And+Upload+List+Search) page.
Note that uploading a large list of targets (or specifying no target at all) could make the results table unwieldy if there are a lot of matches. In this case it can be helpful to add additional constrains using the Column Name/Condition boxes.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/menu_ObsTemplate.png?version=1&modificationDate=1723055950636&api=v2)
**[APT observation template](https://jwst-docs.stsci.edu/jwst-apt-observation-templates#gsc.tab=0):** A compact way of specifying an _instrument_ , its _configuration_ , and _data-taking mode_. All templates are matched by default, but this pull-down menu allows for specific selections or combinations of selections.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/dialog_optConfig.png?version=1&modificationDate=1723147096410&api=v2)
**Optical Elements:** Allows a specification of one or more filters, gratings, or other optical elements (see choices for [MIRI](https://jwst-docs.stsci.edu/jwst-mid-infrared-instrument/miri-instrumentation/miri-filters-and-dispersers#gsc.tab=0), [NIRCam](https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-pupil-and-filter-wheels#gsc.tab=0), [NIRISS](https://jwst-docs.stsci.edu/jwst-near-infrared-imager-and-slitless-spectrograph/niriss-instrumentation/niriss-pupil-and-filter-wheels#gsc.tab=0), [NIRSpec](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-instrumentation/nirspec-dispersers-and-filters#gsc.tab=0)). Matches all optical elements for all instruments by default.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/menu_visitStatus.png?version=1&modificationDate=1723147102873&api=v2)
**Visit Status:** One of: _`Completed`_,_`Failed`_,_`Flight_ready`_,_`Implementation`_._`Scheduled`_,_`Skipped`_,_`Withdrawn`_, Note that Skipped and Failed visits may have been re-planned for a future date. Matches all statuses by default.
![](https://outerspace.stsci.edu/download/attachments/261164035/menu_colCondition.png?version=1&modificationDate=1723136597350&api=v2)
**Column Name/Condition** : Enables setting values or ranges on other field values. These elements and their function are described on the [Additional Search Parameters](https://outerspace.stsci.edu/display/MASTDOCS/Additional+Search+Parameters) page of the [Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide).
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "JWST Duplicate Observation Search", "Header 3": "Results table"} -->
Upon executing a search, a table of results will be displayed (Fig. 2). The table rows are matches from the JWST program database to your search query parameters, and the fields (columns) contain values of metadata that pertain to each matched exposure. These metadata will help you assess whether each given match constitutes a genuine duplication of your intended observation.
The individual table rows aggregate exposures that are identical in:
__Program ID__ , __Observation__ , __Visit__ , __Target ID__ , __Template__ , __Optical elements__ , and __Visit status__
The values of other columns not in the above list are taken from one of the aggregated rows. This includes the __Region shape__ , which would correspond to only one of the aperture positions in a dithered or tiled sequence.  
![](https://outerspace.stsci.edu/download/attachments/261164035/window_jwst_dupResults.png?version=1&modificationDate=1724354815496&api=v2)
**Figure 2 —** Search results table, showing 8 selected rows (blue background) from a GO program. The rows may be sorted by clicking a field (i.e., table column) name.
[Elements](https://outerspace.stsci.edu/display/MASTDOCS/Search+Results+Page) of the interface, such as displayed table size and navigation, are similar to those in other MAST Mission search interfaces, except that there are no options to download data. The table (in its entirety, or only selected rows) may be downloaded for detailed analysis. The names and descriptions of the essential results fields are described below.  
Search Result Essential Field Descriptions
---
Field(s) | Description
Dec Computed | Declination in decimal degrees at the specified epoch. Nominally in the International Celestial Reference System (ICRS). Blank when target_type is MOVING or GENERIC. Blank when primacy is PURE.
Dec Proper Motion | Declination component of proper motion in units of arcsec/year provided by the observer. Can be blank. Positional searches do not take into account proper motion, so increase search radius for targets with large proper motion.
Epoch | Date when the target was at the coordinates in ra_computed and dec_computed, provided by the observer. Can be blank if ra_proper_motion and dec_proper_motion are not specified.
Level 1, Level 2 |  Top-level hierarchical[ identifier](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets/solar-system-targets-position-level-1) for a solar system target. Can be a [standard name](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets/solar-system-standard-targets) (for example, JUPITER), "COMET", or "ASTEROID". Only populated when target_type is MOVING. Second-level hierarchical description of a solar system target. Only standard names (for example EUROPA) are shown here. APT may show additional constraints in one of six  Target Reference Systems. Only populated when target_type is MOVING.
Num Exposures | The number of exposures that were aggregated for that row, with a common Program ID, Observation, Visit, Target ID, Template, Optical Elements, and Visit Status.
Observation |  [Observation number](https://jwst-docs.stsci.edu/jppom/observation-specifications#ObservationSpecifications-ObsNumber) in the range 1 to 999, specified by the observer in APT. This is a link to the corresponding Program Status Information page.
Optical Config | Instrument optical configuration. Depending on which APT template the observer used, the optical configuration encapsulates the filter, pupil, coronagraphic mask, and/or disperser. A forward slash separates different optical elements.
Program | Observing program identification number. Click the program number to visit the [Program Information](https://www.stsci.edu/jwst/science-execution/program-information) web site and retrieve the program in APT to get detailed information about a program.
Visit | Visit number within an observation.
RA Computed | Right ascension in decimal degrees at the specified epoch. Nominally in the International Celestial Reference System (ICRS). Blank when target_type is MOVING or GENERIC. Blank when primacy is PURE.
RA Proper Motion | Right ascension component of proper motion in units of arcsec/year provided by the observer. Can be blank. Positional searches do not take into account proper motion, so increase search radius for targets with large proper motion.
Target Name, Standard Target Name | Convenient [target name in the proposal](https://jwst-docs.stsci.edu/jppom/targets/fixed-targets#FixedTargets-NameintheProposalTargNameProp) provided by the observer. The Standard Target Name is the [target name for the archive](https://jwst-docs.stsci.edu/jppom/targets/fixed-targets#FixedTargets-NamefortheArchiveTargNameArchive) provided by the observer, ideally resolvable by a standard name resolver (e.g., NED, SIMBAD). Can be blank.
Target Type | FIXED for [**fixed targets**](https://jwst-docs.stsci.edu/jppom/targets/fixed-targets), MOVING for [**solar system targets**](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets), GENERIC for [**generic targets**](https://jwst-docs.stsci.edu/jppom/targets/generic-targets) that have not been specified explicitly (e.g., targets of opportunity), or GROUP for [**target groups**](https://jwst-docs.stsci.edu/jppom/targets/target-groups).
Template |  APT [template](https://jwst-docs.stsci.edu/jwst-apt-observation-templates) that the observer used to specify the exposure(s). The 17 main science templates are
* **MIRI** Coron, MIRI Imaging, MIRI LRS, MIRI MRS,
* **NIRCam** Coron, NIRCam Grism TS, NIRCam Imaging, NIRCam TS, NIRCam WFSS,
* **NIRISS** AMI, NIRISS Imaging, NIRISS SOSS, NIRISS WFSS,
* **NIRSpec** BOTS, NIRSpec FSS, NIRSpec IFU, and NIRSpec MOS.  
There are other calibration and engineering templates, some of which are not relevant for duplication checking.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/grid_MMResults_help.png?version=1&modificationDate=1723053922983&api=v2) |  **Other fields** are information-only. View the descriptions by hovering your mouse over the field name, as shown at left.
* * *

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "Alternative tools"} -->
Other tools may also help you determine if your observation will duplicate. These include the MAST Portal and custom notebooks. Here is a comparison.
Tool | Strengths | Weaknesses
---|---|---
[JWST Duplicate Observation Search](https://mast.stsci.edu/duplication/#/search) |
* accesses metadata from the database of observation specifications
* option for specifying observing templates to ensure a precise match to instrument configuration and data-taking mode  
|
* does not provide total exposure duration for an observation
* does not show footprints of matched results
* matches at the exposure level, so there may be many entries per single observation  
[MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) |
* shows spatial footprints of observations against a sky survey background
* can show observations from other MAST missions for planning purposes
* displays correct exposure duration  
|
* harder to match precise instrument configuration; searches by observing template are not possible
* additional work required to determine if matches to TSO observations are genuine duplications
* may not show observations that are being re-planned
* exposure duration for planned observations do not account for combined products
* no special accounting for targets with high proper motion  
[JWST Mission Search](https://mast.stsci.edu/search/ui/#/jwst/) |
* shows a wide variety of observation metadata
* searches can include observing template  
|
* does not show results for planned observations
* does not show footprints
* exposure duration is only useful for combined (L-3) products  
|
* very efficient for querying against many targets at once, and analyzing the results  
|
* does not show footprints of matched results
* additional work required to determine if matches to TSO observations are genuine duplications  
The most accurate means of determining if potential duplicates are genuine is to examine the detailed observation specifications (i.e., the APT file) for programs where a potential duplication is identified.
* * *

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Search Strategies"} -->
The following strategies and tips will help make duplication checking more efficient.
* Limit the initial query to a particular fixed source or set of coordinates, but **without** specifying other criteria.
* If there are no matches, there may be no potential duplicates (except for moving targets)
* If there are too many matches, try searching for one target at a time
* Use a generous search radius (for fixed targets), at least as large as recommended in the [Duplication checking and review procedures](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-general-science-policies/jwst-duplicate-observations-policy#JWSTDuplicateObservationsPolicy-Duplicationcheckingandreviewprocedures).  
* Increase the search radius for small-aperture observations of high proper-motion targets
* Initially use the default of all templates, all program types, and all status values.
* If the search yields matching results, refine your search by selecting parameter values that match your observation in detail.  
Moving object names are not resolvable through the object field. To search for solar system observations  _**add a Condition,**_ as in the following examples.
Column Name | Condition | Result
---|---|---
Level 1 | `Jupiter` | Get observations of anything in the Jupiter system
Target Name | `jup*` | Get observations where one of the target names specified by the observer begins with _**`jup`**_
Target Type | `MOVING` | Get all moving target observations
Standard Target Name
| `*didymos*` | Get observations of this small solar-system body  
Small Solar-System Bodies
For small bodies, the user-provided **Target Name** is often nonstandard. The **Standard Target Name** field, which is the name string used in the archive, follows more predictable naming conventions. Nonetheless, adding wildcard characters before and after the search string is recommended for the most reliable querying. See below for general guidelines on naming conventions.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats"} -->
There are limitations to identifying genuine duplications with search tools, particularly for special circumstances. See also the weakness listed in the Alternative Tools section.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats", "Header 3": "Target names"} -->
It is possible to search MAST for individual sources by name, in one of three ways: _Object Name,_ by _Target Name_ , or (with the Duplicate Observation Search tool) the Standard Target Name.
* **Object Name:** MAST invokes an astrophysical name resolver (e.g.,
* A classic case is the bright star μ Eri from the Bayer Greek letter system, and the star MU Eri in the general catalog of variable stars. In MAST,
* Searching for _`* mu. eri`_(or just plain`mu eri` matches **μ Eri** (RA = 4:45:30.15, Dec = -3:15:16.777)
* Searching for _`V* mu eri`_matches**MU Eri** (RA = 2:48:10.566, Dec = -15:18:04.03)
* **Target Name:** This search matches to target names specified by Investigators in observing proposals to refer to sources. These are not guaranteed to match standard names for astrophysical sources, and often do not.
* **Standard Target Name** : This name is also provided by proposers and is intended to be a name that can be resolved to coordinates by SIMBAD, NED, or other services. The values are not independently vetted, and are often blank.
* For small solar system objects (e.g., asteroids, comets, KBOs), the Standard Target Name field (case-insensitive) follows several naming conventions, which are listed below. For objects with multiple designations, it is recommended that users query all possible designations with wildcard characters using both the Target Name and Standard Target Name conditions.
* **Named small bodies: <number> <name>** (NOTE: Beginning in Cycle 2, the number is no longer included in the Standard Target Name for named asteroids. The use of wildcard characters is recommended (e.g., "*didymos*")
* **Numbered small bodies: <number> (<provisional designation>)** For provisional designations, a space is placed between the year and the first letter (e.g., "459865 (2013 XZ8)")
* **Unnumbered small bodies: ( <provisional designation>)**
* **Named comets: <comet name> **(e.g., "Schwassman-Wachmann 1")
* **Unnamed comets: <discoverer> (<provisional designation>)** (e.g., "PANSTARRS (C/2014 OG392)")  
Because of the limitations noted above, matching observations by Target Name alone may produce misleading results (false positives and false negatives), so it should not be the sole criterion for duplication checking. Entering coordinate pairs is the best approach to searching for matching fixed targets.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats", "Header 3": "Targets with high proper motion"} -->
The fields containing the computed RA and Dec correspond to the celestial coordinates in ICRS (J2000) for fixed targets, or to the coordinates at the specified EPOCH if the proper motion is non-zero. But there are caveats to keep in mind:
* The computed coordinates for sources with significant proper motion will **not** (by construction) be the same as the ICRS coordinates of a resolved source name, nor of the coordinates of your future observation.
* The **Region Shape** field, which contains coordinate pairs that define the observation aperture, must be used with care. The region shapes correspond to the epoch of past observations, not the epoch of your future observation. Keep this in mind when deciding if there is spatial overlap.
* If you conduct a search with the MAST Portal to visualize the footprints (i.e., region shapes), be aware that the background survey, on which the footprints are superimposed, correspond roughly to the mean epoch of the sky survey: DSS (roughly 1990) and Pan-STARRS (roughly 2012.5).

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats", "Header 3": "Exposure duration"} -->
The JWST Duplicate Observations tools does not compute a total exposure duration. This is normally computed by the CAL pipeline, which knows the distinctions between, e.g., dithered vs. tiled images, dithered and nodded spectra, etc.
* * *

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [JWST Duplicate Observations Policy](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-general-science-policies/jwst-duplicate-observations-policy#gsc.tab=0)
* [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)
* Example  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products "Science Data Products")
* [Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products "Supplemental Products")
* [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats "Data Product File Formats")
* [Data Product Linkages](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages "Data Product Linkages")
* [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal "Linkages in the Portal")
* [Keyword Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771333/Keyword+Metadata "Keyword Metadata")
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data "Engineering Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search "Data Search")
* [Data Visualization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771401/Data+Visualization "Data Visualization")
* [Data Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection "Data Selection")
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval "Data Retrieval")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
* [API Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search "API Advanced Search")
* [API Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download "API Curl Download")
* [API for JWST Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata "API for JWST Metadata")
* [API for JWST Science Pixels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113031/API+for+JWST+Science+Pixels "API for JWST Science Pixels")
* [Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API "Basics of an API")
* [Duplication Checking for Proposals](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals "Duplication Checking for Proposals")
* [Special Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771441/Special+Topics "Special Topics")
* [JWST Commissioning Data Highlights](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights "JWST Commissioning Data Highlights")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts "MAST Accounts")
* [FAQ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ "FAQ")
* [Acronym List](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/102531200/Acronym+List "Acronym List")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Searching for Named Sources](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources "Searching for Named Sources")
* [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST "Finding Solar System Bodies in MAST")
* [High PM Stars in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST "High PM Stars in MAST")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [Introduction to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962826/Introduction+to+the+Portal "Introduction to the Portal")
* [Field Guide to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962827/Field+Guide+to+the+Portal "Field Guide to the Portal")
* [Data Holdings](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962855/Data+Holdings "Data Holdings")
* [MAST User Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts "MAST User Accounts")
* [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications "Program Subscriptions and Notifications")
* [Beyond the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962884/Beyond+the+Portal "Beyond the Portal")
* [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching "Searching")
* [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search "Basic Search")
* [Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search "Advanced Search")
* [Catalog Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search "Catalog Search")
* [Search a List of Targets](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets "Search a List of Targets")
* [Special Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches "Special Searches")
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data "Browsing Data")
* [Search Results Grid](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962944/Search+Results+Grid "Search Results Grid")
* [Data Browsing Tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962980/Data+Browsing+Tools "Data Browsing Tools")
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
* [One-Click Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963013/One-Click+Download "One-Click Download")
* [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket "Download Basket")
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods "Retrieval Methods")
* [The Download Bundle](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963052/The+Download+Bundle "The Download Bundle")
* [Tips and Notes](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963055/Tips+and+Notes "Tips and Notes")
* [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials "Demos and Tutorials")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [MAST Primer for JWST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST "MAST Primer for JWST")
* [Updates to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176432244/Updates+to+JWST+Data "Updates to JWST Data")
* [JWST Instrument Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176435458/JWST+Instrument+Names "JWST Instrument Names")
* [JWST Acronyms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150112931/JWST+Acronyms "JWST Acronyms")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products "Science Data Products")
* [Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products "Supplemental Products")
* [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats "Data Product File Formats")
* [Data Product Linkages](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages "Data Product Linkages")
* [Keyword Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771333/Keyword+Metadata "Keyword Metadata")
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data "Engineering Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
* [Duplication Checking for Proposals](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals "Duplication Checking for Proposals")
* [Special Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771441/Special+Topics "Special Topics")
* [JWST Commissioning Data Highlights](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights "JWST Commissioning Data Highlights")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [Cone Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search "Cone Search And Upload List Search")
* [Target Name Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search "Target Name Search And Upload List Search")
* [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview "Search Parameter Overview")
* [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters "Additional Search Parameters")
* [Choose Output Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958266/Choose+Output+Columns "Choose Output Columns")
* [The Search Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958267/The+Search+Bar "The Search Bar")
* [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page "Search Results Page")
* [Image Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/352354485/Image+Previews "Image Previews")
* [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay "Download Overlay")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide "HLSP Search Guide")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Publication Timeline](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/214205149/Publication+Timeline "Publication Timeline")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Collection Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290404/Collection+Contents "Collection Contents")
* [File Types, Formats, and Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content "File Types, Formats, and Content")
* [Organizing the Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection "Organizing the Collection")
* [File Naming Convention](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention "File Naming Convention")
* [Example HLSP README](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290408/Example+HLSP+README "Example HLSP README")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Common Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290410/Common+Metadata "Common Metadata")
* [Image Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290411/Image+Metadata "Image Metadata")
* [Spectral Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290412/Spectral+Metadata "Spectral Metadata")
* [Catalog Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290413/Catalog+Metadata "Catalog Metadata")
* [Light-curve Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290414/Light-curve+Metadata "Light-curve Metadata")
* [Provenance Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata "Provenance Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Jdaviz in the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113048/Jdaviz+in+the+MAST+Portal "Jdaviz in the MAST Portal")
* [Searching for Compatible Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data "Searching for Compatible Data")
* [Interface Field Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide "Interface Field Guide")
* [Viewing Spectra](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra "Viewing Spectra")
* [Finding Associated Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113110/Finding+Associated+Data+Products "Finding Associated Data Products")
* [Supported Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/382632830/Supported+Products "Supported Products")
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
* [Redshift](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113139/Redshift "Redshift")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [Cloud Science Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797523/Cloud+Science+Platforms "Cloud Science Platforms")
* [Getting Started](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started "Getting Started")
* [Managing Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software "Managing Software")
* [Active Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797542/Active+Platforms "Active Platforms")
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [JWST Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products "JWST Supplemental Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [RITA](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA "RITA")
* [RomanCal Refererence Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products "RomanCal Refererence Products")
* [Roman Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products "Roman Supplemental Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
The [JWST Duplicate Observations Policy](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-general-science-policies/jwst-duplicate-observations-policy) requires proposers for new JWST observing time to justify observations that duplicate any existing or planned observations in other programs. This article describes tools and strategies for identifying and understanding potential duplications. It is the proposer's responsibility to determine if matching observations are genuine duplicates according to the policy.
**On this page...**
* 1[Tools for Identifying Duplicate Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-ToolsforIdentifyingDuplicateObservations)
* 1.1[JWST Duplicate Observation Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-JWSTDuplicateObservationSearch)
* 1.2[Alternative tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-Alternativetools)
* 2[Search Strategies](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-SearchStrategies)
* 2.1[Moving Target Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-MovingTargMovingTargetSearch)
* 2.2[Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-Caveats)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-ForFurtherReading...)

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations"} -->
MAST provides tools to discover existing and planned JWST observations that match attributes of those you may be planning for an observing proposal. The information from these searches will help you determine if your observation would be a genuine duplication. This article describes the [JWST Duplicate Observation Search](https://mast.stsci.edu/duplication/#/search), which is optimized for this purpose, and mentions other possible approaches. Later sections of this article summarize strategies for effective searches, as well as caveats that apply to the range of available tools.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "JWST Duplicate Observation Search"} -->
This [custom tool](https://mast.stsci.edu/duplication/#/search), shown in Fig. 1, allows you to compare the parameters of your intended observations with existing or planned observations in the JWST program database. Any matches the tool finds are potential duplicates that require some careful analysis to determine if they are genuine. Detailed comparisons are best done with the program specifications in the APT files of accepted programs with similar observations, but this can be a lengthy and tedious process. This tool will help you identify observations where a potential duplication exists.
Unlike most other MAST tools, this search does not return links to data. Rather, it returns metadata of executed or approved observations.
The search interface (Fig. 1) is similar to other MAST Mission web applications. Use the boxes and pull-down menus to specify the parameters of potential observations, and then execute the search to see if your observations match any that exist in the JWST program database.  
![Interface for JWST Duplicate Observations tool](https://outerspace.stsci.edu/download/attachments/261164035/window_jwst_dupUI.png?version=1&modificationDate=1724329548262&api=v2)
**Figure 1 —** Interface for searching for JWST Observations that match the parameters of your intended observations. Many [elements](https://outerspace.stsci.edu/display/MASTDOCS/Components) of the interface are similar to those in other MAST Mission search interfaces. Various elements of the interface (_numbered boxes_) are described in the text.
To use the tool, enter a fixed target by name or coordinates (_**box 1**_) and specify the search parameters (**_box 2_**) to align with your intended configuration. Then specify additional constraints (_**box 3**_). You may specify more or fewer output fields in the search results (_**box 4**_). See [Moving Target Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals#DuplicationCheckingforProposals-MovingTarg) for strategies to find observations of Solar System targets.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "JWST Duplicate Observation Search", "Header 3": "Search parameters"} -->
The constraint fields provide the means to specify the observing configuration that matches your intended observation.
![](https://outerspace.stsci.edu/download/attachments/261164035/dialog_objCoord.png?version=1&modificationDate=1723136354505&api=v2)
**Object/Coordinates** : Specify the name or coordinates plus the search radius for a fixed target or field of interest, or upload a list of targets/coordinates. These elements and their function are described on the [Target Name Search](https://outerspace.stsci.edu/display/MASTDOCS/Target+Name+Search+And+Upload+List+Search) page.
Note that uploading a large list of targets (or specifying no target at all) could make the results table unwieldy if there are a lot of matches. In this case it can be helpful to add additional constrains using the Column Name/Condition boxes.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/menu_ObsTemplate.png?version=1&modificationDate=1723055950636&api=v2)
**[APT observation template](https://jwst-docs.stsci.edu/jwst-apt-observation-templates#gsc.tab=0):** A compact way of specifying an _instrument_ , its _configuration_ , and _data-taking mode_. All templates are matched by default, but this pull-down menu allows for specific selections or combinations of selections.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/dialog_optConfig.png?version=1&modificationDate=1723147096410&api=v2)
**Optical Elements:** Allows a specification of one or more filters, gratings, or other optical elements (see choices for [MIRI](https://jwst-docs.stsci.edu/jwst-mid-infrared-instrument/miri-instrumentation/miri-filters-and-dispersers#gsc.tab=0), [NIRCam](https://jwst-docs.stsci.edu/jwst-near-infrared-camera/nircam-instrumentation/nircam-pupil-and-filter-wheels#gsc.tab=0), [NIRISS](https://jwst-docs.stsci.edu/jwst-near-infrared-imager-and-slitless-spectrograph/niriss-instrumentation/niriss-pupil-and-filter-wheels#gsc.tab=0), [NIRSpec](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-instrumentation/nirspec-dispersers-and-filters#gsc.tab=0)). Matches all optical elements for all instruments by default.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/menu_visitStatus.png?version=1&modificationDate=1723147102873&api=v2)
**Visit Status:** One of: _`Completed`_,_`Failed`_,_`Flight_ready`_,_`Implementation`_._`Scheduled`_,_`Skipped`_,_`Withdrawn`_, Note that Skipped and Failed visits may have been re-planned for a future date. Matches all statuses by default.
![](https://outerspace.stsci.edu/download/attachments/261164035/menu_colCondition.png?version=1&modificationDate=1723136597350&api=v2)
**Column Name/Condition** : Enables setting values or ranges on other field values. These elements and their function are described on the [Additional Search Parameters](https://outerspace.stsci.edu/display/MASTDOCS/Additional+Search+Parameters) page of the [Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide).
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "JWST Duplicate Observation Search", "Header 3": "Results table"} -->
Upon executing a search, a table of results will be displayed (Fig. 2). The table rows are matches from the JWST program database to your search query parameters, and the fields (columns) contain values of metadata that pertain to each matched exposure. These metadata will help you assess whether each given match constitutes a genuine duplication of your intended observation.
The individual table rows aggregate exposures that are identical in:
__Program ID__ , __Observation__ , __Visit__ , __Target ID__ , __Template__ , __Optical elements__ , and __Visit status__
The values of other columns not in the above list are taken from one of the aggregated rows. This includes the __Region shape__ , which would correspond to only one of the aperture positions in a dithered or tiled sequence.  
![](https://outerspace.stsci.edu/download/attachments/261164035/window_jwst_dupResults.png?version=1&modificationDate=1724354815496&api=v2)
**Figure 2 —** Search results table, showing 8 selected rows (blue background) from a GO program. The rows may be sorted by clicking a field (i.e., table column) name.
[Elements](https://outerspace.stsci.edu/display/MASTDOCS/Search+Results+Page) of the interface, such as displayed table size and navigation, are similar to those in other MAST Mission search interfaces, except that there are no options to download data. The table (in its entirety, or only selected rows) may be downloaded for detailed analysis. The names and descriptions of the essential results fields are described below.  
Search Result Essential Field Descriptions
---
Field(s) | Description
Dec Computed | Declination in decimal degrees at the specified epoch. Nominally in the International Celestial Reference System (ICRS). Blank when target_type is MOVING or GENERIC. Blank when primacy is PURE.
Dec Proper Motion | Declination component of proper motion in units of arcsec/year provided by the observer. Can be blank. Positional searches do not take into account proper motion, so increase search radius for targets with large proper motion.
Epoch | Date when the target was at the coordinates in ra_computed and dec_computed, provided by the observer. Can be blank if ra_proper_motion and dec_proper_motion are not specified.
Level 1, Level 2 |  Top-level hierarchical[ identifier](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets/solar-system-targets-position-level-1) for a solar system target. Can be a [standard name](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets/solar-system-standard-targets) (for example, JUPITER), "COMET", or "ASTEROID". Only populated when target_type is MOVING. Second-level hierarchical description of a solar system target. Only standard names (for example EUROPA) are shown here. APT may show additional constraints in one of six  Target Reference Systems. Only populated when target_type is MOVING.
Num Exposures | The number of exposures that were aggregated for that row, with a common Program ID, Observation, Visit, Target ID, Template, Optical Elements, and Visit Status.
Observation |  [Observation number](https://jwst-docs.stsci.edu/jppom/observation-specifications#ObservationSpecifications-ObsNumber) in the range 1 to 999, specified by the observer in APT. This is a link to the corresponding Program Status Information page.
Optical Config | Instrument optical configuration. Depending on which APT template the observer used, the optical configuration encapsulates the filter, pupil, coronagraphic mask, and/or disperser. A forward slash separates different optical elements.
Program | Observing program identification number. Click the program number to visit the [Program Information](https://www.stsci.edu/jwst/science-execution/program-information) web site and retrieve the program in APT to get detailed information about a program.
Visit | Visit number within an observation.
RA Computed | Right ascension in decimal degrees at the specified epoch. Nominally in the International Celestial Reference System (ICRS). Blank when target_type is MOVING or GENERIC. Blank when primacy is PURE.
RA Proper Motion | Right ascension component of proper motion in units of arcsec/year provided by the observer. Can be blank. Positional searches do not take into account proper motion, so increase search radius for targets with large proper motion.
Target Name, Standard Target Name | Convenient [target name in the proposal](https://jwst-docs.stsci.edu/jppom/targets/fixed-targets#FixedTargets-NameintheProposalTargNameProp) provided by the observer. The Standard Target Name is the [target name for the archive](https://jwst-docs.stsci.edu/jppom/targets/fixed-targets#FixedTargets-NamefortheArchiveTargNameArchive) provided by the observer, ideally resolvable by a standard name resolver (e.g., NED, SIMBAD). Can be blank.
Target Type | FIXED for [**fixed targets**](https://jwst-docs.stsci.edu/jppom/targets/fixed-targets), MOVING for [**solar system targets**](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets), GENERIC for [**generic targets**](https://jwst-docs.stsci.edu/jppom/targets/generic-targets) that have not been specified explicitly (e.g., targets of opportunity), or GROUP for [**target groups**](https://jwst-docs.stsci.edu/jppom/targets/target-groups).
Template |  APT [template](https://jwst-docs.stsci.edu/jwst-apt-observation-templates) that the observer used to specify the exposure(s). The 17 main science templates are
* **MIRI** Coron, MIRI Imaging, MIRI LRS, MIRI MRS,
* **NIRCam** Coron, NIRCam Grism TS, NIRCam Imaging, NIRCam TS, NIRCam WFSS,
* **NIRISS** AMI, NIRISS Imaging, NIRISS SOSS, NIRISS WFSS,
* **NIRSpec** BOTS, NIRSpec FSS, NIRSpec IFU, and NIRSpec MOS.  
There are other calibration and engineering templates, some of which are not relevant for duplication checking.
![](https://outerspace.stsci.edu/download/thumbnails/261164035/grid_MMResults_help.png?version=1&modificationDate=1723053922983&api=v2) |  **Other fields** are information-only. View the descriptions by hovering your mouse over the field name, as shown at left.
* * *

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Tools for Identifying Duplicate Observations", "Header 2": "Alternative tools"} -->
Other tools may also help you determine if your observation will duplicate. These include the MAST Portal and custom notebooks. Here is a comparison.
Tool | Strengths | Weaknesses
---|---|---
[JWST Duplicate Observation Search](https://mast.stsci.edu/duplication/#/search) |
* accesses metadata from the database of observation specifications
* option for specifying observing templates to ensure a precise match to instrument configuration and data-taking mode  
|
* does not provide total exposure duration for an observation
* does not show footprints of matched results
* matches at the exposure level, so there may be many entries per single observation  
[MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) |
* shows spatial footprints of observations against a sky survey background
* can show observations from other MAST missions for planning purposes
* displays correct exposure duration  
|
* harder to match precise instrument configuration; searches by observing template are not possible
* additional work required to determine if matches to TSO observations are genuine duplications
* may not show observations that are being re-planned
* exposure duration for planned observations do not account for combined products
* no special accounting for targets with high proper motion  
[JWST Mission Search](https://mast.stsci.edu/search/ui/#/jwst/) |
* shows a wide variety of observation metadata
* searches can include observing template  
|
* does not show results for planned observations
* does not show footprints
* exposure duration is only useful for combined (L-3) products  
|
* very efficient for querying against many targets at once, and analyzing the results  
|
* does not show footprints of matched results
* additional work required to determine if matches to TSO observations are genuine duplications  
The most accurate means of determining if potential duplicates are genuine is to examine the detailed observation specifications (i.e., the APT file) for programs where a potential duplication is identified.
* * *

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Search Strategies"} -->
The following strategies and tips will help make duplication checking more efficient.
* Limit the initial query to a particular fixed source or set of coordinates, but **without** specifying other criteria.
* If there are no matches, there may be no potential duplicates (except for moving targets)
* If there are too many matches, try searching for one target at a time
* Use a generous search radius (for fixed targets), at least as large as recommended in the [Duplication checking and review procedures](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-general-science-policies/jwst-duplicate-observations-policy#JWSTDuplicateObservationsPolicy-Duplicationcheckingandreviewprocedures).  
* Increase the search radius for small-aperture observations of high proper-motion targets
* Initially use the default of all templates, all program types, and all status values.
* If the search yields matching results, refine your search by selecting parameter values that match your observation in detail.  
Moving object names are not resolvable through the object field. To search for solar system observations  _**add a Condition,**_ as in the following examples.
Column Name | Condition | Result
---|---|---
Level 1 | `Jupiter` | Get observations of anything in the Jupiter system
Target Name | `jup*` | Get observations where one of the target names specified by the observer begins with _**`jup`**_
Target Type | `MOVING` | Get all moving target observations
Standard Target Name
| `*didymos*` | Get observations of this small solar-system body  
Small Solar-System Bodies
For small bodies, the user-provided **Target Name** is often nonstandard. The **Standard Target Name** field, which is the name string used in the archive, follows more predictable naming conventions. Nonetheless, adding wildcard characters before and after the search string is recommended for the most reliable querying. See below for general guidelines on naming conventions.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats"} -->
There are limitations to identifying genuine duplications with search tools, particularly for special circumstances. See also the weakness listed in the Alternative Tools section.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats", "Header 3": "Target names"} -->
It is possible to search MAST for individual sources by name, in one of three ways: _Object Name,_ by _Target Name_ , or (with the Duplicate Observation Search tool) the Standard Target Name.
* **Object Name:** MAST invokes an astrophysical name resolver (e.g.,
* A classic case is the bright star μ Eri from the Bayer Greek letter system, and the star MU Eri in the general catalog of variable stars. In MAST,
* Searching for _`* mu. eri`_(or just plain`mu eri` matches **μ Eri** (RA = 4:45:30.15, Dec = -3:15:16.777)
* Searching for _`V* mu eri`_matches**MU Eri** (RA = 2:48:10.566, Dec = -15:18:04.03)
* **Target Name:** This search matches to target names specified by Investigators in observing proposals to refer to sources. These are not guaranteed to match standard names for astrophysical sources, and often do not.
* **Standard Target Name** : This name is also provided by proposers and is intended to be a name that can be resolved to coordinates by SIMBAD, NED, or other services. The values are not independently vetted, and are often blank.
* For small solar system objects (e.g., asteroids, comets, KBOs), the Standard Target Name field (case-insensitive) follows several naming conventions, which are listed below. For objects with multiple designations, it is recommended that users query all possible designations with wildcard characters using both the Target Name and Standard Target Name conditions.
* **Named small bodies: <number> <name>** (NOTE: Beginning in Cycle 2, the number is no longer included in the Standard Target Name for named asteroids. The use of wildcard characters is recommended (e.g., "*didymos*")
* **Numbered small bodies: <number> (<provisional designation>)** For provisional designations, a space is placed between the year and the first letter (e.g., "459865 (2013 XZ8)")
* **Unnumbered small bodies: ( <provisional designation>)**
* **Named comets: <comet name> **(e.g., "Schwassman-Wachmann 1")
* **Unnamed comets: <discoverer> (<provisional designation>)** (e.g., "PANSTARRS (C/2014 OG392)")  
Because of the limitations noted above, matching observations by Target Name alone may produce misleading results (false positives and false negatives), so it should not be the sole criterion for duplication checking. Entering coordinate pairs is the best approach to searching for matching fixed targets.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats", "Header 3": "Targets with high proper motion"} -->
The fields containing the computed RA and Dec correspond to the celestial coordinates in ICRS (J2000) for fixed targets, or to the coordinates at the specified EPOCH if the proper motion is non-zero. But there are caveats to keep in mind:
* The computed coordinates for sources with significant proper motion will **not** (by construction) be the same as the ICRS coordinates of a resolved source name, nor of the coordinates of your future observation.
* The **Region Shape** field, which contains coordinate pairs that define the observation aperture, must be used with care. The region shapes correspond to the epoch of past observations, not the epoch of your future observation. Keep this in mind when deciding if there is spatial overlap.
* If you conduct a search with the MAST Portal to visualize the footprints (i.e., region shapes), be aware that the background survey, on which the footprints are superimposed, correspond roughly to the mean epoch of the sky survey: DSS (roughly 1990) and Pan-STARRS (roughly 2012.5).

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "Search Strategies", "Header 2": "Caveats", "Header 3": "Exposure duration"} -->
The JWST Duplicate Observations tools does not compute a total exposure duration. This is normally computed by the CAL pipeline, which knows the distinctions between, e.g., dithered vs. tiled images, dithered and nodded spectra, etc.
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [JWST Duplicate Observations Policy](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/jwst-general-science-policies/jwst-duplicate-observations-policy#gsc.tab=0)
* [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html)
* Example  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 23 END -->

