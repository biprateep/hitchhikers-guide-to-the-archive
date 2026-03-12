---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search"
date_accessed: "2026-03-11T11:33:58.112016"
---

<!-- CHUNK 1 START -->
On this page...
* [Search By Object Names To Resolve Into Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-single_target)
* [Search By Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-single_coord)
* [Upload A List Of Object Names To Resolve Into Coordinates, Cone Search Coordinates, or Dataset IDs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-upload_list)
* [Specifying The Cone Search Radius](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-cone_size)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Component Overview"} -->
This page describes the Cone Search and Upload List area. These components are used for searches that are based on coordinates (positions) on the sky (also known as cone searches), or based on an uploaded list of target information, such as resolvable object names, coordinates, or dataset IDs. A Cone Search is performed when the "Resolve" toggle button ![](https://outerspace.stsci.edu/download/thumbnails/104958263/Resolve%20Button.png?version=1&modificationDate=1644443253628&api=v2) is checked (selected):
![](https://outerspace.stsci.edu/download/attachments/104958263/Resolve.png?version=1&modificationDate=1644443254523&api=v2)
If a search by exact match on Target Name is preferred, please refer to the [Target Name Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search) documentation.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Component Overview", "Header 2": "Component Features and Functionality"} -->
A description of the Cone Search and Upload List Component capabilities: Search By Object Names To Resolve Into Coordinates, Search By Coordinates, Upload A List, and Specify The Cone Search Radius.
* Any combination of object names and/or coordinates (see below) can be entered using this component, it can resolve either one as they are entered!
* Enabling a search does not require specifying a coordinate or object name. Use the search form to conduct a search based only on other search parameters, or even no parameters at all! Searching with nothing entered in the form retrieves all available entries from a given data collections.  
* * *
Search By Object Names To Resolve Into Coordinates
One or more object names can be entered into the **'Object Search'** box. Press 'tab', 'return', or 'comma' on your keyboard to finish entering the object name (clicking off the text box will also work). The form will attempt to resolve the object name into a coordinate using the [MAST name resolving service](https://mastresolver.stsci.edu/Santa-war/). This service looks up the object's name using
* Upon a successful resolve, the object name will be surrounded by a green color, a check mark is added in front of the name, and the resolved coordinate will appear to the right of the object name in parenthesis. The coordinate shown will be used as the center of the cone search for that object.  
![](https://outerspace.stsci.edu/download/thumbnails/104958263/nameres_success.png?version=1&modificationDate=1629752426626&api=v2)
* If the object name can not be resolved, the target will be surrounded by a yellow color and an exclamation point is added in front of the name.  
![](https://outerspace.stsci.edu/download/thumbnails/104958263/nameres_fail.png?version=1&modificationDate=1629752426643&api=v2)
* The 'X' mark right next to each entry can used to remove an object.  
![](https://outerspace.stsci.edu/download/attachments/104958263/direct_type_coordinate-3.png?version=2&modificationDate=1630013475029&api=v2)![](https://outerspace.stsci.edu/download/attachments/104958263/direct_type_coordinate.png?version=1&modificationDate=1630012973289&api=v2)![](https://outerspace.stsci.edu/download/attachments/104958263/direct_type_coordinate-2.png?version=1&modificationDate=1630013117432&api=v2)  
Search By Coordinates
One or more coordinates can be entered into the **'Object Search'** box. Coordinates can be entered in sexagesimal notation (Right Ascension in hours; HH MM SS.ss or HH:MM:SS.ss, Declination in degrees; DD MM SS.ss or DD:MM:SS.ss) or in decimal notation (Right Ascension and Declination both in degrees; DDD.dd). Press 'tab', 'return', or 'comma' on your keyboard to finish entering the coordinate (clicking off the text box will also work).
Values outside the bounds
Right Ascension values outside the bounds of 0.0 <= R.A. <= 360.0 degrees will be wrapped to fit with these bounds.
![](https://outerspace.stsci.edu/download/thumbnails/104958263/coords_success.png?version=1&modificationDate=1629752420219&api=v2)
Declination values outside the bounds of -90.0 <= Dec. <= 90.0 will be parsed as invalid.
![](https://outerspace.stsci.edu/download/thumbnails/104958263/coords_falure.png?version=1&modificationDate=1629752420254&api=v2)
For positive values, you may optionally decide to include a '+' sign.  
When entering a coordinate, do not include a comma or semicolon between R.A. and Dec. Separate them with only a space.
Since there are a wide variety of ways to upload lists of objects, a number of sample files is provided in the table below.
**CSV File Format Example**
target,ra,dec,dataset_id
M101, 14:03:12.545, +54:20:56.22, J8OB02011
51 Peg, 22 57 27.960, +20 46 07.75, O4ZE04020
TRAPPIST-1,23h06m29.368s,-05h02m29.03s, ID4301QPQ
helix nebula, 22:29:38.545, -20:50:13.75, W1KA2T01T
Description | Sample Upload File
---|---
One column, only object names. | [example_idonly.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idonly.csv?version=1&modificationDate=1629859322772&api=v2)
One column, only coordinates. | [example_coordonly.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_coordonly.csv?version=1&modificationDate=1629859322208&api=v2)
One column, only dataset IDs. | [example_datasetsonly.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_datasetsonly.csv?version=1&modificationDate=1629859322378&api=v2)
Three columns, object names and coordinates. | [example_idandcoords.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idandcoords.csv?version=1&modificationDate=1629859322476&api=v2)
Four columns, object names, coordinates, and dataset IDs. | [example_idandcoordsanddatasets.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idandcoordsanddatasets.csv?version=1&modificationDate=1629859322585&api=v2)
Five columns, object names, coordinates, and two user-defined columns. | [example_idandcoordsandnotes.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idandcoordsandnotes.csv?version=1&modificationDate=1629859322680&api=v2)
Upload A List Of Object Names To Resolve Into Coordinates, Cone Search Coordinates, or Dataset IDs
A file can be uploaded into the form that contains a list of object names to resolve into coordinates, coordinate pairs of Right Ascension and Declination, or Dataset IDs. The file must be in comma-separated value (CSV) format, and the top row must contain a header with column names. The header row does not need any special character in the front: the first row is always read in as the header row. The header row is case-insensitive.
The uploaded file must contain at least one of three search parameters: object name (using the header "Target"), coordinate (using the headers "RA" and "Dec"), and/or dataset ID (using the header "Dataset_ID"). Remember that the headers are case-insensitive ("dataset_id" works as well as "Dataset_ID").  
* If the file contains object names, coordinates, and dataset IDs, the search form will use the dataset IDs and return those exact matches in the search results.
* If the file contains object names and coordinates, the search form will use the coordinates to perform cone searches, and it will not attempt to resolve any object names.
* If the file contains only object names, the search form will attempt to resolve them into coordinates.  
The number of object names that were successfully and unsuccessfully resolved is reported, and clicking on the number of unsuccessful name resolves will display an overlay with more information and line numbers to provide further information.
The columns in the uploaded file are included in the search results table on the far right, with labels of 'User File <col>'. For example, if the uploaded file contained rows labeled 'target', 'ra', 'dec', 'dataset_id' they are included in the search results table as 'User File target', 'User File ra', 'User File dec', and 'User File dataset_id'.
If there are additional columns in the uploaded CSV file, they will be included in the search result table in the far right as well. This allows additional columns to be cross-matched to the search results and thus included when exporting the search result table.
![](https://outerspace.stsci.edu/download/attachments/104958263/search_radius.png?version=1&modificationDate=1629865182406&api=v2)
Specifying The Cone Search Radius
Regardless of how a position on the sky is specified (through an object name resolved into coordinates, or directly using Right Ascension and Declination) the size of the search radius is defined using the 'Search Radius' component. The radius may be defined in either arcseconds or arcminutes. The default size is 3 arcminutes in the form and a maximum radius of 30 arcminutes is allowed.
If a list is uploaded to the search form, this cone search radius is applied to every object name or coordinate in that list.
If a list of Dataset IDs is specified, a cone search is not conducted; thus this component is not used. Instead, a direct match on the dataset IDs is performed.
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)
* [Target Name Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search)  
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
On this page...
* [Search By Object Names To Resolve Into Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-single_target)
* [Search By Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-single_coord)
* [Upload A List Of Object Names To Resolve Into Coordinates, Cone Search Coordinates, or Dataset IDs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-upload_list)
* [Specifying The Cone Search Radius](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-cone_size)

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Component Overview"} -->
This page describes the Cone Search and Upload List area. These components are used for searches that are based on coordinates (positions) on the sky (also known as cone searches), or based on an uploaded list of target information, such as resolvable object names, coordinates, or dataset IDs. A Cone Search is performed when the "Resolve" toggle button ![](https://outerspace.stsci.edu/download/thumbnails/104958263/Resolve%20Button.png?version=1&modificationDate=1644443253628&api=v2) is checked (selected):
![](https://outerspace.stsci.edu/download/attachments/104958263/Resolve.png?version=1&modificationDate=1644443254523&api=v2)
If a search by exact match on Target Name is preferred, please refer to the [Target Name Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search) documentation.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Component Overview", "Header 2": "Component Features and Functionality"} -->
A description of the Cone Search and Upload List Component capabilities: Search By Object Names To Resolve Into Coordinates, Search By Coordinates, Upload A List, and Specify The Cone Search Radius.
* Any combination of object names and/or coordinates (see below) can be entered using this component, it can resolve either one as they are entered!
* Enabling a search does not require specifying a coordinate or object name. Use the search form to conduct a search based only on other search parameters, or even no parameters at all! Searching with nothing entered in the form retrieves all available entries from a given data collections.  
* * *
Search By Object Names To Resolve Into Coordinates
One or more object names can be entered into the **'Object Search'** box. Press 'tab', 'return', or 'comma' on your keyboard to finish entering the object name (clicking off the text box will also work). The form will attempt to resolve the object name into a coordinate using the [MAST name resolving service](https://mastresolver.stsci.edu/Santa-war/). This service looks up the object's name using
* Upon a successful resolve, the object name will be surrounded by a green color, a check mark is added in front of the name, and the resolved coordinate will appear to the right of the object name in parenthesis. The coordinate shown will be used as the center of the cone search for that object.  
![](https://outerspace.stsci.edu/download/thumbnails/104958263/nameres_success.png?version=1&modificationDate=1629752426626&api=v2)
* If the object name can not be resolved, the target will be surrounded by a yellow color and an exclamation point is added in front of the name.  
![](https://outerspace.stsci.edu/download/thumbnails/104958263/nameres_fail.png?version=1&modificationDate=1629752426643&api=v2)
* The 'X' mark right next to each entry can used to remove an object.  
![](https://outerspace.stsci.edu/download/attachments/104958263/direct_type_coordinate-3.png?version=2&modificationDate=1630013475029&api=v2)![](https://outerspace.stsci.edu/download/attachments/104958263/direct_type_coordinate.png?version=1&modificationDate=1630012973289&api=v2)![](https://outerspace.stsci.edu/download/attachments/104958263/direct_type_coordinate-2.png?version=1&modificationDate=1630013117432&api=v2)  
Search By Coordinates
One or more coordinates can be entered into the **'Object Search'** box. Coordinates can be entered in sexagesimal notation (Right Ascension in hours; HH MM SS.ss or HH:MM:SS.ss, Declination in degrees; DD MM SS.ss or DD:MM:SS.ss) or in decimal notation (Right Ascension and Declination both in degrees; DDD.dd). Press 'tab', 'return', or 'comma' on your keyboard to finish entering the coordinate (clicking off the text box will also work).
Values outside the bounds
Right Ascension values outside the bounds of 0.0 <= R.A. <= 360.0 degrees will be wrapped to fit with these bounds.
![](https://outerspace.stsci.edu/download/thumbnails/104958263/coords_success.png?version=1&modificationDate=1629752420219&api=v2)
Declination values outside the bounds of -90.0 <= Dec. <= 90.0 will be parsed as invalid.
![](https://outerspace.stsci.edu/download/thumbnails/104958263/coords_falure.png?version=1&modificationDate=1629752420254&api=v2)
For positive values, you may optionally decide to include a '+' sign.  
When entering a coordinate, do not include a comma or semicolon between R.A. and Dec. Separate them with only a space.
Since there are a wide variety of ways to upload lists of objects, a number of sample files is provided in the table below.
**CSV File Format Example**
target,ra,dec,dataset_id
M101, 14:03:12.545, +54:20:56.22, J8OB02011
51 Peg, 22 57 27.960, +20 46 07.75, O4ZE04020
TRAPPIST-1,23h06m29.368s,-05h02m29.03s, ID4301QPQ
helix nebula, 22:29:38.545, -20:50:13.75, W1KA2T01T
Description | Sample Upload File
---|---
One column, only object names. | [example_idonly.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idonly.csv?version=1&modificationDate=1629859322772&api=v2)
One column, only coordinates. | [example_coordonly.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_coordonly.csv?version=1&modificationDate=1629859322208&api=v2)
One column, only dataset IDs. | [example_datasetsonly.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_datasetsonly.csv?version=1&modificationDate=1629859322378&api=v2)
Three columns, object names and coordinates. | [example_idandcoords.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idandcoords.csv?version=1&modificationDate=1629859322476&api=v2)
Four columns, object names, coordinates, and dataset IDs. | [example_idandcoordsanddatasets.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idandcoordsanddatasets.csv?version=1&modificationDate=1629859322585&api=v2)
Five columns, object names, coordinates, and two user-defined columns. | [example_idandcoordsandnotes.csv](https://outerspace.stsci.edu/download/attachments/104958263/example_idandcoordsandnotes.csv?version=1&modificationDate=1629859322680&api=v2)
Upload A List Of Object Names To Resolve Into Coordinates, Cone Search Coordinates, or Dataset IDs
A file can be uploaded into the form that contains a list of object names to resolve into coordinates, coordinate pairs of Right Ascension and Declination, or Dataset IDs. The file must be in comma-separated value (CSV) format, and the top row must contain a header with column names. The header row does not need any special character in the front: the first row is always read in as the header row. The header row is case-insensitive.
The uploaded file must contain at least one of three search parameters: object name (using the header "Target"), coordinate (using the headers "RA" and "Dec"), and/or dataset ID (using the header "Dataset_ID"). Remember that the headers are case-insensitive ("dataset_id" works as well as "Dataset_ID").  
* If the file contains object names, coordinates, and dataset IDs, the search form will use the dataset IDs and return those exact matches in the search results.
* If the file contains object names and coordinates, the search form will use the coordinates to perform cone searches, and it will not attempt to resolve any object names.
* If the file contains only object names, the search form will attempt to resolve them into coordinates.  
The number of object names that were successfully and unsuccessfully resolved is reported, and clicking on the number of unsuccessful name resolves will display an overlay with more information and line numbers to provide further information.
The columns in the uploaded file are included in the search results table on the far right, with labels of 'User File <col>'. For example, if the uploaded file contained rows labeled 'target', 'ra', 'dec', 'dataset_id' they are included in the search results table as 'User File target', 'User File ra', 'User File dec', and 'User File dataset_id'.
If there are additional columns in the uploaded CSV file, they will be included in the search result table in the far right as well. This allows additional columns to be cross-matched to the search results and thus included when exporting the search result table.
![](https://outerspace.stsci.edu/download/attachments/104958263/search_radius.png?version=1&modificationDate=1629865182406&api=v2)
Specifying The Cone Search Radius
Regardless of how a position on the sky is specified (through an object name resolved into coordinates, or directly using Right Ascension and Declination) the size of the search radius is defined using the 'Search Radius' component. The radius may be defined in either arcseconds or arcminutes. The default size is 3 arcminutes in the form and a maximum radius of 30 arcminutes is allowed.
If a list is uploaded to the search form, this cone search radius is applied to every object name or coordinate in that list.
If a list of Dataset IDs is specified, a cone search is not conducted; thus this component is not used. Instead, a direct match on the dataset IDs is performed.
* * *

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)
* [Target Name Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 7 END -->

