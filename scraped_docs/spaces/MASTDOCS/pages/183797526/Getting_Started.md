---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started"
date_accessed: "2026-03-11T11:35:45.026908"
---

<!-- CHUNK 1 START -->
On this page...
* 1[Prerequisites](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Prerequisites)
* 2[Getting Started](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-GettingStarted)
* 2.1[Home Directory](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-HomeDirectory)
* 2.2[Opening & Creating Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Opening&CreatingFiles)
* 2.3[Uploading, Downloading, and Caching Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Uploading,Downloading,andCachingFiles)
* 2.4[Announcements](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Announcements)
* 2.5[Internet access](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Internetaccess)
* 3[Getting Help With...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-GettingHelpWith...)
* 3.1[Jupyter](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Jupyter)
* 4[Additional Resources](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-AdditionalResources)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Prerequisites"} -->
To work on any of the platforms, you'll first need to make a MyST account. If you don't already have an account, please visit the [MyST Account Home](https://proper.stsci.edu/proper/authentication/auth) to create one.
You'll interact with the platform via JupyterLab. For an overview of all the features available, see the written

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Home Directory"} -->
When you log into a Notebook session, the active directory is your $HOME directory, which will look similar to **Fig 1** below. These pre-populated files include documentation to help you use the system and Notebook tutorials demonstrating various science use cases. This directory is unique to you: edits and uploads are not visible to other users.
![](https://outerspace.stsci.edu/download/attachments/183797526/nav_panel.png?version=1&modificationDate=1674599346832&api=v2)  
**Figure 1** - The Navigation Panel shows a default file list in the home directory.
Files in this directory are saved on AWS storage and will persist between sessions. In addition, STScI creates backups every two weeks. However, it is always prudent to back up any critical files. Storage limit varies depending on the platform but is typically on the order of 25-50 GB; upload large files sparingly.
Storage Limits
If you exceed **90%** of quota usage, a warning announcement will be sent, and you will be prompted to conserve storage and delete files.
If you exceed **100%** quota usage, you will be **logged off the hub and locked out** until administrators can assist you with reducing your storage consumption.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Opening & Creating Files"} -->
To open a folder, Notebook, or other files, double-click the desired item in the Navigation Panel. Clicking the blue plus sign at the top left of the window will open the launcher window seen below in **Fig 2.**
![](https://outerspace.stsci.edu/download/attachments/183797526/launcher_window.png?version=1&modificationDate=1674746646396&api=v2)**Figure 2** - The Launcher Window, a method of opening new Notebooks, Python files, Markdown files, and terminal windows.
Clicking on a Notebook icon will open an empty JupyterLab Notebook window running in its corresponding kernel. The same is true of clicking on a Read more about kernels and available software in the [Managing Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Managing-Software) section below.
The

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files"} -->
If you're transferring many files, consider creating a zip or tar archive first.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files", "Header 3": "**Uploading**"} -->
Data can be uploaded into the Notebook environment using the **_up-arrow_** located at the top of the navigation panel, to the right of the blue + button:
File size
Be mindful of the storage limit when uploading files!
![](https://outerspace.stsci.edu/download/thumbnails/183797526/uploading.png?version=1&modificationDate=1675191110527&api=v2)
**Figure 3** - The file upload button is located in the window's upper left.
**Downloading**
You can download data from your Notebook environment by navigating to a file, right-clicking on it, then selecting _Download:_
![](https://outerspace.stsci.edu/download/attachments/183797526/Screen%20Shot%202022-11-18%20at%20Nov%2018%2C%202022%20%201.47.35%20PM.png?version=1&modificationDate=1671126458081&api=v2)
**Figure 4** - Download a file by right-clicking on it and navigating the drop-down menu.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files", "Header 3": "**Automatic Data Cache Clearing**"} -->
Many tools and packages implicitly cache data files that are fetched from the internet during program execution. Like any files stored in your $HOME directory, these cached files consume storage space and incur monthly costs to retain. Consequently, upon logout, selected data caches are purged, deleting downloaded files to avoid storage fees. At this time, the packages involved include:
1. Astropy (and many/all client packages of astropy downloads and caching)
2. Lightkurve  
Although the system will automatically clear your data caches when your session ends, the utility scripts used are also accessible to you via a terminal window or Notebook "!" escape. These may prove useful for rapidly reducing storage consumption should you approach or exceed quota limits:
Terminal Command | Example | Description
---|---|---
cache-size | ```
$ cache-size
3G
```
| prints out a human-readable total of your data caches in bytes.
cache-clear | ```
$ cache-clear
$ cache-size
<small residual>
```
| deletes all data files in your data caches but leaves behind directory structures.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files", "Header 3": "**Automatically Synced Notebooks**"} -->
Every Science Platform automatically clones a selection of tutorial Notebooks from GitHub and places them in your $HOME directory. These Notebooks are updated regularly, which poses an issue: the Platforms shouldn't overwrite your progress on a tutorial, but it's essential that the code in the tutorials be kept up to date as software is modified. To resolve this conflict, the tutorials are read-only. You will always have access to the latest version of tutorials, at the expense of not being able to edit them. Instead, to make changes or run a Notebook, you must:
1. Open a read-only Notebook from its original location.
2. Use File → Save as... to save a writable copy in a different location.
3. Make changes to the original example Notebooks manually as desired.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Announcements"} -->
The bottom right corner of the Notebook display has an **Announcements** button. A new message is indicated by the status![](https://outerspace.stsci.edu/download/attachments/183797526/announce.png?version=1&modificationDate=1675201232749&api=v2). High-priority messages, such as warnings, errors, and critical announcements, will automatically open in your display.
![](https://outerspace.stsci.edu/download/attachments/183797526/Screen%20Shot%202022-11-18%20at%20Nov%2018%2C%202022%20%201.36.19%20PM.png?version=1&modificationDate=1671126386085&api=v2)
**Figure 5** - An announcement about current storage usage. This user is within their quota and has an "OK" status.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Internet access"} -->
Notebooks sessions have full access to the internet. You can download data and software packages into the Notebook environment using Notebook code and standard network tools like _wget, curl, pip, and npm._ See more in the 'Managing Software' section below. Installations will likely be fast, as the session runs in a data center with a > 1Gbps connection.
Download Restrictions
Downloading data from a Platform session to a local machine is discouraged. Egress from cloud storage incurs additional costs; we limit downloads so that we can continue to provide this service for free to all users.
You can only access your session through a browser window. Despite full internet connectivity, it is not possible to remotely access (e.g., ssh into) your session.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Getting Help With...", "Header 2": "Jupyter"} -->
Within the menu bar at the top of JupyterHub, the 'Help' option contains excellent reference documentation. From there, you can access full JupyterLab overview FAQs, Markdown tips, and the forum. This is not limited to text-based help: video tutorials are also available.
Science Platforms
To send feedback, report bugs or problems, or request additional pre-installed software, contact the .  
* * *

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Additional Resources"} -->
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
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [Cloud Science Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797523/Cloud+Science+Platforms "Cloud Science Platforms")
* [Getting Started with Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started "Getting Started with Platforms")
* [Managing Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software "Managing Software")
* [Active Platforms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797542/Active+Platforms "Active Platforms")
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
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
On this page...
* 1[Prerequisites](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Prerequisites)
* 2[Getting Started](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-GettingStarted)
* 2.1[Home Directory](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-HomeDirectory)
* 2.2[Opening & Creating Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Opening&CreatingFiles)
* 2.3[Uploading, Downloading, and Caching Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Uploading,Downloading,andCachingFiles)
* 2.4[Announcements](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Announcements)
* 2.5[Internet access](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Internetaccess)
* 3[Getting Help With...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-GettingHelpWith...)
* 3.1[Jupyter](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Jupyter)
* 4[Additional Resources](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-AdditionalResources)

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Prerequisites"} -->
To work on any of the platforms, you'll first need to make a MyST account. If you don't already have an account, please visit the [MyST Account Home](https://proper.stsci.edu/proper/authentication/auth) to create one.
You'll interact with the platform via JupyterLab. For an overview of all the features available, see the written

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Home Directory"} -->
When you log into a Notebook session, the active directory is your $HOME directory, which will look similar to **Fig 1** below. These pre-populated files include documentation to help you use the system and Notebook tutorials demonstrating various science use cases. This directory is unique to you: edits and uploads are not visible to other users.
![](https://outerspace.stsci.edu/download/attachments/183797526/nav_panel.png?version=1&modificationDate=1674599346832&api=v2)  
**Figure 1** - The Navigation Panel shows a default file list in the home directory.
Files in this directory are saved on AWS storage and will persist between sessions. In addition, STScI creates backups every two weeks. However, it is always prudent to back up any critical files. Storage limit varies depending on the platform but is typically on the order of 25-50 GB; upload large files sparingly.
Storage Limits
If you exceed **90%** of quota usage, a warning announcement will be sent, and you will be prompted to conserve storage and delete files.
If you exceed **100%** quota usage, you will be **logged off the hub and locked out** until administrators can assist you with reducing your storage consumption.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Opening & Creating Files"} -->
To open a folder, Notebook, or other files, double-click the desired item in the Navigation Panel. Clicking the blue plus sign at the top left of the window will open the launcher window seen below in **Fig 2.**
![](https://outerspace.stsci.edu/download/attachments/183797526/launcher_window.png?version=1&modificationDate=1674746646396&api=v2)**Figure 2** - The Launcher Window, a method of opening new Notebooks, Python files, Markdown files, and terminal windows.
Clicking on a Notebook icon will open an empty JupyterLab Notebook window running in its corresponding kernel. The same is true of clicking on a Read more about kernels and available software in the [Managing Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797526/Getting+Started#GettingStarted-Managing-Software) section below.
The

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files"} -->
If you're transferring many files, consider creating a zip or tar archive first.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files", "Header 3": "**Uploading**"} -->
Data can be uploaded into the Notebook environment using the **_up-arrow_** located at the top of the navigation panel, to the right of the blue + button:
File size
Be mindful of the storage limit when uploading files!
![](https://outerspace.stsci.edu/download/thumbnails/183797526/uploading.png?version=1&modificationDate=1675191110527&api=v2)
**Figure 3** - The file upload button is located in the window's upper left.
**Downloading**
You can download data from your Notebook environment by navigating to a file, right-clicking on it, then selecting _Download:_
![](https://outerspace.stsci.edu/download/attachments/183797526/Screen%20Shot%202022-11-18%20at%20Nov%2018%2C%202022%20%201.47.35%20PM.png?version=1&modificationDate=1671126458081&api=v2)
**Figure 4** - Download a file by right-clicking on it and navigating the drop-down menu.

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files", "Header 3": "**Automatic Data Cache Clearing**"} -->
Many tools and packages implicitly cache data files that are fetched from the internet during program execution. Like any files stored in your $HOME directory, these cached files consume storage space and incur monthly costs to retain. Consequently, upon logout, selected data caches are purged, deleting downloaded files to avoid storage fees. At this time, the packages involved include:
1. Astropy (and many/all client packages of astropy downloads and caching)
2. Lightkurve  
Although the system will automatically clear your data caches when your session ends, the utility scripts used are also accessible to you via a terminal window or Notebook "!" escape. These may prove useful for rapidly reducing storage consumption should you approach or exceed quota limits:
Terminal Command | Example | Description
---|---|---
cache-size | ```
$ cache-size
3G
```
| prints out a human-readable total of your data caches in bytes.
cache-clear | ```
$ cache-clear
$ cache-size
<small residual>
```
| deletes all data files in your data caches but leaves behind directory structures.

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Uploading, Downloading, and Caching Files", "Header 3": "**Automatically Synced Notebooks**"} -->
Every Science Platform automatically clones a selection of tutorial Notebooks from GitHub and places them in your $HOME directory. These Notebooks are updated regularly, which poses an issue: the Platforms shouldn't overwrite your progress on a tutorial, but it's essential that the code in the tutorials be kept up to date as software is modified. To resolve this conflict, the tutorials are read-only. You will always have access to the latest version of tutorials, at the expense of not being able to edit them. Instead, to make changes or run a Notebook, you must:
1. Open a read-only Notebook from its original location.
2. Use File → Save as... to save a writable copy in a different location.
3. Make changes to the original example Notebooks manually as desired.

<!-- CHUNK 19 END -->

<!-- CHUNK 20 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Announcements"} -->
The bottom right corner of the Notebook display has an **Announcements** button. A new message is indicated by the status![](https://outerspace.stsci.edu/download/attachments/183797526/announce.png?version=1&modificationDate=1675201232749&api=v2). High-priority messages, such as warnings, errors, and critical announcements, will automatically open in your display.
![](https://outerspace.stsci.edu/download/attachments/183797526/Screen%20Shot%202022-11-18%20at%20Nov%2018%2C%202022%20%201.36.19%20PM.png?version=1&modificationDate=1671126386085&api=v2)
**Figure 5** - An announcement about current storage usage. This user is within their quota and has an "OK" status.

<!-- CHUNK 20 END -->

<!-- CHUNK 21 START -->
<!-- Metadata: {"Header 1": "Getting Started", "Header 2": "Internet access"} -->
Notebooks sessions have full access to the internet. You can download data and software packages into the Notebook environment using Notebook code and standard network tools like _wget, curl, pip, and npm._ See more in the 'Managing Software' section below. Installations will likely be fast, as the session runs in a data center with a > 1Gbps connection.
Download Restrictions
Downloading data from a Platform session to a local machine is discouraged. Egress from cloud storage incurs additional costs; we limit downloads so that we can continue to provide this service for free to all users.
You can only access your session through a browser window. Despite full internet connectivity, it is not possible to remotely access (e.g., ssh into) your session.

<!-- CHUNK 21 END -->

<!-- CHUNK 22 START -->
<!-- Metadata: {"Header 1": "Getting Help With...", "Header 2": "Jupyter"} -->
Within the menu bar at the top of JupyterHub, the 'Help' option contains excellent reference documentation. From there, you can access full JupyterLab overview FAQs, Markdown tips, and the forum. This is not limited to text-based help: video tutorials are also available.
Science Platforms
To send feedback, report bugs or problems, or request additional pre-installed software, contact the .  
* * *

<!-- CHUNK 22 END -->

<!-- CHUNK 23 START -->
<!-- Metadata: {"Header 1": "Additional Resources"} -->
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 23 END -->

