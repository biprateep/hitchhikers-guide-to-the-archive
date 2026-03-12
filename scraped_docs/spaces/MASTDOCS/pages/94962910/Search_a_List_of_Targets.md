---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets"
date_accessed: "2026-03-11T11:32:17.668977"
---

<!-- CHUNK 1 START -->
It is possible to search MAST for multiple targets at once, by first uploading list of target names and coordinates.
**On this page...**
* 1[Search a List of Targets](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets#SearchaListofTargets-SearchaListofTargets)
* 1.1[Formatting Rules for Uploads](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets#SearchaListofTargets-FormattingRulesforUploads)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Search a List of Targets"} -->
Here are he steps for uploading a list of targets to the Portal:  
| Introduction | Notes
---|---|---
**1** |  Prepare a list of targets on your local machine, following the formatting rules below. This minimal example file (_right_) uses a list of names and coordinates of 4 Galactic globular clusters. Your target list may include other columns of information, such as source magnitudes. | [globulars.txt](https://outerspace.stsci.edu/download/attachments/94962917/globulars.txt?version=1&modificationDate=1662673221449&api=v2)
**2** | Click the **Upload Target List** button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/button_uploadTargets.png?version=1&modificationDate=1615209732450&api=v2)
**3** | Enter the location of your target list in the upload dialog box, and click "Upload" | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/dialog_uploadTargets.png?version=1&modificationDate=1615209732461&api=v2)
**4** | Select one or more of your targets in the results table. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/grid_list.png?version=1&modificationDate=1615209732478&api=v2)
**5** | Click the cross-match button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/button_crossMatch.png?version=1&modificationDate=1615209732483&api=v2)
**6** | Select a MAST collection against which to cross-match the coordinates of you targets. Also select a search radius about the targets. Then click the **Cross Match** button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/dialog_Xmaatch.png?version=1&modificationDate=1615209732486&api=v2)
It is possible to perform other actions with user tables beyond cross-matching with an uploaded table, such as creating new table columns or plots of column values.
Uploading a large list of targets, and then cross-matching against a large catalog such as __All Observations__ , may take a long time to execute, and may return an unwieldy list of matches.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Search a List of Targets", "Header 2": "Formatting Rules for Uploads"} -->
The **Upload** tool can import custom tables in two file formats: VOTABLE and CSV. See the
* A line is a comment if it begins with a `#`. An exception to this is that before the header line you may specify a column datatype line with `#@`, then a comma-separated list of types.
* Allowed types are: `int`, `float`, `string`, `ra` and `dec`, with the latter two being interpreted from either decimal or sexagesimal coordinates. If no datatypes are specified, the software will attempt to determine them.
* The first un-commented line defines the headers for the columns.
* Right ascension should be titled as: `RA` or `RAJ2000`.
* Declination should be titled as: `DEC` or `DECJ2000`.
* Footprints should be titled as: `s_region` or `regionSTCS`.
* Any number of subsequent rows may be defined, although one should exercise caution with trying to load large numbers of rows.  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
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
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
* [Tips and Notes](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963055/Tips+and+Notes "Tips and Notes")
* [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials "Demos and Tutorials")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
It is possible to search MAST for multiple targets at once, by first uploading list of target names and coordinates.
**On this page...**
* 1[Search a List of Targets](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets#SearchaListofTargets-SearchaListofTargets)
* 1.1[Formatting Rules for Uploads](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets#SearchaListofTargets-FormattingRulesforUploads)

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Search a List of Targets"} -->
Here are he steps for uploading a list of targets to the Portal:  
| Introduction | Notes
---|---|---
**1** |  Prepare a list of targets on your local machine, following the formatting rules below. This minimal example file (_right_) uses a list of names and coordinates of 4 Galactic globular clusters. Your target list may include other columns of information, such as source magnitudes. | [globulars.txt](https://outerspace.stsci.edu/download/attachments/94962917/globulars.txt?version=1&modificationDate=1662673221449&api=v2)
**2** | Click the **Upload Target List** button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/button_uploadTargets.png?version=1&modificationDate=1615209732450&api=v2)
**3** | Enter the location of your target list in the upload dialog box, and click "Upload" | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/dialog_uploadTargets.png?version=1&modificationDate=1615209732461&api=v2)
**4** | Select one or more of your targets in the results table. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/grid_list.png?version=1&modificationDate=1615209732478&api=v2)
**5** | Click the cross-match button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/button_crossMatch.png?version=1&modificationDate=1615209732483&api=v2)
**6** | Select a MAST collection against which to cross-match the coordinates of you targets. Also select a search radius about the targets. Then click the **Cross Match** button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962910/dialog_Xmaatch.png?version=1&modificationDate=1615209732486&api=v2)
It is possible to perform other actions with user tables beyond cross-matching with an uploaded table, such as creating new table columns or plots of column values.
Uploading a large list of targets, and then cross-matching against a large catalog such as __All Observations__ , may take a long time to execute, and may return an unwieldy list of matches.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Search a List of Targets", "Header 2": "Formatting Rules for Uploads"} -->
The **Upload** tool can import custom tables in two file formats: VOTABLE and CSV. See the
* A line is a comment if it begins with a `#`. An exception to this is that before the header line you may specify a column datatype line with `#@`, then a comma-separated list of types.
* Allowed types are: `int`, `float`, `string`, `ra` and `dec`, with the latter two being interpreted from either decimal or sexagesimal coordinates. If no datatypes are specified, the software will attempt to determine them.
* The first un-commented line defines the headers for the columns.
* Right ascension should be titled as: `RA` or `RAJ2000`.
* Declination should be titled as: `DEC` or `DECJ2000`.
* Footprints should be titled as: `s_region` or `regionSTCS`.
* Any number of subsequent rows may be defined, although one should exercise caution with trying to load large numbers of rows.  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 5 END -->

