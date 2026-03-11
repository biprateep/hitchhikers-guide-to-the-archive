---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ"
date_accessed: "2026-03-11T11:31:34.683186"
---

<!-- CHUNK 1 START -->
This article offers answers to MAST **frequently asked questions** (FAQ). Select the tab below for your topic of interest; your question might already be answered!

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "FAQ Topics"} -->
* 1[General](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-General)
* 1.1[How do I create a DOI to reference the data I analyzed in my publication](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIcreateaDOItoreferencethedataIanalyzedinmypublication)
* 1.2[How do I search for solar system bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIsearchforsolarsystembodiesinMAST)
* 2[Data Access](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-DataAccess)
* 2.1[I am a Principal Investigator of an HST or JWST observing program. How do I authorize my Co-Is to access the data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-IamaPrincipalInvestigatorofanHSTorJWSTobservingprogram.HowdoIauthorizemyCo-Istoaccessthedata)
* 2.2[Why do I sometimes get a "404 File Not Found" error when I try to retrieve files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-WhydoIsometimesgeta"404FileNotFound"errorwhenItrytoretrievefiles)
* 2.3[My API queries for data taken with particular instruments do not return the expected results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-MyAPIqueriesfordatatakenwithparticularinstrumentsdonotreturntheexpectedresults)
* 2.4[The Portal won't load Observations into my Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-BasketFullThePortalwon'tloadObservationsintomyBasket)
* 3[JWST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-JWST)
* 3.1[How do I learn when JWST observations have been obtained](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIlearnwhenJWSTobservationshavebeenobtained)
* 3.2[What is the usual delay between the end of a JWST observation and when it first appears in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-WhatistheusualdelaybetweentheendofaJWSTobservationandwhenitfirstappearsinMAST)
* 3.3[How do I know whether data from my JWST program have been reprocessed](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIknowwhetherdatafrommyJWSTprogramhavebeenreprocessed)
* 3.4[Why do I get so many identical reprocessing notifications per day](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-WhydoIgetsomanyidenticalreprocessingnotificationsperday)  
* * *

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "General", "Header 3": "How do I create a DOI to reference the data I analyzed in my publication"} -->
Navigate your browser to the special [DOI Portal](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html). Follow the instructions in the [Special Searches](https://outerspace.stsci.edu/display/MASTDOCS/Special+Searches) article in the [Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide), specifically the section on __Create a DOI__.
The [DOI Homepage](https://archive.stsci.edu/publishing/doi) has additional FAQs and information about pre-made DOIs for bulk datasets (e.g. Kepler, TESS, Pan-STARRS).
DOI for Uncalibrated Products
If you have reduced or extracted products yourself, rather than using the high-level products in MAST, you can still create a DOI for your data. Load the level-2b (calibrated) or Level-3 (calibrated & combined) products into the DOI basket, even if you did not use them directly; users who follow the DOI link will be able to access the lower-level products. When creating your DOI, we recommend that you include a note in the "_About this data_ " field specifying the products used in your analysis.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "General", "Header 3": "How do I search for solar system bodies in MAST"} -->
It is not currently possible to search for moving targets in MAST by position (or using ephemeridies). You can instead search by target name or by finding the target coordinates using the JPL Horizons System. See the article [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/display/MASTDOCS/Finding+Solar+System+Bodies+in+MAST) for details.
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "Data Access", "Header 3": "I am a Principal Investigator of an HST or JWST observing program. How do I authorize my Co-Is to access the data"} -->
Direct your browser to the [MyST site](https://proper.stsci.edu/proper/authentication/auth), and follow the instructions in the [MAST Accounts page](https://outerspace.stsci.edu/display/MASTDOCS/MAST+Accounts).

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "Data Access", "Header 3": "Why do I sometimes get a \"404 File Not Found\" error when I try to retrieve files"} -->
Data from most programs have been reprocessed fairly often. When this happens, updated files eventually replace the prior version. However, there is a latency between the time when updated files are created and when the files are migrated to the area where they are discoverable in MAST. Sometimes the delay can be more than a day. Unfortunately, there is no easy workaround. Patience is the key.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "Data Access", "Header 3": "My API queries for data taken with particular instruments do not return the expected results"} -->
The names of the HST and JWST science instruments as viewed in MAST have been augmented to include configuration information. This affects the way that instrument names should be specified in the [Advanced Search](https://outerspace.stsci.edu/display/MASTDOCS/Advanced+Search) in the Portal, and in **astroquery.mast** API. Other kinds of queries are not affected. See, e.g., the article [JWST Instrument Names](https://outerspace.stsci.edu/display/MASTDOCS/JWST+Instrument+Names) for details.
Some Observations (i.e., rows in the Portal Search Results table) are associated with a very large number of files. Loading too many Observation into the Basket at once can result in a pop-up error message like this one:
![](https://outerspace.stsci.edu/download/attachments/232358851/error_BasketLoad.png?version=1&modificationDate=1754314670291&api=v2)
This problem of loading too many files in the basket is particularly likely for JWST Observations with many extracted spectra (e.g., NIRCam Wide-Field Slitless Spectra), or Observations containing lots of spatial dithers or other spacecraft maneuvers (as for an extended mosaic or moving targets). To get around this problem you can do the following:
1. Select fewer Observations, then load those into the Basket, select files for download, then empty the Download Basket when finished. Repeat as necessary until you have retrieved files from all Observations of interest.
2. Use the __Astroquery Search and Retrieval__ section of the [Using MAST APIs](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs) article. Follow the link to the Jupyter Notebook for API Large Downloads.  
Using the API may be the _**only**_ choice for the very largest programs, where even one Observation over-fills the Portal Download Basket. There is no way to tell whether there are too many files for the Basket other than to try to load an Observation.
* * *

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "How do I learn when JWST observations have been obtained"} -->
There are multiple ways to discover JWST Observations. For instance:
* To be notified when JWST data appear in the archive, become available to all users, or are reprocessed, use the [subscription service](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications) in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). This is the recommended way to find out when data from program IDs get ingested or receive updates.
* In the MAST Portal, click **Advanced Search** , enter "`JWST`" in the __**Mission**__ filter and enter a range of observation start dates, e.g., "`2022-07-02`" and "`2022-07-09`" in the __**Start Time**__ filter boxes, then click the **Search** button. This will search for all JWST observations that were started between 2 July 2022 through 9 July 2022.
* Using the Python library **astroquery.mast** , form a _**query_criteria**_ _`obs_collection="JWST"`_and some other parameters such as _`instrument_name="MIRI*"`_. See the

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "What is the usual delay between the end of a JWST observation and when it first appears in MAST"} -->
From hours to days.
This is a difficult question to answer with precision because it depends on several factors. Many hours can elapse between the end of an exposure and transmission of that data to the ground. This is largely because JWST does not have continuous contact with the ground in the high-bandwidth channel that is required to transmit high-volume science data. Once the data processing system receives the data from Flight Operations, much of the data is processed within a few hours. There are edge cases where complex programs may take more than a day, or even several days, to process. That said, it is likely that most data will appear in MAST within a day or two of the end of the last exposure in an observation.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "How do I know whether data from my JWST program have been reprocessed"} -->
It is best to "subscribe" to data from a program so that you are notified after reprocessed data are available in MAST. See the article [Program Subscriptions and Notifications](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications) for details. Select the __Reprocessed__ check-box under subscription type; it is best to select a _**Daily**_ notification frequency to avoid being bombarded with notifications (see next FAQ).
Absent a subscription, it is more challenging to determine whether extant data in MAST have been reprocessed recently. First, read the JDox article [JWST Operations Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information) for context. In particular, it calls out two FITS header keywords to look at: `CAL_VER` and `CRDS_CTX`. If files you have on your machine show an earlier version than what is shown in MAST, you may want to re-retrieve the data. To see which versions are in the archive,
* Do an [Instrument Keyword search](https://outerspace.stsci.edu/display/MASTDOCS/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords) for data from the relevant instrument and the Program ID of interest
* In the results table, view the following fields (you might want to “Edit Columns” in the Portal to show only these):
* `Filename`
* `Date` (this is the date the file was created, which reflects when processing was last performed)
* `cal_ver` to show the version of the processing software
* `crds_ctx` to show the context of the CRDS reference files  
It is possible that files in MAST are awaiting a new reprocessing because of very recent updates to reference files. There is no easy way to tell that, except by subscribing to the relevant data.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "Why do I get so many identical reprocessing notifications per day"} -->
You probably requested a "Fast" notification frequency, and (for JWST data) possibly for product levels of "2" and higher. Notifications are generated less than an hour after new data products are ingested into the Archive (whether new or reprocessed). For many programs it takes hours, or sometimes days, for all data to be processed. During this time, many notifications are generated as the products are archived; potentially dozens or even hundreds of notifications. Unfortunately, the notifications are not specific enough to link to only the data that have been reprocessed. Instead, the link will take you to a Portal results page with all data from the program.
Editing two settings in the subscriptions menu should help:
1. Select a notification frequency of "Daily" rather than "Fast." Then individual triggers will be combined into a single notification for that day.
2. For JWST programs, request notifications for product Level "3" rather than "2." The L-3 products are (usually) combined from L-2b (calibrated) products, so except for extracted spectra, there are many fewer products from which notifications will be generated.  
If you have already established a subscription, you can click the "Subscriptions" link in the [Portal](https://mast.stsci.edu) and edit the frequency and product level parameters for each subscription. Read [Program Subscriptions and Notifications](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications) to see how to do this.
* * *

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
For questions not addressed in the FAQ, please contact the Archive Help Desk (archive@stsci.edu).
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support)
* [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)  
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
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
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
This article offers answers to MAST **frequently asked questions** (FAQ). Select the tab below for your topic of interest; your question might already be answered!

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "FAQ Topics"} -->
* 1[General](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-General)
* 1.1[How do I create a DOI to reference the data I analyzed in my publication](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIcreateaDOItoreferencethedataIanalyzedinmypublication)
* 1.2[How do I search for solar system bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIsearchforsolarsystembodiesinMAST)
* 2[Data Access](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-DataAccess)
* 2.1[I am a Principal Investigator of an HST or JWST observing program. How do I authorize my Co-Is to access the data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-IamaPrincipalInvestigatorofanHSTorJWSTobservingprogram.HowdoIauthorizemyCo-Istoaccessthedata)
* 2.2[Why do I sometimes get a "404 File Not Found" error when I try to retrieve files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-WhydoIsometimesgeta"404FileNotFound"errorwhenItrytoretrievefiles)
* 2.3[My API queries for data taken with particular instruments do not return the expected results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-MyAPIqueriesfordatatakenwithparticularinstrumentsdonotreturntheexpectedresults)
* 2.4[The Portal won't load Observations into my Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-BasketFullThePortalwon'tloadObservationsintomyBasket)
* 3[JWST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-JWST)
* 3.1[How do I learn when JWST observations have been obtained](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIlearnwhenJWSTobservationshavebeenobtained)
* 3.2[What is the usual delay between the end of a JWST observation and when it first appears in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-WhatistheusualdelaybetweentheendofaJWSTobservationandwhenitfirstappearsinMAST)
* 3.3[How do I know whether data from my JWST program have been reprocessed](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-HowdoIknowwhetherdatafrommyJWSTprogramhavebeenreprocessed)
* 3.4[Why do I get so many identical reprocessing notifications per day](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/232358851/FAQ#FAQ-WhydoIgetsomanyidenticalreprocessingnotificationsperday)  
* * *

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "General", "Header 3": "How do I create a DOI to reference the data I analyzed in my publication"} -->
Navigate your browser to the special [DOI Portal](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html). Follow the instructions in the [Special Searches](https://outerspace.stsci.edu/display/MASTDOCS/Special+Searches) article in the [Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide), specifically the section on __Create a DOI__.
The [DOI Homepage](https://archive.stsci.edu/publishing/doi) has additional FAQs and information about pre-made DOIs for bulk datasets (e.g. Kepler, TESS, Pan-STARRS).
DOI for Uncalibrated Products
If you have reduced or extracted products yourself, rather than using the high-level products in MAST, you can still create a DOI for your data. Load the level-2b (calibrated) or Level-3 (calibrated & combined) products into the DOI basket, even if you did not use them directly; users who follow the DOI link will be able to access the lower-level products. When creating your DOI, we recommend that you include a note in the "_About this data_ " field specifying the products used in your analysis.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "General", "Header 3": "How do I search for solar system bodies in MAST"} -->
It is not currently possible to search for moving targets in MAST by position (or using ephemeridies). You can instead search by target name or by finding the target coordinates using the JPL Horizons System. See the article [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/display/MASTDOCS/Finding+Solar+System+Bodies+in+MAST) for details.
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "Data Access", "Header 3": "I am a Principal Investigator of an HST or JWST observing program. How do I authorize my Co-Is to access the data"} -->
Direct your browser to the [MyST site](https://proper.stsci.edu/proper/authentication/auth), and follow the instructions in the [MAST Accounts page](https://outerspace.stsci.edu/display/MASTDOCS/MAST+Accounts).

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "Data Access", "Header 3": "Why do I sometimes get a \"404 File Not Found\" error when I try to retrieve files"} -->
Data from most programs have been reprocessed fairly often. When this happens, updated files eventually replace the prior version. However, there is a latency between the time when updated files are created and when the files are migrated to the area where they are discoverable in MAST. Sometimes the delay can be more than a day. Unfortunately, there is no easy workaround. Patience is the key.

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "Data Access", "Header 3": "My API queries for data taken with particular instruments do not return the expected results"} -->
The names of the HST and JWST science instruments as viewed in MAST have been augmented to include configuration information. This affects the way that instrument names should be specified in the [Advanced Search](https://outerspace.stsci.edu/display/MASTDOCS/Advanced+Search) in the Portal, and in **astroquery.mast** API. Other kinds of queries are not affected. See, e.g., the article [JWST Instrument Names](https://outerspace.stsci.edu/display/MASTDOCS/JWST+Instrument+Names) for details.
Some Observations (i.e., rows in the Portal Search Results table) are associated with a very large number of files. Loading too many Observation into the Basket at once can result in a pop-up error message like this one:
![](https://outerspace.stsci.edu/download/attachments/232358851/error_BasketLoad.png?version=1&modificationDate=1754314670291&api=v2)
This problem of loading too many files in the basket is particularly likely for JWST Observations with many extracted spectra (e.g., NIRCam Wide-Field Slitless Spectra), or Observations containing lots of spatial dithers or other spacecraft maneuvers (as for an extended mosaic or moving targets). To get around this problem you can do the following:
1. Select fewer Observations, then load those into the Basket, select files for download, then empty the Download Basket when finished. Repeat as necessary until you have retrieved files from all Observations of interest.
2. Use the __Astroquery Search and Retrieval__ section of the [Using MAST APIs](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs) article. Follow the link to the Jupyter Notebook for API Large Downloads.  
Using the API may be the _**only**_ choice for the very largest programs, where even one Observation over-fills the Portal Download Basket. There is no way to tell whether there are too many files for the Basket other than to try to load an Observation.
* * *

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "How do I learn when JWST observations have been obtained"} -->
There are multiple ways to discover JWST Observations. For instance:
* To be notified when JWST data appear in the archive, become available to all users, or are reprocessed, use the [subscription service](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications) in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html). This is the recommended way to find out when data from program IDs get ingested or receive updates.
* In the MAST Portal, click **Advanced Search** , enter "`JWST`" in the __**Mission**__ filter and enter a range of observation start dates, e.g., "`2022-07-02`" and "`2022-07-09`" in the __**Start Time**__ filter boxes, then click the **Search** button. This will search for all JWST observations that were started between 2 July 2022 through 9 July 2022.
* Using the Python library **astroquery.mast** , form a _**query_criteria**_ _`obs_collection="JWST"`_and some other parameters such as _`instrument_name="MIRI*"`_. See the

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "What is the usual delay between the end of a JWST observation and when it first appears in MAST"} -->
From hours to days.
This is a difficult question to answer with precision because it depends on several factors. Many hours can elapse between the end of an exposure and transmission of that data to the ground. This is largely because JWST does not have continuous contact with the ground in the high-bandwidth channel that is required to transmit high-volume science data. Once the data processing system receives the data from Flight Operations, much of the data is processed within a few hours. There are edge cases where complex programs may take more than a day, or even several days, to process. That said, it is likely that most data will appear in MAST within a day or two of the end of the last exposure in an observation.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "How do I know whether data from my JWST program have been reprocessed"} -->
It is best to "subscribe" to data from a program so that you are notified after reprocessed data are available in MAST. See the article [Program Subscriptions and Notifications](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications) for details. Select the __Reprocessed__ check-box under subscription type; it is best to select a _**Daily**_ notification frequency to avoid being bombarded with notifications (see next FAQ).
Absent a subscription, it is more challenging to determine whether extant data in MAST have been reprocessed recently. First, read the JDox article [JWST Operations Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information) for context. In particular, it calls out two FITS header keywords to look at: `CAL_VER` and `CRDS_CTX`. If files you have on your machine show an earlier version than what is shown in MAST, you may want to re-retrieve the data. To see which versions are in the archive,
* Do an [Instrument Keyword search](https://outerspace.stsci.edu/display/MASTDOCS/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords) for data from the relevant instrument and the Program ID of interest
* In the results table, view the following fields (you might want to “Edit Columns” in the Portal to show only these):
* `Filename`
* `Date` (this is the date the file was created, which reflects when processing was last performed)
* `cal_ver` to show the version of the processing software
* `crds_ctx` to show the context of the CRDS reference files  
It is possible that files in MAST are awaiting a new reprocessing because of very recent updates to reference files. There is no easy way to tell that, except by subscribing to the relevant data.

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "FAQ Topics", "Header 2": "JWST", "Header 3": "Why do I get so many identical reprocessing notifications per day"} -->
You probably requested a "Fast" notification frequency, and (for JWST data) possibly for product levels of "2" and higher. Notifications are generated less than an hour after new data products are ingested into the Archive (whether new or reprocessed). For many programs it takes hours, or sometimes days, for all data to be processed. During this time, many notifications are generated as the products are archived; potentially dozens or even hundreds of notifications. Unfortunately, the notifications are not specific enough to link to only the data that have been reprocessed. Instead, the link will take you to a Portal results page with all data from the program.
Editing two settings in the subscriptions menu should help:
1. Select a notification frequency of "Daily" rather than "Fast." Then individual triggers will be combined into a single notification for that day.
2. For JWST programs, request notifications for product Level "3" rather than "2." The L-3 products are (usually) combined from L-2b (calibrated) products, so except for extracted spectra, there are many fewer products from which notifications will be generated.  
If you have already established a subscription, you can click the "Subscriptions" link in the [Portal](https://mast.stsci.edu) and edit the frequency and product level parameters for each subscription. Read [Program Subscriptions and Notifications](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications) to see how to do this.
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
For questions not addressed in the FAQ, please contact the Archive Help Desk (archive@stsci.edu).
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support)
* [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 23 END -->

