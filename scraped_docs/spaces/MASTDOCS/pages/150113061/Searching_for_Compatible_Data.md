---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data"
date_accessed: "2026-03-11T21:27:49.660774"
---

**On this page...**
  * 1[Basic Search for Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-BasicSearchforObservations)
  * 2[Science Instrument (SI) Search for JWST Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ScienceInstrument\(SI\)SearchforJWSTObservations)
  * 3[Icon Nomenclature ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-IconNomenclatureicon_nomenclature)
  * 4[Loading Known Data by URI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-LoadingKnownDatabyURI)
  * 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ForFurtherReading...)

# Basic Search for Observations
After you search for MAST observations following the guide in [Basic Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search), the **Jda** icon ![](https://outerspace.stsci.edu/download/thumbnails/150113061/jdaviz_visualize.png?version=1&modificationDate=1715203290200&api=v2)will appear next to relevant search results that you can view in Jdaviz (**see Figure 1**). This icon indicates that the row result contains data products that can be loaded into the Jdaviz web display. For relevant time-series observations, the **Jda** icon will indicate if you can view the results in the Lcviz web display.
![JDA Icon indicating that this data can be analyzed in Jdaviz](https://outerspace.stsci.edu/download/thumbnails/150113061/mast_jdaviz_new_portal_icon_hover.png?version=1&modificationDate=1715203290211&api=v2)JDA Icon indicating that this data can be analyzed in Jdaviz
**Figure 1 —** The **Jda** icon indicating that the current observation (row result) contains spectroscopic science (level 3) data products that can be visualized in the Jdaviz web quicklook. If you don't see this icon, the data cannot be viewed in the web quicklook.
Clicking the **Visualize Spectra (Jda)** icon produces a drop-down menu with two available options, see**Figure 2**.
The available dropdown options are:
  * **Display default Minimum Recommended Product (MRP)** - opens the default [Minimum Recommended Product](https://outerspace.stsci.edu/display/MASTDOCS/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts) for the selected observation in the Jdaviz or Lcviz quicklook spectra page. See [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra) for more.
  * **Search through other data products related to this observation** - opens a new page containing all relevant data products associated with the selected Observation that can be loaded into Jdaviz. See [Finding Associated Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113110/Finding+Associated+Data+Products) for more.

![JDA Dropdown Menu containing both options for the selected observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_jdaviz_new_portal_dropdown.png?version=1&modificationDate=1715203290230&api=v2)JDA Dropdown Menu
**Figure 2 —** The **Jda** dropdown menu, showing options to display the MRP or search for related data products.
# Science Instrument (SI) Search for JWST Observations
After performing a search for JWST observations following the guide in [Science Instrument (SI) Search ](https://outerspace.stsci.edu/display/MASTDOCS/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords), a new icon will appear for search results that can be viewed in Jdaviz (see **Figure 3**). Each row result represents a single JWST data product. Which icon is displayed in each row depends on the type of data product in that row. See [Icon Nomenclature](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-icon_nomenclature) below for the meaning of each icon. Note, this interface is **only** available for JWST observations, and not other MAST products.
![An example SI Keyword Search with the Jdaviz icon displayed next to each observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_portal_jdaviz_si_search.png?version=1&modificationDate=1715203290235&api=v2)SI Keyword Search  

**Figure 3 —** An example SI Keyword search of the MIRI instrument. Search results highlight the right-most Jdaviz icons, displaying the icon most relevant for opening the data product. For example, row 34 displays the Cubeviz icon for opening the s3d IFU FITS file, while row 35 displays the Specviz icon for opening the related 1d extracted spectrum FITS file.
# Icon Nomenclature
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






# Loading Known Data by URI
Rather than performing a search, if you already know the URI (for MAST products, the "dataURL") of the data product, you can visit the page directly.
The direct URL for the Jdaviz quicklook page is **<https://mast.stsci.edu/viz/ui/>**. It requires one of two query arguments to successfully load a spectrum, either the **uri** or **filename** query argument. Inputting this into the search bar will navigate you to the appropriate page. **Figure 4** shows an example of a spectrum loaded into the specviz module.

![](https://outerspace.stsci.edu/download/attachments/150113061/image2022-7-7_17-3-44.png?version=1&modificationDate=1715203290326&api=v2)
**Figure 4 —** An example of you might see when using the search bar to load data. This dataset will be opened in Specviz, since it is a **.x1d** file.


Alternatively, you can navigate to your page directly using the syntax "`**https://mast.stsci.edu/viz/ui/#/spectra?uri=[MAST_DATA_URI]**`". For example, you might navigate directly to`https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits[](https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits)`.


# For Further Reading...
  * [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
  * [Portal Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching)
  * [Browsing Portal Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data)

Unable to load page tree. It seems that you do not have permission to view the root page.
**On this page...**
  * 1[Basic Search for Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-BasicSearchforObservations)
  * 2[Science Instrument (SI) Search for JWST Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ScienceInstrument\(SI\)SearchforJWSTObservations)
  * 3[Icon Nomenclature ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-IconNomenclatureicon_nomenclature)
  * 4[Loading Known Data by URI](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-LoadingKnownDatabyURI)
  * 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-ForFurtherReading...)

# Basic Search for Observations
After you search for MAST observations following the guide in [Basic Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search), the **Jda** icon ![](https://outerspace.stsci.edu/download/thumbnails/150113061/jdaviz_visualize.png?version=1&modificationDate=1715203290200&api=v2)will appear next to relevant search results that you can view in Jdaviz (**see Figure 1**). This icon indicates that the row result contains data products that can be loaded into the Jdaviz web display. For relevant time-series observations, the **Jda** icon will indicate if you can view the results in the Lcviz web display.
![JDA Icon indicating that this data can be analyzed in Jdaviz](https://outerspace.stsci.edu/download/thumbnails/150113061/mast_jdaviz_new_portal_icon_hover.png?version=1&modificationDate=1715203290211&api=v2)JDA Icon indicating that this data can be analyzed in Jdaviz
**Figure 1 —** The **Jda** icon indicating that the current observation (row result) contains spectroscopic science (level 3) data products that can be visualized in the Jdaviz web quicklook. If you don't see this icon, the data cannot be viewed in the web quicklook.
Clicking the **Visualize Spectra (Jda)** icon produces a drop-down menu with two available options, see**Figure 2**.
The available dropdown options are:
  * **Display default Minimum Recommended Product (MRP)** - opens the default [Minimum Recommended Product](https://outerspace.stsci.edu/display/MASTDOCS/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts) for the selected observation in the Jdaviz or Lcviz quicklook spectra page. See [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra) for more.
  * **Search through other data products related to this observation** - opens a new page containing all relevant data products associated with the selected Observation that can be loaded into Jdaviz. See [Finding Associated Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113110/Finding+Associated+Data+Products) for more.

![JDA Dropdown Menu containing both options for the selected observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_jdaviz_new_portal_dropdown.png?version=1&modificationDate=1715203290230&api=v2)JDA Dropdown Menu
**Figure 2 —** The **Jda** dropdown menu, showing options to display the MRP or search for related data products.
# Science Instrument (SI) Search for JWST Observations
After performing a search for JWST observations following the guide in [Science Instrument (SI) Search ](https://outerspace.stsci.edu/display/MASTDOCS/Data+Search#DataSearch-SearchbyJWSTInstrumentKeywords), a new icon will appear for search results that can be viewed in Jdaviz (see **Figure 3**). Each row result represents a single JWST data product. Which icon is displayed in each row depends on the type of data product in that row. See [Icon Nomenclature](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-icon_nomenclature) below for the meaning of each icon. Note, this interface is **only** available for JWST observations, and not other MAST products.
![An example SI Keyword Search with the Jdaviz icon displayed next to each observation](https://outerspace.stsci.edu/download/attachments/150113061/mast_portal_jdaviz_si_search.png?version=1&modificationDate=1715203290235&api=v2)SI Keyword Search  

**Figure 3 —** An example SI Keyword search of the MIRI instrument. Search results highlight the right-most Jdaviz icons, displaying the icon most relevant for opening the data product. For example, row 34 displays the Cubeviz icon for opening the s3d IFU FITS file, while row 35 displays the Specviz icon for opening the related 1d extracted spectrum FITS file.
# Icon Nomenclature
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






# Loading Known Data by URI
Rather than performing a search, if you already know the URI (for MAST products, the "dataURL") of the data product, you can visit the page directly.
The direct URL for the Jdaviz quicklook page is **<https://mast.stsci.edu/viz/ui/>**. It requires one of two query arguments to successfully load a spectrum, either the **uri** or **filename** query argument. Inputting this into the search bar will navigate you to the appropriate page. **Figure 4** shows an example of a spectrum loaded into the specviz module.

![](https://outerspace.stsci.edu/download/attachments/150113061/image2022-7-7_17-3-44.png?version=1&modificationDate=1715203290326&api=v2)
**Figure 4 —** An example of you might see when using the search bar to load data. This dataset will be opened in Specviz, since it is a **.x1d** file.


Alternatively, you can navigate to your page directly using the syntax "`**https://mast.stsci.edu/viz/ui/#/spectra?uri=[MAST_DATA_URI]**`". For example, you might navigate directly to`https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits[](https://mast.stsci.edu/viz/ui/#/spectra?uri=mast:JWST/product/jw01409-o133_t011_nirspec_prism-clear_x1d.fits)`.


# For Further Reading...
  * [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
  * [Portal Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching)
  * [Browsing Portal Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data)

[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:
