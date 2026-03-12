---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search"
date_accessed: "2026-03-11T11:36:27.639089"
---

<!-- CHUNK 1 START -->
The [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) is a web application that can search for data products from any hosted mission, including JWST. The [MAST Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide) provides step-by-step instructions for [most searches](https://outerspace.stsci.edu/display/MASTDOCS/Searching). This page reviews basic searches, and describes in more detail JWST-specific searches.  
**On this page...**
* 1[Context](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-Context)
* 2[Search by Object Name or Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchbyObjectNameorCoordinates)
* 2.1[Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-AdvancedSearch)
* 2.2[Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchResults)
* 3[Search by JWST Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords)
* 3.1[Example Search by Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-ExampleSearchbyKeywords)
* 4[Search for Wavefront Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchforWavefrontProducts)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Context"} -->
Any search with the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) requires first specifying the collection over which to search. Select the collection with the drop-down menu at the top-left of the [Portal interface](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962827/Field+Guide+to+the+Portal):
![](https://outerspace.stsci.edu/download/thumbnails/113771354/menu_selectCollection_obs.png?version=1&modificationDate=1660679425459&api=v2)
See the _Selecting Collections_ section of the [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) chapter in the Portal Guide for an explanation of the various collections.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Search by Object Name or Coordinates"} -->
The most common search in MAST is to specify either an object name, or a location on the sky in equatorial coordinates. See the [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) chapter in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) to view the accepted formats for target names and for coordinate syntax. In brief, after selecting the collection:  
1. Enter a target name or coordinates into the dialog: ![](https://outerspace.stsci.edu/download/thumbnails/113771354/enter_target.png?version=1&modificationDate=1657043882758&api=v2)MAST Portal target/position dialog box
2. Click the Search button: ![](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search_1.png?version=1&modificationDate=1657043882715&api=v2)  
Note that you may want to specify a search radius in the dialog (e.g. "`ngc2024 r=1m`") if the default of 0.2° returns too many results.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Search by Object Name or Coordinates", "Header 2": "Advanced Search"} -->
Wide-field Slitless Spectroscopy, performed by NIRISS and NIRCAM, produces an extraordinary number of search results (mostly extracted spectra). Use caution when searching for these results in the Portal, as it may result in time-out issues. Instead, the [MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs) offers a more reliable way to to get the data; see the
An _**advanced search**_ is really an elaboration on the basic search by name or position, but provides 30 additional attributes for a finer-grained selection. In brief, after selecting the collection  
1. Click the __Advanced Search__ link, which brings up a new window (see the [Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search) article in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide))
2. Select the filter columns of interest
3. Fill in the dialog boxes (or select enumerated values) in each filter of interest
4. Execute the search ![](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search.png?version=1&modificationDate=1660681478658&api=v2)  
An advanced search is a good choice if, e.g., you want to find data for a particular JWST program: select `JWST` in the Mission filter, and enter the 5-character program number in the Proposal ID filter.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Search by Object Name or Coordinates", "Header 2": "Search Results"} -->
After a successful search the Portal returns a table of matches to **_Observations._** Each match appears as a row in a table, and each row represents multiple data products. See the layout in Figure 1 of the [Field Guide to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962827/Field+Guide+to+the+Portal) chapter of the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide).

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Search by JWST Instrument Keywords"} -->
The JWST Instrument Keyword search will select files that match header keyword values (or ranges of values). See the [JWST Keyword Dictionary](https://mast.stsci.edu/portal/Mashup/Clients/jwkeywords/index.html) for a complete list of the scores of available keywords for each instrument.
Only the highest-level products will be returned
The keyword search results table includes only the **highest-level** **FITS** products that were produced. That is, it will **not include** Level-1b files if a corresponding Level-2 file was created, although it will still show Level-2b files if a corresponding Level-3 file was created. It will **not** show non-FITS science products such as source catalogs in any case. To retrieve lower-level products, use the [Portal Search for Observations](https://outerspace.stsci.edu/display/JARI/JWST+Archive%3A+Portal+Search+for+Observations).
A brief description about the JWST data product levels can be found in the [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) article; see also the

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Search by JWST Instrument Keywords", "Header 2": "Example Search by Keywords"} -->
Follow the instructions below to search by specific keyword values. This example shows how to search for NIRCam observations in the `F070W` filter for JWST Program 1063, and then refine the results to display only those files from Observation 100.  
| Instruction | Notes
---|---|---
1 | Select '_JWST Instrument Keywords'_ from the**Select a collection…** | ![](https://outerspace.stsci.edu/download/thumbnails/113771354/menu_selectCollection_SIkw.png?version=1&modificationDate=1660916376803&api=v2)
2 |  Select an instrument (in this example, _Nircam)_ from the**Instrument** You can also select 'All Instruments' and further refine results in step **4.** | ![MAST Portal instrument pull-down menu for JWST keyword search](https://outerspace.stsci.edu/download/thumbnails/113771354/select_NIRCam.png?version=1&modificationDate=1671557227531&api=v2)MAST Portal instrument pull-down menu for JWST keyword search
3 | Click the**Advanced Search** | ![Advanced search button](https://outerspace.stsci.edu/download/attachments/113771354/advanced_search_button.png?version=1&modificationDate=1657043885948&api=v2)Advanced search button
4 |  Select parameters or ranges for one or more filter menus to limit or expand the search. For instance, specify the JWST Program ID in the **Proposal ID** panel and tick the filter name (in this example, `F070W`) in the Filter panel. If you selected 'All Instruments' in step **2** , you can use the 'instrument' filter to refine results down to NIRCam at this stage. |  ![Filtering by proposal ID, in this case 1063](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_PID_1063.png?version=1&modificationDate=1657044538508&api=v2)Filtering by proposal ID ![Limiting results based on filters used, in this case F070W](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_filt_F070W.png?version=1&modificationDate=1657044538351&api=v2)Limiting results based on filters used
5 | Now click the**Search****Advanced Search** window.  | ![](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search.png?version=1&modificationDate=1660681478658&api=v2)
6 |  Evaluate the search results grid (i.e., the table of matching rows). ![Search results grid](https://outerspace.stsci.edu/download/attachments/113771354/results_PID_1063_v2.png?version=1&modificationDate=1660856840357&api=v2)Search results grid
7 | _Optional_**:**![](https://outerspace.stsci.edu/download/thumbnails/113771354/icon_info_b.png?version=1&modificationDate=1657043883500&api=v2) in a table row for additional details about that file. | ![File metadata information](https://outerspace.stsci.edu/download/attachments/113771354/results_info.png?version=1&modificationDate=1657044538613&api=v2)File metadata information
8 |  **_Optional_ :****Filters****Observation** **100**) are applied, the results table will display observations that match those selections. | ![Options for filtering the results table](https://outerspace.stsci.edu/download/attachments/113771354/filter_observtn_100.png?version=1&modificationDate=1657046048114&api=v2)Options for filtering the results table
9 | **_Optional_ :** Click the**Edit Columns** | ![Edit columns button](https://outerspace.stsci.edu/download/thumbnails/113771354/button_editColumns.png?version=1&modificationDate=1657043882506&api=v2)Edit columns button
* * *

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Search for Wavefront Products"} -->
JWST's primary mirror (the Optical Telescope Element, OTE) has eighteen individual segments. To enable the segments to act like one large primary mirror and to have their wavefronts match correctly, the initial best on-orbit alignment is established during JWST commissioning, and periodically thereafter. Wavefront sensing results include Optical Path Difference (OPD) files, which are available in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). It is possible to use these files with mission software (Webb PSF) to evaluate the quality of the imaging for an instrument and aperture of interest.
Bring up the [Portal interface](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) and follow the steps below:  
| Instruction | Notes
---|---|---
1 |  Select '__JWST WSS__ ' from the '**Select a collection…** ’ pull-down menu on the upper-left. _WSS_ refers to the Wavefront Sensing Software subsystem for JWST. |  ![MAST Portal collection pull-down menu](https://outerspace.stsci.edu/download/thumbnails/113771354/menu_selectCollection_WSS.png?version=1&modificationDate=1660916072053&api=v2)MAST Portal collection pull-down menu  
2 | Click the **Advanced Search** box to the right. | ![Advanced search button](https://outerspace.stsci.edu/download/thumbnails/113771354/advanced_search_button.png?version=1&modificationDate=1657043885948&api=v2)Advanced search button
3 |  Select parameter values for one or more filter menus to restrict the search. **Note:** wildcards are allowed in text boxes. | ![](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_wss.png?version=1&modificationDate=1657046442538&api=v2)
4 | Click the **Search** button in the upper-left of the window. | ![Search button](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search.png?version=1&modificationDate=1660681478658&api=v2)Search button
5 | **_Optional_** : Down-select results in the grid using one or more of the Filters to the left of the results table, which when applied will display only the matching observations.
| ![](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_correctionid.png?version=1&modificationDate=1657046462920&api=v2)
6 |  Download the products by:
* selecting a single entry in the results table, then clicking the file icon, or
* placing in portal basket, then bringing up the download manager  
See [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval) article for more details about downloading data. |  ![](https://outerspace.stsci.edu/download/thumbnails/113771354/icon_file_white.png?version=1&modificationDate=1657043883360&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/113771354/icon_downloadBasket.png?version=1&modificationDate=1657043883374&api=v2)

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Data Holdings](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963702/MAST+Data+Holdings+Home)
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
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
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search "Data Search")
* [Data Visualization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771401/Data+Visualization "Data Visualization")
* [Data Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection "Data Selection")
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval "Data Retrieval")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
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
* [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search "Data Search")
* [Data Visualization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771401/Data+Visualization "Data Visualization")
* [Data Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection "Data Selection")
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval "Data Retrieval")
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
The [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) is a web application that can search for data products from any hosted mission, including JWST. The [MAST Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide) provides step-by-step instructions for [most searches](https://outerspace.stsci.edu/display/MASTDOCS/Searching). This page reviews basic searches, and describes in more detail JWST-specific searches.  
**On this page...**
* 1[Context](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-Context)
* 2[Search by Object Name or Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchbyObjectNameorCoordinates)
* 2.1[Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-AdvancedSearch)
* 2.2[Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchResults)
* 3[Search by JWST Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords)
* 3.1[Example Search by Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-ExampleSearchbyKeywords)
* 4[Search for Wavefront Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-SearchforWavefrontProducts)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search#DataSearch-ForFurtherReading...)

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Context"} -->
Any search with the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) requires first specifying the collection over which to search. Select the collection with the drop-down menu at the top-left of the [Portal interface](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962827/Field+Guide+to+the+Portal):
![](https://outerspace.stsci.edu/download/thumbnails/113771354/menu_selectCollection_obs.png?version=1&modificationDate=1660679425459&api=v2)
See the _Selecting Collections_ section of the [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) chapter in the Portal Guide for an explanation of the various collections.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Search by Object Name or Coordinates"} -->
The most common search in MAST is to specify either an object name, or a location on the sky in equatorial coordinates. See the [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) chapter in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) to view the accepted formats for target names and for coordinate syntax. In brief, after selecting the collection:  
1. Enter a target name or coordinates into the dialog: ![](https://outerspace.stsci.edu/download/thumbnails/113771354/enter_target.png?version=1&modificationDate=1657043882758&api=v2)MAST Portal target/position dialog box
2. Click the Search button: ![](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search_1.png?version=1&modificationDate=1657043882715&api=v2)  
Note that you may want to specify a search radius in the dialog (e.g. "`ngc2024 r=1m`") if the default of 0.2° returns too many results.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Search by Object Name or Coordinates", "Header 2": "Advanced Search"} -->
Wide-field Slitless Spectroscopy, performed by NIRISS and NIRCAM, produces an extraordinary number of search results (mostly extracted spectra). Use caution when searching for these results in the Portal, as it may result in time-out issues. Instead, the [MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs) offers a more reliable way to to get the data; see the
An _**advanced search**_ is really an elaboration on the basic search by name or position, but provides 30 additional attributes for a finer-grained selection. In brief, after selecting the collection  
1. Click the __Advanced Search__ link, which brings up a new window (see the [Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search) article in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide))
2. Select the filter columns of interest
3. Fill in the dialog boxes (or select enumerated values) in each filter of interest
4. Execute the search ![](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search.png?version=1&modificationDate=1660681478658&api=v2)  
An advanced search is a good choice if, e.g., you want to find data for a particular JWST program: select `JWST` in the Mission filter, and enter the 5-character program number in the Proposal ID filter.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Search by Object Name or Coordinates", "Header 2": "Search Results"} -->
After a successful search the Portal returns a table of matches to **_Observations._** Each match appears as a row in a table, and each row represents multiple data products. See the layout in Figure 1 of the [Field Guide to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962827/Field+Guide+to+the+Portal) chapter of the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide).

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Search by JWST Instrument Keywords"} -->
The JWST Instrument Keyword search will select files that match header keyword values (or ranges of values). See the [JWST Keyword Dictionary](https://mast.stsci.edu/portal/Mashup/Clients/jwkeywords/index.html) for a complete list of the scores of available keywords for each instrument.
Only the highest-level products will be returned
The keyword search results table includes only the **highest-level** **FITS** products that were produced. That is, it will **not include** Level-1b files if a corresponding Level-2 file was created, although it will still show Level-2b files if a corresponding Level-3 file was created. It will **not** show non-FITS science products such as source catalogs in any case. To retrieve lower-level products, use the [Portal Search for Observations](https://outerspace.stsci.edu/display/JARI/JWST+Archive%3A+Portal+Search+for+Observations).
A brief description about the JWST data product levels can be found in the [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) article; see also the

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Search by JWST Instrument Keywords", "Header 2": "Example Search by Keywords"} -->
Follow the instructions below to search by specific keyword values. This example shows how to search for NIRCam observations in the `F070W` filter for JWST Program 1063, and then refine the results to display only those files from Observation 100.  
| Instruction | Notes
---|---|---
1 | Select '_JWST Instrument Keywords'_ from the**Select a collection…** | ![](https://outerspace.stsci.edu/download/thumbnails/113771354/menu_selectCollection_SIkw.png?version=1&modificationDate=1660916376803&api=v2)
2 |  Select an instrument (in this example, _Nircam)_ from the**Instrument** You can also select 'All Instruments' and further refine results in step **4.** | ![MAST Portal instrument pull-down menu for JWST keyword search](https://outerspace.stsci.edu/download/thumbnails/113771354/select_NIRCam.png?version=1&modificationDate=1671557227531&api=v2)MAST Portal instrument pull-down menu for JWST keyword search
3 | Click the**Advanced Search** | ![Advanced search button](https://outerspace.stsci.edu/download/attachments/113771354/advanced_search_button.png?version=1&modificationDate=1657043885948&api=v2)Advanced search button
4 |  Select parameters or ranges for one or more filter menus to limit or expand the search. For instance, specify the JWST Program ID in the **Proposal ID** panel and tick the filter name (in this example, `F070W`) in the Filter panel. If you selected 'All Instruments' in step **2** , you can use the 'instrument' filter to refine results down to NIRCam at this stage. |  ![Filtering by proposal ID, in this case 1063](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_PID_1063.png?version=1&modificationDate=1657044538508&api=v2)Filtering by proposal ID ![Limiting results based on filters used, in this case F070W](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_filt_F070W.png?version=1&modificationDate=1657044538351&api=v2)Limiting results based on filters used
5 | Now click the**Search****Advanced Search** window.  | ![](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search.png?version=1&modificationDate=1660681478658&api=v2)
6 |  Evaluate the search results grid (i.e., the table of matching rows). ![Search results grid](https://outerspace.stsci.edu/download/attachments/113771354/results_PID_1063_v2.png?version=1&modificationDate=1660856840357&api=v2)Search results grid
7 | _Optional_**:**![](https://outerspace.stsci.edu/download/thumbnails/113771354/icon_info_b.png?version=1&modificationDate=1657043883500&api=v2) in a table row for additional details about that file. | ![File metadata information](https://outerspace.stsci.edu/download/attachments/113771354/results_info.png?version=1&modificationDate=1657044538613&api=v2)File metadata information
8 |  **_Optional_ :****Filters****Observation** **100**) are applied, the results table will display observations that match those selections. | ![Options for filtering the results table](https://outerspace.stsci.edu/download/attachments/113771354/filter_observtn_100.png?version=1&modificationDate=1657046048114&api=v2)Options for filtering the results table
9 | **_Optional_ :** Click the**Edit Columns** | ![Edit columns button](https://outerspace.stsci.edu/download/thumbnails/113771354/button_editColumns.png?version=1&modificationDate=1657043882506&api=v2)Edit columns button
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Search for Wavefront Products"} -->
JWST's primary mirror (the Optical Telescope Element, OTE) has eighteen individual segments. To enable the segments to act like one large primary mirror and to have their wavefronts match correctly, the initial best on-orbit alignment is established during JWST commissioning, and periodically thereafter. Wavefront sensing results include Optical Path Difference (OPD) files, which are available in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). It is possible to use these files with mission software (Webb PSF) to evaluate the quality of the imaging for an instrument and aperture of interest.
Bring up the [Portal interface](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) and follow the steps below:  
| Instruction | Notes
---|---|---
1 |  Select '__JWST WSS__ ' from the '**Select a collection…** ’ pull-down menu on the upper-left. _WSS_ refers to the Wavefront Sensing Software subsystem for JWST. |  ![MAST Portal collection pull-down menu](https://outerspace.stsci.edu/download/thumbnails/113771354/menu_selectCollection_WSS.png?version=1&modificationDate=1660916072053&api=v2)MAST Portal collection pull-down menu  
2 | Click the **Advanced Search** box to the right. | ![Advanced search button](https://outerspace.stsci.edu/download/thumbnails/113771354/advanced_search_button.png?version=1&modificationDate=1657043885948&api=v2)Advanced search button
3 |  Select parameter values for one or more filter menus to restrict the search. **Note:** wildcards are allowed in text boxes. | ![](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_wss.png?version=1&modificationDate=1657046442538&api=v2)
4 | Click the **Search** button in the upper-left of the window. | ![Search button](https://outerspace.stsci.edu/download/thumbnails/113771354/button_search.png?version=1&modificationDate=1660681478658&api=v2)Search button
5 | **_Optional_** : Down-select results in the grid using one or more of the Filters to the left of the results table, which when applied will display only the matching observations.
| ![](https://outerspace.stsci.edu/download/thumbnails/113771354/filter_correctionid.png?version=1&modificationDate=1657046462920&api=v2)
6 |  Download the products by:
* selecting a single entry in the results table, then clicking the file icon, or
* placing in portal basket, then bringing up the download manager  
See [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval) article for more details about downloading data. |  ![](https://outerspace.stsci.edu/download/thumbnails/113771354/icon_file_white.png?version=1&modificationDate=1657043883360&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/113771354/icon_downloadBasket.png?version=1&modificationDate=1657043883374&api=v2)

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Data Holdings](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963702/MAST+Data+Holdings+Home)
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

