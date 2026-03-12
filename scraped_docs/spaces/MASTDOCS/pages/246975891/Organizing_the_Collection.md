---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection"
date_accessed: "2026-03-11T11:34:43.280992"
---

<!-- CHUNK 1 START -->
Often there are multiple reasonable ways to organize science data within files, and files within an HLSP collection. This article provides advice and some best practices to make the process of incorporating your data in MAST go smoothly.
**On this page...**
* 1[File Organization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-FileOrganization)
* 2[Data Organization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-DataOrganization)
* 2.1[Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Images)
* 2.2[Spectra](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Spectra)
* 2.3[Catalogs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Catalogs)
* 2.4[Metadata within files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Metadatawithinfiles)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "File Organization"} -->
The best organization for files delivered to MAST for an HLSP collection depends mostly upon the number of files, and secondarily on the nature of the products. For small collections consisting of perhaps a few dozen files: it is acceptable to put all files in a single directory. For larger collections it may be better to organize the files in a directory tree, with subfolders named (for instance) by target or field identifier. If organizing by some directory structure, please keep files that apply to the full collection (i.e., the README, the project summary for the Web home page, etc.) in the root directory so that MAST staff can locate them easily.
If you are uploading products for a new data release (new and/or updated products), please place them in a sub-folder of the delivery area, with a name like "/dr2" to indicates the data release ID associated with those products.
The arrangement of files into a directory tree is mostly for the convenience of the contributing team in preparing the collection, and the MAST team in validating and moving the products to our mass storage devices. The presentation of the collection products in MAST interfaces (e.g., the Portal) does not depend upon the submitted file structure.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Data Organization"} -->
There is typically more than one reasonable way to organize data within or among files. In the absence of community standards, the following guidelines will help to ensure that users can:
* retrieve data from MAST without technical problems
* use the products with widely available community tools
* identify the various components of data products (e.g., science vs. error arrays) easily  
While many of the guidelines in the following subsections for science data are described in the context of

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Images"} -->
For organizing data within images, consider the following strategies:
* **Concomitant data:** Put pixel-level arrays of error/uncertainty, data quality flags, exposure maps, etc. in the same file with the science arrays.  
* For image data, put the science array in a FITS **image extension** that includes the keyword EXTNAME = SCI, and put concomitant data in additional extensions with appropriate extension names like "`ERR`", "`DQ`", "`EXP_MAP`", and "`WEIGHT`".
* If data are placed in FITS extensions, do not place any data in the Primary header-data unit (PHDU).
* **File size:** While there is no hard upper-limit, it is often best to keep the size of individual files under about 1 GB. This will facilitate downloads for users with poor internet connectivity. This advice may be at odds with storing concomitant data in the same file as the science pixels; if so, consider storing concomitant data in separate files if doing so doesn't unduly increase the complexity of the file organization.  
* Be sure that the data types of your arrays are consistent with the required precision. For example, 64-bit floating point precision is rarely needed for any quantity other than values of coordinates or timestamps. Similarly, data quality masks may require only 16-bit (short integer) precision.
* **Null data:** Try to avoid creating arrays with large numbers of missing or null pixels. For combined images, this may be as simple as choosing an orientation for the combined array that naturally captures the footprints of all contributing images with minimal dead area; the world coordinate system (WCS) keywords will let downstream applications know the physical orientation without wasting memory.
* **Image maps:** if you have created multiple spatial maps of physical quantities for a given target (e.g., reddening, temperature, star formation rate) for a given target, consider putting them in image extensions within a single file. This will keep information about each target together, and also make it easier to follow the [file naming requirements](https://outerspace.stsci.edu/display/MASTDOCS/File+Naming+Convention).

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra"} -->
There are two main approaches to storing spectra in files: in images or in tables. Here, spectral data includes pixel-level science and concomitant data, including arrays of: flux(density), uncertainty, data quality (DQ) flags, weights, and wavelength (if tabulated).
Science-ready spectra have a variety of types, including
* Spectral image cubes, such as those generated with IFUs, stored as cubes with one dispersion axis and two spatial axes
* Long-slit spectra, with one dispersion and one spatial axis
* Time-series spectra, with one dispersion and one temporal axis  
HSLP contributors may wish to provide more than one type of spectrum, e.g., long-slit and a reference 1-D extraction. It is generally better to provide separate types of products in separate files.
The strategies for arranging data are summarized below.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra", "Header 3": "Spectra in tables"} -->
Two of the most common community conventions for storing one-dimensional extracted spectra in FITS files are:
1. One spectrum per BINTABLE extension, such that 1-D arrays are stored in separate fields, one (wavelength, flux, err, dq) tuple per row.
2. Multiple spectra per BINTABLE extension, with one spectrum per table row. In this case each cell of (wavelength, flux, err, dq) contains an array of the same length.  
A variation on the above options is to express the wavelength array with a function in FITS keywords. If every spectrum in an extension has the same wavelength array, you can use single-valued WCS keywords to describe the function. If the WCS function changes as a function of row in a BINTABLE, you can expand these WCS keywords into BINTABLE columns. This strategy works well for simple 1-D spectra, separate orders of echelle spectra, and Multi-object spectra (from MOS spectrograms of separate targets in a small field of view). Multi-dimensional spectra can also be stored in tables, but it becomes more complicated to describe the WCS in a compact way.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra", "Header 3": "Spectra in images"} -->
Many spectra derive from spectrograms that are multi-dimensional, where the other dimension(s) may be spatial or temporal. These data are sometimes represented as images with two or more dimensions; the dispersion is most commonly expressed as a function, rather than tabulated in a separate array. Examples include:
* Long-slit spectra are stored as images with one dispersion and one spatial (cross-dispersion) axis. (Note: it is possible in this case to use an additional, degenerate spatial axis to provide equatorial coordinates (RA, Dec) at all spatial positions in a long-slit spectrum. Consult MAST staff for details.)
* Spectral image cubes (sometimes called  _**hyperspectral cubes**_), where the arrays have one spectral and two spatial axes. In this case the WCS is commonly characterized with a function rather than a separate, tabulated array (in a separate extension). The concomitant data are stored in separate extensions.
* Spectral time series, with a dispersion axis and a temporal axis. The spectral coordinate is commonly characterized with a function; the time coordinate may also be included in the WCS if the temporal sampling is regular.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra", "Header 3": "Descriptions of spectra"} -->
Consider the following organizational strategies:
* **Concomitant data:** Put pixel-level arrays of error/uncertainty, data quality flags, data quality, etc. in separate columns within the same extension.  
* Use suggestive column names, e.g. `FLUX`, `WAVELENGTH`, `ERR`, `DQ`, `WEIGHT`
* **Constant data:** Scalar, date, or categorical data that vary among spectra should be stored in separate columns. Scalar/categorical data that are common to all spectra in the extension may instead be stored in the extension header. Consult MAST staff for details.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Catalogs"} -->
Source catalogs are commonly stored as binary tables (e.g. FITS BINTABLE extensions), with one row per source and columns to contain various quantities (source name, world coordinates, brightness measurements, errors, etc.). It is critical for users that the fields (columns) be properly annotated with units (where applicable), and also with the Virtual Observatory uniform content descriptors ([Required Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Required+Metadata): [Catalog Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Catalog+Metadata)).
In some cases the catalog data are complex, and can be best expressed as relationships between data in multiple tables. FITS format does not capture such complicated data well; a better choice is

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Metadata within files"} -->
In order for MAST to provide search interfaces for HLSP data, metadata within files needs to specify the _spatial_ , _spectral_ , _temporal_ , and _energy_ coverage of the data product. Metadata must also specify enough provenance and other information for a user to understand the data product. See [Required Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Required+Metadata) for details.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Metadata within files", "Header 3": "Where to store metadata"} -->
For data products stored in FITS files, metadata take the form of header keywords. But which keywords go in which FITS extension? The following advice will help users and applications discover and use important metadata in your products:
* Store metadata that are applicable to every extension in the primary header (PHDU).  
* `DOI`, `HLSPID`, `HLSPLEAD`, `HLSPNAME`, `HLSPVER`, `LICENSE`, `LICENURL` `OBSERVAT`, `TELESCOP`, etc.
* If you have metadata that are required to interpret the data inside extensions, store these metadata within each such extension; one cannot assume that FITS readers will associate metadata in the primary header with metadata in extension headers.  
* WCS keywords `CD**_i_j_**`,`CRPIX_**j**_`,`CRVAL_**i**_`, RADESYS, WCSAXES, etc.
* Coordinate reference systems: RADESYS, TIMESYS
* Store metadata that document the various products that were combined to make the final product in a separate BINTABLE extension, with EXTNAME= 'PROVENANCE'. See [Provenance Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Provenance+Metadata) for details.  
The required metadata should also appear in data files that are not in FITS format (such as ASCII or ASDF), but the form that they take may differ.
It is important to update metadata for combined products, and to delete metadata that are no longer applicable. For example, keywords such as DATE-OBS may be inherited from files that contribute to a product, in which case the value (if retained) should reflect the date of the first observation.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Metadata within files", "Header 3": "Units"} -->
Units are specified in data files with ASCII strings, and appear in FITS header keywords such as BUNIT (in image extensions) and TUNIT (for columns in table extensions). They are composed of a set of unit substrings; the concept of unit substrings is defined in the `erg/cm^2/s`" or "`erg cm-2 s-1`" rather than "`erg*cm**(-2)*s**(-1)`". Group substrings with parentheses in cases where necessary to clarify the meaning. A few common unit strings and our recommended FITS-style expressions are given in the table below; for additional examples of allowed units see Sect 2.4 of
Quantity | Unit String | Meaning
---|---|---
plane angle | `deg` | degree of arc
`arcsec` | second of arc, 1/3600 deg
`mas` | milli-second of arc, 1/3600000 deg
flux density | `erg/cm^2/s/Angstrom` | erg cm-2 s-1 Å-1
Jy | jansky
mag | (stellar) magnitude
event | adu | analog-to-digital unit
electron | count of electrons†
`ct` or `count` | count
`ph` or `photon` | photon
length | `AU` | astronomical unit
`pc` | parsec
mass rate | `solMass/yr` | solar mass per year
surface brightness | `MJy/sr` | mega-jansky per steradian
`mag/arcsec^2` | magnitude per square arcsecond
time | d | day
s | second
yr | Julian year
†Counts in units of electrons does not appear in standards documents, but is nevertheless widely used.
Use standard scientific prefixes for (sub)multiples of quantities, e.g., `kpc` (kilo-parsec), Mpc (mega-parsec), `mmag` (milli-magnitude), and `uJy` (micro-Jansky).
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* IVOA  
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
Often there are multiple reasonable ways to organize science data within files, and files within an HLSP collection. This article provides advice and some best practices to make the process of incorporating your data in MAST go smoothly.
**On this page...**
* 1[File Organization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-FileOrganization)
* 2[Data Organization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-DataOrganization)
* 2.1[Images](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Images)
* 2.2[Spectra](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Spectra)
* 2.3[Catalogs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Catalogs)
* 2.4[Metadata within files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-Metadatawithinfiles)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/246975891/Organizing+the+Collection#OrganizingtheCollection-ForFurtherReading...)

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "File Organization"} -->
The best organization for files delivered to MAST for an HLSP collection depends mostly upon the number of files, and secondarily on the nature of the products. For small collections consisting of perhaps a few dozen files: it is acceptable to put all files in a single directory. For larger collections it may be better to organize the files in a directory tree, with subfolders named (for instance) by target or field identifier. If organizing by some directory structure, please keep files that apply to the full collection (i.e., the README, the project summary for the Web home page, etc.) in the root directory so that MAST staff can locate them easily.
If you are uploading products for a new data release (new and/or updated products), please place them in a sub-folder of the delivery area, with a name like "/dr2" to indicates the data release ID associated with those products.
The arrangement of files into a directory tree is mostly for the convenience of the contributing team in preparing the collection, and the MAST team in validating and moving the products to our mass storage devices. The presentation of the collection products in MAST interfaces (e.g., the Portal) does not depend upon the submitted file structure.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Data Organization"} -->
There is typically more than one reasonable way to organize data within or among files. In the absence of community standards, the following guidelines will help to ensure that users can:
* retrieve data from MAST without technical problems
* use the products with widely available community tools
* identify the various components of data products (e.g., science vs. error arrays) easily  
While many of the guidelines in the following subsections for science data are described in the context of

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Images"} -->
For organizing data within images, consider the following strategies:
* **Concomitant data:** Put pixel-level arrays of error/uncertainty, data quality flags, exposure maps, etc. in the same file with the science arrays.  
* For image data, put the science array in a FITS **image extension** that includes the keyword EXTNAME = SCI, and put concomitant data in additional extensions with appropriate extension names like "`ERR`", "`DQ`", "`EXP_MAP`", and "`WEIGHT`".
* If data are placed in FITS extensions, do not place any data in the Primary header-data unit (PHDU).
* **File size:** While there is no hard upper-limit, it is often best to keep the size of individual files under about 1 GB. This will facilitate downloads for users with poor internet connectivity. This advice may be at odds with storing concomitant data in the same file as the science pixels; if so, consider storing concomitant data in separate files if doing so doesn't unduly increase the complexity of the file organization.  
* Be sure that the data types of your arrays are consistent with the required precision. For example, 64-bit floating point precision is rarely needed for any quantity other than values of coordinates or timestamps. Similarly, data quality masks may require only 16-bit (short integer) precision.
* **Null data:** Try to avoid creating arrays with large numbers of missing or null pixels. For combined images, this may be as simple as choosing an orientation for the combined array that naturally captures the footprints of all contributing images with minimal dead area; the world coordinate system (WCS) keywords will let downstream applications know the physical orientation without wasting memory.
* **Image maps:** if you have created multiple spatial maps of physical quantities for a given target (e.g., reddening, temperature, star formation rate) for a given target, consider putting them in image extensions within a single file. This will keep information about each target together, and also make it easier to follow the [file naming requirements](https://outerspace.stsci.edu/display/MASTDOCS/File+Naming+Convention).

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra"} -->
There are two main approaches to storing spectra in files: in images or in tables. Here, spectral data includes pixel-level science and concomitant data, including arrays of: flux(density), uncertainty, data quality (DQ) flags, weights, and wavelength (if tabulated).
Science-ready spectra have a variety of types, including
* Spectral image cubes, such as those generated with IFUs, stored as cubes with one dispersion axis and two spatial axes
* Long-slit spectra, with one dispersion and one spatial axis
* Time-series spectra, with one dispersion and one temporal axis  
HSLP contributors may wish to provide more than one type of spectrum, e.g., long-slit and a reference 1-D extraction. It is generally better to provide separate types of products in separate files.
The strategies for arranging data are summarized below.

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra", "Header 3": "Spectra in tables"} -->
Two of the most common community conventions for storing one-dimensional extracted spectra in FITS files are:
1. One spectrum per BINTABLE extension, such that 1-D arrays are stored in separate fields, one (wavelength, flux, err, dq) tuple per row.
2. Multiple spectra per BINTABLE extension, with one spectrum per table row. In this case each cell of (wavelength, flux, err, dq) contains an array of the same length.  
A variation on the above options is to express the wavelength array with a function in FITS keywords. If every spectrum in an extension has the same wavelength array, you can use single-valued WCS keywords to describe the function. If the WCS function changes as a function of row in a BINTABLE, you can expand these WCS keywords into BINTABLE columns. This strategy works well for simple 1-D spectra, separate orders of echelle spectra, and Multi-object spectra (from MOS spectrograms of separate targets in a small field of view). Multi-dimensional spectra can also be stored in tables, but it becomes more complicated to describe the WCS in a compact way.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra", "Header 3": "Spectra in images"} -->
Many spectra derive from spectrograms that are multi-dimensional, where the other dimension(s) may be spatial or temporal. These data are sometimes represented as images with two or more dimensions; the dispersion is most commonly expressed as a function, rather than tabulated in a separate array. Examples include:
* Long-slit spectra are stored as images with one dispersion and one spatial (cross-dispersion) axis. (Note: it is possible in this case to use an additional, degenerate spatial axis to provide equatorial coordinates (RA, Dec) at all spatial positions in a long-slit spectrum. Consult MAST staff for details.)
* Spectral image cubes (sometimes called  _**hyperspectral cubes**_), where the arrays have one spectral and two spatial axes. In this case the WCS is commonly characterized with a function rather than a separate, tabulated array (in a separate extension). The concomitant data are stored in separate extensions.
* Spectral time series, with a dispersion axis and a temporal axis. The spectral coordinate is commonly characterized with a function; the time coordinate may also be included in the WCS if the temporal sampling is regular.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Spectra", "Header 3": "Descriptions of spectra"} -->
Consider the following organizational strategies:
* **Concomitant data:** Put pixel-level arrays of error/uncertainty, data quality flags, data quality, etc. in separate columns within the same extension.  
* Use suggestive column names, e.g. `FLUX`, `WAVELENGTH`, `ERR`, `DQ`, `WEIGHT`
* **Constant data:** Scalar, date, or categorical data that vary among spectra should be stored in separate columns. Scalar/categorical data that are common to all spectra in the extension may instead be stored in the extension header. Consult MAST staff for details.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Catalogs"} -->
Source catalogs are commonly stored as binary tables (e.g. FITS BINTABLE extensions), with one row per source and columns to contain various quantities (source name, world coordinates, brightness measurements, errors, etc.). It is critical for users that the fields (columns) be properly annotated with units (where applicable), and also with the Virtual Observatory uniform content descriptors ([Required Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Required+Metadata): [Catalog Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Catalog+Metadata)).
In some cases the catalog data are complex, and can be best expressed as relationships between data in multiple tables. FITS format does not capture such complicated data well; a better choice is

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Metadata within files"} -->
In order for MAST to provide search interfaces for HLSP data, metadata within files needs to specify the _spatial_ , _spectral_ , _temporal_ , and _energy_ coverage of the data product. Metadata must also specify enough provenance and other information for a user to understand the data product. See [Required Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Required+Metadata) for details.

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Metadata within files", "Header 3": "Where to store metadata"} -->
For data products stored in FITS files, metadata take the form of header keywords. But which keywords go in which FITS extension? The following advice will help users and applications discover and use important metadata in your products:
* Store metadata that are applicable to every extension in the primary header (PHDU).  
* `DOI`, `HLSPID`, `HLSPLEAD`, `HLSPNAME`, `HLSPVER`, `LICENSE`, `LICENURL` `OBSERVAT`, `TELESCOP`, etc.
* If you have metadata that are required to interpret the data inside extensions, store these metadata within each such extension; one cannot assume that FITS readers will associate metadata in the primary header with metadata in extension headers.  
* WCS keywords `CD**_i_j_**`,`CRPIX_**j**_`,`CRVAL_**i**_`, RADESYS, WCSAXES, etc.
* Coordinate reference systems: RADESYS, TIMESYS
* Store metadata that document the various products that were combined to make the final product in a separate BINTABLE extension, with EXTNAME= 'PROVENANCE'. See [Provenance Metadata](https://outerspace.stsci.edu/display/MASTDOCS/Provenance+Metadata) for details.  
The required metadata should also appear in data files that are not in FITS format (such as ASCII or ASDF), but the form that they take may differ.
It is important to update metadata for combined products, and to delete metadata that are no longer applicable. For example, keywords such as DATE-OBS may be inherited from files that contribute to a product, in which case the value (if retained) should reflect the date of the first observation.

<!-- CHUNK 23 END -->

<!-- CHUNK 24 START -->
<!-- Metadata: {"Header 1": "Data Organization", "Header 2": "Metadata within files", "Header 3": "Units"} -->
Units are specified in data files with ASCII strings, and appear in FITS header keywords such as BUNIT (in image extensions) and TUNIT (for columns in table extensions). They are composed of a set of unit substrings; the concept of unit substrings is defined in the `erg/cm^2/s`" or "`erg cm-2 s-1`" rather than "`erg*cm**(-2)*s**(-1)`". Group substrings with parentheses in cases where necessary to clarify the meaning. A few common unit strings and our recommended FITS-style expressions are given in the table below; for additional examples of allowed units see Sect 2.4 of
Quantity | Unit String | Meaning
---|---|---
plane angle | `deg` | degree of arc
`arcsec` | second of arc, 1/3600 deg
`mas` | milli-second of arc, 1/3600000 deg
flux density | `erg/cm^2/s/Angstrom` | erg cm-2 s-1 Å-1
Jy | jansky
mag | (stellar) magnitude
event | adu | analog-to-digital unit
electron | count of electrons†
`ct` or `count` | count
`ph` or `photon` | photon
length | `AU` | astronomical unit
`pc` | parsec
mass rate | `solMass/yr` | solar mass per year
surface brightness | `MJy/sr` | mega-jansky per steradian
`mag/arcsec^2` | magnitude per square arcsecond
time | d | day
s | second
yr | Julian year
†Counts in units of electrons does not appear in standards documents, but is nevertheless widely used.
Use standard scientific prefixes for (sub)multiples of quantities, e.g., `kpc` (kilo-parsec), Mpc (mega-parsec), `mmag` (milli-magnitude), and `uJy` (micro-Jansky).
* * *

<!-- CHUNK 24 END -->

<!-- CHUNK 25 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* IVOA  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 25 END -->

