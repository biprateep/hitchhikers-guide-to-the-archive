---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview"
date_accessed: "2026-03-11T11:34:04.164307"
---

<!-- CHUNK 1 START -->
**On this page...**
* 1[Component Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-ComponentOverview)
* 1.1[ Parameter Constraint Syntax](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_constraintsParameterConstraintSyntax)
* 1.1.1[Parameter Constraints: String Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_stringsParameterConstraints:StringFields)
* 1.1.2[Parameter Constraints: Numeric Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_numericsParameterConstraints:NumericFields)
* 1.1.3[Parameter Constraints: DateTime Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_datetimesParameterConstraints:DateTimeFields)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Component Overview"} -->
The **'****Core Search Parameters****'** section contains the most common search parameters for the selected data collection, which can vary between the different collections. This page overviews the types of search components and how to specify parameter constraints for components that can be found on multiple data collections.
There are three categories of search parameters: string (i.e. text), numeric, and datetime. There are thus three slightly different syntaxes when adding additional conditions to a parameter. The specifications outlined below apply equally to [core parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-core_params), [additional search parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters), and any mission-specific fields.
Hovering over a filter box in the search form will show "tooltips" on using search conditions.
* * *
How to specify constraints for search components that accept strings: search conditions, valid formats, and some examples.
Search Operation | Format | Example | Note
---|---|---|---
Exact match | abc | ![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-example-1.png?version=1&modificationDate=1698759247184&api=v2) | Type an exact string into string field boxes such as Dataset ID, Principal Investigator, or [Spectral Element](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-spectral_element) ('Names of Filters/Gratings').
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-exact-match-3.png?version=1&modificationDate=1698759247332&api=v2)
|  This example shows an exact match search for a combination filter set (i.e., a combination of filters delimited by a semicolon '**;'**) used for observations. **This is specific to the****Filters/Gratings component.**  
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-example-2.png?version=1&modificationDate=1698759247219&api=v2) |  There are many more string field input columns in the [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters) section. See more columns by clicking the **'****Column Name'** The **Target Descrip** column uses "substrings", which means that any text you enter will automatically have wildcards added in front and in back of it, e.g. "jup" is treated as "*jup*", and thus will find descriptions that include "Jupiter" in them.
Wildcard | *ab*c | ![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-wildcard-2.png?version=1&modificationDate=1698759247414&api=v2) |  Strings that include one or more asterisks (*) correspond to a wildcard, where zero or more additional characters can exist between the non-wildcard characters. Asterisks can be placed anywhere in each input string. Wildcard search does not support type-ahead functionality.
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-wildcard-1.png?version=1&modificationDate=1698759247378&api=v2)
Multiple |  abc, def
* * *
ab*, def
* * *
abc, de*, fg* |
![](https://outerspace.stsci.edu/download/attachments/104958264/string-conditon-multiple.png?version=1&modificationDate=1698759247528&api=v2) |  Search by multiple strings delimited by a comma (**,**) which acts as the logical operator 'OR'. This type of search includes all observations associated with one or more of the input strings in the [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page). Any number of strings delimited by a comma will work. Make sure not to confuse comma (**,**) with semicolon (**;**) for a 'Multiple' search.
Exclude |  !abc
* * *
!ab*c
* * *
!abc,!def
* * *
!ab*,!cd* |  
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-exclude.png?version=1&modificationDate=1698759247488&api=v2) |  An exclamation character (**!**) in front of a string excludes entries associated with the input string. This 'Exclude' operation can be combined with the 'Multiple' or 'Wildcard' operations, but is applied to the proceeding string only when using a 'Multiple' string search (strings separated by commas)_._ Example: '!G130M,!G160M,G*' will search for all observations that include a grating that begins with 'G', but excludes any that include the G130M or G160M gratings. Entering '!G130M,G160M' will apply the logical 'NOT' only to the G130M string, and thus return all observations that include the G160M grating and excludes the G130M grating.
Type ahead | character or character string |  |  Start typing a character or characters in each string field search box. The form offers a type-ahead operation in some text boxes, which allows scrolling through a suggested list. Once a string of characters is entered, a list of all available observations that match the input string is displayed. Scroll with the mouse or the scroll bar displayed on the right of the type-ahead menu to browse the options and click to select. Not all string fields offer this type-ahead search functionality. None of the fields within the **'Additional Columns'** section.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Component Overview", "Header 3": "Parameter Constraints: Numeric Fields"} -->
How to specify constraints for search components that accept numeric data types (integer, float): search conditions, valid formats, and some examples._
_
Search Operation | Format | Example | Note
---|---|---|---
Exact Number |  any number
| ![](https://outerspace.stsci.edu/download/attachments/104958264/exptime1000.png?version=1&modificationDate=1698759246609&api=v2) |  Type a number (or = a number) on a search condition field to retrieve observations matched with the exact value of the search parameter. The first example returns observations whose exposure time is exactly 1000 seconds, the second example returns observations with exposure time equal to exactly 14660 seconds.
= any number | ![](https://outerspace.stsci.edu/download/attachments/104958264/exptime14660.png?version=1&modificationDate=1698759246558&api=v2)
Comparison |  > number
* * *
>= number
* * *
< number
* * *
<= number |
![](https://outerspace.stsci.edu/download/attachments/104958264/number-condition-comparison-2.png?version=1&modificationDate=1698759248013&api=v2) |  Type a number with simple arithmetic operations (<, >, <=, or >=) to filter the search parameters. Only observations whose spectral resolving power is larger than or equal to 20000 are returned in this example, where the condition of '>= 20000' is used.
Range | num1 .. num2 | ![](https://outerspace.stsci.edu/download/attachments/104958264/numer-condition-range.png?version=1&modificationDate=1698759247935&api=v2) |  Use the special character expression of two periods (..) between two numeric values (numbers) to specify a range. This example (in the RA condition box entering 15.0567..17.6709 and in the Dec condition box entering -10.00..5.56) returns only observations whose targets are located between Right Ascension 15.0567 <= RA (degrees) <= 17.6709 **AND** Declination -10.00 <= Dec (degrees) <= 5.56.
Calculated Range |  num1 +- num2
* * *
num1 +- num2% | ![](https://outerspace.stsci.edu/download/attachments/104958264/number-condition-calculated-range.png?version=1&modificationDate=1698759247146&api=v2) |  Use the special character expression of +- between two numeric values (numbers) to specify a calculated range. This example (in the Exp Time condition box entering 400 +- 300 and in the Central Wavelength condition box entering 3000 +- 15%) returns only observations whose targets have an Exposure Time of 100 <= Exp Time <= 700 **AND** Central Wavelength 2550 <= Central Wavelength <= 3450.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Component Overview", "Header 3": "Parameter Constraints: DateTime Fields"} -->
How to specify constraints for search components that accept dates or times: search conditions, valid formats, and some examples.
Search Operation | Format | Example | Note
---|---|---|---
Exact date/time |  yyyy-mm-dd
* * *
yyyy-mm-dd hh:mm:ss | ![](https://outerspace.stsci.edu/download/attachments/104958264/date-time-example.png?version=1&modificationDate=1698759247776&api=v2) | Each condition for Date and Time can be directly typed using a valid format. However, it is not required to add Time constraints to initiate searches.
| Another option to filter the Date/Time constraint is using the built-in date calendar and the time clock, as seen in the video clip.
Comparison |  > yyyy-mm-dd
* * *
>= yyyy-mm-dd
* * *
< yyyy-mm-dd
* * *
<= yyyy-mm-dd |
![](https://outerspace.stsci.edu/download/attachments/104958264/date-time-comparison.png?version=1&modificationDate=1698759247899&api=v2) | Type dates with simple arithmetic operations (<, >, <=, or >=) to filter the search. This example returns all observations released on and before October 21, 1999 (1999-10-21).
Range |  yyyy-mm-dd
.. yyyy-mm-dd
* * *
yyyy-mm-dd hh:mm:ss .. yyyy-mm-dd hh:mm:ss | ![](https://outerspace.stsci.edu/download/attachments/104958264/date-time-range.png?version=1&modificationDate=1698759247866&api=v2) | Use the special character expression (..) between two dates to set the date range. Observations archived between 2010-05-10 and 2010-06-30 will be returned with this example condition.  
**Examples of Spectral Element Searches**
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

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)
* [HST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components)
* [CLASSY Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131862458/CLASSY+Search+Components)
* [ULLYSES Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158174811/ULLYSES+Search+Components)  
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
* 1[Component Overview](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-ComponentOverview)
* 1.1[ Parameter Constraint Syntax](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_constraintsParameterConstraintSyntax)
* 1.1.1[Parameter Constraints: String Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_stringsParameterConstraints:StringFields)
* 1.1.2[Parameter Constraints: Numeric Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_numericsParameterConstraints:NumericFields)
* 1.1.3[Parameter Constraints: DateTime Fields](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-param_datetimesParameterConstraints:DateTimeFields)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-ForFurtherReading...)

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Component Overview"} -->
The **'****Core Search Parameters****'** section contains the most common search parameters for the selected data collection, which can vary between the different collections. This page overviews the types of search components and how to specify parameter constraints for components that can be found on multiple data collections.
There are three categories of search parameters: string (i.e. text), numeric, and datetime. There are thus three slightly different syntaxes when adding additional conditions to a parameter. The specifications outlined below apply equally to [core parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-core_params), [additional search parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters), and any mission-specific fields.
Hovering over a filter box in the search form will show "tooltips" on using search conditions.
* * *
How to specify constraints for search components that accept strings: search conditions, valid formats, and some examples.
Search Operation | Format | Example | Note
---|---|---|---
Exact match | abc | ![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-example-1.png?version=1&modificationDate=1698759247184&api=v2) | Type an exact string into string field boxes such as Dataset ID, Principal Investigator, or [Spectral Element](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958264/Search+Parameter+Overview#SearchParameterOverview-spectral_element) ('Names of Filters/Gratings').
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-exact-match-3.png?version=1&modificationDate=1698759247332&api=v2)
|  This example shows an exact match search for a combination filter set (i.e., a combination of filters delimited by a semicolon '**;'**) used for observations. **This is specific to the****Filters/Gratings component.**  
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-example-2.png?version=1&modificationDate=1698759247219&api=v2) |  There are many more string field input columns in the [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters) section. See more columns by clicking the **'****Column Name'** The **Target Descrip** column uses "substrings", which means that any text you enter will automatically have wildcards added in front and in back of it, e.g. "jup" is treated as "*jup*", and thus will find descriptions that include "Jupiter" in them.
Wildcard | *ab*c | ![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-wildcard-2.png?version=1&modificationDate=1698759247414&api=v2) |  Strings that include one or more asterisks (*) correspond to a wildcard, where zero or more additional characters can exist between the non-wildcard characters. Asterisks can be placed anywhere in each input string. Wildcard search does not support type-ahead functionality.
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-wildcard-1.png?version=1&modificationDate=1698759247378&api=v2)
Multiple |  abc, def
* * *
ab*, def
* * *
abc, de*, fg* |
![](https://outerspace.stsci.edu/download/attachments/104958264/string-conditon-multiple.png?version=1&modificationDate=1698759247528&api=v2) |  Search by multiple strings delimited by a comma (**,**) which acts as the logical operator 'OR'. This type of search includes all observations associated with one or more of the input strings in the [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page). Any number of strings delimited by a comma will work. Make sure not to confuse comma (**,**) with semicolon (**;**) for a 'Multiple' search.
Exclude |  !abc
* * *
!ab*c
* * *
!abc,!def
* * *
!ab*,!cd* |  
![](https://outerspace.stsci.edu/download/attachments/104958264/string-condition-exclude.png?version=1&modificationDate=1698759247488&api=v2) |  An exclamation character (**!**) in front of a string excludes entries associated with the input string. This 'Exclude' operation can be combined with the 'Multiple' or 'Wildcard' operations, but is applied to the proceeding string only when using a 'Multiple' string search (strings separated by commas)_._ Example: '!G130M,!G160M,G*' will search for all observations that include a grating that begins with 'G', but excludes any that include the G130M or G160M gratings. Entering '!G130M,G160M' will apply the logical 'NOT' only to the G130M string, and thus return all observations that include the G160M grating and excludes the G130M grating.
Type ahead | character or character string |  |  Start typing a character or characters in each string field search box. The form offers a type-ahead operation in some text boxes, which allows scrolling through a suggested list. Once a string of characters is entered, a list of all available observations that match the input string is displayed. Scroll with the mouse or the scroll bar displayed on the right of the type-ahead menu to browse the options and click to select. Not all string fields offer this type-ahead search functionality. None of the fields within the **'Additional Columns'** section.

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Component Overview", "Header 3": "Parameter Constraints: Numeric Fields"} -->
How to specify constraints for search components that accept numeric data types (integer, float): search conditions, valid formats, and some examples._
_
Search Operation | Format | Example | Note
---|---|---|---
Exact Number |  any number
| ![](https://outerspace.stsci.edu/download/attachments/104958264/exptime1000.png?version=1&modificationDate=1698759246609&api=v2) |  Type a number (or = a number) on a search condition field to retrieve observations matched with the exact value of the search parameter. The first example returns observations whose exposure time is exactly 1000 seconds, the second example returns observations with exposure time equal to exactly 14660 seconds.
= any number | ![](https://outerspace.stsci.edu/download/attachments/104958264/exptime14660.png?version=1&modificationDate=1698759246558&api=v2)
Comparison |  > number
* * *
>= number
* * *
< number
* * *
<= number |
![](https://outerspace.stsci.edu/download/attachments/104958264/number-condition-comparison-2.png?version=1&modificationDate=1698759248013&api=v2) |  Type a number with simple arithmetic operations (<, >, <=, or >=) to filter the search parameters. Only observations whose spectral resolving power is larger than or equal to 20000 are returned in this example, where the condition of '>= 20000' is used.
Range | num1 .. num2 | ![](https://outerspace.stsci.edu/download/attachments/104958264/numer-condition-range.png?version=1&modificationDate=1698759247935&api=v2) |  Use the special character expression of two periods (..) between two numeric values (numbers) to specify a range. This example (in the RA condition box entering 15.0567..17.6709 and in the Dec condition box entering -10.00..5.56) returns only observations whose targets are located between Right Ascension 15.0567 <= RA (degrees) <= 17.6709 **AND** Declination -10.00 <= Dec (degrees) <= 5.56.
Calculated Range |  num1 +- num2
* * *
num1 +- num2% | ![](https://outerspace.stsci.edu/download/attachments/104958264/number-condition-calculated-range.png?version=1&modificationDate=1698759247146&api=v2) |  Use the special character expression of +- between two numeric values (numbers) to specify a calculated range. This example (in the Exp Time condition box entering 400 +- 300 and in the Central Wavelength condition box entering 3000 +- 15%) returns only observations whose targets have an Exposure Time of 100 <= Exp Time <= 700 **AND** Central Wavelength 2550 <= Central Wavelength <= 3450.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Component Overview", "Header 3": "Parameter Constraints: DateTime Fields"} -->
How to specify constraints for search components that accept dates or times: search conditions, valid formats, and some examples.
Search Operation | Format | Example | Note
---|---|---|---
Exact date/time |  yyyy-mm-dd
* * *
yyyy-mm-dd hh:mm:ss | ![](https://outerspace.stsci.edu/download/attachments/104958264/date-time-example.png?version=1&modificationDate=1698759247776&api=v2) | Each condition for Date and Time can be directly typed using a valid format. However, it is not required to add Time constraints to initiate searches.
| Another option to filter the Date/Time constraint is using the built-in date calendar and the time clock, as seen in the video clip.
Comparison |  > yyyy-mm-dd
* * *
>= yyyy-mm-dd
* * *
< yyyy-mm-dd
* * *
<= yyyy-mm-dd |
![](https://outerspace.stsci.edu/download/attachments/104958264/date-time-comparison.png?version=1&modificationDate=1698759247899&api=v2) | Type dates with simple arithmetic operations (<, >, <=, or >=) to filter the search. This example returns all observations released on and before October 21, 1999 (1999-10-21).
Range |  yyyy-mm-dd
.. yyyy-mm-dd
* * *
yyyy-mm-dd hh:mm:ss .. yyyy-mm-dd hh:mm:ss | ![](https://outerspace.stsci.edu/download/attachments/104958264/date-time-range.png?version=1&modificationDate=1698759247866&api=v2) | Use the special character expression (..) between two dates to set the date range. Observations archived between 2010-05-10 and 2010-06-30 will be returned with this example condition.  
**Examples of Spectral Element Searches**
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

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Mission Search Guide Home](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Mission+Search+Guide+v1.2)
* [HST Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/127765652/HST+Search+Components)
* [CLASSY Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/131862458/CLASSY+Search+Components)
* [ULLYSES Search Components](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158174811/ULLYSES+Search+Components)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 9 END -->

