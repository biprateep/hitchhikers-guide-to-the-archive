---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay"
date_accessed: "2026-03-11T11:34:21.681808"
---

<!-- CHUNK 1 START -->
Use the download overlay to refine your selection of specific files to retrieve, and to select a method for download.
**On this page...**
* 1[Download Overlay Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-DownloadOverlayOverview)
* 2[The Elements in Detail](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-TheElementsinDetail)
* 2.1[1: Selection Summary](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-1:SelectionSummary)
* 2.2[2: Quick Select Options](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-2:QuickSelectOptions)
* 2.3[3: Data Processing Levels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-3:DataProcessingLevels)
* 2.4[4: Guide Star Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-4:GuideStarFiles)
* 2.5[5: Regex Matching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-5:RegexMatching)
* 2.6[6: View and Export Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-6:ViewandExportSelection)
* 2.7[7: Download Folder Organization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-7:DownloadFolderOrganization)
* 2.8[8: Initiating the Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-8:InitiatingtheDownload)
* 3[Post-download: the Download Manifest](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-Post-download:theDownloadManifest)
* 3.1[Example 1: De-duplication](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-Example1:De-duplication)
* 3.2[Example 2: Exclusive Access Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-Example2:ExclusiveAccessData)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-further-readingForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Download Overlay Overview"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/panel_mmDLO.png?version=1&modificationDate=1698757510104&api=v2)
The download overlay, with selectors or action buttons in numbered boxes. The overlay selectors vary slightly among missions, as described below.
After choosing Datasets in the search window, use the **download overlay** panel to refine your selection of the underlying files. Use the selectors to refine the selection criteria, then use the action buttons to review the products and choose a method for downloading files.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail"} -->
The selector and action elements are described below.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "1: Selection Summary"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/status_selectionOverrview.png?version=1&modificationDate=1698757510149&api=v2)  
The selection overview displays the number and volume of files you've selected. It also displays the total number of files that are available for download. In this case, we've selected "All" but excluded guidestar files.
**Note:** If some selected files are not available to you due to an exclusive access restriction, you will get a warning with the number of files that have been excluded. You must log in using your MyST account and be authorized to retrieve them. See [Downloading Exclusive Access Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-dwld-eap) for more details.
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "2: Quick Select Options"} -->
![the three 'quick select' options: all, recommended, and none](https://outerspace.stsci.edu/download/thumbnails/107840400/quick-select.png?version=1&modificationDate=1698757509364&api=v2)
You can use the "quick selections" to do just that: quickly select a subset of files.
**All** will select all file categories across processing levels, but for JWST will _not_ include guidestar files. These must be added manually using the dedicated selector described below.
**None** clears all selections.
**Recommended** is the minimum set of files that are recommended for scientific analysis. This is a good shortcut for users are satisfied with the data calibration, but may not be applicable to your particular scientific needs.
* * *

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "3: Data Processing Levels"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/hst-download-selection.png?version=1&modificationDate=1706224154197&api=v2)  
This selector shows or hides types of products based on their classification as defined by the archive or mission pipelines. The example at left applies to the HST mission. You can select entire calibration levels (e.g "Uncalibrated"), as well as individual file types within those levels ("e.g. CSPEC_THUMB").
The suffix**CSPEC**), and is not the file extension (e.g., **`.fits`**). The specific product suffix depends on the instruments of each Mission. View the mission-specific conventions in[MAST Data Product Types](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963707/MAST+Data+Product+Types).

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "3: Data Processing Levels", "Header 3": "For HST"} -->
HST results now include data from [HASP, the Hubble Advanced Spectral Products](https://archive.stsci.edu/missions-and-data/hst/hasp). You will see this option available for most COS and STIS observations, in addition to the standard product levels.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "3: Data Processing Levels", "Header 3": "For JWST"} -->
An option to !["include calibration references files"](https://outerspace.stsci.edu/download/thumbnails/107840400/box_inclCalRefFiles.png?version=1&modificationDate=1698757510190&api=v2)will appear in the top right corner. This option provides the files necessary to run the calibration pipeline yourself.  
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "4: Guide Star Files"} -->
Note that this selector is only applicable to the JWST mission.
![](https://outerspace.stsci.edu/download/attachments/107840400/guidestar.png?version=1&modificationDate=1698757509446&api=v2)  
Guidestar files are not included by default, but may be selected. Only the highest calibration level of products are available.
* * *

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "5: Regex Matching"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/dialog_regex.png?version=1&modificationDate=1698757510005&api=v2)
Regular expressions are a powerful selection mechanism, and the Download Overlay supports [Regex in the Download Overlay Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions) for detailed examples.
* * *

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "6: View and Export Selection"} -->
![](https://outerspace.stsci.edu/download/thumbnails/107840400/button_viewFiles.png?version=1&modificationDate=1698757509789&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/107840400/button_exportFileList.png?version=1&modificationDate=1698757509831&api=v2)  
**View All Selected Files** will open a preview of the files you've selected so far. This is particularly useful if you have entered a regular expression (see above).
**Export Selected File List** saves this list of files as a CSV file, with columns corresponding to those displayed in the preview. See the corresponding sections below for more details on both.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "6: View and Export Selection", "Header 3": "6.1 The Preview and Pagination"} -->
![a sample preview of selected files. five files are visible](https://outerspace.stsci.edu/download/attachments/107840400/selection-preview.png?version=1&modificationDate=1698757509581&api=v2)
When previewing file metadata, the filenames are separated into groups based on the parent Datasets.  
Large numbers of products will span multiple pages. The current product range and total number of products are displayed at the bottom of the product-selection table. Paging controls can be modified to navigate more efficiently.
**Note:** not all metadata are visible in the graphic shown at left. It may be necessary for you to scroll horizontally to see all metadata.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "6: View and Export Selection", "Header 3": "6.2 Exporting to CSV"} -->
**Example CSV export**
```
Dataset,Filename,Product Level,Suffix,Instrument,Filter / Grating
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_cal.fits,2b,_cal,NIRISS,NIS_SOSSTA
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_uncal.fits,1b,_uncal,NIRISS,NIS_SOSSTA
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_rate.fits,2a,_rate,NIRISS,NIS_SOSSTA
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_rateints.fits,2a,_rateints,NIRISS,NIS_SOSSTA
jw02734-o002_t002_niriss,jw02734-o002_t002_niriss_clear-gr700xd-substrip256_x1dints.fits,3,_x1dints,NIRISS,NIS_SUBSTRIP256
```  
The file list can also be exported to CSV format. However, the CSV differs slightly: it does not visually separate files based on the parent Dataset ID. Instead, each row begins with the Dataset ID corresponding to the product filename.
Some column names contain spaces; this table should only be parsed using commas.
* * *

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "7: Download Folder Organization"} -->
![the option for file structure; the options are 'flat' and 'nested'](https://outerspace.stsci.edu/download/attachments/107840400/flat-or-nested.png?version=1&modificationDate=1698757509539&api=v2)
![](https://outerspace.stsci.edu/download/attachments/107840400/nested.png?version=1&modificationDate=1698757509702&api=v2)
![](https://outerspace.stsci.edu/download/attachments/107840400/flat.png?version=1&modificationDate=1698757509741&api=v2)
You may choose a __NESTED__ structure, where the main folder contains subdirectories for each parent dataset where the related files are located (middle-left graphic).
Or choose a  __FLAT__ directory structure, where files appear at the top of the download folder tree (lower-left graphic).
* * *

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "8: Initiating the Download"} -->
![Start Download button, to initiate file downloads](https://outerspace.stsci.edu/download/thumbnails/107840400/button_startDownload.png?version=1&modificationDate=1698757509873&api=v2)  
![API Query button, to generate a bash script containing commands to retreive files](https://outerspace.stsci.edu/download/thumbnails/107840400/button_apiQ.png?version=1&modificationDate=1698757509914&api=v2)
**START DOWNLOAD** will initiate a streaming file retrieval through the browser and produce a local ZIP file with the results. Note that the download location is set by the preference settings of the web browser. Some browsers allow a choice of download location; otherwise, the ZIP file will be downloaded to your default location.
**API QUERY** will generate a bash script of curl commands that you can use to retrieve files at a later time. This may be the only option for a large file payload (>1.0 TB uncompressed), and is more robust on slow connections.
To download non-public products via API Query, an Auth.MAST token must be created and provided to the generated script when prompted. You will only be prompted for this Auth.MAST token if there are non-public products requested for download. For more information on Auth.MAST tokens, please visit the [Auth.MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts#MASTAccounts-auth-mast) documentation.
![A yellow padlock, followed by a warning that exclusive access files are not selected](https://outerspace.stsci.edu/download/thumbnails/107840400/eap-files.png?version=1&modificationDate=1698757509319&api=v2)  
![Mission search login menu](https://outerspace.stsci.edu/download/thumbnails/107840400/menu_login.png?version=1&modificationDate=1698757510055&api=v2)
Some new data from Hubble and JWST are temporarily available only to the Investigator teams, which is indicated with a **yellow lock symbol and a warning**. These products will appear in the total file count, but will not be available to download except to signed-in, authorized users.
You will need to be logged in (see pull-down menu at upper-right) and be authorized to retrieve EA files. See [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts) for details.
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Post-download: the Download Manifest"} -->
Within the downloaded folder, you will find a manifest.html file. This manifest includes information about key aspects of file metadata and download status.
The table below highlights these columns. Of note is that "Access" will display either "PUBLIC" or "EXCLUSIVE_ACCESS"; public data is available to all users, while exclusive access data requires authentication. "Logged In User" will give your user name if you have logged in, and "anonymous" otherwise. "Status" will generally be "OK"; see the examples below for cases where it is something different.
URI | File | Access | Status | Logged In User
---|---|---|---|---
mast:MISSION/product/FILENAME | MISSION/path/FILENAME |  PUBLIC
EXCLUSIVE_ACCESS |  OK Duplicate of [file] [File] associated with [obs] ... SUCCESS |  anonymous
YourName

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Post-download: the Download Manifest", "Header 2": "Example 1: De-duplication"} -->
If you selected products that are shared across multiple observations (e.g., guide star files), these files will only be downloaded once. This minimizes download time and storage utilization on your machine.
URI | File | Access | Status | Logged In User
---|---|---|---|---
mast:JWST/product/file1.fits | JWST/product/file1.fits | PUBLIC | OK | anonymous
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | OK | anonymous
mast:JWST/product/file2.fits | JWST/product/file2.fits | PUBLIC | OK | anonymous
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | Duplicate of file pool.csv in folder jw0133_01_01 | anonymous

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Post-download: the Download Manifest", "Header 2": "Example 2: Exclusive Access Data"} -->
When downloading data that requires authentication, the status for all files will display the authentication message (regardless of whether they are publicly available). In the case of duplicated files, the "SUCCESS" will be replaced with a duplication message like the one in example 1.
URI | File | Access | Status | Logged In User
---|---|---|---|---
mast:JWST/product/file3.fits | JWST/product/file3.fits | EXCLUSIVE_ACESS | JWST/product/file3.fits associated with jw123_0_1 ... SUCCESS | YourName
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | JWST/product/pool.csv associated with jw123_0_1 ... SUCCESS | YourName
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | JWST/product/pool.csv associated with jw123_0_1 ... Duplicate of file pool.csv associated with jw123_0_1 | YourName
* [Mission Search Guide Home](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)
* [MAST Data Product Types](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963707/MAST+Data+Product+Types)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [Cone Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search "Cone Search And Upload List Search")
* [Target Name Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search "Target Name Search And Upload List Search")
* [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview "Search Parameter Overview")
* [Core Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters "Core Search Parameters")
* [CLASSY Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131862458/CLASSY+Search+Components "CLASSY Search Components")
* [HST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components "HST Search Components")
* [JWST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350629/JWST+Search+Components "JWST Search Components")
* [ULLYSES Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158174811/ULLYSES+Search+Components "ULLYSES Search Components")
* [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters "Additional Search Parameters")
* [Choose Output Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958266/Choose+Output+Columns "Choose Output Columns")
* [The Search Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958267/The+Search+Bar "The Search Bar")
* [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page "Search Results Page")
* [Image Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/352354485/Image+Previews "Image Previews")
* [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay "Download Overlay")
* [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions "Regular Expressions")
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
* [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions "Regular Expressions")
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
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [RITA](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA "RITA")
* [RomanCal Refererence Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products "RomanCal Refererence Products")
* [Roman Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products "Roman Supplemental Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
Use the download overlay to refine your selection of specific files to retrieve, and to select a method for download.
**On this page...**
* 1[Download Overlay Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-DownloadOverlayOverview)
* 2[The Elements in Detail](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-TheElementsinDetail)
* 2.1[1: Selection Summary](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-1:SelectionSummary)
* 2.2[2: Quick Select Options](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-2:QuickSelectOptions)
* 2.3[3: Data Processing Levels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-3:DataProcessingLevels)
* 2.4[4: Guide Star Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-4:GuideStarFiles)
* 2.5[5: Regex Matching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-5:RegexMatching)
* 2.6[6: View and Export Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-6:ViewandExportSelection)
* 2.7[7: Download Folder Organization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-7:DownloadFolderOrganization)
* 2.8[8: Initiating the Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-8:InitiatingtheDownload)
* 3[Post-download: the Download Manifest](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-Post-download:theDownloadManifest)
* 3.1[Example 1: De-duplication](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-Example1:De-duplication)
* 3.2[Example 2: Exclusive Access Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-Example2:ExclusiveAccessData)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-further-readingForFurtherReading...)

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Download Overlay Overview"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/panel_mmDLO.png?version=1&modificationDate=1698757510104&api=v2)
The download overlay, with selectors or action buttons in numbered boxes. The overlay selectors vary slightly among missions, as described below.
After choosing Datasets in the search window, use the **download overlay** panel to refine your selection of the underlying files. Use the selectors to refine the selection criteria, then use the action buttons to review the products and choose a method for downloading files.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail"} -->
The selector and action elements are described below.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "1: Selection Summary"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/status_selectionOverrview.png?version=1&modificationDate=1698757510149&api=v2)  
The selection overview displays the number and volume of files you've selected. It also displays the total number of files that are available for download. In this case, we've selected "All" but excluded guidestar files.
**Note:** If some selected files are not available to you due to an exclusive access restriction, you will get a warning with the number of files that have been excluded. You must log in using your MyST account and be authorized to retrieve them. See [Downloading Exclusive Access Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay#DownloadOverlay-dwld-eap) for more details.
* * *

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "2: Quick Select Options"} -->
![the three 'quick select' options: all, recommended, and none](https://outerspace.stsci.edu/download/thumbnails/107840400/quick-select.png?version=1&modificationDate=1698757509364&api=v2)
You can use the "quick selections" to do just that: quickly select a subset of files.
**All** will select all file categories across processing levels, but for JWST will _not_ include guidestar files. These must be added manually using the dedicated selector described below.
**None** clears all selections.
**Recommended** is the minimum set of files that are recommended for scientific analysis. This is a good shortcut for users are satisfied with the data calibration, but may not be applicable to your particular scientific needs.
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "3: Data Processing Levels"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/hst-download-selection.png?version=1&modificationDate=1706224154197&api=v2)  
This selector shows or hides types of products based on their classification as defined by the archive or mission pipelines. The example at left applies to the HST mission. You can select entire calibration levels (e.g "Uncalibrated"), as well as individual file types within those levels ("e.g. CSPEC_THUMB").
The suffix**CSPEC**), and is not the file extension (e.g., **`.fits`**). The specific product suffix depends on the instruments of each Mission. View the mission-specific conventions in[MAST Data Product Types](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963707/MAST+Data+Product+Types).

<!-- CHUNK 23 END -->

<!-- CHUNK 24 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "3: Data Processing Levels", "Header 3": "For HST"} -->
HST results now include data from [HASP, the Hubble Advanced Spectral Products](https://archive.stsci.edu/missions-and-data/hst/hasp). You will see this option available for most COS and STIS observations, in addition to the standard product levels.

<!-- CHUNK 24 END -->

<!-- CHUNK 25 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "3: Data Processing Levels", "Header 3": "For JWST"} -->
An option to !["include calibration references files"](https://outerspace.stsci.edu/download/thumbnails/107840400/box_inclCalRefFiles.png?version=1&modificationDate=1698757510190&api=v2)will appear in the top right corner. This option provides the files necessary to run the calibration pipeline yourself.  
* * *

<!-- CHUNK 25 END -->

<!-- CHUNK 26 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "4: Guide Star Files"} -->
Note that this selector is only applicable to the JWST mission.
![](https://outerspace.stsci.edu/download/attachments/107840400/guidestar.png?version=1&modificationDate=1698757509446&api=v2)  
Guidestar files are not included by default, but may be selected. Only the highest calibration level of products are available.
* * *

<!-- CHUNK 26 END -->

<!-- CHUNK 27 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "5: Regex Matching"} -->
![](https://outerspace.stsci.edu/download/attachments/107840400/dialog_regex.png?version=1&modificationDate=1698757510005&api=v2)
Regular expressions are a powerful selection mechanism, and the Download Overlay supports [Regex in the Download Overlay Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions) for detailed examples.
* * *

<!-- CHUNK 27 END -->

<!-- CHUNK 28 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "6: View and Export Selection"} -->
![](https://outerspace.stsci.edu/download/thumbnails/107840400/button_viewFiles.png?version=1&modificationDate=1698757509789&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/107840400/button_exportFileList.png?version=1&modificationDate=1698757509831&api=v2)  
**View All Selected Files** will open a preview of the files you've selected so far. This is particularly useful if you have entered a regular expression (see above).
**Export Selected File List** saves this list of files as a CSV file, with columns corresponding to those displayed in the preview. See the corresponding sections below for more details on both.

<!-- CHUNK 28 END -->

<!-- CHUNK 29 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "6: View and Export Selection", "Header 3": "6.1 The Preview and Pagination"} -->
![a sample preview of selected files. five files are visible](https://outerspace.stsci.edu/download/attachments/107840400/selection-preview.png?version=1&modificationDate=1698757509581&api=v2)
When previewing file metadata, the filenames are separated into groups based on the parent Datasets.  
Large numbers of products will span multiple pages. The current product range and total number of products are displayed at the bottom of the product-selection table. Paging controls can be modified to navigate more efficiently.
**Note:** not all metadata are visible in the graphic shown at left. It may be necessary for you to scroll horizontally to see all metadata.

<!-- CHUNK 29 END -->

<!-- CHUNK 30 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "6: View and Export Selection", "Header 3": "6.2 Exporting to CSV"} -->
**Example CSV export**
```
Dataset,Filename,Product Level,Suffix,Instrument,Filter / Grating
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_cal.fits,2b,_cal,NIRISS,NIS_SOSSTA
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_uncal.fits,1b,_uncal,NIRISS,NIS_SOSSTA
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_rate.fits,2a,_rate,NIRISS,NIS_SOSSTA
jw02734001001_02101_00001,jw02734001001_02101_00001-seg001_nis_rateints.fits,2a,_rateints,NIRISS,NIS_SOSSTA
jw02734-o002_t002_niriss,jw02734-o002_t002_niriss_clear-gr700xd-substrip256_x1dints.fits,3,_x1dints,NIRISS,NIS_SUBSTRIP256
```  
The file list can also be exported to CSV format. However, the CSV differs slightly: it does not visually separate files based on the parent Dataset ID. Instead, each row begins with the Dataset ID corresponding to the product filename.
Some column names contain spaces; this table should only be parsed using commas.
* * *

<!-- CHUNK 30 END -->

<!-- CHUNK 31 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "7: Download Folder Organization"} -->
![the option for file structure; the options are 'flat' and 'nested'](https://outerspace.stsci.edu/download/attachments/107840400/flat-or-nested.png?version=1&modificationDate=1698757509539&api=v2)
![](https://outerspace.stsci.edu/download/attachments/107840400/nested.png?version=1&modificationDate=1698757509702&api=v2)
![](https://outerspace.stsci.edu/download/attachments/107840400/flat.png?version=1&modificationDate=1698757509741&api=v2)
You may choose a __NESTED__ structure, where the main folder contains subdirectories for each parent dataset where the related files are located (middle-left graphic).
Or choose a  __FLAT__ directory structure, where files appear at the top of the download folder tree (lower-left graphic).
* * *

<!-- CHUNK 31 END -->

<!-- CHUNK 32 START -->
<!-- Metadata: {"Header 1": "The Elements in Detail", "Header 2": "8: Initiating the Download"} -->
![Start Download button, to initiate file downloads](https://outerspace.stsci.edu/download/thumbnails/107840400/button_startDownload.png?version=1&modificationDate=1698757509873&api=v2)  
![API Query button, to generate a bash script containing commands to retreive files](https://outerspace.stsci.edu/download/thumbnails/107840400/button_apiQ.png?version=1&modificationDate=1698757509914&api=v2)
**START DOWNLOAD** will initiate a streaming file retrieval through the browser and produce a local ZIP file with the results. Note that the download location is set by the preference settings of the web browser. Some browsers allow a choice of download location; otherwise, the ZIP file will be downloaded to your default location.
**API QUERY** will generate a bash script of curl commands that you can use to retrieve files at a later time. This may be the only option for a large file payload (>1.0 TB uncompressed), and is more robust on slow connections.
To download non-public products via API Query, an Auth.MAST token must be created and provided to the generated script when prompted. You will only be prompted for this Auth.MAST token if there are non-public products requested for download. For more information on Auth.MAST tokens, please visit the [Auth.MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts#MASTAccounts-auth-mast) documentation.
![A yellow padlock, followed by a warning that exclusive access files are not selected](https://outerspace.stsci.edu/download/thumbnails/107840400/eap-files.png?version=1&modificationDate=1698757509319&api=v2)  
![Mission search login menu](https://outerspace.stsci.edu/download/thumbnails/107840400/menu_login.png?version=1&modificationDate=1698757510055&api=v2)
Some new data from Hubble and JWST are temporarily available only to the Investigator teams, which is indicated with a **yellow lock symbol and a warning**. These products will appear in the total file count, but will not be available to download except to signed-in, authorized users.
You will need to be logged in (see pull-down menu at upper-right) and be authorized to retrieve EA files. See [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts) for details.
* * *

<!-- CHUNK 32 END -->

<!-- CHUNK 33 START -->
<!-- Metadata: {"Header 1": "Post-download: the Download Manifest"} -->
Within the downloaded folder, you will find a manifest.html file. This manifest includes information about key aspects of file metadata and download status.
The table below highlights these columns. Of note is that "Access" will display either "PUBLIC" or "EXCLUSIVE_ACCESS"; public data is available to all users, while exclusive access data requires authentication. "Logged In User" will give your user name if you have logged in, and "anonymous" otherwise. "Status" will generally be "OK"; see the examples below for cases where it is something different.
URI | File | Access | Status | Logged In User
---|---|---|---|---
mast:MISSION/product/FILENAME | MISSION/path/FILENAME |  PUBLIC
EXCLUSIVE_ACCESS |  OK Duplicate of [file] [File] associated with [obs] ... SUCCESS |  anonymous
YourName

<!-- CHUNK 33 END -->

<!-- CHUNK 34 START -->
<!-- Metadata: {"Header 1": "Post-download: the Download Manifest", "Header 2": "Example 1: De-duplication"} -->
If you selected products that are shared across multiple observations (e.g., guide star files), these files will only be downloaded once. This minimizes download time and storage utilization on your machine.
URI | File | Access | Status | Logged In User
---|---|---|---|---
mast:JWST/product/file1.fits | JWST/product/file1.fits | PUBLIC | OK | anonymous
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | OK | anonymous
mast:JWST/product/file2.fits | JWST/product/file2.fits | PUBLIC | OK | anonymous
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | Duplicate of file pool.csv in folder jw0133_01_01 | anonymous

<!-- CHUNK 34 END -->

<!-- CHUNK 35 START -->
<!-- Metadata: {"Header 1": "Post-download: the Download Manifest", "Header 2": "Example 2: Exclusive Access Data"} -->
When downloading data that requires authentication, the status for all files will display the authentication message (regardless of whether they are publicly available). In the case of duplicated files, the "SUCCESS" will be replaced with a duplication message like the one in example 1.
URI | File | Access | Status | Logged In User
---|---|---|---|---
mast:JWST/product/file3.fits | JWST/product/file3.fits | EXCLUSIVE_ACESS | JWST/product/file3.fits associated with jw123_0_1 ... SUCCESS | YourName
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | JWST/product/pool.csv associated with jw123_0_1 ... SUCCESS | YourName
mast:JWST/product/pool.csv | JWST/product/pool.csv | PUBLIC | JWST/product/pool.csv associated with jw123_0_1 ... Duplicate of file pool.csv associated with jw123_0_1 | YourName
* [Mission Search Guide Home](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)
* [MAST Data Product Types](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963707/MAST+Data+Product+Types)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 35 END -->

