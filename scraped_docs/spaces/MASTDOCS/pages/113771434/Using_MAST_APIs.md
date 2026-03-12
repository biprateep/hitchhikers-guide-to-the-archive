---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs"
date_accessed: "2026-03-11T11:33:37.262213"
---

<!-- CHUNK 1 START -->
MAST application programming interfaces (APIs) provide a direct and efficient means for experienced users to search for and retrieve data products. The APIs that are most relevant for JWST are illustrated via a collection of tutorials which you can customize to your own scientific needs.
**On this page...**
* 1[MAST Web Services](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-MASTWebServices)
* 1.1[Auth.MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-authAuth.MAST)
* 2[API Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-APITutorialsAPITutorials)
* 2.1[Astroquery Search and Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-AstroquerySearchandRetrieval)
* 2.2[Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-CurlDownload)
* 2.3[MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-MASTAPI)
* 2.4[Duplication Check](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-DuplicationCheckDuplicationCheck)
* 2.5[JWST Engineering Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-EngDataRetrievalJWSTEngineeringDataRetrieval)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "MAST Web Services"} -->
Much of the functionality of MAST is provided through a variety of [MAST web services](https://archive.stsci.edu/vo/mast_services.html) to provide data search, selection, and retrieval functionality. Most of these same services are available to users via multiple MAST application programming interfaces (APIs). These APIs offer a very efficient means to create custom, scripted access to JWST data products. The figure below is a simplified view of the interaction between users and MAST back-end services.  
![Cartoon of MAST user interaction with MAST web services](https://outerspace.stsci.edu/download/attachments/113771434/MAST_services.png?version=1&modificationDate=1630415472947&api=v2)
**Figure 1 —** Users (_right_) interact with a MAST Web UI or an API, either of which call back-end services (_left_) to access databases and data files. The information is retrieved and is forwarded back to the interface.
Most data in MAST can be retrieved anonymously. But retrieving protected data with an API requires both **_authentication_** and _**authorization**_. Authorization is granted by MAST to program Principal Investigators, and may be granted by a PI to their collaborators. Authentication in the Portal is achieved by logging in with your MyST credentials; authentication for scripted retrieval is achieved with a [MAST API token](https://auth.mast.stsci.edu/info). These tokens, which are long alpha-numeric strings, may be provided to a script:
* with a command-line argument
* by a user responding to a prompt
* by storing the token string in the shell environment variable `$MAST_API_TOKEN`
* Users of bash can do this _**in the shell they use to access an API**_ with the following command (or, optionally, store in their **`.bashrc`**file):
```
export MAST_API_TOKEN=<token string>
```  
Generate the token with the [tokens](https://auth.mast.stsci.edu/tokens) page.
Token Expiration Policy
For security reasons MAST tokens expire after 10 days of inactivity or 60 days after creation, whichever comes first. If you have a script which used to work but now fails with an authorization error, check to see if your token is still active. It is easy to generate a new MAST token.
The following subsections provide a variety of examples of how to use the MAST APIs with Python or shell scripts. For a more extensive discussion of MAST APIs, with many more worked examples, see [MAST Web Services](https://archive.stsci.edu/vo/mast_services.html). Some of the tutorials below take the form of Jupyter Notebooks, which reside in the
* * *

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "MAST Web Services", "Header 2": "Astroquery Search and Retrieval"} -->
The Python package **astroquery** provides a general means of creating custom scripts to access astronomical data repositories;
Large JWST Queries
The most highly calibrated and combined JWST observations may contain a very large number (thousands) of data products. These observations may cause timeouts or other performance problems for the Portal application. The tutorials mentioned here provide a robust method for dealing with large numbers of observations and data products.
* [API Advanced Search Tutorial](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search)  
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "MAST Web Services", "Header 2": "Curl Download"} -->
One option for retrieving data via the Portal [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) is to retrieve a "Curl" script. This is in reality a **bash** script which includes [example download script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download) to learn how it works; from this you can create your own download script.
You must know the URI(s) for the data file(s) you wish to download. These may be obtained with a different API, e.g., with an astroquery search.
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "MAST Web Services", "Header 2": "MAST API"} -->
The MAST web services may be called directly, through a
* [MAST API documentation](https://mast.stsci.edu/api/v0/)  
* * *
It is important for investigators who are preparing JWST observing proposals to know in advance if their intended targets might duplicate existing or planned JWST observations. This Jupyter notebook will help:
While helpful, JWST planned observations in MAST do not provide sufficient information to determine if a genuine duplication exists. For instance, parallel observations are omitted, and the prime target orientation may not be known until the visits are scheduled. The results in the notebook will include a link to the program APT file, which should be consulted to evaluate any potential duplication identified in MAST.
* * *
The JWST Engineering Database contents are described in the chapter on [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data). The EDB Retrieval tutorial shows how to retrieve multiple mnemonics over independent time ranges using Python. There is also an example Python script which you may customize for your own use. Both of these methods require a valid [MAST.auth token](https://auth.mast.stsci.edu/tokens).
*  
* Calibrated Engineering Data access via  
* * *

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Web Services](https://archive.stsci.edu/vo/mast_services.html)
* [MAST Authorization](https://auth.mast.stsci.edu/info)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) chapter on [MAST web services](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962884/Beyond+the+Portal)
* [CAOM Field Descriptions](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html)  
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
* [Science Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products "Science Data Products")
* [Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771323/Supplemental+Products "Supplemental Products")
* [Data Product File Formats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/117833935/Data+Product+File+Formats "Data Product File Formats")
* [Data Product Linkages](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771324/Data+Product+Linkages "Data Product Linkages")
* [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal "Linkages in the Portal")
* [Keyword Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771333/Keyword+Metadata "Keyword Metadata")
* [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data "Engineering Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Data Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771354/Data+Search "Data Search")
* [Data Visualization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771401/Data+Visualization "Data Visualization")
* [Data Selection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771408/Data+Selection "Data Selection")
* [Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771412/Data+Retrieval "Data Retrieval")
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
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [JWST Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677647/JWST+Supplemental+Products "JWST Supplemental Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [RITA](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168349/RITA "RITA")
* [RomanCal Refererence Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333678054/RomanCal+Refererence+Products "RomanCal Refererence Products")
* [Roman Supplemental Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677656/Roman+Supplemental+Products "Roman Supplemental Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
MAST application programming interfaces (APIs) provide a direct and efficient means for experienced users to search for and retrieve data products. The APIs that are most relevant for JWST are illustrated via a collection of tutorials which you can customize to your own scientific needs.
**On this page...**
* 1[MAST Web Services](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-MASTWebServices)
* 1.1[Auth.MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-authAuth.MAST)
* 2[API Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-APITutorialsAPITutorials)
* 2.1[Astroquery Search and Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-AstroquerySearchandRetrieval)
* 2.2[Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-CurlDownload)
* 2.3[MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-MASTAPI)
* 2.4[Duplication Check](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-DuplicationCheckDuplicationCheck)
* 2.5[JWST Engineering Data Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-EngDataRetrievalJWSTEngineeringDataRetrieval)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-ForFurtherReading...)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "MAST Web Services"} -->
Much of the functionality of MAST is provided through a variety of [MAST web services](https://archive.stsci.edu/vo/mast_services.html) to provide data search, selection, and retrieval functionality. Most of these same services are available to users via multiple MAST application programming interfaces (APIs). These APIs offer a very efficient means to create custom, scripted access to JWST data products. The figure below is a simplified view of the interaction between users and MAST back-end services.  
![Cartoon of MAST user interaction with MAST web services](https://outerspace.stsci.edu/download/attachments/113771434/MAST_services.png?version=1&modificationDate=1630415472947&api=v2)
**Figure 1 —** Users (_right_) interact with a MAST Web UI or an API, either of which call back-end services (_left_) to access databases and data files. The information is retrieved and is forwarded back to the interface.
Most data in MAST can be retrieved anonymously. But retrieving protected data with an API requires both **_authentication_** and _**authorization**_. Authorization is granted by MAST to program Principal Investigators, and may be granted by a PI to their collaborators. Authentication in the Portal is achieved by logging in with your MyST credentials; authentication for scripted retrieval is achieved with a [MAST API token](https://auth.mast.stsci.edu/info). These tokens, which are long alpha-numeric strings, may be provided to a script:
* with a command-line argument
* by a user responding to a prompt
* by storing the token string in the shell environment variable `$MAST_API_TOKEN`
* Users of bash can do this _**in the shell they use to access an API**_ with the following command (or, optionally, store in their **`.bashrc`**file):
```
export MAST_API_TOKEN=<token string>
```  
Generate the token with the [tokens](https://auth.mast.stsci.edu/tokens) page.
Token Expiration Policy
For security reasons MAST tokens expire after 10 days of inactivity or 60 days after creation, whichever comes first. If you have a script which used to work but now fails with an authorization error, check to see if your token is still active. It is easy to generate a new MAST token.
The following subsections provide a variety of examples of how to use the MAST APIs with Python or shell scripts. For a more extensive discussion of MAST APIs, with many more worked examples, see [MAST Web Services](https://archive.stsci.edu/vo/mast_services.html). Some of the tutorials below take the form of Jupyter Notebooks, which reside in the
* * *

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "MAST Web Services", "Header 2": "Astroquery Search and Retrieval"} -->
The Python package **astroquery** provides a general means of creating custom scripts to access astronomical data repositories;
Large JWST Queries
The most highly calibrated and combined JWST observations may contain a very large number (thousands) of data products. These observations may cause timeouts or other performance problems for the Portal application. The tutorials mentioned here provide a robust method for dealing with large numbers of observations and data products.
* [API Advanced Search Tutorial](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search)  
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "MAST Web Services", "Header 2": "Curl Download"} -->
One option for retrieving data via the Portal [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket) is to retrieve a "Curl" script. This is in reality a **bash** script which includes [example download script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download) to learn how it works; from this you can create your own download script.
You must know the URI(s) for the data file(s) you wish to download. These may be obtained with a different API, e.g., with an astroquery search.
* * *

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "MAST Web Services", "Header 2": "MAST API"} -->
The MAST web services may be called directly, through a
* [MAST API documentation](https://mast.stsci.edu/api/v0/)  
* * *
It is important for investigators who are preparing JWST observing proposals to know in advance if their intended targets might duplicate existing or planned JWST observations. This Jupyter notebook will help:
While helpful, JWST planned observations in MAST do not provide sufficient information to determine if a genuine duplication exists. For instance, parallel observations are omitted, and the prime target orientation may not be known until the visits are scheduled. The results in the notebook will include a link to the program APT file, which should be consulted to evaluate any potential duplication identified in MAST.
* * *
The JWST Engineering Database contents are described in the chapter on [Engineering Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data). The EDB Retrieval tutorial shows how to retrieve multiple mnemonics over independent time ranges using Python. There is also an example Python script which you may customize for your own use. Both of these methods require a valid [MAST.auth token](https://auth.mast.stsci.edu/tokens).
*  
* Calibrated Engineering Data access via  
* * *

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Web Services](https://archive.stsci.edu/vo/mast_services.html)
* [MAST Authorization](https://auth.mast.stsci.edu/info)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) chapter on [MAST web services](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962884/Beyond+the+Portal)
* [CAOM Field Descriptions](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

