---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods"
date_accessed: "2026-03-11T11:32:41.919124"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Direct from Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-DirectfromSearchResults)
* 2[Using the Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-UsingtheDownloadManager)
* 2.1[Options](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-Options)
* 2.1.1[Browser Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-BrowserDownload)
* 2.1.2[Curl Script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-CurlScript)
* 2.1.3[Batch Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-BatchRetrieval)
* 3[Other Download Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-OtherDownloadMethods)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Direct from Search Results"} -->
Retrieving data from MAST in the Portal context requires first executing a successful search (see the chapter on [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching)). Each of the rows in the search results includes a File icon ![](https://outerspace.stsci.edu/download/thumbnails/94963040/icon_file_white.png?version=1&modificationDate=1657650228321&api=v2)which enables a direct download of a single file or observation (see [One-Click Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963013/One-Click+Download) for details).

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Using the Download Manager"} -->
In the Portal _**Download Manager**_ you must check one of more directories or file boxes in the _**File**_ panel before download methods become available to you (see [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket)).
Portal Log-on
You must be logged in to the Portal to download data that is marked as _Exclusive Access_. Such observations appear with a yellow background in the Search Results table.
Browser Pop-ups
The Portal requires that pop-up blockers be disabled for the domain: <https://mast.stsci.edu/> in order to download data. Check the documentation for your browser to determine how this is done, and be alert for notifications from the browser that popups are being blocked.In many cases it simply requires giving approval for pop-ups when you are asked.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Using the Download Manager", "Header 2": "Options"} -->
Click one of the buttons described below to choose the details of your download.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Using the Download Manager", "Header 2": "Options", "Header 3": "Browser Download"} -->
Follow the steps below to initiate a download of the selected files. The files will be bundled into a .zip or a .tar (optionally compressed) file.  
| Instruction | Notes
---|---|---
**1** | Click the **Download** button. | ![Download products button](https://outerspace.stsci.edu/download/thumbnails/94963040/button_dlm_download.png?version=1&modificationDate=1657650228432&api=v2)
**2** | Select your preferred form for the download bundle and click _**Download**_. | ![Download bundle format dialog](https://outerspace.stsci.edu/download/thumbnails/94963040/menu_download.png?version=1&modificationDate=1657650228349&api=v2)
**3** | Save the file bundle to your local storage. The appearance of the file-save dialog depends upon your browser settings. | ![Download to local disk dialog \(browser specific\)](https://outerspace.stsci.edu/download/thumbnails/94963040/dialog_fileSave_opt.png?version=1&modificationDate=1657650228335&api=v2)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Using the Download Manager", "Header 2": "Options", "Header 3": "Curl Script"} -->
You may elect to download a custom Bash script, which when run on your host system will retrieve your selected data files using cURL commands.  
| Instruction | Notes
---|---|---
**1** | Click the **Download** button. | ![Download products button](https://outerspace.stsci.edu/download/thumbnails/94963040/button_dlm_download.png?version=1&modificationDate=1657650228432&api=v2)
**2** | Select __Curl__ from the file **Format** pull-down menu. | ![Download bundle format dialog](https://outerspace.stsci.edu/download/thumbnails/94963040/dialog_download_curl.png?version=1&modificationDate=1657650228418&api=v2)
**3** | Save the Curl shell script in a directory where you wish the data files to be stored. | ![Download to local disk dialog \(browser specific\)](https://outerspace.stsci.edu/download/attachments/94963040/dialog_fileSave_curl.png?version=1&modificationDate=1657650228404&api=v2)
**4** |  Bring up a shell and execute the script. **Note:** If you are retrieving Exclusive Access Protected data, you will need to either provide your MyST login credentials, or have established a [Auth.MAST token](https://auth.mast.stsci.edu/info), in order for the shell to complete the retrieval successfully. |  ```
bash MAST_2018-10-31T2028.sh
```

Choosing Shippable Media
Requesting data via shippable media will involve considerable (i.e., days) delay. Note that you will need to certify that you are unable to use another means of data retrieval.
MAST Auth Tokens
Authentication for access to Exclusive Access data via a cURL or other scripts is managed in MAST via tokens. See [MAST API Tokens](https://auth.mast.stsci.edu/info) to learn how to create or update a MAST.auth token.
### Batch Retrieval
The Batch Retrieval option allows the selected files to be written to external media for subsequent retrieval. Follow the steps below to stage data on the archive.stsci.edu ftp server. Note that requesting data via shippable media will incur a substantial delay, and requires that you certify that you cannot retrieve data via staging.
Staging files for ftp retrieval is currently supported for a few MAST missions (including JWST and HST), but not all. It is highly recommended to instead retrieve large numbers of files via cURL.

| Instruction | Notes
---|---|---
**1** | Click the **Batch Retrieval** button. | ![Batch retrieval button](https://outerspace.stsci.edu/download/thumbnails/94963040/button_batch-retrieval.png?version=1&modificationDate=1657650228501&api=v2)
**2** |  Select __Staging__ from the **Delivery Method** pull-down menu and (if you are not logged in) provide the email address where you wish the notification to be sent. **Note:** If you are logged in to MAST, the e-mail address on record will be pre-filled. | ![Batch retrieval popup](https://outerspace.stsci.edu/download/thumbnails/94963040/mast_batch_retrieval.png?version=1&modificationDate=1657650228308&api=v2)
**3** | Acknowledge the pop-up notification, and check your messages at the delivery email address you specified. | ![Operation completed popup](https://outerspace.stsci.edu/download/thumbnails/94963040/mast_batch_success.png?version=1&modificationDate=1657650228292&api=v2)
**4** | The email notification will give the location of the files that have been staged. | ![Delivery status request email message](https://outerspace.stsci.edu/download/attachments/94963040/mast_batch_email.png?version=1&modificationDate=1657650228260&api=v2)
**5** |  Access the staging disk using an encrypted FTPS connection. See below for suggestions for modern, third-party clients. The MAST FTP server (**`archive.stsci.edu[](http://archive.stsci.edu)`**`)`no longer supports unencrypted FTP connections. Command-line ftp clients, as in Linux or MacOS, may not work with our server. Please see<https://archive.stsci.edu/ftp.html> |

#### Retrieval via third-party clients
Please see the
Cyberduck (Click here to expand...)
To download the app or for more help, please see the site.
Launch the app and select Open Connection. ![](https://outerspace.stsci.edu/download/thumbnails/94963040/cyberduck_open_connection.png?version=1&modificationDate=1657650228233&api=v2)
* Under the FTP dropdown select FTP-SSL (Explicit AUTH TLS)
* Server: [archive.stsci.edu](http://archive.stsci.edu)
* Select Anonymous Login OR enter your MyST login credentials
* Select Connect

![Cyberduck FTP Panel](https://outerspace.stsci.edu/download/attachments/94963040/cyberduck_anonymous_login.png?version=1&modificationDate=1657650228246&api=v2)
You will see two folders: "pub" and "stage":
* __pub__ contains public data available on MAST
* __stage__ contains data that have staged by MAST users. It is purged periodically.


Under "stage", navigate to the directory specified in the email notification and you should see the folder(s) containing your download.
* To download the entire directory highlight the folder, then under Action on the menu bar select Download.
* If you only want a few files from the directory, expand the desired directory, and then select the files you want to download.


FileZilla (Click here to expand...)
To download the app or for more help, please see the site.
Launch the app.
In the Host field enter <ftps://archive.stsci.edu>, then your MyST email address and password in the Username and Password fields, respectively. Select Quickconnect.
* If TLS connection is not set as the default, Quickconnect may be unsuccessful. If so, navigate to the Site Manager. ![](https://outerspace.stsci.edu/download/thumbnails/94963040/filezilla_sitemanager.png?version=1&modificationDate=1657650228217&api=v2)
* Select New Site
* Protocol: FTP - File Transfer Protocol
* Host: <ftps://archive.stsci.edu>
* Encryption: Require explicit FTP over TLS
* Logon Type: Select Anonymous OR enter your MyST credentials
* Select Connect


![Filezilla FTP Panel](https://outerspace.stsci.edu/download/attachments/94963040/filezilla_sitemanager_window.png?version=1&modificationDate=1657650228198&api=v2)
Under Remote site, you will see two folders: "pub" and "stage"
* Pub is all of the public data available on MAST
* Stage is the data that has been added to the staging area


Under "stage", navigate to the directory specified in the email notification and you should see the folder(s) containing your download.
Once you locate the folder(s) or file(s) you want to download, right click and select Download.
wget (Click here to expand...)
To install wget or for more help, please see the site.
Bring up a shell.
If you requested a retrieval anonymously, run the following command in the shell:
```
wget -r --ftp-user='anonymous' --ask-password ftps://archive.stsci.edu/stage/anonymous/<anonymous requestID>/
```

If you were logged into MAST when you requested that your data be staged, run:
```
wget -r --ftp-user='<your full MyST email>' --ask-password ftps://archive.stsci.edu/stage/<userID>/<requestID>/
```

Note, for users internal to STScI there may still be a certificate problem; if you encounter an error add '`--no-check-certificate`' to the command.
curl (Click here to expand...)
To install curl or for more help, please see the  is likely already installed on many machines, and if not, is freely available as open source software.


Bring up a shell.
If you requested a retrieval anonymously, run:
```
curl --ssl-reqd -O ftp://archive.stsci.edu/stage/anonymous/<anonymous requestID>/<filename>
```

If you were logged into MAST when you requested that your data be staged, run:
```
curl --ssl-reqd -O ftp://archive.stsci.edu/stage/<userID>/<requestID>/<filename> -u '<your full MyST email>'
```

Note that you must include the filename in these commands. If you do not know the name of the file you'd like to retrieve, or want to download an entire directory, we recommend wget or one of the other methods detailed here.
ftp (Click here to expand...)
The MAST FTP server (**`archive.stsci.edu[](http://archive.stsci.edu)`**`)`no longer supports unencrypted FTP connections. Command-line ftp clients may not work with our server.
Bring up a shell (see note below) and initiate an ftp session on **`archive.stsci.edu[](http://archive.stsci.edu)`**.
```
% ftp archive.stsci.edu
Connected to archive.stsci.edu
```

The appropriate login credentials will be one of the following:
* If you were logged into MAST when you requested that your data be staged, use your MyST login credentials.
* If you requested a retrieval anonymously (for non-exclusive access data), use:
* Name: anonymous
* Password: <your full MyST email address>


```
Name: anonymous
331 Guest login ok, type your email address as
the password
Password:
```

Navigate to the directory specified in the email notification and initiate the transfer of data files.
```
ftp> cd /stage/anonymous/<anonymous requestID>

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "turn off interactive prompt:"} -->
ftp> prompt
ftp> mget *
```

MAC OS X 10.14+ Users
Apple has removed the native ftp application for Mac OS 10.14 (Mojave) and higher. A solution is to install a third-party file-transfer application, such as
# Other Download Methods
It is possible to search for and retrieve data using MAST web services, or the Python [Beyond the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962884/Beyond+the+Portal).
# For Further Reading...
* [The Download Bundle](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963052/The+Download+Bundle)


Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)


* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [Introduction to the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962826/Introduction+to+the+Portal "Introduction to the Portal")
* [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching "Searching")
* [Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962886/Basic+Search "Basic Search")
* [Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962889/Advanced+Search "Advanced Search")
* [Catalog Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962901/Catalog+Search "Catalog Search")
* [Search a List of Targets](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962910/Search+a+List+of+Targets "Search a List of Targets")
* [Special Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962917/Special+Searches "Special Searches")
* [Browsing Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962939/Browsing+Data "Browsing Data")
* [Search Results Grid](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962944/Search+Results+Grid "Search Results Grid")
* [Refining Results with Filters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962974/Refining+Results+with+Filters "Refining Results with Filters")
* [Data Browsing Tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962980/Data+Browsing+Tools "Data Browsing Tools")
* [AstroView](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962998/AstroView "AstroView")
* [Retrieving Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963010/Retrieving+Data "Retrieving Data")
* [One-Click Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963013/One-Click+Download "One-Click Download")
* [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket "Download Basket")
* [Minimum Recommended Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products "Minimum Recommended Products")
* [Calibration Reference Files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963034/Calibration+Reference+Files "Calibration Reference Files")
* [Retrieval Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods "Retrieval Methods")
* [The Download Bundle](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963052/The+Download+Bundle "The Download Bundle")
* [Tips and Notes](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963055/Tips+and+Notes "Tips and Notes")
* [Demos and Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963057/Demos+and+Tutorials "Demos and Tutorials")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
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




**On this page...**
* 1[Direct from Search Results](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-DirectfromSearchResults)
* 2[Using the Download Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-UsingtheDownloadManager)
* 2.1[Options](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-Options)
* 2.1.1[Browser Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-BrowserDownload)
* 2.1.2[Curl Script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-CurlScript)
* 2.1.3[Batch Retrieval](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-BatchRetrieval)
* 3[Other Download Methods](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-OtherDownloadMethods)
* 4[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963040/Retrieval+Methods#RetrievalMethods-ForFurtherReading...)


# Direct from Search Results
Retrieving data from MAST in the Portal context requires first executing a successful search (see the chapter on [Searching](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962885/Searching)). Each of the rows in the search results includes a File icon ![](https://outerspace.stsci.edu/download/thumbnails/94963040/icon_file_white.png?version=1&modificationDate=1657650228321&api=v2)which enables a direct download of a single file or observation (see [One-Click Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963013/One-Click+Download) for details).
# Using the Download Manager
In the Portal _**Download Manager**_ you must check one of more directories or file boxes in the _**File**_ panel before download methods become available to you (see [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963019/Download+Basket)).
Portal Log-on
You must be logged in to the Portal to download data that is marked as _Exclusive Access_. Such observations appear with a yellow background in the Search Results table.
Browser Pop-ups
The Portal requires that pop-up blockers be disabled for the domain: <https://mast.stsci.edu/> in order to download data. Check the documentation for your browser to determine how this is done, and be alert for notifications from the browser that popups are being blocked.In many cases it simply requires giving approval for pop-ups when you are asked.
## Options
Click one of the buttons described below to choose the details of your download.
### Browser Download
Follow the steps below to initiate a download of the selected files. The files will be bundled into a .zip or a .tar (optionally compressed) file.

| Instruction | Notes
---|---|---
**1** | Click the **Download** button. | ![Download products button](https://outerspace.stsci.edu/download/thumbnails/94963040/button_dlm_download.png?version=1&modificationDate=1657650228432&api=v2)
**2** | Select your preferred form for the download bundle and click _**Download**_. | ![Download bundle format dialog](https://outerspace.stsci.edu/download/thumbnails/94963040/menu_download.png?version=1&modificationDate=1657650228349&api=v2)
**3** | Save the file bundle to your local storage. The appearance of the file-save dialog depends upon your browser settings. | ![Download to local disk dialog \(browser specific\)](https://outerspace.stsci.edu/download/thumbnails/94963040/dialog_fileSave_opt.png?version=1&modificationDate=1657650228335&api=v2)
### Curl Script
You may elect to download a custom Bash script, which when run on your host system will retrieve your selected data files using cURL commands.

| Instruction | Notes
---|---|---
**1** | Click the **Download** button. | ![Download products button](https://outerspace.stsci.edu/download/thumbnails/94963040/button_dlm_download.png?version=1&modificationDate=1657650228432&api=v2)
**2** | Select __Curl__ from the file **Format** pull-down menu. | ![Download bundle format dialog](https://outerspace.stsci.edu/download/thumbnails/94963040/dialog_download_curl.png?version=1&modificationDate=1657650228418&api=v2)
**3** | Save the Curl shell script in a directory where you wish the data files to be stored. | ![Download to local disk dialog \(browser specific\)](https://outerspace.stsci.edu/download/attachments/94963040/dialog_fileSave_curl.png?version=1&modificationDate=1657650228404&api=v2)
**4** |  Bring up a shell and execute the script. **Note:** If you are retrieving Exclusive Access Protected data, you will need to either provide your MyST login credentials, or have established a [Auth.MAST token](https://auth.mast.stsci.edu/info), in order for the shell to complete the retrieval successfully. |  ```
bash MAST_2018-10-31T2028.sh
```  
Choosing Shippable Media
Requesting data via shippable media will involve considerable (i.e., days) delay. Note that you will need to certify that you are unable to use another means of data retrieval.
MAST Auth Tokens
Authentication for access to Exclusive Access data via a cURL or other scripts is managed in MAST via tokens. See [MAST API Tokens](https://auth.mast.stsci.edu/info) to learn how to create or update a MAST.auth token.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "turn off interactive prompt:", "Header 3": "Batch Retrieval"} -->
The Batch Retrieval option allows the selected files to be written to external media for subsequent retrieval. Follow the steps below to stage data on the archive.stsci.edu ftp server. Note that requesting data via shippable media will incur a substantial delay, and requires that you certify that you cannot retrieve data via staging.
Staging files for ftp retrieval is currently supported for a few MAST missions (including JWST and HST), but not all. It is highly recommended to instead retrieve large numbers of files via cURL.  
| Instruction | Notes
---|---|---
**1** | Click the **Batch Retrieval** button. | ![Batch retrieval button](https://outerspace.stsci.edu/download/thumbnails/94963040/button_batch-retrieval.png?version=1&modificationDate=1657650228501&api=v2)
**2** |  Select __Staging__ from the **Delivery Method** pull-down menu and (if you are not logged in) provide the email address where you wish the notification to be sent. **Note:** If you are logged in to MAST, the e-mail address on record will be pre-filled. | ![Batch retrieval popup](https://outerspace.stsci.edu/download/thumbnails/94963040/mast_batch_retrieval.png?version=1&modificationDate=1657650228308&api=v2)
**3** | Acknowledge the pop-up notification, and check your messages at the delivery email address you specified. | ![Operation completed popup](https://outerspace.stsci.edu/download/thumbnails/94963040/mast_batch_success.png?version=1&modificationDate=1657650228292&api=v2)
**4** | The email notification will give the location of the files that have been staged. | ![Delivery status request email message](https://outerspace.stsci.edu/download/attachments/94963040/mast_batch_email.png?version=1&modificationDate=1657650228260&api=v2)
**5** |  Access the staging disk using an encrypted FTPS connection. See below for suggestions for modern, third-party clients. The MAST FTP server (**`archive.stsci.edu[](http://archive.stsci.edu)`**`)`no longer supports unencrypted FTP connections. Command-line ftp clients, as in Linux or MacOS, may not work with our server. Please see<https://archive.stsci.edu/ftp.html> |  
#### Retrieval via third-party clients
Please see the
Cyberduck (Click here to expand...)
To download the app or for more help, please see the site.
Launch the app and select Open Connection. ![](https://outerspace.stsci.edu/download/thumbnails/94963040/cyberduck_open_connection.png?version=1&modificationDate=1657650228233&api=v2)
* Under the FTP dropdown select FTP-SSL (Explicit AUTH TLS)
* Server: [archive.stsci.edu](http://archive.stsci.edu)
* Select Anonymous Login OR enter your MyST login credentials
* Select Connect  
![Cyberduck FTP Panel](https://outerspace.stsci.edu/download/attachments/94963040/cyberduck_anonymous_login.png?version=1&modificationDate=1657650228246&api=v2)
You will see two folders: "pub" and "stage":
* __pub__ contains public data available on MAST
* __stage__ contains data that have staged by MAST users. It is purged periodically.  
Under "stage", navigate to the directory specified in the email notification and you should see the folder(s) containing your download.
* To download the entire directory highlight the folder, then under Action on the menu bar select Download.
* If you only want a few files from the directory, expand the desired directory, and then select the files you want to download.  
FileZilla (Click here to expand...)
To download the app or for more help, please see the site.
Launch the app.
In the Host field enter <ftps://archive.stsci.edu>, then your MyST email address and password in the Username and Password fields, respectively. Select Quickconnect.
* If TLS connection is not set as the default, Quickconnect may be unsuccessful. If so, navigate to the Site Manager. ![](https://outerspace.stsci.edu/download/thumbnails/94963040/filezilla_sitemanager.png?version=1&modificationDate=1657650228217&api=v2)
* Select New Site
* Protocol: FTP - File Transfer Protocol
* Host: <ftps://archive.stsci.edu>
* Encryption: Require explicit FTP over TLS
* Logon Type: Select Anonymous OR enter your MyST credentials
* Select Connect  
![Filezilla FTP Panel](https://outerspace.stsci.edu/download/attachments/94963040/filezilla_sitemanager_window.png?version=1&modificationDate=1657650228198&api=v2)
Under Remote site, you will see two folders: "pub" and "stage"
* Pub is all of the public data available on MAST
* Stage is the data that has been added to the staging area  
Under "stage", navigate to the directory specified in the email notification and you should see the folder(s) containing your download.
Once you locate the folder(s) or file(s) you want to download, right click and select Download.
wget (Click here to expand...)
To install wget or for more help, please see the site.
Bring up a shell.
If you requested a retrieval anonymously, run the following command in the shell:
```
wget -r --ftp-user='anonymous' --ask-password ftps://archive.stsci.edu/stage/anonymous/<anonymous requestID>/
```  
If you were logged into MAST when you requested that your data be staged, run:
```
wget -r --ftp-user='<your full MyST email>' --ask-password ftps://archive.stsci.edu/stage/<userID>/<requestID>/
```  
Note, for users internal to STScI there may still be a certificate problem; if you encounter an error add '`--no-check-certificate`' to the command.
curl (Click here to expand...)
To install curl or for more help, please see the  is likely already installed on many machines, and if not, is freely available as open source software.  
Bring up a shell.
If you requested a retrieval anonymously, run:
```
curl --ssl-reqd -O ftp://archive.stsci.edu/stage/anonymous/<anonymous requestID>/<filename>
```  
If you were logged into MAST when you requested that your data be staged, run:
```
curl --ssl-reqd -O ftp://archive.stsci.edu/stage/<userID>/<requestID>/<filename> -u '<your full MyST email>'
```  
Note that you must include the filename in these commands. If you do not know the name of the file you'd like to retrieve, or want to download an entire directory, we recommend wget or one of the other methods detailed here.
ftp (Click here to expand...)
The MAST FTP server (**`archive.stsci.edu[](http://archive.stsci.edu)`**`)`no longer supports unencrypted FTP connections. Command-line ftp clients may not work with our server.
Bring up a shell (see note below) and initiate an ftp session on **`archive.stsci.edu[](http://archive.stsci.edu)`**.
```
% ftp archive.stsci.edu
Connected to archive.stsci.edu
```  
The appropriate login credentials will be one of the following:
* If you were logged into MAST when you requested that your data be staged, use your MyST login credentials.
* If you requested a retrieval anonymously (for non-exclusive access data), use:
* Name: anonymous
* Password: <your full MyST email address>  
```
Name: anonymous
331 Guest login ok, type your email address as
the password
Password:
```  
Navigate to the directory specified in the email notification and initiate the transfer of data files.
```
ftp> cd /stage/anonymous/<anonymous requestID>
# turn off interactive prompt:
ftp> prompt
ftp> mget *
```  
MAC OS X 10.14+ Users
Apple has removed the native ftp application for Mac OS 10.14 (Mojave) and higher. A solution is to install a third-party file-transfer application, such as

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Other Download Methods"} -->
It is possible to search for and retrieve data using MAST web services, or the Python [Beyond the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962884/Beyond+the+Portal).

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [The Download Bundle](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963052/The+Download+Bundle)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 10 END -->

