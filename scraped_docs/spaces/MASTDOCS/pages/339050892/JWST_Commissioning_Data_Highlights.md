---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights"
date_accessed: "2026-03-11T11:33:46.217319"
---

<!-- CHUNK 1 START -->
JWST commissioning has provided many datasets that astronomers may find useful. Datasets collected during the six month commissioning process provide examples of observation modes to help astronomers become familiar with data formats, the pipeline, and known artifacts, as well as to test their analysis methods. Some commissioning data may also provide serendipitous scientific value. Here we highlight some of the datasets that have been identified by the mission team as potentially useful to astronomers.
**On this page...**
* 1[Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights#JWSTCommissioningDataHighlights-Caveats)
* 2[Highlighted Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights#JWSTCommissioningDataHighlights-HighlightedData)
* 3[Additional Resources...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights#JWSTCommissioningDataHighlights-AdditionalResources...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Caveats"} -->
* These commissioning datasets were not originally intended for detailed scientific analysis, and may have artifacts, non-optimized instrument configurations, and other issues that were addressed during commissioning.
* Datasets obtained prior to the completion of OTE mirror alignment are particularly susceptible to significant variable wavefront error. Fine phasing of the telescope occurred on 11 March 2022. The wavefront stabilized after MIRI achieved operating temperature on 07 April 2022.
* Help for understanding the science content of these programs should be directed to The JWST Help Desk has very limited resources to investigate issues specific to the content of the data obtained during commissioning and will be prioritizing Cycle 1 support.  
MIRI Data
All MIRI commissioning data taken after a detector health and functionality checkout on DOY 101 (11 April 2022) may be of value to the scientific community; references are provided here to several example programs.  
The total volume of commissioning data exceeds 46 TB. Data from even a single program may take a long time to download, and will consume considerable space on local storage. We strongly recommend exploring the subset of programs and observations identified here in the **Highlighted Data** section, and restricting your search and download to only the observations denoted in the table. Observation numbers are denoted with a "-o###" [in observation IDs or file names](https://outerspace.stsci.edu/display/MASTDOCS/Science+Data+Products#ScienceDataProducts-Exposure-vs.Target/Source-basedFileNames) for supported products.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Highlighted Data"} -->
The retrieval scripts have been removed from AWS, since data are reprocessed over time with updated calibrations and pipeline versions.
This table still serves as a useful reference for commissioning observations that the mission and instrument teams have identified of being the most useful. We recommend you use the  [to search for and download the data products](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs#UsingMASTAPIs-AstroquerySearchandRetrieval) associated with these observations.
Target(s) | Instrument(s) | Template | Pointing Mode | PID | Observations | Notes
---|---|---|---|---|---|---
LMC astrometric field |  NIRCam FGS |  NIRCam Imaging FGS External Calibration | FINEGUIDE | [1074](https://www.stsci.edu/jwst-program-info/program/?program=1074) | Obs 1-3 | Observations of the LMC astrometric field in several filters and repeated
LMC Astrometric Field |  NIRISS FGS |  NIRISS External Calibration FGS External Calibration | FINEGUIDE | [1086](https://www.stsci.edu/jwst-program-info/program/?program=1086) | Obs 1 | Nine position imaging mosaic (10 square arcmin) of the LMC astrometric field in all 12 filters.
LMC Astrometric Field |  NIRCam FGS |  NIRCam Engineering Imaging FGS External Calibration | COARSE, TRACK, & FINEGUIDE | [1144](https://www.stsci.edu/jwst-program-info/program/?program=1144) | All NIRCam observations | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  NIRISS FGS |  NIRISS External Calibration FGS External Calibration | TRACK | [1145](https://www.stsci.edu/jwst-program-info/program/?program=1145) | All | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  NIRSpec FGS |  NIRSpec Imaging FGS External Calibration | FINEGUIDE | [1164](https://www.stsci.edu/jwst-program-info/program/?program=1164) | Obs 1-4 | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  MIRI FGS |  MIRI Medium Resolution Spectroscopy FGS External Calibration | FINEGUIDE | [1171](https://www.stsci.edu/jwst-program-info/program/?program=1171) | Obs 1-6 | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  NIRCam FGS/NIRISS NIRSpec MIRI |  NIRCam Imaging FGS External Calibration MIRI Imaging NIRISS Imaging NIRSpec MultiObject Spectroscopy | FINEGUIDE | [1473](https://www.stsci.edu/jwst-program-info/program/?program=1473) | All | This is the data used for the public image release right after OTE alignment complete. Contains many more filters and observations in all instruments.
2MASS05214330-6927498 P330-E P177-D WD1057+719 |  NIRCam FGS |  NIRCam Imaging FGS External Calibration | FINEGUIDE | [1074](https://www.stsci.edu/jwst-program-info/program/?program=1074) | Obs 4-106 | Photometric zero points and stability of two standard stars
P330-E | NIRCam |  NIRCam Grism Time Series NIRCam Wide Field Slitless Spectroscopy | FINEGUIDE | [1076](https://www.stsci.edu/jwst-program-info/program/?program=1076) | All | Includes TSO. LW Grism checkout. Includes WFSS data. Interesting background objects. A planetary nebula was observed as another part of this CAR.
WD1657+343 P330E | NIRISS | NIRISS External Calibration | FINEGUIDE | [1089](https://www.stsci.edu/jwst-program-info/program/?program=1089) | Obs 1-3 | Flux calibration observations in all 6 WFSS filters using standard stars. This is a relatively uncrowded field containing many background galaxies.
TYC 4433-1800-1 2MASS J17430448+6655015 GSPC P177-D PG 1057+719 GSPC P177-D 2MASS J16194609+5534178 | NIRSpec |  NIRSpec Bright Object Time Series NIRSpec IFU Spectroscopy NIRSpec Fixed Slit Spectroscopy NIRSpec MultiObject Spectroscopy | FINEGUIDE | [1128](https://www.stsci.edu/jwst-program-info/program/?program=1128) | All | Includes TSO. Sensitivity and absolute flux calibration using standard stars
BD+60-1753 | NIRISS | NIRISS Single-Object Slitless Spectroscopy | FINEGUIDE | [1091](https://www.stsci.edu/jwst-program-info/program/?program=1091) | Obs 2 | TSO of flux calibrator standard (SOSS)  
HAT-P-14 b | NIRSpec | NIRSpec Bright Object Time Series | FINEGUIDE | [1118](https://www.stsci.edu/jwst-program-info/program/?program=1118) | Obs 1 & 5 | TSO exoplanet transit
HAT-P-14 b  | NIRCam |  NIRCam Grism Time Series NIRCam Engineering Imaging | FINEGUIDE | [1442](https://www.stsci.edu/jwst-program-info/program/?program=1442) | Obs 1 & 3 | TSO exoplanet transit
HAT-P-14 b | NIRISS |  NIRISS Single-Object Slitless Spectroscopy NIRISS External Calibration | FINEGUIDE | [1541](https://www.stsci.edu/jwst-program-info/program/?program=1541) | Obs 1 | TSO exoplanet transit (SOSS)  
L 168-9 b | MIRI | MIRI Low Resolution Spectroscopy | FINEGUIDE | [1033](https://www.stsci.edu/jwst-program-info/program/?program=1033) | Obs 5 | TSO exoplanet transit
6481 Tenzing 2035 Stearns 1773 Rumpelstilz 20460 Robwhiteley 464798 (2004 JX20) 4015 Wilson-Harrington |  NIRCam NIRISS |  NIRCam Imaging NIRISS Aperture Masking Interferometry | MOVING | [1021](https://www.stsci.edu/jwst-program-info/program/?program=1021) | Obs 1-16 | Moving target test with NIRCam and NIRISS; observed various asteroids
Jupiter |  NIRCam FGS |  NIRCam Engineering Imaging FGS External Calibration | MOVING | [1022](https://www.stsci.edu/jwst-program-info/program/?program=1022) | All | Giant planet scattered light test
216 Kleopatra 64698 (2001 XY84) | NIRSpec |  NIRSpec IFU Spectroscopy NIRSpec MultiObject Spectroscopy | MOVING | [1444](https://www.stsci.edu/jwst-program-info/program/?program=1444) | Obs 1-3 | Moving target tracking test; observed various asteroids
2516 Roman 118 Peitho
| MIRI |  MIRI Imaging MIRI Medium Resolution Spectroscopy MIRI Low Resolution Spectroscopy | MOVING | [1449](https://www.stsci.edu/jwst-program-info/program/?program=1449) | Obs 1-3 | Moving target tracking test; observed various asteroids
HD 147980 | FGS |  FGS External Calibration
| FINEGUIDE | [1445](https://www.stsci.edu/jwst-program-info/program/?program=1445) | Obs 1-4, 20-30, 40-45 | FGS "accidental deep field" taken in parallel with WF monitoring during thermal slew. Originally intended for LOS jitter monitoring.
"ECLIPTIC-RA160" | NIRCam | NIRCam Engineering Imaging | COARSE | [1059](https://www.stsci.edu/jwst-program-info/program/?program=1059) | Obs 307 | Mosaic useful for backgrounds
"NIRISS-FOCUS-FIELD" | NIRISS | NIRISS Wide Field Slitless Spectroscopy | FINEGUIDE | [1085](https://www.stsci.edu/jwst-program-info/program/?program=1085) | Obs 12 | Imaging & spectroscopy of the NIRISS focus field in the outer LMC through all 12 filters and with the GR700XD grism and NRM.
SMP-LMC-58 |  NIRISS MIRI |  NIRISS Wide Field Slitless Spectroscopy NIRISS External Calibration MIRI Imaging | FINEGUIDE | [1090](https://www.stsci.edu/jwst-program-info/program/?program=1090) | Obs 1-2 | Wavelength calibration observations in 5 WFSS filters. Crowded LMC field including the planetary nebula SMP LMC-58.
"ECLIPTIC-RA80" | NIRISS | NIRISS External Calibration | FINEGUIDE | [1541](https://www.stsci.edu/jwst-program-info/program/?program=1541) | Obs 5 | Dithered observations with the GR700XD optical element performed to get observations of the (zodiacal) background, useful to correct NIRISS/SOSS observations
Galactic Bulge pointing Other pointings for backgrounds |  NIRCam NIRSpec NIRISS MIRI |  NIRCam Imaging MIRI Imaging NIRSpec MultiObject Spectroscopy NIRISS External Calibration | FINEGUIDE | [1448](https://www.stsci.edu/jwst-program-info/program/?program=1448) | All | Observations to measure stray light at various field points, including near the galactic center
HD 114174 HD 111733 HD 115640 HD 116249 | NIRCam | NIRCam Coronagraphic Imaging | FINEGUIDE | [1441](https://www.stsci.edu/jwst-program-info/program/?program=1441) | All | Check on coronagraphic performance
2MASS-J17554042+6551277 | NIRCam | NIRCam Imaging | FINEGUIDE | [1160](https://www.stsci.edu/jwst-program-info/program/?program=1160) | Obs 22 | First Observations
IRAS-05248-7007 | NIRSpec |  NIRSpec Fixed Slit Spectroscopy NIRSpec MultiObject Spectroscopy NIRSpec IFU Spectroscopy | FINEGUIDE | [1125](https://www.stsci.edu/jwst-program-info/program/?program=1125) | Obs 1, 5, & 6 | Spectra of emission-line object in the 3 NIRSpec modes and in various spectral configuration.
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Additional Resources..."} -->
* [JWST User Documentation Home](https://jwst-docs.stsci.edu/)
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
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
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search "Data Search")
* [Data Visualization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771401/Data+Visualization "Data Visualization")
* [Data Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection "Data Selection")
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval "Data Retrieval")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
* [API Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search "API Advanced Search")
* [API Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download "API Curl Download")
* [API for JWST Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata "API for JWST Metadata")
* [API for JWST Science Pixels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113031/API+for+JWST+Science+Pixels "API for JWST Science Pixels")
* [Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API "Basics of an API")
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
JWST commissioning has provided many datasets that astronomers may find useful. Datasets collected during the six month commissioning process provide examples of observation modes to help astronomers become familiar with data formats, the pipeline, and known artifacts, as well as to test their analysis methods. Some commissioning data may also provide serendipitous scientific value. Here we highlight some of the datasets that have been identified by the mission team as potentially useful to astronomers.
**On this page...**
* 1[Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights#JWSTCommissioningDataHighlights-Caveats)
* 2[Highlighted Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights#JWSTCommissioningDataHighlights-HighlightedData)
* 3[Additional Resources...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights#JWSTCommissioningDataHighlights-AdditionalResources...)

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Caveats"} -->
* These commissioning datasets were not originally intended for detailed scientific analysis, and may have artifacts, non-optimized instrument configurations, and other issues that were addressed during commissioning.
* Datasets obtained prior to the completion of OTE mirror alignment are particularly susceptible to significant variable wavefront error. Fine phasing of the telescope occurred on 11 March 2022. The wavefront stabilized after MIRI achieved operating temperature on 07 April 2022.
* Help for understanding the science content of these programs should be directed to The JWST Help Desk has very limited resources to investigate issues specific to the content of the data obtained during commissioning and will be prioritizing Cycle 1 support.  
MIRI Data
All MIRI commissioning data taken after a detector health and functionality checkout on DOY 101 (11 April 2022) may be of value to the scientific community; references are provided here to several example programs.  
The total volume of commissioning data exceeds 46 TB. Data from even a single program may take a long time to download, and will consume considerable space on local storage. We strongly recommend exploring the subset of programs and observations identified here in the **Highlighted Data** section, and restricting your search and download to only the observations denoted in the table. Observation numbers are denoted with a "-o###" [in observation IDs or file names](https://outerspace.stsci.edu/display/MASTDOCS/Science+Data+Products#ScienceDataProducts-Exposure-vs.Target/Source-basedFileNames) for supported products.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Highlighted Data"} -->
The retrieval scripts have been removed from AWS, since data are reprocessed over time with updated calibrations and pipeline versions.
This table still serves as a useful reference for commissioning observations that the mission and instrument teams have identified of being the most useful. We recommend you use the  [to search for and download the data products](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs#UsingMASTAPIs-AstroquerySearchandRetrieval) associated with these observations.
Target(s) | Instrument(s) | Template | Pointing Mode | PID | Observations | Notes
---|---|---|---|---|---|---
LMC astrometric field |  NIRCam FGS |  NIRCam Imaging FGS External Calibration | FINEGUIDE | [1074](https://www.stsci.edu/jwst-program-info/program/?program=1074) | Obs 1-3 | Observations of the LMC astrometric field in several filters and repeated
LMC Astrometric Field |  NIRISS FGS |  NIRISS External Calibration FGS External Calibration | FINEGUIDE | [1086](https://www.stsci.edu/jwst-program-info/program/?program=1086) | Obs 1 | Nine position imaging mosaic (10 square arcmin) of the LMC astrometric field in all 12 filters.
LMC Astrometric Field |  NIRCam FGS |  NIRCam Engineering Imaging FGS External Calibration | COARSE, TRACK, & FINEGUIDE | [1144](https://www.stsci.edu/jwst-program-info/program/?program=1144) | All NIRCam observations | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  NIRISS FGS |  NIRISS External Calibration FGS External Calibration | TRACK | [1145](https://www.stsci.edu/jwst-program-info/program/?program=1145) | All | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  NIRSpec FGS |  NIRSpec Imaging FGS External Calibration | FINEGUIDE | [1164](https://www.stsci.edu/jwst-program-info/program/?program=1164) | Obs 1-4 | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  MIRI FGS |  MIRI Medium Resolution Spectroscopy FGS External Calibration | FINEGUIDE | [1171](https://www.stsci.edu/jwst-program-info/program/?program=1171) | Obs 1-6 | LMC astrometric field _from pre-OTE-alignment complete_
LMC Astrometric Field |  NIRCam FGS/NIRISS NIRSpec MIRI |  NIRCam Imaging FGS External Calibration MIRI Imaging NIRISS Imaging NIRSpec MultiObject Spectroscopy | FINEGUIDE | [1473](https://www.stsci.edu/jwst-program-info/program/?program=1473) | All | This is the data used for the public image release right after OTE alignment complete. Contains many more filters and observations in all instruments.
2MASS05214330-6927498 P330-E P177-D WD1057+719 |  NIRCam FGS |  NIRCam Imaging FGS External Calibration | FINEGUIDE | [1074](https://www.stsci.edu/jwst-program-info/program/?program=1074) | Obs 4-106 | Photometric zero points and stability of two standard stars
P330-E | NIRCam |  NIRCam Grism Time Series NIRCam Wide Field Slitless Spectroscopy | FINEGUIDE | [1076](https://www.stsci.edu/jwst-program-info/program/?program=1076) | All | Includes TSO. LW Grism checkout. Includes WFSS data. Interesting background objects. A planetary nebula was observed as another part of this CAR.
WD1657+343 P330E | NIRISS | NIRISS External Calibration | FINEGUIDE | [1089](https://www.stsci.edu/jwst-program-info/program/?program=1089) | Obs 1-3 | Flux calibration observations in all 6 WFSS filters using standard stars. This is a relatively uncrowded field containing many background galaxies.
TYC 4433-1800-1 2MASS J17430448+6655015 GSPC P177-D PG 1057+719 GSPC P177-D 2MASS J16194609+5534178 | NIRSpec |  NIRSpec Bright Object Time Series NIRSpec IFU Spectroscopy NIRSpec Fixed Slit Spectroscopy NIRSpec MultiObject Spectroscopy | FINEGUIDE | [1128](https://www.stsci.edu/jwst-program-info/program/?program=1128) | All | Includes TSO. Sensitivity and absolute flux calibration using standard stars
BD+60-1753 | NIRISS | NIRISS Single-Object Slitless Spectroscopy | FINEGUIDE | [1091](https://www.stsci.edu/jwst-program-info/program/?program=1091) | Obs 2 | TSO of flux calibrator standard (SOSS)  
HAT-P-14 b | NIRSpec | NIRSpec Bright Object Time Series | FINEGUIDE | [1118](https://www.stsci.edu/jwst-program-info/program/?program=1118) | Obs 1 & 5 | TSO exoplanet transit
HAT-P-14 b  | NIRCam |  NIRCam Grism Time Series NIRCam Engineering Imaging | FINEGUIDE | [1442](https://www.stsci.edu/jwst-program-info/program/?program=1442) | Obs 1 & 3 | TSO exoplanet transit
HAT-P-14 b | NIRISS |  NIRISS Single-Object Slitless Spectroscopy NIRISS External Calibration | FINEGUIDE | [1541](https://www.stsci.edu/jwst-program-info/program/?program=1541) | Obs 1 | TSO exoplanet transit (SOSS)  
L 168-9 b | MIRI | MIRI Low Resolution Spectroscopy | FINEGUIDE | [1033](https://www.stsci.edu/jwst-program-info/program/?program=1033) | Obs 5 | TSO exoplanet transit
6481 Tenzing 2035 Stearns 1773 Rumpelstilz 20460 Robwhiteley 464798 (2004 JX20) 4015 Wilson-Harrington |  NIRCam NIRISS |  NIRCam Imaging NIRISS Aperture Masking Interferometry | MOVING | [1021](https://www.stsci.edu/jwst-program-info/program/?program=1021) | Obs 1-16 | Moving target test with NIRCam and NIRISS; observed various asteroids
Jupiter |  NIRCam FGS |  NIRCam Engineering Imaging FGS External Calibration | MOVING | [1022](https://www.stsci.edu/jwst-program-info/program/?program=1022) | All | Giant planet scattered light test
216 Kleopatra 64698 (2001 XY84) | NIRSpec |  NIRSpec IFU Spectroscopy NIRSpec MultiObject Spectroscopy | MOVING | [1444](https://www.stsci.edu/jwst-program-info/program/?program=1444) | Obs 1-3 | Moving target tracking test; observed various asteroids
2516 Roman 118 Peitho
| MIRI |  MIRI Imaging MIRI Medium Resolution Spectroscopy MIRI Low Resolution Spectroscopy | MOVING | [1449](https://www.stsci.edu/jwst-program-info/program/?program=1449) | Obs 1-3 | Moving target tracking test; observed various asteroids
HD 147980 | FGS |  FGS External Calibration
| FINEGUIDE | [1445](https://www.stsci.edu/jwst-program-info/program/?program=1445) | Obs 1-4, 20-30, 40-45 | FGS "accidental deep field" taken in parallel with WF monitoring during thermal slew. Originally intended for LOS jitter monitoring.
"ECLIPTIC-RA160" | NIRCam | NIRCam Engineering Imaging | COARSE | [1059](https://www.stsci.edu/jwst-program-info/program/?program=1059) | Obs 307 | Mosaic useful for backgrounds
"NIRISS-FOCUS-FIELD" | NIRISS | NIRISS Wide Field Slitless Spectroscopy | FINEGUIDE | [1085](https://www.stsci.edu/jwst-program-info/program/?program=1085) | Obs 12 | Imaging & spectroscopy of the NIRISS focus field in the outer LMC through all 12 filters and with the GR700XD grism and NRM.
SMP-LMC-58 |  NIRISS MIRI |  NIRISS Wide Field Slitless Spectroscopy NIRISS External Calibration MIRI Imaging | FINEGUIDE | [1090](https://www.stsci.edu/jwst-program-info/program/?program=1090) | Obs 1-2 | Wavelength calibration observations in 5 WFSS filters. Crowded LMC field including the planetary nebula SMP LMC-58.
"ECLIPTIC-RA80" | NIRISS | NIRISS External Calibration | FINEGUIDE | [1541](https://www.stsci.edu/jwst-program-info/program/?program=1541) | Obs 5 | Dithered observations with the GR700XD optical element performed to get observations of the (zodiacal) background, useful to correct NIRISS/SOSS observations
Galactic Bulge pointing Other pointings for backgrounds |  NIRCam NIRSpec NIRISS MIRI |  NIRCam Imaging MIRI Imaging NIRSpec MultiObject Spectroscopy NIRISS External Calibration | FINEGUIDE | [1448](https://www.stsci.edu/jwst-program-info/program/?program=1448) | All | Observations to measure stray light at various field points, including near the galactic center
HD 114174 HD 111733 HD 115640 HD 116249 | NIRCam | NIRCam Coronagraphic Imaging | FINEGUIDE | [1441](https://www.stsci.edu/jwst-program-info/program/?program=1441) | All | Check on coronagraphic performance
2MASS-J17554042+6551277 | NIRCam | NIRCam Imaging | FINEGUIDE | [1160](https://www.stsci.edu/jwst-program-info/program/?program=1160) | Obs 22 | First Observations
IRAS-05248-7007 | NIRSpec |  NIRSpec Fixed Slit Spectroscopy NIRSpec MultiObject Spectroscopy NIRSpec IFU Spectroscopy | FINEGUIDE | [1125](https://www.stsci.edu/jwst-program-info/program/?program=1125) | Obs 1, 5, & 6 | Spectra of emission-line object in the 3 NIRSpec modes and in various spectral configuration.
* * *

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Additional Resources..."} -->
* [JWST User Documentation Home](https://jwst-docs.stsci.edu/)
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 7 END -->

