---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal"
date_accessed: "2026-03-11T16:26:42.501880"
content_length: 23613
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

