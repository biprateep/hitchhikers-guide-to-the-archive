[![](https://catalogs.mast.stsci.edu/static/images/catalogs-logo.svg)](https://catalogs.mast.stsci.edu/)
  * [Pan-STARRS Data Archive](https://panstarrs.stsci.edu "PanStarrs Data Archive")
  * [Pan-STARRS API](https://catalogs.mast.stsci.edu/docs/panstarrs.html "PanStarrs API")


# Pan-STARRS Catalog Search
The Panoramic Survey Telescope & Rapid Response System (Pan-STARRS or PS1) is a wide-field imaging facility developed at the University of Hawaii's Institute for Astronomy for a variety of scientific studies from the nearby to the very distant Universe. The PS1 catalog includes measurements in five filters (grizy) covering 30,000 square degrees of the sky north of declination -30 degrees, with typically ~12 epochs for each filter. This interface allows searches for the mean measurements and the deeper stacked measurements from images combining all the epochs. The DR2 release also includes the detection catalog containing all the multi-epoch observations. 
#####  **Target** Supply the central coordinates or target name.
  * [Coordinates](https://catalogs.mast.stsci.edu/panstarrs#tab-form-coordinate)
  * [Target name](https://catalogs.mast.stsci.edu/panstarrs#tab-form-target)


RA
DEC
Validate Coordinates 
Target
Resolve Target 
Position Resolved: Resolution Error: This position did not resolve. Please check input values. ×
Search Radius
Arcminutes Arcseconds Degrees
Max = 30 arcminutes
Please provide a radius.
#####  **Crossmatch a List of Targets** Upload a CSV file.
Choose CSV file  Resolve & validate targets  [Target file help](https://catalogs.mast.stsci.edu/targets-file-help.html)
Crossmatch Search Radius
Arcminutes Arcseconds Degrees
Max = 3 Arcseconds
Wait: Success: Error:
**Targets that could not be resolved**
×
#####  **What to Search** Select the catalog type and release to search.
Release
PS1 DR1 PS1 DR2
Catalog
Mean object Stacked object Forced mean object Detections
[View Mean Search Table ](https://outerspace.stsci.edu/x/jgnOAQ)
#####  **Display Columns** Select the columns that will be displayed.**67** **selected**
ObjName IAU name for this object.
objAltName1 Alternate name for this object.
objAltName2 Altername name for this object.
objAltName3 Altername name for this object.
objID Unique object identifier.
uniquePspsOBid Unique internal PSPS object identifier.
ippObjID IPP internal object identifier.
surveyID Survey identifier. Details in the Survey table.
htmID Hierarchical triangular mesh (Szalay 2007) index.
zoneID Local zone index, found by dividing the sky into bands of declination 1/2 arcminute in height: zoneID = floor((90 + declination)/0.0083333).
tessID Tessellation identifier. Details in the TessellationType table.
projectionID Projection cell identifier.
skyCellID Skycell region identifier.
randomID Random value drawn from the interval between zero and one.
batchID Internal database batch identifier.
dvoRegionID Internal DVO region identifier.
processingVersion Data release version.
objInfoFlag Information flag bitmask indicating details of the photometry. Values listed in ObjectInfoFlags.
astrometryCorrectionFlag flag for astrometry correction update
qualityFlag Subset of objInfoFlag denoting whether this object is real or a likely false positive. Values listed in ObjectQualityFlags.
raStack Right ascension from stack detections, weighted mean value across filters, in equinox J2000. See StackObjectThin for stack epoch information.
decStack Declination from stack detections, weighted mean value across filters, in equinox J2000. See StackObjectThin for stack epoch information.
raStackErr Right ascension standard deviation from stack detections.
decStackErr Declination standard deviation from stack detections.
raMean Right ascension from single epoch detections (weighted mean) in equinox J2000 at the mean epoch given by epochMean.
decMean Declination from single epoch detections (weighted mean) in equinox J2000 at the mean epoch given by epochMean.
raMeanErr Right ascension standard deviation from single epoch detections.
decMeanErr Declination standard deviation from single epoch detections.
pmra proper motion in ra direction
pmdec proper moton in dec direction
pmraErr error in ra pm
pmdecErr error in dec pm
epochMean Modified Julian Date of the mean epoch corresponding to raMean, decMean (equinox J2000).
posMeanChisq Reduced chi squared value of mean position.
cx Cartesian x on a unit sphere.
cy Cartesian y on a unit sphere.
cz Cartesian z on a unit sphere.
lambda Ecliptic longitude.
beta Ecliptic latitude.
l Galactic longitude.
b Galactic latitude.
nStackObjectRows Number of independent StackObjectThin rows associated with this object.
nStackDetections Number of stack detections.
nDetections Number of single epoch detections in all filters.
ng Number of single epoch detections in g filter.
nr Number of single epoch detections in r filter.
ni Number of single epoch detections in i filter.
nz Number of single epoch detections in z filter.
ny Number of single epoch detections in y filter.
gQfPerfect Maximum PSF weighted fraction of pixels totally unmasked from g filter detections.
gMeanPSFMag Mean PSF magnitude from g filter detections.
gMeanPSFMagErr Error in mean PSF magnitude from g filter detections.
gMeanPSFMagStd Standard deviation of PSF magnitudes from g filter detections.
gMeanPSFMagNpt Number of measurements included in mean PSF magnitude from g filter detections.
gMeanPSFMagMin Minimum PSF magnitude from g filter detections.
gMeanPSFMagMax Maximum PSF magnitude from g filter detections.
gMeanKronMag Mean Kron (1980) magnitude from g filter detections.
gMeanKronMagErr Error in mean Kron (1980) magnitude from g filter detections.
gMeanKronMagStd Standard deviation of Kron (1980) magnitudes from g filter detections.
gMeanKronMagNpt Number of measurements included in mean Kron (1980) magnitude from g filter detections.
gMeanApMag Mean aperture magnitude from g filter detections.
gMeanApMagErr Error in mean aperture magnitude from g filter detections.
gMeanApMagStd Standard deviation of aperture magnitudes from g filter detections.
gMeanApMagNpt Number of measurements included in mean aperture magnitude from g filter detections.
gFlags Information flag bitmask for mean object from g filter detections. Values listed in ObjectFilterFlags.
rQfPerfect Maximum PSF weighted fraction of pixels totally unmasked from r filter detections.
rMeanPSFMag Mean PSF magnitude from r filter detections.
rMeanPSFMagErr Error in mean PSF magnitude from r filter detections.
rMeanPSFMagStd Standard deviation of PSF magnitudes from r filter detections.
rMeanPSFMagNpt Number of measurements included in mean PSF magnitude from r filter detections.
rMeanPSFMagMin Minimum PSF magnitude from r filter detections.
rMeanPSFMagMax Maximum PSF magnitude from r filter detections.
rMeanKronMag Mean Kron (1980) magnitude from r filter detections.
rMeanKronMagErr Error in mean Kron (1980) magnitude from r filter detections.
rMeanKronMagStd Standard deviation of Kron (1980) magnitudes from r filter detections.
rMeanKronMagNpt Number of measurements included in mean Kron (1980) magnitude from r filter detections.
rMeanApMag Mean aperture magnitude from r filter detections.
rMeanApMagErr Error in mean aperture magnitude from r filter detections.
rMeanApMagStd Standard deviation of aperture magnitudes from r filter detections.
rMeanApMagNpt Number of measurements included in mean aperture magnitude from r filter detections.
rFlags Information flag bitmask for mean object from r filter detections. Values listed in ObjectFilterFlags.
iQfPerfect Maximum PSF weighted fraction of pixels totally unmasked from i filter detections.
iMeanPSFMag Mean PSF magnitude from i filter detections.
iMeanPSFMagErr Error in mean PSF magnitude from i filter detections.
iMeanPSFMagStd Standard deviation of PSF magnitudes from i filter detections.
iMeanPSFMagNpt Number of measurements included in mean PSF magnitude from i filter detections.
iMeanPSFMagMin Minimum PSF magnitude from i filter detections.
iMeanPSFMagMax Maximum PSF magnitude from i filter detections.
iMeanKronMag Mean Kron (1980) magnitude from i filter detections.
iMeanKronMagErr Error in mean Kron (1980) magnitude from i filter detections.
iMeanKronMagStd Standard deviation of Kron (1980) magnitudes from i filter detections.
iMeanKronMagNpt Number of measurements included in mean Kron (1980) magnitude from i filter detections.
iMeanApMag Mean aperture magnitude from i filter detections.
iMeanApMagErr Error in mean aperture magnitude from i filter detections.
iMeanApMagStd Standard deviation of aperture magnitudes from i filter detections.
iMeanApMagNpt Number of measurements included in mean aperture magnitude from i filter detections.
iFlags Information flag bitmask for mean object from i filter detections. Values listed in ObjectFilterFlags.
zQfPerfect Maximum PSF weighted fraction of pixels totally unmasked from z filter detections.
zMeanPSFMag Mean PSF magnitude from z filter detections.
zMeanPSFMagErr Error in mean PSF magnitude from z filter detections.
zMeanPSFMagStd Standard deviation of PSF magnitudes from z filter detections.
zMeanPSFMagNpt Number of measurements included in mean PSF magnitude from z filter detections.
zMeanPSFMagMin Minimum PSF magnitude from z filter detections.
zMeanPSFMagMax Maximum PSF magnitude from z filter detections.
zMeanKronMag Mean Kron (1980) magnitude from z filter detections.
zMeanKronMagErr Error in mean Kron (1980) magnitude from z filter detections.
zMeanKronMagStd Standard deviation of Kron (1980) magnitudes from z filter detections.
zMeanKronMagNpt Number of measurements included in mean Kron (1980) magnitude from z filter detections.
zMeanApMag Mean aperture magnitude from z filter detections.
zMeanApMagErr Error in mean aperture magnitude from z filter detections.
zMeanApMagStd Standard deviation of aperture magnitudes from z filter detections.
zMeanApMagNpt Number of measurements included in mean aperture magnitude from z filter detections.
zFlags Information flag bitmask for mean object from z filter detections. Values listed in ObjectFilterFlags.
yQfPerfect Maximum PSF weighted fraction of pixels totally unmasked from y filter detections.
yMeanPSFMag Mean PSF magnitude from y filter detections.
yMeanPSFMagErr Error in mean PSF magnitude from y filter detections.
yMeanPSFMagStd Standard deviation of PSF magnitudes from y filter detections.
yMeanPSFMagNpt Number of measurements included in mean PSF magnitude from y filter detections.
yMeanPSFMagMin Minimum PSF magnitude from y filter detections.
yMeanPSFMagMax Maximum PSF magnitude from y filter detections.
yMeanKronMag Mean Kron (1980) magnitude from y filter detections.
yMeanKronMagErr Error in mean Kron (1980) magnitude from y filter detections.
yMeanKronMagStd Standard deviation of Kron (1980) magnitudes from y filter detections.
yMeanKronMagNpt Number of measurements included in mean Kron (1980) magnitude from y filter detections.
yMeanApMag Mean aperture magnitude from y filter detections.
yMeanApMagErr Error in mean aperture magnitude from y filter detections.
yMeanApMagStd Standard deviation of aperture magnitudes from y filter detections.
yMeanApMagNpt Number of measurements included in mean aperture magnitude from y filter detections.
yFlags Information flag bitmask for mean object from y filter detections. Values listed in ObjectFilterFlags.
Select All Clear All Select Recommended
#####  **Search Conditions** Select the rows that will be displayed.
![](https://catalogs.mast.stsci.edu/static/images/plus-sign.svg)
Add condition
ObjName objAltName1 objAltName2 objAltName3 objID uniquePspsOBid ippObjID surveyID htmID zoneID tessID projectionID skyCellID randomID batchID dvoRegionID processingVersion objInfoFlag astrometryCorrectionFlag qualityFlag raStack decStack raStackErr decStackErr raMean decMean raMeanErr decMeanErr pmra pmdec pmraErr pmdecErr epochMean posMeanChisq cx cy cz lambda beta l b nStackObjectRows nStackDetections nDetections ng nr ni nz ny gQfPerfect gMeanPSFMag gMeanPSFMagErr gMeanPSFMagStd gMeanPSFMagNpt gMeanPSFMagMin gMeanPSFMagMax gMeanKronMag gMeanKronMagErr gMeanKronMagStd gMeanKronMagNpt gMeanApMag gMeanApMagErr gMeanApMagStd gMeanApMagNpt gFlags rQfPerfect rMeanPSFMag rMeanPSFMagErr rMeanPSFMagStd rMeanPSFMagNpt rMeanPSFMagMin rMeanPSFMagMax rMeanKronMag rMeanKronMagErr rMeanKronMagStd rMeanKronMagNpt rMeanApMag rMeanApMagErr rMeanApMagStd rMeanApMagNpt rFlags iQfPerfect iMeanPSFMag iMeanPSFMagErr iMeanPSFMagStd iMeanPSFMagNpt iMeanPSFMagMin iMeanPSFMagMax iMeanKronMag iMeanKronMagErr iMeanKronMagStd iMeanKronMagNpt iMeanApMag iMeanApMagErr iMeanApMagStd iMeanApMagNpt iFlags zQfPerfect zMeanPSFMag zMeanPSFMagErr zMeanPSFMagStd zMeanPSFMagNpt zMeanPSFMagMin zMeanPSFMagMax zMeanKronMag zMeanKronMagErr zMeanKronMagStd zMeanKronMagNpt zMeanApMag zMeanApMagErr zMeanApMagStd zMeanApMagNpt zFlags yQfPerfect yMeanPSFMag yMeanPSFMagErr yMeanPSFMagStd yMeanPSFMagNpt yMeanPSFMagMin yMeanPSFMagMax yMeanKronMag yMeanKronMagErr yMeanKronMagStd yMeanKronMagNpt yMeanApMag yMeanApMagErr yMeanApMagStd yMeanApMagNpt yFlags
equals is less than or equal to is greater than or equal to is like
![](https://catalogs.mast.stsci.edu/static/images/minus-sign.svg)
Remove
Search Catalog
[![](https://catalogs.mast.stsci.edu/static/images/mastlogo_thumb.png)](https://archive.stsci.edu "Mikulski Archive for Space Telescopes \(MAST\)") [![](https://catalogs.mast.stsci.edu/static/images/stsci_dark.png)](https://www.stsci.edu "Space Telescope Science Institute")
Contact Us
