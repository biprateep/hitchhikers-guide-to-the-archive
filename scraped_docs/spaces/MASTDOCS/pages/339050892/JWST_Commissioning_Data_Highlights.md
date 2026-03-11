---
title: "Caveats"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/339050892/JWST+Commissioning+Data+Highlights"
date_accessed: "2026-03-11T16:32:14.471377"
content_length: 11345
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

<!-- CHUNK 4 END -->

