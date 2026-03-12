---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products"
date_accessed: "2026-03-11T11:36:10.292942"
---

<!-- CHUNK 1 START -->
Authorized users may access and retrieve telemetry and selected supplemental Roman data products using the CaSSI web interface, or with curl commands.
**On this page...**
* 1[Product Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ProductSearch)
* 1.1[Product Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ProductType)
* 1.2[File name pattern](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-Filenamepattern)
* 1.3[Date Picker](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-DatePicker)
* 2[Retrieve Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-RetrieveData)
* 2.1[Product Download API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ProductDownloadAPI)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Product Search"} -->
The MAST CaSSI web interface includes a [search form](https://mast.stsci.edu/cassi/#/roman?dataGroup=Eng) for restricted Roman data products, including raw telemetry downlinked from the spacecraft. The web search interface is shown in Fig. 1. The various selectors are described in the following subsections.
Searches for the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to search for or access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to search these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.  
![](https://outerspace.stsci.edu/download/attachments/333677656/window_MM_suppTelm.png?version=1&modificationDate=1749497407338&api=v2)
![](https://outerspace.stsci.edu/download/attachments/333677656/menu_dataGroup_suppTelm.png?version=1&modificationDate=1749497426034&api=v2)
**Figure 1.** CaSSI interface (_above_), and the Data Group selector within it (_below_) to search for Roman supplemental and telemetry files.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "Product Type"} -->
You may constrain a product search by one or more file types, which are listed in the table below. Many of the products are specific to the science instrument in use: Coronagraph Instrument (CGI) or Wide-Field Instrument (WFI). The default is to match any file type.
File Prefix | File Type | Notes
---|---|---
`FPEHK` | Housekeeping Ancillary Telemetry Data |  **F** ocal **P** lane **E** lectronics **H** ouse-**K** eeping files
`SCANC` | Housekeeping Ancillary Telemetry Data | **S** pace**C** raft **ANC** illary files
`CGI` | CGI Science Level 0 |  
`RST_EPH_DEF` | Observatory Definitive Ephemeris* | Past spacecraft position (km) and velocity (km/s) in X, Y, Z as a function of time, accounting for station-keeping maneuvers.
`RST_EPH_PRED` | Observatory Predicted Ephemeris* | Predicted spacecraft position (km) and velocity (km/s) in X, Y, Z as a function of time.
`RST_FSWLOG` | FSW Event Message Logs | Event messages from the **F** light **S** oft**W** are logs
`WFISCI` | WFI Science Level 0 |  
`WFIGW` | WFI Guide Window Level 0 |  
*The coordinate system for the ephemeris data is

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "File name pattern"} -->
Enter the name of one or more files in the File Name dialog box, separated by commas, to match filenames of interest. If you are unsure of the name, or wish to select a range of similar names, you can use a limited set of special characters to match or exclude substrings within a filename. The special characters are given below, and are interpreted syntactically within the context of a limited form of regular expressions (re).
Syntax | Meaning
---|---
% | Matches any substring
`*` | Matches any substring
`,` | Delimiter between filename expressions in a sequence
`[aeiou]` | Matches any character in the listed set
`[^XYZ]` | Matches any character _not_ in the listed set
`[a-z0-9]` | The set of characters can include a range or multiple ranges
The article [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions), which describes filename matching in the Mission MAST [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay), includes detailed examples of how to use the `re` syntax. But be aware of important differences:
* there is no implied wildcard at the beginning or end of a filename expression
* the following symbols are interpreted literally
* **`!`**does not mean logical negation
* **$** does not denote the end of the string
* **`\`**(backslash) is not a means to escape special characters

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "Date Picker"} -->
Use the date pickers to select a date range of interest.
![](https://outerspace.stsci.edu/download/thumbnails/333677656/dlo_datePicker_MM.png?version=1&modificationDate=1749495769187&api=v2)
The** _Date Picker_** (shown at left) can restrict the search to a particular date or (with a paired end-date picker) a date range. Alternatively just type the YYYY-MM-DD into the date field(s), and the `hh:mm:ss` into the time field(s).
The _time_ portion of the _date-time_ defaults to `0:00:00 hr` for the start time, and `23:59:59 hr` for the end time.
* * *

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Retrieve Data"} -->
A successful search will result in a table of results, one file per row, as shown below.  
![](https://outerspace.stsci.edu/download/attachments/333677656/window_SupData_results.png?version=1&modificationDate=1749671632485&api=v2)
**Figure 2.** Results window for the search for supplemental data (observatory ephemeris). After selecting one or more results (rows with checked boxes and light-blue background), the file(s) may be downloaded.  
Various elements of the results table are described in the article [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page), including:
* revising the parameters of the search and re-executing
* exporting the results table to a file
* selecting table rows
* navigating to pages in the results table  
Choose the files of interest for download, then click the **Download Data** button.
Large Downloads
If the combined size of the selected data files is large (>1 GB), download the retrieval script and run it on your machine to minimize the chance of server-side timeouts or other transfer problems.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Retrieve Data", "Header 2": "Product Download API"} -->
In addition to downloading the files via the browser window, you may choose to download a retrieval script.
![](https://outerspace.stsci.edu/download/attachments/333677656/dlo_romanCassi_Api..png?version=1&modificationDate=1749672127091&api=v2)
Selecting the API Script/Curl option will bring up a set of curl commands (one per file), which you can copy to your screen buffer, or download to your machine as a **bash** script. Run the script with a command similar to the following:
```
bash MAST_2025-06-11T191812_retrieve.sh
```  
* * *

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission MAST Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual)  
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
Authorized users may access and retrieve telemetry and selected supplemental Roman data products using the CaSSI web interface, or with curl commands.
**On this page...**
* 1[Product Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ProductSearch)
* 1.1[Product Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ProductType)
* 1.2[File name pattern](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-Filenamepattern)
* 1.3[Date Picker](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-DatePicker)
* 2[Retrieve Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-RetrieveData)
* 2.1[Product Download API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ProductDownloadAPI)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products#RomanSupplementalProducts-ForFurtherReading...)

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Product Search"} -->
The MAST CaSSI web interface includes a [search form](https://mast.stsci.edu/cassi/#/roman?dataGroup=Eng) for restricted Roman data products, including raw telemetry downlinked from the spacecraft. The web search interface is shown in Fig. 1. The various selectors are described in the following subsections.
Searches for the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to search for or access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to search these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.  
![](https://outerspace.stsci.edu/download/attachments/333677656/window_MM_suppTelm.png?version=1&modificationDate=1749497407338&api=v2)
![](https://outerspace.stsci.edu/download/attachments/333677656/menu_dataGroup_suppTelm.png?version=1&modificationDate=1749497426034&api=v2)
**Figure 1.** CaSSI interface (_above_), and the Data Group selector within it (_below_) to search for Roman supplemental and telemetry files.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "Product Type"} -->
You may constrain a product search by one or more file types, which are listed in the table below. Many of the products are specific to the science instrument in use: Coronagraph Instrument (CGI) or Wide-Field Instrument (WFI). The default is to match any file type.
File Prefix | File Type | Notes
---|---|---
`FPEHK` | Housekeeping Ancillary Telemetry Data |  **F** ocal **P** lane **E** lectronics **H** ouse-**K** eeping files
`SCANC` | Housekeeping Ancillary Telemetry Data | **S** pace**C** raft **ANC** illary files
`CGI` | CGI Science Level 0 |  
`RST_EPH_DEF` | Observatory Definitive Ephemeris* | Past spacecraft position (km) and velocity (km/s) in X, Y, Z as a function of time, accounting for station-keeping maneuvers.
`RST_EPH_PRED` | Observatory Predicted Ephemeris* | Predicted spacecraft position (km) and velocity (km/s) in X, Y, Z as a function of time.
`RST_FSWLOG` | FSW Event Message Logs | Event messages from the **F** light **S** oft**W** are logs
`WFISCI` | WFI Science Level 0 |  
`WFIGW` | WFI Guide Window Level 0 |  
*The coordinate system for the ephemeris data is

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "File name pattern"} -->
Enter the name of one or more files in the File Name dialog box, separated by commas, to match filenames of interest. If you are unsure of the name, or wish to select a range of similar names, you can use a limited set of special characters to match or exclude substrings within a filename. The special characters are given below, and are interpreted syntactically within the context of a limited form of regular expressions (re).
Syntax | Meaning
---|---
% | Matches any substring
`*` | Matches any substring
`,` | Delimiter between filename expressions in a sequence
`[aeiou]` | Matches any character in the listed set
`[^XYZ]` | Matches any character _not_ in the listed set
`[a-z0-9]` | The set of characters can include a range or multiple ranges
The article [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions), which describes filename matching in the Mission MAST [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay), includes detailed examples of how to use the `re` syntax. But be aware of important differences:
* there is no implied wildcard at the beginning or end of a filename expression
* the following symbols are interpreted literally
* **`!`**does not mean logical negation
* **$** does not denote the end of the string
* **`\`**(backslash) is not a means to escape special characters

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "Date Picker"} -->
Use the date pickers to select a date range of interest.
![](https://outerspace.stsci.edu/download/thumbnails/333677656/dlo_datePicker_MM.png?version=1&modificationDate=1749495769187&api=v2)
The** _Date Picker_** (shown at left) can restrict the search to a particular date or (with a paired end-date picker) a date range. Alternatively just type the YYYY-MM-DD into the date field(s), and the `hh:mm:ss` into the time field(s).
The _time_ portion of the _date-time_ defaults to `0:00:00 hr` for the start time, and `23:59:59 hr` for the end time.
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Retrieve Data"} -->
A successful search will result in a table of results, one file per row, as shown below.  
![](https://outerspace.stsci.edu/download/attachments/333677656/window_SupData_results.png?version=1&modificationDate=1749671632485&api=v2)
**Figure 2.** Results window for the search for supplemental data (observatory ephemeris). After selecting one or more results (rows with checked boxes and light-blue background), the file(s) may be downloaded.  
Various elements of the results table are described in the article [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page), including:
* revising the parameters of the search and re-executing
* exporting the results table to a file
* selecting table rows
* navigating to pages in the results table  
Choose the files of interest for download, then click the **Download Data** button.
Large Downloads
If the combined size of the selected data files is large (>1 GB), download the retrieval script and run it on your machine to minimize the chance of server-side timeouts or other transfer problems.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Retrieve Data", "Header 2": "Product Download API"} -->
In addition to downloading the files via the browser window, you may choose to download a retrieval script.
![](https://outerspace.stsci.edu/download/attachments/333677656/dlo_romanCassi_Api..png?version=1&modificationDate=1749672127091&api=v2)
Selecting the API Script/Curl option will bring up a set of curl commands (one per file), which you can copy to your screen buffer, or download to your machine as a **bash** script. Run the script with a command similar to the following:
```
bash MAST_2025-06-11T191812_retrieve.sh
```  
* * *

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission MAST Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 15 END -->

