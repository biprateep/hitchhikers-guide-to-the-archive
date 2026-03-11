Select a definitionhst_api jwst_api classy_api ullyses_api roman_api roman_spectra_api all_missions_api iue_api roman_cgi_api
# FastAPI```
 0.1.0 
```
```
OAS 3.1
```

[ hst_api_openapi.json](https://mast.stsci.edu/search/docs/hst_api_openapi.json)
### [Hubble Search](https://mast.stsci.edu/search/docs/#/Hubble%20Search)
POST
[/search/hst/api/v0.1/search](https://mast.stsci.edu/search/docs/#/Hubble%20Search/SearchHandler_post_search_hst_api_v0_1_search_post)
Hubble metadata search
### [default](https://mast.stsci.edu/search/docs/#/default)
GET
[/search/hst/api/v0.1/get_image_list](https://mast.stsci.edu/search/docs/#/default/SearchHandler_get_image_list_search_hst_api_v0_1_get_image_list_get)
Searchhandler.Get Image List
### [HST Image Preview](https://mast.stsci.edu/search/docs/#/HST%20Image%20Preview)
GET
[/search/hst/api/v0.1/get_image_preview](https://mast.stsci.edu/search/docs/#/HST%20Image%20Preview/SearchHandler_get_image_preview_search_hst_api_v0_1_get_image_preview_get)
Get image preview for a fileSetName
### [HST Image Thumbnail](https://mast.stsci.edu/search/docs/#/HST%20Image%20Thumbnail)
GET
[/search/hst/api/v0.1/get_image_thumbnail](https://mast.stsci.edu/search/docs/#/HST%20Image%20Thumbnail/SearchHandler_get_image_thumbnail_search_hst_api_v0_1_get_image_thumbnail_get)
Get image thumbnail for a fileSetName
### [Hubble Data Download](https://mast.stsci.edu/search/docs/#/Hubble%20Data%20Download)
GET
[/search/hst/api/v0.1/list_products](https://mast.stsci.edu/search/docs/#/Hubble%20Data%20Download/SearchHandler_list_products_search_hst_api_v0_1_list_products_get)
List Hubble products associated with one or more datasets
POST
[/search/hst/api/v0.1/post_list_products](https://mast.stsci.edu/search/docs/#/Hubble%20Data%20Download/SearchHandler_post_list_products_search_hst_api_v0_1_post_list_products_post)
List Hubble products associated with one or more filesets
GET
[/search/hst/api/v0.1/retrieve_product](https://mast.stsci.edu/search/docs/#/Hubble%20Data%20Download/SearchHandler_retrieve_product_search_hst_api_v0_1_retrieve_product_get)
Download Hubble dataset product by name
### [Backwards-compatible Hubble Classic Search](https://mast.stsci.edu/search/docs/#/Backwards-compatible%20Hubble%20Classic%20Search)
GET
[/search/hst/api/v0.1/get_classic_search](https://mast.stsci.edu/search/docs/#/Backwards-compatible%20Hubble%20Classic%20Search/SearchHandler_classic_get_search_hst_api_v0_1_get_classic_search_get)
Hubble metadata search using backwards-compatible classic GET format
POST
[/search/hst/api/v0.1/post_classic_search](https://mast.stsci.edu/search/docs/#/Backwards-compatible%20Hubble%20Classic%20Search/SearchHandler_classic_post_search_hst_api_v0_1_post_classic_search_post)
Hubble metadata search using backwards-compatible classic POST format
#### Schemas
ClassicSearchParams
Expand all**object**
DatasetIDs
Expand all**object**
DatasetProduct
Expand all**object**
DatasetProducts
Expand all**object**
HTTPValidationError
Expand all**object**
SearchParams
Expand all**object**
SearchResultItem
Expand all**object**
SearchResults
Expand all**object**
ValidationError
Expand all**object**
[](https://validator.swagger.io/validator/debug?url=https%3A%2F%2Fmast.stsci.edu%2Fsearch%2Fdocs%2Fhst_api_openapi.json)
