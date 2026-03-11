---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide"
date_accessed: "2026-03-11T21:27:52.400565"
---

This page describes the Jdaviz interface as it appears in a web browser.
**On this page...**
  * 1[Elements of the Jdaviz Graphic Interface](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-ElementsoftheJdavizGraphicInterface)
    * 1.1[Navigation Bar ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-NavigationBarnav_bar)
    * 1.2[Sidebar Information Panel ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-SidebarInformationPanelside_bar)
    * 1.3[Jdaviz Application Display Panel ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-JdavizApplicationDisplayPanelapp_display)
    * 1.4[Data Access Dropdown Menu ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-DataAccessDropdownMenuaccess_dropdown)
  * 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-ForFurtherReading...)

# Elements of the Jdaviz Graphic Interface
The main display for [Jdaviz spectroscopic quicklook](https://mast.stsci.edu/viz/ui/) and analysis is shown in **Figure 1**. This page helps you easily look at spectroscopic datasets and perform quick analysis, using the **Docs** button links to the **API** button links to relevant[ API documentation](https://masttest.stsci.edu/viz/docs/index.html) describing a variety of programmatic endpoints the user can use.


![Primary Jdaviz page showcasing its four main sections](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_spectra_new_annotated.png?version=1&modificationDate=1657650343152&api=v2)Primary Jdaviz page
**Figure 1 —** The primary page for Jdaviz Spectroscopic Quicklook in MAST, consisting of four main sections: The [Navigation Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-nav_bar) (1: _top_), [Sidebar Information Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-side_bar) (2: _left_), [Jdaviz application display panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-app_display) (3: _center right_), and [Data Access Dropdown Menu](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-access_dropdown) (4: _top right_).
## Navigation Bar
The data product URI is in the top navigation bar (see Figure 2). You can input either the full URI, or just the filename, and click "Search" to navigate to the desired file.
![Navigation Bar](https://outerspace.stsci.edu/download/attachments/150113072/searchbar.png?version=1&modificationDate=1657650343022&api=v2)Navigation Bar
**Figure 2 —** The Navigation Bar. Used to identify the current file, and search for others.
## Sidebar Information Panel
A panel is displayed on the left-hand side of the page consisting of (up to) three collapsible groups of information and parameters related to the currently viewed data product (**Figure 3**).
  * **Basic Info** - Basic information about the target, the instrument that collected the data, and how the data is stored.
  * **Observation Parameters** - Metadata parameters that are specific to the observation, such as: the principal investigator, proposal ID, and proposal title.
  * **Instrument Keywords** - Science instrument (SI) keywords from the data product FITS header. **For JWST observations only.**

Each panel contains a list of parameters, with relevant ones sub-grouped into descriptive categories. Each parameter row displays a human-readable name, a database or API parameter name, the value of the parameter for the displayed target, and the unit, if any, of the parameter.
![Basic info group - showing the target, instrument, and observation info sub-panels](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_basic_new.png?version=1&modificationDate=1657650343134&api=v2)Basic info | ![Observation Parameters group - showing the Proposal, Observation, Target, Product, Instrument, Access, and Internal info sub-panels](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_obsparams_new.png?version=1&modificationDate=1657650343120&api=v2)Observation Parameters | ![Instrument keywords group - showing the standard, basic, and IFC Parameter sub-panels, along with the Programmatic, Visit, and Target information sub-panels. The sub-panels are cut off at the bottom of the image due to their number](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_inskeys_new.png?version=1&modificationDate=1657650343105&api=v2)Instrument Keywords
---|---|---
**Figure 3 —** Sidebar Information Panel. Left: Basic information about the target of observation. Middle: Parameters related to the observation that produced the data product. Right: For JWST observations, Science Instrument (SI) keywords related to the data product, from the FITS headers.
Hovering over each section, sub-category or parameter item produces a tool-tip with a description of the displayed content (Figure 4).
![Sidebar Information Panel - The hover-text displays information about the  'observation parameters' group](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_obshover.png?version=1&modificationDate=1657650343091&api=v2)Sidebar information panel | ![Sidebar Information Panel - The hover-text displays information about the  'instrument' category, under the 'instrument info' group](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_hover_desc.png?version=1&modificationDate=1657650343075&api=v2)Sidebar information panel
---|---
**Figure 4 —** Sidebar Information Panel. Hovering over section, group or parameter names displays descriptions for the given content.
If you want to collapse the sidebar panel and expand the Jdaviz content window to fill the screen, click the ![](https://outerspace.stsci.edu/download/thumbnails/150113072/image2022-7-8_10-47-37.png?version=1&modificationDate=1657650342927&api=v2) icon at immediately above the sidebar panel. Clicking again will re-expand the sidebar panel.
## Jdaviz Application Display Panel
This is the main window for interacting with the data. Exactly what is visible depends on the type of data being visualized; for more information on all of the features available, please see [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra).
![Example JWST Spectra](https://outerspace.stsci.edu/download/attachments/150113072/Screen%20Shot%202022-06-07%20at%2010.56.57.png?version=1&modificationDate=1657650343008&api=v2)
**Figure 5 —** An example set of JWST data. Depending on your data selection, you may not see the same analysis elements.
## Data Access Dropdown Menu


While viewing data in MAST Jdaviz, you can seamlessly transition to using Jdaviz within a Jupyter notebook in your local environment for deeper analysis. The dropdown menu offers one option: Jupyter (see **Figure 6**). More details about analyzing data in Jupyter, see [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks).


![Dropdown menu that gives the option to open the spectrum in a Jupyter Notebook](https://outerspace.stsci.edu/download/thumbnails/150113072/mast_jdaviz_download_nb.png?version=1&modificationDate=1657650342954&api=v2)
**Figure 6 —** Data Access Dropdown Menu showing the option to open your data in a local Jupyter Notebook.
# For Further Reading...
  * [JWST Jdaviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples)Guided Examples: includes links to guided videos
  * The

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

This page describes the Jdaviz interface as it appears in a web browser.
**On this page...**
  * 1[Elements of the Jdaviz Graphic Interface](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-ElementsoftheJdavizGraphicInterface)
    * 1.1[Navigation Bar ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-NavigationBarnav_bar)
    * 1.2[Sidebar Information Panel ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-SidebarInformationPanelside_bar)
    * 1.3[Jdaviz Application Display Panel ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-JdavizApplicationDisplayPanelapp_display)
    * 1.4[Data Access Dropdown Menu ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-DataAccessDropdownMenuaccess_dropdown)
  * 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-ForFurtherReading...)

# Elements of the Jdaviz Graphic Interface
The main display for [Jdaviz spectroscopic quicklook](https://mast.stsci.edu/viz/ui/) and analysis is shown in **Figure 1**. This page helps you easily look at spectroscopic datasets and perform quick analysis, using the **Docs** button links to the **API** button links to relevant[ API documentation](https://masttest.stsci.edu/viz/docs/index.html) describing a variety of programmatic endpoints the user can use.


![Primary Jdaviz page showcasing its four main sections](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_spectra_new_annotated.png?version=1&modificationDate=1657650343152&api=v2)Primary Jdaviz page
**Figure 1 —** The primary page for Jdaviz Spectroscopic Quicklook in MAST, consisting of four main sections: The [Navigation Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-nav_bar) (1: _top_), [Sidebar Information Panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-side_bar) (2: _left_), [Jdaviz application display panel](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-app_display) (3: _center right_), and [Data Access Dropdown Menu](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113072/Interface+Field+Guide#InterfaceFieldGuide-access_dropdown) (4: _top right_).
## Navigation Bar
The data product URI is in the top navigation bar (see Figure 2). You can input either the full URI, or just the filename, and click "Search" to navigate to the desired file.
![Navigation Bar](https://outerspace.stsci.edu/download/attachments/150113072/searchbar.png?version=1&modificationDate=1657650343022&api=v2)Navigation Bar
**Figure 2 —** The Navigation Bar. Used to identify the current file, and search for others.
## Sidebar Information Panel
A panel is displayed on the left-hand side of the page consisting of (up to) three collapsible groups of information and parameters related to the currently viewed data product (**Figure 3**).
  * **Basic Info** - Basic information about the target, the instrument that collected the data, and how the data is stored.
  * **Observation Parameters** - Metadata parameters that are specific to the observation, such as: the principal investigator, proposal ID, and proposal title.
  * **Instrument Keywords** - Science instrument (SI) keywords from the data product FITS header. **For JWST observations only.**

Each panel contains a list of parameters, with relevant ones sub-grouped into descriptive categories. Each parameter row displays a human-readable name, a database or API parameter name, the value of the parameter for the displayed target, and the unit, if any, of the parameter.
![Basic info group - showing the target, instrument, and observation info sub-panels](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_basic_new.png?version=1&modificationDate=1657650343134&api=v2)Basic info | ![Observation Parameters group - showing the Proposal, Observation, Target, Product, Instrument, Access, and Internal info sub-panels](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_obsparams_new.png?version=1&modificationDate=1657650343120&api=v2)Observation Parameters | ![Instrument keywords group - showing the standard, basic, and IFC Parameter sub-panels, along with the Programmatic, Visit, and Target information sub-panels. The sub-panels are cut off at the bottom of the image due to their number](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_inskeys_new.png?version=1&modificationDate=1657650343105&api=v2)Instrument Keywords
---|---|---
**Figure 3 —** Sidebar Information Panel. Left: Basic information about the target of observation. Middle: Parameters related to the observation that produced the data product. Right: For JWST observations, Science Instrument (SI) keywords related to the data product, from the FITS headers.
Hovering over each section, sub-category or parameter item produces a tool-tip with a description of the displayed content (Figure 4).
![Sidebar Information Panel - The hover-text displays information about the  'observation parameters' group](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_obshover.png?version=1&modificationDate=1657650343091&api=v2)Sidebar information panel | ![Sidebar Information Panel - The hover-text displays information about the  'instrument' category, under the 'instrument info' group](https://outerspace.stsci.edu/download/attachments/150113072/mast_jdaviz_sidebar_hover_desc.png?version=1&modificationDate=1657650343075&api=v2)Sidebar information panel
---|---
**Figure 4 —** Sidebar Information Panel. Hovering over section, group or parameter names displays descriptions for the given content.
If you want to collapse the sidebar panel and expand the Jdaviz content window to fill the screen, click the ![](https://outerspace.stsci.edu/download/thumbnails/150113072/image2022-7-8_10-47-37.png?version=1&modificationDate=1657650342927&api=v2) icon at immediately above the sidebar panel. Clicking again will re-expand the sidebar panel.
## Jdaviz Application Display Panel
This is the main window for interacting with the data. Exactly what is visible depends on the type of data being visualized; for more information on all of the features available, please see [Viewing Spectra and Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113084/Viewing+Spectra).
![Example JWST Spectra](https://outerspace.stsci.edu/download/attachments/150113072/Screen%20Shot%202022-06-07%20at%2010.56.57.png?version=1&modificationDate=1657650343008&api=v2)
**Figure 5 —** An example set of JWST data. Depending on your data selection, you may not see the same analysis elements.
## Data Access Dropdown Menu


While viewing data in MAST Jdaviz, you can seamlessly transition to using Jdaviz within a Jupyter notebook in your local environment for deeper analysis. The dropdown menu offers one option: Jupyter (see **Figure 6**). More details about analyzing data in Jupyter, see [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks).


![Dropdown menu that gives the option to open the spectrum in a Jupyter Notebook](https://outerspace.stsci.edu/download/thumbnails/150113072/mast_jdaviz_download_nb.png?version=1&modificationDate=1657650342954&api=v2)
**Figure 6 —** Data Access Dropdown Menu showing the option to open your data in a local Jupyter Notebook.
# For Further Reading...
  * [JWST Jdaviz ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples)Guided Examples: includes links to guided videos
  * The

[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:
