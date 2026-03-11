---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra"
date_accessed: "2026-03-11T21:27:56.680226"
---

This article describes the various Jdaviz configurations to view different types of spectra. For an explanation on navigating to the Jdaviz analysis tool, visit the page [searching for Jdaviz-compatible data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data).
**On this page...**
  * 1[Jdaviz Display Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-JdavizDisplayPanel)
    * 1.1[Specviz](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Specviz)
    * 1.2[Specviz2D ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Specviz2D)
    * 1.3[Cubeviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Cubeviz)
    * 1.4[Imviz](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Imviz)
    * 1.5[Lcviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Lcviz)
  * 2[Coming soon to the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-ComingsoontotheMASTPortal)
    * 2.1[Mosviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Mosviz)
  * 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-ForFurtherReading...)

# Jdaviz Display Panel
The main display panel contains the Jdaviz python application. Jdaviz has multiple configurations designed to load and view different types of spectroscopic datasets. Which configuration is displayed in the MAST spectral quicklook page depends on the type of data product. See the [Icon Nomenclature](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-icon_nomenclature) for quick reference guide to the different Jdaviz configurations. Jdaviz is designed to work generally with data products from many MAST missions. For JWST specifically, see the table .  Below, we briefly summarize the currently supported Jdaviz configurations available in MAST. For further details, see the  homepage.
Each Jdaviz configuration is built from one or more viewers, displaying either a 2d image, a 2d spectrum, or 1d spectrum profile. Each viewer is fully interactive, enabling pan/zoom, subset region selection, image scaling, colormaps, and more. Each configuration also comes equipped with a series of analysis plugins for on-the-fly analysis. Lcviz is a separate application, built on top of Jdaviz, and lightkurve, to display time-series lightcurve data from TESS, Kepler, and K2.
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/specviz_icon.png?version=1&modificationDate=1715254505637&api=v2)
The primary configuration for 1d spectroscopic data sets. For JWST these data have **x1d****and c1d** product suffixes. By default, Specviz consists a single 1d spectrum profile viewer (see **Figure 1**). See
![Specviz Configuration showing a sample spectrum](https://outerspace.stsci.edu/download/attachments/150113084/mast_jdaviz_specviz.png?version=1&modificationDate=1715254505652&api=v2)
**Figure 1 —** The Jdaviz Specviz configuration, designed to load any 1d spectroscopic data product. By default, it consists of a single 1d spectrum profile viewer.
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/speciz2d%20icon.png?version=1&modificationDate=1715254505629&api=v2)
The **s2d** product types, associated with the NIRSpec instrument. By default, Specviz2D consists of a 2d spectrum viewer, and a 1d spectrum profile viewer, that are linked together (see Figure 2). See
Specviz2D is meant to display a related 2d and 1d spectroscopic data product for a given target, and thus can accept two data product files as input: a 2d spectrum file, and a 1d spectrum file. When only a single 2d spectrum file is provided, Specviz2D will load the 2d spectrum file into the top 2d viewer, and perform a simple 1d spectral extraction from the 2d file to load into the bottom 1d spectrum profile viewer.  This is the default mode in MAST. If you need to load related 2d and 1d spectrum files, download the files locally and load into Specviz2D via Jupyter Lab.
![Specviz2D Configuration. This is identical to the upper right portion of the Mosviz configuration.](https://outerspace.stsci.edu/download/attachments/150113084/mast_jdaviz_specviz2d.png?version=1&modificationDate=1715254505648&api=v2)
**Figure 2 —** The Jdaviz Specviz2D configuration, designed to display any related 2d and 1d spectroscopic data. By default, it consists of a single 2d spectrum viewer (_top_), and 1d spectrum profile viewer (_bottom_).
## ![](https://outerspace.stsci.edu/download/attachments/150113084/cubeviz_icon.png?version=1&modificationDate=1715254505643&api=v2)
The primary configuration for 3d spectroscopic data sets, e.g. IFU spectral data cubes. For JWST these data have **s3d** product types. By default, Cubeviz consists of two image viewers, containing the flux and uncertainty, and a single 1d spectrum profile viewer (see **Figure 3**). By default, the spectrum viewer is populated by collapsing the spatial axes via a "Sum" into a single spectrum. See
![](https://outerspace.stsci.edu/download/attachments/150113084/jdaviz_cubeviz_new.png?version=1&modificationDate=1742320106596&api=v2)
**Figure 3 —** The Jdaviz Cubeviz configuration, designed to load 3d spectroscopic data such as IFU spectral datacubes. By default, Cubeviz consists of two image viewers, containing the flux (_top left_) and uncertainty (_top right_), and a single 1d spectrum profile viewer (_bottom_)
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/imviz%20icon.png?version=1&modificationDate=1715254505441&api=v2)
Imviz is a generalized image viewer for astronomical data (see **Figure 4**). It accepts the the **i2d** When using Imviz programmatically, you can input a **fits** file, an  object, or a 2D NumPy array.
![](https://outerspace.stsci.edu/download/attachments/150113084/jdaviz_mast_imviz.png?version=1&modificationDate=1715254505383&api=v2)
**Figure 4 —** The Jdaviz Imviz configuration, designed to display images. By default the image takes up the entire viewer and is fully zoomed. It supports the ability to pan and zoom the image, display pixel and world coordinates, and perform simple aperture photometry on sources.
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/lcviz_icon.png?version=1&modificationDate=1742320519668&api=v2)
Lcviz is a light curve visualization and analysis tool, built on top of Jdaviz, for displaying time-series data (see **Figure 5**). It primarily supports TESS, Kepler, and K2 **lc, slc, and llc** data products. See
![](https://outerspace.stsci.edu/download/attachments/150113084/jdaviz_lcviz.png?version=1&modificationDate=1742320797574&api=v2)
**Figure 5** - The Lcviz application, designed to display time-series lightcurve data from TESS, Kepler, and K2.
# Coming soon to the MAST Portal
Not all Jdaviz features are available in the MAST Portal, as they are still being integrated by our software teams. For full functionality, you can always use [Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks) or the [standalone application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application).
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/mosviz_icon.png?version=1&modificationDate=1715254505401&api=v2)
The Mosviz configuration is used for multi-object spectroscopy (MOS; see Figure 6). It is was designed to work with the the JWST NIRCam imager and the NIRSpec [microshutter assembly](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-instrumentation/nirspec-micro-shutter-assembly). As such, Mosviz has some features that are specific to NIRSpec and NIRCam data. However, it will work with data from any telescope or instrument.
![Mosviz configuration listing 10 different spectra. The first spectra is shown in both 2D and 1D, along with the flux](https://outerspace.stsci.edu/download/attachments/150113084/Screen%20Shot%202022-06-08%20at%2013.04.01.png?version=1&modificationDate=1715254505468&api=v2)
**Figure 6 —** The Jdaviz Mosviz configuration, designed to display many spectra at once. The default windows are the viewer (_top left_), a 2D spectrum viewer over a Specviz viewer (_top right_**),** and the _bottom_).
# For Further Reading...
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
  * [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
  * [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)

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
    * [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching "Searching")
    * [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data "Browsing Data")
    * [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
    * [Tips and Notes](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963055/Tips+and+Notes "Tips and Notes")
    * [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials "Demos and Tutorials")
  * [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
    * [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
    * [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
    * [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
    * [Duplication Checking for Proposals](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals "Duplication Checking for Proposals")
    * [Special Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771441/Special+Topics "Special Topics")
    * [JWST Commissioning Data Highlights](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights "JWST Commissioning Data Highlights")
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
  * [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
  * [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
  * [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
  * [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
  * [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
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
  * [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
  * [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
  * [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")

This article describes the various Jdaviz configurations to view different types of spectra. For an explanation on navigating to the Jdaviz analysis tool, visit the page [searching for Jdaviz-compatible data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data).
**On this page...**
  * 1[Jdaviz Display Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-JdavizDisplayPanel)
    * 1.1[Specviz](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Specviz)
    * 1.2[Specviz2D ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Specviz2D)
    * 1.3[Cubeviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Cubeviz)
    * 1.4[Imviz](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Imviz)
    * 1.5[Lcviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Lcviz)
  * 2[Coming soon to the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-ComingsoontotheMASTPortal)
    * 2.1[Mosviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-Mosviz)
  * 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra#ViewingSpectra-ForFurtherReading...)

# Jdaviz Display Panel
The main display panel contains the Jdaviz python application. Jdaviz has multiple configurations designed to load and view different types of spectroscopic datasets. Which configuration is displayed in the MAST spectral quicklook page depends on the type of data product. See the [Icon Nomenclature](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113061/Searching+for+Compatible+Data#SearchingforCompatibleData-icon_nomenclature) for quick reference guide to the different Jdaviz configurations. Jdaviz is designed to work generally with data products from many MAST missions. For JWST specifically, see the table .  Below, we briefly summarize the currently supported Jdaviz configurations available in MAST. For further details, see the  homepage.
Each Jdaviz configuration is built from one or more viewers, displaying either a 2d image, a 2d spectrum, or 1d spectrum profile. Each viewer is fully interactive, enabling pan/zoom, subset region selection, image scaling, colormaps, and more. Each configuration also comes equipped with a series of analysis plugins for on-the-fly analysis. Lcviz is a separate application, built on top of Jdaviz, and lightkurve, to display time-series lightcurve data from TESS, Kepler, and K2.
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/specviz_icon.png?version=1&modificationDate=1715254505637&api=v2)
The primary configuration for 1d spectroscopic data sets. For JWST these data have **x1d****and c1d** product suffixes. By default, Specviz consists a single 1d spectrum profile viewer (see **Figure 1**). See
![Specviz Configuration showing a sample spectrum](https://outerspace.stsci.edu/download/attachments/150113084/mast_jdaviz_specviz.png?version=1&modificationDate=1715254505652&api=v2)
**Figure 1 —** The Jdaviz Specviz configuration, designed to load any 1d spectroscopic data product. By default, it consists of a single 1d spectrum profile viewer.
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/speciz2d%20icon.png?version=1&modificationDate=1715254505629&api=v2)
The **s2d** product types, associated with the NIRSpec instrument. By default, Specviz2D consists of a 2d spectrum viewer, and a 1d spectrum profile viewer, that are linked together (see Figure 2). See
Specviz2D is meant to display a related 2d and 1d spectroscopic data product for a given target, and thus can accept two data product files as input: a 2d spectrum file, and a 1d spectrum file. When only a single 2d spectrum file is provided, Specviz2D will load the 2d spectrum file into the top 2d viewer, and perform a simple 1d spectral extraction from the 2d file to load into the bottom 1d spectrum profile viewer.  This is the default mode in MAST. If you need to load related 2d and 1d spectrum files, download the files locally and load into Specviz2D via Jupyter Lab.
![Specviz2D Configuration. This is identical to the upper right portion of the Mosviz configuration.](https://outerspace.stsci.edu/download/attachments/150113084/mast_jdaviz_specviz2d.png?version=1&modificationDate=1715254505648&api=v2)
**Figure 2 —** The Jdaviz Specviz2D configuration, designed to display any related 2d and 1d spectroscopic data. By default, it consists of a single 2d spectrum viewer (_top_), and 1d spectrum profile viewer (_bottom_).
## ![](https://outerspace.stsci.edu/download/attachments/150113084/cubeviz_icon.png?version=1&modificationDate=1715254505643&api=v2)
The primary configuration for 3d spectroscopic data sets, e.g. IFU spectral data cubes. For JWST these data have **s3d** product types. By default, Cubeviz consists of two image viewers, containing the flux and uncertainty, and a single 1d spectrum profile viewer (see **Figure 3**). By default, the spectrum viewer is populated by collapsing the spatial axes via a "Sum" into a single spectrum. See
![](https://outerspace.stsci.edu/download/attachments/150113084/jdaviz_cubeviz_new.png?version=1&modificationDate=1742320106596&api=v2)
**Figure 3 —** The Jdaviz Cubeviz configuration, designed to load 3d spectroscopic data such as IFU spectral datacubes. By default, Cubeviz consists of two image viewers, containing the flux (_top left_) and uncertainty (_top right_), and a single 1d spectrum profile viewer (_bottom_)
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/imviz%20icon.png?version=1&modificationDate=1715254505441&api=v2)
Imviz is a generalized image viewer for astronomical data (see **Figure 4**). It accepts the the **i2d** When using Imviz programmatically, you can input a **fits** file, an  object, or a 2D NumPy array.
![](https://outerspace.stsci.edu/download/attachments/150113084/jdaviz_mast_imviz.png?version=1&modificationDate=1715254505383&api=v2)
**Figure 4 —** The Jdaviz Imviz configuration, designed to display images. By default the image takes up the entire viewer and is fully zoomed. It supports the ability to pan and zoom the image, display pixel and world coordinates, and perform simple aperture photometry on sources.
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/lcviz_icon.png?version=1&modificationDate=1742320519668&api=v2)
Lcviz is a light curve visualization and analysis tool, built on top of Jdaviz, for displaying time-series data (see **Figure 5**). It primarily supports TESS, Kepler, and K2 **lc, slc, and llc** data products. See
![](https://outerspace.stsci.edu/download/attachments/150113084/jdaviz_lcviz.png?version=1&modificationDate=1742320797574&api=v2)
**Figure 5** - The Lcviz application, designed to display time-series lightcurve data from TESS, Kepler, and K2.
# Coming soon to the MAST Portal
Not all Jdaviz features are available in the MAST Portal, as they are still being integrated by our software teams. For full functionality, you can always use [Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks) or the [standalone application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application).
## ![](https://outerspace.stsci.edu/download/thumbnails/150113084/mosviz_icon.png?version=1&modificationDate=1715254505401&api=v2)
The Mosviz configuration is used for multi-object spectroscopy (MOS; see Figure 6). It is was designed to work with the the JWST NIRCam imager and the NIRSpec [microshutter assembly](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-instrumentation/nirspec-micro-shutter-assembly). As such, Mosviz has some features that are specific to NIRSpec and NIRCam data. However, it will work with data from any telescope or instrument.
![Mosviz configuration listing 10 different spectra. The first spectra is shown in both 2D and 1D, along with the flux](https://outerspace.stsci.edu/download/attachments/150113084/Screen%20Shot%202022-06-08%20at%2013.04.01.png?version=1&modificationDate=1715254505468&api=v2)
**Figure 6 —** The Jdaviz Mosviz configuration, designed to display many spectra at once. The default windows are the viewer (_top left_), a 2D spectrum viewer over a Specviz viewer (_top right_**),** and the _bottom_).
# For Further Reading...
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:
