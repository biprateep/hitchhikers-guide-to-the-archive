---
title: "Engineering Database Contents"
source_url: "https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data"
date_accessed: "2026-03-11T16:32:10.949200"
content_length: 3783
---

<!-- CHUNK 1 START -->
This article describes how to search for and retrieve JWST engineering telemetry.
**On this page...**
* 1[Engineering Database Contents](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data#EngineeringData-EngineeringDatabaseContents)
* 1.1[Mnemonics](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data#EngineeringData-Mnemonics)
* 1.2[Data Tuples](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data#EngineeringData-DataTuples)
* 2[For Further Reading...](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771335/Engineering+Data#EngineeringData-ForFurtherReading...)

<!-- CHUNK 1 END -->

<!-- CHUNK 2 START -->
<!-- Metadata: {"Header 1": "Engineering Database Contents", "Header 2": "Mnemonics"} -->
Data associated with the thousands of engineering telemetry points on JWST are stored in the Engineering Database. The data take the form of timeseries, and they may be searched with the [Calibrated Engineering Data Portal](https://mast.stsci.edu/portal/Mashup/Clients/jwstedb/jwstedb.html) by means of an identifier, or _**mnemonic**_. The mnemonics have a naming convention which has the form:
`<**X**><**Y**>`**_**`<**Z**>`
where:
* `<**X**>`indicates the system, with one of the characters:
* _`I`_: for ISIM (the integrated science instrument module)  
* _`S`_: for Spacecraft
* `<**Y**>`indicates the subsystem, instrument, controller, or component (1 to 4 letters)
* `<**Z**>`indicates the telemetry name (2 to as many as 20 alphanumeric characters or underscores)  
For instance, a mnemonic name beginning with **`INRS_`**pertains to the instrument NIRSpec,**`INIS_`**pertains to NIRISS;**`SA_`**to the spacecraft attitude control system, and so on. To search for and retrieve engineering data with these mnemonics, see the article:[Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal).
Time Sampling
Some mnemonics are sampled at a predefined frequency, whether the value has changed or not. Others mnemonics are reported only if they have changed since the last time they were sampled (e.g., for changes of state among a small number of possible values).

<!-- CHUNK 2 END -->

<!-- CHUNK 3 START -->
<!-- Metadata: {"Header 1": "Engineering Database Contents", "Header 2": "Data Tuples"} -->
Some engineering data occur in **_tuples_** , that is, two or more values may be needed to fully define an engineering quantity of interest. For instance,
* `SA_ZATTEST_**n**_`, where the value _**n**_ ranges from 1 through 4, define the coefficients of the quaternion, i.e., the 4-dimensional quantity that defines the JWST pointing and roll.
* `SA_ZADUCMD**X**`and`SA_ZADUCMD**Y**`define the commanded _x_ - and _y_ -position of the fine steering mirror (FSM).  
Such quantities are generally analyzed together, as illustrated in the plot below for the FSM position as simulated during an exercise. See the JWST EDB Retrieval tutorial in the [Using MAST APIs](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs) article for details. Be aware that engineering data as retrieved from MAST are stored one mnemonic per file.  
![Trace of FSM position with time](https://outerspace.stsci.edu/download/attachments/113771335/bokeh_FSM.jpg?version=1&modificationDate=1629750165932&api=v2)Plot of the commanded (x,y) position of the Fine Steering Mirror as a function of time. Colors correspond to time intervals when the FSM was being actively commanded. The color of the trace is different for each time interval: see legend.

<!-- CHUNK 3 END -->

<!-- CHUNK 4 START -->
<!-- Metadata: {"Header 1": "For Further Reading..."} -->
See the following articles for instructions on querying the Engineering Database:
* [Using the Engineering Data Portal](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771415/Using+the+Engineering+Data+Portal)
* [Using the EDB API](https://outerspace.stsci.edu/spaces/MASTDOCS/pages/113771434/Using+MAST+APIs)

<!-- CHUNK 4 END -->

