---
title: "Selecting Collections"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search"
date_accessed: "2026-03-11T16:32:07.590554"
content_length: 8032
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Selecting Collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-SelectingCollections)
* 2[Choosing a Target...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-ChoosingaTarget...)
* 2.1[...by Name](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byName)
* 2.1.1[Allowed Format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-AllowedFormat)
* 2.2[...by Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byCoordinates)
* 2.2.1[Specify the Search Radius](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-SpecifytheSearchRadius)
* 2.2.2[Allowed Format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-AllowedFormat.1)
* 2.3[...by Observation ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-...byObservationID)
* 3[Notes on Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search#BasicSearch-NotesonSearching)  
Basic searches involve two steps:
* select a collection
* input a valid search criterion  
Valid search inputs are either the target name of an astronomical object, or the target coordinates, e.g., Right Ascension (RA) and Declination (Dec). The search box takes specific formatting for target names or coordinates. See the tables within each section below for allowed formatting to ensure correct syntax for proper searches. The search can be initiated by clicking the **Search** button or by pressing the Enter key on your keyboard while the cursor is in the input search box.
![](https://outerspace.stsci.edu/download/attachments/94962886/menu_selectCollection.png?version=2&modificationDate=1660158552235&api=v2)
The basic search form. Select a collection from the pull-down menu (_left_), enter a target name or target coordinates (_right_), then click **Search**.

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Selecting Collections"} -->
Users can choose which collection of data they wish to perform a search in. Most, but not all, collections allow for basic searching by target name or coordinate. The default collection to search is all **MAST Observations**. Unless you wish to search within a specific dataset, it is recommended to leave the default set as is. For more information on searching with the other collections, see sections [Catalog Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search) and [Special Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches).
Collection | Description | Allows Basic Search
---|---|---
MAST Observations | The combined observations from all MAST collections. These include HST, JWST, Kepler, GALEX, EUVE, FUSE, IUE, SWIFT, and several other missions. | yes
Virtual Observatory (VO) | A worldwide collection of repositories providing astronomical images, catalogs and spectra. | yes
[Hubble Source Catalog](https://archive.stsci.edu/hst/hsc/) (HSC) | A catalog of tens of millions of sources from the Hubble Legacy Archive (HLA), derived from HST imaging in multiple instruments and passbands. | yes
Hubble Source Catalog Spectra | A collection of spectra associated with sources in the HSC. | no
MAST Catalogs | MAST-held collections of source lists, e.g. GAIA, TESS input (TIC) catalogs. | yes
Hubble Wide-Field Camera PSF | Libraries of observed, reference point-sources for higher-precision photometry and astrometry. | no
Observations in a DOI | Search for MAST data associated with a Digital Object Identifier. | yes
JWST Instrument Keywords | Search for JWST data by instrument that match a selection of header keyword values. | no
JWST WSS | Search for JWST Wavefront products. | no

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Name"} -->
Users can search for data by inputting the astronomical name of a target object on the sky. Names of objects are passed to a

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Name", "Header 3": "Allowed Format"} -->
Allowed formats for target names are the following:
Example | Description
---|---
`M101, NGC45` | Objects from standard catalogs such as Messier and NGC will be resolved
`Antennae, Eta Carinae` | Common names often work
`T Tau` | Variable star names often work
`BD+19 706` | Star catalogs with coordinate symbols
`png 000.8-07.6` | Other catalogs with coordinate and decimal symbols
`2MASS J04215943+1932063` | All-sky catalogs with coordinate symbols
`TYC 1272-470-1` | All-sky satellite catalogs with restricted symbols

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates"} -->
Users can search for data by providing a target on-sky coordinate of Right Ascension (RA) and Declination (Dec). Coordinates can be given in a variety of formats. Right ascensions must be positive and southern declinations require a leading negative sign. A cone search is performed around the input coordinate at a default radius of 0.2 degrees.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates", "Header 3": "Specify the Search Radius"} -->
A custom search radius can be specified by appending to the coordinates `**r=**[`_number_`][` _unit_`]` , where number is any valid decimal number and unit is one of "d" (degrees), "m" (arc-minutes), "s" (arc-seconds). The default cone search depends on the size of the object but is usually 0.2 degrees for most targets. Note that some collections have search radius limitations. See the table below for examples of various custom search radius inputs.
Example | Description
---|---
`14:03.210 54:20.945r=0.5` | Coordinate search with radius of 0.5°
`14:03.210 54:20.945r=1d` | Coordinate search with radius of 1°
`14:03.210 54:20.945r=1.2m` | Coordinate search with radius of 1.2 arc-minutes

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Coordinates", "Header 3": "Allowed Format"} -->
Coordinates can be input either as decimal degrees, sexagesimal or galactic coordinates, with various formatting. Allowed formats for target coordinates are the following:
Example | Description
---|---
`14 03 12.6 54 20 56.7` | Sexagesimal coordinates delimited with spaces
`14:03.210 54:20.945` | Sexagesimal coordinates delimited with colons; decimal minutes/arcminutes
`14h03m12.6s +54d20m56.7s` | Sexagesimal coordinates with explicit hms/dms
`g102.0373+59.7711` |  Galactic coordinates of the form:
* `g`[lon][+/–][lat]  
_**with no spaces**_
`180.468 -18.866` | Coordinates in decimal degrees

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Choosing a Target...", "Header 2": "...by Observation ID"} -->
Most MAST missions assign a unique identifier to individual observations. When selecting the collection **MAST Observations by Observation ID** , the input search box changes to accept only valid mission observation IDs, rather than target names or coordinates, as input. This collection option is for use cases when you know exactly the mission observation you wish to search for. A single observation ID is valid input, as well as a comma-separated list of IDs.
Example | Description
---|---
`tess-s0015-4-1` | Search for a single TESS observation
`tess-s0015-4-1, n4ro01020` | Search for multiple observations by id: a TESS and HST observation

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Notes on Searching"} -->
When**formulating a search** , note the following:
* Leading zeros are ignored in the name. For example, `M5` returns results for object Messier 005.
* Object names are not case-sensitive, and spaces between the characters (e.g. `M51` and `M 51`) are ignored unless the space is significant in the name.
* All coordinates are interpreted as J2000.
* The maximum allowed search radius is limited on a collection-by-collection basis.
* The results of a search of [Virtual Observatory collections](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches#SpecialSearches-VO_search) may have arbitrary limits on the number of rows returned, on a resource-by-resource basis (i.e., limits which may imposed by the collection provider).
* Most queries are limited to a single object or position, except for searches by observation ID. However, multiple queries may be submitted sequentially, even if one or more queries are still executing.

<!-- CHUNK 9 END -->

