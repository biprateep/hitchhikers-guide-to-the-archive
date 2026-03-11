---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search"
date_accessed: "2026-03-11T11:32:12.131496"
---

<!-- CHUNK 1 START -->
**On this page:**
* 1[The Advanced Search Window](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-TheAdvancedSearchWindow)
* 2[Applied Filters Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-AppliedFiltersPanel)
* 3[Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-SearchParameters)
* 3.1[Columns Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-ColumnsPanel)
* 3.2[Filters Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-FiltersPanelFiltersPanel)
* 3.2.1[Enumerated Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-EnumeratedFilters)
* 3.2.2[Text Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-TextFilters)
* 3.2.3[Filter Ranges](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-FilterRanges)
* 3.3[Available Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-AvailableFilters)
* 4[Executing a Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-ExecutingaSearch)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "The Advanced Search Window"} -->
Advanced searches, using an expanded set of metadata, are provided for certain MAST data collections, including the default search of MAST Missions. Clicking the __Advanced Search__ link below the Portal target name/coordinates dialog box will bring up the MAST Advanced Search window, which is shown below.  
![](https://outerspace.stsci.edu/download/attachments/94962889/winndow_adv_search_ann.png?version=1&modificationDate=1615209483566&api=v2)  
The **Advanced Search****Window** consists of metadata filters which may be used to constrain the search results. The number of matches to observations with the applied filters is displayed (1: _top_), the **Applied Filters** panel displays the names and values (2: _second from top_), the available filter **Columns** panel (3: _lower left_), and the selected dialogs in the **Filters** **Panel** (4: _lower right_).

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Applied Filters Panel"} -->
![](https://outerspace.stsci.edu/download/attachments/94962889/panel_appliedFilters.png?version=1&modificationDate=1615209483554&api=v2)
Filters for which values or ranges have been applied are summarized in the Applied Filters Panel. Filters may be removed individually, or with the _**Clear All**_ button. Specific filters may be selected in the Columns Panel; values or ranges of values may be set in the individual Filter dialogs.
The term "filters" is, unfortunately, overloaded. Astronomers often think of filters as passband-limiting optical elements. In this context, filters are used to select a subset of available results using one or more criteria.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Search Parameters"} -->
The Advanced Search enables custom searches with a wider variety of criteria that may, but do not necessarily, include a target name or coordinates (as with [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search)). As criteria are applied, preliminary searches will be performed in the background to update the __Records Found__ count at the top of the window. This helps narrow the search to a manageable number of results.
The count of search results must be <50,000 to load the results into the MAST Portal, or <500,000 to download the results to a local file.
Search criteria are specified by:
* selecting one or more available filters in the _**Columns**_ panel, and
* specifying the values (or range of values) in the corresponding dialogs in the _**Filters**_ panel.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/panel_filterColumns.png?version=1&modificationDate=1615209483557&api=v2)
Click entries in the _**Columns Panel**_ to toggle whether a given filter appears (checked) or disappears (unchecked) in the _**Filters Panel**_. You may also restore the default filters or hide all of them by clicking the appropriate text at the top of the panel.
Type the name of a filter in the **Filter Columns** dialog to show (or limit) the filters that are displayed in the columns panel.
The column names shown in the panel (left) may be different, depending upon which collection is being searched.
Filters dialogs come in three flavors depending upon the type of parameter, as described below.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel", "Header 3": "Enumerated Filters"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/filter_enum.png?version=1&modificationDate=1615209483560&api=v2)
Click one or more checkboxes to apply filters with enumerated values. If there are a large number of possible values (e.g., for instrument names), simply click the __Name__ text at the top-left of the filter panel to sort the values in alphabetical order. The desired value may also be typed into the dialog box at the top of the panel.
Typing part of a value (e.g., __HR__) will limit the number of enumerated values to those that contain that character sequence. Then just check the box to choose one.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel", "Header 3": "Text Filters"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/filter_text.png?version=1&modificationDate=1615209483562&api=v2)
Type in the text box and press "return" on your keyboard to apply a filter with a text value. Text values may contain a wildcard (asterisk) character.
Wildcard values may not be used in the __Object Name or Position__ filter.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel", "Header 3": "Filter Ranges"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/filtler_range.png?version=1&modificationDate=1615209483564&api=v2)
Use the sliders to constrain a range, or simply enter floating-point values into the text boxes. The value is applied after the mouse focus is changed.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Available Filters"} -->
About 30 filters are available for restricting search parameters. They map to user-accessible metadata in the MAST CAOM (Common Archive Observation Model) database.
Column Name | Field Type | Description
---|---|---
Object Name or Position | Text | Search for a given target name or coordinates, which is analogous to the primary search Portal search bar (see [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search)). The coordinates are assumed to be Equatorial in the ICRS reference frame (epoch J2000).
Observation Type | Enum | Restrict the search to 'science' or 'calibration' observing programs. Note that on-sky calibration exposures may have some science value.
Mission | Enum | Name or acronym for the mission that obtained the data. High-Level Science Products are collected in the 'HLSP' mission.
Provenance Name | Enum | Identifier of the software or team that produced the data. For HST and JWST mission data the mission corresponds to the calibration pipeline that produced the data.
Instrument | Enum | Acronym for the science instrument used to obtain the data.
Project | Enum | Similar to the 'Mission' field (identical in most cases) but reflects the originating mission, e.g. HST-based HLSPs will have 'HST' in this field.
Filters | Enum | Select one or more names of optical elements (i.e., filters, gratings).
Waveband | Enum | Designation of wavebands (broadly defined).
Target Name | Text | Target name or field as specified by the PI in the observing program.
Target Classification | Enum | Target classification in the STScI proposal database, such as 'STAR' or 'GALAXY'.
Sequence Number | Text | The meaning is specific to a missions, e.g. the Sector number for TESS observations.
Observation ID | Text | Search for a specific observation ID, or similar observation ID's using wildcards.
RA | Range | Specify a range of Right Ascension for the target position. Values are displayed in sexagesimal but can be entered in degrees.
Dec | Range | Specify a range of Declination for the target position Values are displayed in sexagesimal but can be entered in degrees.
Proposal ID | Text | Specify a proposal/program ID number. Wildcards are allowed.
Principal Investigator | Text | Filter on certain Principal Investigator names. Wildcards are advised.
Product Type | Enum | Specify certain data product types, such as 'image' or 'spectrum'.
Calibration Level | Enum | Filter on numerical calibration levels assigned to observations. High-Level Science Product (HLSP) data are designated Level 4, while planned-but-not-executed observations are Level –1. The meaning of a level is mission-specific.
Start Time | Range | Specify a range of start date-times (in UTC) for the matched exposures.
End Time | Range | Specify a range of end date-times (in UTC) for the matched exposures.
Exposure Length | Range | Specify a range of exposure duration in seconds.
Min. Wavelength | Range | Specify a range of lower-bound wavelengths in nm.
Max. Wavelength | Range | Specify a range of upper-bound wavelengths in nm.
Observation Title | Text | Filter on specific proposal titles. Wildcards are advised.
Release Date | Range | Specify a range of data release dates (i.e., when the data become public). For Exclusive Access data, this date may be in the future.
Proposal Type | Enum | Filter on specific proposal types, such as 'GO' or 'SNAP'. The appropriate types will vary by mission.
Data Rights | Enum | Filter for 'PUBLIC' or 'EXCLUSIVE_ACCESS' data permissions (or 'PROPRIETARY' but this is being phased out going forward).
Moving Target | Enum | Use this boolean flag to filter moving targets.
Product Group ID | Text | Filter on product group ID's from MAST databases.
Object ID | Text | Filter on object ID's from MAST databases.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Executing a Search"} -->
After adding the desired search parameters, there are two options to inspect the matching observations.  
![](https://outerspace.stsci.edu/download/thumbnails/94962889/button_search.png?version=1&modificationDate=1615209483547&api=v2) | Click the **Search** button to load the search results into a tab in the MAST Portal. The 'Records Found' count must be under 50,000 for this option to become available.
---|---
![](https://outerspace.stsci.edu/download/thumbnails/94962889/button_export_table.png?version=1&modificationDate=1615209483541&api=v2) | Click the **Export Table** button to download the table of search results as a file (CSV, VO Table, or JSON). This will work with search result counts up to 500,000.
![](https://outerspace.stsci.edu/download/thumbnails/94962889/dialog_dl_table.png?version=1&modificationDate=1615209483551&api=v2)
_This dialog box is launched when the user selects 'Export Table' after formulating a search._

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data)  
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
**On this page:**
* 1[The Advanced Search Window](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-TheAdvancedSearchWindow)
* 2[Applied Filters Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-AppliedFiltersPanel)
* 3[Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-SearchParameters)
* 3.1[Columns Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-ColumnsPanel)
* 3.2[Filters Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-FiltersPanelFiltersPanel)
* 3.2.1[Enumerated Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-EnumeratedFilters)
* 3.2.2[Text Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-TextFilters)
* 3.2.3[Filter Ranges](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-FilterRanges)
* 3.3[Available Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-AvailableFilters)
* 4[Executing a Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-ExecutingaSearch)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search#AdvancedSearch-ForFurtherReading...)

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "The Advanced Search Window"} -->
Advanced searches, using an expanded set of metadata, are provided for certain MAST data collections, including the default search of MAST Missions. Clicking the __Advanced Search__ link below the Portal target name/coordinates dialog box will bring up the MAST Advanced Search window, which is shown below.  
![](https://outerspace.stsci.edu/download/attachments/94962889/winndow_adv_search_ann.png?version=1&modificationDate=1615209483566&api=v2)  
The **Advanced Search****Window** consists of metadata filters which may be used to constrain the search results. The number of matches to observations with the applied filters is displayed (1: _top_), the **Applied Filters** panel displays the names and values (2: _second from top_), the available filter **Columns** panel (3: _lower left_), and the selected dialogs in the **Filters** **Panel** (4: _lower right_).

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Applied Filters Panel"} -->
![](https://outerspace.stsci.edu/download/attachments/94962889/panel_appliedFilters.png?version=1&modificationDate=1615209483554&api=v2)
Filters for which values or ranges have been applied are summarized in the Applied Filters Panel. Filters may be removed individually, or with the _**Clear All**_ button. Specific filters may be selected in the Columns Panel; values or ranges of values may be set in the individual Filter dialogs.
The term "filters" is, unfortunately, overloaded. Astronomers often think of filters as passband-limiting optical elements. In this context, filters are used to select a subset of available results using one or more criteria.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Search Parameters"} -->
The Advanced Search enables custom searches with a wider variety of criteria that may, but do not necessarily, include a target name or coordinates (as with [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search)). As criteria are applied, preliminary searches will be performed in the background to update the __Records Found__ count at the top of the window. This helps narrow the search to a manageable number of results.
The count of search results must be <50,000 to load the results into the MAST Portal, or <500,000 to download the results to a local file.
Search criteria are specified by:
* selecting one or more available filters in the _**Columns**_ panel, and
* specifying the values (or range of values) in the corresponding dialogs in the _**Filters**_ panel.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/panel_filterColumns.png?version=1&modificationDate=1615209483557&api=v2)
Click entries in the _**Columns Panel**_ to toggle whether a given filter appears (checked) or disappears (unchecked) in the _**Filters Panel**_. You may also restore the default filters or hide all of them by clicking the appropriate text at the top of the panel.
Type the name of a filter in the **Filter Columns** dialog to show (or limit) the filters that are displayed in the columns panel.
The column names shown in the panel (left) may be different, depending upon which collection is being searched.
Filters dialogs come in three flavors depending upon the type of parameter, as described below.

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel", "Header 3": "Enumerated Filters"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/filter_enum.png?version=1&modificationDate=1615209483560&api=v2)
Click one or more checkboxes to apply filters with enumerated values. If there are a large number of possible values (e.g., for instrument names), simply click the __Name__ text at the top-left of the filter panel to sort the values in alphabetical order. The desired value may also be typed into the dialog box at the top of the panel.
Typing part of a value (e.g., __HR__) will limit the number of enumerated values to those that contain that character sequence. Then just check the box to choose one.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel", "Header 3": "Text Filters"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/filter_text.png?version=1&modificationDate=1615209483562&api=v2)
Type in the text box and press "return" on your keyboard to apply a filter with a text value. Text values may contain a wildcard (asterisk) character.
Wildcard values may not be used in the __Object Name or Position__ filter.

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Columns Panel", "Header 3": "Filter Ranges"} -->
![](https://outerspace.stsci.edu/download/thumbnails/94962889/filtler_range.png?version=1&modificationDate=1615209483564&api=v2)
Use the sliders to constrain a range, or simply enter floating-point values into the text boxes. The value is applied after the mouse focus is changed.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Search Parameters", "Header 2": "Available Filters"} -->
About 30 filters are available for restricting search parameters. They map to user-accessible metadata in the MAST CAOM (Common Archive Observation Model) database.
Column Name | Field Type | Description
---|---|---
Object Name or Position | Text | Search for a given target name or coordinates, which is analogous to the primary search Portal search bar (see [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search)). The coordinates are assumed to be Equatorial in the ICRS reference frame (epoch J2000).
Observation Type | Enum | Restrict the search to 'science' or 'calibration' observing programs. Note that on-sky calibration exposures may have some science value.
Mission | Enum | Name or acronym for the mission that obtained the data. High-Level Science Products are collected in the 'HLSP' mission.
Provenance Name | Enum | Identifier of the software or team that produced the data. For HST and JWST mission data the mission corresponds to the calibration pipeline that produced the data.
Instrument | Enum | Acronym for the science instrument used to obtain the data.
Project | Enum | Similar to the 'Mission' field (identical in most cases) but reflects the originating mission, e.g. HST-based HLSPs will have 'HST' in this field.
Filters | Enum | Select one or more names of optical elements (i.e., filters, gratings).
Waveband | Enum | Designation of wavebands (broadly defined).
Target Name | Text | Target name or field as specified by the PI in the observing program.
Target Classification | Enum | Target classification in the STScI proposal database, such as 'STAR' or 'GALAXY'.
Sequence Number | Text | The meaning is specific to a missions, e.g. the Sector number for TESS observations.
Observation ID | Text | Search for a specific observation ID, or similar observation ID's using wildcards.
RA | Range | Specify a range of Right Ascension for the target position. Values are displayed in sexagesimal but can be entered in degrees.
Dec | Range | Specify a range of Declination for the target position Values are displayed in sexagesimal but can be entered in degrees.
Proposal ID | Text | Specify a proposal/program ID number. Wildcards are allowed.
Principal Investigator | Text | Filter on certain Principal Investigator names. Wildcards are advised.
Product Type | Enum | Specify certain data product types, such as 'image' or 'spectrum'.
Calibration Level | Enum | Filter on numerical calibration levels assigned to observations. High-Level Science Product (HLSP) data are designated Level 4, while planned-but-not-executed observations are Level –1. The meaning of a level is mission-specific.
Start Time | Range | Specify a range of start date-times (in UTC) for the matched exposures.
End Time | Range | Specify a range of end date-times (in UTC) for the matched exposures.
Exposure Length | Range | Specify a range of exposure duration in seconds.
Min. Wavelength | Range | Specify a range of lower-bound wavelengths in nm.
Max. Wavelength | Range | Specify a range of upper-bound wavelengths in nm.
Observation Title | Text | Filter on specific proposal titles. Wildcards are advised.
Release Date | Range | Specify a range of data release dates (i.e., when the data become public). For Exclusive Access data, this date may be in the future.
Proposal Type | Enum | Filter on specific proposal types, such as 'GO' or 'SNAP'. The appropriate types will vary by mission.
Data Rights | Enum | Filter for 'PUBLIC' or 'EXCLUSIVE_ACCESS' data permissions (or 'PROPRIETARY' but this is being phased out going forward).
Moving Target | Enum | Use this boolean flag to filter moving targets.
Product Group ID | Text | Filter on product group ID's from MAST databases.
Object ID | Text | Filter on object ID's from MAST databases.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Executing a Search"} -->
After adding the desired search parameters, there are two options to inspect the matching observations.  
![](https://outerspace.stsci.edu/download/thumbnails/94962889/button_search.png?version=1&modificationDate=1615209483547&api=v2) | Click the **Search** button to load the search results into a tab in the MAST Portal. The 'Records Found' count must be under 50,000 for this option to become available.
---|---
![](https://outerspace.stsci.edu/download/thumbnails/94962889/button_export_table.png?version=1&modificationDate=1615209483541&api=v2) | Click the **Export Table** button to download the table of search results as a file (CSV, VO Table, or JSON). This will work with search result counts up to 500,000.
![](https://outerspace.stsci.edu/download/thumbnails/94962889/dialog_dl_table.png?version=1&modificationDate=1615209483551&api=v2)
_This dialog box is launched when the user selects 'Export Table' after formulating a search._

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 21 END -->

