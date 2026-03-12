---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search"
date_accessed: "2026-03-11T11:36:48.210103"
---

<!-- CHUNK 1 START -->
Using an Application Programming Interface (API) to query and retrieve data from MAST is efficient, and you can customize scripts that use the APIs very easily. This tutorial illustrates how to formulate queries with the __Advanced Search__ feature of the MAST [Portal](https://mast.stsci.edu) web interface. To get started, we suggest trying the
**On this page...**
* 1[Prerequisites](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-Prerequisites)
* 1.1[API Libraries](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-APILibraries)
* 2[API Queries](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-APIQueries)
* 2.1[Query for Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-QueryforObservations)
* 2.2[Query for Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-QueryforDataProducts)
* 2.3[Example API Queries](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-ExampleAPIQueries)
* 3[Data Product Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-DataProductRetrieval)
* 3.1[Download Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-DownloadProducts)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Prerequisites"} -->
Searching and retrieving data from MAST using astroquery requires that you have:
1. A relatively recent version of python (3.8+ recommended) installed on your machine, as well as the
2. You must also install **astroquery** return **astropy** _`Table`_objects.
3. Have a valid [MAST.auth](https://auth.mast.stsci.edu/info) token if you wish to retrieve exclusive-access data.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Prerequisites", "Header 2": "API Libraries"} -->
Using the **`Observation`**class; specify parameter values to set search criteria. In a script or python session, begin by importing the necessary classes and methods:
```
from astroquery.mast import Observations
from astropy.table import unique, vstack, Table
```

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "API Queries"} -->
The workflow when using the API is analogous to that of using the Portal:
1. Use search criteria to match **Observations**
2. For each Observation of interest, find the specific data products contained within it
3. Use filters to select (or omit) specific categories of products, such as Science files, uncalibrated raw files, or guide-star files.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "API Queries", "Header 2": "Query for Observations"} -->
Consult the set of all [available parameters](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html) for **astroquery.mast**. Consider a search for JWST/NIRCam observations in observing program 1073, using the `F277W` filter. Use the **`.query_criteria()`**method to specify the query parameters:
```
matched_obs = Observations.query_criteria(
obs_collection = 'JWST',
proposal_id = '1073',
instrument_name = 'NIRCAM*',
filters = 'F277W',
)
```  
Note the asterisk following the instrument name: that allows for queries for all [instrument configurations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176435458/JWST+Instrument+Names). The result is an **astropy** `Table` object, with one row per matched observation.
If for a particular query you are not interested in observations from any mission except JWST, specify it with the parameter `obs_collection='JWST'`. This will narrow the list of possible matches considerably, and speed up your query.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "API Queries", "Header 2": "Query for Data Products"} -->
Having found Observations that match your criteria, the next step is to fetch a table of data products associated with each Observation.
Some observations contain huge numbers of associated or linked files, sometimes in excess of 10,000 products. This is particularly true for NIRSpec/MSA, MIRI/WFSS, and NIRCam/WFSS spectroscopy, but may also be true for large mosaics of images. Each observation is likely to contain many files in common, such as guide-star files and ancillary products.
**We recommend retrieving product lists for one or a few Observation(s) at a time to avoid server timeouts, and then to construct a set of unique products from the combined observations to avoid large numbers of duplicated products.**
The following retrieves a list of tables of data products for each observation, and returns combined table containing unique data products.
```
if (matched_obs > 0):
t = [Observations.get_product_list(obs) for obs in matched_obs]
files = unique(vstack(t), keys='productFilename')
```  
If at least one observation matched the search criteria the above call returns a table of unique products, one per row, which could number in the hundreds or thousands. You may wish to filter the results by masking all but a limited number of file suffixes and excluding certain sub-strings. Below is such a function, with the explicit option of excluding guide-star products.
**Filtering Filename Substrings** Expand source
```
def product_filter(table, prodList, gs_omit=True):
mask = np.full(len(table), False)
gs_text = '_gs-'
for r in table:
mk = False
fileName = r['productFilename']
for p in prodList:
if p in fileName:
mk = mk | True
if gs_text in fileName:
mk = not gs_omit

mask[r.index] = mk
return mask
```

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "API Queries", "Header 2": "Example API Queries"} -->
We recommended starting with the

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval"} -->
The selected products may now be downloaded to your local machine.
Auth.MAST Token
Note that you will need to login with a valid [Auth.MAST](https://auth.mast.stsci.edu/info) token to download exclusive access (EAP) data. If the token is needed but not supplied, the you will be prompted to enter one. In any case you have the option of logging in explicitly.
```
Observations.login()
```  
Token security
Typing tokens into a terminal or a Jupyter notebook is a security risk. The Observations.login() method takes care of this automatically by using

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval", "Header 2": "Download Products"} -->
You may download all the products in the files table, or select a subset if you prefer. The following will select L-1b products (i.e. the raw, uncalibrated, `*_uncal.fits`) from the data product list for retrieval. Other types of products may instead be selected, either by matching product name sub-strings or selecting named products in the `productSubGroupDescription`.
```
manifest = Observations.download_products(
files,
productSubGroupDescription='UNCAL',
curl_flag=True
#cloud_only=True
)
```

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval", "Header 2": "Download Products", "Header 3": "cURL Flag"} -->
Setting the optional `curl_flag` parameter to **`True`**will instead download a**bash** script that contains **cURL** commands to fetch the files at a later time. This approach can be useful for large numbers of files. The name of the download script will be something like: mastDownload_**YYYYMMDDhhmmss**.sh, where the latter part of the name is a numeric timestamp. What remains is to invoke the downloaded script on your machine to retrieve the files.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval", "Header 2": "Download Products", "Header 3": "Cloud Downloads"} -->
The `cloud_only` option will pull files from the [cloud copy of MAST data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data). This cloud service can be useful, since it generally has more bandwidth than our on-premises servers. However, it cannot be used with the cURL option, nor can it be used to access non-public (i.e. exclusive access period) files.
* * *

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
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
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
Using an Application Programming Interface (API) to query and retrieve data from MAST is efficient, and you can customize scripts that use the APIs very easily. This tutorial illustrates how to formulate queries with the __Advanced Search__ feature of the MAST [Portal](https://mast.stsci.edu) web interface. To get started, we suggest trying the
**On this page...**
* 1[Prerequisites](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-Prerequisites)
* 1.1[API Libraries](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-APILibraries)
* 2[API Queries](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-APIQueries)
* 2.1[Query for Observations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-QueryforObservations)
* 2.2[Query for Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-QueryforDataProducts)
* 2.3[Example API Queries](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-ExampleAPIQueries)
* 3[Data Product Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-DataProductRetrieval)
* 3.1[Download Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-DownloadProducts)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search#APIAdvancedSearch-ForFurtherReading...)

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Prerequisites"} -->
Searching and retrieving data from MAST using astroquery requires that you have:
1. A relatively recent version of python (3.8+ recommended) installed on your machine, as well as the
2. You must also install **astroquery** return **astropy** _`Table`_objects.
3. Have a valid [MAST.auth](https://auth.mast.stsci.edu/info) token if you wish to retrieve exclusive-access data.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Prerequisites", "Header 2": "API Libraries"} -->
Using the **`Observation`**class; specify parameter values to set search criteria. In a script or python session, begin by importing the necessary classes and methods:
```
from astroquery.mast import Observations
from astropy.table import unique, vstack, Table
```

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "API Queries"} -->
The workflow when using the API is analogous to that of using the Portal:
1. Use search criteria to match **Observations**
2. For each Observation of interest, find the specific data products contained within it
3. Use filters to select (or omit) specific categories of products, such as Science files, uncalibrated raw files, or guide-star files.

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "API Queries", "Header 2": "Query for Observations"} -->
Consult the set of all [available parameters](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html) for **astroquery.mast**. Consider a search for JWST/NIRCam observations in observing program 1073, using the `F277W` filter. Use the **`.query_criteria()`**method to specify the query parameters:
```
matched_obs = Observations.query_criteria(
obs_collection = 'JWST',
proposal_id = '1073',
instrument_name = 'NIRCAM*',
filters = 'F277W',
)
```  
Note the asterisk following the instrument name: that allows for queries for all [instrument configurations](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176435458/JWST+Instrument+Names). The result is an **astropy** `Table` object, with one row per matched observation.
If for a particular query you are not interested in observations from any mission except JWST, specify it with the parameter `obs_collection='JWST'`. This will narrow the list of possible matches considerably, and speed up your query.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "API Queries", "Header 2": "Query for Data Products"} -->
Having found Observations that match your criteria, the next step is to fetch a table of data products associated with each Observation.
Some observations contain huge numbers of associated or linked files, sometimes in excess of 10,000 products. This is particularly true for NIRSpec/MSA, MIRI/WFSS, and NIRCam/WFSS spectroscopy, but may also be true for large mosaics of images. Each observation is likely to contain many files in common, such as guide-star files and ancillary products.
**We recommend retrieving product lists for one or a few Observation(s) at a time to avoid server timeouts, and then to construct a set of unique products from the combined observations to avoid large numbers of duplicated products.**
The following retrieves a list of tables of data products for each observation, and returns combined table containing unique data products.
```
if (matched_obs > 0):
t = [Observations.get_product_list(obs) for obs in matched_obs]
files = unique(vstack(t), keys='productFilename')
```  
If at least one observation matched the search criteria the above call returns a table of unique products, one per row, which could number in the hundreds or thousands. You may wish to filter the results by masking all but a limited number of file suffixes and excluding certain sub-strings. Below is such a function, with the explicit option of excluding guide-star products.
**Filtering Filename Substrings** Expand source
```
def product_filter(table, prodList, gs_omit=True):
mask = np.full(len(table), False)
gs_text = '_gs-'
for r in table:
mk = False
fileName = r['productFilename']
for p in prodList:
if p in fileName:
mk = mk | True
if gs_text in fileName:
mk = not gs_omit

mask[r.index] = mk
return mask
```

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "API Queries", "Header 2": "Example API Queries"} -->
We recommended starting with the

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval"} -->
The selected products may now be downloaded to your local machine.
Auth.MAST Token
Note that you will need to login with a valid [Auth.MAST](https://auth.mast.stsci.edu/info) token to download exclusive access (EAP) data. If the token is needed but not supplied, the you will be prompted to enter one. In any case you have the option of logging in explicitly.
```
Observations.login()
```  
Token security
Typing tokens into a terminal or a Jupyter notebook is a security risk. The Observations.login() method takes care of this automatically by using

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval", "Header 2": "Download Products"} -->
You may download all the products in the files table, or select a subset if you prefer. The following will select L-1b products (i.e. the raw, uncalibrated, `*_uncal.fits`) from the data product list for retrieval. Other types of products may instead be selected, either by matching product name sub-strings or selecting named products in the `productSubGroupDescription`.
```
manifest = Observations.download_products(
files,
productSubGroupDescription='UNCAL',
curl_flag=True
#cloud_only=True
)
```

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval", "Header 2": "Download Products", "Header 3": "cURL Flag"} -->
Setting the optional `curl_flag` parameter to **`True`**will instead download a**bash** script that contains **cURL** commands to fetch the files at a later time. This approach can be useful for large numbers of files. The name of the download script will be something like: mastDownload_**YYYYMMDDhhmmss**.sh, where the latter part of the name is a numeric timestamp. What remains is to invoke the downloaded script on your machine to retrieve the files.

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "Data Product Retrieval", "Header 2": "Download Products", "Header 3": "Cloud Downloads"} -->
The `cloud_only` option will pull files from the [cloud copy of MAST data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data). This cloud service can be useful, since it generally has more bandwidth than our on-premises servers. However, it cannot be used with the cURL option, nor can it be used to access non-public (i.e. exclusive access period) files.
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 23 END -->

