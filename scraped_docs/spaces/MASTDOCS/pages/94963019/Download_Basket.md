---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket"
date_accessed: "2026-03-11T11:32:39.065451"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Download Manager Window](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DownloadManagerWindow)
* 1.1[Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DownloadFiltersPanelFilters)
* 1.1.1[Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-MRPRecommendedProducts)
* 1.1.2[Data Product Category](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DPCDataProductCategory)
* 1.1.3[Data Product Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DataProductType)
* 1.1.4[File Extensions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-FileExtensions)
* 1.1.5[Batch Download Availability](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-BatchDownloadAvailability)
* 1.1.6[Data Product Group](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DataProductGroup)
* 1.2[File Selector](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-FileSelector)
* 1.3[File Details](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-FileDetails)
* 1.4[Action Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-ActionBar)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Download Manager Window"} -->
Once observations have been placed in the Portal Download Basket (see [Marking Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data#BrowsingData-MarkingResults)), select which files to retrieve and the method of retrieval using the _**Download Manager**_ window, as shown in the figure below. The workflow is:
1. Use filters to select subsets of files
2. Use checkboxes in the file selector to fine-tune the set of files for download
1. Optionally click _**Retrieve References**_ to include applicable [calibration reference files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files) in the download
3. Select a download method from the _**Action Bar**_.  
![Portal download manager window](https://outerspace.stsci.edu/download/attachments/94963019/panel_dlm.png?version=1&modificationDate=1615210330324&api=v2)
The **Download Manager** window is divided into 4 sections: the **Action Bar** (_top_), the **Filters** panel (_left_), the **Files** selector panel (_middle_), and a **Details** panel (_right_) to view information about each file.
Download History
The Portal preserves a history of your downloads; this history will persist across sessions if you are logged in. Click the **Download History** tab at the upper left to revisit downloads you have requested in the past. You may filter the selected files just as with the **Download Basket** window.
Only a few observations can result in hundreds of primary and associated data files in the download basket. Using one or more filters provide a quick way to exclude from view large numbers of files that may be of little interest to a user, and make it easier to select data products of interest. The filters are grouped on the left-hand side of the screen, and are described below.
![Minimum recommended products filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_MRP.png?version=1&modificationDate=1615210330327&api=v2)
When selecting products for retrieval, by default only a subset of available products are exposed: those deemed to be most essential. These [_**Minimum Recommended Products**_](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products) (MRP) are selected with a Filter checkbox. This selection:
1. Exposes data products that are most relevant for science analysis
2. Reduces the volume of (often large) files to be transferred to your machine.  
Users who wish to select all available products may do so after un-checking the MRP box. This selection will be remembered for subsequent downloads during the same Portal session.
![Product category filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlmProductCategory.png?version=1&modificationDate=1615210330335&api=v2)
Data products are categorized in the MAST database according to their intended use. The set of categories displayed depends somewhat on the specific mission.
Category | Semantic Content
---|---
Auxiliary | Guide-Star products, processing logs, pre-images for target selection, Micro-shutter array metadata (for JWST), processing logs, telemetry files, etc.
Science | Science data products: the most calibrated* products (if the MRP box is checked), plus raw and some intermediate products (if the MRP box is un-checked)
Catalog | Source catalogs containing position, brightness, and other information.
Calibration | If calibration files have been added to the download basket for one or more observations, they will appear in this category.
Preview | These thumbnail images are mostly useful for quick visualizations of available products in MAST. They are generated for all FITS image-type science products.
Info | For JWST, these products are essential for users to re-process data on their own compute platforms, or for understanding in detail how high-level products were produced from contributing low-level products.
*The term "most calibrated" means an endpoint of the calibration pipeline, exclusive of intermediate products.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "Data Product Type"} -->
![Product type filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlm_productType.png?version=1&modificationDate=1615210330345&api=v2)
This filter distinguishes between primary science products and the calibration reference files that were used to produce one or more of them.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "File Extensions"} -->
![File extension filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlmExtension.png?version=1&modificationDate=1615210330330&api=v2)
The file extension indicates the internal file organization and provides a clue about what type of software is necessary to understand the file format. Most types will be familiar to users:
Extension | Description
---|---
`.fits` | Scientific data products in FITS format.
`.jpg` | Preview image, generally of a FITS data product, in JPEG format
`.png` | Preview/thumbnail in PNG format
`.csv` | Comma-separated variable structure in ASCII
`.ecsv` | Enhanced CSV format (i.e., also contains metadata)
`.json` | Structured ASCII data in JSON format

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "Batch Download Availability"} -->
![Filter for retrieval via batch](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlm_batchAvail.png?version=1&modificationDate=1615210330347&api=v2)
Files from certain missions (including HST and JWST) can be downloaded in batch (i.e., by staging to an ftp area for later retrieval). Files from other missions must be fetched with a different [retrieval method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods).

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "Data Product Group"} -->
![Data product group filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlmGroup.png?version=1&modificationDate=1615210330333&api=v2)
The file group indicates the semantic content of the file. It is a suffix to the filename and for most missions is preceded by an underscore, and followed by a period and the file extension. There are dozens of groups; the set of group names presented depends upon the mission, instrument, and the processing pipeline used to produce the data.
* * *

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 2": "File Selector"} -->
![File selector panel](https://outerspace.stsci.edu/download/thumbnails/94963019/fileNav_dlm.png?version=1&modificationDate=1615210330338&api=v2)
The file selector presents only those data products in the download basket that match the **filter** selections (see above). The files are organized in a hierarchical directory structure where clicking the little triangles on the left exposes the contents of each directory. Click the check-boxes to select individual files, or to select all files within a given directory, as shown at left. Only selected files will be packaged for download.' Click a file name to display detailed information about that file.
* * *

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 2": "File Details"} -->
![File details panel](https://outerspace.stsci.edu/download/thumbnails/94963019/panel_dlm_Details.png?version=1&modificationDate=1615210330322&api=v2)
Click any file name in the file selector to display details such as a brief description of the product, including the proposal/program ID, the version of the calibration pipeline used to produce the file, and the size in bytes.
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 2": "Action Bar"} -->
![Retrieve calibration reference files button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_dlm_references.png?version=1&modificationDate=1615210330300&api=v2)
![Download button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_dlm_download.png?version=1&modificationDate=1615210330307&api=v2)
![Retrieve via batch button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_dlm_batch.png?version=1&modificationDate=1615210330319&api=v2)
![Remove all entries from basket button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_RemoveAll.png?version=1&modificationDate=1615210330340&api=v2)
![Remove selected entries from basket button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_RemoveSelected.png?version=1&modificationDate=1615210330342&api=v2)
The action bar displays the total number of files in the basket, as well as the approximate size of the selected files. Once at least one file is selected, the action bar includes buttons for:
* retrieving [calibration reference files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files). This button is only enabled if the __Minimum Recommended Products__ box is unchecked. Clicking it brings up another file panel to select applicable calibration files; then you must add them explicitly to your cart.
* choosing a method for downloading the selected files (see [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods) for details)
* an option for "batch" downloads (i.e., by staging them on an ftp server for later retrieval)  
You can also remove some or all items from the basket.
Bundle Size Limit
File bundles larger than approximately 50 GB are too large to manage through a browser, and must be downloaded using the batch method or a bash (curl) script. Very large bundles typically transfer very slowly, so non-browser options are encouraged in these cases.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files)
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [Introduction to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962826/Introduction+to+the+Portal "Introduction to the Portal")
* [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching "Searching")
* [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search "Basic Search")
* [Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search "Advanced Search")
* [Catalog Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search "Catalog Search")
* [Search a List of Targets](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets "Search a List of Targets")
* [Special Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches "Special Searches")
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data "Browsing Data")
* [Search Results Grid](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962944/Search+Results+Grid "Search Results Grid")
* [Refining Results with Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962974/Refining+Results+with+Filters "Refining Results with Filters")
* [Data Browsing Tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962980/Data+Browsing+Tools "Data Browsing Tools")
* [AstroView](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962998/AstroView "AstroView")
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
* [One-Click Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963013/One-Click+Download "One-Click Download")
* [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket "Download Basket")
* [Minimum Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products "Minimum Recommended Products")
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files "Calibration Reference Files")
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods "Retrieval Methods")
* [The Download Bundle](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963052/The+Download+Bundle "The Download Bundle")
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
* [Minimum Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products "Minimum Recommended Products")
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files "Calibration Reference Files")
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
* 1[Download Manager Window](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DownloadManagerWindow)
* 1.1[Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DownloadFiltersPanelFilters)
* 1.1.1[Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-MRPRecommendedProducts)
* 1.1.2[Data Product Category](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DPCDataProductCategory)
* 1.1.3[Data Product Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DataProductType)
* 1.1.4[File Extensions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-FileExtensions)
* 1.1.5[Batch Download Availability](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-BatchDownloadAvailability)
* 1.1.6[Data Product Group](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-DataProductGroup)
* 1.2[File Selector](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-FileSelector)
* 1.3[File Details](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-FileDetails)
* 1.4[Action Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-ActionBar)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket#DownloadBasket-ForFurtherReading...)

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Download Manager Window"} -->
Once observations have been placed in the Portal Download Basket (see [Marking Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data#BrowsingData-MarkingResults)), select which files to retrieve and the method of retrieval using the _**Download Manager**_ window, as shown in the figure below. The workflow is:
1. Use filters to select subsets of files
2. Use checkboxes in the file selector to fine-tune the set of files for download
1. Optionally click _**Retrieve References**_ to include applicable [calibration reference files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files) in the download
3. Select a download method from the _**Action Bar**_.  
![Portal download manager window](https://outerspace.stsci.edu/download/attachments/94963019/panel_dlm.png?version=1&modificationDate=1615210330324&api=v2)
The **Download Manager** window is divided into 4 sections: the **Action Bar** (_top_), the **Filters** panel (_left_), the **Files** selector panel (_middle_), and a **Details** panel (_right_) to view information about each file.
Download History
The Portal preserves a history of your downloads; this history will persist across sessions if you are logged in. Click the **Download History** tab at the upper left to revisit downloads you have requested in the past. You may filter the selected files just as with the **Download Basket** window.
Only a few observations can result in hundreds of primary and associated data files in the download basket. Using one or more filters provide a quick way to exclude from view large numbers of files that may be of little interest to a user, and make it easier to select data products of interest. The filters are grouped on the left-hand side of the screen, and are described below.
![Minimum recommended products filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_MRP.png?version=1&modificationDate=1615210330327&api=v2)
When selecting products for retrieval, by default only a subset of available products are exposed: those deemed to be most essential. These [_**Minimum Recommended Products**_](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products) (MRP) are selected with a Filter checkbox. This selection:
1. Exposes data products that are most relevant for science analysis
2. Reduces the volume of (often large) files to be transferred to your machine.  
Users who wish to select all available products may do so after un-checking the MRP box. This selection will be remembered for subsequent downloads during the same Portal session.
![Product category filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlmProductCategory.png?version=1&modificationDate=1615210330335&api=v2)
Data products are categorized in the MAST database according to their intended use. The set of categories displayed depends somewhat on the specific mission.
Category | Semantic Content
---|---
Auxiliary | Guide-Star products, processing logs, pre-images for target selection, Micro-shutter array metadata (for JWST), processing logs, telemetry files, etc.
Science | Science data products: the most calibrated* products (if the MRP box is checked), plus raw and some intermediate products (if the MRP box is un-checked)
Catalog | Source catalogs containing position, brightness, and other information.
Calibration | If calibration files have been added to the download basket for one or more observations, they will appear in this category.
Preview | These thumbnail images are mostly useful for quick visualizations of available products in MAST. They are generated for all FITS image-type science products.
Info | For JWST, these products are essential for users to re-process data on their own compute platforms, or for understanding in detail how high-level products were produced from contributing low-level products.
*The term "most calibrated" means an endpoint of the calibration pipeline, exclusive of intermediate products.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "Data Product Type"} -->
![Product type filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlm_productType.png?version=1&modificationDate=1615210330345&api=v2)
This filter distinguishes between primary science products and the calibration reference files that were used to produce one or more of them.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "File Extensions"} -->
![File extension filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlmExtension.png?version=1&modificationDate=1615210330330&api=v2)
The file extension indicates the internal file organization and provides a clue about what type of software is necessary to understand the file format. Most types will be familiar to users:
Extension | Description
---|---
`.fits` | Scientific data products in FITS format.
`.jpg` | Preview image, generally of a FITS data product, in JPEG format
`.png` | Preview/thumbnail in PNG format
`.csv` | Comma-separated variable structure in ASCII
`.ecsv` | Enhanced CSV format (i.e., also contains metadata)
`.json` | Structured ASCII data in JSON format

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "Batch Download Availability"} -->
![Filter for retrieval via batch](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlm_batchAvail.png?version=1&modificationDate=1615210330347&api=v2)
Files from certain missions (including HST and JWST) can be downloaded in batch (i.e., by staging to an ftp area for later retrieval). Files from other missions must be fetched with a different [retrieval method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods).

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 3": "Data Product Group"} -->
![Data product group filter](https://outerspace.stsci.edu/download/thumbnails/94963019/filter_dlmGroup.png?version=1&modificationDate=1615210330333&api=v2)
The file group indicates the semantic content of the file. It is a suffix to the filename and for most missions is preceded by an underscore, and followed by a period and the file extension. There are dozens of groups; the set of group names presented depends upon the mission, instrument, and the processing pipeline used to produce the data.
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 2": "File Selector"} -->
![File selector panel](https://outerspace.stsci.edu/download/thumbnails/94963019/fileNav_dlm.png?version=1&modificationDate=1615210330338&api=v2)
The file selector presents only those data products in the download basket that match the **filter** selections (see above). The files are organized in a hierarchical directory structure where clicking the little triangles on the left exposes the contents of each directory. Click the check-boxes to select individual files, or to select all files within a given directory, as shown at left. Only selected files will be packaged for download.' Click a file name to display detailed information about that file.
* * *

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 2": "File Details"} -->
![File details panel](https://outerspace.stsci.edu/download/thumbnails/94963019/panel_dlm_Details.png?version=1&modificationDate=1615210330322&api=v2)
Click any file name in the file selector to display details such as a brief description of the product, including the proposal/program ID, the version of the calibration pipeline used to produce the file, and the size in bytes.
* * *

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Download Manager Window", "Header 2": "Action Bar"} -->
![Retrieve calibration reference files button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_dlm_references.png?version=1&modificationDate=1615210330300&api=v2)
![Download button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_dlm_download.png?version=1&modificationDate=1615210330307&api=v2)
![Retrieve via batch button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_dlm_batch.png?version=1&modificationDate=1615210330319&api=v2)
![Remove all entries from basket button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_RemoveAll.png?version=1&modificationDate=1615210330340&api=v2)
![Remove selected entries from basket button](https://outerspace.stsci.edu/download/thumbnails/94963019/button_RemoveSelected.png?version=1&modificationDate=1615210330342&api=v2)
The action bar displays the total number of files in the basket, as well as the approximate size of the selected files. Once at least one file is selected, the action bar includes buttons for:
* retrieving [calibration reference files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files). This button is only enabled if the __Minimum Recommended Products__ box is unchecked. Clicking it brings up another file panel to select applicable calibration files; then you must add them explicitly to your cart.
* choosing a method for downloading the selected files (see [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods) for details)
* an option for "batch" downloads (i.e., by staging them on an ftp server for later retrieval)  
You can also remove some or all items from the basket.
Bundle Size Limit
File bundles larger than approximately 50 GB are too large to manage through a browser, and must be downloaded using the batch method or a bash (curl) script. Very large bundles typically transfer very slowly, so non-browser options are encouraged in these cases.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files)
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 19 END -->

