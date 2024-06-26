## Entire video playlist is recommended :-

### https://www.youtube.com/playlist?list=PLGjZwEtPN7j8b9dPA0HrtJDptOB69B506

(personally felt above series is good for basics with practical.)

# AZURE storage tutorial

Video link :- https://www.youtube.com/watch?v=UzTtastcBsk&embeds_referring_euri=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net%2F&embeds_referring_origin=https%3A%2F%2Fct-lms-coe-frontend-dev.azurewebsites.net&source_ve_path=Mjg2NjY&feature=emb_logo

Azure storage offer massively scalable object store for **data objects**, a file system service for the cloud, a messaging store for reliable messaging and a NoSQL store.

Azure storage is :
- durable
- secure
- scalable
- managed
- accesible

![alt text](<Screenshot (835).png>)

## Blob Storage

Blob storage provides flat hierarchy of files.

![](<Screenshot (836).png>)

### Blob storage Access tier

Azure storage provides different options for accessing block blob based data based on usage patterns.

- Hot : optimized for frequent access to objects
- Cool : optimized for storing large amounts of data that is infrequently accessed and stored for at least 30 days

- Archive : optimized for data that can tolerate several hours of retrieval latency and will remain in the Archive tier for at least 180 days.

## File Storage

Managed file shares for cloud or on-promises deployments.

![alt text](<Screenshot (837).png>)

## File vs Blob storage

![alt text](<Screenshot (838).png>)

## Storage Queue

A messaging store for reliable messaging between application components.

![alt text](<Screenshot (839).png>)

## Table Storage

A NoSQL store for schemaless storage of structured data.

![alt text](<Screenshot (840).png>)

### Storage performance tier

General purpose storage accounts may be configured either for the following performance tiers :-

- A **standard** performance tier for storing blob, files, tables, queues, and Azure virtual machine disks.

- A **premium** performance tier for storing unmanaged virtual machine disks only.

## Data redundancy

Azure storage replicates multiple copies of our data.

Replication options for a storage account include :-
- Locally-redundant storage (**LRS**)
- Zone-redundant storage (**ZRS**)
- Geo-redundant storage (**GRS**)
- Read-access geo-redundant storage (**RA-GRS**)

### Locally-redundant storage(**LRS**)

![alt text](<Screenshot (841).png>)

### Zone-redundant storage (**ZRS**)

![alt text](<Screenshot (842).png>)

### Geo-redundant storage (**GRS**)

![alt text](<Screenshot (843).png>)

### Read-access geo-redundant storage (**RA-GRS**)

![alt text](<Screenshot (844).png>)

## See video for demo on how to set up account in  azure and do basic tasks

[how to sign up in azure](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal)

An Azure storage account contains all of your Azure Storage data objects: blobs, files, queues, and tables. The storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world over HTTP or HTTPS.

[Important video](https://youtu.be/UzTtastcBsk?t=476)

# Azure Data Lake Storage Gen2

<p>Data Lake Storage Gen2 converges the capabilities of <a href="../../data-lake-store/" data-linktype="relative-path">Azure Data Lake Storage Gen1</a> with Azure Blob Storage. For example, Data Lake Storage Gen2 provides file system semantics, file-level security, and scale. Because these capabilities are built on Blob storage, you also get low-cost, tiered storage, with high availability/disaster recovery capabilities.</p>

## What is a Data Lake?
A data lake is a **single, centralized repository where you can store all your data, both structured and unstructured**. A data lake enables your organization to quickly and more easily store, access, and analyze a wide variety of data in a single location. **With a data lake, you don't need to conform your data to fit an existing structure. Instead, you can store your data in its raw or native format, usually as files or as binary large objects (blobs)**.

Azure Data Lake Storage is a **cloud-based, enterprise data lake solution**. It's engineered to store massive amounts of data in any format, and to facilitate big data analytical workloads. You use it to capture data of any type and ingestion speed in a single location for easy access and analysis using various frameworks.

## Data Lake Storage Gen2
Azure Data Lake Storage Gen2 refers to the current implementation of Azure's Data Lake Storage solution. <span style="color:yellow">The previous implementation, Azure Data Lake Storage Gen1 will be retired on February 29, 2024.</span>

Unlike Data Lake Storage Gen1, Data Lake Storage Gen2 isn't a dedicated service or account type. Instead, it's implemented as a set of capabilities that you use with the Blob Storage service of your Azure Storage account. You can unlock these capabilities by enabling the hierarchical namespace setting.

**Data Lake Storage Gen2 includes the following capabilities.**

✓   Hadoop-compatible access

✓   Hierarchical directory structure

✓   Optimized cost and performance

✓   Finer grain security model

✓   Massive scalability

<h2 id="hadoop-compatible-access" class="heading-anchor">Hadoop-compatible access</h2>

<p>Azure Data Lake Storage Gen2 is primarily designed to work with Hadoop and all frameworks that use the Apache <a href="https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html" data-linktype="external">Hadoop Distributed File System (HDFS)</a> as their data access layer. Hadoop distributions include the <a href="data-lake-storage-abfs-driver" data-linktype="relative-path">Azure Blob File System (ABFS)</a> driver, which enables many applications and frameworks to access Azure Blob Storage data directly. The ABFS driver is <a href="data-lake-storage-abfs-driver" data-linktype="relative-path">optimized specifically</a> for big data analytics. The corresponding REST APIs are surfaced through the endpoint <code>dfs.core.windows.net</code>.</p>

## Hierarchical directory structure

<p>The <a href="data-lake-storage-namespace" data-linktype="relative-path">hierarchical namespace</a> is a key feature that <b>enables Azure Data Lake Storage Gen2 to provide high-performance data access at object storage scale and price</b>. You can use this feature to organize all the objects and files within your storage account into a hierarchy of directories and nested subdirectories. In other words, your Azure Data Lake Storage Gen2 <b>data is organized in much the same way that files are organized on your computer.</b></p>

Operations such as renaming or deleting a directory, **become single atomic metadata operations on the directory**. There's no need to enumerate and process all objects that share the name prefix of the directory.

## Optimized cost and performance
Azure Data Lake Storage Gen2 is priced at Azure Blob Storage levels. It builds on Azure Blob Storage capabilities such as automated lifecycle policy management and object level tiering to manage big data storage costs.

Performance is optimized because **you don't need to copy or transform data as a prerequisite for analysis. The hierarchical namespace capability of Azure Data Lake Storage allows for efficient access and navigation**. This architecture means that data processing requires fewer computational resources, reducing both the speed and cost of accessing data.

## Finer grain security model
The Azure Data Lake Storage Gen2 access control model supports both **Azure role-based access control (Azure RBAC)** and **Portable Operating System Interface for UNIX (POSIX) access control**lists (ACLs). There are also a few extra security settings that are specific to Azure Data Lake Storage Gen2. You can set permissions either at the directory level or at the file level. All stored data is encrypted at rest by using either Microsoft-managed or customer-managed encryption keys.

## Massive scalability
Azure Data Lake Storage Gen2 offers massive storage and accepts numerous data types for analytics. **It doesn't impose any limits on account sizes, file sizes, or the amount of data that can be stored in the data lake. Individual files can have sizes that range from a few kilobytes (KBs) to a few petabytes (PBs)**. Processing is executed at near-constant per-request latencies that are measured at the service, account, and file levels.

This design means that Azure Data Lake Storage Gen2 can easily and quickly scale up to meet the most demanding workloads. **It can also just as easily scale back down when demand drops**.

## Built on Azure Blob Storage
**The data that you ingest persist as blobs in the storage account. The service that manages blobs is the Azure Blob Storage service**. Data Lake Storage Gen2 describes the capabilities or "enhancements" to this service that caters to the demands of big data analytic workloads.

<p>Because these capabilities are built on Blob Storage, features such as diagnostic logging, access tiers, and lifecycle management policies are available to your account. Most Blob Storage features are fully supported, but some features might be supported only at the preview level and there are a handful of them that aren't yet supported. For a complete list of support statements, see <a href="storage-feature-support-in-storage-accounts" data-linktype="relative-path">Blob Storage feature support in Azure Storage accounts</a>. The status of each listed feature will change over time as support continues to expand.</p>

# Azure Data Factory(ADF)

Video link :- https://youtu.be/Mc9JAra8WZU?si=wJHdMdyk1lYEnmZ2

[Documentation](https://learn.microsoft.com/en-us/azure/data-factory/)

Azure cloud's ETL service for scale-out serverless data integration and data transformation. We can also lift and shift existing SSIS packages to Azure and run them with full compatibility in ADF.

Cloud based ETL and data integration service that allows you to create data driven workflows for orchestrating data movement and transforming data at scale.

## What is ETL ??

[read me](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl)

**extract, transform, load (ETL) is a data pipeline used to collect data from various sources**. It then transforms the data according to business rules, and it loads the data into a destination data store. The transformation work in ETL takes place in a specialized engine, and it often involves using staging tables to temporarily hold data as it is being transformed and ultimately loaded to its destination.

![](https://learn.microsoft.com/en-us/azure/architecture/data-guide/images/etl.png)

## Extract, load, transform (ELT)
**Extract, load, transform (ELT) differs from ETL solely in where the transformation takes place. In the ELT pipeline, the transformation occurs in the target data store**. Instead of using a separate transformation engine, the processing capabilities of the target data store are used to transform data. This simplifies the architecture by removing the transformation engine from the pipeline. Another benefit to this approach is that scaling the target data store also scales the ELT pipeline performance. However, ELT only works well when the target system is powerful enough to transform the data efficiently.

![](https://learn.microsoft.com/en-us/azure/architecture/data-guide/images/elt.png)


### [SQL server technical documentation](https://learn.microsoft.com/en-us/sql/sql-server/?view=sql-server-ver16&redirectedfrom=MSDN)

##  SSIS
**Microsoft SQL Server Integration Services (SSIS)** is a component of the Microsoft SQL Server database software that can be used to perform a broad range of data migration tasks.

SSIS is a platform for data integration and workflow applications. **It features a data warehousing tool used for data extraction, transformation, and loading (ETL)**. The tool may also be used to automate maintenance of SQL Server databases and updates to multidimensional cube data.

First released with Microsoft SQL Server 2005, SSIS replaced Data Transformation Services, which had been a feature of SQL Server since Version 7.0.

[Read more here](https://en.wikipedia.org/wiki/SQL_Server_Integration_Services)





# ETL in Azure
Video link :- https://www.youtube.com/watch?v=EpDkxTHAhOs

Data factory is a cloud  data integration service used to compose to compose data storage, movement, and processing services into data pipelines.

### real life example

Assume transfering some files from **Shop's cabinet** to **Home's cabinet**

All processes in between are done by **delivery boy**.

The delivery boys are managed by **delivery managers**.

![alt text](<Screenshot (850).png>)

## analogy with data factory

Please Please Please see the video to get the feel 🔥🔥🔥 :- https://youtu.be/EpDkxTHAhOs?list=PLGjZwEtPN7j8b9dPA0HrtJDptOB69B506&t=256

![alt text](<Screenshot (851).png>)

Data factory oversees all the Integration runtimes.  Multiple Integration runtime jobs are run in something called **pipeline**.

A pipeline can be one **copy activity** but usually its **more than one** as shown below.

![alt text](<Screenshot (852).png>)

Each copy activity is with 2 datasets :-
- **source dataset**
- **sink dataset**

Each of the datasets needs to have a access to a **linked service🔑** to connect to the source of data where we grab data or to target data where we store data.

![alt text](<Screenshot (853).png>)

So many **linked services** are not needed if we pull data from same source and dump it in a single source as shown below.

![alt text](<Screenshot (854).png>)

### See full demo

https://youtu.be/EpDkxTHAhOs?list=PLGjZwEtPN7j8b9dPA0HrtJDptOB69B506&t=311

# Data factory Parameterization

Video link :- https://www.youtube.com/watch?v=pISBgwrdxPM

Data factory allows for parameterization of pipelines via 3 elements :-

- parameters
- variables
- expressions 

### Parameters

simply are input values for operations in data factory. Each action has set of predefined parameters that needs to be supplied.

Additionally some block of pipelines and datasets allow to define custom parameters.

### Variables

temporary values that can be used within pipeline and workflow to control execution of the workflow.

Can be modified through **expression** using set variable action during the execution of the workflow.

### Expressions

JSON based formula, which allows for modification of variables or any parameters for pipeline, action or connection in Data Factory.

## Typical scenarios that mandate parameterization

- dynamic input file name coming from external service
- dynamic output table names
- appending dates to output
- changing connection parameters like database name
- conditional programming

......and so on


If a single car CSV dataset is to be stored in car table dataset we need to create a `car csv dataset` and `car table dataset` and then have an activity to add data i.e. 3 steps as shown below.

![alt text](<Screenshot (846).png>)

Hence 2 tables cars and planes would be

![alt text](<Screenshot (847).png>)

Hence 20 tables will need about 60 data objects which highly unsatisfactory. Hence we need to use paramterised datasets.

Hence we declare a parameterized dataset with parameters and then pass dynamic variables through the pipeline and then pass cars and plane csv set through the parameterised dataset and pass the cars and planes tables dataset also through parameterised dataset. This helps reduction of extra 20 to 40 data objects.

![alt text](<Screenshot (849).png>)

We can even **parameterize pipelines** to further reduce the amount of data wherein we can grab the files externally thorugh execution and hence copy activity will be once because it will accept parameters as well.

### See demo video from below

link :- https://youtu.be/pISBgwrdxPM?t=225