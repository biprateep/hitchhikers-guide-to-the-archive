---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API"
date_accessed: "2026-03-11T11:36:59.579514"
---

<!-- CHUNK 1 START -->
This guide serves as a basic introduction to the syntax and structure of making an API call. Where possible, MAST APIs adhere to the syntax and structure described here.
**On this page...**
* 1[Types of HTTP Requests](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-TypesofHTTPRequests)
* 1.1[GET](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-GET)
* 1.1.1[Example API call with GET](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ExampleAPIcallwithGET)
* 1.2[POST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-POST)
* 1.2.1[Example API call with POST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ExampleAPIcallwithPOST)
* 2[HTTP Responses](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-HTTPResponses)
* 2.1[Example Responses](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ExampleResponses)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ForFurtherReading...)  
APIs, or Application Programming Interfaces, are a collection of services (sometimes referred to as routes or endpoints) aimed at providing programmatic access to some data, feature, or functionality. It is common for APIs to be designed around a particular product, idea, or function, often grouping related services together. Each service is designed as an  system, i.e. "you submit a request for something, or to do something, and receive a response". A simple playground for trying out sample HTTP requests/responses is . An alternative playground with curl and python examples is
Once an API is served by a host, all services become available as accessible HTTP URLs. To make an HTTP request to a service, one provides the URL name, and any allowed optional input parameters. Additional information, e.g. authorization information, or intended request format, can also be attached in the header of your request. HTTP responses typically, but not always, will return JSON objects containing the result of the API service call.

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests"} -->
The two most common types of requests are GET and POST requests, but other **scheme://host_domain/path** , e.g. <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html>.

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "GET"} -->
GET requests are simple requests to retrieve some data. Input parameters are often referred to as **query parameters** , and can be appended to the end of a URL by a **?** , with additional parameters added with an **&** , e.g. the syntax is **url?parameter=value &parameter=value**. Alternatively, when using a library to submit the request, they can be supplied separately from the URL. See  or  for an example.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "GET", "Header 3": "Example API call with GET"} -->
Example GET HTTP requests with a variety of libraries.
**web browser** - can only make GET requests
Paste into browser url bar:
```
# parameters in url
curl -X GET "https://httpbin.org/get?x=5&y=hello"

# parameters supplied
curl -X GET "https://httpbin.org/get" -G -d 'x=5' -d 'y=hello'
```  
```
# parameters in url
http get "https://httpbin.org/get?x=5&y=hello"

# parameters supplied
http get "https://httpbin.org/get" x==5 y==hello
```  
**Python**
```
# parameters in url
import requests
r = requests.get("https://httpbin.org/get?x=5&y=hello")

# parameters supplied
r = requests.get("https://httpbin.org/get", params={"x": 5, "y": "hello"})
```

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "POST"} -->
POST requests are requests to retrieve or change some data. While similar to GET requests, they differ in a few ways. One, the input parameters are not appended to the end of the URL as in GET requests, and two, they cannot be submitted by the url bar of a front-end web browser. Input parameters are instead passed as form, JSON, or dictionary parameters in the request itself, and are often referred to as **data, form, or json parameters**. See

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "POST", "Header 3": "Example API call with POST"} -->
Example POST HTTP requests with a variety of libraries.
```
# as a form
curl -X POST "https://httpbin.org/post" -d 'x=5' -d 'y=hello'

# as a JSON
curl -X POST "https://httpbin.org/post" -d 'x=5' -d 'y=hello' -H 'Content-Type: application/json'
```  
```
# as a form
http post "https://httpbin.org/post" x=5 y=hello -f

# as a JSON
http post "https://httpbin.org/post" x=5 y=hello
```  
**Python**
```
# as a form
import requests
r = requests.post("https://httpbin.org/post", data={"x": 5, "y": "hello"})

# as a JSON
r = requests.post("https://httpbin.org/post", json={"x":5, "y":"hello"})
```

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "HTTP Responses"} -->
After you make a request, you generally receive an HTTP response. Like requests, HTTP responses have headers, providing contextual information, and a body content with output response data. The success or failure of an HTTP response is indicated with a status code. A successful response usually has a status code of **200**. Other status codes indicate the type of problem that occurred. For example, a status code of **404** means the requested URL does not exist. See **500** means something has gone wrong on the server that has not been accounted for, or is an uncaught error.
HTTP response data can be in a wide variety of formats. These formats are called Mime-Types and are usually specified in the Content-Type field of the response header, which indicates the type of content found in the response. For APIs, a common response data format is JSON, which has a Content-Type of "**application/json** ". Other example formats might be plain text, html, or binary data such as images or files. See

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "HTTP Responses", "Header 2": "Example Responses"} -->
Examples of response data from the browser or from specific libraries. Most of the examples shown here highlight a JSON response format. See **curl** ,
**Python**
When you send a request in Python, you get a Response object back. The raw body content is found in the **r.content** attribute. If the response is in JSON format, you can conveniently convert the content to JSON with the **r.json()** method. The following code block shows an example response for the example POST request:  **r=requests.post(" https://httpbin.org/json")**
**example python JSON response**
```
# send the request and get a response
r = requests.post("https://httpbin.org/json")
r
<Response [200]>

# get the JSON response data
r.json()
{'slideshow': {'author': 'Yours Truly',
'date': 'date of publication',
'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'},
{'items': ['Why <em>WonderWidgets</em> are great',
'Who <em>buys</em> WonderWidgets'],
'title': 'Overview',
'type': 'all'}],
'title': 'Sample Slide Show'}}
```  
Here is an example response of content that is html instead of JSON, to highlight extracting the raw body content instead, from:
`r = requests.post("https://httpbin.org/html")`
See **text/html.**
**example python html response**
```
# send the request and get a response
r = requests.post("https://httpbin.org/html")
r
<Response [200]>

# get the HTML content
r.content
b"<!DOCTYPE html>\n<html>\n  <head>\n  </head>\n  <body>\n      <h1>Herman Melville - Moby-Dick</h1>\n\n      <div>\n        <p>\n          Availing himself of the mild, summer-cool weather that now reigned in these latitudes, and in preparation for the peculiarly active pursuits shortly to be anticipated, Perth, the begrimed, blistered old blacksmith, had not removed his portable forge to the hold again, after concluding his contributory work for Ahab's leg, but still retained it on deck, fast lashed to ringbolts by the foremast; being now almost incessantly invoked by the headsmen, and harpooneers, and bowsmen to do some little job for them; altering, or repairing, or new shaping their various weapons and boat furniture. Often he would be surrounded by an eager circle, all waiting to be served; holding boat-spades, pike-heads, harpoons, and lances, and jealously watching his every sooty movement, as he toiled. Nevertheless, this old man's was a patient hammer wielded by a patient arm. No murmur, no impatience, no petulance did come from him. Silent, slow, and solemn; bowing over still further his chronically broken back, he toiled away, as if toil were life itself, and the heavy beating of his hammer the heavy beating of his heart. And so it was.\xe2\x80\x94Most miserable! A peculiar walk in this old man, a certain slight but painful appearing yawing in his gait, had at an early period of the voyage excited the curiosity of the mariners. And to the importunity of their persisted questionings he had finally given in; and so it came to pass that every one now knew the shameful story of his wretched fate. Belated, and not innocently, one bitter winter's midnight, on the road running between two country towns, the blacksmith half-stupidly felt the deadly numbness stealing over him, and sought refuge in a leaning, dilapidated barn. The issue was, the loss of the extremities of both feet. Out of this revelation, part by part, at last came out the four acts of the gladness, and the one long, and as yet uncatastrophied fifth act of the grief of his life's drama. He was an old man, who, at the age of nearly sixty, had postponedly encountered that thing in sorrow's technicals called ruin. He had been an artisan of famed excellence, and with plenty to do; owned a house and garden; embraced a youthful, daughter-like, loving wife, and three blithe, ruddy children; every Sunday went to a cheerful-looking church, planted in a grove. But one night, under cover of darkness, and further concealed in a most cunning disguisement, a desperate burglar slid into his happy home, and robbed them all of everything. And darker yet to tell, the blacksmith himself did ignorantly conduct this burglar into his family's heart. It was the Bottle Conjuror! Upon the opening of that fatal cork, forth flew the fiend, and shrivelled up his home. Now, for prudent, most wise, and economic reasons, the blacksmith's shop was in the basement of his dwelling, but with a separate entrance to it; so that always had the young and loving healthy wife listened with no unhappy nervousness, but with vigorous pleasure, to the stout ringing of her young-armed old husband's hammer; whose reverberations, muffled by passing through the floors and walls, came up to her, not unsweetly, in her nursery; and so, to stout Labor's iron lullaby, the blacksmith's infants were rocked to slumber. Oh, woe on woe! Oh, Death, why canst thou not sometimes be timely? Hadst thou taken this old blacksmith to thyself ere his full ruin came upon him, then had the young widow had a delicious grief, and her orphans a truly venerable, legendary sire to dream of in their after years; and all of them a care-killing competency.\n        </p>\n      </div>\n  </body>\n</html>"
```

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Data Holdings](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963703/MAST+Data+Collection+Overview)  
Unable to load page tree. It seems that you do not have permission to view the root page.
##### Space shortcuts
* [TESS Archive Manual](https://outerspace.stsci.edu/spaces/TESS/pages/14562808/TESS+Archive+Manual)
* [FIMS-SPEAR Manual](https://outerspace.stsci.edu/spaces/SPEARFIMS/pages/183798103/FIMS-SPEAR+Manual)  
* [Archive Support](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94963058/Archive+Support "Archive Support")
* [MAST Pro Tips](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/286852358/MAST+Pro+Tips "MAST Pro Tips")
* [Portal Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/94962825/Portal+Guide "Portal Guide")
* [JWST Archive Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771318/JWST+Archive+Manual "JWST Archive Manual")
* [Quick Start Guide](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771319/Quick+Start+Guide "Quick Start Guide")
* [Field Guide to JWST Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771321/Field+Guide+to+JWST+Data "Field Guide to JWST Data")
* [Tutorials](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771352/Tutorials "Tutorials")
* [Using the MAST Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771353/Using+the+MAST+Portal "Using the MAST Portal")
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal "Using the Engineering Data Portal")
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs "Using MAST APIs")
* [API Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search "API Advanced Search")
* [API Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download "API Curl Download")
* [API for JWST Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata "API for JWST Metadata")
* [API for JWST Science Pixels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113031/API+for+JWST+Science+Pixels "API for JWST Science Pixels")
* [Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API "Basics of an API")
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
* [API Advanced Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/153686876/API+Advanced+Search "API Advanced Search")
* [API Curl Download](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771439/API+Curl+Download "API Curl Download")
* [API for JWST Metadata](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata "API for JWST Metadata")
* [API for JWST Science Pixels](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113031/API+for+JWST+Science+Pixels "API for JWST Science Pixels")
* [Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API "Basics of an API")
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
* [Public AWS Data](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/183797545/Public+AWS+Data "Public AWS Data")
* [CaSSI Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168331/CaSSI+Manual "CaSSI Manual")
* [JWST Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/333677644/JWST+Mission+Products "JWST Mission Products")
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
This guide serves as a basic introduction to the syntax and structure of making an API call. Where possible, MAST APIs adhere to the syntax and structure described here.
**On this page...**
* 1[Types of HTTP Requests](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-TypesofHTTPRequests)
* 1.1[GET](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-GET)
* 1.1.1[Example API call with GET](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ExampleAPIcallwithGET)
* 1.2[POST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-POST)
* 1.2.1[Example API call with POST](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ExampleAPIcallwithPOST)
* 2[HTTP Responses](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-HTTPResponses)
* 2.1[Example Responses](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ExampleResponses)
* 3[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113032/Basics+of+an+API#BasicsofanAPI-ForFurtherReading...)  
APIs, or Application Programming Interfaces, are a collection of services (sometimes referred to as routes or endpoints) aimed at providing programmatic access to some data, feature, or functionality. It is common for APIs to be designed around a particular product, idea, or function, often grouping related services together. Each service is designed as an  system, i.e. "you submit a request for something, or to do something, and receive a response". A simple playground for trying out sample HTTP requests/responses is . An alternative playground with curl and python examples is
Once an API is served by a host, all services become available as accessible HTTP URLs. To make an HTTP request to a service, one provides the URL name, and any allowed optional input parameters. Additional information, e.g. authorization information, or intended request format, can also be attached in the header of your request. HTTP responses typically, but not always, will return JSON objects containing the result of the API service call.

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests"} -->
The two most common types of requests are GET and POST requests, but other **scheme://host_domain/path** , e.g. <https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html>.

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "GET"} -->
GET requests are simple requests to retrieve some data. Input parameters are often referred to as **query parameters** , and can be appended to the end of a URL by a **?** , with additional parameters added with an **&** , e.g. the syntax is **url?parameter=value &parameter=value**. Alternatively, when using a library to submit the request, they can be supplied separately from the URL. See  or  for an example.

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "GET", "Header 3": "Example API call with GET"} -->
Example GET HTTP requests with a variety of libraries.
**web browser** - can only make GET requests
Paste into browser url bar:
```
# parameters in url
curl -X GET "https://httpbin.org/get?x=5&y=hello"

# parameters supplied
curl -X GET "https://httpbin.org/get" -G -d 'x=5' -d 'y=hello'
```  
```
# parameters in url
http get "https://httpbin.org/get?x=5&y=hello"

# parameters supplied
http get "https://httpbin.org/get" x==5 y==hello
```  
**Python**
```
# parameters in url
import requests
r = requests.get("https://httpbin.org/get?x=5&y=hello")

# parameters supplied
r = requests.get("https://httpbin.org/get", params={"x": 5, "y": "hello"})
```

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "POST"} -->
POST requests are requests to retrieve or change some data. While similar to GET requests, they differ in a few ways. One, the input parameters are not appended to the end of the URL as in GET requests, and two, they cannot be submitted by the url bar of a front-end web browser. Input parameters are instead passed as form, JSON, or dictionary parameters in the request itself, and are often referred to as **data, form, or json parameters**. See

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Types of HTTP Requests", "Header 2": "POST", "Header 3": "Example API call with POST"} -->
Example POST HTTP requests with a variety of libraries.
```
# as a form
curl -X POST "https://httpbin.org/post" -d 'x=5' -d 'y=hello'

# as a JSON
curl -X POST "https://httpbin.org/post" -d 'x=5' -d 'y=hello' -H 'Content-Type: application/json'
```  
```
# as a form
http post "https://httpbin.org/post" x=5 y=hello -f

# as a JSON
http post "https://httpbin.org/post" x=5 y=hello
```  
**Python**
```
# as a form
import requests
r = requests.post("https://httpbin.org/post", data={"x": 5, "y": "hello"})

# as a JSON
r = requests.post("https://httpbin.org/post", json={"x":5, "y":"hello"})
```

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "HTTP Responses"} -->
After you make a request, you generally receive an HTTP response. Like requests, HTTP responses have headers, providing contextual information, and a body content with output response data. The success or failure of an HTTP response is indicated with a status code. A successful response usually has a status code of **200**. Other status codes indicate the type of problem that occurred. For example, a status code of **404** means the requested URL does not exist. See **500** means something has gone wrong on the server that has not been accounted for, or is an uncaught error.
HTTP response data can be in a wide variety of formats. These formats are called Mime-Types and are usually specified in the Content-Type field of the response header, which indicates the type of content found in the response. For APIs, a common response data format is JSON, which has a Content-Type of "**application/json** ". Other example formats might be plain text, html, or binary data such as images or files. See

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "HTTP Responses", "Header 2": "Example Responses"} -->
Examples of response data from the browser or from specific libraries. Most of the examples shown here highlight a JSON response format. See **curl** ,
**Python**
When you send a request in Python, you get a Response object back. The raw body content is found in the **r.content** attribute. If the response is in JSON format, you can conveniently convert the content to JSON with the **r.json()** method. The following code block shows an example response for the example POST request:  **r=requests.post(" https://httpbin.org/json")**
**example python JSON response**
```
# send the request and get a response
r = requests.post("https://httpbin.org/json")
r
<Response [200]>

# get the JSON response data
r.json()
{'slideshow': {'author': 'Yours Truly',
'date': 'date of publication',
'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'},
{'items': ['Why <em>WonderWidgets</em> are great',
'Who <em>buys</em> WonderWidgets'],
'title': 'Overview',
'type': 'all'}],
'title': 'Sample Slide Show'}}
```  
Here is an example response of content that is html instead of JSON, to highlight extracting the raw body content instead, from:
`r = requests.post("https://httpbin.org/html")`
See **text/html.**
**example python html response**
```
# send the request and get a response
r = requests.post("https://httpbin.org/html")
r
<Response [200]>

# get the HTML content
r.content
b"<!DOCTYPE html>\n<html>\n  <head>\n  </head>\n  <body>\n      <h1>Herman Melville - Moby-Dick</h1>\n\n      <div>\n        <p>\n          Availing himself of the mild, summer-cool weather that now reigned in these latitudes, and in preparation for the peculiarly active pursuits shortly to be anticipated, Perth, the begrimed, blistered old blacksmith, had not removed his portable forge to the hold again, after concluding his contributory work for Ahab's leg, but still retained it on deck, fast lashed to ringbolts by the foremast; being now almost incessantly invoked by the headsmen, and harpooneers, and bowsmen to do some little job for them; altering, or repairing, or new shaping their various weapons and boat furniture. Often he would be surrounded by an eager circle, all waiting to be served; holding boat-spades, pike-heads, harpoons, and lances, and jealously watching his every sooty movement, as he toiled. Nevertheless, this old man's was a patient hammer wielded by a patient arm. No murmur, no impatience, no petulance did come from him. Silent, slow, and solemn; bowing over still further his chronically broken back, he toiled away, as if toil were life itself, and the heavy beating of his hammer the heavy beating of his heart. And so it was.\xe2\x80\x94Most miserable! A peculiar walk in this old man, a certain slight but painful appearing yawing in his gait, had at an early period of the voyage excited the curiosity of the mariners. And to the importunity of their persisted questionings he had finally given in; and so it came to pass that every one now knew the shameful story of his wretched fate. Belated, and not innocently, one bitter winter's midnight, on the road running between two country towns, the blacksmith half-stupidly felt the deadly numbness stealing over him, and sought refuge in a leaning, dilapidated barn. The issue was, the loss of the extremities of both feet. Out of this revelation, part by part, at last came out the four acts of the gladness, and the one long, and as yet uncatastrophied fifth act of the grief of his life's drama. He was an old man, who, at the age of nearly sixty, had postponedly encountered that thing in sorrow's technicals called ruin. He had been an artisan of famed excellence, and with plenty to do; owned a house and garden; embraced a youthful, daughter-like, loving wife, and three blithe, ruddy children; every Sunday went to a cheerful-looking church, planted in a grove. But one night, under cover of darkness, and further concealed in a most cunning disguisement, a desperate burglar slid into his happy home, and robbed them all of everything. And darker yet to tell, the blacksmith himself did ignorantly conduct this burglar into his family's heart. It was the Bottle Conjuror! Upon the opening of that fatal cork, forth flew the fiend, and shrivelled up his home. Now, for prudent, most wise, and economic reasons, the blacksmith's shop was in the basement of his dwelling, but with a separate entrance to it; so that always had the young and loving healthy wife listened with no unhappy nervousness, but with vigorous pleasure, to the stout ringing of her young-armed old husband's hammer; whose reverberations, muffled by passing through the floors and walls, came up to her, not unsweetly, in her nursery; and so, to stout Labor's iron lullaby, the blacksmith's infants were rocked to slumber. Oh, woe on woe! Oh, Death, why canst thou not sometimes be timely? Hadst thou taken this old blacksmith to thyself ere his full ruin came upon him, then had the young widow had a delicious grief, and her orphans a truly venerable, legendary sire to dream of in their after years; and all of them a care-killing competency.\n        </p>\n      </div>\n  </body>\n</html>"
```

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [MAST Data Holdings](https://outerspace.stsci.edu/spaces/MASTDATA/pages/94963703/MAST+Data+Collection+Overview)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 17 END -->

