---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions"
date_accessed: "2026-03-11T16:27:04.931540"
content_length: 32976
---

<!-- CHUNK 1 START -->
The Download Overlay component includes the ability to select products with regular expressions. This article gives extensive examples of how to use regex effectively.
**On this page...**
* 1[The What and Why of Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-TheWhatandWhyofRegularExpressions)
* 2[Common Regex Syntax](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-CommonRegexSyntax)
* 3[An Important Distinction](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-AnImportantDistinction)
* 4[Example Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-ExampleSearches)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "The What and Why of Regular Expressions"} -->
A regular expression (often called a regex) is a powerful way to search text for matches. At the most basic level, it functions similarly to the "control/command + f" search function in most text editors and web browsers; any exact match with the "simple string" you enter will be returned. The advantage of regex is its specialized syntax, which allows for complex queries beyond simple 1:1 matching. This page will list the syntaxes available to you in the search form and walk through some examples of regex queries.
Regex is an advanced feature
It is likely that the filter you are attempting to apply can be found within the [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay) itself; you should start there.
Before you attempt to use advanced regex syntax in your search for files, you should try searching as you would in a browser or document. Often, a more complex query is not necessary to match your target filenames.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Common Regex Syntax"} -->
Not all regex syntax is valid for a filename search. The most useful syntaxes are included in the table below.
Syntax | Meaning
---|---
`.` | Matches any character
`*` | The preceding character appears zero or more times
`+` | The preceding character appears one or more times
`$` | Matches the end of a filename
`[aeiou]` | Matches any character in the listed set
`[^XYZ]` | Matches any character _not_ in the listed set
`[a-z0-9]` | The set of characters can include a range or multiple ranges
If you want to use one of the special characters literally, you must 'escape' it. For example, if you actually wanted to include a period in your search query, you should enter "\\."

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "An Important Distinction"} -->
One of the most common mistakes in regex is using `*` (asterisk character) as a generic wildcard character. As is shown in the example table below, the `*` character is always interpreted in conjunction with the preceding character.
The correct syntax for a wildcard is either "`.*`" or "`.+`", depending on whether the absence of a character should be included. See the last two columns of "regex input" for help clarifying this subtle point.  
| Regex input
---|---
Filename | jwst*file | jwst.file | jwst.*file | jwst.+file
`jwstfile.fits` | Match | No match | Match | No match
`jwsttttfile.fits` | Match | No match | Match | Match
`jwstXfile.fits` | No match | Match | Match | Match
`jwst_abc123_file.fits` | No match | No match | Match | Match

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Example Searches"} -->
These examples use real filenames produced by the JWST mission. All text in the Regex Input column is "raw"; that is, you should enter it into the search bar exactly as you see it. Where special characters are used, they either take advantage of regex functionality or are part of the filename.
Regex Input | Match? | Notes
---|---|---
```
rate
```
|  Matches jw02783001001_04103_00001-seg001_mirimage_rate.fits jw02783001001_04103_00001-seg001_mirimage_rateints.fits Does not match jw02783001001_04103_00001-seg001_mirimage_uncal.fits
|  A regex search iterates through the filenames and returns matching strings. In this basic case, we've asked for all files that contain the phrase 'rate' somewhere within the name. It does not matter where this appears within the name; a simple string search is equivalent to a search in most text editors and internet browsers. The last example does not match because it does not have "rate" anywhere in its name.
```
rate\.fits
```
|  Matches jw02783001001_04103_00001-seg001_mirimage_rate.fits Does not match jw02783001001_04103_00001-seg001_mirimage_rateints.fits jwst_miri_filteroffset_0006.asdf |  Although it's recommended to filter file types using the UI, it's also possible to filter using regex. The period is a special input that matches any character in our search string, so we escape it here using a backslash. It is good practice, but unnecessary in this case, to escape the period. There are no files with names like "rate9fits" that would cause an accidental match.
```
fits$
```
|  Matches jwst_miri_flat_0789.fitsjw02783001001_04103_00001-seg001_mirimage_rate.fits
Does not match jwst_1077.pmap jwst_niriss_distortion_0032.asdf | Using the $ character, we can search for patterns at the end of a filename. This is particularly helpful in this example, where we look for filenames ending in fits. All other file types will be excluded.
```
(fits|asdf)$
```
|  Matches jwst_miri_flat_0789.fitsjwst_niriss_distortion_0032.asdf Does not match jwst_1077.pmap | We can combine $ with the "or" operator to great effect. In this query, we keep files ending in 'fits' or 'asdf', but exclude all others.
```
(?<!fits|asdf)$
```
|  Matches jwst_1077.pmap
Does not match jwst_miri_flat_0789.fits jwst_niriss_distortion_0032.asdf
|  This particular combination of special characters does the opposite of the last example: it excludes all fits and asdf files. You can chain together multiple, i.e. more than two, file types using the "or" operator. This uses an advanced  A word of caution that regex contains many such advanced/obscure operators. Getting them to work is only the first step; remembering  _how_ they work is even harder!
```
seg00[123]
```
|  Matches jw02783001001_04103_00001-seg002_mirimage_calints.fits jw02783001001_04103_00001-seg003_mirimage_rate.fits Does not match jw02783001001_04103_00001-seg007_mirimage_x1dints.fits
|  Brackets limit the set of permissible characters. Our search in this example will find any file that contains 'seg00N', where N is either 1, 2, or 3. The last example does not match because '7' is not in the allowed set of characters.
```
seg00[0-8]
```
|  Matches jw02783001001_04103_00001-seg008_mirimage_x1dints.fits Does not match jw02783001001_04103_00001-seg009_mirimage_x1dints.fits
|  Instead of specifying specific allowed characters, as we do in the above example, regex allows for ranges. In this case, we've allowed all numbers between (and inclusive of) 0 and 8. The last example does not match because '9' is not in the allowed set of characters.
```
seg00[^9]
```
|  Matches jw02783001001_04103_00001-seg008_mirimage_x1dints.fits Does not match jw02783001001_04103_00001-seg009_mirimage_x1dints.fits
|  This search returns the same results as the previous, since "not 9" is equivalent to "the numbers 0 to 8" in this case.  **Note:** In general, these searches are not equivalent. A filename containing "seg00B" would match _seg00[^9]_ , since B is not 9. "seg00B" would not match with _seg00[0-8],_ since B is not in the range 0-8. We can conveniently ignore this caveat for this search, as we know that "seg00B" is nonsense in a JWST filename.
```
_[a-z]+ints
```
|  Matches jw02783001001_04103_00001-seg001_mirimage_calints.fits jw02783001001_04103_00001-seg004_mirimage_rateints.fits Does not match jw02783001001_04103_00001-seg009_mirimage_x1dints.fits
|  This search uses a wildcard character: '+', which means "the repeating character should show up at least once". We've used a clever trick here by combining it with "[a-z]", the set of all lowercase letters. In essence, we're asking: "Please find all strings that have an underscore, followed by any sequence of lowercase letters, followed by 'ints'." All of these example names end with _xxxints.fits. Our first two examples match because 'cal' and 'rate' are exclusively lowercase letters. The last example fails because 'x1d' contains a number.

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
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
* [Additional Search Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958265/Additional+Search+Parameters "Additional Search Parameters")
* [Choose Output Columns](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958266/Choose+Output+Columns "Choose Output Columns")
* [The Search Bar](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/104958267/The+Search+Bar "The Search Bar")
* [Search Results Page](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840287/Search+Results+Page "Search Results Page")
* [Image Previews](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/352354485/Image+Previews "Image Previews")
* [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay "Download Overlay")
* [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions "Regular Expressions")
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
* [Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions "Regular Expressions")
* [HLSP Contributor Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290399/HLSP+Contributor+Guide "HLSP Contributor Guide")
* [About HLSPs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290401/About+HLSPs "About HLSPs")
* [HLSP How-To Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290402/HLSP+How-To+Guide "HLSP How-To Guide")
* [Required Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290403/Required+Contents "Required Contents")
* [Required Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/97290409/Required+Metadata "Required Metadata")
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
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
The Download Overlay component includes the ability to select products with regular expressions. This article gives extensive examples of how to use regex effectively.
**On this page...**
* 1[The What and Why of Regular Expressions](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-TheWhatandWhyofRegularExpressions)
* 2[Common Regex Syntax](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-CommonRegexSyntax)
* 3[An Important Distinction](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-AnImportantDistinction)
* 4[Example Searches](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-ExampleSearches)
* 5[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/217350273/Regular+Expressions#RegularExpressions-ForFurtherReading...)

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "The What and Why of Regular Expressions"} -->
A regular expression (often called a regex) is a powerful way to search text for matches. At the most basic level, it functions similarly to the "control/command + f" search function in most text editors and web browsers; any exact match with the "simple string" you enter will be returned. The advantage of regex is its specialized syntax, which allows for complex queries beyond simple 1:1 matching. This page will list the syntaxes available to you in the search form and walk through some examples of regex queries.
Regex is an advanced feature
It is likely that the filter you are attempting to apply can be found within the [Download Overlay](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/107840400/Download+Overlay) itself; you should start there.
Before you attempt to use advanced regex syntax in your search for files, you should try searching as you would in a browser or document. Often, a more complex query is not necessary to match your target filenames.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Common Regex Syntax"} -->
Not all regex syntax is valid for a filename search. The most useful syntaxes are included in the table below.
Syntax | Meaning
---|---
`.` | Matches any character
`*` | The preceding character appears zero or more times
`+` | The preceding character appears one or more times
`$` | Matches the end of a filename
`[aeiou]` | Matches any character in the listed set
`[^XYZ]` | Matches any character _not_ in the listed set
`[a-z0-9]` | The set of characters can include a range or multiple ranges
If you want to use one of the special characters literally, you must 'escape' it. For example, if you actually wanted to include a period in your search query, you should enter "\\."

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "An Important Distinction"} -->
One of the most common mistakes in regex is using `*` (asterisk character) as a generic wildcard character. As is shown in the example table below, the `*` character is always interpreted in conjunction with the preceding character.
The correct syntax for a wildcard is either "`.*`" or "`.+`", depending on whether the absence of a character should be included. See the last two columns of "regex input" for help clarifying this subtle point.  
| Regex input
---|---
Filename | jwst*file | jwst.file | jwst.*file | jwst.+file
`jwstfile.fits` | Match | No match | Match | No match
`jwsttttfile.fits` | Match | No match | Match | Match
`jwstXfile.fits` | No match | Match | Match | Match
`jwst_abc123_file.fits` | No match | No match | Match | Match

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Example Searches"} -->
These examples use real filenames produced by the JWST mission. All text in the Regex Input column is "raw"; that is, you should enter it into the search bar exactly as you see it. Where special characters are used, they either take advantage of regex functionality or are part of the filename.
Regex Input | Match? | Notes
---|---|---
```
rate
```
|  Matches jw02783001001_04103_00001-seg001_mirimage_rate.fits jw02783001001_04103_00001-seg001_mirimage_rateints.fits Does not match jw02783001001_04103_00001-seg001_mirimage_uncal.fits
|  A regex search iterates through the filenames and returns matching strings. In this basic case, we've asked for all files that contain the phrase 'rate' somewhere within the name. It does not matter where this appears within the name; a simple string search is equivalent to a search in most text editors and internet browsers. The last example does not match because it does not have "rate" anywhere in its name.
```
rate\.fits
```
|  Matches jw02783001001_04103_00001-seg001_mirimage_rate.fits Does not match jw02783001001_04103_00001-seg001_mirimage_rateints.fits jwst_miri_filteroffset_0006.asdf |  Although it's recommended to filter file types using the UI, it's also possible to filter using regex. The period is a special input that matches any character in our search string, so we escape it here using a backslash. It is good practice, but unnecessary in this case, to escape the period. There are no files with names like "rate9fits" that would cause an accidental match.
```
fits$
```
|  Matches jwst_miri_flat_0789.fitsjw02783001001_04103_00001-seg001_mirimage_rate.fits
Does not match jwst_1077.pmap jwst_niriss_distortion_0032.asdf | Using the $ character, we can search for patterns at the end of a filename. This is particularly helpful in this example, where we look for filenames ending in fits. All other file types will be excluded.
```
(fits|asdf)$
```
|  Matches jwst_miri_flat_0789.fitsjwst_niriss_distortion_0032.asdf Does not match jwst_1077.pmap | We can combine $ with the "or" operator to great effect. In this query, we keep files ending in 'fits' or 'asdf', but exclude all others.
```
(?<!fits|asdf)$
```
|  Matches jwst_1077.pmap
Does not match jwst_miri_flat_0789.fits jwst_niriss_distortion_0032.asdf
|  This particular combination of special characters does the opposite of the last example: it excludes all fits and asdf files. You can chain together multiple, i.e. more than two, file types using the "or" operator. This uses an advanced  A word of caution that regex contains many such advanced/obscure operators. Getting them to work is only the first step; remembering  _how_ they work is even harder!
```
seg00[123]
```
|  Matches jw02783001001_04103_00001-seg002_mirimage_calints.fits jw02783001001_04103_00001-seg003_mirimage_rate.fits Does not match jw02783001001_04103_00001-seg007_mirimage_x1dints.fits
|  Brackets limit the set of permissible characters. Our search in this example will find any file that contains 'seg00N', where N is either 1, 2, or 3. The last example does not match because '7' is not in the allowed set of characters.
```
seg00[0-8]
```
|  Matches jw02783001001_04103_00001-seg008_mirimage_x1dints.fits Does not match jw02783001001_04103_00001-seg009_mirimage_x1dints.fits
|  Instead of specifying specific allowed characters, as we do in the above example, regex allows for ranges. In this case, we've allowed all numbers between (and inclusive of) 0 and 8. The last example does not match because '9' is not in the allowed set of characters.
```
seg00[^9]
```
|  Matches jw02783001001_04103_00001-seg008_mirimage_x1dints.fits Does not match jw02783001001_04103_00001-seg009_mirimage_x1dints.fits
|  This search returns the same results as the previous, since "not 9" is equivalent to "the numbers 0 to 8" in this case.  **Note:** In general, these searches are not equivalent. A filename containing "seg00B" would match _seg00[^9]_ , since B is not 9. "seg00B" would not match with _seg00[0-8],_ since B is not in the range 0-8. We can conveniently ignore this caveat for this search, as we know that "seg00B" is nonsense in a JWST filename.
```
_[a-z]+ints
```
|  Matches jw02783001001_04103_00001-seg001_mirimage_calints.fits jw02783001001_04103_00001-seg004_mirimage_rateints.fits Does not match jw02783001001_04103_00001-seg009_mirimage_x1dints.fits
|  This search uses a wildcard character: '+', which means "the repeating character should show up at least once". We've used a clever trick here by combining it with "[a-z]", the set of all lowercase letters. In essence, we're asking: "Please find all strings that have an underscore, followed by any sequence of lowercase letters, followed by 'ints'." All of these example names end with _xxxints.fits. Our first two examples match because 'cal' and 'rate' are exclusively lowercase letters. The last example fails because 'x1d' contains a number.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 11 END -->

