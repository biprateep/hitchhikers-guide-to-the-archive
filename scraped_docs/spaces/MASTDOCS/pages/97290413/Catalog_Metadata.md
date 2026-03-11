---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290413/Catalog+Metadata"
date_accessed: "2026-03-11T16:26:50.842541"
content_length: 3809
---

<!-- CHUNK 1 START -->
<!-- Metadata: {"Header 1": "Catalogs as FITS BINTABLES"} -->
The keywords listed below are required or recommended for all FITS files in both primary (P) and extension (E) headers that contain catalogs.
The following table(s) of HLSP metadata, to be included in science products, are color-coded:  
| Required
---|---  
| Recommended  
| Suggested
File headers must also include the[common keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290410/Common+Metadata).  
| Keyword | HDU | Notes
---|---|---|---  
| TUNIT | E | Brightness unit for column containing values of physical quantities  
| RADESYS | E | Mnemonic for celestial coordinate reference system (typically'`FK5`''`ICRS`').  
|  <Filt>MAG0 | E | Flux corresponding to zero magnitude in the<Filt>

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Catalogs as FITS BINTABLES", "Header 2": "Catalog Fields"} -->
Most of the metadata in catalogs is often in the definition of the database fields, or table column names, units, and numeric types. Below are the recommended fields for source catalogs, where text in brackets is entirely user-defined.  
| Name | DataType | Notes
---|---|---|---  
| `DEC` | double | Declination coordinate of source  
| `RA` | double | Right ascension coordinate of source  
| `SOURCE` | string | Alphanumeric identifier of source  
| <Filt> | float | Brightness of source in the passband named<Filt>, with NULL value (NaN) indicating no measurement  
|  <Filt>`_err` | float | Uncertainty in source brightness.  
|  <Filt>`_flag` | int | Applicable, encoded flags that apply to the brightness in the named passband, with the convention that zero indicates no pathologies.
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Catalogs as FITS BINTABLES"} -->
The keywords listed below are required or recommended for all FITS files in both primary (P) and extension (E) headers that contain catalogs.
The following table(s) of HLSP metadata, to be included in science products, are color-coded:  
| Required
---|---  
| Recommended  
| Suggested
File headers must also include the[common keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290410/Common+Metadata).  
| Keyword | HDU | Notes
---|---|---|---  
| TUNIT | E | Brightness unit for column containing values of physical quantities  
| RADESYS | E | Mnemonic for celestial coordinate reference system (typically'`FK5`''`ICRS`').  
|  <Filt>MAG0 | E | Flux corresponding to zero magnitude in the<Filt>

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Catalogs as FITS BINTABLES", "Header 2": "Catalog Fields"} -->
Most of the metadata in catalogs is often in the definition of the database fields, or table column names, units, and numeric types. Below are the recommended fields for source catalogs, where text in brackets is entirely user-defined.  
| Name | DataType | Notes
---|---|---|---  
| `DEC` | double | Declination coordinate of source  
| `RA` | double | Right ascension coordinate of source  
| `SOURCE` | string | Alphanumeric identifier of source  
| <Filt> | float | Brightness of source in the passband named<Filt>, with NULL value (NaN) indicating no measurement  
|  <Filt>`_err` | float | Uncertainty in source brightness.  
|  <Filt>`_flag` | int | Applicable, encoded flags that apply to the brightness in the named passband, with the convention that zero indicates no pathologies.
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 4 END -->

