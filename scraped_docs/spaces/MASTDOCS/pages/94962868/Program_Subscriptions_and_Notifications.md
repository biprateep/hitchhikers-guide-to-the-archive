---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications"
date_accessed: "2026-03-11T11:32:00.495119"
---

<!-- CHUNK 1 START -->
You may elect to be notified automatically when data from an HST or JWST observing program are first archived, are updated, or become publicly available.
**On this page...**
* 1[Creating Subscriptions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-subscriptionsCreatingSubscriptions)
* 1.1[Subscriptions Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-SubscriptionsManager)
* 1.2[Portal Actions Menu](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-PortalActionsMenu)
* 2[Updating Subscriptions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-UpdateSubscriptionsUpdatingSubscriptions)
* 3[Receiving Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-ReceivingNotifications)
* 3.1[Email Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-EmailNotifications)
* 3.2[Portal Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-PortalNotifications)  
Setting up notifications requires logging in to the Portal, setting up a subscription, and specifying how you prefer to receive notifications. There are two ways to create subscriptions: through the _**subscriptions manager**_ , and through the _**actions**_ menu for individual observations in the Portal results table. The methods are described below.
Subscriptions can only be created for HST and JWST observations.
Notifications are generated when certain events are triggered on data to which you are subscribed. These events map to the __subscription type__ , which is one of:
* **New:** Triggers whenever any data for a program appear in MAST for the first time
* **First:** Triggers when the first data for a program appear in MAST (JWST only)
* **Reprocessed:** Triggers when existing program data in MAST have been reprocessed by the pipeline as a result of improved calibration software or reference files
* **Public:** Triggers when data for program transition to "public" access from "exclusive access" protection (EAP)  
Subscriptions may be created for any program, even before data appear in MAST.

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 2": "Subscriptions Manager"} -->
If you wish to be notified about processing events that relate to an observing program, even before any observations have been executed, use the subscriptions manager as described below.  
| Instruction | Notes
---|---|---
**1** | Login to the Portal. Then click __Subscriptions…__ in the login panel located on the upper-right. | ![Portal log-in dialog](https://outerspace.stsci.edu/download/thumbnails/94962868/portal_login.png?version=1&modificationDate=1671558965172&api=v2)
|  The subscription manager will appear, which will look similar to the image below. ![Portal subscription manager](https://outerspace.stsci.edu/download/attachments/94962868/panel_subscrip_manager.png?version=1&modificationDate=1675972326292&api=v2)
**2** | Click the **Add** button at the upper-right of the Subscriptions manager. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_add_subscription.png?version=1&modificationDate=1657201924862&api=v2)
**3** |  Create subscriptions to one or more programs with the pop-up menu, specifying:
* **Notification Type** (__Email__ or Portal)
* **Notification Frequency** (Fast, __Daily__ , Weekly, Monthly)
* **Mission** (__HST__ or JWST)
* **Subscription Type** (__all__ ; see above)
* **Proposal ID**
* **Observation ID**
* **Optional** (JWST only: 2 or __3__. Specify the [data product level](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) of calibration processing. Higher levels translate to more highly calibrated and combined data products.)  
Multiple delivery methods You can specify the method of notifications as both the portal _and_ via email by creating separate subscriptions, one with each type. | ![The Portal subscription creation menu](https://outerspace.stsci.edu/download/attachments/94962868/create_subscription.png?version=1&modificationDate=1671558775697&api=v2)
**4** | Click the **plus** icon to create additional subscriptions. When finished, click the **Save** button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_plus_green.png?version=1&modificationDate=1657201924700&api=v2)![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_save.png?version=1&modificationDate=1657201924736&api=v2)
**5** | After establishing one or more subscriptions, you can modify the attributes by clicking the appropriate icon (edit, pause, delete). Pausing an individual subscription leaves the subscription in place, but turns off notifications. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subsccriptionActions.png?version=1&modificationDate=1657201924853&api=v2)  
Context help
Context help for subscriptions is available with the **Help** button ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subscriptionHelp.png?version=1&modificationDate=1657201924838&api=v2) in the subscriptions window.
Caveats
No validity check is performed on new subscriptions. Thus it is possible to subscribe to, e.g., a non-existent proposal or observation number. Naturally, you will receive no notifications from that subscription.
Selecting "Fast" notification frequency for a "Reprocessed" subscription type may result in very many notifications as program data are generated by the calibration pipeline. It my be preferable in this case to select a "Daily" notification.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 2": "Portal Actions Menu"} -->
If you wish to be notified of events related to individual observations after the data have appeared in MAST, you may subscribe via the Actions menu in the Portal results panel, as described below.  
| Instruction | Notes
---|---|---
**1** |  Login to the Portal, and perform a search for Observations of interest.  It is not possible to subscribe to data from the results of a JWST Instrument Keywords search. | ![Portal log-in dialog](https://outerspace.stsci.edu/download/thumbnails/94962868/portal_login.png?version=1&modificationDate=1671558965172&api=v2)
**2** | After a Portal search, choose a row in the results table on which you would like to establish a subscription. Click the **More Actions** icon ![](https://outerspace.stsci.edu/download/thumbnails/94962868/icon_dots.png?version=1&modificationDate=1657201924668&api=v2) on the **Actions** pull-down menu, and select __Create a Subscription__. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/menu_actions.png?version=1&modificationDate=1657201924759&api=v2)
**3** | Follow the instructions above, located under [Subscriptions Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-subscriptions). |  
You may modify the parameters of existing subscriptions, suspend notifications, or delete them altogether using the Subscriptions Manager window.  
| Instruction | Notes
---|---|---
**1** | Login to the Portal, and bring up the subscriptions manager (see step 1 in the Subscriptions Manager instructions above). |  
**2** | Select one or more rows, then click the **Edit** icon to bring up the editor menu. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subscrip_edit.png?version=1&modificationDate=1675975080714&api=v2)
**3** |  Check the boxes of the attributes you wish to edit, and select the changes with the pull-down menu(s). In this case, change the frequency of the selected subscriptions to __Daily__. Then click the **Save** button. | ![Portal subscriptions editor](https://outerspace.stsci.edu/download/attachments/94962868/menu_subscrip_editor.png?version=1&modificationDate=1675974436736&api=v2)
**4** | Click __OK__ in the pop-up confirmation dialog. | ![Pop-up message to confirm edit\(s\) to subscription\(s\)](https://outerspace.stsci.edu/download/attachments/94962868/popup_subscr_editconfirm.png?version=1&modificationDate=1675974520298&api=v2)
You can delete a subscription entirely by clicking the trash can ![](https://outerspace.stsci.edu/download/thumbnails/94962868/icon_trash.png?version=1&modificationDate=1657201924696&api=v2) in any row, or select multiple rows and click the trashcan button.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications"} -->
Notifications are batched into time intervals corresponding to the requested notification frequency. Multiple events of a given type (say, for reprocessing) will be combined prior sending a notification. "Fast" notifications are generated with a frequency of several minutes.
Notifications occur for calibrated products
Notifications will only be generated for calibrated products. If pipeline processing terminates after generating only raw or intermediate-level products, no notification will be generated.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications", "Header 2": "Email Notifications"} -->
| Instruction | Notes
---|---|---
1 | If the Notification Type was set to __Email__ , users should receive an email from "Space Telescope Science Institute <noreply@stsci.edu>" when the designated milestone is reached. | ![Example email with a MAST notification](https://outerspace.stsci.edu/download/attachments/94962868/subscription_email.png?version=1&modificationDate=1660583276976&api=v2)
2 |  The email will provide one or more links:
* Other links wil be present, one per progam. should Clicking one will open a browser tab with the MAST Portal, showing results for the subscribed program.  
|

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications", "Header 2": "Portal Notifications"} -->
| Instruction | Notes
---|---|---
1 | If the Notification Type was set to __Portal__ , users who are logged into the MAST Portal should see a notification (a bell icon with a number next to it) in the user login panel at the upper right. | ![Portal log-in dialog, with an indicator of an unread notification](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subscriptions.png?version=1&modificationDate=1657201924829&api=v2)
2 | Clicking the bell icon in the login panel, will open a tab with all your Portal notifications. | ![Portal notifications manager](https://outerspace.stsci.edu/download/attachments/94962868/grid_notification.png?version=1&modificationDate=1657201924825&api=v2)
3 |  Selecting a notification will open a pop-up window with a link to query the MAST Portal for data from the subscribed program. Notification Details A single notification may contain information for multiple observations in the same program, depending on the user's subscriptions. | ![Portal notification message, with link to the data](https://outerspace.stsci.edu/download/thumbnails/94962868/popup_notification.png?version=1&modificationDate=1657201924821&api=v2)
4 | (Optional) You may delete individual or all selected notifications by clicking the trash icon. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/icon_trash.png?version=1&modificationDate=1657201924696&api=v2)
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
You may elect to be notified automatically when data from an HST or JWST observing program are first archived, are updated, or become publicly available.
**On this page...**
* 1[Creating Subscriptions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-subscriptionsCreatingSubscriptions)
* 1.1[Subscriptions Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-SubscriptionsManager)
* 1.2[Portal Actions Menu](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-PortalActionsMenu)
* 2[Updating Subscriptions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-UpdateSubscriptionsUpdatingSubscriptions)
* 3[Receiving Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-ReceivingNotifications)
* 3.1[Email Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-EmailNotifications)
* 3.2[Portal Notifications](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-PortalNotifications)  
Setting up notifications requires logging in to the Portal, setting up a subscription, and specifying how you prefer to receive notifications. There are two ways to create subscriptions: through the _**subscriptions manager**_ , and through the _**actions**_ menu for individual observations in the Portal results table. The methods are described below.
Subscriptions can only be created for HST and JWST observations.
Notifications are generated when certain events are triggered on data to which you are subscribed. These events map to the __subscription type__ , which is one of:
* **New:** Triggers whenever any data for a program appear in MAST for the first time
* **First:** Triggers when the first data for a program appear in MAST (JWST only)
* **Reprocessed:** Triggers when existing program data in MAST have been reprocessed by the pipeline as a result of improved calibration software or reference files
* **Public:** Triggers when data for program transition to "public" access from "exclusive access" protection (EAP)  
Subscriptions may be created for any program, even before data appear in MAST.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications", "Header 2": "Subscriptions Manager"} -->
If you wish to be notified about processing events that relate to an observing program, even before any observations have been executed, use the subscriptions manager as described below.  
| Instruction | Notes
---|---|---
**1** | Login to the Portal. Then click __Subscriptions…__ in the login panel located on the upper-right. | ![Portal log-in dialog](https://outerspace.stsci.edu/download/thumbnails/94962868/portal_login.png?version=1&modificationDate=1671558965172&api=v2)
|  The subscription manager will appear, which will look similar to the image below. ![Portal subscription manager](https://outerspace.stsci.edu/download/attachments/94962868/panel_subscrip_manager.png?version=1&modificationDate=1675972326292&api=v2)
**2** | Click the **Add** button at the upper-right of the Subscriptions manager. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_add_subscription.png?version=1&modificationDate=1657201924862&api=v2)
**3** |  Create subscriptions to one or more programs with the pop-up menu, specifying:
* **Notification Type** (__Email__ or Portal)
* **Notification Frequency** (Fast, __Daily__ , Weekly, Monthly)
* **Mission** (__HST__ or JWST)
* **Subscription Type** (__all__ ; see above)
* **Proposal ID**
* **Observation ID**
* **Optional** (JWST only: 2 or __3__. Specify the [data product level](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771322/Science+Data+Products) of calibration processing. Higher levels translate to more highly calibrated and combined data products.)  
Multiple delivery methods You can specify the method of notifications as both the portal _and_ via email by creating separate subscriptions, one with each type. | ![The Portal subscription creation menu](https://outerspace.stsci.edu/download/attachments/94962868/create_subscription.png?version=1&modificationDate=1671558775697&api=v2)
**4** | Click the **plus** icon to create additional subscriptions. When finished, click the **Save** button. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_plus_green.png?version=1&modificationDate=1657201924700&api=v2)![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_save.png?version=1&modificationDate=1657201924736&api=v2)
**5** | After establishing one or more subscriptions, you can modify the attributes by clicking the appropriate icon (edit, pause, delete). Pausing an individual subscription leaves the subscription in place, but turns off notifications. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subsccriptionActions.png?version=1&modificationDate=1657201924853&api=v2)  
Context help
Context help for subscriptions is available with the **Help** button ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subscriptionHelp.png?version=1&modificationDate=1657201924838&api=v2) in the subscriptions window.
Caveats
No validity check is performed on new subscriptions. Thus it is possible to subscribe to, e.g., a non-existent proposal or observation number. Naturally, you will receive no notifications from that subscription.
Selecting "Fast" notification frequency for a "Reprocessed" subscription type may result in very many notifications as program data are generated by the calibration pipeline. It my be preferable in this case to select a "Daily" notification.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications", "Header 2": "Portal Actions Menu"} -->
If you wish to be notified of events related to individual observations after the data have appeared in MAST, you may subscribe via the Actions menu in the Portal results panel, as described below.  
| Instruction | Notes
---|---|---
**1** |  Login to the Portal, and perform a search for Observations of interest.  It is not possible to subscribe to data from the results of a JWST Instrument Keywords search. | ![Portal log-in dialog](https://outerspace.stsci.edu/download/thumbnails/94962868/portal_login.png?version=1&modificationDate=1671558965172&api=v2)
**2** | After a Portal search, choose a row in the results table on which you would like to establish a subscription. Click the **More Actions** icon ![](https://outerspace.stsci.edu/download/thumbnails/94962868/icon_dots.png?version=1&modificationDate=1657201924668&api=v2) on the **Actions** pull-down menu, and select __Create a Subscription__. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/menu_actions.png?version=1&modificationDate=1657201924759&api=v2)
**3** | Follow the instructions above, located under [Subscriptions Manager](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications#ProgramSubscriptionsandNotifications-subscriptions). |  
You may modify the parameters of existing subscriptions, suspend notifications, or delete them altogether using the Subscriptions Manager window.  
| Instruction | Notes
---|---|---
**1** | Login to the Portal, and bring up the subscriptions manager (see step 1 in the Subscriptions Manager instructions above). |  
**2** | Select one or more rows, then click the **Edit** icon to bring up the editor menu. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subscrip_edit.png?version=1&modificationDate=1675975080714&api=v2)
**3** |  Check the boxes of the attributes you wish to edit, and select the changes with the pull-down menu(s). In this case, change the frequency of the selected subscriptions to __Daily__. Then click the **Save** button. | ![Portal subscriptions editor](https://outerspace.stsci.edu/download/attachments/94962868/menu_subscrip_editor.png?version=1&modificationDate=1675974436736&api=v2)
**4** | Click __OK__ in the pop-up confirmation dialog. | ![Pop-up message to confirm edit\(s\) to subscription\(s\)](https://outerspace.stsci.edu/download/attachments/94962868/popup_subscr_editconfirm.png?version=1&modificationDate=1675974520298&api=v2)
You can delete a subscription entirely by clicking the trash can ![](https://outerspace.stsci.edu/download/thumbnails/94962868/icon_trash.png?version=1&modificationDate=1657201924696&api=v2) in any row, or select multiple rows and click the trashcan button.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications"} -->
Notifications are batched into time intervals corresponding to the requested notification frequency. Multiple events of a given type (say, for reprocessing) will be combined prior sending a notification. "Fast" notifications are generated with a frequency of several minutes.
Notifications occur for calibrated products
Notifications will only be generated for calibrated products. If pipeline processing terminates after generating only raw or intermediate-level products, no notification will be generated.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications", "Header 2": "Email Notifications"} -->
| Instruction | Notes
---|---|---
1 | If the Notification Type was set to __Email__ , users should receive an email from "Space Telescope Science Institute <noreply@stsci.edu>" when the designated milestone is reached. | ![Example email with a MAST notification](https://outerspace.stsci.edu/download/attachments/94962868/subscription_email.png?version=1&modificationDate=1660583276976&api=v2)
2 |  The email will provide one or more links:
* Other links wil be present, one per progam. should Clicking one will open a browser tab with the MAST Portal, showing results for the subscribed program.  
|

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Receiving Notifications", "Header 2": "Portal Notifications"} -->
| Instruction | Notes
---|---|---
1 | If the Notification Type was set to __Portal__ , users who are logged into the MAST Portal should see a notification (a bell icon with a number next to it) in the user login panel at the upper right. | ![Portal log-in dialog, with an indicator of an unread notification](https://outerspace.stsci.edu/download/thumbnails/94962868/button_subscriptions.png?version=1&modificationDate=1657201924829&api=v2)
2 | Clicking the bell icon in the login panel, will open a tab with all your Portal notifications. | ![Portal notifications manager](https://outerspace.stsci.edu/download/attachments/94962868/grid_notification.png?version=1&modificationDate=1657201924825&api=v2)
3 |  Selecting a notification will open a pop-up window with a link to query the MAST Portal for data from the subscribed program. Notification Details A single notification may contain information for multiple observations in the same program, depending on the user's subscriptions. | ![Portal notification message, with link to the data](https://outerspace.stsci.edu/download/thumbnails/94962868/popup_notification.png?version=1&modificationDate=1657201924821&api=v2)
4 | (Optional) You may delete individual or all selected notifications by clicking the trash icon. | ![](https://outerspace.stsci.edu/download/thumbnails/94962868/icon_trash.png?version=1&modificationDate=1657201924696&api=v2)
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

