[ ![](https://mastweb.stsci.edu/kplrcasjobs/img/mastlogo.gif)](http://archive.stsci.edu) |  [ ![](https://mastweb.stsci.edu/kplrcasjobs/img/titlebar_left.png)](https://mastweb.stsci.edu/kplrcasjobs/default.aspx) |   
---|---|---  
[Home](https://mastweb.stsci.edu/kplrcasjobs/home.aspx) |  [Help](https://mastweb.stsci.edu/kplrcasjobs/guide.aspx) |  [GOHelp](https://mastweb.stsci.edu/kplrcasjobs/GOHelp.aspx) |  [Tools](https://mastweb.stsci.edu/kplrcasjobs/casjobscl.aspx) |  [Create Account](https://mastweb.stsci.edu/kplrcasjobs/CreateAccount.aspx) |  [Login](https://mastweb.stsci.edu/kplrcasjobs/login.aspx) |  |  Not Logged in   
---|---|---|---|---|---|---|---  
News
# **K e p l e r**
  

## Quick links
[GO Help](https://mastweb.stsci.edu/kplrcasjobs/GOHelp.aspx#intro)   

### SQL Tutorials
[Intro SQL Tutorial](https://mastweb.stsci.edu/kplrcasjobs/SQLTutorial.txt)   
[Advanced SQL Tutorial](http://www.w3schools.com/sql/sql_top.asp)   
**Note: For the Advanced SQL Tutorial, CASJobs is based upon SQL Server Syntax**   

## Greetings and Introduction
#### 1. Provenance and Purposes of CasJobs
CasJobs was originally developed by JHU/SDSS team, a copy of which was given to MAST. Until recently it has been used for downloading target results for GALEX objects, and you will see reference to the GALEX table as well as Kepler in some pages. MAST has posted the latest version (v3.5.16). This greeting and the Guide pages have been written for use with Kepler data. Acknowledgments of the use of CasJobs in publications should note that its authorship by the JHU/SDSS team. The url for the original site is http://casjobs.sdss.org/CasJobs. 
The purpose of CasJobs is to permit large queries, phrased in SQL, to be run in batch queue, such that they don't interfere with execution of small queries run in real time. A Quick run button on the open "Query" page is provided to test submission syntax. Note that no email notification is provided when a job is completed. 
Please note that CasJobs will enable you to obtain metadata (field descriptions, including Kepler IDs) if you've entered coordinate values in an object upload file. If you are searching on large numbers of targets (above several thousand) this is the page for you. However, if you are interested in downloads of all these objects, this will be only a first step. CasJobs alone cannot server this function. 
Groups:   
CasJobs also permits data to be shared by group collaborators. This is useful for for teams working on proprietary data that require a chain of queries to the mission database. 
#### 2. Running CasJobs
Register/login first. This is easy and intuitive. Notice that registration enables you to get into MAST's GALEX implementation of CasJobs too. Therefore, it you've already worked with GALEX data using CasJobs, you shouldn't register again. After registering, it is necessary for you to click on the "MyDB" tab at the top of the page. This will create your own CasJobs-stored database, which you will probably be using. After a period of several minutes' inactivity you will be logged out, so you will have to log back in and to navigate back to the page you had worked on earlier. (Any unsaved or unsubmitted work that you have done will not be saved.) 
Read this and the Help/Guide page for orientation. 
We encourage you to consult our sample queries after logging in by clicking on "Tools" (top banner), which takes you to the main SQL query box page Next, mouse over "Samples," read the descriptions, and select the query you want to work on. If none of these suits your purposes, feel free to contact us and perhaps the next sample will be yours. 
Send any questions, comments, or help requests to archive@stsci.edu. 
#### 3. Query syntax:
Query syntax is in SQL. Knowing SQL helps, but if you don't know SQL, you can Google "SQL tutorials," or come to MAST for recommendations on beginners text or specific queries. . This implementation of CasJobs is designed for you to "fake it." Our strategy to initiate you into its use is to provide "use case" samples. If you have new cases to provide us with, contact us at archive@stsci.edu, and we'll add them, or show you how to customize a posted example. 
[Contact MAST](http://archive.stsci.edu/contacts.html)   
CASJobs is made possible by the [Sloan Digital Sky Survey Collaboration](http://cas.sdss.org)  
$Name: v3_5_16 $ ,$Revision: 1.31 $, Last modified: Tuesday, October 26, 2010 at 9:50:37 AM 
