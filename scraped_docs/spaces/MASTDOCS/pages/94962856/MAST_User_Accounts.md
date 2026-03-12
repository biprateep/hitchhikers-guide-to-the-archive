---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts"
date_accessed: "2026-03-11T11:31:57.574592"
---

<!-- CHUNK 1 START -->
User accounts are necessary to access protected data in MAST, and to make use of certain Portal functionality.
**On this page...**
* 1[Anonymous Use](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-AnonymousUse)
* 2[User Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-UserAccounts)
* 2.1[Data Authorization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-DataAuthorization)
* 2.2[Login](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-Login)
* 2.3[Logout](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-Logout)
* 3[Auth.MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-Auth.MAST)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-ForFurtherReading...)
* 4.1[Related Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-RelatedTopics)
* 4.2[Reference Information](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-ReferenceInformation)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Anonymous Use"} -->
Anyone can use the MAST Portal to search for hosted data. Anonymous users may retrieve any publicly-available data.
![A search resulting in EAP data, showing yellow rows and a black lock icon](https://outerspace.stsci.edu/download/thumbnails/94962856/eap_logo_new.png?version=1&modificationDate=1657650111096&api=v2)
Be aware that recent data from active missions are often protected for an [Exclusive Access Period](https://archive.stsci.edu/publishing/data-use#section-24a4fb60-93bc-4b19-803e-e8e7b04e8823) (**EAP**). This is a limited period of time just after an observation, during which only _authorized_ and _authenticated_ users (i.e., the Investigator team) may retrieve the data. Such protected data are designated in the Portal results table with a yellow row background and the black "lock" icon seen on the left.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "User Accounts"} -->
There are some important circumstances where you will need an account for MAST:
* Retrieval of data protected by an EAP, whether through the Portal or through scripted access
* Viewing preview images in the Portal results table for EAP protected data
* [Subscribing to data notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications) for active missions  
The MAST Portal uses the same MyST Accounts used by other STScI services, such as proposal submission. If you do not already have an account, one can be set up quickly through the [MyST Portal](https://proper.stsci.edu/proper/authentication/auth).
* * *
![MyST landing page with three columns - Create, Update, and Manage Accounts](https://outerspace.stsci.edu/download/thumbnails/94962856/myst_landing.png?version=1&modificationDate=1657650111642&api=v2)

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "User Accounts", "Header 2": "Data Authorization"} -->
Permission to access EAP data is also controlled through your MyST Account. Principal Investigators (PI's) of observing programs are automatically granted access to this data. PIs of programs may also authorize other users to access the data during the EAP period by navigating to the MyST Home screen and selecting the **Update Your Account** option. From there click the **Manage Access to Exclusive-Access Science Data** menu option, select your program, and enter the MyST email address of record for your colleague.
* * *
![Login info and button](https://outerspace.stsci.edu/download/thumbnails/94962856/login_Portal.png?version=1&modificationDate=1657650111204&api=v2)

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "User Accounts", "Header 2": "Login"} -->
Be sure to login to the Portal before attempting to retrieve **EAP** data, or before attempting to subscribe to data notifications. Just click the _**_Login..._**_ text.
* * *  
![Logout button](https://outerspace.stsci.edu/download/thumbnails/94962856/button_Logout.png?version=1&modificationDate=1657650111137&api=v2)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "User Accounts", "Header 2": "Logout"} -->
If for security reasons you must log out of a Portal session (e.g., if you are obliged to share your workstation), go to <https://auth.mast.stsci.edu/sessions>. That page will contain an entry for each active MAST session for which you are logged in. Click the _**Log Out**_ button to terminate the session in question. Then visit the SSO portal to log out of the MyST system: <https://ssoportal.stsci.edu/idp/profile/Logout>.
Another option is to use an Incognito (or Private) browser instance when using the Portal. Logging out would be as simple as closing the Incognito window. The next user can login with another incognito window to start a fresh session.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Auth.MAST"} -->
MAST also offers API token authorization for programmatic access to EAP data. Users with a MyST Account can find instructions on creating and using these tokens on the [auth.MAST documentation page](https://auth.mast.stsci.edu/info). With a valid token in place, authorized users will then be able to retrieve MAST EAP data through __Using Auth.AST Tokens__ in the [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials) chapter. The steps are simply:
1. Navigate to the [Tokens](https://auth.mast.stsci.edu/tokens) page and click the button.
2. Record the long, alpha-numeric string in the environment variable `$MAST_API_TOKEN`, preferably in your `.bashrc` file.  
Be aware that API tokens will expire after 10 days of inactivity or 60 days after creation, whichever comes first. Users experiencing any trouble with existing tokens should first try generating new ones.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "For Further Reading...", "Header 2": "Related Topics"} -->
* [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications)
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data)
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data)

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading...", "Header 2": "Reference Information"} -->
* [MyST Portal](https://proper.stsci.edu/proper/authentication/auth)
* [Auth.MAST Documentation](https://auth.mast.stsci.edu/info)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [Introduction to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962826/Introduction+to+the+Portal "Introduction to the Portal")
* [Field Guide to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962827/Field+Guide+to+the+Portal "Field Guide to the Portal")
* [Data Holdings](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962855/Data+Holdings "Data Holdings")
* [MAST User Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts "MAST User Accounts")
* [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications "Program Subscriptions and Notifications")
* [Beyond the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962884/Beyond+the+Portal "Beyond the Portal")
* [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching "Searching")
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data "Browsing Data")
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
* [Tips and Notes](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963055/Tips+and+Notes "Tips and Notes")
* [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials "Demos and Tutorials")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
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
User accounts are necessary to access protected data in MAST, and to make use of certain Portal functionality.
**On this page...**
* 1[Anonymous Use](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-AnonymousUse)
* 2[User Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-UserAccounts)
* 2.1[Data Authorization](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-DataAuthorization)
* 2.2[Login](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-Login)
* 2.3[Logout](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-Logout)
* 3[Auth.MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-Auth.MAST)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-ForFurtherReading...)
* 4.1[Related Topics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-RelatedTopics)
* 4.2[Reference Information](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962856/MAST+User+Accounts#MASTUserAccounts-ReferenceInformation)

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Anonymous Use"} -->
Anyone can use the MAST Portal to search for hosted data. Anonymous users may retrieve any publicly-available data.
![A search resulting in EAP data, showing yellow rows and a black lock icon](https://outerspace.stsci.edu/download/thumbnails/94962856/eap_logo_new.png?version=1&modificationDate=1657650111096&api=v2)
Be aware that recent data from active missions are often protected for an [Exclusive Access Period](https://archive.stsci.edu/publishing/data-use#section-24a4fb60-93bc-4b19-803e-e8e7b04e8823) (**EAP**). This is a limited period of time just after an observation, during which only _authorized_ and _authenticated_ users (i.e., the Investigator team) may retrieve the data. Such protected data are designated in the Portal results table with a yellow row background and the black "lock" icon seen on the left.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "User Accounts"} -->
There are some important circumstances where you will need an account for MAST:
* Retrieval of data protected by an EAP, whether through the Portal or through scripted access
* Viewing preview images in the Portal results table for EAP protected data
* [Subscribing to data notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications) for active missions  
The MAST Portal uses the same MyST Accounts used by other STScI services, such as proposal submission. If you do not already have an account, one can be set up quickly through the [MyST Portal](https://proper.stsci.edu/proper/authentication/auth).
* * *
![MyST landing page with three columns - Create, Update, and Manage Accounts](https://outerspace.stsci.edu/download/thumbnails/94962856/myst_landing.png?version=1&modificationDate=1657650111642&api=v2)

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "User Accounts", "Header 2": "Data Authorization"} -->
Permission to access EAP data is also controlled through your MyST Account. Principal Investigators (PI's) of observing programs are automatically granted access to this data. PIs of programs may also authorize other users to access the data during the EAP period by navigating to the MyST Home screen and selecting the **Update Your Account** option. From there click the **Manage Access to Exclusive-Access Science Data** menu option, select your program, and enter the MyST email address of record for your colleague.
* * *
![Login info and button](https://outerspace.stsci.edu/download/thumbnails/94962856/login_Portal.png?version=1&modificationDate=1657650111204&api=v2)

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "User Accounts", "Header 2": "Login"} -->
Be sure to login to the Portal before attempting to retrieve **EAP** data, or before attempting to subscribe to data notifications. Just click the _**_Login..._**_ text.
* * *  
![Logout button](https://outerspace.stsci.edu/download/thumbnails/94962856/button_Logout.png?version=1&modificationDate=1657650111137&api=v2)

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "User Accounts", "Header 2": "Logout"} -->
If for security reasons you must log out of a Portal session (e.g., if you are obliged to share your workstation), go to <https://auth.mast.stsci.edu/sessions>. That page will contain an entry for each active MAST session for which you are logged in. Click the _**Log Out**_ button to terminate the session in question. Then visit the SSO portal to log out of the MyST system: <https://ssoportal.stsci.edu/idp/profile/Logout>.
Another option is to use an Incognito (or Private) browser instance when using the Portal. Logging out would be as simple as closing the Incognito window. The next user can login with another incognito window to start a fresh session.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Auth.MAST"} -->
MAST also offers API token authorization for programmatic access to EAP data. Users with a MyST Account can find instructions on creating and using these tokens on the [auth.MAST documentation page](https://auth.mast.stsci.edu/info). With a valid token in place, authorized users will then be able to retrieve MAST EAP data through __Using Auth.AST Tokens__ in the [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials) chapter. The steps are simply:
1. Navigate to the [Tokens](https://auth.mast.stsci.edu/tokens) page and click the button.
2. Record the long, alpha-numeric string in the environment variable `$MAST_API_TOKEN`, preferably in your `.bashrc` file.  
Be aware that API tokens will expire after 10 days of inactivity or 60 days after creation, whichever comes first. Users experiencing any trouble with existing tokens should first try generating new ones.

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "For Further Reading...", "Header 2": "Related Topics"} -->
* [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications)
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data)
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data)

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "For Further Reading...", "Header 2": "Reference Information"} -->
* [MyST Portal](https://proper.stsci.edu/proper/authentication/auth)
* [Auth.MAST Documentation](https://auth.mast.stsci.edu/info)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

