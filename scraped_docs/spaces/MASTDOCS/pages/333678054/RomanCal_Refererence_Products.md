---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products"
date_accessed: "2026-03-11T11:36:07.230886"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Product Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-ProductSearch)
* 1.1[General Attribute Selectors](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-GeneralAttributeSelectors)
* 2[Retrieve Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-RetrieveData)
* 2.1[Pedigree](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-Pedigree)
* 2.2[Product Download API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-ProductDownloadAPI)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Product Search"} -->
The MAST CaSSI web interface includes a [search form](https://mast.stsci.edu/cassi/#/roman?dataGroup=SOC) for Roman calibration reference files, including all products delivered from ground calibrations onward. The web search interface is shown in Fig. 1. The various selectors are described in the following subsections.
Downloads of the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to access these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.  
![](https://outerspace.stsci.edu/download/attachments/333678054/window_romanSoc_CalRef.png?version=1&modificationDate=1749582458147&api=v2)
![](https://outerspace.stsci.edu/download/attachments/333678054/menu_dataGroup_roman-calRef.png?version=1&modificationDate=1749584909852&api=v2)
**Figure 1.** CaSSI interface (_above_), and the Data Group selector within it (_below_) to search for Roman/SOC calibration reference files.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "General Attribute Selectors"} -->
Most of the selectors for specifying search criteria are pull-down menus. You may select (![](https://outerspace.stsci.edu/download/thumbnails/333678054/button_selectAll.png?version=1&modificationDate=1749755787623&api=v2)) all or de-select (![](https://outerspace.stsci.edu/download/thumbnails/333678054/button_selectNone.png?version=1&modificationDate=1749755808388&api=v2)) all values at once. Note that if no value is chosen with a selector, the search will match any value for that selector. The following table gives a brief description of each attribute.
Selector | Description
---|---
Reference File Type | Type of calibration for which the file is used
Optical Element | Filter(s) or disperser(s) for which the reference file applies
Exposure Type | Type of exposure to which the reference file applies
Detector | Detector(s) in the focal plane array to which the reference file applies
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Retrieve Data"} -->
A successful search will result in a table of results, one file per row, as shown in Fig. 2, below.  
![](https://outerspace.stsci.edu/download/attachments/333678054/window_cassi-Roman_CalRef_results.png?version=1&modificationDate=1749750680173&api=v2)
**Figure 2.** Results table for Roman SOC calibration reference files, along with the pull-down menu for data download options.
Various elements of the results table are described in the article [Search Results Page](https://outerspace.stsci.edu/display/MASTDOCS/Search+Results+Page), including:
* revising the parameters of the search and re-executing
* exporting the results table to a file
* selecting table rows
* navigating to pages in the results table  
Choose the files of interest for download, then click the **Download Data** button.
Wildcards in results
Some fields in the results table will have a value **`*`**(asterisk). This indicates that the corresponding file is applicable for all possible values in that field.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Retrieve Data", "Header 2": "Pedigree"} -->
The calibration reference file types are distinguished by their pedigree, as described in the article [CRDS for Reference Files](https://roman-docs.stsci.edu/data-handbook-home/accessing-wfi-data/crds-for-reference-files) and summarized the the table below.
Pedigree | Description
---|---
dummy | Pixel values are arbitrary, but structure and metadata will be representative of genuine reference files of this type. Used for testing.
ground | Pixell values are derived from ground-based test data. Structure and metadata should be applicable for calibration of in-flight data.
simulation | Derived from simulated data. Structure and metadata may be applicable for calibration of in-flight data.
in-flight | Derived from in-flight data. Should be applicable in all respects for the stated interval of time.  
Large Downloads
If the combined size of the selected data files is large (>1 GB), download the retrieval script and run it on your machine to minimize the chance of server-side timeouts or other transfer problems.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Retrieve Data", "Header 2": "Product Download API"} -->
In addition to downloading the files via the browser window, you may choose to download a retrieval script.
![](https://outerspace.stsci.edu/download/attachments/333678054/dlo_APIquery.png?version=1&modificationDate=1749586906818&api=v2)  
Selecting the API Script/Curl option will bring up a set of curl commands (one per file), which you can copy to your screen buffer, or download to your machine as a **bash** script. Run the script with a command similar to the following:
```
bash MAST_2025-03-24T191812_retrieve.sh
```  
* * *

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* Roman calibration reference data system ([Roman: CRDS](https://roman-crds.stsci.edu/))
* [Mission MAST Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide)
* [CaSSI Manual](https://outerspace.stsci.edu/display/MASTDOCS/CaSSI+Manual)  
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
**On this page...**
* 1[Product Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-ProductSearch)
* 1.1[General Attribute Selectors](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-GeneralAttributeSelectors)
* 2[Retrieve Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-RetrieveData)
* 2.1[Pedigree](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-Pedigree)
* 2.2[Product Download API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-ProductDownloadAPI)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products#RomanCalRefererenceProducts-ForFurtherReading...)

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Product Search"} -->
The MAST CaSSI web interface includes a [search form](https://mast.stsci.edu/cassi/#/roman?dataGroup=SOC) for Roman calibration reference files, including all products delivered from ground calibrations onward. The web search interface is shown in Fig. 1. The various selectors are described in the following subsections.
Downloads of the CaSSI products described here are restricted to authorized persons. This means you must have an account in [MyST](https://proper.stsci.edu/proper/authentication/auth), and be logged in to a MAST session to access these data via the Web interface. If you are using an API, such as [MAST API Tokens](https://auth.mast.stsci.edu/info) article for details.
If you believe you should be authorized to access these restricted products but cannot, contact Archive [User Support](https://outerspace.stsci.edu/display/RAPD/Roman+Archive+Pre-Launch+Documentation#RomanArchivePreLaunchDocumentation-User_support) to request authorization.  
![](https://outerspace.stsci.edu/download/attachments/333678054/window_romanSoc_CalRef.png?version=1&modificationDate=1749582458147&api=v2)
![](https://outerspace.stsci.edu/download/attachments/333678054/menu_dataGroup_roman-calRef.png?version=1&modificationDate=1749584909852&api=v2)
**Figure 1.** CaSSI interface (_above_), and the Data Group selector within it (_below_) to search for Roman/SOC calibration reference files.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Product Search", "Header 2": "General Attribute Selectors"} -->
Most of the selectors for specifying search criteria are pull-down menus. You may select (![](https://outerspace.stsci.edu/download/thumbnails/333678054/button_selectAll.png?version=1&modificationDate=1749755787623&api=v2)) all or de-select (![](https://outerspace.stsci.edu/download/thumbnails/333678054/button_selectNone.png?version=1&modificationDate=1749755808388&api=v2)) all values at once. Note that if no value is chosen with a selector, the search will match any value for that selector. The following table gives a brief description of each attribute.
Selector | Description
---|---
Reference File Type | Type of calibration for which the file is used
Optical Element | Filter(s) or disperser(s) for which the reference file applies
Exposure Type | Type of exposure to which the reference file applies
Detector | Detector(s) in the focal plane array to which the reference file applies
* * *

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Retrieve Data"} -->
A successful search will result in a table of results, one file per row, as shown in Fig. 2, below.  
![](https://outerspace.stsci.edu/download/attachments/333678054/window_cassi-Roman_CalRef_results.png?version=1&modificationDate=1749750680173&api=v2)
**Figure 2.** Results table for Roman SOC calibration reference files, along with the pull-down menu for data download options.
Various elements of the results table are described in the article [Search Results Page](https://outerspace.stsci.edu/display/MASTDOCS/Search+Results+Page), including:
* revising the parameters of the search and re-executing
* exporting the results table to a file
* selecting table rows
* navigating to pages in the results table  
Choose the files of interest for download, then click the **Download Data** button.
Wildcards in results
Some fields in the results table will have a value **`*`**(asterisk). This indicates that the corresponding file is applicable for all possible values in that field.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Retrieve Data", "Header 2": "Pedigree"} -->
The calibration reference file types are distinguished by their pedigree, as described in the article [CRDS for Reference Files](https://roman-docs.stsci.edu/data-handbook-home/accessing-wfi-data/crds-for-reference-files) and summarized the the table below.
Pedigree | Description
---|---
dummy | Pixel values are arbitrary, but structure and metadata will be representative of genuine reference files of this type. Used for testing.
ground | Pixell values are derived from ground-based test data. Structure and metadata should be applicable for calibration of in-flight data.
simulation | Derived from simulated data. Structure and metadata may be applicable for calibration of in-flight data.
in-flight | Derived from in-flight data. Should be applicable in all respects for the stated interval of time.  
Large Downloads
If the combined size of the selected data files is large (>1 GB), download the retrieval script and run it on your machine to minimize the chance of server-side timeouts or other transfer problems.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Retrieve Data", "Header 2": "Product Download API"} -->
In addition to downloading the files via the browser window, you may choose to download a retrieval script.
![](https://outerspace.stsci.edu/download/attachments/333678054/dlo_APIquery.png?version=1&modificationDate=1749586906818&api=v2)  
Selecting the API Script/Curl option will bring up a set of curl commands (one per file), which you can copy to your screen buffer, or download to your machine as a **bash** script. Run the script with a command similar to the following:
```
bash MAST_2025-03-24T191812_retrieve.sh
```  
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* Roman calibration reference data system ([Roman: CRDS](https://roman-crds.stsci.edu/))
* [Mission MAST Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide)
* [CaSSI Manual](https://outerspace.stsci.edu/display/MASTDOCS/CaSSI+Manual)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 13 END -->

