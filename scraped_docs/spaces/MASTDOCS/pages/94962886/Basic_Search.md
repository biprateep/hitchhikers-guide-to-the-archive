---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search"
date_accessed: "2026-03-11T11:32:09.054105"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Selecting Collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-SelectingCollections)
* 2[Choosing a Target...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-ChoosingaTarget...)
* 2.1[...by Name](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byName)
* 2.1.1[Allowed Format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-AllowedFormat)
* 2.2[...by Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byCoordinates)
* 2.2.1[Specify the Search Radius](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-SpecifytheSearchRadius)
* 2.2.2[Allowed Format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-AllowedFormat.1)
* 2.3[...by Observation ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byObservationID)
* 3[Notes on Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-NotesonSearching)  
Basic searches involve two steps:
* select a collection
* input a valid search criterion  
Valid search inputs are either the target name of an astronomical object, or the target coordinates, e.g., Right Ascension (RA) and Declination (Dec). The search box takes specific formatting for target names or coordinates. See the tables within each section below for allowed formatting to ensure correct syntax for proper searches. The search can be initiated by clicking the **Search** button or by pressing the Enter key on your keyboard while the cursor is in the input search box.
![](https://outerspace.stsci.edu/download/attachments/94962886/menu_selectCollection.png?version=2&modificationDate=1660158552235&api=v2)
The basic search form. Select a collection from the pull-down menu (_left_), enter a target name or target coordinates (_right_), then click **Search**.

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Selecting Collections"} -->
Users can choose which collection of data they wish to perform a search in. Most, but not all, collections allow for basic searching by target name or coordinate. The default collection to search is all **MAST Observations**. Unless you wish to search within a specific dataset, it is recommended to leave the default set as is. For more information on searching with the other collections, see sections [Catalog Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search) and [Special Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches).
Collection | Description | Allows Basic Search
---|---|---
MAST Observations | The combined observations from all MAST collections. These include HST, JWST, Kepler, GALEX, EUVE, FUSE, IUE, SWIFT, and several other missions. | yes
Virtual Observatory (VO) | A worldwide collection of repositories providing astronomical images, catalogs and spectra. | yes
[Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/) (HSC) | A catalog of tens of millions of sources from the Hubble Legacy Archive (HLA), derived from HST imaging in multiple instruments and passbands. | yes
Hubble Source Catalog Spectra | A collection of spectra associated with sources in the HSC. | no
MAST Catalogs | MAST-held collections of source lists, e.g. GAIA, TESS input (TIC) catalogs. | yes
Hubble Wide-Field Camera PSF | Libraries of observed, reference point-sources for higher-precision photometry and astrometry. | no
Observations in a DOI | Search for MAST data associated with a Digital Object Identifier. | yes
JWST Instrument Keywords | Search for JWST data by instrument that match a selection of header keyword values. | no
JWST WSS | Search for JWST Wavefront products. | no

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Name"} -->
Users can search for data by inputting the astronomical name of a target object on the sky. Names of objects are passed to a

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Name", "Header 3": "Allowed Format"} -->
Allowed formats for target names are the following:
Example | Description
---|---
`M101, NGC45` | Objects from standard catalogs such as Messier and NGC will be resolved
`Antennae, Eta Carinae` | Common names often work
`T Tau` | Variable star names often work
`BD+19 706` | Star catalogs with coordinate symbols
`png 000.8-07.6` | Other catalogs with coordinate and decimal symbols
`2MASS J04215943+1932063` | All-sky catalogs with coordinate symbols
`TYC 1272-470-1` | All-sky satellite catalogs with restricted symbols

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates"} -->
Users can search for data by providing a target on-sky coordinate of Right Ascension (RA) and Declination (Dec). Coordinates can be given in a variety of formats. Right ascensions must be positive and southern declinations require a leading negative sign. A cone search is performed around the input coordinate at a default radius of 0.2 degrees.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates", "Header 3": "Specify the Search Radius"} -->
A custom search radius can be specified by appending to the coordinates `**r=**[`_number_`][` _unit_`]` , where number is any valid decimal number and unit is one of "d" (degrees), "m" (arc-minutes), "s" (arc-seconds). The default cone search depends on the size of the object but is usually 0.2 degrees for most targets. Note that some collections have search radius limitations. See the table below for examples of various custom search radius inputs.
Example | Description
---|---
`14:03.210 54:20.945r=0.5` | Coordinate search with radius of 0.5°
`14:03.210 54:20.945r=1d` | Coordinate search with radius of 1°
`14:03.210 54:20.945r=1.2m` | Coordinate search with radius of 1.2 arc-minutes

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates", "Header 3": "Allowed Format"} -->
Coordinates can be input either as decimal degrees, sexagesimal or galactic coordinates, with various formatting. Allowed formats for target coordinates are the following:
Example | Description
---|---
`14 03 12.6 54 20 56.7` | Sexagesimal coordinates delimited with spaces
`14:03.210 54:20.945` | Sexagesimal coordinates delimited with colons; decimal minutes/arcminutes
`14h03m12.6s +54d20m56.7s` | Sexagesimal coordinates with explicit hms/dms
`g102.0373+59.7711` |  Galactic coordinates of the form:
* `g`[lon][+/–][lat]  
_**with no spaces**_
`180.468 -18.866` | Coordinates in decimal degrees

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Observation ID"} -->
Most MAST missions assign a unique identifier to individual observations. When selecting the collection **MAST Observations by Observation ID** , the input search box changes to accept only valid mission observation IDs, rather than target names or coordinates, as input. This collection option is for use cases when you know exactly the mission observation you wish to search for. A single observation ID is valid input, as well as a comma-separated list of IDs.
Example | Description
---|---
`tess-s0015-4-1` | Search for a single TESS observation
`tess-s0015-4-1, n4ro01020` | Search for multiple observations by id: a TESS and HST observation

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Notes on Searching"} -->
When**formulating a search** , note the following:
* Leading zeros are ignored in the name. For example, `M5` returns results for object Messier 005.
* Object names are not case-sensitive, and spaces between the characters (e.g. `M51` and `M 51`) are ignored unless the space is significant in the name.
* All coordinates are interpreted as J2000.
* The maximum allowed search radius is limited on a collection-by-collection basis.
* The results of a search of [Virtual Observatory collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-VO_search) may have arbitrary limits on the number of rows returned, on a resource-by-resource basis (i.e., limits which may imposed by the collection provider).
* Most queries are limited to a single object or position, except for searches by observation ID. However, multiple queries may be submitted sequentially, even if one or more queries are still executing.  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
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
**On this page...**
* 1[Selecting Collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-SelectingCollections)
* 2[Choosing a Target...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-ChoosingaTarget...)
* 2.1[...by Name](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byName)
* 2.1.1[Allowed Format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-AllowedFormat)
* 2.2[...by Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byCoordinates)
* 2.2.1[Specify the Search Radius](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-SpecifytheSearchRadius)
* 2.2.2[Allowed Format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-AllowedFormat.1)
* 2.3[...by Observation ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byObservationID)
* 3[Notes on Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-NotesonSearching)  
Basic searches involve two steps:
* select a collection
* input a valid search criterion  
Valid search inputs are either the target name of an astronomical object, or the target coordinates, e.g., Right Ascension (RA) and Declination (Dec). The search box takes specific formatting for target names or coordinates. See the tables within each section below for allowed formatting to ensure correct syntax for proper searches. The search can be initiated by clicking the **Search** button or by pressing the Enter key on your keyboard while the cursor is in the input search box.
![](https://outerspace.stsci.edu/download/attachments/94962886/menu_selectCollection.png?version=2&modificationDate=1660158552235&api=v2)
The basic search form. Select a collection from the pull-down menu (_left_), enter a target name or target coordinates (_right_), then click **Search**.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Selecting Collections"} -->
Users can choose which collection of data they wish to perform a search in. Most, but not all, collections allow for basic searching by target name or coordinate. The default collection to search is all **MAST Observations**. Unless you wish to search within a specific dataset, it is recommended to leave the default set as is. For more information on searching with the other collections, see sections [Catalog Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search) and [Special Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches).
Collection | Description | Allows Basic Search
---|---|---
MAST Observations | The combined observations from all MAST collections. These include HST, JWST, Kepler, GALEX, EUVE, FUSE, IUE, SWIFT, and several other missions. | yes
Virtual Observatory (VO) | A worldwide collection of repositories providing astronomical images, catalogs and spectra. | yes
[Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/) (HSC) | A catalog of tens of millions of sources from the Hubble Legacy Archive (HLA), derived from HST imaging in multiple instruments and passbands. | yes
Hubble Source Catalog Spectra | A collection of spectra associated with sources in the HSC. | no
MAST Catalogs | MAST-held collections of source lists, e.g. GAIA, TESS input (TIC) catalogs. | yes
Hubble Wide-Field Camera PSF | Libraries of observed, reference point-sources for higher-precision photometry and astrometry. | no
Observations in a DOI | Search for MAST data associated with a Digital Object Identifier. | yes
JWST Instrument Keywords | Search for JWST data by instrument that match a selection of header keyword values. | no
JWST WSS | Search for JWST Wavefront products. | no

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Name"} -->
Users can search for data by inputting the astronomical name of a target object on the sky. Names of objects are passed to a

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Name", "Header 3": "Allowed Format"} -->
Allowed formats for target names are the following:
Example | Description
---|---
`M101, NGC45` | Objects from standard catalogs such as Messier and NGC will be resolved
`Antennae, Eta Carinae` | Common names often work
`T Tau` | Variable star names often work
`BD+19 706` | Star catalogs with coordinate symbols
`png 000.8-07.6` | Other catalogs with coordinate and decimal symbols
`2MASS J04215943+1932063` | All-sky catalogs with coordinate symbols
`TYC 1272-470-1` | All-sky satellite catalogs with restricted symbols

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates"} -->
Users can search for data by providing a target on-sky coordinate of Right Ascension (RA) and Declination (Dec). Coordinates can be given in a variety of formats. Right ascensions must be positive and southern declinations require a leading negative sign. A cone search is performed around the input coordinate at a default radius of 0.2 degrees.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates", "Header 3": "Specify the Search Radius"} -->
A custom search radius can be specified by appending to the coordinates `**r=**[`_number_`][` _unit_`]` , where number is any valid decimal number and unit is one of "d" (degrees), "m" (arc-minutes), "s" (arc-seconds). The default cone search depends on the size of the object but is usually 0.2 degrees for most targets. Note that some collections have search radius limitations. See the table below for examples of various custom search radius inputs.
Example | Description
---|---
`14:03.210 54:20.945r=0.5` | Coordinate search with radius of 0.5°
`14:03.210 54:20.945r=1d` | Coordinate search with radius of 1°
`14:03.210 54:20.945r=1.2m` | Coordinate search with radius of 1.2 arc-minutes

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates", "Header 3": "Allowed Format"} -->
Coordinates can be input either as decimal degrees, sexagesimal or galactic coordinates, with various formatting. Allowed formats for target coordinates are the following:
Example | Description
---|---
`14 03 12.6 54 20 56.7` | Sexagesimal coordinates delimited with spaces
`14:03.210 54:20.945` | Sexagesimal coordinates delimited with colons; decimal minutes/arcminutes
`14h03m12.6s +54d20m56.7s` | Sexagesimal coordinates with explicit hms/dms
`g102.0373+59.7711` |  Galactic coordinates of the form:
* `g`[lon][+/–][lat]  
_**with no spaces**_
`180.468 -18.866` | Coordinates in decimal degrees

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Observation ID"} -->
Most MAST missions assign a unique identifier to individual observations. When selecting the collection **MAST Observations by Observation ID** , the input search box changes to accept only valid mission observation IDs, rather than target names or coordinates, as input. This collection option is for use cases when you know exactly the mission observation you wish to search for. A single observation ID is valid input, as well as a comma-separated list of IDs.
Example | Description
---|---
`tess-s0015-4-1` | Search for a single TESS observation
`tess-s0015-4-1, n4ro01020` | Search for multiple observations by id: a TESS and HST observation

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Notes on Searching"} -->
When**formulating a search** , note the following:
* Leading zeros are ignored in the name. For example, `M5` returns results for object Messier 005.
* Object names are not case-sensitive, and spaces between the characters (e.g. `M51` and `M 51`) are ignored unless the space is significant in the name.
* All coordinates are interpreted as J2000.
* The maximum allowed search radius is limited on a collection-by-collection basis.
* The results of a search of [Virtual Observatory collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-VO_search) may have arbitrary limits on the number of rows returned, on a resource-by-resource basis (i.e., limits which may imposed by the collection provider).
* Most queries are limited to a single object or position, except for searches by observation ID. However, multiple queries may be submitted sequentially, even if one or more queries are still executing.  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

