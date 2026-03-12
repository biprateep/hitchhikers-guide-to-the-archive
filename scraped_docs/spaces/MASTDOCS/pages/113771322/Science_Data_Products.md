---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products"
date_accessed: "2026-03-11T11:33:11.644112"
---

<!-- CHUNK 1 START -->
Learning which of the many JWST data products are appropriate for science analysis requires a basic understanding of how the data are processed, the file naming scheme, and the format and semantic content of the science-ready products.
**On this page...**
* 1[Science Data Processing](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-ScienceDataProcessing)
* 1.1[Level vs Stage](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-Level_StageLevelvsStage)
* 2[File Naming Scheme](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-FileNamingScheme)
* 2.1[Exposure- vs. Target/Source-based File Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-Exposure-vs.Target/Source-basedFileNames)
* 2.2[File Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-FileContents)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Science Data Processing"} -->
A key point to understand is that, with _every_ JWST Observation (e.g., a row in the Portal results table), _all_ science and associated data products are bundled with it. These products include:
* All calibration levels of science data processing (see the summary in the [Level vs Stage](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) subsection below)
* Various [supplemental products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products)  
In all, the set of files per Observation could number in the hundreds or even thousands. Exactly which calibrated products are generated depends upon the configuration of the instrument that obtained the data (imaging, various forms of spectroscopy, coronagraphy), and the operating mode (time-series, dithered, moving target, etc.). See the detailed description of
The other products are useful either for evaluating the quality of the data processing, or to provide inputs in case you wish to re-process data with some or all stages of the
When searching for products in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html), those identified in the MAST [Portal Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) as [Minimum Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products) (MRP) are a good approximation to the most relevant for science analysis. These files usually number less than a dozen, except for multi-object spectroscopy where there is one highest-level, combined, extracted product per spectrum (i.e., potentially hundreds of spectra).
You will encounter slightly different labels to denote Science products, depending upon the document collection you are reading.
* **JDox:** The JWST mission document collection focuses on the pipeline processing __**stages**__ that are used to produce different products. See [Stages of Processing](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview) for details.
* **Processing (DMS):** The _**data management system**_ (which processes all JWST science data) focuses on the __**Level**__ of data product that is being produced; for products visible to users this starts with L-1b and ends with L-3. For comparison, the Stage 0 pipeline takes DMS L-1b products and produces L-2a products, which themselves comprise the input for the Stage-1 pipeline, and so on.
* **Archive (MAST):** The MAST Common Archive Observation Model (CAOM) database labels products by a generic calibration level that applies to many instruments and telescopes, whether ground- or space-based. It does not currently distinguish between DMS L-2a (slope corrected) and L-2b (instrument signature removed, calibrated to physical units).  
The following table summarizes the products and the translation between the vocabularies. You may also find helpful the diagrams in the [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) article.
Description | JDox Data Stage | DMS Processing Level | MAST/CAOM Calibration Level
---|---|---|---
Planned/approved but not yet executed observations | N/A | N/A | –1
Uncalibrated FITS files with all header keywords populated, per detector/exposure | Stage 0 | L–1b | 1
Slope-corrected FITS files (up-the-ramp slope removed), per detector | Stage 1 | L–2a | 2
FITS files, per detector and exposure, where instrument signature has been removed and the data have been astrometrically and radiometrically calibrated | Stage 2 |  L–2b (also L-2bs, L-2c, L-2cs) | 2
Combined, calibrated science product per target or source | Stage 3 | L–3 | 3
Contributed Science Products | N/A | N/A* | 4
*DMS does produce L-4 products for HST, but presently no such products are defined or produced for JWST.
**The target/source-based combined products (L-3), and the fully calibrated exposure-based images** from which they were derived (L-2b), are the most likely to be relevant for your science analysis.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "File Naming Scheme"} -->
The file name convention for JWST data products was designed in large part to facilitate automated processing of data products per observation. The names are not scientist-friendly, and can be as long as 70 characters. It is useful to learn enough about the naming scheme to identify products that are relevant for science analysis. In particular, L-3 product filenames are distinguishable from all the others, as explained below.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "File Naming Scheme", "Header 2": "Exposure- vs. Target/Source-based File Names"} -->
Lower-level, _exposure_ -based products correspond to a particular program, observation, visit, instrument, detector, and exposure. The file names are similar in structure to:
`jw00689001001_02201_00001_nrcalong_uncal.fits`
Note the program ID (`00689`), observation number (`001`) and visit number (`001`) concatenated near the beginning of the name. The string following the last underscore is the data product semantic type.
Higher-level, _target_ /_source_ -based products have file names similar in structure to:
`jw00689-o001_t001_nircam_clear-f356w_i2d.fits`
Note the program ID, followed by a dash, and then additional information including the instrument name and optical elements. See the article

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "File Naming Scheme", "Header 2": "File Contents"} -->
The semantic content of the files is encoded in the filename suffix (the part of the filename just preceding the file extension). For example, filenames ending with `_uncal.fits` are uncalibrated (Level-1) FITS-formatted data, while a file ending in `_cat.ecsv` is a Level-3 source catalog in ECSV format. See [MAST Data Product Types](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963707/MAST+Data+Product+Types) for a brief description of all semantic types found in MAST. See also JWST
Most, but not all, data products are in [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats) for a summary of data products and their formats, and the article on

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
The on-line documentation in JDox and in the calibration documentation (CAL) is very detailed and comprehensive.
* JWST
* [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
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
Learning which of the many JWST data products are appropriate for science analysis requires a basic understanding of how the data are processed, the file naming scheme, and the format and semantic content of the science-ready products.
**On this page...**
* 1[Science Data Processing](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-ScienceDataProcessing)
* 1.1[Level vs Stage](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-Level_StageLevelvsStage)
* 2[File Naming Scheme](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-FileNamingScheme)
* 2.1[Exposure- vs. Target/Source-based File Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-Exposure-vs.Target/Source-basedFileNames)
* 2.2[File Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-FileContents)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products#ScienceDataProducts-ForFurtherReading...)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Science Data Processing"} -->
A key point to understand is that, with _every_ JWST Observation (e.g., a row in the Portal results table), _all_ science and associated data products are bundled with it. These products include:
* All calibration levels of science data processing (see the summary in the [Level vs Stage](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) subsection below)
* Various [supplemental products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products)  
In all, the set of files per Observation could number in the hundreds or even thousands. Exactly which calibrated products are generated depends upon the configuration of the instrument that obtained the data (imaging, various forms of spectroscopy, coronagraphy), and the operating mode (time-series, dithered, moving target, etc.). See the detailed description of
The other products are useful either for evaluating the quality of the data processing, or to provide inputs in case you wish to re-process data with some or all stages of the
When searching for products in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html), those identified in the MAST [Portal Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) as [Minimum Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products) (MRP) are a good approximation to the most relevant for science analysis. These files usually number less than a dozen, except for multi-object spectroscopy where there is one highest-level, combined, extracted product per spectrum (i.e., potentially hundreds of spectra).
You will encounter slightly different labels to denote Science products, depending upon the document collection you are reading.
* **JDox:** The JWST mission document collection focuses on the pipeline processing __**stages**__ that are used to produce different products. See [Stages of Processing](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview) for details.
* **Processing (DMS):** The _**data management system**_ (which processes all JWST science data) focuses on the __**Level**__ of data product that is being produced; for products visible to users this starts with L-1b and ends with L-3. For comparison, the Stage 0 pipeline takes DMS L-1b products and produces L-2a products, which themselves comprise the input for the Stage-1 pipeline, and so on.
* **Archive (MAST):** The MAST Common Archive Observation Model (CAOM) database labels products by a generic calibration level that applies to many instruments and telescopes, whether ground- or space-based. It does not currently distinguish between DMS L-2a (slope corrected) and L-2b (instrument signature removed, calibrated to physical units).  
The following table summarizes the products and the translation between the vocabularies. You may also find helpful the diagrams in the [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) article.
Description | JDox Data Stage | DMS Processing Level | MAST/CAOM Calibration Level
---|---|---|---
Planned/approved but not yet executed observations | N/A | N/A | –1
Uncalibrated FITS files with all header keywords populated, per detector/exposure | Stage 0 | L–1b | 1
Slope-corrected FITS files (up-the-ramp slope removed), per detector | Stage 1 | L–2a | 2
FITS files, per detector and exposure, where instrument signature has been removed and the data have been astrometrically and radiometrically calibrated | Stage 2 |  L–2b (also L-2bs, L-2c, L-2cs) | 2
Combined, calibrated science product per target or source | Stage 3 | L–3 | 3
Contributed Science Products | N/A | N/A* | 4
*DMS does produce L-4 products for HST, but presently no such products are defined or produced for JWST.
**The target/source-based combined products (L-3), and the fully calibrated exposure-based images** from which they were derived (L-2b), are the most likely to be relevant for your science analysis.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "File Naming Scheme"} -->
The file name convention for JWST data products was designed in large part to facilitate automated processing of data products per observation. The names are not scientist-friendly, and can be as long as 70 characters. It is useful to learn enough about the naming scheme to identify products that are relevant for science analysis. In particular, L-3 product filenames are distinguishable from all the others, as explained below.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "File Naming Scheme", "Header 2": "Exposure- vs. Target/Source-based File Names"} -->
Lower-level, _exposure_ -based products correspond to a particular program, observation, visit, instrument, detector, and exposure. The file names are similar in structure to:
`jw00689001001_02201_00001_nrcalong_uncal.fits`
Note the program ID (`00689`), observation number (`001`) and visit number (`001`) concatenated near the beginning of the name. The string following the last underscore is the data product semantic type.
Higher-level, _target_ /_source_ -based products have file names similar in structure to:
`jw00689-o001_t001_nircam_clear-f356w_i2d.fits`
Note the program ID, followed by a dash, and then additional information including the instrument name and optical elements. See the article

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "File Naming Scheme", "Header 2": "File Contents"} -->
The semantic content of the files is encoded in the filename suffix (the part of the filename just preceding the file extension). For example, filenames ending with `_uncal.fits` are uncalibrated (Level-1) FITS-formatted data, while a file ending in `_cat.ecsv` is a Level-3 source catalog in ECSV format. See [MAST Data Product Types](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963707/MAST+Data+Product+Types) for a brief description of all semantic types found in MAST. See also JWST
Most, but not all, data products are in [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats) for a summary of data products and their formats, and the article on

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
The on-line documentation in JDox and in the calibration documentation (CAL) is very detailed and comprehensive.
* JWST
* [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

