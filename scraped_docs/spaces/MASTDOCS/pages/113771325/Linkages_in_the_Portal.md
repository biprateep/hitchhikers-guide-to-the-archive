---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal"
date_accessed: "2026-03-11T11:36:37.152386"
---

<!-- CHUNK 1 START -->
This article illustrates how various related JWST products are represented as an Observation. in the Portal.
**On this page...**
* 1[Associations and Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal#LinkagesinthePortal-AssociationsandLinkagesinthePortal)
* 1.1[What if L-3 Products are Absent?](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal#LinkagesinthePortal-WhatifL-3ProductsareAbsent?)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal#LinkagesinthePortal-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Associations and Linkages in the Portal"} -->
The relationships between various categories of JWST data products are illustrated schematically in Figs. 1 and 2, including the way linked data products appear in the MAST Portal [**Download Manager**](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket). The comprehensive but abridged view in Fig. 1 represents a single JWST science Observation for the common case where **Level-3 (L-3) products are produced** for a single instrument. (See _**Minimum Recommended Products**_ (MRP) filter is applied.  
ObservationCAL Reference**Associated
** All other product levels (L-1b to L-2b)Engineering DatabaseThumbnails, External pre-image, etc.Guide-Star**Linked
****Minimum Recommended Products (L-3)**![](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) CAOM_Portal | ![Portal Download Manager showing Minimum Recommended Products](https://outerspace.stsci.edu/download/attachments/113771325/DLM_MRP2.png?version=1&modificationDate=1629833015622&api=v2)
---|---
**Figure 1 —**  _Left:_ Symbolic relationships of data products from a single JWST Observation, which is composed of (composition denoted with _black diamond_) associated and linked products. The Level-3 products are themselves composed of lower-level products. Some ancillary products such as previews and external pre-images (_gold box_) are linked by MAST but are not formally associated. Static calibration reference files (_blue box_) and contemporaneous engineering data (_purple box_) are neither linked nor associated to the Observation, but can be accessed separately. _Right_ : Level-3 data product(s) are the only ones displayed in the Portal [Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) file tree if the MRP checkbox is ticked.
It is important to understand that all data products for an **Observation** are accessible in the Portal; the visibility of a particular product in the Portal [Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) depends upon what filtering is applied. The relationships between associated data products (see _green box_ in Fig. 1), where guide-star products have been de-selected for clarity, is shown in greater detail in Figure 2. The multiplicity of boxes at each level is intended to represent the various ways many exposures might originate for a given instrument configuration and operating mode: multiple detectors in an instrument, multiple dither positions, different orientations for coronography, etc.  
Contemp. CAL**MRP****Associated Science Products** L-1bL-1bL-1bL-1bL-2aL-2aL-2aL-2aL-2bL-2bL-2bL-2bS1S1S1L-3**S3** L-3L-3S2S2S2S2S1![](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) CAOM_Portal_detail | ![Portal Download Manager Filters panel and File Navigation Tree, showing Science and Info products](https://outerspace.stsci.edu/download/attachments/113771325/DLM_All.png?version=1&modificationDate=1629749501183&api=v2)
---|---
**Figure 2 —** _Left_ : Representation of JWST associated products for a single target or field. Associated _exposure-based_ science products (_green boxes_) are processed in parallel by early stages of the calibration pipeline (Stage-1 or Stage-2). Products are then combined by the Stage-3 pipeline to create the L-3 products. Calibration processing sometimes includes the processing and application of contemporaneous calibration exposures (e.g., arc-lamps; _yellow box_). _Right_ : All products are represented in the Download Manager file tree when the MRP box is _**not**_ checked, showing all levels of calibration processing: in this case for 3 dither positions.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Associations and Linkages in the Portal", "Header 2": "What if L-3 Products are Absent?"} -->
There are some cases where L-3 products will not be present in MAST for a given Observation, including:
* Certain calibration programs (e.g., darks)
* Certain engineering programs
* Science programs where not all intended exposures have been executed on the spacecraft
* Failed observations within a planned sequence, where repeat visits or exposures have yet to be (or will never be) executed  
In these cases, the Observations will correspond to the highest level data product, and be listed separately in the Portal search results. Their representation will be similar to that in Fig. 2, except that no L-3 products will be present.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Data Product Linkages](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages)
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products "Science Data Products")
* [Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products "Supplemental Products")
* [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats "Data Product File Formats")
* [Data Product Linkages](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages "Data Product Linkages")
* [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal "Linkages in the Portal")
* [Keyword Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771333/Keyword+Metadata "Keyword Metadata")
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data "Engineering Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Duplication Checking for Proposals](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/261164035/Duplication+Checking+for+Proposals "Duplication Checking for Proposals")
* [Special Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771441/Special+Topics "Special Topics")
* [JWST Commissioning Data Highlights](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights "JWST Commissioning Data Highlights")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
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
* [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal "Linkages in the Portal")
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
This article illustrates how various related JWST products are represented as an Observation. in the Portal.
**On this page...**
* 1[Associations and Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal#LinkagesinthePortal-AssociationsandLinkagesinthePortal)
* 1.1[What if L-3 Products are Absent?](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal#LinkagesinthePortal-WhatifL-3ProductsareAbsent?)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal#LinkagesinthePortal-ForFurtherReading...)

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Associations and Linkages in the Portal"} -->
The relationships between various categories of JWST data products are illustrated schematically in Figs. 1 and 2, including the way linked data products appear in the MAST Portal [**Download Manager**](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket). The comprehensive but abridged view in Fig. 1 represents a single JWST science Observation for the common case where **Level-3 (L-3) products are produced** for a single instrument. (See _**Minimum Recommended Products**_ (MRP) filter is applied.  
ObservationCAL Reference**Associated
** All other product levels (L-1b to L-2b)Engineering DatabaseThumbnails, External pre-image, etc.Guide-Star**Linked
****Minimum Recommended Products (L-3)**![](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) CAOM_Portal | ![Portal Download Manager showing Minimum Recommended Products](https://outerspace.stsci.edu/download/attachments/113771325/DLM_MRP2.png?version=1&modificationDate=1629833015622&api=v2)
---|---
**Figure 1 —**  _Left:_ Symbolic relationships of data products from a single JWST Observation, which is composed of (composition denoted with _black diamond_) associated and linked products. The Level-3 products are themselves composed of lower-level products. Some ancillary products such as previews and external pre-images (_gold box_) are linked by MAST but are not formally associated. Static calibration reference files (_blue box_) and contemporaneous engineering data (_purple box_) are neither linked nor associated to the Observation, but can be accessed separately. _Right_ : Level-3 data product(s) are the only ones displayed in the Portal [Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) file tree if the MRP checkbox is ticked.
It is important to understand that all data products for an **Observation** are accessible in the Portal; the visibility of a particular product in the Portal [Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) depends upon what filtering is applied. The relationships between associated data products (see _green box_ in Fig. 1), where guide-star products have been de-selected for clarity, is shown in greater detail in Figure 2. The multiplicity of boxes at each level is intended to represent the various ways many exposures might originate for a given instrument configuration and operating mode: multiple detectors in an instrument, multiple dither positions, different orientations for coronography, etc.  
Contemp. CAL**MRP****Associated Science Products** L-1bL-1bL-1bL-1bL-2aL-2aL-2aL-2aL-2bL-2bL-2bL-2bS1S1S1L-3**S3** L-3L-3S2S2S2S2S1![](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) CAOM_Portal_detail | ![Portal Download Manager Filters panel and File Navigation Tree, showing Science and Info products](https://outerspace.stsci.edu/download/attachments/113771325/DLM_All.png?version=1&modificationDate=1629749501183&api=v2)
---|---
**Figure 2 —** _Left_ : Representation of JWST associated products for a single target or field. Associated _exposure-based_ science products (_green boxes_) are processed in parallel by early stages of the calibration pipeline (Stage-1 or Stage-2). Products are then combined by the Stage-3 pipeline to create the L-3 products. Calibration processing sometimes includes the processing and application of contemporaneous calibration exposures (e.g., arc-lamps; _yellow box_). _Right_ : All products are represented in the Download Manager file tree when the MRP box is _**not**_ checked, showing all levels of calibration processing: in this case for 3 dither positions.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Associations and Linkages in the Portal", "Header 2": "What if L-3 Products are Absent?"} -->
There are some cases where L-3 products will not be present in MAST for a given Observation, including:
* Certain calibration programs (e.g., darks)
* Certain engineering programs
* Science programs where not all intended exposures have been executed on the spacecraft
* Failed observations within a planned sequence, where repeat visits or exposures have yet to be (or will never be) executed  
In these cases, the Observations will correspond to the highest level data product, and be listed separately in the Portal search results. Their representation will be similar to that in Fig. 2, except that no L-3 products will be present.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Data Product Linkages](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages)
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 7 END -->

