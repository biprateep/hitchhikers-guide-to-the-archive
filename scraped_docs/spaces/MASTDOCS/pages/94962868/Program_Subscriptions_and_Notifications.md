---
title: "Creating Subscriptions"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962868/Program+Subscriptions+and+Notifications"
date_accessed: "2026-03-11T16:32:05.938448"
content_length: 11440
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

<!-- CHUNK 6 END -->

