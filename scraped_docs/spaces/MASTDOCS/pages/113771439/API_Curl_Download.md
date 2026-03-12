---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download"
date_accessed: "2026-03-11T11:36:51.183201"
---

<!-- CHUNK 1 START -->
When downloading large files, or a large number of them, it is often advisable to use a bash script to download via the API. These scripts use the
**On this page...**
* 1[Example Bash Script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-ExampleBashScript)
* 1.1[The API Token](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-TheAPIToken)
* 1.2[Retrieve Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-RetrieveFiles)
* 2[Interactive Python Example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-InteractivePythonExample)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Example Bash Script"} -->
When retrieving a selection of files from the MAST Portal, one of the download options is an auto-generated **bash** (shell) script. Note that this option will download only the script; the actual files are download when the script is run.
If you would like to customize the example script provided here to access data files in MAST, you will first need to determine the URIs for the files of interest using another API, e.g., astroquery.mast. See the 'Interactive Example' section down below to try it yourself.
You must invoke the script in a unix terminal to download the files:
```
bash MAST_2022-04-30T2140.sh
```  
A look at the example script [MAST_2022-04-30T2153.sh](https://outerspace.stsci.edu/download/attachments/113771439/MAST_2022-04-30T2153.sh?version=1&modificationDate=1657650330960&api=v2) shows that, apart from some housekeeping, it does a few main things:
1. For [EAP protected data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide), fetch the [MAST API Token](https://auth.mast.stsci.edu/info)
2. Create a folder for the payload
3. Create a `MANIFEST.HTML` file to report status of the requested vs. retrieved data files
4. Retrieve each data file with a cURL command  
Items 1 and 4 are described below in more detail.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Example Bash Script", "Header 2": "The API Token"} -->
If the requested files include at least one with EAP protection, a MAST API token is required. As the following code snippet shows, the bash script will attempt to get the MAST token multiple ways.
**Supplying the MAST Token** Expand source
```
# Check for command-line argument
if [ -z "$1" ]
then
# Check for environment variable
if [ -z "$MAST_API_TOKEN" ]
then
# Prompt the user
echo "Please enter your token here: "
read MAST_API_TOKEN
fi
else
MAST_API_TOKEN=$1
fi
```

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Example Bash Script", "Header 2": "Retrieve Files"} -->
The following code snippet shows how each file is retrieved with cURL. For readability, the cURL command is re-formatted here as multi-line, with linux/MacOS escape characters.
**cURL File Retrieval** Expand source
```
# Announce the file
cat <<EOT
<<< Downloading
File: mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_i2d.fits
To: ${DOWNLOAD_FOLDER}/JWST/jw01409-o031_t014_nircam_clear-f212n/jw01409-o031_t014_nircam_clear-f212n_i2d.fits
EOT
# Retrieve the file
curl -H "Authorization: token $MAST_API_TOKEN" \
--globoff \
--location-trusted \
-f \
--progress-bar \
--create-dirs $CONT \
--output ./${DOWNLOAD_FOLDER}'/JWST/jw01409-o031_t014_nircam_clear-f212n/jw00839-o003_t001_miri_f560w_i2d.fits' \
'https://mast.stsci.edu/jwst/api/v0.1/Download/file?bundle_name=MAST_2022-04-30T2153&uri=mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_i2d.fits'

# Announce the second file
cat <<EOT
<<< Downloading
File: mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv
To: ${DOWNLOAD_FOLDER}/JWST/jw01409-o031_t014_nircam_clear-f212n/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv
EOT
# Retrieve the second file
curl -H "Authorization: token $MAST_API_TOKEN" \
--globoff \
--location-trusted \
-f \
--progress-bar \
--create-dirs $CONT \
--output ./${DOWNLOAD_FOLDER}'/JWST/jw01409-o031_t014_nircam_clear-f212n/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv' \
'https://mast.stsci.edu/jwst/api/v0.1/Download/file?bundle_name=MAST_2022-04-30T2153&uri=mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv'


```  
It is worth calling out two important cURL command-line options:
* **`-H`**: pass custom header to the server. In this case, the MAST auth token
* `**--location-trusted**`: Follow re-directs, and send auth to other hosts

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Interactive Python Example"} -->
In addition to requesting a cURL script from the MAST Portal, you can get one from the astroquery.mast Python API. We offer an interactive
For completeness, we also reproduce that code on this webpage. To begin, you must import the necessary packages. You'll need astroquery.mast to access the API, and astropy.table to handle the results, which are returned as a Table object. Then you can create a query, searching on any of the [fields listed on our API page](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html). Here we'll query for JWST NIRCam observations, and specify a specific proposal ID.
**Imports and Initial Query** Expand source
```
from astroquery.mast import Observations
from astropy.table import unique, vstack, Table

matched_obs = Observations.query_criteria(
obs_collection = 'JWST',
proposal_id = '1073',
instrument_name = 'NIRCam',
)
```  
The above code will return only matched  _observations_. Each observation has a set of files associated with it; these may be guide-star images, uncalibrated exposures, or the final calibrated science product. In any case, we will need to retrieve all of these products before we can filter the results.
Requesting the products for many observations at once increases the risk of timeout errors. However, requesting products one at a time is often slow. The best balance is achieved by requesting products in groups of five.
**Optimizing Product Requests** Expand source
```
# Split the observations into "chunks" of size five
sz_chunk = 5
chunks = [matched_obs[i:i+sz_chunk] for i in range(0,len(matched_obs), sz_chunk)]

# Get the list of products for each chunk
t = [Observations.get_product_list(chunk) for chunk in chunks]

# Combine, and keep only the unique files
files = unique(vstack(t), keys='productFilename')
```  
With our set of unique files, all that remains is to pass the table to the download products function. We also include the 'extension' filter to limit our download to .fits files. Any criteria listed on the [products fields page](https://mast.stsci.edu/api/v0/_productsfields.html) may also be used.
**Downloading Files** Expand source
```
manifest = Observations.download_products(
files,
extension='fits',
curl_flag=True,
)
```

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Web Services](https://archive.stsci.edu/vo/mast_services.html)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
* [API Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search "API Advanced Search")
* [API Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download "API Curl Download")
* [API for JWST Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata "API for JWST Metadata")
* [API for JWST Science Pixels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113031/API+for+JWST+Science+Pixels "API for JWST Science Pixels")
* [Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API "Basics of an API")
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
* [Keyword Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771333/Keyword+Metadata "Keyword Metadata")
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data "Engineering Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
* [API Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search "API Advanced Search")
* [API Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download "API Curl Download")
* [API for JWST Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata "API for JWST Metadata")
* [API for JWST Science Pixels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113031/API+for+JWST+Science+Pixels "API for JWST Science Pixels")
* [Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API "Basics of an API")
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
When downloading large files, or a large number of them, it is often advisable to use a bash script to download via the API. These scripts use the
**On this page...**
* 1[Example Bash Script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-ExampleBashScript)
* 1.1[The API Token](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-TheAPIToken)
* 1.2[Retrieve Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-RetrieveFiles)
* 2[Interactive Python Example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-InteractivePythonExample)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download#APICurlDownload-ForFurtherReading...)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Example Bash Script"} -->
When retrieving a selection of files from the MAST Portal, one of the download options is an auto-generated **bash** (shell) script. Note that this option will download only the script; the actual files are download when the script is run.
If you would like to customize the example script provided here to access data files in MAST, you will first need to determine the URIs for the files of interest using another API, e.g., astroquery.mast. See the 'Interactive Example' section down below to try it yourself.
You must invoke the script in a unix terminal to download the files:
```
bash MAST_2022-04-30T2140.sh
```  
A look at the example script [MAST_2022-04-30T2153.sh](https://outerspace.stsci.edu/download/attachments/113771439/MAST_2022-04-30T2153.sh?version=1&modificationDate=1657650330960&api=v2) shows that, apart from some housekeeping, it does a few main things:
1. For [EAP protected data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide), fetch the [MAST API Token](https://auth.mast.stsci.edu/info)
2. Create a folder for the payload
3. Create a `MANIFEST.HTML` file to report status of the requested vs. retrieved data files
4. Retrieve each data file with a cURL command  
Items 1 and 4 are described below in more detail.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Example Bash Script", "Header 2": "The API Token"} -->
If the requested files include at least one with EAP protection, a MAST API token is required. As the following code snippet shows, the bash script will attempt to get the MAST token multiple ways.
**Supplying the MAST Token** Expand source
```
# Check for command-line argument
if [ -z "$1" ]
then
# Check for environment variable
if [ -z "$MAST_API_TOKEN" ]
then
# Prompt the user
echo "Please enter your token here: "
read MAST_API_TOKEN
fi
else
MAST_API_TOKEN=$1
fi
```

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Example Bash Script", "Header 2": "Retrieve Files"} -->
The following code snippet shows how each file is retrieved with cURL. For readability, the cURL command is re-formatted here as multi-line, with linux/MacOS escape characters.
**cURL File Retrieval** Expand source
```
# Announce the file
cat <<EOT
<<< Downloading
File: mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_i2d.fits
To: ${DOWNLOAD_FOLDER}/JWST/jw01409-o031_t014_nircam_clear-f212n/jw01409-o031_t014_nircam_clear-f212n_i2d.fits
EOT
# Retrieve the file
curl -H "Authorization: token $MAST_API_TOKEN" \
--globoff \
--location-trusted \
-f \
--progress-bar \
--create-dirs $CONT \
--output ./${DOWNLOAD_FOLDER}'/JWST/jw01409-o031_t014_nircam_clear-f212n/jw00839-o003_t001_miri_f560w_i2d.fits' \
'https://mast.stsci.edu/jwst/api/v0.1/Download/file?bundle_name=MAST_2022-04-30T2153&uri=mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_i2d.fits'

# Announce the second file
cat <<EOT
<<< Downloading
File: mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv
To: ${DOWNLOAD_FOLDER}/JWST/jw01409-o031_t014_nircam_clear-f212n/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv
EOT
# Retrieve the second file
curl -H "Authorization: token $MAST_API_TOKEN" \
--globoff \
--location-trusted \
-f \
--progress-bar \
--create-dirs $CONT \
--output ./${DOWNLOAD_FOLDER}'/JWST/jw01409-o031_t014_nircam_clear-f212n/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv' \
'https://mast.stsci.edu/jwst/api/v0.1/Download/file?bundle_name=MAST_2022-04-30T2153&uri=mast:JWST/product/jw01409-o031_t014_nircam_clear-f212n_cat.ecsv'


```  
It is worth calling out two important cURL command-line options:
* **`-H`**: pass custom header to the server. In this case, the MAST auth token
* `**--location-trusted**`: Follow re-directs, and send auth to other hosts

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Interactive Python Example"} -->
In addition to requesting a cURL script from the MAST Portal, you can get one from the astroquery.mast Python API. We offer an interactive
For completeness, we also reproduce that code on this webpage. To begin, you must import the necessary packages. You'll need astroquery.mast to access the API, and astropy.table to handle the results, which are returned as a Table object. Then you can create a query, searching on any of the [fields listed on our API page](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html). Here we'll query for JWST NIRCam observations, and specify a specific proposal ID.
**Imports and Initial Query** Expand source
```
from astroquery.mast import Observations
from astropy.table import unique, vstack, Table

matched_obs = Observations.query_criteria(
obs_collection = 'JWST',
proposal_id = '1073',
instrument_name = 'NIRCam',
)
```  
The above code will return only matched  _observations_. Each observation has a set of files associated with it; these may be guide-star images, uncalibrated exposures, or the final calibrated science product. In any case, we will need to retrieve all of these products before we can filter the results.
Requesting the products for many observations at once increases the risk of timeout errors. However, requesting products one at a time is often slow. The best balance is achieved by requesting products in groups of five.
**Optimizing Product Requests** Expand source
```
# Split the observations into "chunks" of size five
sz_chunk = 5
chunks = [matched_obs[i:i+sz_chunk] for i in range(0,len(matched_obs), sz_chunk)]

# Get the list of products for each chunk
t = [Observations.get_product_list(chunk) for chunk in chunks]

# Combine, and keep only the unique files
files = unique(vstack(t), keys='productFilename')
```  
With our set of unique files, all that remains is to pass the table to the download products function. We also include the 'extension' filter to limit our download to .fits files. Any criteria listed on the [products fields page](https://mast.stsci.edu/api/v0/_productsfields.html) may also be used.
**Downloading Files** Expand source
```
manifest = Observations.download_products(
files,
extension='fits',
curl_flag=True,
)
```

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Web Services](https://archive.stsci.edu/vo/mast_services.html)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

