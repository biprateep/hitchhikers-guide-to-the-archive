---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components"
date_accessed: "2026-03-11T11:37:05.462463"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[HST-Specific Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-HST-SpecificSearchComponents)
* 1.1[Dataset ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-DatasetID)
* 1.2[Data Types](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-DataTypes)
* 1.3[ Instrument Selector](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-InstrumentSelector)
* 1.4[Observation Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-ObservationType)
* 2[Filtering for Enhanced Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-FilteringforEnhancedData)
* 2.1[HASP](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-HASP)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components"} -->
This page describes elements of the search form which are either unique to JWST, or are shared with other missions but contain options that are best explained on a per-mission basis.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Dataset ID"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/string-condition-example-1.png?version=1&modificationDate=1664284570162&api=v2)
The **'****Dataset ID'** is a unique dataset name. For HST, it is 9-characters long, e.g., J8BA7JCAQ or O4140Q020, where the first character indicates the instrument used: L=COS; I=WFC3; J=ACS; N=NICMOS; O=STIS; U=WFPC2; W=WFPC; X=FOC; Y=FOS; Z=GHRS; F=FGS; V=HSP.
This component is a [String field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview), so 'Exact Match', 'Wildcard', 'Exclude', and search by 'Multiple' entries are allowed. If known, type the exact dataset ID into this field's box. If the exact dataset ID is not known, conduct a wildcard search or type a string to enable a type-ahead menu. It will show a list of dataset IDs that contain that text. Browse through the suggested list to find the right one by scrolling the mouse or use the scroll bar on the right of the menu, and then click to select.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Data Types"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/data-type.png?version=1&modificationDate=1664284572632&api=v2)  
By default, the **'Data Type'** is set to 'ALL'. Check the check box for a preferred data type: 'SPECTRUM' or 'IMAGE'.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Instrument Selector"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/instrument-selector.png?version=1&modificationDate=1664284572608&api=v2)
This video clip demonstrates how to select different instruments to include in searches.
Some data collections contain datasets from a wide range of instruments, for example, the various [HST instruments](https://archive.stsci.edu/missions-and-data/hst#section-a998adf3-358a-4e01-828d-a3535b29fffd). Mission Search can include results from across all available instruments or a subset of them. By default, all available instruments are selected. Hovering the mouse over each instrument will show the full name of the instrument.
Depending on the **'Data Types'** selection, such as 'SPECTRUM' only or 'IMAGE' only, the list of available instruments will also change (an instrument that only takes images will not be shown if only 'SPECTRUM' data types are selected, for example). To select a single instrument, click the 'none' (![](https://outerspace.stsci.edu/download/thumbnails/102535413/hst-output-none.png?version=1&modificationDate=1628808842546&api=v2)) button and then select the desired instrument to include.
Some instruments produce neither images nor spectra: the Fine Guidance Sensors (FGS, which produce astrometric, usually interferometric, data) and the High Speed Photometer (HSP, which produced photometric data). These instruments will only appear if 'ALL' is selected in the Data Types area.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Observation Type"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/obs-type.png?version=1&modificationDate=1664284572655&api=v2)
The **'Observations'** selector can choose 'SCIENCE' and/or 'CALIBRATION'. The default setting is to search only 'SCIENCE'.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Filtering for Enhanced Data"} -->
While searching for HST Observations, you may find products from additional processing pipelines.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Filtering for Enhanced Data", "Header 2": "HASP"} -->
The [HASP (Hubble Advanced Spectral Products)](https://archive.stsci.edu/missions-and-data/hst/hasp) are a collection of co-added spectra for nearly all HST Observations. These are only generated for observations that used COS or STIS.
![an additional condition for selecting HASP data, with the include value \('1'\) filled in](https://outerspace.stsci.edu/download/attachments/127765652/HASP-filter.png?version=1&modificationDate=1706222733676&api=v2)
After [selecting an additional condition](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters), you can add a filter to include (1) or exclude (0) data from the HASP pipeline. By default, (i.e., with no value in the condition box), the HASP column will merely be included in the results table, with no selection by the value of this field.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)
* [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [Cone Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search "Cone Search And Upload List Search")
* [Target Name Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search "Target Name Search And Upload List Search")
* [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview "Search Parameter Overview")
* [Core Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters "Core Search Parameters")
* [CLASSY Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131862458/CLASSY+Search+Components "CLASSY Search Components")
* [HST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components "HST Search Components")
* [JWST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350629/JWST+Search+Components "JWST Search Components")
* [ULLYSES Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158174811/ULLYSES+Search+Components "ULLYSES Search Components")
* [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters "Additional Search Parameters")
* [Choose Output Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958266/Choose+Output+Columns "Choose Output Columns")
* [The Search Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958267/The+Search+Bar "The Search Bar")
* [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page "Search Results Page")
* [Image Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/352354485/Image+Previews "Image Previews")
* [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay "Download Overlay")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Mission Search Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958260/Mission+Search+Guide "Mission Search Guide")
* [Search Form Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958261/Search+Form+Overview "Search Form Overview")
* [Mission Search Caveats](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350249/Mission+Search+Caveats "Mission Search Caveats")
* [Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958262/Components "Components")
* [Cone Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958263/Cone+Search+And+Upload+List+Search "Cone Search And Upload List Search")
* [Target Name Search And Upload List Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765614/Target+Name+Search+And+Upload+List+Search "Target Name Search And Upload List Search")
* [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview "Search Parameter Overview")
* [Core Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters "Core Search Parameters")
* [CLASSY Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131862458/CLASSY+Search+Components "CLASSY Search Components")
* [HST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components "HST Search Components")
* [JWST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350629/JWST+Search+Components "JWST Search Components")
* [ULLYSES Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158174811/ULLYSES+Search+Components "ULLYSES Search Components")
* [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters "Additional Search Parameters")
* [Choose Output Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958266/Choose+Output+Columns "Choose Output Columns")
* [The Search Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958267/The+Search+Bar "The Search Bar")
* [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page "Search Results Page")
* [Image Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/352354485/Image+Previews "Image Previews")
* [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay "Download Overlay")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [Jdaviz Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113039/Jdaviz+Guide "Jdaviz Guide")
* [Cloud Services Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797522/Cloud+Services+Manual "Cloud Services Manual")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")  
**On this page...**
* 1[HST-Specific Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-HST-SpecificSearchComponents)
* 1.1[Dataset ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-DatasetID)
* 1.2[Data Types](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-DataTypes)
* 1.3[ Instrument Selector](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-InstrumentSelector)
* 1.4[Observation Type](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-ObservationType)
* 2[Filtering for Enhanced Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-FilteringforEnhancedData)
* 2.1[HASP](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-HASP)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components#HSTSearchComponents-ForFurtherReading...)

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components"} -->
This page describes elements of the search form which are either unique to JWST, or are shared with other missions but contain options that are best explained on a per-mission basis.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Dataset ID"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/string-condition-example-1.png?version=1&modificationDate=1664284570162&api=v2)
The **'****Dataset ID'** is a unique dataset name. For HST, it is 9-characters long, e.g., J8BA7JCAQ or O4140Q020, where the first character indicates the instrument used: L=COS; I=WFC3; J=ACS; N=NICMOS; O=STIS; U=WFPC2; W=WFPC; X=FOC; Y=FOS; Z=GHRS; F=FGS; V=HSP.
This component is a [String field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview), so 'Exact Match', 'Wildcard', 'Exclude', and search by 'Multiple' entries are allowed. If known, type the exact dataset ID into this field's box. If the exact dataset ID is not known, conduct a wildcard search or type a string to enable a type-ahead menu. It will show a list of dataset IDs that contain that text. Browse through the suggested list to find the right one by scrolling the mouse or use the scroll bar on the right of the menu, and then click to select.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Data Types"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/data-type.png?version=1&modificationDate=1664284572632&api=v2)  
By default, the **'Data Type'** is set to 'ALL'. Check the check box for a preferred data type: 'SPECTRUM' or 'IMAGE'.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Instrument Selector"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/instrument-selector.png?version=1&modificationDate=1664284572608&api=v2)
This video clip demonstrates how to select different instruments to include in searches.
Some data collections contain datasets from a wide range of instruments, for example, the various [HST instruments](https://archive.stsci.edu/missions-and-data/hst#section-a998adf3-358a-4e01-828d-a3535b29fffd). Mission Search can include results from across all available instruments or a subset of them. By default, all available instruments are selected. Hovering the mouse over each instrument will show the full name of the instrument.
Depending on the **'Data Types'** selection, such as 'SPECTRUM' only or 'IMAGE' only, the list of available instruments will also change (an instrument that only takes images will not be shown if only 'SPECTRUM' data types are selected, for example). To select a single instrument, click the 'none' (![](https://outerspace.stsci.edu/download/thumbnails/102535413/hst-output-none.png?version=1&modificationDate=1628808842546&api=v2)) button and then select the desired instrument to include.
Some instruments produce neither images nor spectra: the Fine Guidance Sensors (FGS, which produce astrometric, usually interferometric, data) and the High Speed Photometer (HSP, which produced photometric data). These instruments will only appear if 'ALL' is selected in the Data Types area.

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "HST-Specific Search Components", "Header 2": "Observation Type"} -->
![](https://outerspace.stsci.edu/download/attachments/127765652/obs-type.png?version=1&modificationDate=1664284572655&api=v2)
The **'Observations'** selector can choose 'SCIENCE' and/or 'CALIBRATION'. The default setting is to search only 'SCIENCE'.

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Filtering for Enhanced Data"} -->
While searching for HST Observations, you may find products from additional processing pipelines.

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Filtering for Enhanced Data", "Header 2": "HASP"} -->
The [HASP (Hubble Advanced Spectral Products)](https://archive.stsci.edu/missions-and-data/hst/hasp) are a collection of co-added spectra for nearly all HST Observations. These are only generated for observations that used COS or STIS.
![an additional condition for selecting HASP data, with the include value \('1'\) filled in](https://outerspace.stsci.edu/download/attachments/127765652/HASP-filter.png?version=1&modificationDate=1706222733676&api=v2)
After [selecting an additional condition](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters), you can add a filter to include (1) or exclude (0) data from the HASP pipeline. By default, (i.e., with no value in the condition box), the HASP column will merely be included in the results table, with no selection by the value of this field.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)
* [Search Parameter Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

