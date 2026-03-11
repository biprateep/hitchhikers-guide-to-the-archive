---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data"
date_accessed: "2026-03-11T11:35:16.647012"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Basic Search for Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-BasicSearchforObservations)
* 2[Science Instrument (SI) Search for JWST Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ScienceInstrument\(SI\)SearchforJWSTObservations)
* 3[Icon Nomenclature ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-IconNomenclatureicon_nomenclature)
* 4[Loading Known Data by URI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-LoadingKnownDatabyURI)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Basic Search for Observations"} -->
After you search for MAST observations following the guide in [Basic Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search), the **Jda** icon ![](https://outerspace.stsci.edu/download/thumbnails/150113061/jdaviz_visualize.png?version=1&modificationDate=1715203290200&api=v2)will appear next to relevant search results that you can view in Jdaviz (**see Figure 1**). This icon indicates that the row result contains data products that can be loaded into the Jdaviz web display. For relevant time-series observations, the **Jda** icon will indicate if you can view the results in the Lcviz web display.
![JDA Icon indicating that this data can be analyzed in Jdaviz](https://outerspace.stsci.edu/download/thumbnails/150113061/mast_jdaviz_new_portal_icon_hover.png?version=1&modificationDate=1715203290211&api=v2)JDA Icon indicating that this data can be analyzed in Jdaviz
**Figure 1 —** The **Jda** icon indicating that the current observation (row result) contains spectroscopic science (level 3) data products that can be visualized in the Jdaviz web quicklook. If you don't see this icon, the data cannot be viewed in the web quicklook.
Clicking the **Visualize Spectra (Jda)** icon produces a drop-down menu with two available options, see**Figure 2**.
The available dropdown options are:
* **Display default Minimum Recommended Product (MRP)** - opens the default [Minimum Recommended Product](https://outerspace.stsci.edu/display/MASTDOCS/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts) for the selected observation in the Jdaviz or Lcviz quicklook spectra page. See [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra) for more.
* **Search through other data products related to this observation** - opens a new page containing all relevant data products associated with the selected Observation that can be loaded into Jdaviz. See [Finding Associated Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113110/Finding+Associated+Data+Products) for more.  
![JDA Dropdown Menu containing both options for the selected observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_jdaviz_new_portal_dropdown.png?version=1&modificationDate=1715203290230&api=v2)JDA Dropdown Menu
**Figure 2 —** The **Jda** dropdown menu, showing options to display the MRP or search for related data products.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Science Instrument (SI) Search for JWST Observations"} -->
After performing a search for JWST observations following the guide in [Science Instrument (SI) Search ](https://outerspace.stsci.edu/display/MASTDOCS/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords), a new icon will appear for search results that can be viewed in Jdaviz (see **Figure 3**). Each row result represents a single JWST data product. Which icon is displayed in each row depends on the type of data product in that row. See [Icon Nomenclature](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-icon_nomenclature) below for the meaning of each icon. Note, this interface is **only** available for JWST observations, and not other MAST products.
![An example SI Keyword Search with the Jdaviz icon displayed next to each observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_portal_jdaviz_si_search.png?version=1&modificationDate=1715203290235&api=v2)SI Keyword Search  
**Figure 3 —** An example SI Keyword search of the MIRI instrument. Search results highlight the right-most Jdaviz icons, displaying the icon most relevant for opening the data product. For example, row 34 displays the Cubeviz icon for opening the s3d IFU FITS file, while row 35 displays the Specviz icon for opening the related 1d extracted spectrum FITS file.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Icon Nomenclature"} -->
These icons represent the Jdaviz application and its different configurations or sub-applications. When performing a Portal or Science Instrument search – as shown above – a relevant icon will be displayed when possible, depending on the data type.
Icon | Name | Description | Data Products | Product Suffixes
---|---|---|---|---
![General Jdaviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/jdaviz_visualize.png?version=1&modificationDate=1715203290200&api=v2)General Jdaviz icon |  | A general icon indicating you can visualize data in Jdaviz | N/A | N/A
![Cubeviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/cubeviz_icon.png?version=1&modificationDate=1715203290242&api=v2)Cubeviz icon |  | The icon for the Cubeviz configuration of Jdaviz | IFU spectral cubes | s3d
![Specviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/specviz_icon.png?version=1&modificationDate=1715203290270&api=v2)Specviz icon |  | The icon for the Specviz configuration of Jdaviz | 1d extracted spectra | x1d, c1d
![Mosviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/mosviz_icon.png?version=1&modificationDate=1715203290286&api=v2)Mosviz icon |  | The icon for the Mosviz configuration of Jdaviz | multi-object spectra | x1d, c1d, s2d, x1dints
![Specviz2d icon](https://outerspace.stsci.edu/download/thumbnails/150113061/speciz2d%20icon.png?version=1&modificationDate=1715203290310&api=v2)Specviz2d icon |  | The icon for the Specviz2d configuration of Jdaviz | 2d and 1d associated extracted spectra | s2d, x1d
![Imviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/imviz%20icon.png?version=1&modificationDate=1715203290319&api=v2)Imviz icon |  | The icon for the Imviz configuration of Jdaviz | Image data | i2
![](https://outerspace.stsci.edu/download/thumbnails/150113061/lcviz_icon.png?version=1&modificationDate=1742314284655&api=v2)lcviz icon |  | The icon for Lcviz, a child application of Jdaviz | time-series data | lc, slc, llc

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Loading Known Data by URI"} -->
Rather than performing a search, if you already know the URI (for MAST products, the "dataURL") of the data product, you can visit the page directly.
The direct URL for the Jdaviz quicklook page is **<https://mast.stsci.edu/viz/ui/>**. It requires one of two query arguments to successfully load a spectrum, either the **uri** or **filename** query argument. Inputting this into the search bar will navigate you to the appropriate page. **Figure 4** shows an example of a spectrum loaded into the specviz module.  
![](https://outerspace.stsci.edu/download/attachments/150113061/image2022-7-7_17-3-44.png?version=1&modificationDate=1715203290326&api=v2)
**Figure 4 —** An example of you might see when using the search bar to load data. This dataset will be opened in Specviz, since it is a **.x1d** file.  
Alternatively, you can navigate to your page directly using the syntax "`**https://mast.stsci.edu/viz/ui/#/spectra?uri=[MAST_DATA_URI]**`". For example, you might navigate directly to`https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits[](https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits)`.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [Portal Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching)
* [Browsing Portal Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data)  
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
* [Jdaviz in the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113048/Jdaviz+in+the+MAST+Portal "Jdaviz in the MAST Portal")
* [Searching for Compatible Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data "Searching for Compatible Data")
* [Interface Field Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide "Interface Field Guide")
* [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra "Viewing Spectra and Images")
* [Finding Associated Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113110/Finding+Associated+Data+Products "Finding Associated Data Products")
* [Supported Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/382632830/Supported+Products "Supported Products")
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
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
**On this page...**
* 1[Basic Search for Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-BasicSearchforObservations)
* 2[Science Instrument (SI) Search for JWST Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ScienceInstrument\(SI\)SearchforJWSTObservations)
* 3[Icon Nomenclature ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-IconNomenclatureicon_nomenclature)
* 4[Loading Known Data by URI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-LoadingKnownDatabyURI)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ForFurtherReading...)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Basic Search for Observations"} -->
After you search for MAST observations following the guide in [Basic Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search), the **Jda** icon ![](https://outerspace.stsci.edu/download/thumbnails/150113061/jdaviz_visualize.png?version=1&modificationDate=1715203290200&api=v2)will appear next to relevant search results that you can view in Jdaviz (**see Figure 1**). This icon indicates that the row result contains data products that can be loaded into the Jdaviz web display. For relevant time-series observations, the **Jda** icon will indicate if you can view the results in the Lcviz web display.
![JDA Icon indicating that this data can be analyzed in Jdaviz](https://outerspace.stsci.edu/download/thumbnails/150113061/mast_jdaviz_new_portal_icon_hover.png?version=1&modificationDate=1715203290211&api=v2)JDA Icon indicating that this data can be analyzed in Jdaviz
**Figure 1 —** The **Jda** icon indicating that the current observation (row result) contains spectroscopic science (level 3) data products that can be visualized in the Jdaviz web quicklook. If you don't see this icon, the data cannot be viewed in the web quicklook.
Clicking the **Visualize Spectra (Jda)** icon produces a drop-down menu with two available options, see**Figure 2**.
The available dropdown options are:
* **Display default Minimum Recommended Product (MRP)** - opens the default [Minimum Recommended Product](https://outerspace.stsci.edu/display/MASTDOCS/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts) for the selected observation in the Jdaviz or Lcviz quicklook spectra page. See [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra) for more.
* **Search through other data products related to this observation** - opens a new page containing all relevant data products associated with the selected Observation that can be loaded into Jdaviz. See [Finding Associated Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113110/Finding+Associated+Data+Products) for more.  
![JDA Dropdown Menu containing both options for the selected observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_jdaviz_new_portal_dropdown.png?version=1&modificationDate=1715203290230&api=v2)JDA Dropdown Menu
**Figure 2 —** The **Jda** dropdown menu, showing options to display the MRP or search for related data products.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Science Instrument (SI) Search for JWST Observations"} -->
After performing a search for JWST observations following the guide in [Science Instrument (SI) Search ](https://outerspace.stsci.edu/display/MASTDOCS/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords), a new icon will appear for search results that can be viewed in Jdaviz (see **Figure 3**). Each row result represents a single JWST data product. Which icon is displayed in each row depends on the type of data product in that row. See [Icon Nomenclature](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-icon_nomenclature) below for the meaning of each icon. Note, this interface is **only** available for JWST observations, and not other MAST products.
![An example SI Keyword Search with the Jdaviz icon displayed next to each observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_portal_jdaviz_si_search.png?version=1&modificationDate=1715203290235&api=v2)SI Keyword Search  
**Figure 3 —** An example SI Keyword search of the MIRI instrument. Search results highlight the right-most Jdaviz icons, displaying the icon most relevant for opening the data product. For example, row 34 displays the Cubeviz icon for opening the s3d IFU FITS file, while row 35 displays the Specviz icon for opening the related 1d extracted spectrum FITS file.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Icon Nomenclature"} -->
These icons represent the Jdaviz application and its different configurations or sub-applications. When performing a Portal or Science Instrument search – as shown above – a relevant icon will be displayed when possible, depending on the data type.
Icon | Name | Description | Data Products | Product Suffixes
---|---|---|---|---
![General Jdaviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/jdaviz_visualize.png?version=1&modificationDate=1715203290200&api=v2)General Jdaviz icon |  | A general icon indicating you can visualize data in Jdaviz | N/A | N/A
![Cubeviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/cubeviz_icon.png?version=1&modificationDate=1715203290242&api=v2)Cubeviz icon |  | The icon for the Cubeviz configuration of Jdaviz | IFU spectral cubes | s3d
![Specviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/specviz_icon.png?version=1&modificationDate=1715203290270&api=v2)Specviz icon |  | The icon for the Specviz configuration of Jdaviz | 1d extracted spectra | x1d, c1d
![Mosviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/mosviz_icon.png?version=1&modificationDate=1715203290286&api=v2)Mosviz icon |  | The icon for the Mosviz configuration of Jdaviz | multi-object spectra | x1d, c1d, s2d, x1dints
![Specviz2d icon](https://outerspace.stsci.edu/download/thumbnails/150113061/speciz2d%20icon.png?version=1&modificationDate=1715203290310&api=v2)Specviz2d icon |  | The icon for the Specviz2d configuration of Jdaviz | 2d and 1d associated extracted spectra | s2d, x1d
![Imviz icon](https://outerspace.stsci.edu/download/thumbnails/150113061/imviz%20icon.png?version=1&modificationDate=1715203290319&api=v2)Imviz icon |  | The icon for the Imviz configuration of Jdaviz | Image data | i2
![](https://outerspace.stsci.edu/download/thumbnails/150113061/lcviz_icon.png?version=1&modificationDate=1742314284655&api=v2)lcviz icon |  | The icon for Lcviz, a child application of Jdaviz | time-series data | lc, slc, llc

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Loading Known Data by URI"} -->
Rather than performing a search, if you already know the URI (for MAST products, the "dataURL") of the data product, you can visit the page directly.
The direct URL for the Jdaviz quicklook page is **<https://mast.stsci.edu/viz/ui/>**. It requires one of two query arguments to successfully load a spectrum, either the **uri** or **filename** query argument. Inputting this into the search bar will navigate you to the appropriate page. **Figure 4** shows an example of a spectrum loaded into the specviz module.  
![](https://outerspace.stsci.edu/download/attachments/150113061/image2022-7-7_17-3-44.png?version=1&modificationDate=1715203290326&api=v2)
**Figure 4 —** An example of you might see when using the search bar to load data. This dataset will be opened in Specviz, since it is a **.x1d** file.  
Alternatively, you can navigate to your page directly using the syntax "`**https://mast.stsci.edu/viz/ui/#/spectra?uri=[MAST_DATA_URI]**`". For example, you might navigate directly to`https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits[](https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits)`.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [Portal Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching)
* [Browsing Portal Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

