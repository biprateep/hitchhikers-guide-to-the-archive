---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products"
date_accessed: "2026-03-11T11:35:58.628384"
---

<!-- CHUNK 1 START -->
Authorized users may access and retrieve selected telemetry and supplemental JWST data product types using the CaSSI web interface, or with curl commands.
**On this page...**
* 1[Product Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-ProductSearch)
* 1.1[Date of relevance](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-jw_ns_dateDateofrelevance)
* 1.2[Product File Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-jw_eng_prodTypeProductFileType)
* 1.3[Filename pattern](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-FileNamePatternFilenamepattern)
* 2[Retrieve Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-jw_ns_retrieveRetrieveData)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Product Search"} -->
The MAST CaSSI web interface includes a [search form](https://mast.stsci.edu/cassi/#/jwst) for a subset of restricted JWST data products, including raw science and engineering telemetry downlinked from the spacecraft. The web search interface is shown in Fig. 1. The various search parameters are described in the following subsections.
Searches for the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to search for or access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to search these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.  
![](https://outerspace.stsci.edu/download/attachments/333677647/window_Cassi-Jwst_SuppTelm.png?version=1&modificationDate=1752610506793&api=v2)
![](https://outerspace.stsci.edu/download/attachments/333677647/menu_dataGroup_CaSSI.png?version=1&modificationDate=1752610720882&api=v2)
**Figure 1.** CaSSI interface (_above_), and the Data Group selector within it (_below_) to search for JWST supplemental and telemetry files. The message **Filtered results:** at the bottom of the window dynamically updates the count of all files that match as values are entered for the search parameters.
Use the **Date** dialog box to select files that pertain to a date of interest. The date that applies to these products is currently derived from date substring embedded in the file name. Note that the contents within the files may span a date boundary.
![](https://outerspace.stsci.edu/download/thumbnails/333677647/datePicker_Cassi-Jwst.png?version=1&modificationDate=1752613708351&api=v2)
Click the date picker icon (![](https://outerspace.stsci.edu/download/thumbnails/333677647/icon_datePicker.png?version=1&modificationDate=1752613500662&api=v2)) and choose a year/day/month from the calendar, as shown at left, or simply type the date into the dialog box, in YYYY-MM-DD format.
Since not all file types include an embedded date string, choosing a date will implicitly exclude these file types from your search.
You may constrain a product search to one or more of the supported file types, which are listed in the table below. The default (i.e., no types selected) is to match any file type. File prefix characters are given when they apply to all files of a given type.
Prod. ID | Product | File Prefix | File Suffix | Description
---|---|---|---|---
1 | Recorded Science Data | `S0000` | `.out` | Raw telemetry from the SSR science partition. Data from instruments operating in parallel are interleaved. (Binary)
2 | Recorded Engineering Data |  `E0000` `C0000` | `.out` | Engineering telemetry from the SSR engineering partition. Data are in engineering units, collected from tens of thousands of telemetry points on the spacecraft and within the instruments. (Binary)
3 | Observatory Status File |
| `_osf.xml` | Summary of instrument and spacecraft activities, in time order (XML)
4 | Observatory Ephemeris* | `JWST_` | `.OEM` | Either predicted or derived spacecraft position (km) and velocity (km/s) in X, Y, Z as a function of time (CSV)
15 | Processing Logs** |
| `.log` | Processing logs for the DMS Pipelines (ASCII)
100 | Diagnostics** |
| `.bin` | Currently, diagnostics related to the MIRI grating wheel
*The coordinate system for the ephemeris data is
**Product filenames do not contain date-time sub-string.
Enter the name(s) for one or more files in the **Filename** dialog box to match files of interest. A list of filenames can be entered on separate rows in the dialog box. If you wish to select a range of similar names, you can create a _filename pattern_ using a limited set of special characters to match or exclude sub-strings within a filename. The special characters are given below, and are interpreted syntactically within the context of a limited form of regular expressions (`re`).
Syntax | Meaning
---|---
% | Matches any substring
`*` | Matches any substring
`[aeiou]` | Matches any character in the listed set
`[^XYZ]` | Matches any character _not_ in the listed set
`[a-z0-9]` | The set of characters can include a range or multiple ranges
The article [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions), which describes filename matching in the Mission MAST [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay), includes detailed examples of how to use the `re` syntax. But be aware of important differences:
* there is no implied wildcard at the beginning or end of a filename pattern (though you can add them explicitly)
* more than one wildcard character may appear in the pattern
* the following symbols are interpreted literally
* **`!`**does not mean logical negation
* **$** does not denote the end of the string
* **`\`**(backslash) is not a means to escape special characters  
Filename matching is not case sensitive.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 3": "File list upload"} -->
File names or name patterns can be stored in a file and uploaded to the **Filename** dialog box by clicking the **UPLOAD FILE NAME LIST** button. The results of the upload is shown in Fig. 2, below. Note that the patterns must be given one per line in the uploaded file.  
![](https://outerspace.stsci.edu/download/attachments/333677647/dialog_Cassi-Jwst_filePattern.png?version=1&modificationDate=1752672416174&api=v2)
**Figure 2.** Filename matching dialog box, after uploading a list of filename patterns from a local file.
* * *
A successful search will result in a table of results, one file per row, as shown in Fig. 3 below.  
![](https://outerspace.stsci.edu/download/attachments/333677647/window_cassi-Jwst_SuppTelm_Results.png?version=1&modificationDate=1752158083367&api=v2)
**Figure 3.** Results window for the search for supplemental engineering. After selecting one or more results (rows with checked boxes and light-blue background), the file(s) may be downloaded via a method selected from the **Download Data** menu.
Only the first 5000 matching results will be accessible in the results window. If the number of potential matches equals or exceeds this limit you will need to click the **EDIT SEARCH** button and narrow your search criteria.
Various elements of the results table are described in the article [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page), including:
* revising the parameters of the search and re-executing
* exporting the results table to a file
* selecting table rows
* navigating to pages in the results table  
Choose the files of interest for download, then click the **Download Data** button to select the retrieval method.
Large Downloads
If the combined size of the selected data files is large (>1 GB), we recommend downloading the retrieval script and running it on your machine to minimize the chance of server-side timeouts or other transfer problems.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 3": "Product download API"} -->
In addition to downloading the files via the browser window, you may choose to download a retrieval script.
![](https://outerspace.stsci.edu/download/attachments/333677647/dlo_jwst-supp_downloadScript.png?version=1&modificationDate=1752160031978&api=v2)
Selecting the API Script/Curl option will bring up a set of curl commands (one per file), which you can copy to your screen buffer, or download to your machine as a **bash** script. Run the script with a command similar to the following:
```
bash MAST_2025-03-24T191812_retrieve.sh
```  
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
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
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [Cloud Science Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797523/Cloud+Science+Platforms "Cloud Science Platforms")
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
Authorized users may access and retrieve selected telemetry and supplemental JWST data product types using the CaSSI web interface, or with curl commands.
**On this page...**
* 1[Product Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-ProductSearch)
* 1.1[Date of relevance](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-jw_ns_dateDateofrelevance)
* 1.2[Product File Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-jw_eng_prodTypeProductFileType)
* 1.3[Filename pattern](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-FileNamePatternFilenamepattern)
* 2[Retrieve Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-jw_ns_retrieveRetrieveData)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products#JWSTSupplementalProducts-ForFurtherReading...)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Product Search"} -->
The MAST CaSSI web interface includes a [search form](https://mast.stsci.edu/cassi/#/jwst) for a subset of restricted JWST data products, including raw science and engineering telemetry downlinked from the spacecraft. The web search interface is shown in Fig. 1. The various search parameters are described in the following subsections.
Searches for the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to search for or access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to search these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.  
![](https://outerspace.stsci.edu/download/attachments/333677647/window_Cassi-Jwst_SuppTelm.png?version=1&modificationDate=1752610506793&api=v2)
![](https://outerspace.stsci.edu/download/attachments/333677647/menu_dataGroup_CaSSI.png?version=1&modificationDate=1752610720882&api=v2)
**Figure 1.** CaSSI interface (_above_), and the Data Group selector within it (_below_) to search for JWST supplemental and telemetry files. The message **Filtered results:** at the bottom of the window dynamically updates the count of all files that match as values are entered for the search parameters.
Use the **Date** dialog box to select files that pertain to a date of interest. The date that applies to these products is currently derived from date substring embedded in the file name. Note that the contents within the files may span a date boundary.
![](https://outerspace.stsci.edu/download/thumbnails/333677647/datePicker_Cassi-Jwst.png?version=1&modificationDate=1752613708351&api=v2)
Click the date picker icon (![](https://outerspace.stsci.edu/download/thumbnails/333677647/icon_datePicker.png?version=1&modificationDate=1752613500662&api=v2)) and choose a year/day/month from the calendar, as shown at left, or simply type the date into the dialog box, in YYYY-MM-DD format.
Since not all file types include an embedded date string, choosing a date will implicitly exclude these file types from your search.
You may constrain a product search to one or more of the supported file types, which are listed in the table below. The default (i.e., no types selected) is to match any file type. File prefix characters are given when they apply to all files of a given type.
Prod. ID | Product | File Prefix | File Suffix | Description
---|---|---|---|---
1 | Recorded Science Data | `S0000` | `.out` | Raw telemetry from the SSR science partition. Data from instruments operating in parallel are interleaved. (Binary)
2 | Recorded Engineering Data |  `E0000` `C0000` | `.out` | Engineering telemetry from the SSR engineering partition. Data are in engineering units, collected from tens of thousands of telemetry points on the spacecraft and within the instruments. (Binary)
3 | Observatory Status File |
| `_osf.xml` | Summary of instrument and spacecraft activities, in time order (XML)
4 | Observatory Ephemeris* | `JWST_` | `.OEM` | Either predicted or derived spacecraft position (km) and velocity (km/s) in X, Y, Z as a function of time (CSV)
15 | Processing Logs** |
| `.log` | Processing logs for the DMS Pipelines (ASCII)
100 | Diagnostics** |
| `.bin` | Currently, diagnostics related to the MIRI grating wheel
*The coordinate system for the ephemeris data is
**Product filenames do not contain date-time sub-string.
Enter the name(s) for one or more files in the **Filename** dialog box to match files of interest. A list of filenames can be entered on separate rows in the dialog box. If you wish to select a range of similar names, you can create a _filename pattern_ using a limited set of special characters to match or exclude sub-strings within a filename. The special characters are given below, and are interpreted syntactically within the context of a limited form of regular expressions (`re`).
Syntax | Meaning
---|---
% | Matches any substring
`*` | Matches any substring
`[aeiou]` | Matches any character in the listed set
`[^XYZ]` | Matches any character _not_ in the listed set
`[a-z0-9]` | The set of characters can include a range or multiple ranges
The article [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions), which describes filename matching in the Mission MAST [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay), includes detailed examples of how to use the `re` syntax. But be aware of important differences:
* there is no implied wildcard at the beginning or end of a filename pattern (though you can add them explicitly)
* more than one wildcard character may appear in the pattern
* the following symbols are interpreted literally
* **`!`**does not mean logical negation
* **$** does not denote the end of the string
* **`\`**(backslash) is not a means to escape special characters  
Filename matching is not case sensitive.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 3": "File list upload"} -->
File names or name patterns can be stored in a file and uploaded to the **Filename** dialog box by clicking the **UPLOAD FILE NAME LIST** button. The results of the upload is shown in Fig. 2, below. Note that the patterns must be given one per line in the uploaded file.  
![](https://outerspace.stsci.edu/download/attachments/333677647/dialog_Cassi-Jwst_filePattern.png?version=1&modificationDate=1752672416174&api=v2)
**Figure 2.** Filename matching dialog box, after uploading a list of filename patterns from a local file.
* * *
A successful search will result in a table of results, one file per row, as shown in Fig. 3 below.  
![](https://outerspace.stsci.edu/download/attachments/333677647/window_cassi-Jwst_SuppTelm_Results.png?version=1&modificationDate=1752158083367&api=v2)
**Figure 3.** Results window for the search for supplemental engineering. After selecting one or more results (rows with checked boxes and light-blue background), the file(s) may be downloaded via a method selected from the **Download Data** menu.
Only the first 5000 matching results will be accessible in the results window. If the number of potential matches equals or exceeds this limit you will need to click the **EDIT SEARCH** button and narrow your search criteria.
Various elements of the results table are described in the article [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page), including:
* revising the parameters of the search and re-executing
* exporting the results table to a file
* selecting table rows
* navigating to pages in the results table  
Choose the files of interest for download, then click the **Download Data** button to select the retrieval method.
Large Downloads
If the combined size of the selected data files is large (>1 GB), we recommend downloading the retrieval script and running it on your machine to minimize the chance of server-side timeouts or other transfer problems.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 3": "Product download API"} -->
In addition to downloading the files via the browser window, you may choose to download a retrieval script.
![](https://outerspace.stsci.edu/download/attachments/333677647/dlo_jwst-supp_downloadScript.png?version=1&modificationDate=1752160031978&api=v2)
Selecting the API Script/Curl option will bring up a set of curl commands (one per file), which you can copy to your screen buffer, or download to your machine as a **bash** script. Run the script with a command similar to the following:
```
bash MAST_2025-03-24T191812_retrieve.sh
```  
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission MAST Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 9 END -->

