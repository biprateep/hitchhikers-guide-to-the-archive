---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST"
date_accessed: "2026-03-11T16:26:27.981982"
content_length: 36337
---

<!-- CHUNK 1 START -->
This article describes how to discover MAST mission observations of solar system bodies.
**On this page...**
* 1[Search by Target](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-SearchbyTarget)
* 1.1[Portal searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-Portalsearches)
* 1.2[JWST/HST mission search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-JWST/HSTmissionsearch)
* 2[Search by Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-SearchbyCoordinates)
* 2.1[A detailed search of Pan-STARRS](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-AdetailedsearchofPan-STARRS)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-ForFurtherReading...)  
Searching for observations of solar system bodies (planets, moons of planets, dwarf planets, comets, asteroids) is useful to:
* identify data for archival research
* identify observations that might duplicate future observations (e.g., with HST or JWST) you are contemplating
* chart the past history of positions, brightness, or other properties of individual objects  
Crafting queries of such targets with MAST interfaces requires special attention because:
* searching by time-dependent coordinates is not well supported
* object names for solar system bodies are not resolvable to positions by standard catalog services (e.g.,
* targets where the original observer specified a name that may not correspond to an IAU standard name  
There are a few approaches to overcoming these challenges, which are described below.
This article does **not** address determining future target positions for the purpose of**planning observations**. See the article [Solar System Targets](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets#gsc.tab=0) in the Astronomer Proposal Tool ([APT](https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt)) documentation for guidance in this area.

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Search by Target"} -->
The most straightforward approach to search for fixed targets in MAST is by name and (optionally) other metadata. Searching for moving targets (solar system bodies) is different, and requires you to specify additional metadata. The values for metadata in MAST (HST and JWST only) related to solar system bodies are taken from database fields in the Astronomers Proposal Tool ([APT](https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt)), where observers provide their detailed observing plans. Note: some of these fields are auto-populated for APT  _[standard targets](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets/solar-system-standard-targets#gsc.tab=0)_ (e.g., planets and their major moons), but not for _minor bodies_ —e.g., less famous asteroids and recently discovered comets. There are complications, however:
* the target names in MAST may or may not include ancillary information (such as annotations related to offsets or of particular features on an extended target) included in the value string
* the target name for minor bodies is chosen by the observer, and may or may not match a standard name  
Searches in MAST distinguish between
* **Object Name** , where the name is matched to external catalogs and, if successful, determines source coordinates
* **Target Name** , which performs a string match of Observation metadata that are derived from observing programs  
The **Target Name** field is not guaranteed to be populated for any MAST mission except for HST and JWST.
The equivalent _`objectname`_and _`target_name`_, respectively.
Below are strategies to employ when searching MAST for sources by name.
It is not especially helpful to search MAST for observations where the **Moving Target** field has the value 1 (i.e, True): There are thousands of results for both HST and JWST.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "Portal searches"} -->
See the [Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide) chapter [Advanced Search](https://outerspace.stsci.edu/display/MASTDOCS/Advanced+Search) to learn about searching MAST with the [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). In all cases, it is helpful to surround filter values with wildcard characters (use an asterisk: **`*`**) to ensure it matches relevant values in the associated database field.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "Portal searches", "Header 3": "Advanced search"} -->
1. Select the __MAST Observatinos by Object Name or RA/Dec__ collection from the drop-down menu.
2. Click the **Advanced Search** link in the [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) search area.
3. In the **Advanced Search** window select and populate one or both of the filter dialogs for  __Target Name__ and __Target Classification__. The example at right shows the filter dialogs for __Target Name__ (`*didymos*)` and __Target Classification__ (`*asteroid*)`. Remember to enter <_Return_ >_Tab_ > on your keyboard to include text filters in the search criteria.
4. Click the **Search** button.  
![](https://outerspace.stsci.edu/download/attachments/286852359/dialog_nameClass.png?version=1&modificationDate=1736445176489&api=v2)

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "Portal searches", "Header 3": "JWST keyword search"} -->
1. Select the __JWST Instrument Keywords__ collection from the drop-down menu.
2. Click **Advanced Search** in the [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) search area.
3. In the **Advanced Search** window select and populate one or both of the filter dialogs for  __targname__ , __targcat__ , and __targdesc__. The examples at right show the filter dialogs for __targname__ (`*didymos*`), __targcat__ (`*solar system*)` , and __targdesc__ (`*asteroid*)`.
4. Remember to enter <_Return_**>** or <_Tab_ > on your keyboard to include text filters in the search criteria.
5. Click the **Search** button.  
![Portal filter dialogs for targname and targcat](https://outerspace.stsci.edu/download/attachments/286852359/filter_nameCat.png?version=1&modificationDate=1736445177333&api=v2)
![Portal filter dialog for targdesc](https://outerspace.stsci.edu/download/thumbnails/286852359/filter_desc.png?version=1&modificationDate=1736445176985&api=v2)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "JWST/HST mission search"} -->
See the [Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide) chapter [Search Parameter Overview](https://outerspace.stsci.edu/display/MASTDOCS/Search+Parameter+Overview) to learn about searching MAST with the mission-specific searches.
1. From the [HST](https://mast.stsci.edu/search/ui/#/hst/) or [JWST Mission](https://mast.stsci.edu/search/ui/#/jwst/) search, add additional columns to match one or more of __Target Name__ , __Target description from APT__ , and __Target category from APT__.
2. Click the **Search** button.  
![Mission MAST conditions for the column "Target Name", "Target description" and "Target Category"](https://outerspace.stsci.edu/download/attachments/286852359/MM_targetFields.png?version=1&modificationDate=1736445177803&api=v2)
It may be instructive to search solely on __Target Classification__ (or __Target Description__) with the value *`asteroid`* just to see the variety of target names that appear in the results table.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Search by Coordinates"} -->
Discovering observations in MAST of some targets, particularly for missions other than HST and JWST, requires searching by position. The coordinates as a function of time for known solar system bodies can be found from the  
![JPL Horizons System web application interface](https://outerspace.stsci.edu/download/attachments/286852359/ui_horizons.png?version=1&modificationDate=1736445178211&api=v2)
**Figure 1 –** NASA/JPL Horizons System web interface, with selections to request the ephemeris for the asteroid _Didymos_ as observed from JWST in the time interval 2022-09-26 through 2022-10-15 (i.e. starting just before the date of the
If you are suspect that a particular solar system body has been observed and know the approximate time, finding Observations in MAST is straightfoward.
1. Navigate to the JPL Horizons System app, enter the target name, the observer location and time window
1. be sure to set the time step to a sufficiently small interval
2. Generate an ephemeris
3. Use the coordinates from the dates/times of interest, and conduct a search by position in a MAST web tool
1. be sure to set a sufficiently large search radius to ensure a match with the MAST mission/instrument observing aperture

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Search by Coordinates", "Header 2": "A detailed search of Pan-STARRS"} -->
The Pan-STARRS survey includes both images and a catalog; these products are hosted at MAST (see the [Pan-STARRS1 data archive](https://outerspace.stsci.edu/display/PANSTARRS/Pan-STARRS1+data+archive+home+page)). Many images over 3/4 of the sky were obtained in 5 optical passbands over the course of the ~5 year survey, so there is a very good chance that sufficiently bright solar system bodies were detected, often multiple times, in this survey.
A [tutorial](https://outerspace.stsci.edu/display/PANSTARRS/How+to+search+for+moving+targets+in+PS1+images+and+catalogs) has been developed (with an accompanying [Jupyter notebook](https://ps1images.stsci.edu/ps1-moving-database-CADC.html)) to search for a known, but faint, asteroid in the Pan-STARRS catalog and to extract cut-out images from the survey images. To replicate this technique for other know solar system bodies, you will need:
* The
* The
* a working Python installation on your compute environment with the astroquery package installed
* an account on the [MAST CasJobs](https://mastweb.stsci.edu/ps1casjobs/) system to search the PS1! database  
The results show how the position and brightness of the source can be tracked.
The
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* MAST [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) search
* [HST Mission](https://mast.stsci.edu/search/ui/#/hst/) search
* [JWST Mission](https://mast.stsci.edu/search/ui/#/jwst/) search
* [Pan-STARRS tutorial on searching for moving objects](https://outerspace.stsci.edu/display/PANSTARRS/How+to+search+for+moving+targets+in+PS1+images+and+catalogs)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
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
* [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching "Searching")
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data "Browsing Data")
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
* [Tips and Notes](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963055/Tips+and+Notes "Tips and Notes")
* [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials "Demos and Tutorials")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Duplication Checking for Proposals](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals "Duplication Checking for Proposals")
* [Special Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771441/Special+Topics "Special Topics")
* [JWST Commissioning Data Highlights](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights "JWST Commissioning Data Highlights")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Jdaviz in the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113048/Jdaviz+in+the+MAST+Portal "Jdaviz in the MAST Portal")
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [Cloud Science Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797523/Cloud+Science+Platforms "Cloud Science Platforms")
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
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
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
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
* [Duplication Checking for Proposals](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals "Duplication Checking for Proposals")
* [Special Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771441/Special+Topics "Special Topics")
* [JWST Commissioning Data Highlights](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights "JWST Commissioning Data Highlights")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Jdaviz in the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113048/Jdaviz+in+the+MAST+Portal "Jdaviz in the MAST Portal")
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [Cloud Science Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797523/Cloud+Science+Platforms "Cloud Science Platforms")
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
This article describes how to discover MAST mission observations of solar system bodies.
**On this page...**
* 1[Search by Target](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-SearchbyTarget)
* 1.1[Portal searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-Portalsearches)
* 1.2[JWST/HST mission search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-JWST/HSTmissionsearch)
* 2[Search by Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-SearchbyCoordinates)
* 2.1[A detailed search of Pan-STARRS](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-AdetailedsearchofPan-STARRS)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST#FindingSolarSystemBodiesinMAST-ForFurtherReading...)  
Searching for observations of solar system bodies (planets, moons of planets, dwarf planets, comets, asteroids) is useful to:
* identify data for archival research
* identify observations that might duplicate future observations (e.g., with HST or JWST) you are contemplating
* chart the past history of positions, brightness, or other properties of individual objects  
Crafting queries of such targets with MAST interfaces requires special attention because:
* searching by time-dependent coordinates is not well supported
* object names for solar system bodies are not resolvable to positions by standard catalog services (e.g.,
* targets where the original observer specified a name that may not correspond to an IAU standard name  
There are a few approaches to overcoming these challenges, which are described below.
This article does **not** address determining future target positions for the purpose of**planning observations**. See the article [Solar System Targets](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets#gsc.tab=0) in the Astronomer Proposal Tool ([APT](https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt)) documentation for guidance in this area.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Search by Target"} -->
The most straightforward approach to search for fixed targets in MAST is by name and (optionally) other metadata. Searching for moving targets (solar system bodies) is different, and requires you to specify additional metadata. The values for metadata in MAST (HST and JWST only) related to solar system bodies are taken from database fields in the Astronomers Proposal Tool ([APT](https://www.stsci.edu/scientific-community/software/astronomers-proposal-tool-apt)), where observers provide their detailed observing plans. Note: some of these fields are auto-populated for APT  _[standard targets](https://jwst-docs.stsci.edu/jppom/targets/solar-system-targets/solar-system-standard-targets#gsc.tab=0)_ (e.g., planets and their major moons), but not for _minor bodies_ —e.g., less famous asteroids and recently discovered comets. There are complications, however:
* the target names in MAST may or may not include ancillary information (such as annotations related to offsets or of particular features on an extended target) included in the value string
* the target name for minor bodies is chosen by the observer, and may or may not match a standard name  
Searches in MAST distinguish between
* **Object Name** , where the name is matched to external catalogs and, if successful, determines source coordinates
* **Target Name** , which performs a string match of Observation metadata that are derived from observing programs  
The **Target Name** field is not guaranteed to be populated for any MAST mission except for HST and JWST.
The equivalent _`objectname`_and _`target_name`_, respectively.
Below are strategies to employ when searching MAST for sources by name.
It is not especially helpful to search MAST for observations where the **Moving Target** field has the value 1 (i.e, True): There are thousands of results for both HST and JWST.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "Portal searches"} -->
See the [Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide) chapter [Advanced Search](https://outerspace.stsci.edu/display/MASTDOCS/Advanced+Search) to learn about searching MAST with the [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). In all cases, it is helpful to surround filter values with wildcard characters (use an asterisk: **`*`**) to ensure it matches relevant values in the associated database field.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "Portal searches", "Header 3": "Advanced search"} -->
1. Select the __MAST Observatinos by Object Name or RA/Dec__ collection from the drop-down menu.
2. Click the **Advanced Search** link in the [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) search area.
3. In the **Advanced Search** window select and populate one or both of the filter dialogs for  __Target Name__ and __Target Classification__. The example at right shows the filter dialogs for __Target Name__ (`*didymos*)` and __Target Classification__ (`*asteroid*)`. Remember to enter <_Return_ >_Tab_ > on your keyboard to include text filters in the search criteria.
4. Click the **Search** button.  
![](https://outerspace.stsci.edu/download/attachments/286852359/dialog_nameClass.png?version=1&modificationDate=1736445176489&api=v2)

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "Portal searches", "Header 3": "JWST keyword search"} -->
1. Select the __JWST Instrument Keywords__ collection from the drop-down menu.
2. Click **Advanced Search** in the [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) search area.
3. In the **Advanced Search** window select and populate one or both of the filter dialogs for  __targname__ , __targcat__ , and __targdesc__. The examples at right show the filter dialogs for __targname__ (`*didymos*`), __targcat__ (`*solar system*)` , and __targdesc__ (`*asteroid*)`.
4. Remember to enter <_Return_**>** or <_Tab_ > on your keyboard to include text filters in the search criteria.
5. Click the **Search** button.  
![Portal filter dialogs for targname and targcat](https://outerspace.stsci.edu/download/attachments/286852359/filter_nameCat.png?version=1&modificationDate=1736445177333&api=v2)
![Portal filter dialog for targdesc](https://outerspace.stsci.edu/download/thumbnails/286852359/filter_desc.png?version=1&modificationDate=1736445176985&api=v2)

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Search by Target", "Header 2": "JWST/HST mission search"} -->
See the [Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide) chapter [Search Parameter Overview](https://outerspace.stsci.edu/display/MASTDOCS/Search+Parameter+Overview) to learn about searching MAST with the mission-specific searches.
1. From the [HST](https://mast.stsci.edu/search/ui/#/hst/) or [JWST Mission](https://mast.stsci.edu/search/ui/#/jwst/) search, add additional columns to match one or more of __Target Name__ , __Target description from APT__ , and __Target category from APT__.
2. Click the **Search** button.  
![Mission MAST conditions for the column "Target Name", "Target description" and "Target Category"](https://outerspace.stsci.edu/download/attachments/286852359/MM_targetFields.png?version=1&modificationDate=1736445177803&api=v2)
It may be instructive to search solely on __Target Classification__ (or __Target Description__) with the value *`asteroid`* just to see the variety of target names that appear in the results table.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Search by Coordinates"} -->
Discovering observations in MAST of some targets, particularly for missions other than HST and JWST, requires searching by position. The coordinates as a function of time for known solar system bodies can be found from the  
![JPL Horizons System web application interface](https://outerspace.stsci.edu/download/attachments/286852359/ui_horizons.png?version=1&modificationDate=1736445178211&api=v2)
**Figure 1 –** NASA/JPL Horizons System web interface, with selections to request the ephemeris for the asteroid _Didymos_ as observed from JWST in the time interval 2022-09-26 through 2022-10-15 (i.e. starting just before the date of the
If you are suspect that a particular solar system body has been observed and know the approximate time, finding Observations in MAST is straightfoward.
1. Navigate to the JPL Horizons System app, enter the target name, the observer location and time window
1. be sure to set the time step to a sufficiently small interval
2. Generate an ephemeris
3. Use the coordinates from the dates/times of interest, and conduct a search by position in a MAST web tool
1. be sure to set a sufficiently large search radius to ensure a match with the MAST mission/instrument observing aperture

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Search by Coordinates", "Header 2": "A detailed search of Pan-STARRS"} -->
The Pan-STARRS survey includes both images and a catalog; these products are hosted at MAST (see the [Pan-STARRS1 data archive](https://outerspace.stsci.edu/display/PANSTARRS/Pan-STARRS1+data+archive+home+page)). Many images over 3/4 of the sky were obtained in 5 optical passbands over the course of the ~5 year survey, so there is a very good chance that sufficiently bright solar system bodies were detected, often multiple times, in this survey.
A [tutorial](https://outerspace.stsci.edu/display/PANSTARRS/How+to+search+for+moving+targets+in+PS1+images+and+catalogs) has been developed (with an accompanying [Jupyter notebook](https://ps1images.stsci.edu/ps1-moving-database-CADC.html)) to search for a known, but faint, asteroid in the Pan-STARRS catalog and to extract cut-out images from the survey images. To replicate this technique for other know solar system bodies, you will need:
* The
* The
* a working Python installation on your compute environment with the astroquery package installed
* an account on the [MAST CasJobs](https://mastweb.stsci.edu/ps1casjobs/) system to search the PS1! database  
The results show how the position and brightness of the source can be tracked.
The
* * *

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* MAST [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) search
* [HST Mission](https://mast.stsci.edu/search/ui/#/hst/) search
* [JWST Mission](https://mast.stsci.edu/search/ui/#/jwst/) search
* [Pan-STARRS tutorial on searching for moving objects](https://outerspace.stsci.edu/display/PANSTARRS/How+to+search+for+moving+targets+in+PS1+images+and+catalogs)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

