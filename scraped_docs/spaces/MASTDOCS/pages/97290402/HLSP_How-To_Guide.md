---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide"
date_accessed: "2026-03-11T16:26:46.642625"
content_length: 14845
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Contributing a New Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-ContributingaNewCollection)
* 1.1[Uploading Files to MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-UploadingFilestoMAST)
* 1.2[Tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-Tools)
* 2[Updating an Existing Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-HLSPUpdateUpdatinganExistingCollection)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Contributing a New Collection"} -->
Hosting HLSP collections is a collaborative effort between the contributing science team and MAST staff. For carefully prepared data collections, contributing the ensemble to MAST is straightforward. Just follow these steps:
1. Fill out the on-line[Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form)  
1. Consult with MAST staff early about the contribution process, ideally before the details of your collection have been finalized.
2. Contributors who wish to deliver a new version of their collection, or who are adding to an existing collection,_should not_[Updating an Existing Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-HLSPUpdate) below, and contact MAST through the [Archive Help Desk](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support).
2. Ensure that your HLSP collection contains all of the[required files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents).
3. Ensure that the science data files:
1. are provided in an[accepted format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content), and are well formed
2. contain the[required metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata)
3. are[properly named](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention)
4. Place your data products and supporting documents on an appropriate platform for electronic transfer to STScI.
1. Your MAST contact will provide specific instructions for transferring the data. See the "Uploading Files to MAST" section below for additional instructions.
2. If electronic transfer is not possible for your collection, please consult your MAST contact or e-mail the
3. (optional) Compress the files with a non-proprietary tool (e.g.,
5. Work with your MAST contact to resolve problems with the collection, if any.
6. Prior to data publication, review for accuracy the new MAST web page that describes your project.  
Details of the process for publishing an HLSP collection, along with an approximate timeline, are described in the article [Publication Timeline](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/214205149/Publication+Timeline).
Contact MAST Early!
MAST staff will gladly help you formulate and prepare your HLSP collection. It is best to contact MAST as soon as possible if you think you want to contribute a science product collection. This will provide time to work with MAST staff to understand and comply with the contribution requirements, as well as time to prepare your collection for publication when your descriptive paper is accepted for publication. Many HLSP collections are added each year. If you wish to offer an HLSP collection to MAST, please contact MAST via [submission form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form) at least 6 weeks in advance of the date you wish for the collection to be available in MAST.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Contributing a New Collection", "Header 2": "Uploading Files to MAST"} -->
Please follow these instructions **after** you have worked with MAST staff to setup your upload directory.
You can use curl and the FTPS protocol to upload files to the MAST archive, as shown in the example below:
```
curl --ssl-reqd -u USERNAME
-T 'hlsp_{dogs.txt,cats.fits,birds-and-worms.fits}'
ftp://archive.stsci.edu/pub/MY_DIR/
```  
Note the following:
1. We use --ssl-reqd to create an explicit FTPS connection. MAST [no longer supports](https://archive.stsci.edu/ftp.html) FTP connections.
2. Your username is your MyST email address; you will be prompted for your MyST password.
3. Wildcard characters in filenames are not supported, but you may use curl  
4. The destination URL should, as in the example, end with a "/". When uploading multiple files, this will fail without the ending "/".  
Another option is to use an FTP Client, such as .
Cyberduck example
To download the app or for more help, please see the site.
Launch the app and select Open Connection. ![](https://outerspace.stsci.edu/download/thumbnails/97290402/cyberduck_open_connection.png?version=1&modificationDate=1659032093796&api=v2)
* Under the FTP dropdown select FTP-SSL (Explicit AUTH TLS)
* Server: [archive.stsci.edu](http://archive.stsci.edu)
* Enter your MyST login credentials (uncheck Anonymous login)
* Select Connect  
![Cyberduck FTP Panel](https://outerspace.stsci.edu/download/attachments/97290402/cyberduck_anonymous_login.png?version=1&modificationDate=1659032093812&api=v2)Cyberduck FTP Panel
You will see two folders: "pub" and "stage":
* Pub is all of the public data available on MAST
* Stage is the staging area for your HLSP data  
Under "stage", navigate to the directory specified by MAST staff. Under 'Action' on the menu bar, select upload, then select your files.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Contributing a New Collection", "Header 2": "Tools"} -->
A small set of tools is being developed to help contributors prepare and verify their collection contents. Until they are available, contributors may benefit from
Depending upon the project, data may be delivered in stages, or re-delivered if, for instance:
* new products become available, e.g., from
* another observing program
* the continuation of a large survey program
* the software used to process and create the HLSP is revised and results in improved products  
If you find that your HLSP data products or documentation need to be revised or supplemented, please contact MAST staff at  It is not necessary to fill out a new request form.
Although MAST can discover literature references to papers related to HLSP products, it is helpful for the HLSP originators to provide updates to the list of refereed papers as they become available. Please email links to these papers to

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* HLSP [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form)
* [Publication TImeline](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/214205149/Publication+Timeline)
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents)
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
**On this page...**
* 1[Contributing a New Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-ContributingaNewCollection)
* 1.1[Uploading Files to MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-UploadingFilestoMAST)
* 1.2[Tools](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-Tools)
* 2[Updating an Existing Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-HLSPUpdateUpdatinganExistingCollection)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-ForFurtherReading...)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Contributing a New Collection"} -->
Hosting HLSP collections is a collaborative effort between the contributing science team and MAST staff. For carefully prepared data collections, contributing the ensemble to MAST is straightforward. Just follow these steps:
1. Fill out the on-line[Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form)  
1. Consult with MAST staff early about the contribution process, ideally before the details of your collection have been finalized.
2. Contributors who wish to deliver a new version of their collection, or who are adding to an existing collection,_should not_[Updating an Existing Collection](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide#HLSPHowToGuide-HLSPUpdate) below, and contact MAST through the [Archive Help Desk](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support).
2. Ensure that your HLSP collection contains all of the[required files](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents).
3. Ensure that the science data files:
1. are provided in an[accepted format](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290405/File+Types+Formats+and+Content), and are well formed
2. contain the[required metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata)
3. are[properly named](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290407/File+Naming+Convention)
4. Place your data products and supporting documents on an appropriate platform for electronic transfer to STScI.
1. Your MAST contact will provide specific instructions for transferring the data. See the "Uploading Files to MAST" section below for additional instructions.
2. If electronic transfer is not possible for your collection, please consult your MAST contact or e-mail the
3. (optional) Compress the files with a non-proprietary tool (e.g.,
5. Work with your MAST contact to resolve problems with the collection, if any.
6. Prior to data publication, review for accuracy the new MAST web page that describes your project.  
Details of the process for publishing an HLSP collection, along with an approximate timeline, are described in the article [Publication Timeline](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/214205149/Publication+Timeline).
Contact MAST Early!
MAST staff will gladly help you formulate and prepare your HLSP collection. It is best to contact MAST as soon as possible if you think you want to contribute a science product collection. This will provide time to work with MAST staff to understand and comply with the contribution requirements, as well as time to prepare your collection for publication when your descriptive paper is accepted for publication. Many HLSP collections are added each year. If you wish to offer an HLSP collection to MAST, please contact MAST via [submission form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form) at least 6 weeks in advance of the date you wish for the collection to be available in MAST.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Contributing a New Collection", "Header 2": "Uploading Files to MAST"} -->
Please follow these instructions **after** you have worked with MAST staff to setup your upload directory.
You can use curl and the FTPS protocol to upload files to the MAST archive, as shown in the example below:
```
curl --ssl-reqd -u USERNAME
-T 'hlsp_{dogs.txt,cats.fits,birds-and-worms.fits}'
ftp://archive.stsci.edu/pub/MY_DIR/
```  
Note the following:
1. We use --ssl-reqd to create an explicit FTPS connection. MAST [no longer supports](https://archive.stsci.edu/ftp.html) FTP connections.
2. Your username is your MyST email address; you will be prompted for your MyST password.
3. Wildcard characters in filenames are not supported, but you may use curl  
4. The destination URL should, as in the example, end with a "/". When uploading multiple files, this will fail without the ending "/".  
Another option is to use an FTP Client, such as .
Cyberduck example
To download the app or for more help, please see the site.
Launch the app and select Open Connection. ![](https://outerspace.stsci.edu/download/thumbnails/97290402/cyberduck_open_connection.png?version=1&modificationDate=1659032093796&api=v2)
* Under the FTP dropdown select FTP-SSL (Explicit AUTH TLS)
* Server: [archive.stsci.edu](http://archive.stsci.edu)
* Enter your MyST login credentials (uncheck Anonymous login)
* Select Connect  
![Cyberduck FTP Panel](https://outerspace.stsci.edu/download/attachments/97290402/cyberduck_anonymous_login.png?version=1&modificationDate=1659032093812&api=v2)Cyberduck FTP Panel
You will see two folders: "pub" and "stage":
* Pub is all of the public data available on MAST
* Stage is the staging area for your HLSP data  
Under "stage", navigate to the directory specified by MAST staff. Under 'Action' on the menu bar, select upload, then select your files.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Contributing a New Collection", "Header 2": "Tools"} -->
A small set of tools is being developed to help contributors prepare and verify their collection contents. Until they are available, contributors may benefit from
Depending upon the project, data may be delivered in stages, or re-delivered if, for instance:
* new products become available, e.g., from
* another observing program
* the continuation of a large survey program
* the software used to process and create the HLSP is revised and results in improved products  
If you find that your HLSP data products or documentation need to be revised or supplemented, please contact MAST staff at  It is not necessary to fill out a new request form.
Although MAST can discover literature references to papers related to HLSP products, it is helpful for the HLSP originators to provide updates to the list of refereed papers as they become available. Please email links to these papers to

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* HLSP [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form)
* [Publication TImeline](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/214205149/Publication+Timeline)
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents)
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 9 END -->

