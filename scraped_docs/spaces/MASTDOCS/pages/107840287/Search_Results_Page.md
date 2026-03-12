---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page"
date_accessed: "2026-03-11T11:34:15.556653"
---

<!-- CHUNK 1 START -->
The results of a successful search are presented in a new window, in tabular format. This article describes the various user controls for navigating the results, saving the results table, and downloading data.
**On this page...**
* 1[Features and Functionality](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-FeaturesandFunctionality)
* 1.1[Select Rows](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-row_selectSelectRows)
* 1.1.1[ Non-Public (Exclusive Access) Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-non_public_resultsNon-Public\(ExclusiveAccess\)SearchResults)
* 1.2[Download Selections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-download_buttonDownloadSelections)
* 1.3[Export Table](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-export_buttonExportTable)
* 1.4[Navigate the Results Table](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-NavigatetheResultsTable)
* 1.4.1[Sort Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-sort_columnsSortColumns)
* 1.4.2[Pagination](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-paginationPagination)
* 1.4.3[Set The Page Size](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-page_sizeSetThePageSize)
* 1.5[Edit the Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-edit_search_buttonEdittheSearch)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Features and Functionality"} -->
Each row in the table is associated with multiple data products, and the columns contain metadata in common for those products. You can explore the table, download selected data, and export the results table itself.
Use the selection checkboxes on the far left in the table to select datasets to download or select rows to export. The top-most checkbox that is inside the header row will select all the rows on the current page. Click that box again to deselect all rows on the current page. The checkbox at the far left of each row of the results table will select or deselect that individual row.
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_rowselection.png?version=1&modificationDate=1630383322328&api=v2)
NOTE: The top-most checkbox selects all rows only on the current page. It does **not** select **all** the rows across all the pages. Rows that are selected or deselected will remain selected/deselected as the results table is paginated.
If there are too many results, consider constraining the search with [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview) and [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters).

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 3": "Non-Public (Exclusive Access) Search Results"} -->
Some data collections have products that are not publicly available to download, for example some of the HST observations. However, the metadata associated with those observations are publicly available. Any search results that contain observations that are not publicly released yet are shown with a yellow background in the search results table. The observational metadata in the search results table may be exported, but the products may not be downloaded unless signed into a [MyST account](https://proper.stsci.edu/proper/authentication/auth) that is authorized by the Principal Investigator of the observations to download those products. For login information, see [MAST User Accounts](https://outerspace.stsci.edu/display/MASTDOCS/MAST+User+Accounts). For more information, see [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay) section.
![](https://outerspace.stsci.edu/download/attachments/107840287/results_nonpublic.png?version=1&modificationDate=1630381587802&api=v2)
* * *
As datasets are selected in the results table, the **DOWNLOAD SELECTED** menu will become active. When ready to retrieve products for the selected datasets, select an option from the menu to begin the download process. The first menu option, __Choose which files to download__ , will open the [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay).
![](https://outerspace.stsci.edu/download/thumbnails/107840287/Results-Download-Data-Button.png?version=2&modificationDate=1709826931217&api=v2)
You can instead select either the __Quick Download__ or __Quick API Script__ option to begin downloading immediately.
* __Quick Download__
* __Quick API Script__  
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Export Table"} -->
The search results table itself (that is, all the metadata shown in the table) can be exported to a local file.
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_exportbutton.png?version=1&modificationDate=1630383321892&api=v2)
You can export all rows in the entire table, or only selected rows. The supported export formats are:
* `csv`
* `json`
* `VO Table`  
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table"} -->
There are various controls for navigating the results table when it spans more than one page on the screen.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table", "Header 3": "Sort Columns"} -->
The columns of the search results table can be sorted in ascending or descending order by clicking on the column names. Multi-sort is supported—the table can be sorted by first one column, then a second, then a third, etc. Click a column name once to sort by ascending order (upward arrow and a number will show up next to the column), then again to sort by descending order (downward arrow and a number shows up next to column). Click a third time to turn off sorting for that column and the arrow and number will disappear.
Specification of multi-sort:
* A number and an arrow will show up when sort functionality is active
* Ascending order can be verified by the upward arrow next to the column name
* Descending order can be checked by the downward arrow next to the column name
* The order of multi-sort can be determined by the number next to the arrow and the column name  
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_pagination.png?version=1&modificationDate=1630383322151&api=v2)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table", "Header 3": "Pagination"} -->
For search results larger than the page size, use the pagination buttons on either the top right of the table just above column names, or at the bottom right of the table to jump through the pages. To the left of pagination, the number of rows shown per table page is listed compared to the total number of observations retrieved. The pagination has options to jump to the first page (![](https://outerspace.stsci.edu/download/thumbnails/107840287/First%20Page.png?version=1&modificationDate=1630504986793&api=v2)), the previous page(![](https://outerspace.stsci.edu/download/thumbnails/107840287/Back%20one%20page.png?version=1&modificationDate=1630504987202&api=v2)), the next page (![](https://outerspace.stsci.edu/download/thumbnails/107840287/Forward%20one%20Page.png?version=1&modificationDate=1630504987065&api=v2)), and the last page of search results(![](https://outerspace.stsci.edu/download/thumbnails/107840287/Last%20Page.png?version=1&modificationDate=1630504986920&api=v2)).  
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_pagesize.png?version=1&modificationDate=1630383322045&api=v2)

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table", "Header 3": "Set The Page Size"} -->
The page size is controlled with the **Rows per page** drop-down menu. By default, 500 results per page are displayed. It can be adjusted to show 50, 100, 250, 500 or 1000 rows per page.
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Edit the Search"} -->
Use the **EDIT SEARCH** button to change the search parameters. This will return you to the search interface, where you can modify or add search parameters. Use the **CLEAR FORM** button to reset all parameters, then set parameters as needed to start a new search.  
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_editsearch.png?version=1&modificationDate=1630384679701&api=v2)  
Clicking the back button of the browser will lose the previous search history. Make sure to click **EDIT SEARCH** to modify or reset the search parameters.
* * *

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)  
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
The results of a successful search are presented in a new window, in tabular format. This article describes the various user controls for navigating the results, saving the results table, and downloading data.
**On this page...**
* 1[Features and Functionality](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-FeaturesandFunctionality)
* 1.1[Select Rows](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-row_selectSelectRows)
* 1.1.1[ Non-Public (Exclusive Access) Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-non_public_resultsNon-Public\(ExclusiveAccess\)SearchResults)
* 1.2[Download Selections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-download_buttonDownloadSelections)
* 1.3[Export Table](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-export_buttonExportTable)
* 1.4[Navigate the Results Table](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-NavigatetheResultsTable)
* 1.4.1[Sort Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-sort_columnsSortColumns)
* 1.4.2[Pagination](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-paginationPagination)
* 1.4.3[Set The Page Size](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-page_sizeSetThePageSize)
* 1.5[Edit the Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-edit_search_buttonEdittheSearch)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page#SearchResultsPage-ForFurtherReading...)

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Features and Functionality"} -->
Each row in the table is associated with multiple data products, and the columns contain metadata in common for those products. You can explore the table, download selected data, and export the results table itself.
Use the selection checkboxes on the far left in the table to select datasets to download or select rows to export. The top-most checkbox that is inside the header row will select all the rows on the current page. Click that box again to deselect all rows on the current page. The checkbox at the far left of each row of the results table will select or deselect that individual row.
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_rowselection.png?version=1&modificationDate=1630383322328&api=v2)
NOTE: The top-most checkbox selects all rows only on the current page. It does **not** select **all** the rows across all the pages. Rows that are selected or deselected will remain selected/deselected as the results table is paginated.
If there are too many results, consider constraining the search with [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview) and [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters).

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 3": "Non-Public (Exclusive Access) Search Results"} -->
Some data collections have products that are not publicly available to download, for example some of the HST observations. However, the metadata associated with those observations are publicly available. Any search results that contain observations that are not publicly released yet are shown with a yellow background in the search results table. The observational metadata in the search results table may be exported, but the products may not be downloaded unless signed into a [MyST account](https://proper.stsci.edu/proper/authentication/auth) that is authorized by the Principal Investigator of the observations to download those products. For login information, see [MAST User Accounts](https://outerspace.stsci.edu/display/MASTDOCS/MAST+User+Accounts). For more information, see [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay) section.
![](https://outerspace.stsci.edu/download/attachments/107840287/results_nonpublic.png?version=1&modificationDate=1630381587802&api=v2)
* * *
As datasets are selected in the results table, the **DOWNLOAD SELECTED** menu will become active. When ready to retrieve products for the selected datasets, select an option from the menu to begin the download process. The first menu option, __Choose which files to download__ , will open the [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay).
![](https://outerspace.stsci.edu/download/thumbnails/107840287/Results-Download-Data-Button.png?version=2&modificationDate=1709826931217&api=v2)
You can instead select either the __Quick Download__ or __Quick API Script__ option to begin downloading immediately.
* __Quick Download__
* __Quick API Script__  
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Export Table"} -->
The search results table itself (that is, all the metadata shown in the table) can be exported to a local file.
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_exportbutton.png?version=1&modificationDate=1630383321892&api=v2)
You can export all rows in the entire table, or only selected rows. The supported export formats are:
* `csv`
* `json`
* `VO Table`  
* * *

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table"} -->
There are various controls for navigating the results table when it spans more than one page on the screen.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table", "Header 3": "Sort Columns"} -->
The columns of the search results table can be sorted in ascending or descending order by clicking on the column names. Multi-sort is supported—the table can be sorted by first one column, then a second, then a third, etc. Click a column name once to sort by ascending order (upward arrow and a number will show up next to the column), then again to sort by descending order (downward arrow and a number shows up next to column). Click a third time to turn off sorting for that column and the arrow and number will disappear.
Specification of multi-sort:
* A number and an arrow will show up when sort functionality is active
* Ascending order can be verified by the upward arrow next to the column name
* Descending order can be checked by the downward arrow next to the column name
* The order of multi-sort can be determined by the number next to the arrow and the column name  
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_pagination.png?version=1&modificationDate=1630383322151&api=v2)

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table", "Header 3": "Pagination"} -->
For search results larger than the page size, use the pagination buttons on either the top right of the table just above column names, or at the bottom right of the table to jump through the pages. To the left of pagination, the number of rows shown per table page is listed compared to the total number of observations retrieved. The pagination has options to jump to the first page (![](https://outerspace.stsci.edu/download/thumbnails/107840287/First%20Page.png?version=1&modificationDate=1630504986793&api=v2)), the previous page(![](https://outerspace.stsci.edu/download/thumbnails/107840287/Back%20one%20page.png?version=1&modificationDate=1630504987202&api=v2)), the next page (![](https://outerspace.stsci.edu/download/thumbnails/107840287/Forward%20one%20Page.png?version=1&modificationDate=1630504987065&api=v2)), and the last page of search results(![](https://outerspace.stsci.edu/download/thumbnails/107840287/Last%20Page.png?version=1&modificationDate=1630504986920&api=v2)).  
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_pagesize.png?version=1&modificationDate=1630383322045&api=v2)

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Navigate the Results Table", "Header 3": "Set The Page Size"} -->
The page size is controlled with the **Rows per page** drop-down menu. By default, 500 results per page are displayed. It can be adjusted to show 50, 100, 250, 500 or 1000 rows per page.
* * *

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Features and Functionality", "Header 2": "Edit the Search"} -->
Use the **EDIT SEARCH** button to change the search parameters. This will return you to the search interface, where you can modify or add search parameters. Use the **CLEAR FORM** button to reset all parameters, then set parameters as needed to start a new search.  
![](https://outerspace.stsci.edu/download/thumbnails/107840287/results_editsearch.png?version=1&modificationDate=1630384679701&api=v2)  
Clicking the back button of the browser will lose the previous search history. Make sure to click **EDIT SEARCH** to modify or reset the search parameters.
* * *

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 19 END -->

