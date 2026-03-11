---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290408/Example+HLSP+README"
date_accessed: "2026-03-11T16:26:49.632862"
content_length: 14322
---

<!-- CHUNK 1 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Contributor"} -->
* R.A. Shaw (STScI)
* 2018-May-1

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "General Information"} -->
This file is intended as an example of a well organized README file, which would be included in a delivery of an HLSP data collection. The following text is excerpted from the README provided by the GOODS v2.0 release of the ACS multi-band catalog data.
These catalogs, prepared using the SExtractor package (Bertin & Arnouts 1996,
The catalogs are *z*-band based, that is, source detection has been made using the *z*-band images. A variety of photometric apertures defined during the detection process have then been used as "fixed apertures" in the *i*, *v*, and *b*-band images to derive the multi-band photometry.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "What is Being Released"} -->
This v2.0 release of the multi-band source catalogs comprises:
* 8 primary ASCII files (the updated catalogs)
* 1 updated file required to configure SExtractor
* this "README" file  
The primary catalog files have names of the form:
hlsp_goods_hst_acs_<region>_<filter>_v2.0_drz_cat.txt  
where _region_ _filter is_ one of: (b,v,i,z). The file format is ASCII text with whitespace-separated columns.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Changes from Previous GOODS ACS Data Releases"} -->
The v2.0 catalog release is based on the v2.0 images, which, as described above, have significantly longer total exposure times in the z850 bandpass, and somewhat longer exposure times in the i775 and v606 bands as well. The only significant difference in the catalogs, other than that of being based on deeper data, is that we have applied a small astrometric offset to the GOODS-North images (only), as explained in the v2.0 documentation.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "How the Catalogs Were Prepared"} -->
With the scale of the images set at 0.03 arcsec per pixel (to improve the sampling of the PSF), each GOODS field would have resulted in images too large in size for practical purposes (40,000×40,000 pixels for the HDF-N and 32,000×40,000 pixels for the CDF-S). As a result, each field has been divided into contiguous sections, each 8,192×8,192 pixels in size. A total of 17 sections cover the HDF-N, and a total of 18 sections cover the CDF-S....

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Source Detection and Photometry"} -->
Source detection was carried out on the z-band images, and photometry was then measured in the other bandpasses using SExtractor "dual image mode", i.e., through fixed apertures defined from the z-band detection catalog...
Before cataloging, we verified the noise scaling by measuring the amplitude and autocorrelation of the background noise in the drizzled science images, and using this information to rescale the weight maps ("w") by a weight scale factor ("s") before converting to RMS maps ("rms"): rms = 1/√(s*w)
**GOODS ACS Weight Map Rescaling Factors (arcsec)**
Bandpass | North | South
---|---|---
F435W | 0.9052 | 0.8487
F606W | 0.9386 | 0.8987
F775W | 0.9094 | 0.9199
F850LP | 0.9307 | 0.9295
In most cases, these factors change the scaling of the RMS maps by less than 5%....

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Column Description for the Catalogs"} -->
A listing of the 104 individual columns of the catalogs, reproduced from the catalog file headers, is provided below. We have added brief descriptions of the output quantities here, but in many cases the user should refer to the SExtractor documentation for more detailed explanations....
**GOODS ACS Weight Map Rescaling Factors**
Col | Field | Description
---|---|---
1 | ID_IAU | IAU-format coordinate-based name for object
2 | ALPHA_J2000 | J2000 Right Ascension (degrees)
3 | DELTA_J2000 | J2000 Declination (degrees)
4 | SECT_REFNUM | section number from GOODS v2.0 imaging data
5 | X_SECT | centroid pixel x coordinate within section
6 | Y_SECT | centroid pixel y coordinate within section
7 | X_MOSAIC | centroid pixel x coordinate within a virtual mosaic of all sections
8 | Y_MOSAIC | centroid pixel y coordinate within a virtual mosaic of all sections
9 | ... | ...

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Publications"} -->
A description of the GOODS observations and data products is given in:
Giavalisco, M. and the GOODS Team 2004,  _The Great Observatories Origins Deep Survey: Initial Results from Optical and Near-Infrared Imaging_
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
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide "HLSP Search Guide")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Publication Timeline](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/214205149/Publication+Timeline "Publication Timeline")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Collection Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290404/Collection+Contents "Collection Contents")
* [File Types, Formats, Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content "File Types, Formats, Content")
* [Organizing the Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection "Organizing the Collection")
* [File Naming Convention](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention "File Naming Convention")
* [Example HLSP README](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290408/Example+HLSP+README "Example HLSP README")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Collection Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290404/Collection+Contents "Collection Contents")
* [File Types, Formats, and Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content "File Types, Formats, and Content")
* [Organizing the Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection "Organizing the Collection")
* [File Naming Convention](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention "File Naming Convention")
* [Example HLSP README](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290408/Example+HLSP+README "Example HLSP README")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Contributor"} -->
* R.A. Shaw (STScI)
* 2018-May-1

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "General Information"} -->
This file is intended as an example of a well organized README file, which would be included in a delivery of an HLSP data collection. The following text is excerpted from the README provided by the GOODS v2.0 release of the ACS multi-band catalog data.
These catalogs, prepared using the SExtractor package (Bertin & Arnouts 1996,
The catalogs are *z*-band based, that is, source detection has been made using the *z*-band images. A variety of photometric apertures defined during the detection process have then been used as "fixed apertures" in the *i*, *v*, and *b*-band images to derive the multi-band photometry.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "What is Being Released"} -->
This v2.0 release of the multi-band source catalogs comprises:
* 8 primary ASCII files (the updated catalogs)
* 1 updated file required to configure SExtractor
* this "README" file  
The primary catalog files have names of the form:
hlsp_goods_hst_acs_<region>_<filter>_v2.0_drz_cat.txt  
where _region_ _filter is_ one of: (b,v,i,z). The file format is ASCII text with whitespace-separated columns.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Changes from Previous GOODS ACS Data Releases"} -->
The v2.0 catalog release is based on the v2.0 images, which, as described above, have significantly longer total exposure times in the z850 bandpass, and somewhat longer exposure times in the i775 and v606 bands as well. The only significant difference in the catalogs, other than that of being based on deeper data, is that we have applied a small astrometric offset to the GOODS-North images (only), as explained in the v2.0 documentation.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "How the Catalogs Were Prepared"} -->
With the scale of the images set at 0.03 arcsec per pixel (to improve the sampling of the PSF), each GOODS field would have resulted in images too large in size for practical purposes (40,000×40,000 pixels for the HDF-N and 32,000×40,000 pixels for the CDF-S). As a result, each field has been divided into contiguous sections, each 8,192×8,192 pixels in size. A total of 17 sections cover the HDF-N, and a total of 18 sections cover the CDF-S....

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Source Detection and Photometry"} -->
Source detection was carried out on the z-band images, and photometry was then measured in the other bandpasses using SExtractor "dual image mode", i.e., through fixed apertures defined from the z-band detection catalog...
Before cataloging, we verified the noise scaling by measuring the amplitude and autocorrelation of the background noise in the drizzled science images, and using this information to rescale the weight maps ("w") by a weight scale factor ("s") before converting to RMS maps ("rms"): rms = 1/√(s*w)
**GOODS ACS Weight Map Rescaling Factors (arcsec)**
Bandpass | North | South
---|---|---
F435W | 0.9052 | 0.8487
F606W | 0.9386 | 0.8987
F775W | 0.9094 | 0.9199
F850LP | 0.9307 | 0.9295
In most cases, these factors change the scaling of the RMS maps by less than 5%....

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Column Description for the Catalogs"} -->
A listing of the 104 individual columns of the catalogs, reproduced from the catalog file headers, is provided below. We have added brief descriptions of the output quantities here, but in many cases the user should refer to the SExtractor documentation for more detailed explanations....
**GOODS ACS Weight Map Rescaling Factors**
Col | Field | Description
---|---|---
1 | ID_IAU | IAU-format coordinate-based name for object
2 | ALPHA_J2000 | J2000 Right Ascension (degrees)
3 | DELTA_J2000 | J2000 Declination (degrees)
4 | SECT_REFNUM | section number from GOODS v2.0 imaging data
5 | X_SECT | centroid pixel x coordinate within section
6 | Y_SECT | centroid pixel y coordinate within section
7 | X_MOSAIC | centroid pixel x coordinate within a virtual mosaic of all sections
8 | Y_MOSAIC | centroid pixel y coordinate within a virtual mosaic of all sections
9 | ... | ...

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "README", "Header 2": "Publications"} -->
A description of the GOODS observations and data products is given in:
Giavalisco, M. and the GOODS Team 2004,  _The Great Observatories Origins Deep Survey: Initial Results from Optical and Near-Infrared Imaging_
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 16 END -->

