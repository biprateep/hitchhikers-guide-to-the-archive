---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide"
date_accessed: "2026-03-11T11:34:26.718466"
---

<!-- CHUNK 1 START -->
High Level Science Products are [user-contributed](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide) observations, catalogs, or models that complement, or are derived from, MAST-supported missions. This page describes the [HLSP Search](https://mast.stsci.edu/hlsp/#/) form, which is one way to find HLSP product collections.
**On this page...**
* 1[The search form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Thesearchform)
* 1.1[Text-based search fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Text-basedsearchfields)
* 1.2[Tag-based search fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Tag-basedsearchfields)
* 1.3[The search bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Thesearchbar)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-ForFurtherReading...)  
The [HLSP Search](https://mast.stsci.edu/hlsp/#/) form described on this page is not the only way to discover HLSP collections. Many collections have had some or all of their data ingested into our multi-mission database, which is accessible from the [Multi-mission Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) and

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "The search form"} -->
![Screenshot of the search form. The top row of components \(HLSP name and abstracts\) is labeled #1, the middle row of components \(object type, mission, product type, waveband\) #2, and the search bar #3.](https://outerspace.stsci.edu/download/attachments/218367490/form.png?version=1&modificationDate=1699284170097&api=v2)
The HLSP Search form includes text-based search fields (within the box labelled __1__) and tag-based search fields (__2__) which create filters to match against HLSP collection metadata. Buttons in the search bar (__3__) can reset the form or apply your search criteria.
Boolean logic
There is a Boolean `AND` _between_ individual search fields of any type. For example, if you search for `"``HLSP Name Contains=TASOC` and `Abstract Text Contains=cats"`, you will get no results, because no HLSP meets both criteria. Different Boolean logic applies  _within_ individual search fields, depending on the type: Boolean `AND` within a text-based field, Boolean `OR` within a tag-based field, as discussed below.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "The search form", "Header 2": "Text-based search fields"} -->
The **HLSP Name** and **Abstract Text** fields perform string-matching to HLSP names and abstracts, respectively. Within a single field, an HLSP must be a match for  _all_ space-separated strings that you enter (Boolean `AND`), but these strings do not need to match whole words or be in any particular order.
![](https://outerspace.stsci.edu/download/thumbnails/218367490/dialog_HlspAbstract.png?version=1&modificationDate=1699884715216&api=v2)  
For example, when matching against **Abstract Text** :
`light curve`
matches abstracts that contain either "light curve" or "lightcurve", and will not match abstracts that are missing the string "curve" even if they contain "light".  
`lightcurve`
without a space only matches abstracts that contain "lightcurve" without a space.
`curv ligh`
would match abstracts that contain either "light curve" or "lightcurve". This query is for demonstration purposes only!  
![](https://outerspace.stsci.edu/download/thumbnails/218367490/dialog_HlspName.png?version=1&modificationDate=1699884067638&api=v2)
Matching against **HLSP** **Name** works the same way. In addition, matches to the abbreviated, parenthetical short name are ranked first in the results list, before matches to the long-form titles. For example,
`COSMOS`
will rank [A Wide‑Field WFC3 Imaging Survey in the COSMOS Field (COSMOS‑DASH)](https://archive.stsci.edu/hlsp/cosmos-dash) above [A Wide‑Field WFC3 Imaging Survey with Grism Spectroscopy in the COSMOS Field (3D‑DASH)](https://archive.stsci.edu/hlsp/3d-dash/).
* * *

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "The search form", "Header 2": "Tag-based search fields"} -->
The **Object Type** , **Mission** , **Product Type** , and **Waveband** fields will filter on tags that have been attached to HLSPs. Within a single field, an HLSP project that is a match for _any_ of the selected tags will be included in the results (Boolean `OR`).
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_objTypes.png?version=1&modificationDate=1699890549552&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_missions.png?version=1&modificationDate=1699890549231&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_prodTypes.png?version=1&modificationDate=1699890549799&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_waveband.png?version=1&modificationDate=1699890550002&api=v2)
For example, when matching the **Mission** :
`Kepler,K2,TESS`
yields all HLSPs that are based on any of these missions, including HLSPs that are only based on TESS.  
When matching multiple fields:
**Mission** = `Kepler,K2,TESS`
and **Waveband** = `Radio`
yields no results because there is a Boolean `AND` between fields, and HLSPs based on Kepler/K2/TESS tend not to involve radio data.  
For now, the product type and object type vocabularies have not been significantly updated in the move from the previous iteration of this form, and they contain some information gaps that may affect your search. Improved tagging vocabularies will be implemented in future versions of this form.
* * *

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "The search form", "Header 2": "The search bar"} -->
Any filters you add will not be executed until you either click **Filter Results** or hit enter within a text-based search field. To clear all filters, click **Clear Filters** , which will also re-execute the search. A count of the number of results from your search is displayed below the Filter Results button. This number will not change until you execute a search.
* * *

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)  
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
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide "HLSP Search Guide")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide "HLSP Search Guide")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
* [Contribution Request Form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290416/Contribution+Request+Form "Contribution Request Form")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
High Level Science Products are [user-contributed](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide) observations, catalogs, or models that complement, or are derived from, MAST-supported missions. This page describes the [HLSP Search](https://mast.stsci.edu/hlsp/#/) form, which is one way to find HLSP product collections.
**On this page...**
* 1[The search form](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Thesearchform)
* 1.1[Text-based search fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Text-basedsearchfields)
* 1.2[Tag-based search fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Tag-basedsearchfields)
* 1.3[The search bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-Thesearchbar)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/218367490/HLSP+Search+Guide#HLSPSearchGuide-ForFurtherReading...)  
The [HLSP Search](https://mast.stsci.edu/hlsp/#/) form described on this page is not the only way to discover HLSP collections. Many collections have had some or all of their data ingested into our multi-mission database, which is accessible from the [Multi-mission Portal](https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html) and

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "The search form"} -->
![Screenshot of the search form. The top row of components \(HLSP name and abstracts\) is labeled #1, the middle row of components \(object type, mission, product type, waveband\) #2, and the search bar #3.](https://outerspace.stsci.edu/download/attachments/218367490/form.png?version=1&modificationDate=1699284170097&api=v2)
The HLSP Search form includes text-based search fields (within the box labelled __1__) and tag-based search fields (__2__) which create filters to match against HLSP collection metadata. Buttons in the search bar (__3__) can reset the form or apply your search criteria.
Boolean logic
There is a Boolean `AND` _between_ individual search fields of any type. For example, if you search for `"``HLSP Name Contains=TASOC` and `Abstract Text Contains=cats"`, you will get no results, because no HLSP meets both criteria. Different Boolean logic applies  _within_ individual search fields, depending on the type: Boolean `AND` within a text-based field, Boolean `OR` within a tag-based field, as discussed below.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "The search form", "Header 2": "Text-based search fields"} -->
The **HLSP Name** and **Abstract Text** fields perform string-matching to HLSP names and abstracts, respectively. Within a single field, an HLSP must be a match for  _all_ space-separated strings that you enter (Boolean `AND`), but these strings do not need to match whole words or be in any particular order.
![](https://outerspace.stsci.edu/download/thumbnails/218367490/dialog_HlspAbstract.png?version=1&modificationDate=1699884715216&api=v2)  
For example, when matching against **Abstract Text** :
`light curve`
matches abstracts that contain either "light curve" or "lightcurve", and will not match abstracts that are missing the string "curve" even if they contain "light".  
`lightcurve`
without a space only matches abstracts that contain "lightcurve" without a space.
`curv ligh`
would match abstracts that contain either "light curve" or "lightcurve". This query is for demonstration purposes only!  
![](https://outerspace.stsci.edu/download/thumbnails/218367490/dialog_HlspName.png?version=1&modificationDate=1699884067638&api=v2)
Matching against **HLSP** **Name** works the same way. In addition, matches to the abbreviated, parenthetical short name are ranked first in the results list, before matches to the long-form titles. For example,
`COSMOS`
will rank [A Wide‑Field WFC3 Imaging Survey in the COSMOS Field (COSMOS‑DASH)](https://archive.stsci.edu/hlsp/cosmos-dash) above [A Wide‑Field WFC3 Imaging Survey with Grism Spectroscopy in the COSMOS Field (3D‑DASH)](https://archive.stsci.edu/hlsp/3d-dash/).
* * *

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "The search form", "Header 2": "Tag-based search fields"} -->
The **Object Type** , **Mission** , **Product Type** , and **Waveband** fields will filter on tags that have been attached to HLSPs. Within a single field, an HLSP project that is a match for _any_ of the selected tags will be included in the results (Boolean `OR`).
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_objTypes.png?version=1&modificationDate=1699890549552&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_missions.png?version=1&modificationDate=1699890549231&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_prodTypes.png?version=1&modificationDate=1699890549799&api=v2)
![](https://outerspace.stsci.edu/download/thumbnails/218367490/menu_waveband.png?version=1&modificationDate=1699890550002&api=v2)
For example, when matching the **Mission** :
`Kepler,K2,TESS`
yields all HLSPs that are based on any of these missions, including HLSPs that are only based on TESS.  
When matching multiple fields:
**Mission** = `Kepler,K2,TESS`
and **Waveband** = `Radio`
yields no results because there is a Boolean `AND` between fields, and HLSPs based on Kepler/K2/TESS tend not to involve radio data.  
For now, the product type and object type vocabularies have not been significantly updated in the move from the previous iteration of this form, and they contain some information gaps that may affect your search. Improved tagging vocabularies will be implemented in future versions of this form.
* * *

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "The search form", "Header 2": "The search bar"} -->
Any filters you add will not be executed until you either click **Filter Results** or hit enter within a text-based search field. To clear all filters, click **Clear Filters** , which will also re-execute the search. A count of the number of results from your search is displayed below the Filter Results button. This number will not change until you execute a search.
* * *

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide)
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide)
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

