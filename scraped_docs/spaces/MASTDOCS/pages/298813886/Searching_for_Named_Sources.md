---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources"
date_accessed: "2026-03-11T11:31:40.369304"
---

<!-- CHUNK 1 START -->
This article describes how to make effective searches for data by astrophysical source name, and how avoid problems with the underlying translations from name to sky coordinates.
**On this page...**
* 1[Source Identifiers in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-SourceIdentifiersinMAST)
* 2[Search by source name](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Searchbysourcename)
* 2.1[Name translation](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Nametranslation)
* 2.2[Problem cases](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Problemcases)
* 3[MAST Search Interfaces](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-MASTSearchInterfaces)
* 3.1[Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Portal)
* 3.2[MAST Mission Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-MASTMissionSearch)
* 3.3[MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-MASTAPI)
* 4[Best Practices](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-best_practicesBestPractices)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Source Identifiers in MAST"} -->
Most MAST search interfaces, apart from those specifically devoted to source catalogs, query the MAST archive catalog of **Observations**. Observations are collections of products and metadata related to exposures by a given mission at a given sky position. The archive catalog:
* **is** a database of _**Observations**_ from missions hosted by MAST
* **is _not_** a database of individual astrophysical sources  
Thus, searching MAST for sources (or positions) amounts to querying the archive catalog for Mission data that overlap the astrophysical source position or extent.
Note that these queries apply to _fixed_ astrophysical sources—i.e., not solar system bodies. (See [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST) for non-fixed sources, which uses the term _target_ to describe planned pointings of the telescope.) This article describes how MAST translates searches of positions and source names to queries of matching Observations. The following terms take on a specific meaning for searches of MAST holdings:
Term | Usage
---|---
**Identifier** | **Designation** is the official **identifier**. An astrophysical source may have multiple identifiers (most often this means it is listed in multiple published catalogs), but the key point is that all identifier synonyms refer unambiguously to a _single, unique source_. Any of these names can be **resolved** (i.e., translated) to sky coordinates of the fixed source, provided the name string matches the syntax rules of the resolver service.
**Object** |  Refers to a generic source or field name, which is translated to sky coordinates via MAST or another name resolution service. MAST syntax rules are somewhat more restrictive than SIMBAD.  MAST also uses the term Object to refer to an Observation identifier (a name for a collection of related files, rather than the name of an astrophysical source), which one of the MAST-hosted services can resolve to a spatial position. This conflation of terms can lead to confusion in some contexts.
**Source** | A generic term used in the literature or in MAST documentation to refer to an astrophysical entity. Can refer to (often spatially unresolved) aggregate objects.
**Target** | The name of a target or field associated with an observation by a MAST-hosted mission. The target name is provided by the observer, and may or may not match an official designation. Targets are string-matched to a field in the MAST observation database. See warning below.
Searching by _target name_ in MAST can problematic because:
* it must match exactly to values in the database field, unless wildcard characters are used
* it may or may not match an official designation
* it may or may not match the name given for a different Observation by another observer of the same source or field  
Because of these issues, searches for data by target name may not match every entry in the MAST catalog that one might expect.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Search by source name"} -->
Searches by source name in MAST are translated to searches by sky coordinates using a back-end web service called  _**SANTA**_ (_STScI Archive Name Translation Applications_). SANTA itself depends on multiple name resolution services: the major astronomical name services  _**S**_ et of _**I**_ dentifications, _**M**_ easurements and _**B**_ ibliography for _**A**_ stronomical _**D**_ ata; curated by CDS) and _**N**_ ASA/IPAC _**E**_ xtragalactic _**D**_ atabase), in addition to internal services for identifiers specific to MAST.
NED, as its name implies, contains extensive holdings on extra-Galactic sources. Though their database does contain entries for point-sources, it is not intended to be complete for stars. SIMBAD includes both Galactic and extra-Galactic sources, with excellent completeness on the former. Both services harvest source catalogs in the published literature.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Name translation"} -->
The MAST SANTA service uses coordinates directly, or queries one or more back-end name translation services, or **name resolvers** , to determine source coordinates. The services are searched in the order of the table below until a match is found.
Name resolvers  
| Resolver | Description | Example
---|---|---|---
1 | TIC | MAST translates identifiers from the  | `TIC 52031993`
2 | KEPLER | MAST translates [Kepler](https://archive.stsci.edu/kepler/) identifiers starting with `Kepler`, `Kplr` or `KIC` | `KPLR 757076`
3 | K2 | MAST translates [K2](https://archive.stsci.edu/missions-and-data/k2) identifiers starting with `EPIC`, `K2` or `KTWO` | `EPIC 201124136`
4 | DADS | MAST translates HST IPPPSSOOT observation identifiers, **or partial (IPPPSS) identifiers.**(Searches for HLA products work similarly, except that the **`hst_`**prefix must be omitted.) Note that these translations are from Observations to coordinates, rather than source identifier to coordinates. |  `ocr7jkOaq,` `j91k10` `10188_10`
5 | EXO | MAST translates [Exoplanet](https://exo.mast.stsci.edu/) identifiers, including TESS Target of Interest (TOI) identifiers | `TOI 172 b`
6 | SIMBAD | Name resolver at CDS |  
7 | SIMBAD/CfA | Mirror of SIMBAD service at CfA/Harvard |  
8 | NED | Uses the  |  
The order is fixed, and MAST applications do not currently offer users the option to specify an alternative name resolver, except when using the SANTA service directly.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases"} -->
There are cases where the returned coordinates differ between SIMBAD and NED, though the coordinates usually agree to within 0.25 arcsec among services. But there are many cases where the returned coordinates between SIMBAD and NED are quite discrepant. These cases fall into a few categories.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases", "Header 3": "Imprecise source specification"} -->
There are cases where source identifiers (expressed in ASCII text) for different objects are very similar, but refer to very different astrophysical sources. Examples include:
Imprecise source names
The designation for the name **`mu eri`**which is interpreted as a different star in each resolver. This illustrates the need to pay strict attention to the specialized naming conventions in SIMBAD and NED.
Designation | Notes |  ASCII Identifier | Resolver | RA(J2000) | Dec(J2000)
---|---|---|---|---|---
**µ Eri** | Bright star with a Bayer designation |  **`* mu. eri`**`**mu eri**` | SIMBAD | `4:45:30.15` | `-3:15:16.777`
**`muu eri`**|  NED
**MU Eri** | Variable star | **`V* mu eri`**|  SIMBAD | `2:48:10.566` | `-15:18:04.03`
**`mu eri`**|  NED
Since the SANTA resolver defaults to SIMBAD, searching for the name **`mu eri`**will return observations matching the source**μ Eri.** Note that SIMBAD follows a number of naming conventions, including:
**`*^`**indicates what follows the asterisk (plus blank space) is a star name
`**V*^**`indicates what follows is a variable star name
See the

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases", "Header 3": "Ambiguous names"} -->
Names of sources can be ambiguous for a resolver service, or the name can be conflated by the service. Examples include:
Ambiguous source names
#### Popular names
Popular names are resolved by searching a "name" database table to match a more formal catalog designation; the match is not guaranteed to be the same in different name resolver services. For example, the name **`ophiuchus`**is interpreted by SIMBAD as the Ophiuchus molecular cloud, a Galactic star forming region. NED interprets it as the Ophiuchus cluster of galaxies. These sources are about 10° apart on the sky. Similarly, SIMBAD interprets the name**`taurus`**as the
#### Name Overloading
A search for the name **`Arp 2`**in SIMBAD returns the coordinates for a Galactic globular cluster, but NED returns the coordinates for a galaxy with the canonical name UGC 10310. These sources are 84° apart on the sky.
#### M 51
This source in the Messier catalog (published 1784) refers to two sources in the NGC (first published in 1888): SIMBAD returns the position of the bright spiral galaxy NGC 5194, rather than the companion NGC 5195. NED adopts a mean position. From the NED documentation:
_"M51" refers to the pair of galaxies, NGC 5194 and NGC 5195, not just to the larger spiral NGC 5194. The position that NED adopts for M51 is therefore the mean position of the two galaxies. We treat other pairs, triplets, groups, and clusters listed in NED the same way: we adopt mean positions for all the galaxies rather than for just the brightest or for the most centrally-located._

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases", "Header 3": "Angularly large sources"} -->
The exact center of certain extended sources can be uncertain. Examples include:
Large sources
#### IC 2118
SIMBAD and NED both resolve to the same canonical name (NGC 1909), but the coordinates differ by nearly a degree. The source is an extended reflection nebula, and the coordinates are derived from separate catalogs. The coordinates returned by SIMBAD appear to be approximate (i.e., the precision is one-tenth of a degree).
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces"} -->
Searches by source name may be executed with one of the MAST web user interfaces, with user-written software by calling an API, or by using the [SANTA interface](https://mastresolver.stsci.edu/Santa-war/) directly. Note that MAST does not support the full syntax allowed by SIMBAD, and in particular partial identifiers with wildcards are not allowed in source names. Spaces in source names, including between the catalog abbreviation and the member number, are allowed but often not necessary in MAST.
An important feature of these interfaces is the ability to specify a **search radius** , that is, the radius of a circle centered on the resolved coordinate that will produce matches with MAST observations that overlap the circle. (These are often called **cone searches** , in reference to the linearly growing size of the implied physical radius with distance to the source.) If no radius is specified, a default will be used. Keep the following in mind for cone searches:
* The default for point-sources is 0.2 deg, but may be increased dynamically in the search if the source angular size (as recorded in SIMBAD or NED) is larger.
* The search results will include all data for which any part of the observing aperture overlaps the search cone.
* The observing aperture is just the extent of a (possibly composite) image, or the slit of a spectrograph. The projection of the aperture boundaries onto the sky is often called the observation **footprint**.**
**
* **Note:** any portion of a footprint that overlaps the search cone will be matched, whether the image actually includes the source or not.
* Use a search radius of r=0 to match only data that overlap that exact location in the sky.
* This is often best when searching for small or unresolved sources, provided the source does not have high proper motion.  
For some very large sources where MAST-hosted missions have made many observations, the returned results may be quite large. For M31, the default search radius is over 1.6 deg, which currently matches nearly a quarter-million observations. In such cases you may find the query times out (yielding no results at all, and hanging the application), or you may find it impossible to do anything with the results, such as load rows into the download basket. See [Best Practices](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-best_practices) below.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces", "Header 2": "Portal"} -->
The MAST [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) enables searches for sources in two ways, summarized below. See the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) chapter [Basic Search](https://outerspace.stsci.edu/display/MASTDOCS/Basic+Search) for formatting and other details.
![](https://outerspace.stsci.edu/download/attachments/298813886/dialog_PortalSearch.png?version=1&modificationDate=1740421076302&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/298813886/filter_m57.png?version=1&modificationDate=1739303900303&api=v2)
Enter the name of a source (and optionally, the search radius) into the  _target_ search dialog box in the main Portal window (_top_), or into the _Object Name or Position_ filter in the Advanced Search window (_bottom_).
The interface should really use the term __Object__ rather than __target__ , which would be in line with the vocabulary defined here, and with other MAST interfaces.  
* * *

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces", "Header 2": "MAST Mission Search"} -->
The MAST Mission searches, like the Portal, can also search by source name. However, the results will be specific to the particular mission (e.g., HST, JWST).
![](https://outerspace.stsci.edu/download/attachments/298813886/dialog_MM_objSearch.png?version=1&modificationDate=1740421313706&api=v2)
Enter coordinates or the name of one or more objects (and optionally, a search radius) into the __Object__ dialog box in the search window.
* * *

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces", "Header 2": "MAST API"} -->
**astroquery.mast**
```
from astroquery.mast import Observations, Mast
obs = Observations.query_object("M57", radius="1 m")
coords = Mast.resolve_object('M57')
```  
**MAST API**
```
resolver_request = {'service':'Mast.Name.Lookup',
'params':{'input':'M57',
'format':'json'},
}
headers, resolved_object_string = mast_query(resolver_request)
```  
The Python package _top left_).
A fragment of the same query is shown for the MAST API (_bottom left_), where the object name is resolved with the **Mast.Name.Lookup** service. See the [MAST API Tutorial](https://mast.stsci.edu/api/v0/MastApiTutorial.html) for the full query.
**SANTA service**
```
https://mastresolver.stsci.edu/Santa-war/query?name=EPIC 201124136&resolveAll=true
```  
The [SANTA](https://mastresolver.stsci.edu/Santa-war/) service can be queried directly with a URL of the form shown at left. It is possible to select the back-end resolver service, or to show the results of all resolvers available to SANTA. In addition to coordinates, SANTA returns the canonical name of the source, its angular size (if extended), and the name of the back-end resolver.
* * *
Searches by source name in MAST will be more robust, accurate, and efficient if you embrace the following best practices:
* Query by the source designation in a major, modern catalog, rather than by common name
* If all you know is the common name, try searching SIMBAD or NED directly to find the canonical name
* Leverage the syntax rules of the back-end name resolvers (SIMBAD or NED)
* SIMBAD often follows conventions for catalog entries (where the **^** symbol indicates a blank space): catalog abbreviation(**^** catalog version)**^** member number
* **Gaia ^DR3^2090486618786534784**
* **IRAS ^18517+3257
**
* Identifiers from major catalogs where the source name includes coordinates often follow the rule: catalog abbreviation**^** coordinate type ID+coordinates, where the coordinate type is J for J(2000) equatorial coordinates, G for Galactic coordinates, B for Besselian FK4 (1950) coordinates, etc.  
* **2MASS ^J00054775-7145571**
* **GB6 ^B1851+3257 **
* **PN ^G063.1+13.9**
* Always specify a search radius, with a value that is no larger than what is needed for your science purpose
* This will limit the size (and minimize the response time) of the results returned by the query
* Use _`r=0`_to match a position exactly, assuming the source does not have significant proper motion
* Be aware of the need to re-cast coordinates to the epoch of interest for high proper-motion sources. (See the article [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST).)  
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* SIMBAD
* See also the
* NED
* MAST [SANTA](https://mastresolver.stsci.edu/Santa-war/) name resolver
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* MAST Mission searches for [HST](https://mast.stsci.edu/search/ui/#/hst/) and [JWST](https://mast.stsci.edu/search/ui/#/jwst/)  
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
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Jdaviz in the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113048/Jdaviz+in+the+MAST+Portal "Jdaviz in the MAST Portal")
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [Cloud Science Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797523/Cloud+Science+Platforms "Cloud Science Platforms")
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
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
This article describes how to make effective searches for data by astrophysical source name, and how avoid problems with the underlying translations from name to sky coordinates.
**On this page...**
* 1[Source Identifiers in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-SourceIdentifiersinMAST)
* 2[Search by source name](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Searchbysourcename)
* 2.1[Name translation](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Nametranslation)
* 2.2[Problem cases](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Problemcases)
* 3[MAST Search Interfaces](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-MASTSearchInterfaces)
* 3.1[Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-Portal)
* 3.2[MAST Mission Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-MASTMissionSearch)
* 3.3[MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-MASTAPI)
* 4[Best Practices](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-best_practicesBestPractices)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-ForFurtherReading...)

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Source Identifiers in MAST"} -->
Most MAST search interfaces, apart from those specifically devoted to source catalogs, query the MAST archive catalog of **Observations**. Observations are collections of products and metadata related to exposures by a given mission at a given sky position. The archive catalog:
* **is** a database of _**Observations**_ from missions hosted by MAST
* **is _not_** a database of individual astrophysical sources  
Thus, searching MAST for sources (or positions) amounts to querying the archive catalog for Mission data that overlap the astrophysical source position or extent.
Note that these queries apply to _fixed_ astrophysical sources—i.e., not solar system bodies. (See [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST) for non-fixed sources, which uses the term _target_ to describe planned pointings of the telescope.) This article describes how MAST translates searches of positions and source names to queries of matching Observations. The following terms take on a specific meaning for searches of MAST holdings:
Term | Usage
---|---
**Identifier** | **Designation** is the official **identifier**. An astrophysical source may have multiple identifiers (most often this means it is listed in multiple published catalogs), but the key point is that all identifier synonyms refer unambiguously to a _single, unique source_. Any of these names can be **resolved** (i.e., translated) to sky coordinates of the fixed source, provided the name string matches the syntax rules of the resolver service.
**Object** |  Refers to a generic source or field name, which is translated to sky coordinates via MAST or another name resolution service. MAST syntax rules are somewhat more restrictive than SIMBAD.  MAST also uses the term Object to refer to an Observation identifier (a name for a collection of related files, rather than the name of an astrophysical source), which one of the MAST-hosted services can resolve to a spatial position. This conflation of terms can lead to confusion in some contexts.
**Source** | A generic term used in the literature or in MAST documentation to refer to an astrophysical entity. Can refer to (often spatially unresolved) aggregate objects.
**Target** | The name of a target or field associated with an observation by a MAST-hosted mission. The target name is provided by the observer, and may or may not match an official designation. Targets are string-matched to a field in the MAST observation database. See warning below.
Searching by _target name_ in MAST can problematic because:
* it must match exactly to values in the database field, unless wildcard characters are used
* it may or may not match an official designation
* it may or may not match the name given for a different Observation by another observer of the same source or field  
Because of these issues, searches for data by target name may not match every entry in the MAST catalog that one might expect.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Search by source name"} -->
Searches by source name in MAST are translated to searches by sky coordinates using a back-end web service called  _**SANTA**_ (_STScI Archive Name Translation Applications_). SANTA itself depends on multiple name resolution services: the major astronomical name services  _**S**_ et of _**I**_ dentifications, _**M**_ easurements and _**B**_ ibliography for _**A**_ stronomical _**D**_ ata; curated by CDS) and _**N**_ ASA/IPAC _**E**_ xtragalactic _**D**_ atabase), in addition to internal services for identifiers specific to MAST.
NED, as its name implies, contains extensive holdings on extra-Galactic sources. Though their database does contain entries for point-sources, it is not intended to be complete for stars. SIMBAD includes both Galactic and extra-Galactic sources, with excellent completeness on the former. Both services harvest source catalogs in the published literature.

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Name translation"} -->
The MAST SANTA service uses coordinates directly, or queries one or more back-end name translation services, or **name resolvers** , to determine source coordinates. The services are searched in the order of the table below until a match is found.
Name resolvers  
| Resolver | Description | Example
---|---|---|---
1 | TIC | MAST translates identifiers from the  | `TIC 52031993`
2 | KEPLER | MAST translates [Kepler](https://archive.stsci.edu/kepler/) identifiers starting with `Kepler`, `Kplr` or `KIC` | `KPLR 757076`
3 | K2 | MAST translates [K2](https://archive.stsci.edu/missions-and-data/k2) identifiers starting with `EPIC`, `K2` or `KTWO` | `EPIC 201124136`
4 | DADS | MAST translates HST IPPPSSOOT observation identifiers, **or partial (IPPPSS) identifiers.**(Searches for HLA products work similarly, except that the **`hst_`**prefix must be omitted.) Note that these translations are from Observations to coordinates, rather than source identifier to coordinates. |  `ocr7jkOaq,` `j91k10` `10188_10`
5 | EXO | MAST translates [Exoplanet](https://exo.mast.stsci.edu/) identifiers, including TESS Target of Interest (TOI) identifiers | `TOI 172 b`
6 | SIMBAD | Name resolver at CDS |  
7 | SIMBAD/CfA | Mirror of SIMBAD service at CfA/Harvard |  
8 | NED | Uses the  |  
The order is fixed, and MAST applications do not currently offer users the option to specify an alternative name resolver, except when using the SANTA service directly.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases"} -->
There are cases where the returned coordinates differ between SIMBAD and NED, though the coordinates usually agree to within 0.25 arcsec among services. But there are many cases where the returned coordinates between SIMBAD and NED are quite discrepant. These cases fall into a few categories.

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases", "Header 3": "Imprecise source specification"} -->
There are cases where source identifiers (expressed in ASCII text) for different objects are very similar, but refer to very different astrophysical sources. Examples include:
Imprecise source names
The designation for the name **`mu eri`**which is interpreted as a different star in each resolver. This illustrates the need to pay strict attention to the specialized naming conventions in SIMBAD and NED.
Designation | Notes |  ASCII Identifier | Resolver | RA(J2000) | Dec(J2000)
---|---|---|---|---|---
**µ Eri** | Bright star with a Bayer designation |  **`* mu. eri`**`**mu eri**` | SIMBAD | `4:45:30.15` | `-3:15:16.777`
**`muu eri`**|  NED
**MU Eri** | Variable star | **`V* mu eri`**|  SIMBAD | `2:48:10.566` | `-15:18:04.03`
**`mu eri`**|  NED
Since the SANTA resolver defaults to SIMBAD, searching for the name **`mu eri`**will return observations matching the source**μ Eri.** Note that SIMBAD follows a number of naming conventions, including:
**`*^`**indicates what follows the asterisk (plus blank space) is a star name
`**V*^**`indicates what follows is a variable star name
See the

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases", "Header 3": "Ambiguous names"} -->
Names of sources can be ambiguous for a resolver service, or the name can be conflated by the service. Examples include:
Ambiguous source names
#### Popular names
Popular names are resolved by searching a "name" database table to match a more formal catalog designation; the match is not guaranteed to be the same in different name resolver services. For example, the name **`ophiuchus`**is interpreted by SIMBAD as the Ophiuchus molecular cloud, a Galactic star forming region. NED interprets it as the Ophiuchus cluster of galaxies. These sources are about 10° apart on the sky. Similarly, SIMBAD interprets the name**`taurus`**as the
#### Name Overloading
A search for the name **`Arp 2`**in SIMBAD returns the coordinates for a Galactic globular cluster, but NED returns the coordinates for a galaxy with the canonical name UGC 10310. These sources are 84° apart on the sky.
#### M 51
This source in the Messier catalog (published 1784) refers to two sources in the NGC (first published in 1888): SIMBAD returns the position of the bright spiral galaxy NGC 5194, rather than the companion NGC 5195. NED adopts a mean position. From the NED documentation:
_"M51" refers to the pair of galaxies, NGC 5194 and NGC 5195, not just to the larger spiral NGC 5194. The position that NED adopts for M51 is therefore the mean position of the two galaxies. We treat other pairs, triplets, groups, and clusters listed in NED the same way: we adopt mean positions for all the galaxies rather than for just the brightest or for the most centrally-located._

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Search by source name", "Header 2": "Problem cases", "Header 3": "Angularly large sources"} -->
The exact center of certain extended sources can be uncertain. Examples include:
Large sources
#### IC 2118
SIMBAD and NED both resolve to the same canonical name (NGC 1909), but the coordinates differ by nearly a degree. The source is an extended reflection nebula, and the coordinates are derived from separate catalogs. The coordinates returned by SIMBAD appear to be approximate (i.e., the precision is one-tenth of a degree).
* * *

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces"} -->
Searches by source name may be executed with one of the MAST web user interfaces, with user-written software by calling an API, or by using the [SANTA interface](https://mastresolver.stsci.edu/Santa-war/) directly. Note that MAST does not support the full syntax allowed by SIMBAD, and in particular partial identifiers with wildcards are not allowed in source names. Spaces in source names, including between the catalog abbreviation and the member number, are allowed but often not necessary in MAST.
An important feature of these interfaces is the ability to specify a **search radius** , that is, the radius of a circle centered on the resolved coordinate that will produce matches with MAST observations that overlap the circle. (These are often called **cone searches** , in reference to the linearly growing size of the implied physical radius with distance to the source.) If no radius is specified, a default will be used. Keep the following in mind for cone searches:
* The default for point-sources is 0.2 deg, but may be increased dynamically in the search if the source angular size (as recorded in SIMBAD or NED) is larger.
* The search results will include all data for which any part of the observing aperture overlaps the search cone.
* The observing aperture is just the extent of a (possibly composite) image, or the slit of a spectrograph. The projection of the aperture boundaries onto the sky is often called the observation **footprint**.**
**
* **Note:** any portion of a footprint that overlaps the search cone will be matched, whether the image actually includes the source or not.
* Use a search radius of r=0 to match only data that overlap that exact location in the sky.
* This is often best when searching for small or unresolved sources, provided the source does not have high proper motion.  
For some very large sources where MAST-hosted missions have made many observations, the returned results may be quite large. For M31, the default search radius is over 1.6 deg, which currently matches nearly a quarter-million observations. In such cases you may find the query times out (yielding no results at all, and hanging the application), or you may find it impossible to do anything with the results, such as load rows into the download basket. See [Best Practices](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/298813886/Searching+for+Named+Sources#SearchingforNamedSources-best_practices) below.

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces", "Header 2": "Portal"} -->
The MAST [Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) enables searches for sources in two ways, summarized below. See the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) chapter [Basic Search](https://outerspace.stsci.edu/display/MASTDOCS/Basic+Search) for formatting and other details.
![](https://outerspace.stsci.edu/download/attachments/298813886/dialog_PortalSearch.png?version=1&modificationDate=1740421076302&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/298813886/filter_m57.png?version=1&modificationDate=1739303900303&api=v2)
Enter the name of a source (and optionally, the search radius) into the  _target_ search dialog box in the main Portal window (_top_), or into the _Object Name or Position_ filter in the Advanced Search window (_bottom_).
The interface should really use the term __Object__ rather than __target__ , which would be in line with the vocabulary defined here, and with other MAST interfaces.  
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces", "Header 2": "MAST Mission Search"} -->
The MAST Mission searches, like the Portal, can also search by source name. However, the results will be specific to the particular mission (e.g., HST, JWST).
![](https://outerspace.stsci.edu/download/attachments/298813886/dialog_MM_objSearch.png?version=1&modificationDate=1740421313706&api=v2)
Enter coordinates or the name of one or more objects (and optionally, a search radius) into the __Object__ dialog box in the search window.
* * *

<!-- CHUNK 23 END -->

<!-- CHUNK 24 START -->
<!-- Metadata: {"Header 1": "MAST Search Interfaces", "Header 2": "MAST API"} -->
**astroquery.mast**
```
from astroquery.mast import Observations, Mast
obs = Observations.query_object("M57", radius="1 m")
coords = Mast.resolve_object('M57')
```  
**MAST API**
```
resolver_request = {'service':'Mast.Name.Lookup',
'params':{'input':'M57',
'format':'json'},
}
headers, resolved_object_string = mast_query(resolver_request)
```  
The Python package _top left_).
A fragment of the same query is shown for the MAST API (_bottom left_), where the object name is resolved with the **Mast.Name.Lookup** service. See the [MAST API Tutorial](https://mast.stsci.edu/api/v0/MastApiTutorial.html) for the full query.
**SANTA service**
```
https://mastresolver.stsci.edu/Santa-war/query?name=EPIC 201124136&resolveAll=true
```  
The [SANTA](https://mastresolver.stsci.edu/Santa-war/) service can be queried directly with a URL of the form shown at left. It is possible to select the back-end resolver service, or to show the results of all resolvers available to SANTA. In addition to coordinates, SANTA returns the canonical name of the source, its angular size (if extended), and the name of the back-end resolver.
* * *
Searches by source name in MAST will be more robust, accurate, and efficient if you embrace the following best practices:
* Query by the source designation in a major, modern catalog, rather than by common name
* If all you know is the common name, try searching SIMBAD or NED directly to find the canonical name
* Leverage the syntax rules of the back-end name resolvers (SIMBAD or NED)
* SIMBAD often follows conventions for catalog entries (where the **^** symbol indicates a blank space): catalog abbreviation(**^** catalog version)**^** member number
* **Gaia ^DR3^2090486618786534784**
* **IRAS ^18517+3257
**
* Identifiers from major catalogs where the source name includes coordinates often follow the rule: catalog abbreviation**^** coordinate type ID+coordinates, where the coordinate type is J for J(2000) equatorial coordinates, G for Galactic coordinates, B for Besselian FK4 (1950) coordinates, etc.  
* **2MASS ^J00054775-7145571**
* **GB6 ^B1851+3257 **
* **PN ^G063.1+13.9**
* Always specify a search radius, with a value that is no larger than what is needed for your science purpose
* This will limit the size (and minimize the response time) of the results returned by the query
* Use _`r=0`_to match a position exactly, assuming the source does not have significant proper motion
* Be aware of the need to re-cast coordinates to the epoch of interest for high proper-motion sources. (See the article [Finding Solar System Bodies in MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852359/Finding+Solar+System+Bodies+in+MAST).)  
* * *

<!-- CHUNK 24 END -->

<!-- CHUNK 25 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* SIMBAD
* See also the
* NED
* MAST [SANTA](https://mastresolver.stsci.edu/Santa-war/) name resolver
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* MAST Mission searches for [HST](https://mast.stsci.edu/search/ui/#/hst/) and [JWST](https://mast.stsci.edu/search/ui/#/jwst/)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 25 END -->

