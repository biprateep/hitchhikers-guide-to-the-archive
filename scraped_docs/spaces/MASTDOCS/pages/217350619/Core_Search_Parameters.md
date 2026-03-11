---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters"
date_accessed: "2026-03-11T11:37:13.760369"
---

<!-- CHUNK 1 START -->
Some parameters are used on many (but not all) search forms. The most common of these are described in this article.
* 1[Exposure Duration](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-ExposureDuration)
* 2[Observed Date](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-ObservedDate)
* 3[Principal Investigator](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_principalinvPrincipalInvestigator)
* 4[Proposal ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_programidProposalID)
* 5[Release Date](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_reldateReleaseDate)
* 6[Spectral Element](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_spec_elemSpectralElement)
* 6.1[Example Spectral Element Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-ExampleSpectralElementSearches)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Exposure Duration"} -->
The **Exposure Time** is a [Numeric field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_numerics).
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_expTime.png?version=1&modificationDate=1734360314691&api=v2)
The **Exposure Time** field allows querying for observations based on values or ranges of exposure duration, in seconds. Type a number, conditional operation, or a range.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Observed Date"} -->
The **Observation Start Date** is a [DateTime field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_datetimes).
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_obsDate.png?version=1&modificationDate=1734361582372&api=v2)
To constrain data by Date and/or Time, use the format: yyyy-mm-dd in the **Obs Start Date** field and hh:mm:ss in the **Time** field. Note the **Time** field is not required.
Shortcuts are available in these fields. Entering just a year in the **Obs Start Date** field will default to January 1st of the year, e.g., entering just '2001' is the same as entering '2001-01-01'. Entering just a year and month will default to the 1st of that month, e.g., entering just '2001-04' is the same as entering '2001-04-01'. Entering partial times will fill in the rest with zeroes, e.g., entering '15' in the 'Time' field is the same as entering '15:00:00', and entering '11:30' is the same as entering '11:30:00'.
In addition to directly typing in an exact date/time, this component offers a built-in calendar and clock to set the parameters.
The **Principal Investigator** is a [String field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_strings).  
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_piName.png?version=1&modificationDate=1734361883334&api=v2)
Type an exact surname or a character string to enable a type-ahead menu. Once the type-ahead menu pops out, scroll through the surname list and select a name. 'Wildcard' search, 'Exclude' search, and search by 'Multiple' entries are allowed, but will not work with the type-ahead drop-down list.
The **Proposal ID** is a [Numeric field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_numerics).
![](https://outerspace.stsci.edu/download/attachments/217350619/proposal_id.png?version=1&modificationDate=1699475769672&api=v2)
The **Proposal ID** component allows search by proposal ID number(s) assigned to observation(s). Note that for some data collections, this might refer to Proposal ID or Guest Investigator ID.
This field allows an exact match, conditional search (for example, >= 14657) or a range search (for example, 12500 .. 12600). Type the Proposal ID with a preferred numeric search operation.
The **Release Date** is a [DateTime field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_datetimes).
![](https://outerspace.stsci.edu/download/attachments/217350619/release-date.png?version=1&modificationDate=1699475769666&api=v2)
An Observation is considered "released" when it becomes available to people outside the Principal Investigator Team; depending on the exclusive access period, this could be instant or take up to a year.
See [the Observed Date component](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_obsdate) for tips on how to use this component.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Spectral Element"} -->
The **Spectral Element** is a special [String Field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-param_strings).  
Example of a type-ahead search result for Filters/Gratings that start with 'G13':
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_optElement.png?version=1&modificationDate=1734362744677&api=v2)  
Example of 3 filter/grating entries: an exact match of POL120, a wildcard search on G*, and an exclusion of G130M:
![](https://outerspace.stsci.edu/download/attachments/217350619/spec_elem_sample_entries.png?version=1&modificationDate=1699475769631&api=v2)
The **Spectral Element** refers to filters, gratings, both, or combination filter sets such as 'POL120UV;F330W' depending on the data collection.
One or more filters or gratings can be entered into the **Filters/ Gratings** box. Press 'tab', 'return', or 'comma' on your keyboard to finish entering the filter/grating name (clicking off the text box will also work).
* Upon entering a filter/grating, it will be added and surrounded by a light-blue color. The filter/grating shown will be included as a search filter.  
![](https://outerspace.stsci.edu/download/thumbnails/217350619/spec_elem_chip.png?version=1&modificationDate=1699475769605&api=v2)
* The 'X' mark right next to each entry can used to remove a filter/grating.  
This field supports type-ahead. Once a key is pressed, a list of filters/gratings that contain that text will be shown. Browse through the suggested list to find the one being searched for, and then click to select it.
Since there are many options for searching based on the filter/grating list, we expand the description with more examples below. There are various ways to constrain the search. Below are some examples of how to use these constraints. Experiment with other options for further constraining the search.

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Spectral Element", "Header 2": "Example Spectral Element Searches"} -->
Operation | Examples | Note
---|---|---
Exact match  
| G130M |  Type an exact name of the filter, grating, or the combination filter set to retrieve only observations associated with the input string. Combination filter sets are delimited by a semicolon (;). Remember that combination sets are **single** strings.
MIRRORA
POL120UV;F330W
F2ND;CLEAR2;F1ND;F372M
Wildcard | G*M | This example retrieves observations that used grating names starting with 'G' and ending with 'M' such as 'G150M' or 'G220M'.
F81* | Since a combination filter set is considered as a single string, the input wildcard characters 'F81*' retrieve all observations associated with the filter 'F814W' and the other ones such as 'F814W;POLQN18 and 'F814W;F791W'.
Multiple | G130M, F550W | The 'Multiple' operator (',') acts as the logical operator 'OR'. Thus this example retrieves observations used the grating 'G130M' or the filter 'F550W'.  
| F550W,POL60UV;PR200L |  This example retrieves observations used the filter 'F550W' or the combination filter set 'POL60UV;PR200L'. Be sure to use the 'Multiple' operator, comma (,) not a semicolon (;) used for appending filters for combination filter set names.
Exclude | !F550W | This operation excludes any observations using the filter 'F550W'.
G*,!G140L | This search retrieves observations using all grating options ('G*) except the grating 'G140L'.
Type ahead |
|  Type ahead limitation Note that this only shows a list of single spectral elements and not combination filter sets.
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
Some parameters are used on many (but not all) search forms. The most common of these are described in this article.
* 1[Exposure Duration](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-ExposureDuration)
* 2[Observed Date](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-ObservedDate)
* 3[Principal Investigator](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_principalinvPrincipalInvestigator)
* 4[Proposal ID](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_programidProposalID)
* 5[Release Date](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_reldateReleaseDate)
* 6[Spectral Element](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_spec_elemSpectralElement)
* 6.1[Example Spectral Element Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-ExampleSpectralElementSearches)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Exposure Duration"} -->
The **Exposure Time** is a [Numeric field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_numerics).
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_expTime.png?version=1&modificationDate=1734360314691&api=v2)
The **Exposure Time** field allows querying for observations based on values or ranges of exposure duration, in seconds. Type a number, conditional operation, or a range.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Observed Date"} -->
The **Observation Start Date** is a [DateTime field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_datetimes).
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_obsDate.png?version=1&modificationDate=1734361582372&api=v2)
To constrain data by Date and/or Time, use the format: yyyy-mm-dd in the **Obs Start Date** field and hh:mm:ss in the **Time** field. Note the **Time** field is not required.
Shortcuts are available in these fields. Entering just a year in the **Obs Start Date** field will default to January 1st of the year, e.g., entering just '2001' is the same as entering '2001-01-01'. Entering just a year and month will default to the 1st of that month, e.g., entering just '2001-04' is the same as entering '2001-04-01'. Entering partial times will fill in the rest with zeroes, e.g., entering '15' in the 'Time' field is the same as entering '15:00:00', and entering '11:30' is the same as entering '11:30:00'.
In addition to directly typing in an exact date/time, this component offers a built-in calendar and clock to set the parameters.
The **Principal Investigator** is a [String field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_strings).  
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_piName.png?version=1&modificationDate=1734361883334&api=v2)
Type an exact surname or a character string to enable a type-ahead menu. Once the type-ahead menu pops out, scroll through the surname list and select a name. 'Wildcard' search, 'Exclude' search, and search by 'Multiple' entries are allowed, but will not work with the type-ahead drop-down list.
The **Proposal ID** is a [Numeric field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_numerics).
![](https://outerspace.stsci.edu/download/attachments/217350619/proposal_id.png?version=1&modificationDate=1699475769672&api=v2)
The **Proposal ID** component allows search by proposal ID number(s) assigned to observation(s). Note that for some data collections, this might refer to Proposal ID or Guest Investigator ID.
This field allows an exact match, conditional search (for example, >= 14657) or a range search (for example, 12500 .. 12600). Type the Proposal ID with a preferred numeric search operation.
The **Release Date** is a [DateTime field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_datetimes).
![](https://outerspace.stsci.edu/download/attachments/217350619/release-date.png?version=1&modificationDate=1699475769666&api=v2)
An Observation is considered "released" when it becomes available to people outside the Principal Investigator Team; depending on the exclusive access period, this could be instant or take up to a year.
See [the Observed Date component](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-comp_obsdate) for tips on how to use this component.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Spectral Element"} -->
The **Spectral Element** is a special [String Field](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350619/Core+Search+Parameters#CoreSearchParameters-param_strings).  
Example of a type-ahead search result for Filters/Gratings that start with 'G13':
![](https://outerspace.stsci.edu/download/thumbnails/217350619/dialog_MM_optElement.png?version=1&modificationDate=1734362744677&api=v2)  
Example of 3 filter/grating entries: an exact match of POL120, a wildcard search on G*, and an exclusion of G130M:
![](https://outerspace.stsci.edu/download/attachments/217350619/spec_elem_sample_entries.png?version=1&modificationDate=1699475769631&api=v2)
The **Spectral Element** refers to filters, gratings, both, or combination filter sets such as 'POL120UV;F330W' depending on the data collection.
One or more filters or gratings can be entered into the **Filters/ Gratings** box. Press 'tab', 'return', or 'comma' on your keyboard to finish entering the filter/grating name (clicking off the text box will also work).
* Upon entering a filter/grating, it will be added and surrounded by a light-blue color. The filter/grating shown will be included as a search filter.  
![](https://outerspace.stsci.edu/download/thumbnails/217350619/spec_elem_chip.png?version=1&modificationDate=1699475769605&api=v2)
* The 'X' mark right next to each entry can used to remove a filter/grating.  
This field supports type-ahead. Once a key is pressed, a list of filters/gratings that contain that text will be shown. Browse through the suggested list to find the one being searched for, and then click to select it.
Since there are many options for searching based on the filter/grating list, we expand the description with more examples below. There are various ways to constrain the search. Below are some examples of how to use these constraints. Experiment with other options for further constraining the search.

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Spectral Element", "Header 2": "Example Spectral Element Searches"} -->
Operation | Examples | Note
---|---|---
Exact match  
| G130M |  Type an exact name of the filter, grating, or the combination filter set to retrieve only observations associated with the input string. Combination filter sets are delimited by a semicolon (;). Remember that combination sets are **single** strings.
MIRRORA
POL120UV;F330W
F2ND;CLEAR2;F1ND;F372M
Wildcard | G*M | This example retrieves observations that used grating names starting with 'G' and ending with 'M' such as 'G150M' or 'G220M'.
F81* | Since a combination filter set is considered as a single string, the input wildcard characters 'F81*' retrieve all observations associated with the filter 'F814W' and the other ones such as 'F814W;POLQN18 and 'F814W;F791W'.
Multiple | G130M, F550W | The 'Multiple' operator (',') acts as the logical operator 'OR'. Thus this example retrieves observations used the grating 'G130M' or the filter 'F550W'.  
| F550W,POL60UV;PR200L |  This example retrieves observations used the filter 'F550W' or the combination filter set 'POL60UV;PR200L'. Be sure to use the 'Multiple' operator, comma (,) not a semicolon (;) used for appending filters for combination filter set names.
Exclude | !F550W | This operation excludes any observations using the filter 'F550W'.
G*,!G140L | This search retrieves observations using all grating options ('G*) except the grating 'G140L'.
Type ahead |
|  Type ahead limitation Note that this only shows a list of single spectral elements and not combination filter sets.
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 9 END -->

