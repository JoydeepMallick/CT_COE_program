# System Variables in Azure Data Factory

Video link : https://youtu.be/-VtZtajW2Hc?si=vHeQBsz-MnYQyxTg

System varibles are available at below 3 scopes. We can use these varibles in the expressions in ADF.

- ### Pipeline scope
- ### schedule trigger scope
- ### tumbling window trigger scope

#### ⭐⭐Read entire article [here](https://learn.microsoft.com/en-us/azure/data-factory/control-flow-system-variables)

<h2 id="pipeline-scope" class="heading-anchor" ><a href="https://learn.microsoft.com/en-us/azure/data-factory/control-flow-system-variables#pipeline-scope"> Pipeline scope</a></h2>

These system variables can be referenced anywhere in the pipeline JSON.

<table aria-label="Table 1" class="table table-sm margin-top-none">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().DataFactory</span></td>
<td>Name of the data  or Synapse workspace the pipeline run is running in</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().Pipeline</span></td>
<td>Name of the pipeline</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().RunId</span></td>
<td>ID of the specific pipeline run</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().TriggerType</span></td>
<td>The type of trigger that invoked the pipeline (for example, <code>ScheduleTrigger</code>, <code>BlobEventsTrigger</code>). For a list of supported trigger types, see <a href="concepts-pipeline-execution-triggers" data-linktype="relative-path">Pipeline execution and triggers</a>. A trigger type of <code>Manual</code> indicates that the pipeline was triggered manually.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().TriggerId</span></td>
<td>ID of the trigger that invoked the pipeline</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().TriggerName</span></td>
<td>Name of the trigger that invoked the pipeline</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().TriggerTime</span></td>
<td>Time of the trigger run that invoked the pipeline. This is the time at which the trigger <strong>actually</strong> fired to invoke the pipeline run, and it may differ slightly from the trigger's scheduled time.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline().GroupId</span></td>
<td>ID of the group to which pipeline run belongs.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline()</span>?.TriggeredByPipelineName</td>
<td>Name of the pipeline that triggers the pipeline run. Applicable when the pipeline run is triggered by an ExecutePipeline activity. Evaluate to <em>Null</em> when used in other circumstances. Note the question mark after <span class="no-loc" dir="ltr" lang="en-us">@pipeline()</span></td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@pipeline()</span>?.TriggeredByPipelineRunId</td>
<td>Run ID of the pipeline that triggers the pipeline run. Applicable when the pipeline run is triggered by an ExecutePipeline activity. Evaluate to <em>Null</em> when used in other circumstances. Note the question mark after <span class="no-loc" dir="ltr" lang="en-us">@pipeline()</span></td>
</tr>
</tbody>
</table>



<h2 id="schedule-trigger-scope" class="heading-anchor"><a href="https://learn.microsoft.com/en-us/azure/data-factory/control-flow-system-variables#schedule-trigger-scope">Schedule trigger scope</a></h2>

These system variables can be referenced anywhere in the trigger JSON for triggers of type ScheduleTrigger.

<table aria-label="Table 2" class="table table-sm margin-top-none">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@trigger().scheduledTime</span></td>
<td>Time at which the trigger was scheduled to invoke the pipeline run.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@trigger().startTime</span></td>
<td>Time at which the trigger <strong>actually</strong> fired to invoke the pipeline run. This may differ slightly from the trigger's scheduled time.</td>
</tr>
</tbody>
</table>

<h2 id="storage-event-trigger-scope" class="heading-anchor">Storage event trigger scope</h2>


<h2 id="storage-event-trigger-scope" class="heading-anchor"><a href="https://learn.microsoft.com/en-us/azure/data-factory/control-flow-system-variables#storage-event-trigger-scope">Storage event trigger scope</a></h2>

These system variables can be referenced anywhere in the trigger JSON for triggers of type BlobEventsTrigger.

<table aria-label="Table 4" class="table table-sm margin-top-none">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@triggerBody().fileName</span></td>
<td>Name of the file whose creation or deletion caused the trigger to fire.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@triggerBody().folderPath</span></td>
<td>Path to the folder that contains the file specified by <code>@triggerBody().fileName</code>. The first segment of the folder path is the name of the Azure Blob Storage container.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@trigger().startTime</span></td>
<td>Time at which the trigger fired to invoke the pipeline run.</td>
</tr>
</tbody>
</table>

<h2 id="custom-event-trigger-scope" class="heading-anchor"><a href="https://learn.microsoft.com/en-us/azure/data-factory/control-flow-system-variables#custom-event-trigger-scope">Custom event trigger scope</a></h2>

These system variables can be referenced anywhere in the trigger JSON for triggers of type CustomEventsTrigger.

<table aria-label="Table 5" class="table table-sm margin-top-none">
<thead>
<tr>
<th>Variable Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@triggerBody().event.eventType</span></td>
<td>Type of events that triggered the Custom Event Trigger run. Event type is customer-defined field and take on any values of string type.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@triggerBody().event.subject</span></td>
<td>Subject of the custom event that caused the trigger to fire.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@triggerBody().event.data._keyName_</span></td>
<td>Data field in custom event is a free from JSON blob, which customer can use to send messages and data. Please use data.<em>keyName</em> to reference each field. For example, <span class="no-loc" dir="ltr" lang="en-us">@triggerBody().event.data.callback</span> returns the value for the <em>callback</em> field stored under <em>data</em>.</td>
</tr>
<tr>
<td><span class="no-loc" dir="ltr" lang="en-us">@trigger().startTime</span></td>
<td>Time at which the trigger fired to invoke the pipeline run.</td>
</tr>
</tbody>
</table>

### demo for pipeline scope: https://youtu.be/-VtZtajW2Hc?t=90

When To use what :-
- Pipeline Scope system variables : Copy data from one storage to another and then log details of pipeline execution into SQL DB.

- Schedule trigger scope of system variables : Copy data one storage to another storage daily for given date.

- Tumbling window trigger scope system variable : copy data one storage to another storage for every hours.

### demo for schedule trigger pipeline : https://youtu.be/-VtZtajW2Hc?t=522

### demo for tumbling window trigger pipeline : https://youtu.be/-VtZtajW2Hc?t=672





# Connectors Overview in Azure Data Factory

Video link : https://youtu.be/KMzQgkdKnBc?si=0_y-tdLr4-Z8e3xo

⭐⭐Read [here](https://www.google.com/search?q=azure+darta+factory+connector+overview&oq=azure+darta+factory+connector+overview&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDcxNzVqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8)

Azure Data Factory connectors help establish a connection with source and destination data stores.

Remember that these connectors are used in linked services. 

Different activities include:
- **Copy** : copy data from one storage to another
- **lookup** : you  can connect storage and then search for an object
- **getmetadata** : connect to data store and give metadata of data
- **delete** : to delete any type of data within the store

### Demo : https://youtu.be/KMzQgkdKnBc?t=287

Azure data factory supports more than 80 data stores to work with.

Supported formats :
- avro format
- binary format
- deliminated text format
- JSON format
- ORC format
- Parquet format





# Supported File Formats in Azure Data Factory

Video link : https://youtu.be/uE8IZMiRc5s?si=w5j7PkYI-0BHmAQ-

Supported formats :
- 😀binary format : **text files**
- 😀deliminated text format : **CSV (comma seperated values)**
- 😀JSON format : **JSON files**
- ORC format 🤔
- Parquet format 🤔
- avro format 🤔

<h3 style="color:yellow">First 3 formats are common😀 but the last 3 are new🤔</h3>

### Demo : https://youtu.be/uE8IZMiRc5s?t=87

ORC, Avro, Parquet are the formats  which are part of **Apache Hadoop ecosystem**.

All 3 formats works on **compression algorithms**. Data will stored in compression hence query results will be **much faster**.

Using ADF, if you read data from SQL  table and load data in different formats, **then JSON and text files sizes will be more compared to ORC, Parquet & Avro**.

### Read about [ORC format](https://learn.microsoft.com/en-us/azure/data-factory/format-orc), [PArquet format](https://learn.microsoft.com/en-us/azure/data-factory/format-parquet) and [Avro Format](https://learn.microsoft.com/en-us/azure/data-factory/format-avro)

### ⭐⭐Important notes :-
- Azure data is **build on Apache Hadoop**
- Avro is a **row based storage format** for Hadoop. Avro **stores data defination(schema) in JSON format** making it easy to read and interpret by any program
- Parquet is **column based storage format**





# Copy Data Activity in Azure Data Factory

Video link : https://youtu.be/XOJeyRBXBos?si=_mstU3KGcBEa3LbT

Copy data activity is the core of ADF. We can copy data from more than 90 connectors one to another.


Read more [here](https://learn.microsoft.com/en-us/azure/data-factory/connector-azure-blob-storage?tabs=data-factory)

### ⭐⭐demo link : https://youtu.be/XOJeyRBXBos?t=109



# Copy Data Activity in Azure data factory Continuation

Video link : https://youtu.be/pjGN_4BfORM?si=VoKxfgOT8C_shfBI

Settings sections in Copy Data Activity in ADF
- **Data Integration Units** - THink it like a combination  of CPU, Memory and Networking power, more power means more cost.

- **Degree of Parallelism** - number of connections or threads to perform read and write

- Copy data can copy data from csv file to SQL table

User properties in Copy Data Activity in ADF 
- User Properties help to view addition information while monitoring Activity runs(**like displaying source and destination locations which are not shown by default**)



### demo : https://youtu.be/pjGN_4BfORM?t=55



# Monitor Copy Data Activity in Azure Data Factory

Video link : https://youtu.be/bIITK_WUF0w?si=JGBk_ZGdktqZkrxD

Once you have created and published the pipeline in ADF, we can associate it with a trigger or manually kick off an adhoc run. You can monitor all of our pipeline runs natively in the ADF user experience.



# Delete Activity in Azure Data Factory

Video link : https://youtu.be/7B5BJ1SV_Pw?si=FPjmk6jywWBGXXmI

You can use the Delete activity in ADF to delete files or folders from on-premise storage stores or cloud storage stores 

**Deleted files or folders cannot be stored(permananent)**.

Supported data stores :-
- Azure Blob Storage
- Azure Data Lake Storage Gen1
- Azure Data Lake Storage Gen2
- Azure File Storage

File system data stores:-
- File system
- FTP
- SFTP
- Amazon S3
- Google Cloud Storage

### ⭐⭐Demo link : https://youtu.be/7B5BJ1SV_Pw?t=86





# Variables in Azure Data Factory

Video link : https://youtu.be/6cPv1TlVviA?si=HzblIFfK6FifX6KS

Variables are like internal to pipeline and they can be changed  inside your pipeline.

Variables support 3 data types :- `string`, `bool` and `array`

We refer these user variables as below :-
```sh
@variables('variableName')
```

### difference between Parameters and Variables

- To pass value to **parameters** from triggers and then used inside pipeline.

- We can set values of **variables** internally inside pipelines using `Set Variable` and `Append Variable` activity.

### Demo link : https://youtu.be/6cPv1TlVviA?t=183

#### Example
Assume 2 blob based storages containing:-
1. HourlyFiles contain `HourlySales.csv`
2. DailySales contain `DailySails.csv`

We need to store them in **HourlySale table** and **DailySale Table** respectively.

To perform this we need to use **Event based trigger**:-
```sh
@triggerBody.fileName
```
### demo link : https://youtu.be/6cPv1TlVviA?t=183


<br/><br/><br/><br/><br/><br/>

# All **control flow** activities

![](https://azurede.com/wp-content/uploads/2020/06/azure-control-flow-activities.png)

## 1. Set Variable Activity in Azure Data Factory

Video link : https://youtu.be/rzDZdRifC40?si=rbMeactaJ97230-P

Use the set variable activity to set the value of an existing variable of type String, bool, or array defined in data factory pipeline.

### ⭐⭐demo : https://youtu.be/rzDZdRifC40?t=108



## 2. Append Variable Activity in Azure Data Factory

Video link : https://youtu.be/aJuohp8a-fA?si=6VpmF8uU7PfPlwWE

Use append variable activity to add value to an exisiting array variable in Data Factory pipeline.

### ⭐⭐demo : https://youtu.be/aJuohp8a-fA?t=147



## User Properties in Azure Data Factory

Video link : https://youtu.be/0QExfRwhhDo?si=e5Y1SgHTH_rYBOgB

**User properties** help to view additional information while monitoring acitivity runs

We can create only <span style="color:yellow">5 properties under User properties.</span>

#### DEMO : https://youtu.be/0QExfRwhhDo?t=84






## 3. Execute Pipeline Activity in Azure Data Factory

Video link : https://youtu.be/nc4IFKkkfXM?si=reIkSFn2TVLpOa-A

The **execute pipeline activity** allows a data factory pipeline to invoke another pipeline.

#### DEMO : https://youtu.be/nc4IFKkkfXM?t=54





## 4. Filter Activity in Azure Data Factory

Video link : https://youtu.be/y2KDonUDuPc?si=DCgdbk7RYQmiMcHj

We can use **filter activity** in a pipeline to apply filter expression to an input array.

#### DEMO : https://youtu.be/y2KDonUDuPc?t=78






## 5. ForEach Activity in Azure Data Factory

Video link : https://youtu.be/KuWYuHlUwD0?si=tpv57z8zpSkoeHx_

**ForEach activity** defines a repeating control flow in your pipeline. This activity is used to iterate over a collection and executes specified activities in a loop.

The **item property** is a collection of each item inside collection is referred by `@item()`

    If items in an array : [1, 2, 3]
    @item() returns 1 in first iteration
                    2 in second iteration
                    3 in third iteration

#### DEMO : https://youtu.be/KuWYuHlUwD0?t=98






## 6. Get Metadata Activity in Azure Data Factory

Video link : https://youtu.be/_VNOabanIV4?si=SMCxIemXy_1AGFSi

We can use **Get Metadata activity** to retrieve the metadata of an ADF.

#### DEMO : https://youtu.be/_VNOabanIV4?t=29

#### ⭐⭐Read more [here](https://unstop.com/hackathons/flipkart-grid-60-software-development-track-flipkart-grid-60-flipkart-1024247)

<table aria-label="Table 3" class="table table-sm margin-top-none">
<thead>
<tr>
<th style="text-align: left;">Metadata type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">itemName</td>
<td style="text-align: left;">Name of the file or folder.</td>
</tr>
<tr>
<td style="text-align: left;">itemType</td>
<td style="text-align: left;">Type of the file or folder. Returned value is <code>File</code> or <code>Folder</code>.</td>
</tr>
<tr>
<td style="text-align: left;">size</td>
<td style="text-align: left;">Size of the file, in bytes. Applicable only to files.</td>
</tr>
<tr>
<td style="text-align: left;">created</td>
<td style="text-align: left;">Created datetime of the file or folder.</td>
</tr>
<tr>
<td style="text-align: left;">lastModified</td>
<td style="text-align: left;">Last modified datetime of the file or folder.</td>
</tr>
<tr>
<td style="text-align: left;">childItems</td>
<td style="text-align: left;">List of subfolders and files in the given folder. Applicable only to folders. Returned value is a list of the name and type of each child item.</td>
</tr>
<tr>
<td style="text-align: left;">contentMD5</td>
<td style="text-align: left;">MD5 of the file. Applicable only to files.</td>
</tr>
<tr>
<td style="text-align: left;">structure</td>
<td style="text-align: left;">Data structure of the file or relational database table. Returned value is a list of column names and column types.</td>
</tr>
<tr>
<td style="text-align: left;">columnCount</td>
<td style="text-align: left;">Number of columns in the file or relational table.</td>
</tr>
<tr>
<td style="text-align: left;">exists</td>
<td style="text-align: left;">Whether a file, folder, or table exists. If <code>exists</code> is specified in the Get Metadata field list, the activity won't fail even if the file, folder, or table doesn't exist. Instead, <code>exists: false</code> is returned in the output.</td>
</tr>
</tbody>
</table>

#### DEMO : https://youtu.be/_VNOabanIV4?t=643

### [Sample Output](https://learn.microsoft.com/en-us/azure/data-factory/control-flow-get-metadata-activity#sample-output)
The Get Metadata results are shown in the activity output. Following are two samples showing extensive metadata options. To use the results in a subsequent activity, use this pattern: `@{activity('MyGetMetadataActivity').output.itemName}`.

#### Get a file's metadata
```json
{
  "exists": true,
  "itemName": "test.csv",
  "itemType": "File",
  "size": 104857600,
  "lastModified": "2017-02-23T06:17:09Z",
  "created": "2017-02-23T06:17:09Z",
  "contentMD5": "cMauY+Kz5zDm3eWa9VpoyQ==",
  "structure": [
    {
        "name": "id",
        "type": "Int64"
    },
    {
        "name": "name",
        "type": "String"
    }
  ],
  "columnCount": 2
}
```

#### Get a folder's metadata
```json
{
  "exists": true,
  "itemName": "testFolder",
  "itemType": "Folder",
  "lastModified": "2017-02-23T06:17:09Z",
  "created": "2017-02-23T06:17:09Z",
  "childItems": [
    {
      "name": "test.avro",
      "type": "File"
    },
    {
      "name": "folder hello",
      "type": "Folder"
    }
  ]
}
```




## 7. If Condition Activity in Azure Data Factory

Video link : https://youtu.be/pd-DJJUhnsw?si=H04JWM2nyTKQupUj

**If condition** activity provides the same functionality as an if statement in programming languages.

If the expression(s) within if resolve the true then the set of activities within scope of if runs else not and goes to the else part.

#### DEMO : https://youtu.be/pd-DJJUhnsw?t=111





## 8. Wait Activity in Azure Data Factory

Video link : https://youtu.be/JVNt4unI06Y?si=V1wLWDll4jTGDfnF

When we use the **Wait Activity** in a pipeline, the pipeline waits for a specified period of time before continuing  with execution of subsequence activities.

#### DEMO : https://youtu.be/JVNt4unI06Y?t=66








## 9. Until Activity in Azure Data Factory

Video link : https://youtu.be/n8e_exWMH5k?si=ZzjrWBoqZZeiKsxG

**Until activity** is like Do-While or Do-Until of programming languages. 

**It guarantees that at least once loops runs since condition is evaluated after loop body is executed.**

Similar to do-while loops it executed till the condition is satisfied.

#### DEMO : https://youtu.be/n8e_exWMH5k?t=82







## 10. Web Activity in Azure Data Factory

Video link : https://youtu.be/rvIcklXCLVk?si=cDxTTvEV2Ig2AeMg

**Web activity** can be used to call custom REST endpoint from a Data Factory pipeline.

We can pass datasets and linked services also to REST API

Web Activity can call only publicly exposed URLs, its not supported for URLs that are hosted in a private virtual network.

#### DEMO : https://youtu.be/rvIcklXCLVk?t=93




## 11. WebHook Activity in Azure Data Factory

Video link : https://youtu.be/XQExOQ3KLhg?si=mBGS2hiz_8N0sKvZ

In WebHook Activity we can call an endpoint and pass it a callback 

How it actually happens :-
    
    when we issue a call to a REST API
    ADF adds a callback URL to the request body automatically.

  Here we issue a request then wait for the request to complete successfully, after confirmation we move forward operation. This is the **Synchronous behavior**.


In case of **Asynchronous request** we simply issue a request and then move forward the pipeline for the next activity. We do not wait for the confirmation.

e.g. **Web Activity**

<span style="color:yellow"> Read the difference between Web activity and webhook activity to get insights on asynchronous and synchronous behavior  </span>

#### DEMO : https://youtu.be/XQExOQ3KLhg?t=186






## 12. Switch Activity in Azure Data Factory

Video link : https://youtu.be/-YwdbnEc_9Q?si=nb_kRJFAIk7f2i61

**Switch activity** provides the same functionality that switch statement provides in many programming languages

It evaluates a set of activities corresponding to a case that matches the condition evaluation.

#### ⭐⭐⭐See example DEMO : https://youtu.be/-YwdbnEc_9Q?t=66




## 13. Validation Activity in Azure Data Factory

Video link : https://youtu.be/Jesb-nLXtQ4?si=_2jLMxE1TzAKdAPP


We can use Validation in a pipeline to ensure that pipeline continues execution only if it has validated the attached dataset reference exists.

#### DEMO : https://youtu.be/Jesb-nLXtQ4?t=72




## 14. Lookup Activity in Azure Data Factory

Video link : https://youtu.be/Jesb-nLXtQ4?si=6xFhaN3BrX0AuWen

**Lookup activity can retrieve a dataset from any of the ADF supported data sources.**

**Lookup activity** reads and returns  the contents of a configuration file or table. It also returns the result of executing query or stored procedure.

The output from **lookup activity** can be used in subsequent activity.

### [Supported capabilities](https://learn.microsoft.com/en-us/azure/data-factory/control-flow-lookup-activity#supported-capabilities)

- The Lookup activity can return up to 5000 rows; if the result set contains more records, the first 5000 rows will be returned.
- The Lookup activity output supports up to 4 MB in size, activity will fail if the size exceeds the limit.
- The longest duration for Lookup activity before timeout is 24 hours.
 Note

#### NOTE
When you use query or stored procedure to lookup data, make sure to return one and exact one result set. Otherwise, Lookup activity fails.

The following data sources are supported for Lookup activity.

<table aria-label="Table 1" class="table table-sm margin-top-none">
<thead>
<tr>
<th style="text-align: left;">Category</th>
<th style="text-align: left;">Data store</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Azure</strong></td>
<td style="text-align: left;"><a href="connector-azure-blob-storage" data-linktype="relative-path">Azure Blob storage</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-cosmos-db" data-linktype="relative-path">Azure Cosmos DB for NoSQL</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-data-explorer" data-linktype="relative-path">Azure Data Explorer (Kusto)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-data-lake-store" data-linktype="relative-path">Azure Data Lake Storage Gen1</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-data-lake-storage" data-linktype="relative-path">Azure Data Lake Storage Gen2</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-database-for-mariadb" data-linktype="relative-path">Azure Database for MariaDB</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-database-for-mysql" data-linktype="relative-path">Azure Database for MySQL</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-database-for-postgresql" data-linktype="relative-path">Azure Database for PostgreSQL</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-databricks-delta-lake" data-linktype="relative-path">Azure Databricks Delta Lake</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-file-storage" data-linktype="relative-path">Azure Files</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-sql-database" data-linktype="relative-path">Azure SQL Database</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="/en-us/azure/azure-sql/managed-instance/sql-managed-instance-paas-overview" data-linktype="absolute-path">Azure SQL Managed Instance</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-sql-data-warehouse" data-linktype="relative-path">Azure Synapse Analytics</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-table-storage" data-linktype="relative-path">Azure Table storage</a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Database</strong></td>
<td style="text-align: left;"><a href="connector-amazon-rds-for-oracle" data-linktype="relative-path">Amazon RDS for Oracle</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-amazon-rds-for-sql-server" data-linktype="relative-path">Amazon RDS for SQL Server</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-amazon-redshift" data-linktype="relative-path">Amazon Redshift</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-impala" data-linktype="relative-path">Apache Impala</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-sql-managed-instance" data-linktype="relative-path">Azure SQL Managed Instance</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-db2" data-linktype="relative-path">DB2</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-drill" data-linktype="relative-path">Drill</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-google-adwords" data-linktype="relative-path">Google AdWords</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-google-bigquery" data-linktype="relative-path">Google BigQuery</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-greenplum" data-linktype="relative-path">Greenplum</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-hbase" data-linktype="relative-path">HBase</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-hive" data-linktype="relative-path">Hive</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-informix" data-linktype="relative-path">Informix</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-mariadb" data-linktype="relative-path">MariaDB</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-microsoft-access" data-linktype="relative-path">Microsoft Access</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-mysql" data-linktype="relative-path">MySQL</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-netezza" data-linktype="relative-path">Netezza</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-oracle" data-linktype="relative-path">Oracle</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-phoenix" data-linktype="relative-path">Phoenix</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-postgresql" data-linktype="relative-path">PostgreSQL</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-presto" data-linktype="relative-path">Presto</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sap-business-warehouse-open-hub" data-linktype="relative-path">SAP Business Warehouse Open Hub</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sap-business-warehouse" data-linktype="relative-path">SAP Business Warehouse via MDX</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sap-hana" data-linktype="relative-path">SAP HANA</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sap-table" data-linktype="relative-path">SAP Table</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sql-server" data-linktype="relative-path">SQL Server</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-spark" data-linktype="relative-path">Spark</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sybase" data-linktype="relative-path">Sybase</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-teradata" data-linktype="relative-path">Teradata</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-vertica" data-linktype="relative-path">Vertica</a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>NoSQL</strong></td>
<td style="text-align: left;"><a href="connector-cassandra" data-linktype="relative-path">Cassandra</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-couchbase" data-linktype="relative-path">Couchbase (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>File</strong></td>
<td style="text-align: left;"><a href="connector-amazon-simple-storage-service" data-linktype="relative-path">Amazon S3</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-amazon-s3-compatible-storage" data-linktype="relative-path">Amazon S3 Compatible Storage</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-file-system" data-linktype="relative-path">File System</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-ftp" data-linktype="relative-path">FTP</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-google-cloud-storage" data-linktype="relative-path">Google Cloud Storage</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-hdfs" data-linktype="relative-path">HDFS</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-http" data-linktype="relative-path">Generic HTTP</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-microsoft-fabric-lakehouse" data-linktype="relative-path">Microsoft Fabric Lakehouse</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-oracle-cloud-storage" data-linktype="relative-path">Oracle Cloud Storage</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sftp" data-linktype="relative-path">SFTP</a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Generic protocol</strong></td>
<td style="text-align: left;"><a href="connector-odata" data-linktype="relative-path">Generic OData</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-odbc" data-linktype="relative-path">Generic ODBC</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sharepoint-online-list" data-linktype="relative-path">SharePoint Online List</a></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Services and apps</strong></td>
<td style="text-align: left;"><a href="connector-amazon-marketplace-web-service" data-linktype="relative-path">Amazon Marketplace Web Service</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-concur" data-linktype="relative-path">Concur (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-dynamics-crm-office-365" data-linktype="relative-path">Dataverse</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-dynamics-crm-office-365" data-linktype="relative-path">Dynamics 365</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-dynamics-ax" data-linktype="relative-path">Dynamics AX</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-dynamics-crm-office-365" data-linktype="relative-path">Dynamics CRM</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-hubspot" data-linktype="relative-path">HubSpot</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-jira" data-linktype="relative-path">Jira</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-azure-data-explorer" data-linktype="relative-path">Azure Data Explorer (Kusto)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-magento" data-linktype="relative-path">Magento (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-marketo" data-linktype="relative-path">Marketo (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-oracle-eloqua" data-linktype="relative-path">Oracle Eloqua (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-oracle-responsys" data-linktype="relative-path">Oracle Responsys (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-oracle-service-cloud" data-linktype="relative-path">Oracle Service Cloud (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-paypal" data-linktype="relative-path">PayPal (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-quickbooks" data-linktype="relative-path">QuickBooks (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sap-cloud-for-customer" data-linktype="relative-path">SAP Cloud for Customer (C4C)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-sap-ecc" data-linktype="relative-path">SAP ECC</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-salesforce" data-linktype="relative-path">Salesforce</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-salesforce-marketing-cloud" data-linktype="relative-path">Salesforce Marketing Cloud</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-salesforce-service-cloud" data-linktype="relative-path">Salesforce Service Cloud</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-servicenow" data-linktype="relative-path">ServiceNow</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-shopify" data-linktype="relative-path">Shopify (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-snowflake" data-linktype="relative-path">Snowflake</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-square" data-linktype="relative-path">Square (Preview)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-web-table" data-linktype="relative-path">Web Table (HTML table)</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-xero" data-linktype="relative-path">Xero</a></td>
</tr>
<tr>
<td style="text-align: left;">&nbsp;</td>
<td style="text-align: left;"><a href="connector-zoho" data-linktype="relative-path">Zoho (Preview)</a></td>
</tr>
</tbody>
</table>

#### ⭐⭐⭐See example DEMO : https://youtu.be/MWuWanhrNoU?t=159






<br/><br/><br/><br/><br/><br/>

# Transform Data Activities Overview in Azure Data Factory

Video link : https://www.youtube.com/watch?v=wsQYuVT4Dpw

**Transform Data activities**   can be used to process and transform data in compute environment such as Azure Data Bricks or Azure HDInsight or Azure Data Analytics, etc.

    Reading logs is difficult directly. Hence we can write scripts to transform logs in readable and useful format by extracting specific parts(transformed data -> DAU, MAU etc)

Above problem is addressed by **different compute engines available in Azure Data factory** like:-
- DataLake Analytics
- DataBricks
- HDInsights

All the different transform data activities are :-

![](./Screenshot%20(874).png)





# Stored Procedure Activity in Azure Data Factory

Video link : https://www.youtube.com/watch?v=4Npu4F6dqMo

**Stored procedure activity** is  one of the transformation activities that Data factory supports. We run stored procedure as one of the step using this Activity.

#### DEMO : https://youtu.be/4Npu4F6dqMo?t=35









# Data flow in Azure data factory

Video link : https://www.youtube.com/watch?v=tdShbtu3shw


Data Flow in ADF will allow us to **develop graphical data transformation logic that can be executed as activities in ADF pipelines**.

Our Data Flow will execute on your own Azure data bricks cluster  for scaled out data processing using spark.

ADF internally handles all the code translation, spark optimization and exection of transformation.

#### DEMO : https://youtu.be/tdShbtu3shw?t=42







# Mapping Data Flow in Azure Data Factory

Video link : https://www.youtube.com/watch?v=HgcaPcBYXNI

**Mapping data flows** are visually designed data transformations in ADF. Data flows allow data engineers to develop graphical data transformation logic without writing code.

Data flows are executed as activities with ADF pipelines using Data Flow Activities.

ADF internally handles all the code translation, spark optimization and execution of transformation.

#### SEE VIDEO🔼




# Data Flow Activity in Azure Data Factory

Video link : https://youtu.be/FxkN1vctsB4

Use Dat Flow Activity to execute Data flows in our pipeline.
#### SEE VIDEO🔼




# Mapping Data Flow Debug Mode in Azure Data Factory

Video link : https://youtu.be/1MrnawEbO2U

**ADF Mapping data flow's debug mode** allows us to **interactively watch the data shape transform while you build and debug our data flows**.

To turn on debug mode, use the "`Data Flow Debug`" button at the top of the design surface.

A cluster with eight cores of general compute with a 60 minute time to live will be spun up.

The session will close once you turn debug off in ADF.
#### SEE VIDEO🔼


# Filter Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/hpXePPFqJCs

**Filter transforms** allow row transformation based upon a condition. The output stream includes all rows that mathing the filter condition. **The filter transformation is similar to a WHERE clause in SQL**.

#### SEE VIDEO🔼





# Aggregate Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/-sxpg-6zgww

The **Aggregate transformation** defines aggregation of columns in your data streams. Using the Expression Builder, you can define different types of aggregations such **SUM**, **MIN**, **MAX**, and **COUNT** grouped by existing or computed columns.

#### SEE VIDEO🔼






# JOIN Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/hq5BtHbATIc

Use **Join Transformation** to combine data from two sources or streams in a mapping data flow. The **output stream will include all columns from both sources matched based on a join condition**.

#### SEE VIDEO🔼










# Conditional Split Transformation in Mapping Data Flow in Azure data factory

Video link : https://youtu.be/20iyvIrW7mg

**Conditional Split transformation** routes data rows to different streams based on matching conditions. **The conditional split transformation is similar to a CASE decision structure in a programming language**.

#### SEE VIDEO🔼




# Derived Column Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/a5KClu7LboQ

Use the **derived column transformation** to generate new columns in your data flow or to modify existing fields.

#### SEE VIDEO🔼






# Exists Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/a5KClu7LboQ

The **Exists transformation is a row filtering transformation** that checks whether your data exists in another source or stream.

**The output stream includes all rows in the left stream that either exist or don't exist in the right stream.**

The Exists transformation is similar to SQL `WHERE EXISTS` and SQL `WHERE NOT EXISTS`.

#### SEE VIDEO🔼




# Union Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/vFCNbHqWct8

Union will combine multiple data streams into one, with the **SQL Union of those streams as the output** from the union transformation.

We can combine n number of streams in the settings table by selecting the `+` icon next to each configured row, including both source data as well as streams from existing transformations in  your data flow.

#### SEE VIDEO🔼

# Lookup Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/Z4xfVDYbNNE

A **lookup transformation** is similar to a **left outer join**. All rows from the primary stream will exist in the output stream with additional columns from the lookup stream.

#### SEE VIDEO🔼



# Sort Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/XyLVCH-v1Ag 

The sort transformation allow you to sort the incoming rows on the current data stream. 

You choose individual columns and sort them in ascending or descending order.

#### SEE VIDEO🔼





# New Branch in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/tU44UB7cqwk

**Add a new branch to do multiple sets of operations and transformations against same data stream**. 

Adding a new branch is useful when we want to use same source for multiple sinks.

#### SEE VIDEO🔼









# Select Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/wWIiIxf4ME4 

Use the **select transformation** to rename, drop or reorder columns. This transformation does not alter row data, but chooses which columns are propagated downstream.

#### SEE VIDEO🔼






# Pivot Transformation in Mapping Data Flow in Azure Data Factory

Video link :  https://youtu.be/ozQYffvt2aI

Use the **pivot transformation** to create multiple columns from the unique row values of a single columns.

#### SEE VIDEO🔼








# Unpivot Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/BzeFnHF6lIE

Use **Unpilot in ADF mapping data flow as a way to turn  an unormalized dataset into a more normalized version** by expanding values from multiple columns in a single record into multiple records with the same values in same column.

<span style="color:yellow">Completely opposite to pivot transformation </span>

#### SEE VIDEO🔼







# Surrogate Key Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/UquN1EVaGaM

Use Surrogate key transformation to add an incrementing key value to each row of data.

#### SEE VIDEO🔼






# Window Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/EMWa8XsmKok

**Window Transformation** is where you define window-based aggregations of columns in your data streams.

In the Expression Builder, you can define different types of aggregations that are based on data or time windows (SQL `OVER` clause) such as `LEAD`, `LAG`, `NTILE`, `CUMEDIST`, `RANK`, etc. 

A new field will be generated in your output that includes these aggregations. We can also include optional group fields.

#### SEE VIDEO🔼







# Alter Row Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/12Bt9N5lODA 

USe the **ALter Row transformation to set, insert, delete, update and upsert policies on rows**. We can add one-to-many conditions as expressions. These conditions should be specified in order of priority  as each row will be marked with the policy corresponding to the first-matching expression. Each of those conditions can result in a row (or rows) being inserted, updated, deleted or upserted.

**Alter row transformations will only operate on database or CosmosDB in our data flow**.

#### SEE VIDEO🔼






# Flatten Transformation in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/12Bt9N5lODA

Use the flatten transformation to **take array values inside the hierarchical structures such as JSON and unroll them into individual rows**. This process is known as <span style="color:yellow">denormalization</span>.

#### SEE VIDEO🔼





# Parameterize Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/6rKZ7Om1gKo 

**Mapping data flows in ADF** support the use of parameters. We can define parameters inside of our data flow defination, which can then be **reused throughout our expressions**.

We can use this capability to make our data flows general purpose, flexible and reusable.

#### SEE VIDEO🔼








# Validate Schema in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/6rKZ7Om1gKo

**Validate schema** option in source will look for the schema in source. **If any changes in the schema then it will make data flow to fail**.

#### SEE VIDEO🔼







# Schema Drift in Mapping Data Flow in Azure Data Factory

Video link : https://youtu.be/LS0u7DxhpDI

**Schema drift** is the case when our <span style="color:orange">sources often change metadata.</span>

**Field, columns and types can be added, removed, or changed on the go.**

Without handling for schema drift, your data flow becomes vulnerable to upstream data changes.

#### SEE VIDEO🔼

