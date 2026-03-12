---
title: "MAST Document"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata"
date_accessed: "2026-03-11T11:36:54.189045"
---

<!-- CHUNK 1 START -->
The Jdaviz.MAST API provides programmatic access to a variety of parameters and metadata related to JWST data products and observations. This article provides a brief summary of the available API endpoints. See the complete [API documentation](https://mast.stsci.edu/viz/docs/index.html) for more details.
**On this page...**
* 1[The Jdaviz.MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-TheJdaviz.MASTAPI)
* 2[Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-BasicsofanAPI)
* 3[Accessing Observation Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingObservationParameters)
* 4[Accessing Science Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingScienceInstrumentKeywords)
* 5[Accessing Related Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingRelatedDataProducts)
* 6[Accessing Metadata Information](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingMetadataInformation)
* 6.1[Science Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-ScienceInstrumentKeywords)
* 6.2[Engineering Mnemonics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-EngineeringMnemonics)
* 7[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "The Jdaviz.MAST API"} -->
The global URL for the Jdaviz.MAST API is **https://mast.stsci.edu/viz/api/v0.1/** , which has the following service endpoints:
* **parameters** : return observation parameters
* **keywords/search** : return instrument keywords
* **products** : return related data products
* **info/keywords** : return instrument keyword metadata
* **info/mnemonics** : return engineering mnemonic metadata

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Basics of an API"} -->
The examples on this page assume basic knowledge of APIs and making HTTP requests. For a refresher, see the [Basics of an API](https://outerspace.stsci.edu/display/DraftMASTDOCS/Basics+of+an+API). Unless otherwise specified, all API calls and URLS on this page are HTTP GET requests.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "Accessing Observation Parameters"} -->
You can access the observations parameters for any JWST data product given a MAST DATA URI. Use the endpoint **https://mast.stsci.edu/viz/api/v0.1/parameters** , which accepts a URI query parameter with syntax "**uri=[MAST_DATA_URI]** ". See the [Parameters API Documentation](https://mast.stsci.edu/viz/docs/parameters.html) for complete details. The parameters returned by this endpoint, in JSON format, are the same as the [Portal Product File Details](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Download+Basket+v1.1#id-.DownloadBasketv1.1-FileDetails).
**Example** : <https://mast.stsci.edu/viz/api/v0.1/parameters?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits>
**Example Output** Expand source
```
{
"dataproduct_type":"cube",
"calib_level":3,
"obs_collection":"JWST",
"obs_id":"jw01039-o004_t001_miri_ch3-long",
"obsType":"PRIME",
"intentType":"science",
"target_name":"NGC6552",
"s_ra":270.0302116666667,
"s_dec":66.61509722222222,
"mtFlag":false,
"t_min":59706.50301039352,
"t_max":59706.51692592593,
"t_exptime":555.008,
"wavelength_region":null,
"instrument_name":"MIRI",
"filters":null,
"em_min":null,
"em_max":null,
"pol_states":null,
"target_classification":null,
"obs_title":"MIRI Detector Latent Image Characterization",
"t_obs_release":59774.8541666,
"proposal_pi":"Dicken, Daniel",
"proposal_id":"1039",
"proposal_type":"JWST",
"provenance_name":"CALJWST",
"project":"JWST",
"sequence_number":-999,
"s_region":"POLYGON -89.975360290000026 66.59444259 -89.967807240000013 66.59444259 -89.967807240000212 66.5955008252255 -89.966547260000027 66.5955008 ...",
"jpegURL":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_s3d.jpg",
"dataURL":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_s3d.fits",
"dataRights":"PUBLIC",
"metaDataRights":"PUBLIC",
"srcDen":null,
"obsid":83209967,
"objID":165643579
}
```

<!-- CHUNK 4 END -->

<!-- CHUNK 5 START -->
<!-- Metadata: {"Header 1": "Accessing Science Instrument Keywords"} -->
You can access the science instrument (SI) keywords for any JWST data product given a MAST DATA URI or product filename. Use the endpoint **https://mast.stsci.edu/viz/api/v0.1/keywords/search** , which accepts a URI query parameter with syntax "**uri=[MAST_DATA_URI]** ". See the [Keywords API Documentation](https://mast.stsci.edu/viz/docs/jwst_keywords.html) for complete details. This endpoint returns the SI keywords in JSON format.
**Example** : <https://mast.stsci.edu/viz/api/v0.1/keywords/search?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits>
**Example Output** Expand source
```
{
"ArchiveFileID":5924537,
"filename":"jw01039-o004_t001_miri_ch3-long_x1d.fits",
"fileSetName":"jw01039-o004_t001_miri",
"productLevel":"3",
"act_id":"01",
"apername":"MIRIFU_CHANNEL1A",
"asnpool":"jw01039_20220702t204540_pool.csv",
"asntable":"jw01039-o004_20220702t204540_spec3_001_asn.json",
"bartdelt":-198.8018335774541,
"bendtime":59706.5108916159,
"bkgdtarg":"f",
"bkglevel":null,
"bkgsub":null,
"bmidtime":59706.51049015499,
"bstrtime":59706.51008869405,
"category":"COM",
"cont_id":null,
"datamode":7,
"dataprob":"f",
"date":"2022-07-02T22:16:43.890000",
"date_mjd":59762.92828576389,
"date_end":"2022-05-07T12:24:21.760000",
"date_end_mjd":59706.516918518515,
"date_obs":"2022-05-07T12:04:20.097999",
"date_obs_mjd":59706.50301037037,
"detector":"MIRIFULONG",
"drpfrms1":0,
"drpfrms3":0,
"duration":555.008,
"effexptm":555.008,
"effinttm":69.376,
"eng_qual":"OK",
"exp_type":"MIR_MRS",
"expcount":1,
"expend":59706.51691851852,
"expmid":59706.5099846412,
"exposure":6,
"expripar":"PRIME",
"expstart":59706.50301039352,
"fastaxis":1,
"filter":null,
"frmdivsr":1,
"gainfact":null,
"gdstarid":"N4E8004471",
"groupgap":0,
"gs_dec":66.77963507876898,
"gs_mag":15.89793395996094,
"gs_order":1,
"gs_ra":269.9185220667708,
"gsendtim":"2022-05-07T12:01:50.338000",
"gsendtim_mjd":59706.50127703704,
"gsstrttm":"2022-05-07T12:00:21.250000",
"gsstrttm_mjd":59706.50024594907,
"gs_udec":0.000722415601193118,
"gs_umag":0.05136068910360336,
"gs_ura":0.000455751810140842,
"helidelt":-199.7010667808354,
"hendtime":59706.51088120813,
"hga_move":"f",
"hmidtime":59706.51047974721,
"hstrtime":59706.51007828626,
"instrume":"MIRI",
"intarget":"f",
"is_psf":null,
"lamp":"OFF",
"mu_dec":0.0,
"mu_epoch":"2015-07-02T12:00:00",
"mu_epoch_mjd":57205.5,
"mu_ra":0.0,
"nexposur":8,
"nextend":null,
"nframes":1,
"ngroups":25,
"nints":1,
"nresets":1,
"nrststrt":0,
"nsamples":1,
"numdthpt":8,
"nwfsest":59706.90709584491,
"obs_id":"V01039004001P0000000002101",
"observtn":4,
"obslabel":"Latent soak Imager F560W - Position 3",
"origin":"STSCI",
"pcs_mode":"FINEGUIDE",
"pi_name":"Dicken,
Daniel",
"pps_aper":"MIRIM_ILLUM",
"prd_ver":"PRDOPSSOC-054",
"program":1039,
"prop_dec":66.61509722222222,
"prop_ra":270.0302116666667,
"pwfseet":59705.6527646875,
"readpatt":"FASTR1",
"sca_num":494,
"scicat":null,
"sdp_ver":"2022_2a",
"selfref":null,
"seq_id":"1",
"slowaxis":2,
"subarray":"FULL",
"subcat":"MIRI",
"subsize1":1032,
"subsize2":1024,
"substrt1":1,
"substrt2":1,
"targ_dec":66.61509722222222,
"targ_ra":270.0302116666667,
"targname":"NGC 6552",
"targoopp":"f",
"targprop":"NGC-6552",
"targtype":"FIXED",
"targudec":0.1,
"targura":0.1,
"telescop":"JWST",
"template":"MIRI External Flat",
"tframe":2.77504,
"tgroup":2.77504,
"timesys":"UTC",
"title":"MIRI Detector Latent Image Characterization",
"tsample":10.0,
"tsovisit":"f",
"visit":1,
"visit_id":"01039004001",
"visitend":"2022-05-07T12:25:40.864000",
"visitend_mjd":59706.5178340625,
"visitgrp":"02",
"visitsta":"SUCCESSFUL",
"visitype":"PRIME_TARGETED_FIXED",
"vststart":"2022-05-07T11:55:26.338000",
"vststart_mjd":59706.496832592595,
"xoffset":5.332307520493426,
"yoffset":6.47702245978903,
"zerofram":"f",
"errtype":null,
"rois":null,
"roiw":null,
"wpower":null,
"wtype":null,
"datamodl":"MultiSpecModel",
"exp_only":"f",
"exsegnum":null,
"exsegtot":null,
"intstart":null,
"intend":null,
"date_beg":"2022-05-07T12:04:20.098000",
"date_beg_mjd":59706.50301037037,
"obsfoldr":"Latent observations",
"sctarate":-0.720384722948798,
"opmode":null,
"osf_file":"2022127T123106704_002_osf.xml",
"expsteng":null,
"expsteng_mjd":null,
"masterbg":null,
"scatfile":null,
"srctyapt":"UNKNOWN",
"tcatfile":null,
"texptime":null,
"patt_num":6,
"pattsize":null,
"patttype":"4-POINT-SETS",
"pridtpts":null,
"subpxpts":null,
"crowdfld":"f",
"engqlptg":"CALCULATED_TRACK_TR_202111",
"oss_ver":"8.4.2",
"noutputs":null,
"gs_v3_pa":223.1384655404019,
"dirimage":null,
"pixfrac":null,
"pxsclrt":null,
"segmfile":null,
"va_dec":66.59280573616425,
"va_ra":270.039912295606,
"compress":null,
"bkgmeth":null,
"s_region":null,
"cal_ver":"1.5.3",
"cal_vcs":"RELEASE",
"crds_ctx":"jwst_0913.pmap",
"crds_ver":"11.16.3",
"band":"LONG",
"cccstate":"OPEN",
"channel":"3",
"coronmsk":null,
"pattstrt":null,
"spat_num":null,
"spatnstp":null,
"spatstep":null,
"spcoffst":null,
"spec_num":null,
"specnstp":null,
"specstep":null,
"sptoffst":null,
"mirngrps":null,
"mirnfrms":null,
"dithdirc":"POSITIVE",
"dithopfr":"EXTENDED-SOURCE",
"dithpnts":null,
"dsetstrt":null,
"mrsprchn":null,
"numdsets":null,
"pattnpts":null,
"detmode":null,
"cmd_tsel":null,
"fpe_side":"A",
"ice_side":"A",
"fileSize":190080,
"checksum":"988f90cad25ebfcae20481d6d7aa35e1",
"ingestStartDate":"2022-07-02T22:17:45.037000",
"ingestStartDate_mjd":59762.928993472226,
"ingestCompletionDate":"2022-07-02T22:17:59.651000",
"ingestCompletionDate_mjd":59762.92916261574,
"FileTypeID":63,
"publicReleaseDate":"2022-07-14T20:30:00",
"publicReleaseDate_mjd":59774.854166666664,
"isRestricted":false,
"isItar":false,
"isStale":false,
"FileSetId":876299
}
```

<!-- CHUNK 5 END -->

<!-- CHUNK 6 START -->
<!-- Metadata: {"Header 1": "Accessing Related Data Products"} -->
You can access all related data product for any JWST data product given a MAST DATA URI. Use the endpoint **https://mast.stsci.edu/viz/api/v0.1/products** , which accepts a **URI** query parameter with syntax "**uri=[MAST_DATA_URI]** ", and **level** query parameter, indicating the MAST Calibration Level of the products. See the [Products API Documentation](https://mast.stsci.edu/viz/docs/products.html) for complete details. This endpoint returns a list of data products for a given JWST observation ID. Each item in the list is a dictionary of data product parameters.
**Example** : [https://mast.stsci.edu/viz/api/v0.1/products?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits&level=3](https://mast.stsci.edu/viz/api/v0.1/products?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits&level=3)
**Example Output** Expand source
```
{
"jw01039-o004_t001_miri_ch3-long":[
{
"obsID":83209967,
"obs_collection":"JWST",
"obs_id":"jw01039-o004_t001_miri_ch3-long",
"dataproduct_type":"cube",
"type":"D",
"productType":"SCIENCE",
"productGroupDescription":"Minimum Recommended Products",
"productSubGroupDescription":"S3D",
"productDocumentationURL":null,
"project":"CALJWST",
"prvversion":"1.5.3",
"proposal_id":"1039",
"dataURI":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_s3d.fits",
"productFilename":"jw01039-o004_t001_miri_ch3-long_s3d.fits",
"description":"exposure/target (L2b/L3): 3D image of spectrum",
"size":370405440,
"parent_obsid":83209967,
"dataRights":"PUBLIC",
"calib_level":3,
"exp_type":"MIR_MRS",
"template":"MIRI External Flat"
},
{
"obsID":83209967,
"obs_collection":"JWST",
"obs_id":"jw01039-o004_t001_miri_ch3-long",
"dataproduct_type":"cube",
"type":"D",
"productType":"SCIENCE",
"productGroupDescription":"Minimum Recommended Products",
"productSubGroupDescription":"X1D",
"productDocumentationURL":null,
"project":"CALJWST",
"prvversion":"1.5.3",
"proposal_id":"1039",
"dataURI":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits",
"productFilename":"jw01039-o004_t001_miri_ch3-long_x1d.fits",
"description":"exposure/target (L2b/L3): 1D extracted spectrum",
"size":190080,
"parent_obsid":83209967,
"dataRights":"PUBLIC",
"calib_level":3,
"exp_type":"MIR_MRS",
"template":"MIRI External Flat"
}
]
}
```

<!-- CHUNK 6 END -->

<!-- CHUNK 7 START -->
<!-- Metadata: {"Header 1": "Accessing Metadata Information"} -->
You can access metadata information about the JWST Science Instrument (SI) keywords and Engineering Mnemonics using the API endpoint <https://mast.stsci.edu/viz/api/v0.1/info/>. See the [Info API Documentation](https://mast.stsci.edu/viz/docs/info.html) for complete details.

<!-- CHUNK 7 END -->

<!-- CHUNK 8 START -->
<!-- Metadata: {"Header 1": "Accessing Metadata Information", "Header 2": "Science Instrument Keywords"} -->
To access the metadata information about the science instrument keywords, use the endpoint **https://mast.stsci.edu/viz/api/v0.1/info/keywords/**. You can optionally specify a **name** query parameter, specifying the name of the keyword you wish to return information on. This endpoint returns the Instrument Keyword schema information in JSON format, the same information as displayed in the [JWST Keyword Dictionary](https://mast.stsci.edu/portal/Mashup/Clients/jwkeywords/index.html).
**Example - Return all keywords** : https://mast.stsci.edu/viz/api/v0.1/info/keywords/
**Example Output** Expand source
```
{
"all.dither.schema.json": {
"total_points": {
"fits_keyword": "NUMDTHPT",
"title": "Total number of points in dither pattern",
"description": "Total number of points in entire dither pattern",
"type": "integer",
"units": "",
"example": "3",
"default_value": "1",
"source": "Proposal and Planning System (PPS)",
"sw_source": "",
"calculation": "maximum(PPS:exposures.dither_point_index) in pattern (for program, observation, and pattern dither_id)",
"destination": [
"ScienceCommon.numdthpt"
],
"sql_dtype": "int",
"si": "All",
"mode": "All",
"level": "1b",
"fits_hdu": "PRIMARY",
"section": "Dither",
"misc": ""
},
"position_number": {
"fits_keyword": "PATT_NUM",
"title": "Position number within dither pattern",
"description": "Position number within dither pattern",
"type": "integer",
"units": "",
"example": "1",
"default_value": "1",
"source": "Proposal and Planning System (PPS)",
"sw_source": "PPS:exposures.dither_point_index",
"calculation": "",
"destination": [
"ScienceCommon.patt_num"
],
"sql_dtype": "smallint",
"si": "All",
"mode": "All",
"level": "1b",
"fits_hdu": "PRIMARY",
"section": "Dither",
"misc": ""
},
...
}


```  
**Example - Return a single keyword** : https://mast.stsci.edu/viz/api/v0.1/info/keywords?name=BKGDTARG
**Example Output** Expand source
```
{
"science.observation.schema.json": {
"bkgdtarg": {
"fits_keyword": "BKGDTARG",
"title": "Background target",
"description": "Indicates whether the proposer flagged the target or target field contained in the exposure to be used as a background target for other exposures.",
"type": "boolean",
"units": "",
"example": "T",
"default_value": "F",
"source": "",
"sw_source": "PPS:dms_target_view.background",
"calculation": "",
"destination": [
"ScienceCommon.bkgdtarg"
],
"sql_dtype": "nchar(1)",
"si": "Multiple",
"mode": "All",
"level": "1b",
"fits_hdu": "PRIMARY",
"section": "Observation identifiers",
"misc": ""
}
}
}
```

<!-- CHUNK 8 END -->

<!-- CHUNK 9 START -->
<!-- Metadata: {"Header 1": "Accessing Metadata Information", "Header 2": "Engineering Mnemonics"} -->
To access the metadata information about the engineering mnemonics, use the endpoint **https://mast.stsci.edu/viz/api/v0.1/info/mnemonics/**. You can optionally specify a **name** query parameter, specifying the name of the mnemonic you wish to return information on. This endpoint returns the mnemonic schema information in JSON format, the same information as displayed in the [JWST Engineering Portal](https://mast.stsci.edu/portal_jwst/Mashup/Clients/jwstedb/jwstedb.html).
**Example - Return all mnemonics** : https://mast.stsci.edu/viz/api/v0.1/info/mnemonics/
**Example Output** Expand source
```
{
"data": [
{
"subsystem": "FOS",
"tlmMnemonic": "FGDP_ICDH_STATE",
"tlmIdentifier": 570000,
"description": "ICDH state",
"sqlDataType": "varchar",
"unit": ""
},
{
"subsystem": "FOS",
"tlmMnemonic": "FGDP_INRS_FPE_A1FL",
"tlmIdentifier": 570067,
"description": "NIRSpec FPE ASIC1 Files Loaded Status",
"sqlDataType": "varchar",
"unit": ""
},
{...},
{...},
]
}
```  
**Example - Return a single mnemonic** : https://mast.stsci.edu/viz/api/v0.1/info/mnemonics/?name=so_zfxposns
**Example Output** Expand source
```
{
"data": [
{
"subsystem": "OTE",
"tlmMnemonic": "SO_ZFXPOSNS",
"tlmIdentifier": 81669,
"description": "x axis position of the FSM",
"sqlDataType": "float",
"unit": "rad"
}
]
}
```

<!-- CHUNK 9 END -->

<!-- CHUNK 10 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs)  
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
* [Roman Mission Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/282168347/Roman+Mission+Products "Roman Mission Products")
* [HST Classic Migration Manual](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172245/HST+Classic+Migration+Manual "HST Classic Migration Manual")
* [HST Basic Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172246/HST+Basic+Search "HST Basic Search")
* [Time-Tag Search](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/168693279/Time-Tag+Search "Time-Tag Search")
* [New Features](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/158172268/New+Features "New Features")  
The Jdaviz.MAST API provides programmatic access to a variety of parameters and metadata related to JWST data products and observations. This article provides a brief summary of the available API endpoints. See the complete [API documentation](https://mast.stsci.edu/viz/docs/index.html) for more details.
**On this page...**
* 1[The Jdaviz.MAST API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-TheJdaviz.MASTAPI)
* 2[Basics of an API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-BasicsofanAPI)
* 3[Accessing Observation Parameters](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingObservationParameters)
* 4[Accessing Science Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingScienceInstrumentKeywords)
* 5[Accessing Related Data Products](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingRelatedDataProducts)
* 6[Accessing Metadata Information](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-AccessingMetadataInformation)
* 6.1[Science Instrument Keywords](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-ScienceInstrumentKeywords)
* 6.2[Engineering Mnemonics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-EngineeringMnemonics)
* 7[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/150113030/API+for+JWST+Metadata#APIforJWSTMetadata-ForFurtherReading...)

<!-- CHUNK 10 END -->

<!-- CHUNK 11 START -->
<!-- Metadata: {"Header 1": "The Jdaviz.MAST API"} -->
The global URL for the Jdaviz.MAST API is **https://mast.stsci.edu/viz/api/v0.1/** , which has the following service endpoints:
* **parameters** : return observation parameters
* **keywords/search** : return instrument keywords
* **products** : return related data products
* **info/keywords** : return instrument keyword metadata
* **info/mnemonics** : return engineering mnemonic metadata

<!-- CHUNK 11 END -->

<!-- CHUNK 12 START -->
<!-- Metadata: {"Header 1": "Basics of an API"} -->
The examples on this page assume basic knowledge of APIs and making HTTP requests. For a refresher, see the [Basics of an API](https://outerspace.stsci.edu/display/DraftMASTDOCS/Basics+of+an+API). Unless otherwise specified, all API calls and URLS on this page are HTTP GET requests.

<!-- CHUNK 12 END -->

<!-- CHUNK 13 START -->
<!-- Metadata: {"Header 1": "Accessing Observation Parameters"} -->
You can access the observations parameters for any JWST data product given a MAST DATA URI. Use the endpoint **https://mast.stsci.edu/viz/api/v0.1/parameters** , which accepts a URI query parameter with syntax "**uri=[MAST_DATA_URI]** ". See the [Parameters API Documentation](https://mast.stsci.edu/viz/docs/parameters.html) for complete details. The parameters returned by this endpoint, in JSON format, are the same as the [Portal Product File Details](https://outerspace.stsci.edu/display/DraftMASTDOCS/.Download+Basket+v1.1#id-.DownloadBasketv1.1-FileDetails).
**Example** : <https://mast.stsci.edu/viz/api/v0.1/parameters?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits>
**Example Output** Expand source
```
{
"dataproduct_type":"cube",
"calib_level":3,
"obs_collection":"JWST",
"obs_id":"jw01039-o004_t001_miri_ch3-long",
"obsType":"PRIME",
"intentType":"science",
"target_name":"NGC6552",
"s_ra":270.0302116666667,
"s_dec":66.61509722222222,
"mtFlag":false,
"t_min":59706.50301039352,
"t_max":59706.51692592593,
"t_exptime":555.008,
"wavelength_region":null,
"instrument_name":"MIRI",
"filters":null,
"em_min":null,
"em_max":null,
"pol_states":null,
"target_classification":null,
"obs_title":"MIRI Detector Latent Image Characterization",
"t_obs_release":59774.8541666,
"proposal_pi":"Dicken, Daniel",
"proposal_id":"1039",
"proposal_type":"JWST",
"provenance_name":"CALJWST",
"project":"JWST",
"sequence_number":-999,
"s_region":"POLYGON -89.975360290000026 66.59444259 -89.967807240000013 66.59444259 -89.967807240000212 66.5955008252255 -89.966547260000027 66.5955008 ...",
"jpegURL":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_s3d.jpg",
"dataURL":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_s3d.fits",
"dataRights":"PUBLIC",
"metaDataRights":"PUBLIC",
"srcDen":null,
"obsid":83209967,
"objID":165643579
}
```

<!-- CHUNK 13 END -->

<!-- CHUNK 14 START -->
<!-- Metadata: {"Header 1": "Accessing Science Instrument Keywords"} -->
You can access the science instrument (SI) keywords for any JWST data product given a MAST DATA URI or product filename. Use the endpoint **https://mast.stsci.edu/viz/api/v0.1/keywords/search** , which accepts a URI query parameter with syntax "**uri=[MAST_DATA_URI]** ". See the [Keywords API Documentation](https://mast.stsci.edu/viz/docs/jwst_keywords.html) for complete details. This endpoint returns the SI keywords in JSON format.
**Example** : <https://mast.stsci.edu/viz/api/v0.1/keywords/search?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits>
**Example Output** Expand source
```
{
"ArchiveFileID":5924537,
"filename":"jw01039-o004_t001_miri_ch3-long_x1d.fits",
"fileSetName":"jw01039-o004_t001_miri",
"productLevel":"3",
"act_id":"01",
"apername":"MIRIFU_CHANNEL1A",
"asnpool":"jw01039_20220702t204540_pool.csv",
"asntable":"jw01039-o004_20220702t204540_spec3_001_asn.json",
"bartdelt":-198.8018335774541,
"bendtime":59706.5108916159,
"bkgdtarg":"f",
"bkglevel":null,
"bkgsub":null,
"bmidtime":59706.51049015499,
"bstrtime":59706.51008869405,
"category":"COM",
"cont_id":null,
"datamode":7,
"dataprob":"f",
"date":"2022-07-02T22:16:43.890000",
"date_mjd":59762.92828576389,
"date_end":"2022-05-07T12:24:21.760000",
"date_end_mjd":59706.516918518515,
"date_obs":"2022-05-07T12:04:20.097999",
"date_obs_mjd":59706.50301037037,
"detector":"MIRIFULONG",
"drpfrms1":0,
"drpfrms3":0,
"duration":555.008,
"effexptm":555.008,
"effinttm":69.376,
"eng_qual":"OK",
"exp_type":"MIR_MRS",
"expcount":1,
"expend":59706.51691851852,
"expmid":59706.5099846412,
"exposure":6,
"expripar":"PRIME",
"expstart":59706.50301039352,
"fastaxis":1,
"filter":null,
"frmdivsr":1,
"gainfact":null,
"gdstarid":"N4E8004471",
"groupgap":0,
"gs_dec":66.77963507876898,
"gs_mag":15.89793395996094,
"gs_order":1,
"gs_ra":269.9185220667708,
"gsendtim":"2022-05-07T12:01:50.338000",
"gsendtim_mjd":59706.50127703704,
"gsstrttm":"2022-05-07T12:00:21.250000",
"gsstrttm_mjd":59706.50024594907,
"gs_udec":0.000722415601193118,
"gs_umag":0.05136068910360336,
"gs_ura":0.000455751810140842,
"helidelt":-199.7010667808354,
"hendtime":59706.51088120813,
"hga_move":"f",
"hmidtime":59706.51047974721,
"hstrtime":59706.51007828626,
"instrume":"MIRI",
"intarget":"f",
"is_psf":null,
"lamp":"OFF",
"mu_dec":0.0,
"mu_epoch":"2015-07-02T12:00:00",
"mu_epoch_mjd":57205.5,
"mu_ra":0.0,
"nexposur":8,
"nextend":null,
"nframes":1,
"ngroups":25,
"nints":1,
"nresets":1,
"nrststrt":0,
"nsamples":1,
"numdthpt":8,
"nwfsest":59706.90709584491,
"obs_id":"V01039004001P0000000002101",
"observtn":4,
"obslabel":"Latent soak Imager F560W - Position 3",
"origin":"STSCI",
"pcs_mode":"FINEGUIDE",
"pi_name":"Dicken,
Daniel",
"pps_aper":"MIRIM_ILLUM",
"prd_ver":"PRDOPSSOC-054",
"program":1039,
"prop_dec":66.61509722222222,
"prop_ra":270.0302116666667,
"pwfseet":59705.6527646875,
"readpatt":"FASTR1",
"sca_num":494,
"scicat":null,
"sdp_ver":"2022_2a",
"selfref":null,
"seq_id":"1",
"slowaxis":2,
"subarray":"FULL",
"subcat":"MIRI",
"subsize1":1032,
"subsize2":1024,
"substrt1":1,
"substrt2":1,
"targ_dec":66.61509722222222,
"targ_ra":270.0302116666667,
"targname":"NGC 6552",
"targoopp":"f",
"targprop":"NGC-6552",
"targtype":"FIXED",
"targudec":0.1,
"targura":0.1,
"telescop":"JWST",
"template":"MIRI External Flat",
"tframe":2.77504,
"tgroup":2.77504,
"timesys":"UTC",
"title":"MIRI Detector Latent Image Characterization",
"tsample":10.0,
"tsovisit":"f",
"visit":1,
"visit_id":"01039004001",
"visitend":"2022-05-07T12:25:40.864000",
"visitend_mjd":59706.5178340625,
"visitgrp":"02",
"visitsta":"SUCCESSFUL",
"visitype":"PRIME_TARGETED_FIXED",
"vststart":"2022-05-07T11:55:26.338000",
"vststart_mjd":59706.496832592595,
"xoffset":5.332307520493426,
"yoffset":6.47702245978903,
"zerofram":"f",
"errtype":null,
"rois":null,
"roiw":null,
"wpower":null,
"wtype":null,
"datamodl":"MultiSpecModel",
"exp_only":"f",
"exsegnum":null,
"exsegtot":null,
"intstart":null,
"intend":null,
"date_beg":"2022-05-07T12:04:20.098000",
"date_beg_mjd":59706.50301037037,
"obsfoldr":"Latent observations",
"sctarate":-0.720384722948798,
"opmode":null,
"osf_file":"2022127T123106704_002_osf.xml",
"expsteng":null,
"expsteng_mjd":null,
"masterbg":null,
"scatfile":null,
"srctyapt":"UNKNOWN",
"tcatfile":null,
"texptime":null,
"patt_num":6,
"pattsize":null,
"patttype":"4-POINT-SETS",
"pridtpts":null,
"subpxpts":null,
"crowdfld":"f",
"engqlptg":"CALCULATED_TRACK_TR_202111",
"oss_ver":"8.4.2",
"noutputs":null,
"gs_v3_pa":223.1384655404019,
"dirimage":null,
"pixfrac":null,
"pxsclrt":null,
"segmfile":null,
"va_dec":66.59280573616425,
"va_ra":270.039912295606,
"compress":null,
"bkgmeth":null,
"s_region":null,
"cal_ver":"1.5.3",
"cal_vcs":"RELEASE",
"crds_ctx":"jwst_0913.pmap",
"crds_ver":"11.16.3",
"band":"LONG",
"cccstate":"OPEN",
"channel":"3",
"coronmsk":null,
"pattstrt":null,
"spat_num":null,
"spatnstp":null,
"spatstep":null,
"spcoffst":null,
"spec_num":null,
"specnstp":null,
"specstep":null,
"sptoffst":null,
"mirngrps":null,
"mirnfrms":null,
"dithdirc":"POSITIVE",
"dithopfr":"EXTENDED-SOURCE",
"dithpnts":null,
"dsetstrt":null,
"mrsprchn":null,
"numdsets":null,
"pattnpts":null,
"detmode":null,
"cmd_tsel":null,
"fpe_side":"A",
"ice_side":"A",
"fileSize":190080,
"checksum":"988f90cad25ebfcae20481d6d7aa35e1",
"ingestStartDate":"2022-07-02T22:17:45.037000",
"ingestStartDate_mjd":59762.928993472226,
"ingestCompletionDate":"2022-07-02T22:17:59.651000",
"ingestCompletionDate_mjd":59762.92916261574,
"FileTypeID":63,
"publicReleaseDate":"2022-07-14T20:30:00",
"publicReleaseDate_mjd":59774.854166666664,
"isRestricted":false,
"isItar":false,
"isStale":false,
"FileSetId":876299
}
```

<!-- CHUNK 14 END -->

<!-- CHUNK 15 START -->
<!-- Metadata: {"Header 1": "Accessing Related Data Products"} -->
You can access all related data product for any JWST data product given a MAST DATA URI. Use the endpoint **https://mast.stsci.edu/viz/api/v0.1/products** , which accepts a **URI** query parameter with syntax "**uri=[MAST_DATA_URI]** ", and **level** query parameter, indicating the MAST Calibration Level of the products. See the [Products API Documentation](https://mast.stsci.edu/viz/docs/products.html) for complete details. This endpoint returns a list of data products for a given JWST observation ID. Each item in the list is a dictionary of data product parameters.
**Example** : [https://mast.stsci.edu/viz/api/v0.1/products?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits&level=3](https://mast.stsci.edu/viz/api/v0.1/products?uri=mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits&level=3)
**Example Output** Expand source
```
{
"jw01039-o004_t001_miri_ch3-long":[
{
"obsID":83209967,
"obs_collection":"JWST",
"obs_id":"jw01039-o004_t001_miri_ch3-long",
"dataproduct_type":"cube",
"type":"D",
"productType":"SCIENCE",
"productGroupDescription":"Minimum Recommended Products",
"productSubGroupDescription":"S3D",
"productDocumentationURL":null,
"project":"CALJWST",
"prvversion":"1.5.3",
"proposal_id":"1039",
"dataURI":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_s3d.fits",
"productFilename":"jw01039-o004_t001_miri_ch3-long_s3d.fits",
"description":"exposure/target (L2b/L3): 3D image of spectrum",
"size":370405440,
"parent_obsid":83209967,
"dataRights":"PUBLIC",
"calib_level":3,
"exp_type":"MIR_MRS",
"template":"MIRI External Flat"
},
{
"obsID":83209967,
"obs_collection":"JWST",
"obs_id":"jw01039-o004_t001_miri_ch3-long",
"dataproduct_type":"cube",
"type":"D",
"productType":"SCIENCE",
"productGroupDescription":"Minimum Recommended Products",
"productSubGroupDescription":"X1D",
"productDocumentationURL":null,
"project":"CALJWST",
"prvversion":"1.5.3",
"proposal_id":"1039",
"dataURI":"mast:JWST/product/jw01039-o004_t001_miri_ch3-long_x1d.fits",
"productFilename":"jw01039-o004_t001_miri_ch3-long_x1d.fits",
"description":"exposure/target (L2b/L3): 1D extracted spectrum",
"size":190080,
"parent_obsid":83209967,
"dataRights":"PUBLIC",
"calib_level":3,
"exp_type":"MIR_MRS",
"template":"MIRI External Flat"
}
]
}
```

<!-- CHUNK 15 END -->

<!-- CHUNK 16 START -->
<!-- Metadata: {"Header 1": "Accessing Metadata Information"} -->
You can access metadata information about the JWST Science Instrument (SI) keywords and Engineering Mnemonics using the API endpoint <https://mast.stsci.edu/viz/api/v0.1/info/>. See the [Info API Documentation](https://mast.stsci.edu/viz/docs/info.html) for complete details.

<!-- CHUNK 16 END -->

<!-- CHUNK 17 START -->
<!-- Metadata: {"Header 1": "Accessing Metadata Information", "Header 2": "Science Instrument Keywords"} -->
To access the metadata information about the science instrument keywords, use the endpoint **https://mast.stsci.edu/viz/api/v0.1/info/keywords/**. You can optionally specify a **name** query parameter, specifying the name of the keyword you wish to return information on. This endpoint returns the Instrument Keyword schema information in JSON format, the same information as displayed in the [JWST Keyword Dictionary](https://mast.stsci.edu/portal/Mashup/Clients/jwkeywords/index.html).
**Example - Return all keywords** : https://mast.stsci.edu/viz/api/v0.1/info/keywords/
**Example Output** Expand source
```
{
"all.dither.schema.json": {
"total_points": {
"fits_keyword": "NUMDTHPT",
"title": "Total number of points in dither pattern",
"description": "Total number of points in entire dither pattern",
"type": "integer",
"units": "",
"example": "3",
"default_value": "1",
"source": "Proposal and Planning System (PPS)",
"sw_source": "",
"calculation": "maximum(PPS:exposures.dither_point_index) in pattern (for program, observation, and pattern dither_id)",
"destination": [
"ScienceCommon.numdthpt"
],
"sql_dtype": "int",
"si": "All",
"mode": "All",
"level": "1b",
"fits_hdu": "PRIMARY",
"section": "Dither",
"misc": ""
},
"position_number": {
"fits_keyword": "PATT_NUM",
"title": "Position number within dither pattern",
"description": "Position number within dither pattern",
"type": "integer",
"units": "",
"example": "1",
"default_value": "1",
"source": "Proposal and Planning System (PPS)",
"sw_source": "PPS:exposures.dither_point_index",
"calculation": "",
"destination": [
"ScienceCommon.patt_num"
],
"sql_dtype": "smallint",
"si": "All",
"mode": "All",
"level": "1b",
"fits_hdu": "PRIMARY",
"section": "Dither",
"misc": ""
},
...
}


```  
**Example - Return a single keyword** : https://mast.stsci.edu/viz/api/v0.1/info/keywords?name=BKGDTARG
**Example Output** Expand source
```
{
"science.observation.schema.json": {
"bkgdtarg": {
"fits_keyword": "BKGDTARG",
"title": "Background target",
"description": "Indicates whether the proposer flagged the target or target field contained in the exposure to be used as a background target for other exposures.",
"type": "boolean",
"units": "",
"example": "T",
"default_value": "F",
"source": "",
"sw_source": "PPS:dms_target_view.background",
"calculation": "",
"destination": [
"ScienceCommon.bkgdtarg"
],
"sql_dtype": "nchar(1)",
"si": "Multiple",
"mode": "All",
"level": "1b",
"fits_hdu": "PRIMARY",
"section": "Observation identifiers",
"misc": ""
}
}
}
```

<!-- CHUNK 17 END -->

<!-- CHUNK 18 START -->
<!-- Metadata: {"Header 1": "Accessing Metadata Information", "Header 2": "Engineering Mnemonics"} -->
To access the metadata information about the engineering mnemonics, use the endpoint **https://mast.stsci.edu/viz/api/v0.1/info/mnemonics/**. You can optionally specify a **name** query parameter, specifying the name of the mnemonic you wish to return information on. This endpoint returns the mnemonic schema information in JSON format, the same information as displayed in the [JWST Engineering Portal](https://mast.stsci.edu/portal_jwst/Mashup/Clients/jwstedb/jwstedb.html).
**Example - Return all mnemonics** : https://mast.stsci.edu/viz/api/v0.1/info/mnemonics/
**Example Output** Expand source
```
{
"data": [
{
"subsystem": "FOS",
"tlmMnemonic": "FGDP_ICDH_STATE",
"tlmIdentifier": 570000,
"description": "ICDH state",
"sqlDataType": "varchar",
"unit": ""
},
{
"subsystem": "FOS",
"tlmMnemonic": "FGDP_INRS_FPE_A1FL",
"tlmIdentifier": 570067,
"description": "NIRSpec FPE ASIC1 Files Loaded Status",
"sqlDataType": "varchar",
"unit": ""
},
{...},
{...},
]
}
```  
**Example - Return a single mnemonic** : https://mast.stsci.edu/viz/api/v0.1/info/mnemonics/?name=so_zfxposns
**Example Output** Expand source
```
{
"data": [
{
"subsystem": "OTE",
"tlmMnemonic": "SO_ZFXPOSNS",
"tlmIdentifier": 81669,
"description": "x axis position of the FSM",
"sqlDataType": "float",
"unit": "rad"
}
]
}
```

<!-- CHUNK 18 END -->

<!-- CHUNK 19 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
* [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs)  
[Data Use](https://archive.stsci.edu/publishing/data-use) | [Acknowledgements](https://archive.stsci.edu/publishing/mission-acknowledgements) | [DOI](https://archive.stsci.edu/publishing/doi) | [Privacy](https://www.stsci.edu/privacy)
Send comments & corrections on this MAST document to:

<!-- CHUNK 19 END -->

