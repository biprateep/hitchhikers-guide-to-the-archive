---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176432244/Updates+to+JWST+Data"
date_accessed: "2026-03-11T16:26:36.908167"
content_length: 13243
---

<!-- CHUNK 1 START -->
<!-- Metadata: {"Header 1": "Reprocessing JWST Data"} -->
After observations are executed on the telescope, JWST science data are processed to produce fully calibrated data products. See the articlev [JWST Science Calibration Pipeline](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-operationsOperationspipelinebuilds&gsc.tab=0) for details. The data calibration is being continuously improved over time as better, in-flight characterizations of instrument performance are derived. JWST science data are periodically reprocessed to leverage new improvements and provide the best quality products to the community. Reprocessing may happen after:
* new versions of calibration software are installed in Operations,
* new calibration reference data are delivered to the [Calibration Reference Data System](https://jwst-crds.stsci.edu/) (CRDS),
* new data are obtained for an observing program, e.g., where individual observations need to be repeated.  
The schedule for reprocessing data, and related details, are discussed in the article [Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information).

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "The Product Pedigree", "Header 2": "Pedigree of Your Data"} -->
It is useful to identify the pedigree of your data to help you figure out if you have the best available products. There are a few keyword records in the headers of science FITS files that record this information:
Keyword | Description
---|---
`CAL_VER` | The JWST Science Calibration Pipeline version used to process data (with a value like "`1.4.6`").
`CRDS_CTX` | The [context](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-crdsCRDSreferencefiles) of calibration reference data that was used to process data (with a value like "`jwst_1061.pmap`"). The context is basically a self-consistent mapping of best reference files to be used for processing to a specific version of the calibration pipeline.
`DATE` | The date/time that a product was created.
The operational version of the pipeline is typically updated every few months, but the pipeline is also released independently to the user community for custom processing. See [JWST Operations Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information) for details. Reference file updates may happen as often as a few times per month.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "The Product Pedigree", "Header 2": "Pedigree of Data in MAST"} -->
You can view pedigree of the data products in MAST by performing a search of the [JWST Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST) collection for the appropriate instrument, and selecting the Program ID for your data. After the search, look for the above-named pedigree keywords in the results table. If the values of the pedigree keywords are higher than those of the data on your machine, or the creation date is later than that of your data, the products in the Archive are newer  
There are dozens of fields displayed in the results table. To find your fields of interest more quickly, click the "Edit Columns" button, click the "Select None" button, and then check the boxes next to the pedigree keyword names, as well as that for the `filename` column.
![](https://outerspace.stsci.edu/download/thumbnails/176432244/dialog_editColumns.png?version=1&modificationDate=1677508774109&api=v2)

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Notifications of Data Updates", "Header 2": "...from MAST"} -->
You may elect to receive notifications from MAST when data from particular JWST Programs or Observations are reprocessed. See [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications) in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) to learn how to subscribe.
Some JWST programs, or even observations within programs, can take many hours (or even days) to process. If you subscribe to JWST data it is **strongly recommended** that you choose to receive notifications no more frequently than "Daily" to avoid being bombarded with messages. To manage the frequency of your subscriptions see the section on [Updating Subscriptions](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-UpdateSubscriptions).

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Notifications of Data Updates", "Header 2": "...from MAST", "Header 3": "Stale Data"} -->
You will see a warning dialog in the MAST Portal if you attempt to download Observations that are queued to be reprocessed. You have the option to proceed with the download, cancel, or subscribe to receive a notification when the data have been updated in MAST.
![Pop-up warning of selected data queued for reprocessing.](https://outerspace.stsci.edu/download/thumbnails/176432244/diallog_filesStale.png?version=1&modificationDate=1677078510685&api=v2)
The wait time specified in the dialog for calibration to complete is not currently meaningful. It may take many hours or even a few days for updated data to be available in MAST.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Notifications of Data Updates", "Header 2": "...from CRDS"} -->
You may elect to be notified when new reference files are delivered to CRDS by subscribing to a list server. There are separate distribution lists for each instrument. See the sub-section "Reference Files and my data" in the article [JWST Data Calibration Reference Files](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-crdsCRDSreferencefiles). The notification email will include a list of updated reference file names and a summary of why the reference files were updated. It may be take some time between the delivery of a new reference file and its application the operational pipeline.
New reference files are often specific to particular instrument configurations or operating modes, and therefore may not be applicable to your particular data.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [JWST Operations Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information#gsc.tab=0)
* [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications)
* [JWST Data Calibration Reference Files](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-crdsCRDSreferencefiles)
* [Calibration Reference Data System](https://jwst-crds.stsci.edu/)  
Unable to load page tree. It seems that you do not have permission to view the root page.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Reprocessing JWST Data"} -->
After observations are executed on the telescope, JWST science data are processed to produce fully calibrated data products. See the articlev [JWST Science Calibration Pipeline](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-operationsOperationspipelinebuilds&gsc.tab=0) for details. The data calibration is being continuously improved over time as better, in-flight characterizations of instrument performance are derived. JWST science data are periodically reprocessed to leverage new improvements and provide the best quality products to the community. Reprocessing may happen after:
* new versions of calibration software are installed in Operations,
* new calibration reference data are delivered to the [Calibration Reference Data System](https://jwst-crds.stsci.edu/) (CRDS),
* new data are obtained for an observing program, e.g., where individual observations need to be repeated.  
The schedule for reprocessing data, and related details, are discussed in the article [Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information).

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "The Product Pedigree", "Header 2": "Pedigree of Your Data"} -->
It is useful to identify the pedigree of your data to help you figure out if you have the best available products. There are a few keyword records in the headers of science FITS files that record this information:
Keyword | Description
---|---
`CAL_VER` | The JWST Science Calibration Pipeline version used to process data (with a value like "`1.4.6`").
`CRDS_CTX` | The [context](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-crdsCRDSreferencefiles) of calibration reference data that was used to process data (with a value like "`jwst_1061.pmap`"). The context is basically a self-consistent mapping of best reference files to be used for processing to a specific version of the calibration pipeline.
`DATE` | The date/time that a product was created.
The operational version of the pipeline is typically updated every few months, but the pipeline is also released independently to the user community for custom processing. See [JWST Operations Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information) for details. Reference file updates may happen as often as a few times per month.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "The Product Pedigree", "Header 2": "Pedigree of Data in MAST"} -->
You can view pedigree of the data products in MAST by performing a search of the [JWST Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST) collection for the appropriate instrument, and selecting the Program ID for your data. After the search, look for the above-named pedigree keywords in the results table. If the values of the pedigree keywords are higher than those of the data on your machine, or the creation date is later than that of your data, the products in the Archive are newer  
There are dozens of fields displayed in the results table. To find your fields of interest more quickly, click the "Edit Columns" button, click the "Select None" button, and then check the boxes next to the pedigree keyword names, as well as that for the `filename` column.
![](https://outerspace.stsci.edu/download/thumbnails/176432244/dialog_editColumns.png?version=1&modificationDate=1677508774109&api=v2)

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Notifications of Data Updates", "Header 2": "...from MAST"} -->
You may elect to receive notifications from MAST when data from particular JWST Programs or Observations are reprocessed. See [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications) in the [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide) to learn how to subscribe.
Some JWST programs, or even observations within programs, can take many hours (or even days) to process. If you subscribe to JWST data it is **strongly recommended** that you choose to receive notifications no more frequently than "Daily" to avoid being bombarded with messages. To manage the frequency of your subscriptions see the section on [Updating Subscriptions](https://outerspace.stsci.edu/display/MASTDOCS/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-UpdateSubscriptions).

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Notifications of Data Updates", "Header 2": "...from MAST", "Header 3": "Stale Data"} -->
You will see a warning dialog in the MAST Portal if you attempt to download Observations that are queued to be reprocessed. You have the option to proceed with the download, cancel, or subscribe to receive a notification when the data have been updated in MAST.
![Pop-up warning of selected data queued for reprocessing.](https://outerspace.stsci.edu/download/thumbnails/176432244/diallog_filesStale.png?version=1&modificationDate=1677078510685&api=v2)
The wait time specified in the dialog for calibration to complete is not currently meaningful. It may take many hours or even a few days for updated data to be available in MAST.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Notifications of Data Updates", "Header 2": "...from CRDS"} -->
You may elect to be notified when new reference files are delivered to CRDS by subscribing to a list server. There are separate distribution lists for each instrument. See the sub-section "Reference Files and my data" in the article [JWST Data Calibration Reference Files](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-crdsCRDSreferencefiles). The notification email will include a list of updated reference file names and a summary of why the reference files were updated. It may be take some time between the delivery of a new reference file and its application the operational pipeline.
New reference files are often specific to particular instrument configurations or operating modes, and therefore may not be applicable to your particular data.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [JWST Operations Pipeline Build Information](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline/jwst-operations-pipeline-build-information#gsc.tab=0)
* [Program Subscriptions and Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications)
* [JWST Data Calibration Reference Files](https://jwst-docs.stsci.edu/jwst-science-calibration-pipeline#JWSTScienceCalibrationPipeline-crdsCRDSreferencefiles)
* [Calibration Reference Data System](https://jwst-crds.stsci.edu/)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 14 END -->

