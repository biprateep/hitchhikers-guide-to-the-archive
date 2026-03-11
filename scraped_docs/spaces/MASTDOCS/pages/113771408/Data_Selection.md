---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection"
date_accessed: "2026-03-11T11:36:43.019224"
---

<!-- CHUNK 1 START -->
After a successful [search for data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search), and [browsing](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data) to determine which observations are of interest, the next step is to select particular data products for download. Since JWST provides many files per observation, it is especially important to carefully choose the products that are most relevant for your science goals.
**On this page...**
* 1[File Selector](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-FileSelector)
* 1.1[Filtering](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-Filtering)
* 1.2[Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-Cal_RefCalibrationReferenceFiles)
* 2[Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-DataRetrieval)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "File Selector"} -->
The Portal **Download Manager** window provides mechanisms to select which files will be packaged for download. Careful file selection is especially important for JWST Observations because so many science and supplemental files (often hundreds, or even thousands) may be related to one another. Use the file browser tree in the '**Files'** panel (at right, in the image below) to select files, or directories of files, using the checkboxes.See the [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) article in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) for details.  
![](https://outerspace.stsci.edu/download/attachments/113771408/DLM_file_selector.png?version=2&modificationDate=1660921098575&api=v2)
The file navigation panel in the Portal **Download Manager** window. Check boxes in the **Filters** panel (_left_) to select which product types, categories, file extensions, etc. to display in the **Files** panel (_right_). Select individual files or directories of files in the **Files** panel by checking the adjacent boxes.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "File Selector", "Header 2": "Filtering"} -->
It is common with JWST queries to find very large numbers of files that are related to even a single Observation. The **Filters** panel provides a way to hide many categories of files that may not be of scientific interest, such as auxiliary products (which include guide star data), preview images, and the like (see [Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products) for details of non-science data products). Filtering makes the process of excluding unwanted files vastly more efficient.
Use care when filtering
The default setting for the __Recommended Products__ filter is that only [Minimum Recommended Products](https://outerspace.stsci.edu/display/MASTDOCS/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts) (usually Level-3) are displayed. This has the effect of hiding all lower-level products, including the contributing L-2b (fully calibrated per detector) files which may be useful for scientific analysis. See [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) to learn more about JWST product levels. It also has the effect of suppressing the ability to select static calibration reference files (see below).
Removing Files from the Basket
If the number of files is so large as to make file selection confusing, you may elect to first filter for files of no interest (for example, guide-star products), select them, and remove them entirely from the download basket by clicking the **Remove Selected** button in the upper left of the window. Then resume filtering for files of interest.
![](https://outerspace.stsci.edu/download/thumbnails/113771408/Screenshot%202021-10-07%20at%2011-42-25%20STScI%20Mikulski%20Archive%20for%20Space%20Telescopes%20%28MAST%29%20Portal.png?version=1&modificationDate=1633621568831&api=v2)

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "File Selector", "Header 2": "Calibration Reference Files"} -->
Click the **Retrieve References** button to retrieve the static This action will bring up a file selector sub-menu to select files to add to your basket. For the step-by-step guide for reference product retrieval, see the MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) chapter on retrieving[ ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data)[Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files).
![](https://outerspace.stsci.edu/download/thumbnails/113771408/button_retrieveRefs.png?version=1&modificationDate=1633635204247&api=v2)
You must **_uncheck_** the __MRP__ filter check box **_and_** select at least one calibrated product for the Retrieve References to be active. Note that after you add reference files to the Basket (in the sub-panel), you must then select them in the **Download Manager** to be included in the download bundle.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Data Retrieval"} -->
After selecting all files of interest, they may be downloaded via one of the available methods. Click either the **Download** button or the **Batch Retrieval** button![](https://outerspace.stsci.edu/download/thumbnails/113771408/button_download-batch.png?version=1&modificationDate=1633625944009&api=v2); see the [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval) article, or the [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data) chapter of the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide).

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* The MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide), especially the articles:  
* [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket)
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods)
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files)
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval)  
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
After a successful [search for data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search), and [browsing](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data) to determine which observations are of interest, the next step is to select particular data products for download. Since JWST provides many files per observation, it is especially important to carefully choose the products that are most relevant for your science goals.
**On this page...**
* 1[File Selector](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-FileSelector)
* 1.1[Filtering](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-Filtering)
* 1.2[Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-Cal_RefCalibrationReferenceFiles)
* 2[Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-DataRetrieval)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection#DataSelection-ForFurtherReading...)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "File Selector"} -->
The Portal **Download Manager** window provides mechanisms to select which files will be packaged for download. Careful file selection is especially important for JWST Observations because so many science and supplemental files (often hundreds, or even thousands) may be related to one another. Use the file browser tree in the '**Files'** panel (at right, in the image below) to select files, or directories of files, using the checkboxes.See the [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) article in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) for details.  
![](https://outerspace.stsci.edu/download/attachments/113771408/DLM_file_selector.png?version=2&modificationDate=1660921098575&api=v2)
The file navigation panel in the Portal **Download Manager** window. Check boxes in the **Filters** panel (_left_) to select which product types, categories, file extensions, etc. to display in the **Files** panel (_right_). Select individual files or directories of files in the **Files** panel by checking the adjacent boxes.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "File Selector", "Header 2": "Filtering"} -->
It is common with JWST queries to find very large numbers of files that are related to even a single Observation. The **Filters** panel provides a way to hide many categories of files that may not be of scientific interest, such as auxiliary products (which include guide star data), preview images, and the like (see [Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products) for details of non-science data products). Filtering makes the process of excluding unwanted files vastly more efficient.
Use care when filtering
The default setting for the __Recommended Products__ filter is that only [Minimum Recommended Products](https://outerspace.stsci.edu/display/MASTDOCS/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts) (usually Level-3) are displayed. This has the effect of hiding all lower-level products, including the contributing L-2b (fully calibrated per detector) files which may be useful for scientific analysis. See [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) to learn more about JWST product levels. It also has the effect of suppressing the ability to select static calibration reference files (see below).
Removing Files from the Basket
If the number of files is so large as to make file selection confusing, you may elect to first filter for files of no interest (for example, guide-star products), select them, and remove them entirely from the download basket by clicking the **Remove Selected** button in the upper left of the window. Then resume filtering for files of interest.
![](https://outerspace.stsci.edu/download/thumbnails/113771408/Screenshot%202021-10-07%20at%2011-42-25%20STScI%20Mikulski%20Archive%20for%20Space%20Telescopes%20%28MAST%29%20Portal.png?version=1&modificationDate=1633621568831&api=v2)

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "File Selector", "Header 2": "Calibration Reference Files"} -->
Click the **Retrieve References** button to retrieve the static This action will bring up a file selector sub-menu to select files to add to your basket. For the step-by-step guide for reference product retrieval, see the MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) chapter on retrieving[ ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data)[Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files).
![](https://outerspace.stsci.edu/download/thumbnails/113771408/button_retrieveRefs.png?version=1&modificationDate=1633635204247&api=v2)
You must **_uncheck_** the __MRP__ filter check box **_and_** select at least one calibrated product for the Retrieve References to be active. Note that after you add reference files to the Basket (in the sub-panel), you must then select them in the **Download Manager** to be included in the download bundle.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Data Retrieval"} -->
After selecting all files of interest, they may be downloaded via one of the available methods. Click either the **Download** button or the **Batch Retrieval** button![](https://outerspace.stsci.edu/download/thumbnails/113771408/button_download-batch.png?version=1&modificationDate=1633625944009&api=v2); see the [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval) article, or the [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data) chapter of the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide).

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* The MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide), especially the articles:  
* [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket)
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods)
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files)
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

