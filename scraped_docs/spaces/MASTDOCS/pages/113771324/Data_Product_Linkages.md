---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages"
date_accessed: "2026-03-11T11:33:20.161922"
---

<!-- CHUNK 1 START -->
General users of JWST data may initially be concerned with only the most calibrated, combined science data products for a given target. Yet many other products are important to developing a full understanding the science data. This article summarizes the relationships between the science vs. other products, and their representation in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html).
**On this page...**
* 1[Relationships Among Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-RelationshipsAmongDataProducts)
* 1.1[Associations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-Associations)
* 1.2[Linked Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-LinkedDataProducts)
* 1.3[Contributing Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-ContributingProducts)
* 2[Minimum Recommended Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products"} -->
Many different data products, often hundreds or even thousands, contribute to the construction of a small set of high-level, most-combined JWST science products. They are all connected within MAST to one or more primary _**Observations,**_ which are displayed as single rows in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) results table. Users should be aware how all of these data products are related to the final Science products. This article describes the nature of these relationships; the article [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) provides a visual representation of how they are represented in the [Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) user interface.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations"} -->
The term [JWST Data Associations](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview#JWSTScienceDataOverview-assocAssociations) for more information. Here are informal descriptions of the types of relationships that are included in associations:

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Prerequisite"} -->
The products in this relationship support the proper execution of the science observations on the spacecraft, or provide evidence that observations were executed as planned. They do not contribute to science data processing.
* [Pre-image](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-operations/nirspec-mos-operations/nirspec-mos-operations-pre-imaging-using-nircam#gsc.tab=0) (if obtained as a part of the program)
* Confirmation image

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Antecedent"} -->
The input products for a stage of the pipeline are related to output products by a parent-child relationship. That is, Level-1b products for a given program, observation, visit, detector, and exposure are _antecedents_ for their corresponding Level-2a products; L-2a are antecedents for L-2b, and so on. (See the [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) article for information about product levels.) In addition, the association definition files are themselves required to specify the output child products.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Composition"} -->
Level-2b products, or the output of Stage 2 processing, are the final, calibrated science products _per-exposure_. Further processing by the Stage-3 pipeline produces L-3 products per _source_ or _target_ by combining L-2b products in a way that depends on the instrument configuration. That is, L-3 products for a given source or target are _composed of_ L-2b exposure-level products. Here are examples of types of exposures from a given instrument, filter/grating that are [associated](https://jwst-docs.stsci.edu/understanding-jwst-data-files/associations) by composition to form L-3 products:
* All dither positions
* All detectors in a camera
* All mosaic tiles within or among observations in a single program
* All segments of a (lengthy) time-series observation
* All orientations (for coronagraphy)  
See the section __Associations__ in the [JWST Science Data Overview](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview#JWSTScienceDataOverview-assocAssociations) article for an exhaustive list. See the article [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) for a visual representation of associations as viewed from the Portal.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Multiplicity"} -->
Some L-3 spectroscopic products are processed after combination to produce multiple derived products, e.g., one extracted spectrum per target.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Contemporaneous Calibration"} -->
Some types of calibration observations are obtained as a part of an observation, and near in time to specific science exposures. Contemporaneous calibrations are specific to the instrument configuration and to the specific target, and are used in science calibration processing:
* Arc lamp and flat-field exposures
* Astrophysical background exposures
* Reference PSF exposures in the same program for coronagraphy

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Aggregation"} -->
Some anciliary data products are associated with the Observation, but are not used in the science processing to create the highest-level science products. These include:
* Intermediate products generated during calibration processing
* Guide-star products obtained during guided observations

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Linked Data Products"} -->
Other products are also related to the science observations, though less directly than associated products. They are represented in MAST as _**linked**_ data, and include:
* Contemporaneous guide-star observations
* Micro-shutter Array (MSA) Plan source catalog (NIRSpec only)
* Previews and image cut-outs generated to aid in data visualization within the Portal
* Links to data from other missions (applies to [High-Level Science Products](https://outerspace.stsci.edu/display/MASTDOCS/About+HLSPs), but not currently to standard JWST products)

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products"} -->
The following kinds of data products are neither associated nor linked within MAST, although they do contribute to constructing the highest-level products in an Observation. They can be accessed from the MAST Portal via special mechanisms.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products", "Header 3": "Calibration Reference Files"} -->
Static calibration products are used during pipeline calibration processing to remove some element of the instrumental signature, or are used to specify how output products are to be created from input products. These products are updated periodically to reflect some improvement in the calibration, or to capture a temporal change in a calibration.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products", "Header 3": "Engineering Data"} -->
Engineering data are incorporated as header metadata in science data processing. The engineering data related to a specific exposure or observation are available in the [Engineering Database interface](https://mast.stsci.edu/portal_jwst/Mashup/Clients/JwstEdb/JwstEdb.html).

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products", "Header 3": "External Pre-Images"} -->
Pre-images of a field from an external source (e.g., an HST program) may be contributed by an observer as an astrometric reference for a multi-object spectroscopic observation.
Of the many different data products produced by the calibration pipeline, a subset has been identified as essential for extracting the intended science from the data. These are identified in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) as "minimum recommended products" (MRP). The data products included in this set depends upon the the highest level product that is produced. Generally, products in the MRP include the most calibrated science products (i.e., those for which the instrumental signature has been removed, plus the combined products), but _exclude_ anciliary products.
MRP Checkbox
The MRP checkbox in the **Download Manager** must be de-selected in order to see and select raw or intermediate-level data products, and ancillary products, for retrieval. **Note:** Some L-2b products may also be appropriate for science analysis, but will not be visible if MRP is checked and L-3 products exist.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Associations](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview#JWSTScienceDataOverview-assocAssociations) (JDox)
* Pipeline definition of
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
General users of JWST data may initially be concerned with only the most calibrated, combined science data products for a given target. Yet many other products are important to developing a full understanding the science data. This article summarizes the relationships between the science vs. other products, and their representation in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html).
**On this page...**
* 1[Relationships Among Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-RelationshipsAmongDataProducts)
* 1.1[Associations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-Associations)
* 1.2[Linked Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-LinkedDataProducts)
* 1.3[Contributing Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-ContributingProducts)
* 2[Minimum Recommended Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-MRPMinimumRecommendedDataProducts)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages#DataProductLinkages-ForFurtherReading...)

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products"} -->
Many different data products, often hundreds or even thousands, contribute to the construction of a small set of high-level, most-combined JWST science products. They are all connected within MAST to one or more primary _**Observations,**_ which are displayed as single rows in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) results table. Users should be aware how all of these data products are related to the final Science products. This article describes the nature of these relationships; the article [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) provides a visual representation of how they are represented in the [Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) user interface.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations"} -->
The term [JWST Data Associations](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview#JWSTScienceDataOverview-assocAssociations) for more information. Here are informal descriptions of the types of relationships that are included in associations:

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Prerequisite"} -->
The products in this relationship support the proper execution of the science observations on the spacecraft, or provide evidence that observations were executed as planned. They do not contribute to science data processing.
* [Pre-image](https://jwst-docs.stsci.edu/jwst-near-infrared-spectrograph/nirspec-operations/nirspec-mos-operations/nirspec-mos-operations-pre-imaging-using-nircam#gsc.tab=0) (if obtained as a part of the program)
* Confirmation image

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Antecedent"} -->
The input products for a stage of the pipeline are related to output products by a parent-child relationship. That is, Level-1b products for a given program, observation, visit, detector, and exposure are _antecedents_ for their corresponding Level-2a products; L-2a are antecedents for L-2b, and so on. (See the [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) article for information about product levels.) In addition, the association definition files are themselves required to specify the output child products.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Composition"} -->
Level-2b products, or the output of Stage 2 processing, are the final, calibrated science products _per-exposure_. Further processing by the Stage-3 pipeline produces L-3 products per _source_ or _target_ by combining L-2b products in a way that depends on the instrument configuration. That is, L-3 products for a given source or target are _composed of_ L-2b exposure-level products. Here are examples of types of exposures from a given instrument, filter/grating that are [associated](https://jwst-docs.stsci.edu/understanding-jwst-data-files/associations) by composition to form L-3 products:
* All dither positions
* All detectors in a camera
* All mosaic tiles within or among observations in a single program
* All segments of a (lengthy) time-series observation
* All orientations (for coronagraphy)  
See the section __Associations__ in the [JWST Science Data Overview](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview#JWSTScienceDataOverview-assocAssociations) article for an exhaustive list. See the article [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) for a visual representation of associations as viewed from the Portal.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Multiplicity"} -->
Some L-3 spectroscopic products are processed after combination to produce multiple derived products, e.g., one extracted spectrum per target.

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Contemporaneous Calibration"} -->
Some types of calibration observations are obtained as a part of an observation, and near in time to specific science exposures. Contemporaneous calibrations are specific to the instrument configuration and to the specific target, and are used in science calibration processing:
* Arc lamp and flat-field exposures
* Astrophysical background exposures
* Reference PSF exposures in the same program for coronagraphy

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Associations", "Header 3": "Aggregation"} -->
Some anciliary data products are associated with the Observation, but are not used in the science processing to create the highest-level science products. These include:
* Intermediate products generated during calibration processing
* Guide-star products obtained during guided observations

<!-- CHUNK 23 END -->

<!-- CHUNK 24 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Linked Data Products"} -->
Other products are also related to the science observations, though less directly than associated products. They are represented in MAST as _**linked**_ data, and include:
* Contemporaneous guide-star observations
* Micro-shutter Array (MSA) Plan source catalog (NIRSpec only)
* Previews and image cut-outs generated to aid in data visualization within the Portal
* Links to data from other missions (applies to [High-Level Science Products](https://outerspace.stsci.edu/display/MASTDOCS/About+HLSPs), but not currently to standard JWST products)

<!-- CHUNK 24 END -->

<!-- CHUNK 25 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products"} -->
The following kinds of data products are neither associated nor linked within MAST, although they do contribute to constructing the highest-level products in an Observation. They can be accessed from the MAST Portal via special mechanisms.

<!-- CHUNK 25 END -->

<!-- CHUNK 26 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products", "Header 3": "Calibration Reference Files"} -->
Static calibration products are used during pipeline calibration processing to remove some element of the instrumental signature, or are used to specify how output products are to be created from input products. These products are updated periodically to reflect some improvement in the calibration, or to capture a temporal change in a calibration.

<!-- CHUNK 26 END -->

<!-- CHUNK 27 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products", "Header 3": "Engineering Data"} -->
Engineering data are incorporated as header metadata in science data processing. The engineering data related to a specific exposure or observation are available in the [Engineering Database interface](https://mast.stsci.edu/portal_jwst/Mashup/Clients/JwstEdb/JwstEdb.html).

<!-- CHUNK 27 END -->

<!-- CHUNK 28 START -->
<!-- Metadata: {"Header 1": "Relationships Among Data Products", "Header 2": "Contributing Products", "Header 3": "External Pre-Images"} -->
Pre-images of a field from an external source (e.g., an HST program) may be contributed by an observer as an astrometric reference for a multi-object spectroscopic observation.
Of the many different data products produced by the calibration pipeline, a subset has been identified as essential for extracting the intended science from the data. These are identified in the [MAST Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) as "minimum recommended products" (MRP). The data products included in this set depends upon the the highest level product that is produced. Generally, products in the MRP include the most calibrated science products (i.e., those for which the instrumental signature has been removed, plus the combined products), but _exclude_ anciliary products.
MRP Checkbox
The MRP checkbox in the **Download Manager** must be de-selected in order to see and select raw or intermediate-level data products, and ancillary products, for retrieval. **Note:** Some L-2b products may also be appropriate for science analysis, but will not be visible if MRP is checked and L-3 products exist.

<!-- CHUNK 28 END -->

<!-- CHUNK 29 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Associations](https://jwst-docs.stsci.edu/accessing-jwst-data/jwst-science-data-overview#JWSTScienceDataOverview-assocAssociations) (JDox)
* Pipeline definition of
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 29 END -->

