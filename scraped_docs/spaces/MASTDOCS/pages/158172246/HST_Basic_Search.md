---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search"
date_accessed: "2026-03-11T11:36:13.389779"
---

<!-- CHUNK 1 START -->
This page shows two side-by-side examples of a basic search in the Classic and New ("Missions") Search forms.
**On this page...**
* 1[Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-SearchParameters)
* 2[Entering your Target(s)](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-EnteringyourTarget\(s\))
* 2.1[Manually](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Manually)
* 2.2[By Uploading a File](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-ByUploadingaFile)
* 3[Selecting Instruments](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-SelectingInstruments)
* 4[Filtering by Given Fields: Exposure Time](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-FilteringbyGivenFields:ExposureTime)
* 5[Filtering by Other Fields: Wavelength](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-FilteringbyOtherFields:Wavelength)
* 6[Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Results)
* 7[Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Previews)
* 8[Downloads](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Downloads)
* 9[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Search Parameters"} -->
In this example search, we'll be looking for UV observations of the edge-on galaxies M102 and M104. The left column will follow this process in the classic search form, while the right column will do the same in the new search form.
* * *

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Entering your Target(s)", "Header 2": "Manually"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_target_search.png?version=1&modificationDate=1693413133436&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_target_search.png?version=1&modificationDate=1693413133429&api=v2)
In the old search form, there were three fields you could fill with information about the target(s): 'Target Name', 'Right Ascension', and 'Declination'. To avoid resolving a target (for example, when looking for a a Solar System object), you could select 'Don't Resolve' from the dropdown menu.
The 'Equinox' box allowed you to specify the equinox of your choice: either B1900, B1950, or J2000.
Search 'Radius' had to be entered in arcminutes, and could be either an integer or floating point number.
The new 'Object Name' box allows you to search by target name, or enter the coordinates directly. With the 'Resolve' box checked, the names will be resolved by a query using , , and several databases internal to MAST. The box will turn green if the target is successfully resolved, or yellow if it is not. You can uncheck the box to turn off the resolve function, allowing you to search by direct matches of the target names as submitted in the proposals; this is especially useful when looking for Solar System targets. Wildcards are supported using '*' if the Resolve box is not checked.
There is no 'Equinox' option in the new search; all searches are assumed to be J2000.
'Search radius' can now be specified in either arcminutes or arcseconds. Any inputs will be rounded up to the nearest integer.
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Entering your Target(s)", "Header 2": "By Uploading a File"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/file_upload_form.png?version=1&modificationDate=1693413133371&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/158172246/upload_button.png?version=1&modificationDate=1693413133356&api=v2)  
To upload a file required switching to the 'File Upload Form'. From here, you could upload your file, then edit the search fields to reflect your file structure.
The 'Upload List of Objects' button is located above the search bar, to the left of the 'Resolve' checkbox. When you click it, you're given the option to select your CSV file containing a list of targets. The first row of this CSV should be a header containing the column names. For more details about acceptable formatting, and to see examples, see the [Upload List Search page](https://outerspace.stsci.edu/display/MASTDOCS/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-upload_list).
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Selecting Instruments"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_instrument_selection.png?version=1&modificationDate=1693413133423&api=v2)
![](https://outerspace.stsci.edu/download/attachments/158172246/new_instrument_selection.png?version=1&modificationDate=1693413133416&api=v2)  
Instrument selection was divided into three sections: 'Imagers', 'Spectrographs', and 'Other'. To get all data from the WFC3, as we do in the example, you must select it in both the 'Imagers' and 'Spectrographs' columns.
The new instrument collection field is notably changed from its predecessor: you first select the type of data you want (i.e. Spectrum, Image, or All), then select the associated instruments. This has the advantage of making it a single-click selection.
In the upper right of the instrument selection, there are two checkboxes; the left option is used to select all instruments, while the right option deselects all instruments. ![](https://outerspace.stsci.edu/download/thumbnails/158172246/toggle_all_or_none.png?version=1&modificationDate=1693413133336&api=v2)  
These search fields also present an opportunity to select Science data, Calibration data, or All. These categories are set by the data processing pipeline; generally, you will want to specify 'All' or 'Science'.
* * *

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Filtering by Given Fields: Exposure Time"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_exposure_time.png?version=1&modificationDate=1693413133378&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/mm-exptime.png?version=1&modificationDate=1693413200004&api=v2)
Many queryable fields were available to be filled in on the Classic Form. In this example, we filter for observations with an exposure time longer than 1000 seconds.
The same fields from the Classic Form are also available in the Missions Form. Although their shapes have changed, their core functionality remains the same; entering '>1000' in the exposure duration field still returns results with an exposure time greater than 1000 seconds.
* * *

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Filtering by Other Fields: Wavelength"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_wavelength_selection.png?version=1&modificationDate=1693413133408&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_exposure_time.png?version=1&modificationDate=1693413133286&api=v2)  
In the Classic Form, it was possible to add a maximum of two 'User-specified' fields. You could choose one option from a drop-down menu, then enter an appropriate value in the box to its right.
Unlike the Classic Form, the Missions Form is not limited to two additional fields. You may add more by clicking the 'Add Another Condition' button. ![](https://outerspace.stsci.edu/download/thumbnails/158172246/new_condition.png?version=1&modificationDate=1693413133312&api=v2)
You can search for an additional column by typing directly in the box. The 'typeahead' feature will suggest criteria based on matching column names _and_ column descriptions.
* * *

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Results"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_results.png?version=1&modificationDate=1693413133296&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_results.png?version=1&modificationDate=1693413133305&api=v2)  
In HST Classic, the results were segregated by target. For the search we performed, this results in two tables: one for M102, and one for M104.
In the Missions Form, all results are collated into one table. This makes it possible to filter and sort across all of your results at once.
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Previews"} -->
![](https://outerspace.stsci.edu/download/thumbnails/158172246/old_preview.png?version=1&modificationDate=1693413133243&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_preview.png?version=1&modificationDate=1693413133234&api=v2)  
To access an image preview, you could click on the link under either the 'Dataset' or 'Target Name' columns.
As before, you can click on the link under either column to open a preview page. The preview page is identical to the one from the HST Classic Search.
* * *

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Downloads"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_download.png?version=1&modificationDate=1693413133153&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_download.png?version=1&modificationDate=1693413133079&api=v2)  
After selecting your desired observations, the data had to be staged for retrieval from STDADS. This required an email address so that you could be notified when the files had been staged.
Using file options, you could select a desired file option or extension, but not specific files.
As in the old search form, you first select your desired observations. Then, click the 'Download Data' button to open the Download menu displayed above. ![](https://outerspace.stsci.edu/download/thumbnails/158172246/download_data.png?version=1&modificationDate=1693413133092&api=v2)
You can still filter by file option or extension. There are also additional options to individually select files from the list using the checkboxes or use the 'All', 'None', or 'Recommended' options.
After selecting the files you want, the 'Download with API Query' and 'Start Download' buttons will become active. 'Start Download' is quick and convenient for small batches of files. If your query includes many thousands of files, or is larger than a few GB, you should use the API Query option. This will generate a curl script that you can run at your convenience to download your files.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)  
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
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
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
This page shows two side-by-side examples of a basic search in the Classic and New ("Missions") Search forms.
**On this page...**
* 1[Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-SearchParameters)
* 2[Entering your Target(s)](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-EnteringyourTarget\(s\))
* 2.1[Manually](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Manually)
* 2.2[By Uploading a File](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-ByUploadingaFile)
* 3[Selecting Instruments](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-SelectingInstruments)
* 4[Filtering by Given Fields: Exposure Time](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-FilteringbyGivenFields:ExposureTime)
* 5[Filtering by Other Fields: Wavelength](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-FilteringbyOtherFields:Wavelength)
* 6[Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Results)
* 7[Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Previews)
* 8[Downloads](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-Downloads)
* 9[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search#HSTBasicSearch-ForFurtherReading...)

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Search Parameters"} -->
In this example search, we'll be looking for UV observations of the edge-on galaxies M102 and M104. The left column will follow this process in the classic search form, while the right column will do the same in the new search form.
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Entering your Target(s)", "Header 2": "Manually"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_target_search.png?version=1&modificationDate=1693413133436&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_target_search.png?version=1&modificationDate=1693413133429&api=v2)
In the old search form, there were three fields you could fill with information about the target(s): 'Target Name', 'Right Ascension', and 'Declination'. To avoid resolving a target (for example, when looking for a a Solar System object), you could select 'Don't Resolve' from the dropdown menu.
The 'Equinox' box allowed you to specify the equinox of your choice: either B1900, B1950, or J2000.
Search 'Radius' had to be entered in arcminutes, and could be either an integer or floating point number.
The new 'Object Name' box allows you to search by target name, or enter the coordinates directly. With the 'Resolve' box checked, the names will be resolved by a query using , , and several databases internal to MAST. The box will turn green if the target is successfully resolved, or yellow if it is not. You can uncheck the box to turn off the resolve function, allowing you to search by direct matches of the target names as submitted in the proposals; this is especially useful when looking for Solar System targets. Wildcards are supported using '*' if the Resolve box is not checked.
There is no 'Equinox' option in the new search; all searches are assumed to be J2000.
'Search radius' can now be specified in either arcminutes or arcseconds. Any inputs will be rounded up to the nearest integer.
* * *

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Entering your Target(s)", "Header 2": "By Uploading a File"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/file_upload_form.png?version=1&modificationDate=1693413133371&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/158172246/upload_button.png?version=1&modificationDate=1693413133356&api=v2)  
To upload a file required switching to the 'File Upload Form'. From here, you could upload your file, then edit the search fields to reflect your file structure.
The 'Upload List of Objects' button is located above the search bar, to the left of the 'Resolve' checkbox. When you click it, you're given the option to select your CSV file containing a list of targets. The first row of this CSV should be a header containing the column names. For more details about acceptable formatting, and to see examples, see the [Upload List Search page](https://outerspace.stsci.edu/display/MASTDOCS/Cone+Search+And+Upload+List+Search#ConeSearchAndUploadListSearch-upload_list).
* * *

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Selecting Instruments"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_instrument_selection.png?version=1&modificationDate=1693413133423&api=v2)
![](https://outerspace.stsci.edu/download/attachments/158172246/new_instrument_selection.png?version=1&modificationDate=1693413133416&api=v2)  
Instrument selection was divided into three sections: 'Imagers', 'Spectrographs', and 'Other'. To get all data from the WFC3, as we do in the example, you must select it in both the 'Imagers' and 'Spectrographs' columns.
The new instrument collection field is notably changed from its predecessor: you first select the type of data you want (i.e. Spectrum, Image, or All), then select the associated instruments. This has the advantage of making it a single-click selection.
In the upper right of the instrument selection, there are two checkboxes; the left option is used to select all instruments, while the right option deselects all instruments. ![](https://outerspace.stsci.edu/download/thumbnails/158172246/toggle_all_or_none.png?version=1&modificationDate=1693413133336&api=v2)  
These search fields also present an opportunity to select Science data, Calibration data, or All. These categories are set by the data processing pipeline; generally, you will want to specify 'All' or 'Science'.
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Filtering by Given Fields: Exposure Time"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_exposure_time.png?version=1&modificationDate=1693413133378&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/mm-exptime.png?version=1&modificationDate=1693413200004&api=v2)
Many queryable fields were available to be filled in on the Classic Form. In this example, we filter for observations with an exposure time longer than 1000 seconds.
The same fields from the Classic Form are also available in the Missions Form. Although their shapes have changed, their core functionality remains the same; entering '>1000' in the exposure duration field still returns results with an exposure time greater than 1000 seconds.
* * *

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Filtering by Other Fields: Wavelength"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_wavelength_selection.png?version=1&modificationDate=1693413133408&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_exposure_time.png?version=1&modificationDate=1693413133286&api=v2)  
In the Classic Form, it was possible to add a maximum of two 'User-specified' fields. You could choose one option from a drop-down menu, then enter an appropriate value in the box to its right.
Unlike the Classic Form, the Missions Form is not limited to two additional fields. You may add more by clicking the 'Add Another Condition' button. ![](https://outerspace.stsci.edu/download/thumbnails/158172246/new_condition.png?version=1&modificationDate=1693413133312&api=v2)
You can search for an additional column by typing directly in the box. The 'typeahead' feature will suggest criteria based on matching column names _and_ column descriptions.
* * *

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Results"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_results.png?version=1&modificationDate=1693413133296&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_results.png?version=1&modificationDate=1693413133305&api=v2)  
In HST Classic, the results were segregated by target. For the search we performed, this results in two tables: one for M102, and one for M104.
In the Missions Form, all results are collated into one table. This makes it possible to filter and sort across all of your results at once.
* * *

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Previews"} -->
![](https://outerspace.stsci.edu/download/thumbnails/158172246/old_preview.png?version=1&modificationDate=1693413133243&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_preview.png?version=1&modificationDate=1693413133234&api=v2)  
To access an image preview, you could click on the link under either the 'Dataset' or 'Target Name' columns.
As before, you can click on the link under either column to open a preview page. The preview page is identical to the one from the HST Classic Search.
* * *

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Downloads"} -->
![](https://outerspace.stsci.edu/download/attachments/158172246/old_download.png?version=1&modificationDate=1693413133153&api=v2)  
![](https://outerspace.stsci.edu/download/attachments/158172246/new_download.png?version=1&modificationDate=1693413133079&api=v2)  
After selecting your desired observations, the data had to be staged for retrieval from STDADS. This required an email address so that you could be notified when the files had been staged.
Using file options, you could select a desired file option or extension, but not specific files.
As in the old search form, you first select your desired observations. Then, click the 'Download Data' button to open the Download menu displayed above. ![](https://outerspace.stsci.edu/download/thumbnails/158172246/download_data.png?version=1&modificationDate=1693413133092&api=v2)
You can still filter by file option or extension. There are also additional options to individually select files from the list using the checkboxes or use the 'All', 'None', or 'Recommended' options.
After selecting the files you want, the 'Download with API Query' and 'Start Download' buttons will become active. 'Start Download' is quick and convenient for small batches of files. If your query includes many thousands of files, or is larger than a few GB, you should use the API Query option. This will generate a curl script that you can run at your convenience to download your files.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 21 END -->

