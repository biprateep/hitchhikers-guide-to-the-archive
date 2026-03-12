---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention"
date_accessed: "2026-03-11T11:34:46.144778"
---

<!-- CHUNK 1 START -->
Flies in HLSP collections must follow the naming convention described here. This convention facilitates ingestion of the collection into MAST, and helps to enable automated searches.
**On this page...**
* 1[HLSP File Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-HLSPFileNames)
* 1.1[Character set](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Characterset)
* 1.2[Directory structure](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Directorystructure)
* 1.3[File name fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Filenamefields)
* 1.4[Recommendations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Recommendations)
* 2[Example File Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-ExampleFileNames)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "HLSP File Names"} -->
The names for science products and ancillary files in HLSP collections must comply with the guidance offered here to enable the files to be ingested into MAST databases, and to enable MAST services to locate them among the billions of files in MAST. Filenames are best if users can tell with some certainty the semantic content of a file from the name. For these reasons HLSP filenames:
* must be unique within a collection
* must use a restricted character set
* must be limited in overall length
* must contain certain metadata within the name, in a structured way  
To support these goals, HLSP filenames (with the exception of README files) are composed of 9 sub-strings called _**fields**_ , separated by underscores. Certain fields may be further sub-divided into sub-strings called _**elements**_ , separated by hyphens. Specific guidance is offered in the subsections below.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "Character set"} -->
File names must be composed of a limited character set, and are restricted in length.
* All filenames must be composed only of lower-case ASCII alphanumeric characters (`**a-z,0-9**`), plus the following special characters:
* underscore ( `**_**`), but only to separate fields within filenames
* hyphen ( `**-**`), to separate elements within fields, and as a part of target names
* period ( `**.**`), which is permitted within the target field, the version ID and as a field separator for the file extension
* plus sign ( `**+**`), which is only permitted within the target field
* Most fields must begin with a lower-case letter (`**a-z**`), except as noted in the table below
* Each field has a maximum length, however overall filenames should be limited in length to no more than 90 characters

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "Directory structure"} -->
For collections of more than a few dozen files, it would help for them to be organized into folders. The specific organization is up to the contributing team, but the sub-folder names must:
* consist of only lower-case alphnumeric characters (`**a-z,0-9**`)
* may also contain underscores and hyphens, except as the first or last character
* be limited in length to 20 characters  
The structure supplied by the team is primarily used to facilitate review and characterization of collection files prior to ingest. Note that MAST may or may not use the directory structure provided by the team to organize files in the archive mass storage system, or to represent files in any user interface.
Where applicable, it often speeds up the ingest of particularly complex collections if files, corresponding to an observation of a target in space and time with a particular instrument and optical element, are grouped together underneath a higher-level directory representing that observation.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "File name fields"} -->
File names are composed of 9 _**fields**_ , separated by underscores (the exception being the collection README file, which need only have fields 1, 2, 8, and 9 listed below). Certain fields may be sub-divided into _**elements**_ , separated by dashes. The name template is shown below, where characters in**black bold** _green italic_ text are symbolic, and are explained in the table below.
`**hlsp_**_proj-id_**_**_observatory_**_**_instrument_**_**_target_**_**_opt-elem_**_**_version_**_**_product-type_**.**_extension_`
Where the components, in order, are:  
| Component | Max Chars | Description | Examples
---|---|---|---|---
1 | **`hlsp`**|  4**
** | A literal string that identifies the file as a community-contributed data product |  
2 | `proj-id``
` | 20
|  An agreed upon acronym or initializm for the HLSP collection. This name is also used in MAST as a directory name and as a database keyword.
* This field may contain a hyphen  
| `wide`
3 | `observatory` | 20
|  Observatory or mission used to acquire the data, or for which the data were simulated.
* May include multiple elements If multiple observatories were used  
|  `hst-iue`, `galex`, `jwst`  
4 | `instrument` | 20
|  Name of Instrument used to obtain the data, or for which the data were simulated.
* May include multiple elements if multiple instruments were used
* When not applicable (e.g. for GALEX data), use a descriptive tag like`img``spec`  
| `nircam`, `cos-stis`
5 | `target` | 30
|  Field name or target as designated by the team, or as a general identifier where a specific target designation is not relevant. Parts, counter numbers, and epochs are allowed in this field and should be separated by hyphens. Counters can be used, e.g., when the same field is observed multiple times with the same observing parameters.
* May include hyphen, period, and plus sign
* If multiple observing epochs apply, please append a hyphenated suffix (beginning with the literal**`ep,`**
* For parts and counters, leading zeros are required if more than one digit is needed (e.g. for 17 exposures ofm101, each file has field-name as follows:`m101-01`, `m101-02` ... `m101-17`; the same approach applies to epochs).  
Please describe your usage of target/general parts and counters within the collection README file. |  m57, m101-ep1, m101-ep2  
6 | `opt-elem` | 20
|  Names of optical element(s) (i.e., filter or disperser) used to obtain the data.
* May include field elements if multiple filters/dispersers were used
* Clear or empty filter elements need not be included  
| `f606w-f814w`
7 | `version` | 9
|  Version designation used by the team for the HLSP delivery, Versions in the filename may relate in some way to data release or software versions, but ultimately they must represent the version of a file, and must be incremented with any delivery that replaces that file. The value must begin with the literal "v" and contain an alphanumeric value, with the syntax `**v**X[.Y[.Z]]` where X and Y are numeric values with up to 2 digits, X cannot have a leading zero, and Z is alphanumeric (**`a-z,0-9`**) up to 2 characters. | `v2`, v1.2.2a
8 | `product-type` | 16
|  Type of data as designated by the team (models/simulations can be indicated here). Use a widely recognized type. Be sure to distinguish products of similar type, possibly by using a simple compound type. e.g., a photometric catalog (`phot-cat`) vs. a catalog of simulated object morphologies (`sim-cat`).  
* hyphens are allowed for compound product types  
| `img`, `cat`, `drz`, `lc`, `model-spec`, `sci`, `wht`, `sim``-img`, `map`
9 | `extension` | 8
| Standard extension name for the file format, which must include standard notation for compression if applicable | `.asdf`, `.txt`., `.md`, `.png`, `.fits`, `.fits.gz`

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "Recommendations"} -->
* Version numbers can be specific to the project. Teams should use increasing version numbers to make it easy to tell which data are superseded; MAST will _not_ keep older versions of datasets unless the team demonstrates a need for it.  
* If your collection involves a time-domain component, this should be reflected in the _**target**_ field (rather than in the _**version**_ field), using suffix of the form **ep-NN** as noted above. Contributors should take special care to explain time-dependent aspects of their collections in the README file.
* Re-delivered data should contain both the re-processed data along with the single-epoch data associated with these products, if applicable.
* All images identified using the same target name should cover approximately the same area of the sky. If there are multiple images covering different parts of a region or source, their target field values should have appended elements indicating the different parts..

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Example File Names"} -->
A drizzle-combined image of the GOODS field, obtained with the HST/ACS camera WFC channel using the F435W filter:
* `hlsp_goods_hst_acs-wfc_north-sect13_f435w_v2.0_drz.fits`  
An image of the Hubble ultra-deep field obtained with the HST/NICMOS NIC3 camera using the F110W filter:
* `hlsp_udf_hst_nicmos-nic3_treasury_f110w_v2_img.fits`  
A text catalog from the 47 Tuc from the DEEP47TUC survey obtained with HST/ACS, containing stellar magnitudes in the F606W and F814W filters:
* `hlsp_deep47tuc_hst_acs_47tuc_f606w-f814w_v1_cat.txt`  
A combined spectrum with different observatories, instruments, gratings and cenwave positions all abutted, of the target AV-16 from the ULLYSES survey, obtained with HST/STIS and FUSE. Note that the opt-elem field is shortened to uv-opt, rather than list the more than 8 individual elements:
* `hlsp_ullyses_hst-fuse_fuse-stis_av-16_uv-opt_dr7_preview-spec.fits`

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Collection Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290404/Collection+Contents)
* [File Types, Formats, Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content)  
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
Flies in HLSP collections must follow the naming convention described here. This convention facilitates ingestion of the collection into MAST, and helps to enable automated searches.
**On this page...**
* 1[HLSP File Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-HLSPFileNames)
* 1.1[Character set](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Characterset)
* 1.2[Directory structure](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Directorystructure)
* 1.3[File name fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Filenamefields)
* 1.4[Recommendations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-Recommendations)
* 2[Example File Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-ExampleFileNames)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention#FileNamingConvention-ForFurtherReading...)

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "HLSP File Names"} -->
The names for science products and ancillary files in HLSP collections must comply with the guidance offered here to enable the files to be ingested into MAST databases, and to enable MAST services to locate them among the billions of files in MAST. Filenames are best if users can tell with some certainty the semantic content of a file from the name. For these reasons HLSP filenames:
* must be unique within a collection
* must use a restricted character set
* must be limited in overall length
* must contain certain metadata within the name, in a structured way  
To support these goals, HLSP filenames (with the exception of README files) are composed of 9 sub-strings called _**fields**_ , separated by underscores. Certain fields may be further sub-divided into sub-strings called _**elements**_ , separated by hyphens. Specific guidance is offered in the subsections below.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "Character set"} -->
File names must be composed of a limited character set, and are restricted in length.
* All filenames must be composed only of lower-case ASCII alphanumeric characters (`**a-z,0-9**`), plus the following special characters:
* underscore ( `**_**`), but only to separate fields within filenames
* hyphen ( `**-**`), to separate elements within fields, and as a part of target names
* period ( `**.**`), which is permitted within the target field, the version ID and as a field separator for the file extension
* plus sign ( `**+**`), which is only permitted within the target field
* Most fields must begin with a lower-case letter (`**a-z**`), except as noted in the table below
* Each field has a maximum length, however overall filenames should be limited in length to no more than 90 characters

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "Directory structure"} -->
For collections of more than a few dozen files, it would help for them to be organized into folders. The specific organization is up to the contributing team, but the sub-folder names must:
* consist of only lower-case alphnumeric characters (`**a-z,0-9**`)
* may also contain underscores and hyphens, except as the first or last character
* be limited in length to 20 characters  
The structure supplied by the team is primarily used to facilitate review and characterization of collection files prior to ingest. Note that MAST may or may not use the directory structure provided by the team to organize files in the archive mass storage system, or to represent files in any user interface.
Where applicable, it often speeds up the ingest of particularly complex collections if files, corresponding to an observation of a target in space and time with a particular instrument and optical element, are grouped together underneath a higher-level directory representing that observation.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "File name fields"} -->
File names are composed of 9 _**fields**_ , separated by underscores (the exception being the collection README file, which need only have fields 1, 2, 8, and 9 listed below). Certain fields may be sub-divided into _**elements**_ , separated by dashes. The name template is shown below, where characters in**black bold** _green italic_ text are symbolic, and are explained in the table below.
`**hlsp_**_proj-id_**_**_observatory_**_**_instrument_**_**_target_**_**_opt-elem_**_**_version_**_**_product-type_**.**_extension_`
Where the components, in order, are:  
| Component | Max Chars | Description | Examples
---|---|---|---|---
1 | **`hlsp`**|  4**
** | A literal string that identifies the file as a community-contributed data product |  
2 | `proj-id``
` | 20
|  An agreed upon acronym or initializm for the HLSP collection. This name is also used in MAST as a directory name and as a database keyword.
* This field may contain a hyphen  
| `wide`
3 | `observatory` | 20
|  Observatory or mission used to acquire the data, or for which the data were simulated.
* May include multiple elements If multiple observatories were used  
|  `hst-iue`, `galex`, `jwst`  
4 | `instrument` | 20
|  Name of Instrument used to obtain the data, or for which the data were simulated.
* May include multiple elements if multiple instruments were used
* When not applicable (e.g. for GALEX data), use a descriptive tag like`img``spec`  
| `nircam`, `cos-stis`
5 | `target` | 30
|  Field name or target as designated by the team, or as a general identifier where a specific target designation is not relevant. Parts, counter numbers, and epochs are allowed in this field and should be separated by hyphens. Counters can be used, e.g., when the same field is observed multiple times with the same observing parameters.
* May include hyphen, period, and plus sign
* If multiple observing epochs apply, please append a hyphenated suffix (beginning with the literal**`ep,`**
* For parts and counters, leading zeros are required if more than one digit is needed (e.g. for 17 exposures ofm101, each file has field-name as follows:`m101-01`, `m101-02` ... `m101-17`; the same approach applies to epochs).  
Please describe your usage of target/general parts and counters within the collection README file. |  m57, m101-ep1, m101-ep2  
6 | `opt-elem` | 20
|  Names of optical element(s) (i.e., filter or disperser) used to obtain the data.
* May include field elements if multiple filters/dispersers were used
* Clear or empty filter elements need not be included  
| `f606w-f814w`
7 | `version` | 9
|  Version designation used by the team for the HLSP delivery, Versions in the filename may relate in some way to data release or software versions, but ultimately they must represent the version of a file, and must be incremented with any delivery that replaces that file. The value must begin with the literal "v" and contain an alphanumeric value, with the syntax `**v**X[.Y[.Z]]` where X and Y are numeric values with up to 2 digits, X cannot have a leading zero, and Z is alphanumeric (**`a-z,0-9`**) up to 2 characters. | `v2`, v1.2.2a
8 | `product-type` | 16
|  Type of data as designated by the team (models/simulations can be indicated here). Use a widely recognized type. Be sure to distinguish products of similar type, possibly by using a simple compound type. e.g., a photometric catalog (`phot-cat`) vs. a catalog of simulated object morphologies (`sim-cat`).  
* hyphens are allowed for compound product types  
| `img`, `cat`, `drz`, `lc`, `model-spec`, `sci`, `wht`, `sim``-img`, `map`
9 | `extension` | 8
| Standard extension name for the file format, which must include standard notation for compression if applicable | `.asdf`, `.txt`., `.md`, `.png`, `.fits`, `.fits.gz`

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "HLSP File Names", "Header 2": "Recommendations"} -->
* Version numbers can be specific to the project. Teams should use increasing version numbers to make it easy to tell which data are superseded; MAST will _not_ keep older versions of datasets unless the team demonstrates a need for it.  
* If your collection involves a time-domain component, this should be reflected in the _**target**_ field (rather than in the _**version**_ field), using suffix of the form **ep-NN** as noted above. Contributors should take special care to explain time-dependent aspects of their collections in the README file.
* Re-delivered data should contain both the re-processed data along with the single-epoch data associated with these products, if applicable.
* All images identified using the same target name should cover approximately the same area of the sky. If there are multiple images covering different parts of a region or source, their target field values should have appended elements indicating the different parts..

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Example File Names"} -->
A drizzle-combined image of the GOODS field, obtained with the HST/ACS camera WFC channel using the F435W filter:
* `hlsp_goods_hst_acs-wfc_north-sect13_f435w_v2.0_drz.fits`  
An image of the Hubble ultra-deep field obtained with the HST/NICMOS NIC3 camera using the F110W filter:
* `hlsp_udf_hst_nicmos-nic3_treasury_f110w_v2_img.fits`  
A text catalog from the 47 Tuc from the DEEP47TUC survey obtained with HST/ACS, containing stellar magnitudes in the F606W and F814W filters:
* `hlsp_deep47tuc_hst_acs_47tuc_f606w-f814w_v1_cat.txt`  
A combined spectrum with different observatories, instruments, gratings and cenwave positions all abutted, of the target AV-16 from the ULLYSES survey, obtained with HST/STIS and FUSE. Note that the opt-elem field is shortened to uv-opt, rather than list the more than 8 individual elements:
* `hlsp_ullyses_hst-fuse_fuse-stis_av-16_uv-opt_dr7_preview-spec.fits`

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Collection Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290404/Collection+Contents)
* [File Types, Formats, Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 15 END -->

