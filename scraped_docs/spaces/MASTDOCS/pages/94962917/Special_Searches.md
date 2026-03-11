---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches"
date_accessed: "2026-03-11T16:26:33.392912"
content_length: 30239
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Search Virtual Observatory Collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-VO_searchSearchVirtualObservatoryCollections)
* 2[Search the Hubble Source Catalog](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-SearchtheHubbleSourceCatalog)
* 3[Create a DOI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-DOICreateaDOI)
* 4[Load a DOI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-LoadaDOI)
* 5[Other Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-OtherSearches)
* 6[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-ForFurtherReading...)  
The Portal enables searches of a few special collections, most of which can be selected from the collection menu.
![](https://outerspace.stsci.edu/download/thumbnails/94962917/menu_selectCollection_VO.png?version=1&modificationDate=1662673220939&api=v2)
The [Virtual Observatory](https://archive.stsci.edu/access-mast-data/virtual-observatory) (VO) is composed of electronic archives from many astronomical centers around the world. These archives contain a wide variety of data and other resources, including catalogs, images, and spectra. The results of a VO search will look similar to that shown in the figure below.
![VO search for M57](https://outerspace.stsci.edu/download/attachments/94962917/panel_VOsearch.png?version=1&modificationDate=1662673222043&api=v2)A search of the VO for the target M 57. The results table shows all VO resources (images, spectra, or catalogs) within a 1 arcmin radius. The Data Load button in each row will provide more descriptive information and links to retrieve the data.
Searching the VO with the Portal differs from a [basic search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) in a few important respects:
1. Searches are only by target name or sky coordinates; there is no "advanced search" option.
2. The resuts of a VO search are not observations of a target. Rather, the table rows contain metadata about each VO resource, including the type of data objects (images, spectra, catalog).
3. To access science data, click the Data Load button![Data Load button](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_loadData.png?version=1&modificationDate=1662673222262&api=v2), which in effect initiates a search of that resource to return the associated science data. This action is referred to as a _drill-down_ , and is a key component of using the Portal to explore multi-tiered data hierarchies, such as those in the VO.
4. Click the file icon![File icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_file_white.png?version=1&modificationDate=1662673221991&api=v2)in a given row to retrieve the science metadata (in XML format) associated with that resource.
5. Optionally download the metadata in the results table to a file on your local system by clicking the export button ![Export Button](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_fileDownload.png?version=1&modificationDate=1662673222199&api=v2). Select your desired output format in the _**Export**_ dialog.  
VO searches are effectively simultaneous searches of multiple astronomical archives. It may take considerable time (minutes) for the last archive to return results. Since the results are displayed as they become available, it is possible to browse or download some results while others are still being loaded.

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Search the Hubble Source Catalog"} -->
The [Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/) (HSC) consists of photometry of sources that have been imaged with one or more instruments on HST. MAST supports multiple ways to search the HSC; the Portal allows searches in a circular region around a user-specified position on the sky (a _**cone search**_). Searching the HSC is a form of [catalog search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search), and the chapter on [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials) shows several science-motivated example searches.
Although an earlier version of the HSC is still available, it is best to search the version 3 catalog (HSCv3), which is substantially better and now contains the [Hubble Catalog of Variables](https://archive.stsci.edu/hlsp/hcv).
As with VO searches, an HSC search returns results that differ from a [basic search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) in a few important respects:
1. Searches are only by target name or sky coordinates; there is no "advanced search" option.
2. It is possible to retrieve brightness measurements that were made using a finite aperture (MagAper2), or an approximate total brightness (MagAuto). See
3. The results of an HSC search are not exposures of a target. Rather, the table rows contain photometric measurements and other metadata about each source.
4. It is possible to access the images that contributed to each photometric measurement by clicking the **Data Load** icon![Data Load Icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_loadData.png?version=1&modificationDate=1662673222262&api=v2). These images can be overlayed in the AstroView tool by clicking the **Overlay** icon![Overlay icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_overlay.png?version=1&modificationDate=1662673221863&api=v2).  
1. To retrieve one or more of the contributing images, click the **Download Basket** icon![Download Basket Icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_basket_simple.png?version=1&modificationDate=1662673221943&api=v2); or click the **File** icon![File Icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_file_white.png?version=1&modificationDate=1662673221991&api=v2) to instantly download a single image.
5. Optionally download the photometric results table (or selected rows within the table) to a file on your local system by clicking the **Export** button ![Export Button](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_fileDownload.png?version=1&modificationDate=1662673222199&api=v2). Select your desired output format in the _**Export** **Dialog**_.  
A Digital Object Identifier (DOI) is a persistent link to a resource on the internet, and is often used in astronomy to provide access to specific data collections. Investigators can use a [special instance of the Portal](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html) to generate a DOI for one or more datasets hosted by MAST. This will generate a permanent link that may be included in a research paper to refer to the data that were analyzed.
DOIs for many collections, including High-Level Science Products, certain catalogs, and Kepler/K2 campaigns have already been created. To use them in your work, see the detailed [DOI documentation](https://archive.stsci.edu/publishing/doi). To create a new custom DOI for data you wish to publish, see the following how-to video, or follow the written instructions below.  
Create-a-DOI walkthrough video.  
| Instruction | Notes
---|---|---
**1** |  Navigate to the DOI Portal at: [https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html.](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html) You must login to the Portal to create a DOI. |  ![DOI Portal Logo](https://outerspace.stsci.edu/download/thumbnails/94962917/logo_DOIportal.png?version=1&modificationDate=1662673222669&api=v2) ![Portal Login Box](https://outerspace.stsci.edu/download/thumbnails/94962917/login_Portal.png?version=1&modificationDate=1662673222359&api=v2)
**2** | Execute a [Portal search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) for observations that include the data to be published. | !['Search by' dropdown menu](https://outerspace.stsci.edu/download/thumbnails/94962917/menu_DOI_searchBy.png?version=1&modificationDate=1662673222618&api=v2)
**3** |  Select rows in the results table that correspond to the specific observations to which the DOI should refer, and place them in the download basket. If necessary, make multiple searches and place relevant observations from each in the download basket. | !['Add to DOI basket' button](https://outerspace.stsci.edu/download/thumbnails/94962917/button_DOI_basket.png?version=1&modificationDate=1662673222548&api=v2)
**4** | Click the **My DOI Basket** button to bring up Download Manager, which will look something like the picture below. | !['My DOI basket' button](https://outerspace.stsci.edu/download/thumbnails/94962917/button_DOI_dlm.png?version=1&modificationDate=1662673222497&api=v2)  
| ![Example DOI basket](https://outerspace.stsci.edu/download/attachments/94962917/dlm_DOI_panel.png?version=1&modificationDate=1662673222305&api=v2)
**5** | Select the rows corresponding to the desired observation IDs and filters, then click the button to create a DOI. If you need to update an existing DOI you created, contact MAST.
|  ![Create and Upload DOI buttons](https://outerspace.stsci.edu/download/thumbnails/94962917/button_createDOI.png?version=1&modificationDate=1662673222445&api=v2)  
**6** | Fill in the DOI requested metadata in the dialog box, then click the **Create DOI** button. | !['Create DOI' box with metadata fields](https://outerspace.stsci.edu/download/attachments/94962917/dialog_DOImetada.png?version=1&modificationDate=1662673222398&api=v2)
To update a DOI you created with new information, contact the

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Load a DOI"} -->
There are three ways to access the data that a MAST DOI points to:
1. Resolve the DOI in your browser. For example, for the TESS Input Catalog (doi:**10.17909/fwdt-2x66** , from the [list of pre-made MAST DOIs](https://archive.stsci.edu/publishing/doi)), the following URLs will both work:  
[ https://archive.stsci.edu/doi/resolve/resolve.html?doi=**10.17909/fwdt-2x66**](https://archive.stsci.edu/doi/resolve/resolve.html?doi=10.17909/fwdt-2x66)
These will lead you to a landing page, where you can follow a link to "display data":
![A MAST DOI landing page. A link labeled Display Data is highlighted.](https://outerspace.stsci.edu/download/attachments/94962917/viewdata_highlight.png?version=1&modificationDate=1662673221350&api=v2)
Depending on the nature of the data cited by the DOI, the "display data" link will either load a set of observations in the Portal, or lead to another webpage with information about retrieving the data.  
2. You can search for a MAST DOI's observations using the general-purpose MAST Portal as follows. This will only work if the DOI you wish to access points _directly_ to observations in the MAST Portal. (So it won't work for the TESS Input Catalog pre-made DOI we used above. We'll instead use  
| Instruction | Notes
---|---|---
**1** | Navigate to the Portal at: <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html> | ![MAST Portal logo.](https://outerspace.stsci.edu/download/attachments/94962917/mastlogo.png?version=1&modificationDate=1662673221305&api=v2)
**2** | Under the **Select a collection...** dropdown menu, choose __Observations in a DOI__. | ![Dropdown for Select a collection. Observations in a DOI is highlighted.](https://outerspace.stsci.edu/download/attachments/94962917/obsinadoi.png?version=1&modificationDate=1662673221233&api=v2)Dropdown for Select a collection. Observations in a DOI is highlighted.
**3** | Enter the DOI string (e.g., **Search**. | ![Under Enter a DOI, a number beginning 10.17909 is typed into the search field.](https://outerspace.stsci.edu/download/thumbnails/94962917/searchdoi.png?version=1&modificationDate=1662673221079&api=v2)
This method will not work for certain pre-made MAST DOIs for catalogs, HLSP webpages, or bulk mission data, which point to informational webpages or custom download scripts even when the data actually are available in the Portal.
3. You can use the MAST DOI Portal view any DOIs that you have created using your account. You will not be able to download data using this method; see above for data retrieval options.  
| Instruction | Notes
---|---|---
**1** | Navigate to the DOI Portal at: [https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html.](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html)You must login to the Portal to see the list of DOIs that you have created. |  ![DOI Portal Logo.](https://outerspace.stsci.edu/download/attachments/94962917/logo_DOIportal.png?version=1&modificationDate=1662673222669&api=v2) ![Portal Login Box](https://outerspace.stsci.edu/download/thumbnails/94962917/login_Portal.png?version=1&modificationDate=1662673222359&api=v2)
**2** | Select __Show my DOIs__ in the **Search by...** dropdown menu, and click the **Load All** button. | ![Search By dropdown, with Show my DOIs highlighted. A button labeled Load All is to the right.](https://outerspace.stsci.edu/download/attachments/94962917/showdois_loadall.png?version=1&modificationDate=1662673221146&api=v2)
**3** | Select the __Show DOI Data__ entry in the Actions column. | ![Arrow points to an image of a telescope in the Actions column, which is the link to Show DOI Data.](https://outerspace.stsci.edu/download/attachments/94962917/showdata.png?version=1&modificationDate=1662673221115&api=v2)

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Other Searches"} -->
A few special searches enable access to lesser-used or mission-specific collections, which are listed in the table below.
Collection | Description
---|---
HSC Spectra | A collection of tens of thousands of spectra in various bands associated with sources in the [Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/). Many of the sources are categorized by astrophysical type.
WFC3 PSF | Search a library of observed point-spread functions (PSFs) from archived HST/WFC3 observations. These PSFs enable higher precision photometry of WFC3 observations. See [PSF Search](https://www.stsci.edu/hst/instrumentation/wfc3/data-analysis/psf/psf-search) for more information about this collection.
JWST Instrument Keywords | Search for JWST science data using header keyword metadata. See the [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search) page for more information about how to perform a search on JWST data.
JWST WSS | Search for JWST wavefront sensing (optical path difference) data. See the [Supplemental Products](https://outerspace.stsci.edu/display/MASTDOCS/Supplemental+Products) page for details about this and other ancillary file types.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [DOI documentation](https://archive.stsci.edu/doi/search/)  
Unable to load page tree. It seems that you do not have permission to view the root page.
**On this page...**
* 1[Search Virtual Observatory Collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-VO_searchSearchVirtualObservatoryCollections)
* 2[Search the Hubble Source Catalog](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-SearchtheHubbleSourceCatalog)
* 3[Create a DOI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-DOICreateaDOI)
* 4[Load a DOI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-LoadaDOI)
* 5[Other Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-OtherSearches)
* 6[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-ForFurtherReading...)  
The Portal enables searches of a few special collections, most of which can be selected from the collection menu.
![](https://outerspace.stsci.edu/download/thumbnails/94962917/menu_selectCollection_VO.png?version=1&modificationDate=1662673220939&api=v2)
The [Virtual Observatory](https://archive.stsci.edu/access-mast-data/virtual-observatory) (VO) is composed of electronic archives from many astronomical centers around the world. These archives contain a wide variety of data and other resources, including catalogs, images, and spectra. The results of a VO search will look similar to that shown in the figure below.
![VO search for M57](https://outerspace.stsci.edu/download/attachments/94962917/panel_VOsearch.png?version=1&modificationDate=1662673222043&api=v2)A search of the VO for the target M 57. The results table shows all VO resources (images, spectra, or catalogs) within a 1 arcmin radius. The Data Load button in each row will provide more descriptive information and links to retrieve the data.
Searching the VO with the Portal differs from a [basic search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) in a few important respects:
1. Searches are only by target name or sky coordinates; there is no "advanced search" option.
2. The resuts of a VO search are not observations of a target. Rather, the table rows contain metadata about each VO resource, including the type of data objects (images, spectra, catalog).
3. To access science data, click the Data Load button![Data Load button](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_loadData.png?version=1&modificationDate=1662673222262&api=v2), which in effect initiates a search of that resource to return the associated science data. This action is referred to as a _drill-down_ , and is a key component of using the Portal to explore multi-tiered data hierarchies, such as those in the VO.
4. Click the file icon![File icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_file_white.png?version=1&modificationDate=1662673221991&api=v2)in a given row to retrieve the science metadata (in XML format) associated with that resource.
5. Optionally download the metadata in the results table to a file on your local system by clicking the export button ![Export Button](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_fileDownload.png?version=1&modificationDate=1662673222199&api=v2). Select your desired output format in the _**Export**_ dialog.  
VO searches are effectively simultaneous searches of multiple astronomical archives. It may take considerable time (minutes) for the last archive to return results. Since the results are displayed as they become available, it is possible to browse or download some results while others are still being loaded.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Search the Hubble Source Catalog"} -->
The [Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/) (HSC) consists of photometry of sources that have been imaged with one or more instruments on HST. MAST supports multiple ways to search the HSC; the Portal allows searches in a circular region around a user-specified position on the sky (a _**cone search**_). Searching the HSC is a form of [catalog search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search), and the chapter on [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials) shows several science-motivated example searches.
Although an earlier version of the HSC is still available, it is best to search the version 3 catalog (HSCv3), which is substantially better and now contains the [Hubble Catalog of Variables](https://archive.stsci.edu/hlsp/hcv).
As with VO searches, an HSC search returns results that differ from a [basic search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) in a few important respects:
1. Searches are only by target name or sky coordinates; there is no "advanced search" option.
2. It is possible to retrieve brightness measurements that were made using a finite aperture (MagAper2), or an approximate total brightness (MagAuto). See
3. The results of an HSC search are not exposures of a target. Rather, the table rows contain photometric measurements and other metadata about each source.
4. It is possible to access the images that contributed to each photometric measurement by clicking the **Data Load** icon![Data Load Icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_loadData.png?version=1&modificationDate=1662673222262&api=v2). These images can be overlayed in the AstroView tool by clicking the **Overlay** icon![Overlay icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_overlay.png?version=1&modificationDate=1662673221863&api=v2).  
1. To retrieve one or more of the contributing images, click the **Download Basket** icon![Download Basket Icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_basket_simple.png?version=1&modificationDate=1662673221943&api=v2); or click the **File** icon![File Icon](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_file_white.png?version=1&modificationDate=1662673221991&api=v2) to instantly download a single image.
5. Optionally download the photometric results table (or selected rows within the table) to a file on your local system by clicking the **Export** button ![Export Button](https://outerspace.stsci.edu/download/thumbnails/94962917/icon_fileDownload.png?version=1&modificationDate=1662673222199&api=v2). Select your desired output format in the _**Export** **Dialog**_.  
A Digital Object Identifier (DOI) is a persistent link to a resource on the internet, and is often used in astronomy to provide access to specific data collections. Investigators can use a [special instance of the Portal](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html) to generate a DOI for one or more datasets hosted by MAST. This will generate a permanent link that may be included in a research paper to refer to the data that were analyzed.
DOIs for many collections, including High-Level Science Products, certain catalogs, and Kepler/K2 campaigns have already been created. To use them in your work, see the detailed [DOI documentation](https://archive.stsci.edu/publishing/doi). To create a new custom DOI for data you wish to publish, see the following how-to video, or follow the written instructions below.  
Create-a-DOI walkthrough video.  
| Instruction | Notes
---|---|---
**1** |  Navigate to the DOI Portal at: [https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html.](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html) You must login to the Portal to create a DOI. |  ![DOI Portal Logo](https://outerspace.stsci.edu/download/thumbnails/94962917/logo_DOIportal.png?version=1&modificationDate=1662673222669&api=v2) ![Portal Login Box](https://outerspace.stsci.edu/download/thumbnails/94962917/login_Portal.png?version=1&modificationDate=1662673222359&api=v2)
**2** | Execute a [Portal search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search) for observations that include the data to be published. | !['Search by' dropdown menu](https://outerspace.stsci.edu/download/thumbnails/94962917/menu_DOI_searchBy.png?version=1&modificationDate=1662673222618&api=v2)
**3** |  Select rows in the results table that correspond to the specific observations to which the DOI should refer, and place them in the download basket. If necessary, make multiple searches and place relevant observations from each in the download basket. | !['Add to DOI basket' button](https://outerspace.stsci.edu/download/thumbnails/94962917/button_DOI_basket.png?version=1&modificationDate=1662673222548&api=v2)
**4** | Click the **My DOI Basket** button to bring up Download Manager, which will look something like the picture below. | !['My DOI basket' button](https://outerspace.stsci.edu/download/thumbnails/94962917/button_DOI_dlm.png?version=1&modificationDate=1662673222497&api=v2)  
| ![Example DOI basket](https://outerspace.stsci.edu/download/attachments/94962917/dlm_DOI_panel.png?version=1&modificationDate=1662673222305&api=v2)
**5** | Select the rows corresponding to the desired observation IDs and filters, then click the button to create a DOI. If you need to update an existing DOI you created, contact MAST.
|  ![Create and Upload DOI buttons](https://outerspace.stsci.edu/download/thumbnails/94962917/button_createDOI.png?version=1&modificationDate=1662673222445&api=v2)  
**6** | Fill in the DOI requested metadata in the dialog box, then click the **Create DOI** button. | !['Create DOI' box with metadata fields](https://outerspace.stsci.edu/download/attachments/94962917/dialog_DOImetada.png?version=1&modificationDate=1662673222398&api=v2)
To update a DOI you created with new information, contact the

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Load a DOI"} -->
There are three ways to access the data that a MAST DOI points to:
1. Resolve the DOI in your browser. For example, for the TESS Input Catalog (doi:**10.17909/fwdt-2x66** , from the [list of pre-made MAST DOIs](https://archive.stsci.edu/publishing/doi)), the following URLs will both work:  
[ https://archive.stsci.edu/doi/resolve/resolve.html?doi=**10.17909/fwdt-2x66**](https://archive.stsci.edu/doi/resolve/resolve.html?doi=10.17909/fwdt-2x66)
These will lead you to a landing page, where you can follow a link to "display data":
![A MAST DOI landing page. A link labeled Display Data is highlighted.](https://outerspace.stsci.edu/download/attachments/94962917/viewdata_highlight.png?version=1&modificationDate=1662673221350&api=v2)
Depending on the nature of the data cited by the DOI, the "display data" link will either load a set of observations in the Portal, or lead to another webpage with information about retrieving the data.  
2. You can search for a MAST DOI's observations using the general-purpose MAST Portal as follows. This will only work if the DOI you wish to access points _directly_ to observations in the MAST Portal. (So it won't work for the TESS Input Catalog pre-made DOI we used above. We'll instead use  
| Instruction | Notes
---|---|---
**1** | Navigate to the Portal at: <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html> | ![MAST Portal logo.](https://outerspace.stsci.edu/download/attachments/94962917/mastlogo.png?version=1&modificationDate=1662673221305&api=v2)
**2** | Under the **Select a collection...** dropdown menu, choose __Observations in a DOI__. | ![Dropdown for Select a collection. Observations in a DOI is highlighted.](https://outerspace.stsci.edu/download/attachments/94962917/obsinadoi.png?version=1&modificationDate=1662673221233&api=v2)Dropdown for Select a collection. Observations in a DOI is highlighted.
**3** | Enter the DOI string (e.g., **Search**. | ![Under Enter a DOI, a number beginning 10.17909 is typed into the search field.](https://outerspace.stsci.edu/download/thumbnails/94962917/searchdoi.png?version=1&modificationDate=1662673221079&api=v2)
This method will not work for certain pre-made MAST DOIs for catalogs, HLSP webpages, or bulk mission data, which point to informational webpages or custom download scripts even when the data actually are available in the Portal.
3. You can use the MAST DOI Portal view any DOIs that you have created using your account. You will not be able to download data using this method; see above for data retrieval options.  
| Instruction | Notes
---|---|---
**1** | Navigate to the DOI Portal at: [https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html.](https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html)You must login to the Portal to see the list of DOIs that you have created. |  ![DOI Portal Logo.](https://outerspace.stsci.edu/download/attachments/94962917/logo_DOIportal.png?version=1&modificationDate=1662673222669&api=v2) ![Portal Login Box](https://outerspace.stsci.edu/download/thumbnails/94962917/login_Portal.png?version=1&modificationDate=1662673222359&api=v2)
**2** | Select __Show my DOIs__ in the **Search by...** dropdown menu, and click the **Load All** button. | ![Search By dropdown, with Show my DOIs highlighted. A button labeled Load All is to the right.](https://outerspace.stsci.edu/download/attachments/94962917/showdois_loadall.png?version=1&modificationDate=1662673221146&api=v2)
**3** | Select the __Show DOI Data__ entry in the Actions column. | ![Arrow points to an image of a telescope in the Actions column, which is the link to Show DOI Data.](https://outerspace.stsci.edu/download/attachments/94962917/showdata.png?version=1&modificationDate=1662673221115&api=v2)

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Other Searches"} -->
A few special searches enable access to lesser-used or mission-specific collections, which are listed in the table below.
Collection | Description
---|---
HSC Spectra | A collection of tens of thousands of spectra in various bands associated with sources in the [Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/). Many of the sources are categorized by astrophysical type.
WFC3 PSF | Search a library of observed point-spread functions (PSFs) from archived HST/WFC3 observations. These PSFs enable higher precision photometry of WFC3 observations. See [PSF Search](https://www.stsci.edu/hst/instrumentation/wfc3/data-analysis/psf/psf-search) for more information about this collection.
JWST Instrument Keywords | Search for JWST science data using header keyword metadata. See the [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search) page for more information about how to perform a search on JWST data.
JWST WSS | Search for JWST wavefront sensing (optical path difference) data. See the [Supplemental Products](https://outerspace.stsci.edu/display/MASTDOCS/Supplemental+Products) page for details about this and other ancillary file types.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [DOI documentation](https://archive.stsci.edu/doi/search/)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 9 END -->

