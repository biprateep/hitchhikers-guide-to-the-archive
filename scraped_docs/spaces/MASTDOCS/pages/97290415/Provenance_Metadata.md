---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata"
date_accessed: "2026-03-11T21:27:42.070031"
---

**On this page...**
  * 1[Data Provenance](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-DataProvenance)
    * 1.1[Header Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-HeaderKeywords)
    * 1.2[FITS Provenance Extension](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-FITSProvenanceExtension)
      * 1.2.1[Table Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-TableFields)
  * 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-ForFurtherReading...)

# Data Provenance
Establishing the provenance of science data products is important to the users of HLSP collections for a number of reasons, including:
  * Promoting data traceability and reproducibility
  * Establishing the pedigree for the quality of the data processing
  * Understanding the facilities, instruments, configurations used obtain the data, and under what environmental circumstances the data were obtained

Provenance should be recorded in multiple ways, including the Project Description file and the README file that must be included in every HLSP collection (see [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents)). It is also established in the primary journal paper where each HLSP collection is described. Various of the metadata listed in this chapter as required or recommended partially address these needs. The focus of this article is the recording of sufficient metadata that associations can be created between HLSP products and the MAST mission products (or the products from other observatories) from which they were derived. Two approaches have been used for this purpose, as described in the subsections below.
## Header Keywords
The other sections of this chapter identified some keywords where the value in the contributing products may be different. To represent a meaningful value in the HLSP product:
  * the value should be 'MULTI'
  * the keyword record should be followed by supplemental records with an abbreviation of the original keyword, with a 2-digit numerical suffix
    * each supplemental record should contain a value appropriate to the contributing product, in numerical order

The following table illustrates the concept for a composite UV spectrum of a target, using two HST instruments. Note that the contributing observations are linked to the HLSP product through the MAST Observation ID, shown in the table as '`FILEID`nn'.

Keyword | Value
---|---
`DISPERSR` | `'MULTI'`
`DISPER01` | `'G130M/180'`
`DISPER02` | `'E230M'`
`FILEID01` | `'lea22cx3q'`
`FILEID02` | `'ockp07020'`
`INSTRUME` | `'MULTI'`
`INSTRU01` | `'COS'`
`INSTRU02` | `'STIS'`
An acceptable synonym for `FILEID`_**nn**_ is `DATA`_**nn**_.
## FITS Provenance Extension
It is sometimes tedious, even impractical, to record critical metadata for every data product that contributed to constructing an HLSP product. Examples include:
  * combined images constructed from many exposures,
  * multi-band catalogs that draw data from many observing facilities,
  * SEDs composed from spectra from multiple observing facilities, telescopes, and instruments in one or more configurations

In these cases it may be better to collect this information in a BINTABLE extension to each HLSP FITS product. The table should have the following attributes:
  * Specify `EXTNAME = 'PROVENANCE'` in the extension header
  * List each contributing data product, one per table row
  * Use one table column per attribute
  * At a minimum, include all relevant attributes that vary among contributing products
  * Specify the data type and units (if applicable) in the header for each attribute

### Table Fields
The following table gives examples of attributes that may be applicable to an HLSP collection.
Field Name | Example Value | Description
---|---|---
`FILE_ID` | '`ockp11020`' | File name or observatory-unique identifier of the contributing observation. For products from MAST missions, provide the Observation ID so that the contributing data may be linked within MAST.
`DATE-BEG` | `'2021-01-05T12:34:56.78'` | ISO 8601-formatted date-time string for observation start
`DATE-END` | `'2021-01-05T12:39:56.78'` | ISO 8601-formatted date-time string for observation end
`DISPRSR` | `'G140L'` | Name of dispersing optical element used
`FILTER` | `'F25ND'` | Name of (possibly passband limiting) filter used
`INSTRUME` | `'STIS'` | Name of instrument used
`RADESYS` | `'ICRS'` | Coordinate reference frame
`TELESCOP` | `'HST'` | Name of telescope used
`XPOSURE` | `300` | Total duration of exposure in sec, exclusive of dead-time
# For Further Reading...
  * [Common Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290410/Common+Metadata)

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
    * [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
    * [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
    * [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
    * [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
      * [Common Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290410/Common+Metadata "Common Metadata")
      * [Image Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290411/Image+Metadata "Image Metadata")
      * [Spectral Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290412/Spectral+Metadata "Spectral Metadata")
      * [Catalog Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290413/Catalog+Metadata "Catalog Metadata")
      * [Light-curve Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290414/Light-curve+Metadata "Light-curve Metadata")
      * [Provenance Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata "Provenance Metadata")
    * [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
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
    * [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
    * [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
    * [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
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
  * [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
  * [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
  * [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")

**On this page...**
  * 1[Data Provenance](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-DataProvenance)
    * 1.1[Header Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-HeaderKeywords)
    * 1.2[FITS Provenance Extension](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-FITSProvenanceExtension)
      * 1.2.1[Table Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-TableFields)
  * 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290415/Provenance+Metadata#ProvenanceMetadata-ForFurtherReading...)

# Data Provenance
Establishing the provenance of science data products is important to the users of HLSP collections for a number of reasons, including:
  * Promoting data traceability and reproducibility
  * Establishing the pedigree for the quality of the data processing
  * Understanding the facilities, instruments, configurations used obtain the data, and under what environmental circumstances the data were obtained

Provenance should be recorded in multiple ways, including the Project Description file and the README file that must be included in every HLSP collection (see [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents)). It is also established in the primary journal paper where each HLSP collection is described. Various of the metadata listed in this chapter as required or recommended partially address these needs. The focus of this article is the recording of sufficient metadata that associations can be created between HLSP products and the MAST mission products (or the products from other observatories) from which they were derived. Two approaches have been used for this purpose, as described in the subsections below.
## Header Keywords
The other sections of this chapter identified some keywords where the value in the contributing products may be different. To represent a meaningful value in the HLSP product:
  * the value should be 'MULTI'
  * the keyword record should be followed by supplemental records with an abbreviation of the original keyword, with a 2-digit numerical suffix
    * each supplemental record should contain a value appropriate to the contributing product, in numerical order

The following table illustrates the concept for a composite UV spectrum of a target, using two HST instruments. Note that the contributing observations are linked to the HLSP product through the MAST Observation ID, shown in the table as '`FILEID`nn'.

Keyword | Value
---|---
`DISPERSR` | `'MULTI'`
`DISPER01` | `'G130M/180'`
`DISPER02` | `'E230M'`
`FILEID01` | `'lea22cx3q'`
`FILEID02` | `'ockp07020'`
`INSTRUME` | `'MULTI'`
`INSTRU01` | `'COS'`
`INSTRU02` | `'STIS'`
An acceptable synonym for `FILEID`_**nn**_ is `DATA`_**nn**_.
## FITS Provenance Extension
It is sometimes tedious, even impractical, to record critical metadata for every data product that contributed to constructing an HLSP product. Examples include:
  * combined images constructed from many exposures,
  * multi-band catalogs that draw data from many observing facilities,
  * SEDs composed from spectra from multiple observing facilities, telescopes, and instruments in one or more configurations

In these cases it may be better to collect this information in a BINTABLE extension to each HLSP FITS product. The table should have the following attributes:
  * Specify `EXTNAME = 'PROVENANCE'` in the extension header
  * List each contributing data product, one per table row
  * Use one table column per attribute
  * At a minimum, include all relevant attributes that vary among contributing products
  * Specify the data type and units (if applicable) in the header for each attribute

### Table Fields
The following table gives examples of attributes that may be applicable to an HLSP collection.
Field Name | Example Value | Description
---|---|---
`FILE_ID` | '`ockp11020`' | File name or observatory-unique identifier of the contributing observation. For products from MAST missions, provide the Observation ID so that the contributing data may be linked within MAST.
`DATE-BEG` | `'2021-01-05T12:34:56.78'` | ISO 8601-formatted date-time string for observation start
`DATE-END` | `'2021-01-05T12:39:56.78'` | ISO 8601-formatted date-time string for observation end
`DISPRSR` | `'G140L'` | Name of dispersing optical element used
`FILTER` | `'F25ND'` | Name of (possibly passband limiting) filter used
`INSTRUME` | `'STIS'` | Name of instrument used
`RADESYS` | `'ICRS'` | Coordinate reference frame
`TELESCOP` | `'HST'` | Name of telescope used
`XPOSURE` | `300` | Total duration of exposure in sec, exclusive of dead-time
# For Further Reading...
  * [Common Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290410/Common+Metadata)

[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:
