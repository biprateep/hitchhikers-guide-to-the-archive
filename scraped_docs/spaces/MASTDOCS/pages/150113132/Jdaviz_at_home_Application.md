---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application"
date_accessed: "2026-03-11T16:26:54.999673"
content_length: 6366
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Prerequisites](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-Prerequisites)
* 1.1[Installing the Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-InstallingtheSoftware)
* 2[Running the Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-RunningtheApplication)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Prerequisites"} -->
Prior to running Jdaviz as a standalone application, you should:
1. Make sure Jdaviz is installed on your system
2. Download the data file you want to analyze

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Prerequisites", "Header 2": "Installing the Software"} -->
Installation is fairly straightforward using pip. Open a terminal and type:
```
pip install jdaviz --upgrade
```  
That's all! Once the code has finished executing, you should have a fresh installation on your machine. You may want to familiarize yourself with available commands by entering:
```
jdaviz --help
```

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Running the Application"} -->
To start the application, open a terminal window and enter a command of the following type:
```
jdaviz --layout=[module] [filename]
```  
For example, if we wanted to open **`jw01288-o013_t013_nirspec_g395h-f290lp_s3d.fits`** using the the Cubeviz module we would enter:
```
jdaviz --layout=cubeviz jw01288-o013_t013_nirspec_g395h-f290lp_s3d.fits
```  
This will open a window in your default browser that looks like the image in **Figure 1**.
![](https://outerspace.stsci.edu/download/attachments/150113132/jdaviz_cubeviz_new.png?version=1&modificationDate=1742321465214&api=v2)
**Figure 1 —** An example set of JWST data. Depending on your data selection, you may not see the same analysis elements.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
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
* [Jdaviz in the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113048/Jdaviz+in+the+MAST+Portal "Jdaviz in the MAST Portal")
* [Jdaviz at home: Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application "Jdaviz at home: Application")
* [Jdaviz at home: Jupyter Notebooks](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113134/Jdaviz+at+home+Jupyter+Notebooks "Jdaviz at home: Jupyter Notebooks")
* [Guided examples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113138/Guided+examples "Guided examples")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
**On this page...**
* 1[Prerequisites](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-Prerequisites)
* 1.1[Installing the Software](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-InstallingtheSoftware)
* 2[Running the Application](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-RunningtheApplication)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113132/Jdaviz+at+home+Application#Jdavizathome:Application-ForFurtherReading...)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Prerequisites"} -->
Prior to running Jdaviz as a standalone application, you should:
1. Make sure Jdaviz is installed on your system
2. Download the data file you want to analyze

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Prerequisites", "Header 2": "Installing the Software"} -->
Installation is fairly straightforward using pip. Open a terminal and type:
```
pip install jdaviz --upgrade
```  
That's all! Once the code has finished executing, you should have a fresh installation on your machine. You may want to familiarize yourself with available commands by entering:
```
jdaviz --help
```

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Running the Application"} -->
To start the application, open a terminal window and enter a command of the following type:
```
jdaviz --layout=[module] [filename]
```  
For example, if we wanted to open **`jw01288-o013_t013_nirspec_g395h-f290lp_s3d.fits`** using the the Cubeviz module we would enter:
```
jdaviz --layout=cubeviz jw01288-o013_t013_nirspec_g395h-f290lp_s3d.fits
```  
This will open a window in your default browser that looks like the image in **Figure 1**.
![](https://outerspace.stsci.edu/download/attachments/150113132/jdaviz_cubeviz_new.png?version=1&modificationDate=1742321465214&api=v2)
**Figure 1 —** An example set of JWST data. Depending on your data selection, you may not see the same analysis elements.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 9 END -->

