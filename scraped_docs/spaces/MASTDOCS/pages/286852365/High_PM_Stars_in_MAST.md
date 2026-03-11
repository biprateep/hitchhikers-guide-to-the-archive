---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST"
date_accessed: "2026-03-11T16:26:28.890228"
content_length: 36239
---

<!-- CHUNK 1 START -->
This article describes how to discover MAST Mission observations of stars with high proper motion, and to interpret the results of searches you perform.
**On this page...**
* 1[Searches for Stars with High Proper Motion](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-SearchesforStarswithHighProperMotion)
* 2[Example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-Example)
* 2.1[Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-Coordinates)
* 3[Visualization with AstroView](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-VisualizationwithAstroView)
* 3.1[Background Survey](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-BackgroundSurvey)
* 3.2[Observation Footprints](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-ObservationFootprints)
* 4[Implications for Understanding Prior Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-ImplicationsforUnderstandingPriorObservations)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Searches for Stars with High Proper Motion"} -->
Stars with high proper motion (PM) are popular targets to observe for a variety of astrophysical reasons, including their propensity to appear in catalogs of stars thought to host systems of planets. Finding prior observations of such sources, or planning for future observations, can present special challenges when searching MAST. Here are points to keep in mind:
* Most stars with high PM are known only by a catalog designation, which may not be recognized by standard tools that resolve names to coordinates.
* You must pay attention to the reference system and epoch of the source catalog.
* Searches by object name (in MAST APIs or a Web application like the Portal) will be resolved to positions in the
* MAST search tools assume ICRS coordinates (epoch 2000.0)  
In MAST web applications source positions can be visualized on a sky background, but different elements of the visualization correspond to different epochs:
* For Portal searches, the displayed sky background in **AstroView** is in the ICRS frame, with an _epoch that depends on the background survey_. The background survey images were obtained over a span of years, so any given high-PM source may be blurry and appear at an unexpected location relative to background stars.  
* For DSS (the default) the epoch is roughly 1990; for Pan-STARRS the epoch is about 2012.5.
* The displayed footprints of the observation apertures are in the ICRS frame at the _epoch of each observation_.
* Cone searches (of a circular region of sky about a position) match an observation if the cone (at epoch 2000.0) matches any part of the footprint (defined at the epoch of the observation).  
For sources with low proper motion, these various epochs typically do not matter. However, to obtain accurate matches of observations of targets with high proper motion, users must either:
* correct the source position to the current epoch, and then re-execute a search, this time by position
* use a cone search radius that is large enough to include the source position at all epochs of MAST mission observation footprints  
In either case, note that the Observation footprints will have to be interpreted in the current epoch to know if they apply to your target.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Example"} -->
To understand the implications of high proper-motion targets on MAST searches, consider the example of Trappist-1. This source is an M-dwarf and a well known exoplanet host star; it is designated in GAIA-DR3 as 2635476908753563008. It has a proper motion in excess of 1 arcsec/yr.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Example", "Header 2": "Coordinates"} -->
The coordinates for this source are fundamentally drawn from [SANTA query](https://mastresolver.stsci.edu/Santa-war/query?name=Trappist-1&resolveAll=True) (the MAST resolver engine) to
The GAIA DR3 ID is: **2635476908753563008**. Note that other catalog identifiers, notably 2MASS (J23062928-0502285) and WISE (J230630.01-050233.9), include coordinates which presumably apply to the reference epoch of those catalogs.
Catalog |  Parameter | Reference Frame | Value (HH/DD mm ss) | Value (DDD.dddd)
---|---|---|---|---
SIMBAD | RA | ICRS, Ep=2000.0 | `**23 06 29.3684948589**`| `346.622368728575`
Dec | ICRS, Ep=2000.0 | `**-05 02 29.037301866**`| ` -5.041399250518333`
GAIA (Barycentric) | RA | ICRS, Ep=2016.0 | `23 06 30.3651906336` | `**346.62652162764**`
Dec | ICRS, Ep=2016.0 | `-05 02 36.70195` | `** -5.04352831943
**`  
| PM |
| 1046.825 (mas/yr) |  
| PM_RA*cos(Dec) |
| 930.788 ±0.087 (mas/yr) |  
| PM_Dec |
| -479.038 ±0.070 (mas/yr) |  
The difference in epoch from SIMBAD vs. GAIA shows the star has moved >17 arcsec.
To compute the coordinates for some future epoch, say 2027-Feb-5 at noon UTC, use utilities in astropy:
```
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord

# ICRS coordinates for Trappist-1
ra = 346.62652162764
dec = -5.04352831943
pm_ra = 930.788
pm_dec = -479.038
# Create a SkyCoord object for the epoch of GAIA
c_2016 = SkyCoord(ra=ra*u.deg,
dec=dec*u.deg,
pm_ra_cosdec=pm_ra*u.mas/u.yr,
pm_dec=pm_dec*u.mas/u.yr,
obstime=Time(2016.0, format='jyear', scale='tcb')
)
# Compute coordinates for new epoch
c_new = c_2016.apply_space_motion(Time('2027-02-05T12:00:00'))
print(f'RA: {c_new.ra.deg}, Dec: {c_new.dec.deg}')

'RA: 346.62888293361175, Dec: -5.044738873941171'
```

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView"} -->
**AstroView** displays Observations in MAST in the

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Background Survey"} -->
Astroview displays images from one of a selection of wide-area sky surveys. The **epoch** of AstroView all-sky images depends upon the selected background survey, and even the position on the sky, since the contributing images were obtained over time during the course of each survey. The epoch for any given region of sky is effectively the mean epoch of the image stack from the survey used to create the sky background. For two popular surveys:

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Background Survey", "Header 3": "**DSS**"} -->
The **Digitized Sky Survey** is the default background survey because of its all-sky coverage, and average resolution and depth. Photographic plates, the source medium for the DSS, were taken between 1970 and 2000, with a mid-point of about 1990. Note that the red-blue dispersion of point-sources is in part an artifact of a systematic difference in time between the mean epochs of the red vs. the blue plates.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Background Survey", "Header 3": "**Pan-STARRS**"} -->
CCD images from the Pan-STARRS-1 survey were were obtained from 2010 through 2014; the mid-point of the survey is about 2012.5. The color background images used in MAST were created from stacked images in multiple passbands, which of course spanned some range in time.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Observation Footprints"} -->
Observations in MAST include a spatial extent (a **footprint**) of an instrument **aperture** , which is characterized by a polygon or a simple geometric shape. The coordinates of the footprint for each Observation are defined in the ICRS reference frame at the epoch of that observation. This is of course different than the epoch of the background survey image.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Observation Footprints", "Header 3": "Cone Search for Trappist-1"} -->
An AstroView rendering is shown in the figure below, which is the result of performing an Object cone search for this star ("`Trappist-1, r=1m`") and filtering for the JWST mission. The footprints are from matching JWST Observations, which were obtained from 2022 July to 2023 Dec. The position in DSS indicates that the epoch of that background images is about 1990.9. The source position at different epochs is consistent with the GAIA proper motion measurement.  
![](https://outerspace.stsci.edu/download/attachments/286852365/Tr-1_DSS.png?version=1&modificationDate=1736447094971&api=v2)![](https://outerspace.stsci.edu/download/attachments/286852365/Tr-1_PS.png?version=1&modificationDate=1736447095675&api=v2)
AstroView display of Observation footprints matching an Object search for Trappist-1, with the Pan-STARRS (_left_ , with the star just to the lower-left of center) and DSS (_right_) sky backgrounds. A 1.0 arcmin search area (_dashed red circle_) is shown; the center is also marked (_small red cross-hair_), which is also the location in 2000.0. Also shown are the positions in DSS (small _purple cross-hair_ , just to the upper-right of center), the position in 2016.0 (_small white box_). and the position in 2022.6 (_larger white box_) during some early JWST observations. The remainder of the footprints (blue rectangles) are of other JWST Observations.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Implications for Understanding Prior Observations"} -->
There are >3 M stars brighter than m=12 in the GAIA catalog, which are easily bright enough to obtain light curves from TESS. Of those, >185,000 have PM >50 mas/yr, which would result in displacements of 1.7 arcsec during the lifetime of the HST mission. Such displacements would potentially complicate searches for prior Observations in MAST, and in planning future, small-aperture observations with our Flagship missions. Some key steps can help future Observation planning for high PM stars:  
* Be sure to obtain good coordinates and proper-motions for your targets, ideally from GAIA
* If you search for your target by name (using the name-resolver in the Porta)l, note that the returned coordinates will be at the 2000.0 epoch
* Re-compute the coordinates of your target at the anticipated epoch of the Observation
* Execute a MAST search at the anticipated coordinates, with a search radius large enough to include the target position at the earliest epoch of interest
* Recognize that the displayed footprints in the MAST Portal reflect the epochs of those prior observations.  
* * *

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [MAST Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide)  
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
This article describes how to discover MAST Mission observations of stars with high proper motion, and to interpret the results of searches you perform.
**On this page...**
* 1[Searches for Stars with High Proper Motion](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-SearchesforStarswithHighProperMotion)
* 2[Example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-Example)
* 2.1[Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-Coordinates)
* 3[Visualization with AstroView](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-VisualizationwithAstroView)
* 3.1[Background Survey](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-BackgroundSurvey)
* 3.2[Observation Footprints](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-ObservationFootprints)
* 4[Implications for Understanding Prior Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-ImplicationsforUnderstandingPriorObservations)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852365/High+PM+Stars+in+MAST#HighPMStarsinMAST-ForFurtherReading...)

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Searches for Stars with High Proper Motion"} -->
Stars with high proper motion (PM) are popular targets to observe for a variety of astrophysical reasons, including their propensity to appear in catalogs of stars thought to host systems of planets. Finding prior observations of such sources, or planning for future observations, can present special challenges when searching MAST. Here are points to keep in mind:
* Most stars with high PM are known only by a catalog designation, which may not be recognized by standard tools that resolve names to coordinates.
* You must pay attention to the reference system and epoch of the source catalog.
* Searches by object name (in MAST APIs or a Web application like the Portal) will be resolved to positions in the
* MAST search tools assume ICRS coordinates (epoch 2000.0)  
In MAST web applications source positions can be visualized on a sky background, but different elements of the visualization correspond to different epochs:
* For Portal searches, the displayed sky background in **AstroView** is in the ICRS frame, with an _epoch that depends on the background survey_. The background survey images were obtained over a span of years, so any given high-PM source may be blurry and appear at an unexpected location relative to background stars.  
* For DSS (the default) the epoch is roughly 1990; for Pan-STARRS the epoch is about 2012.5.
* The displayed footprints of the observation apertures are in the ICRS frame at the _epoch of each observation_.
* Cone searches (of a circular region of sky about a position) match an observation if the cone (at epoch 2000.0) matches any part of the footprint (defined at the epoch of the observation).  
For sources with low proper motion, these various epochs typically do not matter. However, to obtain accurate matches of observations of targets with high proper motion, users must either:
* correct the source position to the current epoch, and then re-execute a search, this time by position
* use a cone search radius that is large enough to include the source position at all epochs of MAST mission observation footprints  
In either case, note that the Observation footprints will have to be interpreted in the current epoch to know if they apply to your target.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Example"} -->
To understand the implications of high proper-motion targets on MAST searches, consider the example of Trappist-1. This source is an M-dwarf and a well known exoplanet host star; it is designated in GAIA-DR3 as 2635476908753563008. It has a proper motion in excess of 1 arcsec/yr.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Example", "Header 2": "Coordinates"} -->
The coordinates for this source are fundamentally drawn from [SANTA query](https://mastresolver.stsci.edu/Santa-war/query?name=Trappist-1&resolveAll=True) (the MAST resolver engine) to
The GAIA DR3 ID is: **2635476908753563008**. Note that other catalog identifiers, notably 2MASS (J23062928-0502285) and WISE (J230630.01-050233.9), include coordinates which presumably apply to the reference epoch of those catalogs.
Catalog |  Parameter | Reference Frame | Value (HH/DD mm ss) | Value (DDD.dddd)
---|---|---|---|---
SIMBAD | RA | ICRS, Ep=2000.0 | `**23 06 29.3684948589**`| `346.622368728575`
Dec | ICRS, Ep=2000.0 | `**-05 02 29.037301866**`| ` -5.041399250518333`
GAIA (Barycentric) | RA | ICRS, Ep=2016.0 | `23 06 30.3651906336` | `**346.62652162764**`
Dec | ICRS, Ep=2016.0 | `-05 02 36.70195` | `** -5.04352831943
**`  
| PM |
| 1046.825 (mas/yr) |  
| PM_RA*cos(Dec) |
| 930.788 ±0.087 (mas/yr) |  
| PM_Dec |
| -479.038 ±0.070 (mas/yr) |  
The difference in epoch from SIMBAD vs. GAIA shows the star has moved >17 arcsec.
To compute the coordinates for some future epoch, say 2027-Feb-5 at noon UTC, use utilities in astropy:
```
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord

# ICRS coordinates for Trappist-1
ra = 346.62652162764
dec = -5.04352831943
pm_ra = 930.788
pm_dec = -479.038
# Create a SkyCoord object for the epoch of GAIA
c_2016 = SkyCoord(ra=ra*u.deg,
dec=dec*u.deg,
pm_ra_cosdec=pm_ra*u.mas/u.yr,
pm_dec=pm_dec*u.mas/u.yr,
obstime=Time(2016.0, format='jyear', scale='tcb')
)
# Compute coordinates for new epoch
c_new = c_2016.apply_space_motion(Time('2027-02-05T12:00:00'))
print(f'RA: {c_new.ra.deg}, Dec: {c_new.dec.deg}')

'RA: 346.62888293361175, Dec: -5.044738873941171'
```

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView"} -->
**AstroView** displays Observations in MAST in the

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Background Survey"} -->
Astroview displays images from one of a selection of wide-area sky surveys. The **epoch** of AstroView all-sky images depends upon the selected background survey, and even the position on the sky, since the contributing images were obtained over time during the course of each survey. The epoch for any given region of sky is effectively the mean epoch of the image stack from the survey used to create the sky background. For two popular surveys:

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Background Survey", "Header 3": "**DSS**"} -->
The **Digitized Sky Survey** is the default background survey because of its all-sky coverage, and average resolution and depth. Photographic plates, the source medium for the DSS, were taken between 1970 and 2000, with a mid-point of about 1990. Note that the red-blue dispersion of point-sources is in part an artifact of a systematic difference in time between the mean epochs of the red vs. the blue plates.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Background Survey", "Header 3": "**Pan-STARRS**"} -->
CCD images from the Pan-STARRS-1 survey were were obtained from 2010 through 2014; the mid-point of the survey is about 2012.5. The color background images used in MAST were created from stacked images in multiple passbands, which of course spanned some range in time.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Observation Footprints"} -->
Observations in MAST include a spatial extent (a **footprint**) of an instrument **aperture** , which is characterized by a polygon or a simple geometric shape. The coordinates of the footprint for each Observation are defined in the ICRS reference frame at the epoch of that observation. This is of course different than the epoch of the background survey image.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "Visualization with AstroView", "Header 2": "Observation Footprints", "Header 3": "Cone Search for Trappist-1"} -->
An AstroView rendering is shown in the figure below, which is the result of performing an Object cone search for this star ("`Trappist-1, r=1m`") and filtering for the JWST mission. The footprints are from matching JWST Observations, which were obtained from 2022 July to 2023 Dec. The position in DSS indicates that the epoch of that background images is about 1990.9. The source position at different epochs is consistent with the GAIA proper motion measurement.  
![](https://outerspace.stsci.edu/download/attachments/286852365/Tr-1_DSS.png?version=1&modificationDate=1736447094971&api=v2)![](https://outerspace.stsci.edu/download/attachments/286852365/Tr-1_PS.png?version=1&modificationDate=1736447095675&api=v2)
AstroView display of Observation footprints matching an Object search for Trappist-1, with the Pan-STARRS (_left_ , with the star just to the lower-left of center) and DSS (_right_) sky backgrounds. A 1.0 arcmin search area (_dashed red circle_) is shown; the center is also marked (_small red cross-hair_), which is also the location in 2000.0. Also shown are the positions in DSS (small _purple cross-hair_ , just to the upper-right of center), the position in 2016.0 (_small white box_). and the position in 2022.6 (_larger white box_) during some early JWST observations. The remainder of the footprints (blue rectangles) are of other JWST Observations.

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "Implications for Understanding Prior Observations"} -->
There are >3 M stars brighter than m=12 in the GAIA catalog, which are easily bright enough to obtain light curves from TESS. Of those, >185,000 have PM >50 mas/yr, which would result in displacements of 1.7 arcsec during the lifetime of the HST mission. Such displacements would potentially complicate searches for prior Observations in MAST, and in planning future, small-aperture observations with our Flagship missions. Some key steps can help future Observation planning for high PM stars:  
* Be sure to obtain good coordinates and proper-motions for your targets, ideally from GAIA
* If you search for your target by name (using the name-resolver in the Porta)l, note that the returned coordinates will be at the 2000.0 epoch
* Re-compute the coordinates of your target at the anticipated epoch of the Observation
* Execute a MAST search at the anticipated coordinates, with a search radius large enough to include the target position at the earliest epoch of interest
* Recognize that the displayed footprints in the MAST Portal reflect the epochs of those prior observations.  
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [MAST Mission Search Guide](https://outerspace.stsci.edu/display/MASTDOCS/Mission+Search+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 23 END -->

