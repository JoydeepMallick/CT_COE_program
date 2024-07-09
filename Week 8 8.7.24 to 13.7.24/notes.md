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

## Set Variable Activity in Azure Data Factory

Video link : https://youtu.be/rzDZdRifC40?si=rbMeactaJ97230-P

Use the set variable activity to set the value of an existing variable of type String, bool, or array defined in data factory pipeline.

### ⭐⭐demo : https://youtu.be/rzDZdRifC40?t=108



## Append Variable Activity in Azure Data Factory

Video link : https://youtu.be/aJuohp8a-fA?si=6VpmF8uU7PfPlwWE

Use append variable activity to add value to an exisiting array variable in Data Factory pipeline.

### ⭐⭐demo : https://youtu.be/aJuohp8a-fA?t=147



# User Properties in Azure Data Factory

Video link : https://youtu.be/0QExfRwhhDo?si=e5Y1SgHTH_rYBOgB





# Execute Pipeline Activity in Azure Data Factory

Video link : https://youtu.be/nc4IFKkkfXM?si=reIkSFn2TVLpOa-A





# Filter Activity in Azure Data Factory

Video link : https://youtu.be/y2KDonUDuPc?si=DCgdbk7RYQmiMcHj





# ForEach Activity in Azure Data Factory

Video link : https://youtu.be/KuWYuHlUwD0?si=tpv57z8zpSkoeHx_





# Get Metadata Activity in Azure Data Factory

Video link : https://youtu.be/_VNOabanIV4?si=SMCxIemXy_1AGFSi





# If Condition Activity in Azure Data Factory

Video link : https://youtu.be/pd-DJJUhnsw?si=H04JWM2nyTKQupUj





# Wait Activity in Azure Data Factory

Video link : https://youtu.be/JVNt4unI06Y?si=V1wLWDll4jTGDfnF





# Until Activity in Azure Data Factory

Video link : https://youtu.be/n8e_exWMH5k?si=ZzjrWBoqZZeiKsxG





# Web Activity in Azure Data Factory

Video link : https://youtu.be/rvIcklXCLVk?si=cDxTTvEV2Ig2AeMg





# WebHook Activity in Azure Data Factory

Video link : https://youtu.be/XQExOQ3KLhg?si=mBGS2hiz_8N0sKvZ





# Switch Activity in Azure Data Factory

Video link : https://youtu.be/-YwdbnEc_9Q?si=nb_kRJFAIk7f2i61





# Validation Activity in Azure Data Factory

Video link : https://youtu.be/Jesb-nLXtQ4?si=_2jLMxE1TzAKdAPP




# Lookup Activity in Azure Data Factory

Video link : https://youtu.be/Jesb-nLXtQ4?si=6xFhaN3BrX0AuWen





# Transform Data Activities Overview in Azure Data Factory

Video link : 





# Stored Procedure Activity in Azure Data Factory

Video link : 





# Data flow in Azure data factory

Video link : 





# Mapping Data Flow in Azure Data Factory

Video link : 





# Data Flow Activity in Azure Data Factory

Video link : 





# Mapping Data Flow Debug Mode in Azure Data Factory

Video link : 





# Filter Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Aggregate Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# JOIN Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Conditional Split Transformation in Mapping Data Flow in Azure data factory

Video link : 





# Derived Column Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Exists Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Union Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Lookup Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Sort Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# New Branch in Mapping Data Flow in Azure Data Factory

Video link : 





# Select Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Pivot Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Unpivot Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Surrogate Key Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Window Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Alter Row Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Flatten Transformation in Mapping Data Flow in Azure Data Factory

Video link : 





# Parameterize Mapping Data Flow in Azure Data Factory

Video link : 





# Validate Schema in Mapping Data Flow in Azure Data Factory

Video link : 





# Schema Drift in Mapping Data Flow in Azure Data Factory

Video link : 




