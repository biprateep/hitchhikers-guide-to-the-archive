---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal"
date_accessed: "2026-03-11T11:33:33.960106"
---

<!-- CHUNK 1 START -->
Data from thousands of monitors on JWST are collected and stored in an Engineering Database as timeseries, and are identified by mnemonics as described in the article on [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data). This article describes how to access those data through the Calibrated Engineering Data Portal.
**On this page...**
* 1[Calibrated Engineering Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-CalibratedEngineeringPortal)
* 2[Navigating to the Engineering Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-NavigatingtotheEngineeringPortal)
* 3[Search for Engineering Mnemonics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-SearchforEngineeringMnemonics)
* 3.1[Construct and Execute a Query](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-ConstructandExecuteaQuery)
* 4[Visualize Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-VisualizeEngineeringData)
* 5[Retrieve Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-RetrieveEngineeringData)
* 6[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Calibrated Engineering Portal"} -->
The JWST Calibrated Engineering Portal, which is a web application for searching, visualizing, and retrieving engineering data, is illustrated in Fig. 1.  
![JWST Engineering Database Portal](https://outerspace.stsci.edu/download/attachments/113771415/jwst_edb_frontpage.png?version=1&modificationDate=1684784276965&api=v2)JWST Engineering Database Portal
**Figure 1 —** The JWST Calibrated Engineering Data Portal as it appears prior to a query, with menus for entering mnemonics of interest (_upper left_) and time ranges (_lower left_). Results of successful queries are displayed as rows in a table (_right_), with options for plotting and downloading the timeseries.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Navigating to the Engineering Portal"} -->
There are two ways to access the Calibrated Engineering Portal user interface:
* Navigate directly to the [Calibrated Engineering Portal](https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html)  
* Execute a search for JWST data from the [MAST Discovery Portal](https://mast.stsci.edu/portal_jwst/Mashup/Clients/Mast/Portal.html):
* After a [successful search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching) with the Portal, click the EDB icon ![](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_EDB_24x24.png?version=1&modificationDate=1683654234414&api=v2) in the **Actions** menu (see Fig. 2) to bring up the EDB Portal; this will enable you to search for engineering data for that observation. The EDB Portal will be pre-populated with the Date Range corresponding to the exposure duration of the science data.  
![](https://outerspace.stsci.edu/download/attachments/113771415/EDB_menu_Actions.png?version=1&modificationDate=1683654234407&api=v2)
**Figure 2 —** The orange EDB link, seen here in the search results **Actions** menu of the [MAST Discovery Portal](https://mast.stsci.edu/portal_jwst/Mashup/Clients/Mast/Portal.html), will take users to the Calibrated Engineering Data Portal with the start/stop search range pre-populated from the associated Observation.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics"} -->
Engineering data are stored in the database as timeseries, and are identified by _**mnemonics**_ ; see the article on [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data) for details. There are a few means to execute a search; the options are described below.
It is possible to download a time-series for multiple mnemonics programmatically using an API. See the tutorial [JWST Engineering Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs).

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query"} -->
| Instruction | Notes
---|---|---
**1** | Navigate your browser to the [JWST Calibrated Engineering Data Portal](https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html). You can also use a link from the search [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) for an individual observation. | ![](https://outerspace.stsci.edu/download/attachments/113771415/banner_engPortal.png?version=1&modificationDate=1684784767588&api=v2)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query", "Header 3": "Method A: Dialog Boxes"} -->
| Instruction | Notes
---|---|---
2a |  Enter an engineering mnemonic name into the **Mnemonic Search** dialog box on the upper-left. The mnemonic names will auto-complete as you type. Here are some example mnemonics:
* `SA_ZATTEST1` through `4`: These are the parameters for the quaternion
* `SA_ZRFGS2J11` through `33`: These define the J-Frame
* SA_ZHGAUPST: this provides the status of the High-Gain Antenna (e.g., MOVING, FINISHED)  
You may search for multiple mnemonics, and multiple date ranges, in a single query. | ![Mnemonic search dialog box with an example entered](https://outerspace.stsci.edu/download/thumbnails/113771415/select_mnemonic.png?version=1&modificationDate=1683654234483&api=v2)Mnemonic search dialog box
3a |  Using the sliders or the dialog boxes, select a date range that is applicable to the mnemonic. Then click the **Add Date Range** button. You may search over multiple time ranges at once. **Note:** The initial range of available values in the **Start Time** filter will be pre-populated if you navigated to the EDB interface by clicking the EDB icon in the Portal results grid of a prior search. | ![Date range silder](https://outerspace.stsci.edu/download/attachments/113771415/edb_date.png?version=1&modificationDate=1683654234352&api=v2)Date range silder
4 | Click the _**Run Query**_ link at the bottom-left of the Portal window. | ![Run query button](https://outerspace.stsci.edu/download/thumbnails/113771415/EDB_run-query.png?version=1&modificationDate=1683654234558&api=v2)Run query button

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query", "Header 3": "Method B: Upload a Mnemonic List"} -->
| Instruction | Notes
---|---|---
2b |  Click **Upload Mnemonic List** button at the bottom of the search window. Then click the **Browse** button to to enter the name of a `.csv` file containing a comma-separated list of mnemonic names. **Note:** the names must be in upper-case. | ![Upload mnemonic list portal](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_MnUpload.png?version=1&modificationDate=1683654234567&api=v2)Upload mnemonic list portal
3b | Follow instruction **3a** to add a date range. |  
4 | Click the _**Run Query**_ link at the bottom-left of the Portal. | ![Run query button](https://outerspace.stsci.edu/download/thumbnails/113771415/EDB_run-query.png?version=1&modificationDate=1683654234558&api=v2)Run query button

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query", "Header 3": "Method C: Upload a Query List"} -->
| Instruction | Notes
---|---|---
2c |  Click **Upload Query List** button at the bottom of the search window. Then click the **Browse** button to to enter the name of a `.csv` file containing row tuples. Each tuple must include a mnemonic name, and an initial and final date-time. **Note:** the format of the date-times must be compatible with Microsoft Excel date formats. This format includes two ISO-8601 variants: `2022-06-11 17:28:19` `2022-06-11T17:28:19` The search will commence once the query list is uploaded successfully. | ![Upload query list portal](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_QLUpload.png?version=1&modificationDate=1683654234588&api=v2)Upload query list portal

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Visualize Engineering Data"} -->
The results of a successful query will look something like this;
![Successful EDB query](https://outerspace.stsci.edu/download/attachments/113771415/edb_results.png?version=1&modificationDate=1683654234346&api=v2)Successful EDB query
**Note:** The results grid by default also shows the **mnemonic search** panels to the left of the list view, which was collapsed in the above graphic.
Plot Range
The extracted engineering data cover a time range that is slightly larger than the Date Range interval specified in the search. This is to ensure that the data timeseries is not truncated by rounding in the date-time extraction.
Time Sampling
The time sampling may be different for different mnemonics: some are sampled regularly and continuously, others are sampled when there is a change. This will require some care when comparing or correlating data from different mnemonics during analysis.  
| Instruction | Notes
---|---|---
5 |  Click the box for a mnemonic in the results grid, then click the plot icon to view an interactive plot. **Note:** Not all mnenomics data can be plotted, such as binary changes in state. The plot icon will not appear in these cases. | ![EDB plot icon](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_EDB_plot.png?version=1&modificationDate=1683654234627&api=v2)EDB plot icon  
|  The plot will look something like this: ![](https://outerspace.stsci.edu/download/attachments/113771415/EDB_plot.png?version=1&modificationDate=1683654234665&api=v2)

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Retrieve Engineering Data"} -->
Engineering data will be delivered to the user as a set of one or more CSV files, one per mnemonic, containing time stamps (in MJD) and telemetry values.  
| Instruction | Notes
---|---|---
6a | Click the file icon above the rows to retrieve the time-ordered data for all matched mnemonics, in **csv** format. Use the pop-up window to save the file to disk. | ![File icon](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_file_white.png?version=1&modificationDate=1683654234673&api=v2)File icon
7a | Click the **Save File** button in the pop-up window. The location where the file will appear on your system depends upon your browser settings. | ![Save file pop-up window](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_fileRetrieve.png?version=1&modificationDate=1683654234681&api=v2)Save file pop-up window
6b | Click the checkbox at the beginning of one or more rows. Then click the file icon at the top right of the _List View_. | ![File icon](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_file_white.png?version=1&modificationDate=1683654234673&api=v2)File icon
7b |  Select an option in the **Format** pull-down menu, then click the **Download** button. The options are:
* **_zip_** , **_tar_ , or _tar.gz_** for streaming retrieval through your browser
* **_Curl_** to download a script to retrieve the files at a later time  
| ![Download file window](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_save-files.png?version=1&modificationDate=1683654234733&api=v2)Download file window
Very Large Files
Direct (streaming) download of very large files may fail silently. Select the Curl script download option to retrieve the file(s) in these cases.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* See the _JWST Engineering Data Retrieval_ tutorial in [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs)
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data)  
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
Data from thousands of monitors on JWST are collected and stored in an Engineering Database as timeseries, and are identified by mnemonics as described in the article on [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data). This article describes how to access those data through the Calibrated Engineering Data Portal.
**On this page...**
* 1[Calibrated Engineering Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-CalibratedEngineeringPortal)
* 2[Navigating to the Engineering Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-NavigatingtotheEngineeringPortal)
* 3[Search for Engineering Mnemonics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-SearchforEngineeringMnemonics)
* 3.1[Construct and Execute a Query](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-ConstructandExecuteaQuery)
* 4[Visualize Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-VisualizeEngineeringData)
* 5[Retrieve Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-RetrieveEngineeringData)
* 6[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal#UsingtheEngineeringDataPortal-ForFurtherReading...)

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Calibrated Engineering Portal"} -->
The JWST Calibrated Engineering Portal, which is a web application for searching, visualizing, and retrieving engineering data, is illustrated in Fig. 1.  
![JWST Engineering Database Portal](https://outerspace.stsci.edu/download/attachments/113771415/jwst_edb_frontpage.png?version=1&modificationDate=1684784276965&api=v2)JWST Engineering Database Portal
**Figure 1 —** The JWST Calibrated Engineering Data Portal as it appears prior to a query, with menus for entering mnemonics of interest (_upper left_) and time ranges (_lower left_). Results of successful queries are displayed as rows in a table (_right_), with options for plotting and downloading the timeseries.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Navigating to the Engineering Portal"} -->
There are two ways to access the Calibrated Engineering Portal user interface:
* Navigate directly to the [Calibrated Engineering Portal](https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html)  
* Execute a search for JWST data from the [MAST Discovery Portal](https://mast.stsci.edu/portal_jwst/Mashup/Clients/Mast/Portal.html):
* After a [successful search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching) with the Portal, click the EDB icon ![](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_EDB_24x24.png?version=1&modificationDate=1683654234414&api=v2) in the **Actions** menu (see Fig. 2) to bring up the EDB Portal; this will enable you to search for engineering data for that observation. The EDB Portal will be pre-populated with the Date Range corresponding to the exposure duration of the science data.  
![](https://outerspace.stsci.edu/download/attachments/113771415/EDB_menu_Actions.png?version=1&modificationDate=1683654234407&api=v2)
**Figure 2 —** The orange EDB link, seen here in the search results **Actions** menu of the [MAST Discovery Portal](https://mast.stsci.edu/portal_jwst/Mashup/Clients/Mast/Portal.html), will take users to the Calibrated Engineering Data Portal with the start/stop search range pre-populated from the associated Observation.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics"} -->
Engineering data are stored in the database as timeseries, and are identified by _**mnemonics**_ ; see the article on [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data) for details. There are a few means to execute a search; the options are described below.
It is possible to download a time-series for multiple mnemonics programmatically using an API. See the tutorial [JWST Engineering Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs).

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query"} -->
| Instruction | Notes
---|---|---
**1** | Navigate your browser to the [JWST Calibrated Engineering Data Portal](https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html). You can also use a link from the search [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) for an individual observation. | ![](https://outerspace.stsci.edu/download/attachments/113771415/banner_engPortal.png?version=1&modificationDate=1684784767588&api=v2)

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query", "Header 3": "Method A: Dialog Boxes"} -->
| Instruction | Notes
---|---|---
2a |  Enter an engineering mnemonic name into the **Mnemonic Search** dialog box on the upper-left. The mnemonic names will auto-complete as you type. Here are some example mnemonics:
* `SA_ZATTEST1` through `4`: These are the parameters for the quaternion
* `SA_ZRFGS2J11` through `33`: These define the J-Frame
* SA_ZHGAUPST: this provides the status of the High-Gain Antenna (e.g., MOVING, FINISHED)  
You may search for multiple mnemonics, and multiple date ranges, in a single query. | ![Mnemonic search dialog box with an example entered](https://outerspace.stsci.edu/download/thumbnails/113771415/select_mnemonic.png?version=1&modificationDate=1683654234483&api=v2)Mnemonic search dialog box
3a |  Using the sliders or the dialog boxes, select a date range that is applicable to the mnemonic. Then click the **Add Date Range** button. You may search over multiple time ranges at once. **Note:** The initial range of available values in the **Start Time** filter will be pre-populated if you navigated to the EDB interface by clicking the EDB icon in the Portal results grid of a prior search. | ![Date range silder](https://outerspace.stsci.edu/download/attachments/113771415/edb_date.png?version=1&modificationDate=1683654234352&api=v2)Date range silder
4 | Click the _**Run Query**_ link at the bottom-left of the Portal window. | ![Run query button](https://outerspace.stsci.edu/download/thumbnails/113771415/EDB_run-query.png?version=1&modificationDate=1683654234558&api=v2)Run query button

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query", "Header 3": "Method B: Upload a Mnemonic List"} -->
| Instruction | Notes
---|---|---
2b |  Click **Upload Mnemonic List** button at the bottom of the search window. Then click the **Browse** button to to enter the name of a `.csv` file containing a comma-separated list of mnemonic names. **Note:** the names must be in upper-case. | ![Upload mnemonic list portal](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_MnUpload.png?version=1&modificationDate=1683654234567&api=v2)Upload mnemonic list portal
3b | Follow instruction **3a** to add a date range. |  
4 | Click the _**Run Query**_ link at the bottom-left of the Portal. | ![Run query button](https://outerspace.stsci.edu/download/thumbnails/113771415/EDB_run-query.png?version=1&modificationDate=1683654234558&api=v2)Run query button

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Search for Engineering Mnemonics", "Header 2": "Construct and Execute a Query", "Header 3": "Method C: Upload a Query List"} -->
| Instruction | Notes
---|---|---
2c |  Click **Upload Query List** button at the bottom of the search window. Then click the **Browse** button to to enter the name of a `.csv` file containing row tuples. Each tuple must include a mnemonic name, and an initial and final date-time. **Note:** the format of the date-times must be compatible with Microsoft Excel date formats. This format includes two ISO-8601 variants: `2022-06-11 17:28:19` `2022-06-11T17:28:19` The search will commence once the query list is uploaded successfully. | ![Upload query list portal](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_QLUpload.png?version=1&modificationDate=1683654234588&api=v2)Upload query list portal

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Visualize Engineering Data"} -->
The results of a successful query will look something like this;
![Successful EDB query](https://outerspace.stsci.edu/download/attachments/113771415/edb_results.png?version=1&modificationDate=1683654234346&api=v2)Successful EDB query
**Note:** The results grid by default also shows the **mnemonic search** panels to the left of the list view, which was collapsed in the above graphic.
Plot Range
The extracted engineering data cover a time range that is slightly larger than the Date Range interval specified in the search. This is to ensure that the data timeseries is not truncated by rounding in the date-time extraction.
Time Sampling
The time sampling may be different for different mnemonics: some are sampled regularly and continuously, others are sampled when there is a change. This will require some care when comparing or correlating data from different mnemonics during analysis.  
| Instruction | Notes
---|---|---
5 |  Click the box for a mnemonic in the results grid, then click the plot icon to view an interactive plot. **Note:** Not all mnenomics data can be plotted, such as binary changes in state. The plot icon will not appear in these cases. | ![EDB plot icon](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_EDB_plot.png?version=1&modificationDate=1683654234627&api=v2)EDB plot icon  
|  The plot will look something like this: ![](https://outerspace.stsci.edu/download/attachments/113771415/EDB_plot.png?version=1&modificationDate=1683654234665&api=v2)

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Retrieve Engineering Data"} -->
Engineering data will be delivered to the user as a set of one or more CSV files, one per mnemonic, containing time stamps (in MJD) and telemetry values.  
| Instruction | Notes
---|---|---
6a | Click the file icon above the rows to retrieve the time-ordered data for all matched mnemonics, in **csv** format. Use the pop-up window to save the file to disk. | ![File icon](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_file_white.png?version=1&modificationDate=1683654234673&api=v2)File icon
7a | Click the **Save File** button in the pop-up window. The location where the file will appear on your system depends upon your browser settings. | ![Save file pop-up window](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_fileRetrieve.png?version=1&modificationDate=1683654234681&api=v2)Save file pop-up window
6b | Click the checkbox at the beginning of one or more rows. Then click the file icon at the top right of the _List View_. | ![File icon](https://outerspace.stsci.edu/download/thumbnails/113771415/icon_file_white.png?version=1&modificationDate=1683654234673&api=v2)File icon
7b |  Select an option in the **Format** pull-down menu, then click the **Download** button. The options are:
* **_zip_** , **_tar_ , or _tar.gz_** for streaming retrieval through your browser
* **_Curl_** to download a script to retrieve the files at a later time  
| ![Download file window](https://outerspace.stsci.edu/download/thumbnails/113771415/dialog_EDB_save-files.png?version=1&modificationDate=1683654234733&api=v2)Download file window
Very Large Files
Direct (streaming) download of very large files may fail silently. Select the Curl script download option to retrieve the file(s) in these cases.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* See the _JWST Engineering Data Retrieval_ tutorial in [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs)
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 21 END -->

