---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA"
date_accessed: "2026-03-11T11:36:04.317455"
---

<!-- CHUNK 1 START -->
You may access and retrieve data from the Roman Integration and Test Archive (RITA) using the CaSSI web tool, or with curl commands.
**On this page...**
* 1[Roman Ground Tests](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-RomanGroundTests)
* 2[CaSSI Interface](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-CaSSIInterface)
* 2.1[Provenance](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Provenance)
* 2.2[General Attribute Selectors](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-GeneralAttributeSelectors)
* 2.3[Optional Attribute Selectors](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-OptionalAttributeSelectors)
* 2.4[Display Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-DisplayFields)
* 2.5[Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Results)
* 3[RITA Common Terms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-RITACommonTerms)
* 4[API for RITA](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-APIforRITA)
* 4.1[Query](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Query)
* 4.2[Retrieve](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Retrieve)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Roman Ground Tests"} -->
Roman science Instruments were tested prior to launch for functionality and to characterize the detector response. (See, e.g., the summary of [WFI Ground Testing Campaigns](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns).) The data from these tests have been stored in the Roman Integration and Test Archive (RITA) to support the generation of calibration reference files, and to provide a baseline for post-launch instrument performance.
Downloads of the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to access these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.
Data products from ground tests have not yet been fully deployed to the Operations environment. Until all products are made available, the RITA interface will function but searches will return incomplete results.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface"} -->
The MAST CaSSI web interface includes a [RITA search form](https://mast.stsci.edu/cassi/#/roman) for data obtained during pre-launch ground testing, including epochs of Thermal Vacuum (TVac) testing. The RITA web interface is shown in Fig. 1.  
![](https://outerspace.stsci.edu/download/attachments/282168349/window_cassi_romanRita.png?version=3&modificationDate=1749580946581&api=v2)
**Figure 1.** MAST CaSSI interface for Roman Integration & Test Archive (RITA), with regions (_numbered yellow boxes_) showing the provenance selectors (1), general attribute selectors (2, 3), optional attribute selectors (4), and display fields for the results table (5). The selectors in box 3 are not relevant for FPS testing, and do not appear for that provenance.
Most elements of the interface (pull-down menus, checkboxes, buttons) are similar to those in other MAST web interfaces (see the [Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide)). Features specific to RITA are summarized in subsections below, followed by definitions of some common acronyms.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Provenance"} -->
Data in RITA were obtained during multiple ground-tests in thermal-vacuum (TVAC). These data will be ingested into RITA over time, and offered in RITA as they become available. The provenance is labelled as in the following table. The provenance links will take you to descriptions of the TVAC campaigns.
Provenance | Description
---|---
[FPS](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-FPS) | Tests of the **F** ocal-**P** lane **S** ystem in TVAC, prior to instrument integration
WFI [TVAC 1](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-TVAC1) |  **T** hermal **VAC** uum test 1, with the fully assembled WFI instrument
WFI [TVAC 2](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-TVAC2) |  **T** hermal **VAC** uum test 2, with the fully assembled WFI instrument
[SCIPA](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-SCIPA) | Tests of WFI in TVAC, after integration with the **S** pace**C** raft +**I** ntegrated **P** ayload **A** ssembly

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors"} -->
Attributes of the test data may be used to narrow your search to products of interest. Not specifying an attribute has the effect of matching all products with respect to that attribute (e.g., an unspecified Detector name will match all detectors).

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors", "Header 3": "Dates"} -->
If the date when the data were generated is known approximately, the start/end date selectors will limit the scope of the search. For reference, the dates of the ground tests are given below.
Test | Start date | End date
---|---|---
TVAC 1 | 2023-09-11 | 2023-11-11
TVAC 2 | 2024-03-18 | 2024-05-30

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors", "Header 3": "Name of the Ground Test"} -->
Exposures were obtained to support the various test activities. For a summary see [TVAC Flash Cards](https://innerspace.stsci.edu/display/RI/TVAC+Flash+Cards).

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors", "Header 3": "Optical Elements and Calibration Source"} -->
One or more of the [WFI Optical Elements](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/wfi-optical-elements) may be selected from the pull-down menu (see the [Spectral Element widget description](https://outerspace.stsci.edu/display/MASTDOCS/Core+Search+Parameters#CoreSearchParameters-comp_spec_elemSpectralElement)). You may also select whether the Relative Calibration System ([RCS](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/description-of-wfi#DescriptionofWFI-RelativeCalibrationSystem\(RCS\)sRCS)) was on during the exposure, and whether an apparent point-source was generated with the SORC.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Optional Attribute Selectors"} -->
Most all metadata (each of which corresponds to an output table column) can be used to further constrain the search. Select the column name from the pull-down menu and apply a condition (i.e., a constraint), as show in the article on [Additional Search Parameters](https://outerspace.stsci.edu/display/MASTDOCS/Additional+Search+Parameters#AdditionalSearchParameters-AddConditionOverview). The example below shows how to select only data where the exposure type matches the string `WFI_IMAGE`.
![](https://outerspace.stsci.edu/download/attachments/282168349/constraint_cassi.png?version=1&modificationDate=1734038885100&api=v2)

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Display Fields"} -->
Use the pull-down menu (shown in box 5 of [Fig. 1](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-rita_fig1)) to select which metadata (fields) to display in the results table. There are buttons to select recommended fields, all (![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_selectAll.png?version=1&modificationDate=1743769684976&api=v2)), or none (![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_selectNone.png?version=1&modificationDate=1743769718583&api=v2)). Fig. 2 highlights the Exposure Type field, which may be selected.  
![](https://outerspace.stsci.edu/download/attachments/282168349/menu_ritaFields.png?version=1&modificationDate=1734103355780&api=v2)
**Figure 2.** Expansion of pull-down menu (from box 5 of [Fig. 1](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-rita_fig1)) of display fields, highlighting the Exposure Type (_orange_) which can be added by ticking the checkbox. A short description is displayed beneath each field.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Results"} -->
A successful search will be displayed as a table, shown in Fig. 3, with one row per matching product. The Search Results Page article describes general features of the search results table, including selecting files for download. Fig. 3 below shows a somewhat simplified pull-down menu for download, since the results table for RITA is simply a list of files, rather than a list of collections of files.  
![](https://outerspace.stsci.edu/download/attachments/282168349/window_cassiResultsTab.png?version=1&modificationDate=1734106113910&api=v2)
**Figure 3.** Table of matching products, one per row. Products selected for download are marked with checkboxes (_left_) and are highlighted with a blue background. The pull-down menu for **Download Data** (_upper left_) is also shown, which offers a choice of download options.
See the

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "RITA Common Terms"} -->
The following terms are important for creating meaningful queries for TVac data. Some of the instrument components are visible in the [Description of WFI](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/description-of-wfi). See the [Roman acronym list](https://innerspace.stsci.edu/display/ROMAN/Roman+Acronyms+List) for more definitions.
Term/Acronym | Description
---|---
COBA | Cold Optical Baffle Assembly
EWA | Element Wheel Assembly
LLTF | Laser Line Tunable Filter
RCS | Relative Calibration System
SCA | Sensor Chip Assembly
SCE | Sensor Control Electronics
SDS | Source Delivery System
SORC | Stimulus of Ray Cones (used to simulate a point-source in the test data)
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "API for RITA"} -->
A simplified python interface for RITA is planned. For now, you may download from CaSSI and use curl scripts to query for products, and to retrieve them. The query scripts can be adapted from those that are available in the CaSSI web interface. The tables below shows the button/menu options that generate the queries, and the corresponding curl commands. (Backslash characters have been inserted into the example commands in the tables below to make them more readable.) Simply run the queries on the command line to generatae

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "API for RITA", "Header 2": "Query"} -->
You may delete the limit of 5000 results (_bolded text_) from the search command, but be aware that larger queries may take a long time to produce results. The result will be a json-formatted file of results: one for each row of the results table that would be generated after a search of RITA.
Widget | Command
---|---
![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_apiQuery.png?version=1&modificationDate=1734032213165&api=v2) |  **Search** curl -H "Content-Type: application/json" \ -X POST '<https://mast.stsci.edu/cassi/api/v0.1/rita/search/TVAC1>' \ -d '{"select_cols":[],"conditions":[{"rcs_on":"T"},{"gsorc_sds_sorc_on":"T"}]**,"limit":5000**}' \ --compressed \ --output cassi_rita_filtered_search_results2024-12-12T20:10:13.936Z.json

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "API for RITA", "Header 2": "Retrieve"} -->
You may also retrieve data using curl, as illustrated below. Note that your MAST authorization token is read from the shell environment variable **`MAST_API_TOKEN`**(see bolded text). The token is necessary to assure that you are authorized to retrieve products from RITA. To generate a token, see the[Auth.MAST](https://auth.mast.stsci.edu/info) page.
Widget | Command
---|---
![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_apiScript_download.png?version=1&modificationDate=1734032506615&api=v2) |  **Retrieve** curl -H "Content-Type: application/json" \ -H "**Authorization: token $MAST_API_TOKEN** " \ -X POST '<https://mast.stsci.edu/cassi/api/v0.1/download/roman/rita>'\ -d '{"query_params":["<https://pl9dmsdaapi.stsci.edu/api/assets/v1/mast/rita/product/TVAC1_COLDQUAL_WFIFIN_20231008003314_WFI18_uncal.asdf>"]}' \ --compressed \ --output TVAC1_COLDQUAL_WFIFIN_20231008003314_WFI18_uncal.asdf.zip curl -H "Content-Type: application/json"\ -H "**Authorization: token $MAST_API_TOKEN** " \ -X POST '<https://mast.stsci.edu/cassi/api/v0.1/download/roman/rita>' \ -d '{"query_params":["<https://pl9dmsdaapi.stsci.edu/api/assets/v1/mast/rita/product/TVAC1_NOMOPS_WFIFIN_20231015132524_WFI05_uncal.asdf>"]}' \ --compressed \ --output TVAC1_NOMOPS_WFIFIN_20231015132524_WFI05_uncal.asdf.zip  
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [RITA search](https://mast.stsci.edu/cassi/#/roman?dataGroup=RITA)
* [CaSSI.MAST API](https://mast.stsci.edu/cassi/docs/index.html)
* [WFI Ground Testing Campaigns](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns)
* [Summary table](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-Testing-summary-table) of the ground testing campaigns
* [Description of WFI](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/description-of-wfi)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [JWST Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products "JWST Supplemental Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [RITA](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA "RITA")
* [RomanCal Refererence Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products "RomanCal Refererence Products")
* [Roman Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products "Roman Supplemental Products")
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
You may access and retrieve data from the Roman Integration and Test Archive (RITA) using the CaSSI web tool, or with curl commands.
**On this page...**
* 1[Roman Ground Tests](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-RomanGroundTests)
* 2[CaSSI Interface](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-CaSSIInterface)
* 2.1[Provenance](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Provenance)
* 2.2[General Attribute Selectors](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-GeneralAttributeSelectors)
* 2.3[Optional Attribute Selectors](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-OptionalAttributeSelectors)
* 2.4[Display Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-DisplayFields)
* 2.5[Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Results)
* 3[RITA Common Terms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-RITACommonTerms)
* 4[API for RITA](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-APIforRITA)
* 4.1[Query](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Query)
* 4.2[Retrieve](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-Retrieve)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-ForFurtherReading...)

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Roman Ground Tests"} -->
Roman science Instruments were tested prior to launch for functionality and to characterize the detector response. (See, e.g., the summary of [WFI Ground Testing Campaigns](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns).) The data from these tests have been stored in the Roman Integration and Test Archive (RITA) to support the generation of calibration reference files, and to provide a baseline for post-launch instrument performance.
Downloads of the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to access these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.
Data products from ground tests have not yet been fully deployed to the Operations environment. Until all products are made available, the RITA interface will function but searches will return incomplete results.

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface"} -->
The MAST CaSSI web interface includes a [RITA search form](https://mast.stsci.edu/cassi/#/roman) for data obtained during pre-launch ground testing, including epochs of Thermal Vacuum (TVac) testing. The RITA web interface is shown in Fig. 1.  
![](https://outerspace.stsci.edu/download/attachments/282168349/window_cassi_romanRita.png?version=3&modificationDate=1749580946581&api=v2)
**Figure 1.** MAST CaSSI interface for Roman Integration & Test Archive (RITA), with regions (_numbered yellow boxes_) showing the provenance selectors (1), general attribute selectors (2, 3), optional attribute selectors (4), and display fields for the results table (5). The selectors in box 3 are not relevant for FPS testing, and do not appear for that provenance.
Most elements of the interface (pull-down menus, checkboxes, buttons) are similar to those in other MAST web interfaces (see the [Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide)). Features specific to RITA are summarized in subsections below, followed by definitions of some common acronyms.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Provenance"} -->
Data in RITA were obtained during multiple ground-tests in thermal-vacuum (TVAC). These data will be ingested into RITA over time, and offered in RITA as they become available. The provenance is labelled as in the following table. The provenance links will take you to descriptions of the TVAC campaigns.
Provenance | Description
---|---
[FPS](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-FPS) | Tests of the **F** ocal-**P** lane **S** ystem in TVAC, prior to instrument integration
WFI [TVAC 1](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-TVAC1) |  **T** hermal **VAC** uum test 1, with the fully assembled WFI instrument
WFI [TVAC 2](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-TVAC2) |  **T** hermal **VAC** uum test 2, with the fully assembled WFI instrument
[SCIPA](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-SCIPA) | Tests of WFI in TVAC, after integration with the **S** pace**C** raft +**I** ntegrated **P** ayload **A** ssembly

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors"} -->
Attributes of the test data may be used to narrow your search to products of interest. Not specifying an attribute has the effect of matching all products with respect to that attribute (e.g., an unspecified Detector name will match all detectors).

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors", "Header 3": "Dates"} -->
If the date when the data were generated is known approximately, the start/end date selectors will limit the scope of the search. For reference, the dates of the ground tests are given below.
Test | Start date | End date
---|---|---
TVAC 1 | 2023-09-11 | 2023-11-11
TVAC 2 | 2024-03-18 | 2024-05-30

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors", "Header 3": "Name of the Ground Test"} -->
Exposures were obtained to support the various test activities. For a summary see [TVAC Flash Cards](https://innerspace.stsci.edu/display/RI/TVAC+Flash+Cards).

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "General Attribute Selectors", "Header 3": "Optical Elements and Calibration Source"} -->
One or more of the [WFI Optical Elements](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/wfi-optical-elements) may be selected from the pull-down menu (see the [Spectral Element widget description](https://outerspace.stsci.edu/display/MASTDOCS/Core+Search+Parameters#CoreSearchParameters-comp_spec_elemSpectralElement)). You may also select whether the Relative Calibration System ([RCS](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/description-of-wfi#DescriptionofWFI-RelativeCalibrationSystem\(RCS\)sRCS)) was on during the exposure, and whether an apparent point-source was generated with the SORC.

<!-- CHUNK 23 END -->

<!-- CHUNK 24 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Optional Attribute Selectors"} -->
Most all metadata (each of which corresponds to an output table column) can be used to further constrain the search. Select the column name from the pull-down menu and apply a condition (i.e., a constraint), as show in the article on [Additional Search Parameters](https://outerspace.stsci.edu/display/MASTDOCS/Additional+Search+Parameters#AdditionalSearchParameters-AddConditionOverview). The example below shows how to select only data where the exposure type matches the string `WFI_IMAGE`.
![](https://outerspace.stsci.edu/download/attachments/282168349/constraint_cassi.png?version=1&modificationDate=1734038885100&api=v2)

<!-- CHUNK 24 END -->

<!-- CHUNK 25 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Display Fields"} -->
Use the pull-down menu (shown in box 5 of [Fig. 1](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-rita_fig1)) to select which metadata (fields) to display in the results table. There are buttons to select recommended fields, all (![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_selectAll.png?version=1&modificationDate=1743769684976&api=v2)), or none (![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_selectNone.png?version=1&modificationDate=1743769718583&api=v2)). Fig. 2 highlights the Exposure Type field, which may be selected.  
![](https://outerspace.stsci.edu/download/attachments/282168349/menu_ritaFields.png?version=1&modificationDate=1734103355780&api=v2)
**Figure 2.** Expansion of pull-down menu (from box 5 of [Fig. 1](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA#RITA-rita_fig1)) of display fields, highlighting the Exposure Type (_orange_) which can be added by ticking the checkbox. A short description is displayed beneath each field.

<!-- CHUNK 25 END -->

<!-- CHUNK 26 START -->
<!-- Metadata: {"Header 1": "CaSSI Interface", "Header 2": "Results"} -->
A successful search will be displayed as a table, shown in Fig. 3, with one row per matching product. The Search Results Page article describes general features of the search results table, including selecting files for download. Fig. 3 below shows a somewhat simplified pull-down menu for download, since the results table for RITA is simply a list of files, rather than a list of collections of files.  
![](https://outerspace.stsci.edu/download/attachments/282168349/window_cassiResultsTab.png?version=1&modificationDate=1734106113910&api=v2)
**Figure 3.** Table of matching products, one per row. Products selected for download are marked with checkboxes (_left_) and are highlighted with a blue background. The pull-down menu for **Download Data** (_upper left_) is also shown, which offers a choice of download options.
See the

<!-- CHUNK 26 END -->

<!-- CHUNK 27 START -->
<!-- Metadata: {"Header 1": "RITA Common Terms"} -->
The following terms are important for creating meaningful queries for TVac data. Some of the instrument components are visible in the [Description of WFI](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/description-of-wfi). See the [Roman acronym list](https://innerspace.stsci.edu/display/ROMAN/Roman+Acronyms+List) for more definitions.
Term/Acronym | Description
---|---
COBA | Cold Optical Baffle Assembly
EWA | Element Wheel Assembly
LLTF | Laser Line Tunable Filter
RCS | Relative Calibration System
SCA | Sensor Chip Assembly
SCE | Sensor Control Electronics
SDS | Source Delivery System
SORC | Stimulus of Ray Cones (used to simulate a point-source in the test data)
* * *

<!-- CHUNK 27 END -->

<!-- CHUNK 28 START -->
<!-- Metadata: {"Header 1": "API for RITA"} -->
A simplified python interface for RITA is planned. For now, you may download from CaSSI and use curl scripts to query for products, and to retrieve them. The query scripts can be adapted from those that are available in the CaSSI web interface. The tables below shows the button/menu options that generate the queries, and the corresponding curl commands. (Backslash characters have been inserted into the example commands in the tables below to make them more readable.) Simply run the queries on the command line to generatae

<!-- CHUNK 28 END -->

<!-- CHUNK 29 START -->
<!-- Metadata: {"Header 1": "API for RITA", "Header 2": "Query"} -->
You may delete the limit of 5000 results (_bolded text_) from the search command, but be aware that larger queries may take a long time to produce results. The result will be a json-formatted file of results: one for each row of the results table that would be generated after a search of RITA.
Widget | Command
---|---
![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_apiQuery.png?version=1&modificationDate=1734032213165&api=v2) |  **Search** curl -H "Content-Type: application/json" \ -X POST '<https://mast.stsci.edu/cassi/api/v0.1/rita/search/TVAC1>' \ -d '{"select_cols":[],"conditions":[{"rcs_on":"T"},{"gsorc_sds_sorc_on":"T"}]**,"limit":5000**}' \ --compressed \ --output cassi_rita_filtered_search_results2024-12-12T20:10:13.936Z.json

<!-- CHUNK 29 END -->

<!-- CHUNK 30 START -->
<!-- Metadata: {"Header 1": "API for RITA", "Header 2": "Retrieve"} -->
You may also retrieve data using curl, as illustrated below. Note that your MAST authorization token is read from the shell environment variable **`MAST_API_TOKEN`**(see bolded text). The token is necessary to assure that you are authorized to retrieve products from RITA. To generate a token, see the[Auth.MAST](https://auth.mast.stsci.edu/info) page.
Widget | Command
---|---
![](https://outerspace.stsci.edu/download/thumbnails/282168349/button_apiScript_download.png?version=1&modificationDate=1734032506615&api=v2) |  **Retrieve** curl -H "Content-Type: application/json" \ -H "**Authorization: token $MAST_API_TOKEN** " \ -X POST '<https://mast.stsci.edu/cassi/api/v0.1/download/roman/rita>'\ -d '{"query_params":["<https://pl9dmsdaapi.stsci.edu/api/assets/v1/mast/rita/product/TVAC1_COLDQUAL_WFIFIN_20231008003314_WFI18_uncal.asdf>"]}' \ --compressed \ --output TVAC1_COLDQUAL_WFIFIN_20231008003314_WFI18_uncal.asdf.zip curl -H "Content-Type: application/json"\ -H "**Authorization: token $MAST_API_TOKEN** " \ -X POST '<https://mast.stsci.edu/cassi/api/v0.1/download/roman/rita>' \ -d '{"query_params":["<https://pl9dmsdaapi.stsci.edu/api/assets/v1/mast/rita/product/TVAC1_NOMOPS_WFIFIN_20231015132524_WFI05_uncal.asdf>"]}' \ --compressed \ --output TVAC1_NOMOPS_WFIFIN_20231015132524_WFI05_uncal.asdf.zip  
* * *

<!-- CHUNK 30 END -->

<!-- CHUNK 31 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [RITA search](https://mast.stsci.edu/cassi/#/roman?dataGroup=RITA)
* [CaSSI.MAST API](https://mast.stsci.edu/cassi/docs/index.html)
* [WFI Ground Testing Campaigns](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns)
* [Summary table](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-detectors/detector-performance/wfi-ground-testing-campaigns#WFIGroundTestingCampaigns-Testing-summary-table) of the ground testing campaigns
* [Description of WFI](https://roman-docs.stsci.edu/roman-instruments-home/wfi-imaging-mode-user-guide/wfi-design/description-of-wfi)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 31 END -->

