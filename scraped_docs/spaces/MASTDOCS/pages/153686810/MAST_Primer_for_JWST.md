---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST"
date_accessed: "2026-03-11T11:32:57.012638"
---

<!-- CHUNK 1 START -->
Key elements of MAST interfaces are summarized here, and include Portal tutorials for users new to MAST.
**On this page...**
* 1[Getting Started with MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-GettingStartedwithMAST)
* 1.1[Login](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Login)
* 1.2[Exclusive Access Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ExclusiveAccessData)
* 1.3[MAST Interfaces](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-MASTInterfaces)
* 1.3.1[Web Applications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-WebApplications)
* 1.3.2[API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-API)
* 2[Portal Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorialsPortalTutorials)
* 2.1[Searches with the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-SearcheswiththePortal)
* 2.1.1[Target Name or Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-TargetNameorCoordinates)
* 2.1.2[Program ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ProgramID)
* 2.1.3[JWST Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Instrument_KWJWSTInstrumentKeywords)
* 3[Data Retrieval Options](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-RetrievalDataRetrievalOptions)
* 3.1[Direct Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-DirectDownload)
* 3.2[Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-BasketDownloadBasket)
* 3.2.1[Streaming Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-StreamingDownload)
* 3.2.2[Download via cURL Script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-DownloadviacURLScript)
* 3.2.3[Batch Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-BatchDownload)
* 4[API Tutorial](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-APITutorial)
* 5[What's in the Box](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-What'sintheBox)
* 5.1[File Names and Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-FileNamesandContent)
* 6[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ForFurtherReading...)
* 6.1[Reference Documents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ReferenceDocuments)
* 6.2[User Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-UserSupport)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Login"} -->
Certain operations require that you log into MAST. This includes access to most data from active JWST observing programs. See [MAST Accounts](https://outerspace.stsci.edu/display/MASTDOCS/MAST+Accounts) for details.
If you have a MyST account and login to MAST you may [subscribe to notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications) about JWST program data availability, even for observations that have not yet executed.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Exclusive Access Data"} -->
All data from JWST will eventually become public, and anyone may conduct searches for JWST data. However, when data fall under an **_exclusive access period_** (**EAP**) the files may only be retrieved by authorized persons. To retrieve EAP data from MAST:
* You _**must**_ have a MyST account. See this URL to create one: <https://proper.stsci.edu/proper/authentication/auth>
* Login to MAST at any point prior to retrieving data. See [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts) for details.
* Those with MyST accounts must be authorized by the PI of the program to retrieve EAP data.
* PIs of observing programs may grant access to Co-Is (or anyone with a MyST account) by visiting [MyST](https://proper.stsci.edu/proper/authentication/auth) and selecting __Registered Users__ → __Update__ → __Manage Access to Exclusive Access Science Data__.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "MAST Interfaces", "Header 3": "Web Applications"} -->
MAST offers a multiple web-based tools to search for and retrieve science and engineering data, or for other information. Links to these tools appear in the table below.
Search Type | Select a collection... | URL
---|---|---
**Observations of a target or field** | _MAST Observations by Object Name or RA/Dec_ | <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html>
**Observations Matching a Program ID** | Observations by Program ID
**Files matching Instrument Keyword Values** | _JWST Instrument Keywords_
**Wavefront Sensing products** | _JWST WSS_
**DOI Portal
** |  | <https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html>
**Calibrated Engineering Data** |
| <https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html>
**Keyword Dictionary** |
| <https://mast.stsci.edu/portal/Mashup/Clients/jwkeywords/index.html>
Browser Issues
Note that the MAST Portal has incompatibilities with certain browsers and settings. In particular, pop-up blockers must grant an exception for the [mast.stsci.edu](http://mast.stsci.edu) domain. For details see [Introduction to the MAST Portal](https://outerspace.stsci.edu/display/MASTDOCS/Introduction+to+the+Portal) in the [Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide).

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "MAST Interfaces", "Header 3": "API"} -->
Many users find scripted access to MAST searches and data retrievals to suit their needs better. The most popular interface offered is the Python package [JWST Archive Manual](https://outerspace.stsci.edu/display/MASTDOCS/JWST+Archive+Manual) in the [Using MAST APIs](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs) chapter.
* * *
The MAST Portal search panel is shown below. It is a starting point for your interactions with MAST.
![](https://outerspace.stsci.edu/download/attachments/153686810/panel_search.png?version=1&modificationDate=1683571071500&api=v2)
All of the searches described below start with selecting the appropriate __collection__ for a search, from the drop-down menu shown at right.
![](https://outerspace.stsci.edu/download/thumbnails/153686810/menu_selectCollection_obs.png?version=1&modificationDate=1683571071477&api=v2)
Search results are displayed below the search panel, as shown in the example below.  
![](https://outerspace.stsci.edu/download/attachments/153686810/window_results_m57.png?version=1&modificationDate=1683571071467&api=v2)
Results consist of Filter dialogs (_left_); a table of matched results (_center_) showing rows for public (_white background_), Exclusive Access (_yellow background_ , with the padlock icon), and planned but not yet executed observations (_orange background_); and the AstroView tool (_right_) which shows the spatial extent (_colored footprints_) of the exposures superimposed on an image of the sky. For details see [Field Guide to the Portal](https://outerspace.stsci.edu/display/MASTDOCS/Field+Guide+to+the+Portal).

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Searches with the Portal"} -->
Many types of Portal search return _**Observations**_ , which are really collections of all available data products, including uncalibrated, intermediate, fully calibrated, and combined science data. See [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) to learn more about how various kinds of data products are associated in the Portal. See [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Basket) to learn how to select and download one or more of these types of products.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Searches with the Portal", "Header 3": "Target Name or Coordinates"} -->
A basic search will return Observations from all hosted MAST missions. **This search will provide access to all levels of JWST data products.**
Standard Search for Target/Coordinates...  
| Instruction | Notes
---|---|---
**1** | Select '_MAST Observations by Object Name or RA/Dec_ ' from the '**Select a collection…** ’ pull-down menu at the left of the search panel. |  
**2** |  Enter a target name and (optionally) a search radius, which will be resolved to coordinates. See [Basic Search](https://outerspace.stsci.edu/display/MASTDOCS/Basic+Search) for syntax rules. `**m57 r=1m**` | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_target_m57.png?version=1&modificationDate=1683571071459&api=v2)
**3** | Click the **Search** button to the right of the target dialog. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_search_1.png?version=1&modificationDate=1683571071448&api=v2)
**4
** |  **Optional:** Filter the results in the left panel by selecting Mission: _`JWST`_and the Instrument(s)/configuration(s). For example:_`MIRI/IFU`_and __`NIRSPEC/IFU`__ | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_grid_miri.png?version=1&modificationDate=1683577980839&api=v2)
**5** | Evaluate the search results grid. It will look something like the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). |  
An advanced search allows you to customize the query by additional attributes, and can return Observations for all hosted MAST missions. This search will provide access for access to all levels of JWST data products (unless you choose to restrict the calibration level).
Advanced Search for Targets...  
| Instruction | Notes
---|---|---
**1** | Select __MAST Observations by Object Name or RA/Dec__ from the '**Select a collection…** ’ pull-down menu on the upper-left. |  
**2** | To search using more criteria than target name or position, click the __Advanced Search__ link below the target dialog. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_enterTarget.png?version=1&modificationDate=1683571070908&api=v2)
**3
** |  Search by multiple criteria with filter dialogs. In this case:
* Mission: _`JWST`_will greatly accelerate the query
* Instrument: _MIRI*_ (i.e., all configurations of MIRI). Note typing the name of the instrument in the dialog box will accelerate the selection.
* Target Name: _NGC6720*_. Including the asterisk (wildcard) at the end will select the target name and variants, which may include offset positions.  
|  ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_mission_jwst.png?version=1&modificationDate=1683571070858&api=v2)![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_instr_miri.png?version=1&modificationDate=1683578421008&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_target_m57.png?version=1&modificationDate=1683571070692&api=v2)
**4
** | Click the search button at upper-left. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_search.png?version=1&modificationDate=1683571071244&api=v2)
**5** | The search results grid will look similar to the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). Select one or more Observations by ticking the box(es) at the left of the results table, then choose a [download method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Retrieval).  |

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Searches with the Portal", "Header 3": "Program ID"} -->
This type of search will return all Observations for a given observing program (a.k.a. proposal number). This is a quick way for Investigator Teams to search for all data related to their science program.
This search will match program IDs for both JWST and HST, even though the results for one mission are not scientifically related to the other. It is easy to filter the results table for the mission of interest.
Search by Proposal ID...  
| Instruction | Notes
---|---|---
**1** | Select __MAST Observations by Proposal ID__ from the '**Select a collection…** ’ pull-down menu on the upper-left. |  
**2** | Enter one or more proposal numbers, separated by commas, then click the **Search** button. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_propID.png?version=1&modificationDate=1683571071393&api=v2)
**3** | Filter the results to select the common target `VV191`. (Note the variations in the spelling.) | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_targName.png?version=1&modificationDate=1683571071372&api=v2)
**4** | The search results grid will look something like the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). Select one or more Observations by ticking the box(es) at the left of the results table, then choose a [download method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Retrieval).  |  
This type of search for JWST data provides a much larger set of criteria, including important metadata that are not available in standard searches such as:
* the flag for time-series observations (`tsovisit`)
* exposure type (`exp_type`, which could indicate, e.g., coronographic observations)
* observation sequence identifier (`observtn`)
* program category (`category`, e.g., COM and ERS where all data are instantly public)  
Beware that this type of search matches data for only one selected JWST instrument, and only the _highest-level calibrated science FITS files_.
Highest-level products only!
This kind of search will **not** provide access to ancillary files, nor to uncalibrated (e.g., Level-1b) files if higher-level products exist. It will also not match calibrated files that are not in FITS format, such as source catalogs or light curves.
Instrument Keywords...  
| Instruction | Notes
---|---|---
**1** | Select __JWST Instrument Keywords__ from the '**Select a collection…** ’ pull-down menu on the upper-left, and select the instrument of interest from the pull-down menu below that. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/menu_JwInstr_niriss.png?version=1&modificationDate=1683571071353&api=v2)
**2** | Click the __Advanced Search__ button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_adv-search.png?version=1&modificationDate=1683571071333&api=v2)
**3** | Open filter dialogs of interest and enter search parameters. In this example we search **COM** and **ERS** programs for **Single-Object Slitless Spectra** taken in **Time-series** mode. |  ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_Category.png?version=1&modificationDate=1683571071312&api=v2)![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_ExpType.png?version=1&modificationDate=1683571071281&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_TsoVisit.png?version=1&modificationDate=1683571071260&api=v2)
**4** | Click the **Search** button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_search.png?version=1&modificationDate=1683571071244&api=v2)
**5** |  **Optional:** Filter the results table for Level-3 (fully calibrated and combined) data products. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_L3products.png?version=1&modificationDate=1683571071229&api=v2)
**6** | The search results grid will look something like the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). Select one or more Observations by ticking the box(es) at the left of the results table, then choose a [download method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Retrieval).  |  
There is a way, using scripted queries, to search by values of instrument keywords and return Observations, that is, complete collections of all data products that match the query criteria. See [API Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-APITutorials) for details.
* * *
There are multiple options for downloading data products from MAST. Each option has its strengths, as noted below.
Searches that return Observations to the results table contain links to all available JWST products associated with each Observation. Place one or more results in the Download Basket to view and select exactly which products (e.g., uncalibrated data) to download.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Direct Download"} -->
This is the simplest form of download, and works for individual entries in the results table. The download bundle is streamed to your machine through your browser.
MRP files only
This option **does not** download all available products, but rather the most highly calibrated and combined science products. It is similar to downloading from the basket when the [_Minimum Recommended Products_](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products) option is selected.
Direct Streaming Download...  
| Instruction | Notes
---|---|---
1 | Click the **file icon** in one of the rows in the results table. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/file_icon_white.png?version=1&modificationDate=1683571071203&api=v2)
2 |  After a moment a pop-up dialog may appear, asking if the file should be saved. Note that the files are zipped for transfer efficiency.  Whether a dialog appears, and the specific wording in the dialog, depend upon browser settings. The location where the files will be written also depends upon your browser settings. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_fileSave.png?version=1&modificationDate=1683571071191&api=v2)
This form of download is intended for retrieving multiple observations at once, and for retrieving all (or only selected) types of products. There are three options: immediate streaming download (which imposes a size limit), and retrieval by curl script or ftp staging (which do not).

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Direct Download", "Header 3": "Streaming Download"} -->
This example applies to results that contain Observations, rather than individual files (as you would have after an Instrument Keyword search).
Streaming Download from Basket...  
| Instruction | Notes
---|---|---
**1** | Select one or more rows in the results grid. |  
**2** | Click the **basket button** just above the grid to add the selected files to your download basket. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_downloadBasket.png?version=1&modificationDate=1683571071164&api=v2)
**3
** |  The Download Manager window may look something like that below. Note that the number of files associated with JWST Observations can be very large (nearly 7500 in this case). ![](https://outerspace.stsci.edu/download/attachments/153686810/DLM_panel.png?version=1&modificationDate=1683571071156&api=v2)
**4
** | The next task is to select which files to include in the download bundle, which consists of two steps:
**4a** |  **Recommended:** use one or more filter dialogs to select _types_ of products to include or exclude.
* Note that selecting [Minimum Recommended Products](https://outerspace.stsci.edu/display/MASTDOCS/Minimum+Recommended+Products) will hide lower-level (uncalibrated) products from the file selector tree.
* Selecting `SCIENCE` and `INFO` categories will include all files necessary for re-running the calibration pipeline on your own machine.
* Not including the `AUXILIARY` category will have the effect of excluding guide-star files. This may greatly decrease the volume of data (7282 files in this example)
* Selecting the `UNCAL` group will include uncalibrated (Level 1-b) files. Your selection for the MRP checkbox will be remembered for subsequent downloads during your Portal session.  
|  ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_MRP.png?version=1&modificationDate=1683571071141&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/DLM_filter_productCat.png?version=1&modificationDate=1683571071117&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/DLM_filter_Group.png?version=1&modificationDate=1683571071095&api=v2)
**4b** |  **Required:** Select specific files or sub-directories of files to include.
* check the boxes of observations and/or files you wish to download.
* **Note:** checking the box of a parent observation automatically checks the boxes of all child files in the dataset.
* **optional:** click the triangle on the left to review the detailed contents of the sub-directory.  
| ![](https://outerspace.stsci.edu/download/thumbnails/153686810/DLM_file_selector_detail.png?version=1&modificationDate=1683571071066&api=v2)
**6
** |  **Optional:** After selecting exposures of interest, click the **Retrieve References** button to bring up a dialog where you can choose one or more of all the [calibration reference files](https://outerspace.stsci.edu/display/MASTDOCS/Calibration+Reference+Files) that were used by the CAL pipeline to produce the selected data products. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_retrieve-refs.png?version=1&modificationDate=1683571071043&api=v2)
**7** | Click the **Download** button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_download.png?version=1&modificationDate=1683571071034&api=v2)
**8** |  Select the format for the download package from the pull-down, then click the **Download** but **Optional:** Check the "Remove completed files from basket" box. This will purge download basket, which may help avoid confusion the next time you prepare to download files using the basket. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_download-fmt.png?version=1&modificationDate=1683571071026&api=v2)

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Direct Download", "Header 3": "Download via cURL Script"} -->
This type of retrieval is asynchronous and has no limits to the volume of data to download. It is more robust against internet interruptions, and can be resumed if interrupted.
Download cURL retrieval script...  
| Instruction | Notes
---|---|---
**1** | Follow instructions 1–7 for Streaming Download (above). |  
**2** | Select __Curl__ from the file **Format** pull-down menu. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_download_curl.png?version=1&modificationDate=1683571071001&api=v2)
**3** |  Save the cURL shell script in a directory where you wish the data files to be stored. Whether a dialog appears, and the specific wording in the dialog, depend upon browser settings. The location where the files will be written also depends upon your browser settings. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_fileSave_curl.png?version=1&modificationDate=1683571070993&api=v2)
**4** |  Bring up a shell and execute the downloaded script. **Note:** If you are retrieving Exclusive Access Protected data, you will need to either provide your MyST login credentials, or have set an environment varialbe with your [Auth.MAST token](https://auth.mast.stsci.edu/info), in order for the shell to complete the retrieval successfully. The cURL script is targeted to a **bash** shell. Specifying **bash** on the command line allows it to be invoked from any unix shell. |  ```
bash MAST_2018-10-31T2028.sh
```

MAST Auth Tokens
Authentication for access to EAP data via a cURL or other scripts is managed in MAST via tokens. See [MAST API Tokens](https://auth.mast.stsci.edu/info) to learn how to create or update a MAST.auth token.
### Batch Download
Staging files for **ftps** retrieval is currently supported for a few MAST missions (including JWST and HST), but not all. It is highly recommended to instead retrieve large numbers of files via cURL scripts.
Staging for FTPS Retrieval...

| Instruction | Notes
---|---|---
**1** | Follow instructions 1–6 for Immediate Download (above). |

**2** | Click the **Batch Retrieval** button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_batch-retrieval.png?version=1&modificationDate=1683571070977&api=v2)
**3** |  Select __staging__ from the file **Delivery Method** pull-down menu and (if you are not logged in) provide the email address where you wish the notification to be sent. **Note:** If you are logged in to MAST, the e-mail address on record will be pre-filled. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_staging.png?version=1&modificationDate=1683571070959&api=v2)
**4** | Acknowledge the email pop-up notification, and check your email at the delivery address you specified.

| ![](https://outerspace.stsci.edu/download/thumbnails/153686810/popUp_email.png?version=1&modificationDate=1683571070936&api=v2)
**5
** | The email notification will give the location of the files that have been staged. |
**6
** | Use a third-party client such as Cyberduck or  |
* * *
# API Tutorial
The following tutorial introduces the basics of MAST queries with the [JWST Archive Manual](https://outerspace.stsci.edu/display/MASTDOCS/JWST+Archive+Manual) in the [Using MAST APIs](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs) chapter.
API Example...
The set of all available parameters for this type of query is summarized [here](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html). Consider a search for JWST/NIRCam observations in observing program 1073, using the F277W filter. Use the **`.query_criteria()`**method.
```
matched_obs = Observations.query_criteria(
obs_collection = 'JWST'
, proposal_id = '1073'
, instrument_name = 'Nircam'
, filters = 'F277W'
)
```

The result is an **astropy** `Table` object, with one row per matched observation.
If for a particular query you are not interested in observations from any mission except JWST, specify it with the parameter `obs_collection='JWST'`. This will narrow the list of possible matches considerably, and speed up your query.
Having found Observations that match your criteria, the next step is to fetch a table of data products associated with each Observation.
Some observations contain huge numbers of associated or linked files, sometimes in excess of 10,000 products. This is particularly true for NIRSpec MSA, or MIRI and NIRCam slitless spectroscopy, but may also be true for large mosaics of images. Each observation is likely to contain many files in common, such as guide-star files and ancillary products.
**It is strongly recommended to retrieve product lists one or a few at a time from each observation to avoid server timeouts, and then to construct a set of unique products from the combined observations to avoid large numbers of duplicated products.**
The following retrieves a list of tables of data products for each observation, and returns combined table containing unique data products.
```
if (matched_obs > 0):
t = [Observations.get_product_list(obs) for obs in matched_obs]
files = unique(vstack(t), keys='productFilename')
```

If at least one observation matched the search criteria the above call returns a table of unique products, one per row, which could number in the hundreds or thousands. You may wish to filter the results by masking all but a limited number of file suffixes and excluding certain sub-strings.
The selected products may now be downloaded to your local machine. Note that you will need to login with a valid [Auth.MAST](https://auth.mast.stsci.edu/info) token to download exclusive access (EAP) data. If the token is needed but not supplied, the you will be prompted to enter one.
You may download all the products in the files table, or select a subset if you prefer. The following will select L-1b products (i.e. the raw, uncalibrated, `*_uncal.fits`) from the data product list for retrieval. Other types of products may instead be selected, either by matching product name sub-strings or selecting named products in the `productSubGroupDescription`.
```
manifest = Observations.download_products(
files,
productSubGroupDescription='UNCAL',
curl_flag=True
)
```

Setting the optional `curl_flag` parameter to **`True`**will instead download a**bash** script that contains **cURL** commands to fetch the files at a later time. This approach is highly recommended for large numbers of files. The name of the download script will be something like: mastDownload_**YYYYMMDDhhmmss**.sh, where the latter part of the name is a numeric timestamp. What remains is to invoke the downloaded script on your machine to retrieve the files.
* * *
# What's in the Box
All data products for all selected observations will be bundled together for delivery. When the Zip or tar file is unpacked, data for each observation/visit/exposure will appear in a separate sub-directory.
For each sub-directory, the data bundle includes by default the highest-level data products, _plus all parent data_. For example, if an observation/visit/exposure combination resulted in Level-2 data products, all Level-1 products would automatically be included unless the user explicitly chooses otherwise.
The Download Manifest
The zip (or tar) file will include a file called **`MANIFEST.HTML`**which lists each file name, a short description, and whether access is restricted. It will also note any files that could not be downloaded and the reason why (e.g., if you do not have permission to retrieve them).
## File Names and Content
The semantic content of science files may be inferred from the file suffix, and the filename signature. For example, files ending in _**`_uncal.fits`**_are Level-1b uncalibrated science products. See the JWST**.
**
* * *
# For Further Reading...
## Reference Documents
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual)
* [JWST User Documentation Home](https://jwst-docs.stsci.edu/) (JDox)


## User Support
* **Archive Help Desk:**
* **JWST**


Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)


* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [MAST Primer for JWST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST "MAST Primer for JWST")
* [Updates to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176432244/Updates+to+JWST+Data "Updates to JWST Data")
* [JWST Instrument Names](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/176435458/JWST+Instrument+Names "JWST Instrument Names")
* [JWST Acronyms](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150112931/JWST+Acronyms "JWST Acronyms")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
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
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")


Key elements of MAST interfaces are summarized here, and include Portal tutorials for users new to MAST.
**On this page...**
* 1[Getting Started with MAST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-GettingStartedwithMAST)
* 1.1[Login](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Login)
* 1.2[Exclusive Access Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ExclusiveAccessData)
* 1.3[MAST Interfaces](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-MASTInterfaces)
* 1.3.1[Web Applications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-WebApplications)
* 1.3.2[API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-API)
* 2[Portal Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorialsPortalTutorials)
* 2.1[Searches with the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-SearcheswiththePortal)
* 2.1.1[Target Name or Coordinates](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-TargetNameorCoordinates)
* 2.1.2[Program ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ProgramID)
* 2.1.3[JWST Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Instrument_KWJWSTInstrumentKeywords)
* 3[Data Retrieval Options](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-RetrievalDataRetrievalOptions)
* 3.1[Direct Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-DirectDownload)
* 3.2[Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-BasketDownloadBasket)
* 3.2.1[Streaming Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-StreamingDownload)
* 3.2.2[Download via cURL Script](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-DownloadviacURLScript)
* 3.2.3[Batch Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-BatchDownload)
* 4[API Tutorial](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-APITutorial)
* 5[What's in the Box](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-What'sintheBox)
* 5.1[File Names and Content](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-FileNamesandContent)
* 6[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ForFurtherReading...)
* 6.1[Reference Documents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-ReferenceDocuments)
* 6.2[User Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-UserSupport)


# Getting Started with MAST
## Login
Certain operations require that you log into MAST. This includes access to most data from active JWST observing programs. See [MAST Accounts](https://outerspace.stsci.edu/display/MASTDOCS/MAST+Accounts) for details.
If you have a MyST account and login to MAST you may [subscribe to notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications) about JWST program data availability, even for observations that have not yet executed.
## Exclusive Access Data
All data from JWST will eventually become public, and anyone may conduct searches for JWST data. However, when data fall under an **_exclusive access period_** (**EAP**) the files may only be retrieved by authorized persons. To retrieve EAP data from MAST:
* You _**must**_ have a MyST account. See this URL to create one: <https://proper.stsci.edu/proper/authentication/auth>
* Login to MAST at any point prior to retrieving data. See [MAST Accounts](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/136481910/MAST+Accounts) for details.
* Those with MyST accounts must be authorized by the PI of the program to retrieve EAP data.
* PIs of observing programs may grant access to Co-Is (or anyone with a MyST account) by visiting [MyST](https://proper.stsci.edu/proper/authentication/auth) and selecting __Registered Users__ → __Update__ → __Manage Access to Exclusive Access Science Data__.


## MAST Interfaces
### Web Applications
MAST offers a multiple web-based tools to search for and retrieve science and engineering data, or for other information. Links to these tools appear in the table below.
Search Type | Select a collection... | URL
---|---|---
**Observations of a target or field** | _MAST Observations by Object Name or RA/Dec_ | <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html>
**Observations Matching a Program ID** | Observations by Program ID
**Files matching Instrument Keyword Values** | _JWST Instrument Keywords_
**Wavefront Sensing products** | _JWST WSS_
**DOI Portal
** |  | <https://mast.stsci.edu/portal/Mashup/Clients/DOI/DOIPortal.html>
**Calibrated Engineering Data** |
| <https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html>
**Keyword Dictionary** |
| <https://mast.stsci.edu/portal/Mashup/Clients/jwkeywords/index.html>
Browser Issues
Note that the MAST Portal has incompatibilities with certain browsers and settings. In particular, pop-up blockers must grant an exception for the [mast.stsci.edu](http://mast.stsci.edu) domain. For details see [Introduction to the MAST Portal](https://outerspace.stsci.edu/display/MASTDOCS/Introduction+to+the+Portal) in the [Portal Guide](https://outerspace.stsci.edu/display/MASTDOCS/Portal+Guide).
### API
Many users find scripted access to MAST searches and data retrievals to suit their needs better. The most popular interface offered is the Python package [JWST Archive Manual](https://outerspace.stsci.edu/display/MASTDOCS/JWST+Archive+Manual) in the [Using MAST APIs](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs) chapter.
* * *
The MAST Portal search panel is shown below. It is a starting point for your interactions with MAST.
![](https://outerspace.stsci.edu/download/attachments/153686810/panel_search.png?version=1&modificationDate=1683571071500&api=v2)
All of the searches described below start with selecting the appropriate __collection__ for a search, from the drop-down menu shown at right.
![](https://outerspace.stsci.edu/download/thumbnails/153686810/menu_selectCollection_obs.png?version=1&modificationDate=1683571071477&api=v2)
Search results are displayed below the search panel, as shown in the example below.


![](https://outerspace.stsci.edu/download/attachments/153686810/window_results_m57.png?version=1&modificationDate=1683571071467&api=v2)
Results consist of Filter dialogs (_left_); a table of matched results (_center_) showing rows for public (_white background_), Exclusive Access (_yellow background_ , with the padlock icon), and planned but not yet executed observations (_orange background_); and the AstroView tool (_right_) which shows the spatial extent (_colored footprints_) of the exposures superimposed on an image of the sky. For details see [Field Guide to the Portal](https://outerspace.stsci.edu/display/MASTDOCS/Field+Guide+to+the+Portal).
## Searches with the Portal
Many types of Portal search return _**Observations**_ , which are really collections of all available data products, including uncalibrated, intermediate, fully calibrated, and combined science data. See [Linkages in the Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771325/Linkages+in+the+Portal) to learn more about how various kinds of data products are associated in the Portal. See [Download Basket](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Basket) to learn how to select and download one or more of these types of products.
### Target Name or Coordinates
A basic search will return Observations from all hosted MAST missions. **This search will provide access to all levels of JWST data products.**
Standard Search for Target/Coordinates...

| Instruction | Notes
---|---|---
**1** | Select '_MAST Observations by Object Name or RA/Dec_ ' from the '**Select a collection…** ’ pull-down menu at the left of the search panel. |

**2** |  Enter a target name and (optionally) a search radius, which will be resolved to coordinates. See [Basic Search](https://outerspace.stsci.edu/display/MASTDOCS/Basic+Search) for syntax rules. `**m57 r=1m**` | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_target_m57.png?version=1&modificationDate=1683571071459&api=v2)
**3** | Click the **Search** button to the right of the target dialog. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_search_1.png?version=1&modificationDate=1683571071448&api=v2)
**4
** |  **Optional:** Filter the results in the left panel by selecting Mission: _`JWST`_and the Instrument(s)/configuration(s). For example:_`MIRI/IFU`_and __`NIRSPEC/IFU`__ | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_grid_miri.png?version=1&modificationDate=1683577980839&api=v2)
**5** | Evaluate the search results grid. It will look something like the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). |

An advanced search allows you to customize the query by additional attributes, and can return Observations for all hosted MAST missions. This search will provide access for access to all levels of JWST data products (unless you choose to restrict the calibration level).
Advanced Search for Targets...

| Instruction | Notes
---|---|---
**1** | Select __MAST Observations by Object Name or RA/Dec__ from the '**Select a collection…** ’ pull-down menu on the upper-left. |

**2** | To search using more criteria than target name or position, click the __Advanced Search__ link below the target dialog. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_enterTarget.png?version=1&modificationDate=1683571070908&api=v2)
**3
** |  Search by multiple criteria with filter dialogs. In this case:
* Mission: _`JWST`_will greatly accelerate the query
* Instrument: _MIRI*_ (i.e., all configurations of MIRI). Note typing the name of the instrument in the dialog box will accelerate the selection.
* Target Name: _NGC6720*_. Including the asterisk (wildcard) at the end will select the target name and variants, which may include offset positions.

|  ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_mission_jwst.png?version=1&modificationDate=1683571070858&api=v2)![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_instr_miri.png?version=1&modificationDate=1683578421008&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_target_m57.png?version=1&modificationDate=1683571070692&api=v2)
**4
** | Click the search button at upper-left. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_search.png?version=1&modificationDate=1683571071244&api=v2)
**5** | The search results grid will look similar to the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). Select one or more Observations by ticking the box(es) at the left of the results table, then choose a [download method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Retrieval).  |

### Program ID
This type of search will return all Observations for a given observing program (a.k.a. proposal number). This is a quick way for Investigator Teams to search for all data related to their science program.
This search will match program IDs for both JWST and HST, even though the results for one mission are not scientifically related to the other. It is easy to filter the results table for the mission of interest.
Search by Proposal ID...

| Instruction | Notes
---|---|---
**1** | Select __MAST Observations by Proposal ID__ from the '**Select a collection…** ’ pull-down menu on the upper-left. |

**2** | Enter one or more proposal numbers, separated by commas, then click the **Search** button. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_propID.png?version=1&modificationDate=1683571071393&api=v2)
**3** | Filter the results to select the common target `VV191`. (Note the variations in the spelling.) | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_targName.png?version=1&modificationDate=1683571071372&api=v2)
**4** | The search results grid will look something like the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). Select one or more Observations by ticking the box(es) at the left of the results table, then choose a [download method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Retrieval).  |

This type of search for JWST data provides a much larger set of criteria, including important metadata that are not available in standard searches such as:
* the flag for time-series observations (`tsovisit`)
* exposure type (`exp_type`, which could indicate, e.g., coronographic observations)
* observation sequence identifier (`observtn`)
* program category (`category`, e.g., COM and ERS where all data are instantly public)


Beware that this type of search matches data for only one selected JWST instrument, and only the _highest-level calibrated science FITS files_.
Highest-level products only!
This kind of search will **not** provide access to ancillary files, nor to uncalibrated (e.g., Level-1b) files if higher-level products exist. It will also not match calibrated files that are not in FITS format, such as source catalogs or light curves.
Instrument Keywords...

| Instruction | Notes
---|---|---
**1** | Select __JWST Instrument Keywords__ from the '**Select a collection…** ’ pull-down menu on the upper-left, and select the instrument of interest from the pull-down menu below that. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/menu_JwInstr_niriss.png?version=1&modificationDate=1683571071353&api=v2)
**2** | Click the __Advanced Search__ button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_adv-search.png?version=1&modificationDate=1683571071333&api=v2)
**3** | Open filter dialogs of interest and enter search parameters. In this example we search **COM** and **ERS** programs for **Single-Object Slitless Spectra** taken in **Time-series** mode. |  ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_Category.png?version=1&modificationDate=1683571071312&api=v2)![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_ExpType.png?version=1&modificationDate=1683571071281&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_TsoVisit.png?version=1&modificationDate=1683571071260&api=v2)
**4** | Click the **Search** button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_search.png?version=1&modificationDate=1683571071244&api=v2)
**5** |  **Optional:** Filter the results table for Level-3 (fully calibrated and combined) data products. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_L3products.png?version=1&modificationDate=1683571071229&api=v2)
**6** | The search results grid will look something like the [example](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-PortalTutorials). Select one or more Observations by ticking the box(es) at the left of the results table, then choose a [download method](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686810/MAST+Primer+for+JWST#MASTPrimerforJWST-Retrieval).  |

There is a way, using scripted queries, to search by values of instrument keywords and return Observations, that is, complete collections of all data products that match the query criteria. See [API Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs#UsingMASTAPIs-APITutorials) for details.
* * *
There are multiple options for downloading data products from MAST. Each option has its strengths, as noted below.
Searches that return Observations to the results table contain links to all available JWST products associated with each Observation. Place one or more results in the Download Basket to view and select exactly which products (e.g., uncalibrated data) to download.
## Direct Download
This is the simplest form of download, and works for individual entries in the results table. The download bundle is streamed to your machine through your browser.
MRP files only
This option **does not** download all available products, but rather the most highly calibrated and combined science products. It is similar to downloading from the basket when the [_Minimum Recommended Products_](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131859421/Minimum+Recommended+Products) option is selected.
Direct Streaming Download...

| Instruction | Notes
---|---|---
1 | Click the **file icon** in one of the rows in the results table. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/file_icon_white.png?version=1&modificationDate=1683571071203&api=v2)
2 |  After a moment a pop-up dialog may appear, asking if the file should be saved. Note that the files are zipped for transfer efficiency.  Whether a dialog appears, and the specific wording in the dialog, depend upon browser settings. The location where the files will be written also depends upon your browser settings. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_fileSave.png?version=1&modificationDate=1683571071191&api=v2)
This form of download is intended for retrieving multiple observations at once, and for retrieving all (or only selected) types of products. There are three options: immediate streaming download (which imposes a size limit), and retrieval by curl script or ftp staging (which do not).
### Streaming Download
This example applies to results that contain Observations, rather than individual files (as you would have after an Instrument Keyword search).
Streaming Download from Basket...

| Instruction | Notes
---|---|---
**1** | Select one or more rows in the results grid. |

**2** | Click the **basket button** just above the grid to add the selected files to your download basket. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_downloadBasket.png?version=1&modificationDate=1683571071164&api=v2)
**3
** |  The Download Manager window may look something like that below. Note that the number of files associated with JWST Observations can be very large (nearly 7500 in this case). ![](https://outerspace.stsci.edu/download/attachments/153686810/DLM_panel.png?version=1&modificationDate=1683571071156&api=v2)
**4
** | The next task is to select which files to include in the download bundle, which consists of two steps:
**4a** |  **Recommended:** use one or more filter dialogs to select _types_ of products to include or exclude.
* Note that selecting [Minimum Recommended Products](https://outerspace.stsci.edu/display/MASTDOCS/Minimum+Recommended+Products) will hide lower-level (uncalibrated) products from the file selector tree.
* Selecting `SCIENCE` and `INFO` categories will include all files necessary for re-running the calibration pipeline on your own machine.
* Not including the `AUXILIARY` category will have the effect of excluding guide-star files. This may greatly decrease the volume of data (7282 files in this example)
* Selecting the `UNCAL` group will include uncalibrated (Level 1-b) files. Your selection for the MRP checkbox will be remembered for subsequent downloads during your Portal session.

|  ![](https://outerspace.stsci.edu/download/thumbnails/153686810/filter_MRP.png?version=1&modificationDate=1683571071141&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/DLM_filter_productCat.png?version=1&modificationDate=1683571071117&api=v2) ![](https://outerspace.stsci.edu/download/thumbnails/153686810/DLM_filter_Group.png?version=1&modificationDate=1683571071095&api=v2)
**4b** |  **Required:** Select specific files or sub-directories of files to include.
* check the boxes of observations and/or files you wish to download.
* **Note:** checking the box of a parent observation automatically checks the boxes of all child files in the dataset.
* **optional:** click the triangle on the left to review the detailed contents of the sub-directory.

| ![](https://outerspace.stsci.edu/download/thumbnails/153686810/DLM_file_selector_detail.png?version=1&modificationDate=1683571071066&api=v2)
**6
** |  **Optional:** After selecting exposures of interest, click the **Retrieve References** button to bring up a dialog where you can choose one or more of all the [calibration reference files](https://outerspace.stsci.edu/display/MASTDOCS/Calibration+Reference+Files) that were used by the CAL pipeline to produce the selected data products. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_retrieve-refs.png?version=1&modificationDate=1683571071043&api=v2)
**7** | Click the **Download** button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_download.png?version=1&modificationDate=1683571071034&api=v2)
**8** |  Select the format for the download package from the pull-down, then click the **Download** but **Optional:** Check the "Remove completed files from basket" box. This will purge download basket, which may help avoid confusion the next time you prepare to download files using the basket. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_download-fmt.png?version=1&modificationDate=1683571071026&api=v2)
### Download via cURL Script
This type of retrieval is asynchronous and has no limits to the volume of data to download. It is more robust against internet interruptions, and can be resumed if interrupted.
Download cURL retrieval script...

| Instruction | Notes
---|---|---
**1** | Follow instructions 1–7 for Streaming Download (above). |

**2** | Select __Curl__ from the file **Format** pull-down menu. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/dialog_download_curl.png?version=1&modificationDate=1683571071001&api=v2)
**3** |  Save the cURL shell script in a directory where you wish the data files to be stored. Whether a dialog appears, and the specific wording in the dialog, depend upon browser settings. The location where the files will be written also depends upon your browser settings. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_fileSave_curl.png?version=1&modificationDate=1683571070993&api=v2)
**4** |  Bring up a shell and execute the downloaded script. **Note:** If you are retrieving Exclusive Access Protected data, you will need to either provide your MyST login credentials, or have set an environment varialbe with your [Auth.MAST token](https://auth.mast.stsci.edu/info), in order for the shell to complete the retrieval successfully. The cURL script is targeted to a **bash** shell. Specifying **bash** on the command line allows it to be invoked from any unix shell. |  ```
bash MAST_2018-10-31T2028.sh
```  
MAST Auth Tokens
Authentication for access to EAP data via a cURL or other scripts is managed in MAST via tokens. See [MAST API Tokens](https://auth.mast.stsci.edu/info) to learn how to create or update a MAST.auth token.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Getting Started with MAST", "Header 2": "Direct Download", "Header 3": "Batch Download"} -->
Staging files for **ftps** retrieval is currently supported for a few MAST missions (including JWST and HST), but not all. It is highly recommended to instead retrieve large numbers of files via cURL scripts.
Staging for FTPS Retrieval...  
| Instruction | Notes
---|---|---
**1** | Follow instructions 1–6 for Immediate Download (above). |  
**2** | Click the **Batch Retrieval** button. | ![](https://outerspace.stsci.edu/download/thumbnails/153686810/button_batch-retrieval.png?version=1&modificationDate=1683571070977&api=v2)
**3** |  Select __staging__ from the file **Delivery Method** pull-down menu and (if you are not logged in) provide the email address where you wish the notification to be sent. **Note:** If you are logged in to MAST, the e-mail address on record will be pre-filled. | ![](https://outerspace.stsci.edu/download/attachments/153686810/dialog_staging.png?version=1&modificationDate=1683571070959&api=v2)
**4** | Acknowledge the email pop-up notification, and check your email at the delivery address you specified.  
| ![](https://outerspace.stsci.edu/download/thumbnails/153686810/popUp_email.png?version=1&modificationDate=1683571070936&api=v2)
**5
** | The email notification will give the location of the files that have been staged. |
**6
** | Use a third-party client such as Cyberduck or  |
* * *

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "API Tutorial"} -->
The following tutorial introduces the basics of MAST queries with the [JWST Archive Manual](https://outerspace.stsci.edu/display/MASTDOCS/JWST+Archive+Manual) in the [Using MAST APIs](https://outerspace.stsci.edu/display/MASTDOCS/Using+MAST+APIs) chapter.
API Example...
The set of all available parameters for this type of query is summarized [here](https://mast.stsci.edu/api/v0/_c_a_o_mfields.html). Consider a search for JWST/NIRCam observations in observing program 1073, using the F277W filter. Use the **`.query_criteria()`**method.
```
matched_obs = Observations.query_criteria(
obs_collection = 'JWST'
, proposal_id = '1073'
, instrument_name = 'Nircam'
, filters = 'F277W'
)
```  
The result is an **astropy** `Table` object, with one row per matched observation.
If for a particular query you are not interested in observations from any mission except JWST, specify it with the parameter `obs_collection='JWST'`. This will narrow the list of possible matches considerably, and speed up your query.
Having found Observations that match your criteria, the next step is to fetch a table of data products associated with each Observation.
Some observations contain huge numbers of associated or linked files, sometimes in excess of 10,000 products. This is particularly true for NIRSpec MSA, or MIRI and NIRCam slitless spectroscopy, but may also be true for large mosaics of images. Each observation is likely to contain many files in common, such as guide-star files and ancillary products.
**It is strongly recommended to retrieve product lists one or a few at a time from each observation to avoid server timeouts, and then to construct a set of unique products from the combined observations to avoid large numbers of duplicated products.**
The following retrieves a list of tables of data products for each observation, and returns combined table containing unique data products.
```
if (matched_obs > 0):
t = [Observations.get_product_list(obs) for obs in matched_obs]
files = unique(vstack(t), keys='productFilename')
```  
If at least one observation matched the search criteria the above call returns a table of unique products, one per row, which could number in the hundreds or thousands. You may wish to filter the results by masking all but a limited number of file suffixes and excluding certain sub-strings.
The selected products may now be downloaded to your local machine. Note that you will need to login with a valid [Auth.MAST](https://auth.mast.stsci.edu/info) token to download exclusive access (EAP) data. If the token is needed but not supplied, the you will be prompted to enter one.
You may download all the products in the files table, or select a subset if you prefer. The following will select L-1b products (i.e. the raw, uncalibrated, `*_uncal.fits`) from the data product list for retrieval. Other types of products may instead be selected, either by matching product name sub-strings or selecting named products in the `productSubGroupDescription`.
```
manifest = Observations.download_products(
files,
productSubGroupDescription='UNCAL',
curl_flag=True
)
```  
Setting the optional `curl_flag` parameter to **`True`**will instead download a**bash** script that contains **cURL** commands to fetch the files at a later time. This approach is highly recommended for large numbers of files. The name of the download script will be something like: mastDownload_**YYYYMMDDhhmmss**.sh, where the latter part of the name is a numeric timestamp. What remains is to invoke the downloaded script on your machine to retrieve the files.
* * *

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "What's in the Box"} -->
All data products for all selected observations will be bundled together for delivery. When the Zip or tar file is unpacked, data for each observation/visit/exposure will appear in a separate sub-directory.
For each sub-directory, the data bundle includes by default the highest-level data products, _plus all parent data_. For example, if an observation/visit/exposure combination resulted in Level-2 data products, all Level-1 products would automatically be included unless the user explicitly chooses otherwise.
The Download Manifest
The zip (or tar) file will include a file called **`MANIFEST.HTML`**which lists each file name, a short description, and whether access is restricted. It will also note any files that could not be downloaded and the reason why (e.g., if you do not have permission to retrieve them).

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "What's in the Box", "Header 2": "File Names and Content"} -->
The semantic content of science files may be inferred from the file suffix, and the filename signature. For example, files ending in _**`_uncal.fits`**_are Level-1b uncalibrated science products. See the JWST**.
**
* * *

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "For Further Reading...", "Header 2": "Reference Documents"} -->
* MAST [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual)
* [JWST User Documentation Home](https://jwst-docs.stsci.edu/) (JDox)

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "For Further Reading...", "Header 2": "User Support"} -->
* **Archive Help Desk:**
* **JWST**  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

