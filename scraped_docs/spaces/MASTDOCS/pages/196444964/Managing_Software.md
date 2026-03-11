---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software"
date_accessed: "2026-03-11T11:35:47.836210"
---

<!-- CHUNK 1 START -->
On this page...
* 1[Python Environments ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-PythonEnvironments)
* 2[JupyterLab Kernels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-JupyterLabKernels)
* 3[Pre-installed Software and Temporary Additions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-Pre-installedSoftwareandTemporaryAdditions)
* 3.1[From a Notebook cell:](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-FromaNotebookcell:)
* 3.2[From a terminal window:](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-Fromaterminalwindow:)
* 4[Persistent User-Installed Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-PersistentUser-InstalledSoftware)
* 4.1[Other Information](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-OtherInformation)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Python Environments"} -->
The JupyterLab environment is based on Like Python, miniconda can have multiple virtual environments, each containing its own isolated software versions. Our JupyterHub system typically has at least two pre-installed environments, which conceptually are:
* generic analysis
* generic analysis + astronomical packages  
In general, you will want to use the environment customized for astronomy. The generic option is a "basic" installation of Python, which may not be suitable for your analysis.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "JupyterLab Kernels"} -->
In Jupyter, kernels are the background processes that execute cells and return results for display. Conda environments can be used to create a kernel, automatically providing all of the packages needed to run a Notebook. If a Notebook fails to import a package you expected, it may be a sign the wrong kernel is running. To select the kernel on which you want to run your Notebook, go to the _**Kernel** _menu and choose _**Change Kernel.**_ You can also click directly on the name of the active kernel to switch to another.
![](https://outerspace.stsci.edu/download/attachments/196444964/kernel.png?version=1&modificationDate=1688070481799&api=v2)  
**Figure 6** - Switching kernels. The active kernel is boxed in red in the upper right corner.
When the kernel is idle, the circle to the right of the kernel name is unfilled. When the kernel is actively running the Notebook, the circle is filled.
Each kernel maintains the Python state for the currently executing Notebook. This saved state includes imported packages and the values of variables. Consequently, the **_Kernel_** menu has numerous options for clearing the state and restarting or continuing Notebook execution.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Pre-installed Software and Temporary Additions"} -->
The pre-installed software environment is part of the JupyterLab container. While it can be changed – and software can be installed or removed – the changes do not persist between sessions, and users cannot affect one another. The principal advantage of modifying the pre-installed environments is that, generally, it is fast since there is no need to install dependencies already included in the environment.
Installing additional packages into the pre-existing environments is fairly straightforward. The only real trick is that you must activate the desired installation environment before installing packages. Two equivalent techniques for fast but temporary package installs are shown below.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Pre-installed Software and Temporary Additions", "Header 2": "From a Notebook cell:"} -->
To install without leaving your Notebook, enter a command like the following, substituting a real environment name and real package names. The sequence is actually two commands, one which chooses your target environment and a second, nested command which installs packages within the chosen environment. Note the entire command begins with "!" to make it execute as native commands instead of Python commands.
```
[1]: !conda run -n <pre-installed environment name> pip install <pkg1> <pkg2> ...
```  
Pip-installing packages generally produces copious output that we have omitted here.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Pre-installed Software and Temporary Additions", "Header 2": "From a terminal window:"} -->
For those comfortable with using the terminal window, the required commands are a little simpler and clearer. Open a terminal window and type the following, substituting a real environment name and real package names for the placeholders:
```
$ conda activate <pre-installed environment>
$ pip install <pkg1> <pkg2> ...
```  
As when installing from a Notebook cell, the "pip-installation" will produce copious output that we do not reproduce here.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Persistent User-Installed Software"} -->
If the pre-installed environments don't have the software you need, you can create your own persistent environment. available across multiple sessions.
To assist in setting up, using, and deleting persistent user environments, the science platforms provide a set of scripts that manage the details:
Terminal Command |  Examples | Description
---|---|---
**kernel-create** |  **kernel-create** _< environment-name>_ [_< python-version>_] [_< lab-display-name>_] **kernel-create** my-tess 3.12 "My Persistent Env" |  Executed in a terminal window, **kernel-create** creates a conda environment located in persistent storage. **kernel-create** makes a minimal persistent conda environment stored in the _$HOME/envs/conda/ <environment-name>_ subdirectory. It also creates a corresponding JupyterLab kernel so the environment is accessible to Notebooks. Because they are stored under your personal $HOME, these environments are not affected by system changes to /opt/conda. Conda environments made this way consume more space than virtual environments but are largely independent of the pre-installed software and other persistent environments.
**kernel-create-venv** |  **kernel-create-venv** _< virtual-env-name>_ [_< lab-display-name>_] **kernel-create-venv** my-tess-venv "My Persistent Virtual Env" |  Executed in a terminal window, **create-kernel-venv** creates a Python virtual environment within the active Python environment. **kernel-create-venv** creates a persistent Python virtualenv stored in the $HOME/envs/venv/<environment-name> subdirectory. It also creates a JupyterLab kernel so the environment can be used in Notebooks. The virtual environment will be created using the version of Python active in the terminal window; for the most stable results, a persistent conda environment should be active when you create a virtual environment. Virtual environments tend to consume less space than typical conda environments by linking to software that is already installed. For the same reason, they also tend to be quicker to install. There is no requirement to use virtual environments, you can stop with conda (documented above) if desired, but some may find them beneficial.
**kernel-activate** |  **source kernel-activate** <_env-or-venv-name_ > **source kernel-activate** my-tess **source kernel-activate** my-tess-venv |  When sourced into a terminal window, activates the specified user conda or virtual environment. The **kernel-activate** script will activate the specified <environment-name> for use on the command line. The environment may be either a conda or a virtual environment but must be installed as described above. The Notebook analog to **kernel-activate** is choosing **menu item Kernel → Select Kernel...** Not effective for pre-installed conda kernels.
**kernel-deactivate** |  **source kernel-deactivate** <_env-or-venv-name_ > **source kernel-activate** my-tess **source kernel-activate** my-tess-venv |  When sourced into a terminal window, **kernel-deactivate** exits the current environment and activates a previously active environment. Not effective for pre-installed conda kernels.
**kernel-delete** |  **kernel-delete** <_env-or-venv-name_ > **kernel-delete** my-tess **kernel-delete** my-tess-venv |  When executed in a terminal window, **delete-kernel** deletes a persistent user environment, whether conda or virtual. Not effective for pre-installed conda kernels.
The commands in the table above establish largely empty environments into which you can then conda or pip install the remainder of your requirements. The environments are immediately accessible as Notebook kernels for you to select and execute Notebooks in.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Persistent User-Installed Software", "Header 2": "Other Information"} -->
The TIKE project has additional instructions on
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
* 1[Python Environments ](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-PythonEnvironments)
* 2[JupyterLab Kernels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-JupyterLabKernels)
* 3[Pre-installed Software and Temporary Additions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-Pre-installedSoftwareandTemporaryAdditions)
* 3.1[From a Notebook cell:](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-FromaNotebookcell:)
* 3.2[From a terminal window:](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-Fromaterminalwindow:)
* 4[Persistent User-Installed Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-PersistentUser-InstalledSoftware)
* 4.1[Other Information](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/196444964/Managing+Software#ManagingSoftware-OtherInformation)

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Python Environments"} -->
The JupyterLab environment is based on Like Python, miniconda can have multiple virtual environments, each containing its own isolated software versions. Our JupyterHub system typically has at least two pre-installed environments, which conceptually are:
* generic analysis
* generic analysis + astronomical packages  
In general, you will want to use the environment customized for astronomy. The generic option is a "basic" installation of Python, which may not be suitable for your analysis.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "JupyterLab Kernels"} -->
In Jupyter, kernels are the background processes that execute cells and return results for display. Conda environments can be used to create a kernel, automatically providing all of the packages needed to run a Notebook. If a Notebook fails to import a package you expected, it may be a sign the wrong kernel is running. To select the kernel on which you want to run your Notebook, go to the _**Kernel** _menu and choose _**Change Kernel.**_ You can also click directly on the name of the active kernel to switch to another.
![](https://outerspace.stsci.edu/download/attachments/196444964/kernel.png?version=1&modificationDate=1688070481799&api=v2)  
**Figure 6** - Switching kernels. The active kernel is boxed in red in the upper right corner.
When the kernel is idle, the circle to the right of the kernel name is unfilled. When the kernel is actively running the Notebook, the circle is filled.
Each kernel maintains the Python state for the currently executing Notebook. This saved state includes imported packages and the values of variables. Consequently, the **_Kernel_** menu has numerous options for clearing the state and restarting or continuing Notebook execution.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Pre-installed Software and Temporary Additions"} -->
The pre-installed software environment is part of the JupyterLab container. While it can be changed – and software can be installed or removed – the changes do not persist between sessions, and users cannot affect one another. The principal advantage of modifying the pre-installed environments is that, generally, it is fast since there is no need to install dependencies already included in the environment.
Installing additional packages into the pre-existing environments is fairly straightforward. The only real trick is that you must activate the desired installation environment before installing packages. Two equivalent techniques for fast but temporary package installs are shown below.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Pre-installed Software and Temporary Additions", "Header 2": "From a Notebook cell:"} -->
To install without leaving your Notebook, enter a command like the following, substituting a real environment name and real package names. The sequence is actually two commands, one which chooses your target environment and a second, nested command which installs packages within the chosen environment. Note the entire command begins with "!" to make it execute as native commands instead of Python commands.
```
[1]: !conda run -n <pre-installed environment name> pip install <pkg1> <pkg2> ...
```  
Pip-installing packages generally produces copious output that we have omitted here.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Pre-installed Software and Temporary Additions", "Header 2": "From a terminal window:"} -->
For those comfortable with using the terminal window, the required commands are a little simpler and clearer. Open a terminal window and type the following, substituting a real environment name and real package names for the placeholders:
```
$ conda activate <pre-installed environment>
$ pip install <pkg1> <pkg2> ...
```  
As when installing from a Notebook cell, the "pip-installation" will produce copious output that we do not reproduce here.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Persistent User-Installed Software"} -->
If the pre-installed environments don't have the software you need, you can create your own persistent environment. available across multiple sessions.
To assist in setting up, using, and deleting persistent user environments, the science platforms provide a set of scripts that manage the details:
Terminal Command |  Examples | Description
---|---|---
**kernel-create** |  **kernel-create** _< environment-name>_ [_< python-version>_] [_< lab-display-name>_] **kernel-create** my-tess 3.12 "My Persistent Env" |  Executed in a terminal window, **kernel-create** creates a conda environment located in persistent storage. **kernel-create** makes a minimal persistent conda environment stored in the _$HOME/envs/conda/ <environment-name>_ subdirectory. It also creates a corresponding JupyterLab kernel so the environment is accessible to Notebooks. Because they are stored under your personal $HOME, these environments are not affected by system changes to /opt/conda. Conda environments made this way consume more space than virtual environments but are largely independent of the pre-installed software and other persistent environments.
**kernel-create-venv** |  **kernel-create-venv** _< virtual-env-name>_ [_< lab-display-name>_] **kernel-create-venv** my-tess-venv "My Persistent Virtual Env" |  Executed in a terminal window, **create-kernel-venv** creates a Python virtual environment within the active Python environment. **kernel-create-venv** creates a persistent Python virtualenv stored in the $HOME/envs/venv/<environment-name> subdirectory. It also creates a JupyterLab kernel so the environment can be used in Notebooks. The virtual environment will be created using the version of Python active in the terminal window; for the most stable results, a persistent conda environment should be active when you create a virtual environment. Virtual environments tend to consume less space than typical conda environments by linking to software that is already installed. For the same reason, they also tend to be quicker to install. There is no requirement to use virtual environments, you can stop with conda (documented above) if desired, but some may find them beneficial.
**kernel-activate** |  **source kernel-activate** <_env-or-venv-name_ > **source kernel-activate** my-tess **source kernel-activate** my-tess-venv |  When sourced into a terminal window, activates the specified user conda or virtual environment. The **kernel-activate** script will activate the specified <environment-name> for use on the command line. The environment may be either a conda or a virtual environment but must be installed as described above. The Notebook analog to **kernel-activate** is choosing **menu item Kernel → Select Kernel...** Not effective for pre-installed conda kernels.
**kernel-deactivate** |  **source kernel-deactivate** <_env-or-venv-name_ > **source kernel-activate** my-tess **source kernel-activate** my-tess-venv |  When sourced into a terminal window, **kernel-deactivate** exits the current environment and activates a previously active environment. Not effective for pre-installed conda kernels.
**kernel-delete** |  **kernel-delete** <_env-or-venv-name_ > **kernel-delete** my-tess **kernel-delete** my-tess-venv |  When executed in a terminal window, **delete-kernel** deletes a persistent user environment, whether conda or virtual. Not effective for pre-installed conda kernels.
The commands in the table above establish largely empty environments into which you can then conda or pip install the remainder of your requirements. The environments are immediately accessible as Notebook kernels for you to select and execute Notebooks in.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Persistent User-Installed Software", "Header 2": "Other Information"} -->
The TIKE project has additional instructions on
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 15 END -->

