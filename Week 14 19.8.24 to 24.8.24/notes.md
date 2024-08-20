# Unity Catalog

### ⭐⭐⭐Read blog : https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/
 
Unity Catalog provides **centralized access control, auditing, lineage, and data discovery capabilities across Azure Databricks workspaces**.

![](https://learn.microsoft.com/en-us/azure/databricks/_static/images/unity-catalog/with-unity-catalog.png
)

Key features of Unity Catalog include:

* **Define once, secure everywhere**: Unity Catalog offers a single place to administer data access policies that apply across all workspaces.
* **Standards-compliant security model**: Unity Catalog’s security model is based on **standard ANSI SQL and allows administrators to grant permissions in their existing data lake using familiar syntax**, at the level of catalogs, schemas (also called databases), tables, and views.
* **Built-in auditing and lineage**: Unity Catalog **automatically captures user-level audit logs that record access to your data**. Unity Catalog also captures lineage data that tracks how data assets are created and used across all languages.
* **Data discovery**: Unity Catalog lets you tag and document data assets, and provides a search interface to help data consumers find data.
* **System tables (Public Preview)**: Unity Catalog lets you easily access and query your account’s operational data, including audit logs, billable usage, and lineage.


## The Unity Catalog object model

In Unity Catalog, all metadata is registered in a metastore. **The hierarchy of database objects in any Unity Catalog metastore is divided into three levels**, represented as a three-level namespace (`catalog.schema.table-etc`) when you reference tables, views, volumes, models, and functions.

![](https://learn.microsoft.com/en-us/azure/databricks/_static/images/unity-catalog/object-model.png)

## Metastores
The metastore is the <span style="color:yellow">top-level container for metadata in Unity Catalog. It registers metadata about data and AI assets and the permissions that govern access to them.</span> For a workspace to use Unity Catalog, it must have a Unity Catalog metastore attached.


## Object hierarchy in the metastore
In a Unity Catalog metastore, the three-level database object hierarchy consists of catalogs that contain schemas, which in turn contain data and AI objects, like tables and models.

### Level one:

**Catalogs** are used to organize your data assets and are typically used as the top level in your data isolation scheme. Catalogs often mirror organizational units or software development lifecycle scopes. 

**Non-data securable objects**, such as storage credentials and external locations, are used to managed your data governance model in Unity Catalog. These also live directly under the metastore. 

### Level two:

**Schemas (also known as databases)** contain tables, views, volumes, AI models, and functions. Schemas organize data and AI assets into logical categories that are more granular than catalogs. Typically a schema represents a single use case, project, or team sandbox. 

### Level three:

**Volumes** are logical volumes of unstructured, non-tabular data in cloud object storage. Volumes can be either managed, with Unity Catalog managing the full lifecycle and layout of the data in storage, or external, with Unity Catalog managing access to the data from within Azure Databricks, but not managing access to the data in cloud storage from other clients. 

**Tables** are collections of data organized by rows and columns. Tables can be either managed, with Unity Catalog managing the full lifecycle of the table, or external, with Unity Catalog managing access to the data from within Azure Databricks, but not managing access to the data in cloud storage from other clients. 

**Views** are saved queries against one or more tables. 

**Functions** are units of saved logic that return a scalar value or set of rows. 

**Models** are AI models packaged with MLflow and registered in Unity Catalog. 

## Other securable objects
In addition to the database objects and AI assets that are contained in schemas, Unity Catalog also governs access to data using the following securable objects:

* **Storage credentials**, which encapsulate a long-term cloud credential that provides access to cloud storage. 

* **External locations**, which contain a reference to a storage credential and a cloud storage path. External locations can be used to create external tables or to assign a managed storage location for managed tables and volumes. 

* **Connections**, which represent credentials that give read-only access to an external database in a database system like MySQL using Lakehouse Federation. 

* **Clean rooms**, which represent a Databricks-managed environment where multiple participants can collaborate on projects without sharing underlying data with each other.

* **Shares**, which are Delta Sharing objects that represent a read-only collection of data and AI assets that a data provider shares with one or more recipients.

* **Recipients**, which are Delta Sharing objects that represent an entity that receives shares from a data provider.

* **Providers**, which are Delta Sharing objects that represent an entity that shares data with a recipient.


## Granting and revoking access to database objects and other securable objects in Unity Catalog

You can grant and revoke access to securable objects at any level in the hierarchy, including the metastore itself. Access to an object implicitly grants the same access to all children of that object, unless access is revoked.

You can use typical ANSI SQL commands to grant and revoke access to objects in Unity Catalog. For example:

```SQL
GRANT CREATE TABLE ON SCHEMA mycatalog.myschema TO `finance-team`;
```

You can also use Catalog Explorer, the Databricks CLI, and REST APIs to manage object permissions.

![](https://learn.microsoft.com/en-us/azure/databricks/_static/images/unity-catalog/catalog-explorer-grant.png)


## File format support
Unity Catalog supports the following table formats:

* **Managed tables** must use the **delta table** format.
* **External tables**can use **delta, CSV, JSON, avro, parquet, ORC, or text**.

## Limitations
Unity Catalog has the following limitations. Some of these are specific to older Databricks Runtime versions and compute access modes.

Structured Streaming workloads have additional limitations, depending on Databricks Runtime and access mode. See Compute access mode limitations for Unity Catalog.

Databricks releases new functionality that shrinks this list regularly.

- Groups that were previously created in a workspace (that is, workspace-level groups) **cannot be used** in Unity Catalog `GRANT`   statements. This is to **ensure a consistent view of groups that can span across workspaces**. To use groups in `GRANT` statements, create your groups at the account level and update any automation for principal or group management (such as SCIM, Okta and Microsoft Entra ID connectors, and Terraform) to reference account endpoints instead of workspace endpoints. See Difference between account groups and workspace-local groups.

- Workloads in R do not **support the use of dynamic views for row-level or column-level security on compute running Databricks Runtime 15.3 and below**.

- Use a single-user compute resource running Databricks Runtime 15.4 LTS or above for workloads in R that query dynamic views (Public Preview). Such workloads also **require a workspace that is enabled for serverless compute**. 

- Shallow clones are unsupported in Unity Catalog on compute running Databricks Runtime 12.2 LTS and below. You can use shallow clones to create managed tables on Databricks Runtime 13.3 LTS and above. **You cannot use them to create external tables, regardless of Databricks Runtime version**. 

- **Bucketing is not supported for Unity Catalog tables.** If you run commands that try to create a bucketed table in Unity Catalog, it will **throw an exception**.

- Writing to the same path or Delta Lake table from workspaces in multiple regions **can lead to unreliable performance if some clusters access Unity Catalog and others do not**.

- Custom partition schemes created using commands like `ALTER TABLE ADD PARTITION` are not supported for tables in Unity Catalog. Unity Catalog **can access tables that use directory-style partitioning**.

- Overwrite mode for DataFrame write operations into Unity Catalog is supported only for Delta tables, **not for other file formats**. The user must have the `CREATE` privilege on the parent schema and must be the owner of the existing object or have the `MODIFY` privilege on the object.

- **Python UDFs are not supported in Databricks Runtime 12.2 LTS and below**. This includes UDAFs, UDTFs, and Pandas on Spark (applyInPandas and mapInPandas). Python scalar UDFs are supported in Databricks Runtime 13.3 LTS and above.

- **Scala UDFs are not supported in Databricks Runtime 14.1 and below on shared clusters**. Scala scalar UDFs are supported in Databricks Runtime 14.2 and above on shared clusters.

- **Standard Scala thread pools are not supported. Instead, use the special thread pools in `org.apache.spark.util.ThreadUtils`**, for example, `org.apache.spark.util.ThreadUtils.newDaemonFixedThreadPool`. However, the following thread pools in `ThreadUtils` are **not supported**: `ThreadUtils.newForkJoinPool` and any `ScheduledExecutorService` thread pool.

- **Audit logging is supported for Unity Catalog events at the workspace level only**. Events that take place at the account level without reference to a workspace, such as creating a metastore, are not logged.


# Auto loader

### ⭐⭐Video Link : https://youtu.be/DEDcJ3R54mo

Autoloader allows Databricks users to incrementally ingest data into **Delta Lake** from a variety of data sources. AutoLoader is an optimized cloud file source for **Apache Spark** that loads data continuously and efficiently from cloud storage as new data arrives. A data ingestion network of partner integrations allow you to ingest data from hundreds of data sources directly into Delta Lake.

![](./Screenshot%20(1184).png)
![](./Screenshot%20(1185).png)
![](./Screenshot%20(1186).png)
![](./Screenshot%20(1187).png)
![](./Screenshot%20(1188).png)

### See demo from current [timeline](https://youtu.be/DEDcJ3R54mo?t=393)

# Data Sharing

Read blog : https://learn.microsoft.com/en-us/azure/databricks/data-sharing/  or https://docs.databricks.com/en/data-sharing/index.html

## Share data and AI assets securely with users in other organizations

This article introduces the following features that enable you to share the data and AI assets you have in Azure Databricks with users outside your organization or on different metastores within your Azure Databricks account:

- **Delta Sharing** is the core of the Azure Databricks secure data sharing platform, enabling you to share data and AI assets in Databricks with users outside your organization, whether those users use Databricks or not. Also available as an open-source project for sharing tabular data, using it in Databricks adds on the ability to share non-tabular, unstructured data (volumes), AI models, views, filtered data, and notebooks. Delta Sharing also provides the backbone for Databricks Marketplace and Databricks Clean Rooms.
- **Databricks Marketplace** is an open forum for exchanging data products. Providers must have a Databricks account, but recipients can be anybody. Marketplace assets include **datasets, Databricks notebooks, Databricks Solution Accelerators, and machine learning (AI) models**. Datasets are typically made available as catalogs of tabular data, although non-tabular data, in the form of Azure Databricks volumes, is also supported. Solution Accelerators are available as clonable Git repos.
- **Clean Rooms** uses Delta Sharing and serverless compute to provide a secure and privacy-protecting environment where multiple parties can share sensitive enterprise data and collaborate without direct access to each other’s data. With Clean Rooms, users from other Databricks accounts can collaborate to generate unique insights about shared projects, such as advertising campaigns, investment decisions, or research and development, without sharing access to sensitive underlying data. When you collaborate in a clean room, your data stays in place and you are always in control of where and how the data is being used.

# Delta Table

Read blog : https://hevodata.com/learn/databricks-delta-tables/ 

 **Databricks’ Delta Table** is designed to handle batch as well as streaming data on big feeds to reduce transmit-time and send the updated data to facilitate Data Pipelines at ease.

## Need for Databricks Delta Lakes

Organizations collect large amounts of data from different sources that can be — **schema-based, schema-less, or streaming data**. Such large volumes of data can be stored either in a data warehouse or data lake. Companies are often in a **dilemma while selecting appropriate data storage tools for storing incoming data and then streamlining the flow of data for analysis**. 

However, Databricks fuses the performance of data warehouses and the affordability of data lakes in a **single Cloud-based repository** called <span style="color:yellow">Lake House</span>. The **Lake House (Data Lake + Data Warehouse) Architecture** built on top of the data lake is called <span style="color:yellow">Delta Lake</span>. Below are a few aspects that describe the need for Databricks’ Delta Lake:

* It is an **open format storage layer** that delivers reliability, security, and performance on your Data Lake for both streaming and batch operations.
* It not only houses structured, semi-structured, and unstructured data but also provides Low-cost Data Management solutions. 
* Databricks Delta Lake also handles **ACID** (Atomicity, Consistency, Isolation, and Durability) transactions, scalable metadata handling, and data processing on existing data lakes.


## Delta Live Tables: Data pipelines
Delta Live Tables **handle the flow of data between several Delta tables, making it easier for data engineers to create and manage ETL**. Delta Live Tables pipeline serves as its primary execution unit. Delta Live Tables enables declarative pipeline building, better data reliability, and cloud-scale production. Users can run both streaming and batch operations on the same table, and the data is readily available for querying. You define the transformations to be applied to your data, and Delta Live Tables handles job orchestration, monitoring, cluster management, data quality, and error management. Delta Live Tables Enhanced Autoscaling can manage spiky and erratic streaming workloads.

## Delta Lake: Open Source Data Management for Data Lake
Delta Lake is an **open-source storage layer** that improves data lake dependability by providing a transactional storage layer to cloud-stored data. **It supports data versioning, ACID transactions, and rollback capabilities**. It helps you manage batch and streaming data in a cohesive manner.

Delta tables are constructed on top of this storage layer and provide a table abstraction, making it simple to interact with vast amounts of structured data via SQL and the DataFrame API.


## 5 Databricks Delta Functionalities

Below are a few functionalities offered by Delta to derive compelling solutions for Data Engineers:

### 1) Query Performance
As the data grows exponentially over time, query performance becomes a crucial factor. **Delta improves the performance from 10 to 100 times faster as compared to Apache Spark on the Parquet (human unreadable) file format**. Below are some techniques that assist in improving the performance:

- Indexing: Databricks Delta creates and maintains Indexes on the tables to arrange queried data.
- Skipping: Databricks Delta helps maintain file statistics so that only relevant portions of the data are read.
- Compression: Databricks Delta consumes less memory space by efficiently managing Parquet files to optimize queries.
- Caching: Databricks Delta automatically caches highly accessed data to improve run times for commonly run queries.

### 2) Optimize Layout
Delta optimizes table size with a built-in “`optimize`” command. End users can optimize certain portions of the Databricks Delta Table that are most relevant instead of querying an entire table. It **saves the overhead cost of storing metadata and can help speed up queries**.

### 3) System Complexity
System Complexity increases the effort required to complete data-related tasks, making it difficult while responding to any changes. With Delta, organizations solve system complexities by:

- Providing flexible Data Analytics Architecture and response to any changes.
- Writing Batch and Streaming data into the same table.
- Allow a simpler architecture and quicker Data Ingestion to query results.
- The ability to ‘infer schemas’ for the data input reduces the effort required to manage schema changes.


### 4) Automated Data Engineering
Data engineering can be simplified with Delta Live Tables that provide a simpler way to build and manage Data Pipelines for the latest, high-quality data in Delta Lake. It aids Data Engineering teams in developing and managing ETL process with Declarative Pipeline Development as well as Cloud-scale production operation to build Lake House foundations to ensure good data movement.

### 5) Time Travel
Time travel allows users to roll back in case of bad writes. Some Data Scientists run models on datasets for a specific time, and this ability to reference previous versions becomes useful for Temporal Data Management. A user can query Delta Tables for a specific timestamp because any change in Databricks Delta Table creates new table versions. These tasks help data pipelines to audit, roll back accidental deletes, or reproduce experiments and reports. 

## What is Databricks Delta Table?
A Databricks Delta Table **records version changes or modifications in a feature class of table in Delta Lake**. Unlike traditional tables that store data in a row and column format, the Databricks Delta Table facilitates ACID transactions and time travel features to store metadata information for quicker Data Ingestion. Data stored in a Databricks Delta Table is a secure Parquet file format that is an encoded layer over data.

**These stale data files and logs of transactions are converted from `‘Parquet’` to `‘Delta’` format to reduce custom coding in the Databricks Delta Table**. It also facilitates some advanced features that provide a history of events, and more flexibility in changing content — **update, delete and merge operations** — to avoid dDduplication.

Every transaction performed on a Delta Lake table contains an ordered record of a transaction log called <span style="color:yellow">DeltaLog</span>. Delta Lake breaks the process into discrete steps of one or more actions whenever a user performs modification operations in a table. It facilitates multiple readers and writers to work on a given Databricks Delta Table at the same time. These actions are recorded in the ordered transaction log known as commits. For instance, if a user creates a transaction to add a new column to a Databricks Delta Table while adding some more data, Delta Lake would break that transaction into its consequent parts.

Once the transaction is completed in the Databricks Delta Table, the files are added to the transaction log like the following commits:

- Update Metadata: To change the Schema while including the new column to the Databricks Delta Table.
- Add File: To add new files to the Databricks Delta Table.


## Delta Table Operation and Commands
* ### Time Travel
    * **Feature Overview**: Delta Lake’s time travel feature allows users to access and query historical versions of a Delta table. This is achieved by querying the table as it existed at a specific time or using a version number.
    * **Use Cases**:
        * **Data Audits**: Review historical changes and track modifications over time for auditing purposes.
        * **Debugging**: Investigate issues or discrepancies by examining the state of the data at previous points in time.
* ### Vacuum Command
    * **Command Overview**: The VACUUM command removes old, obsolete data files from a Delta table, which are no longer needed after data deletions or updates.
    * **Managing Data Retention Policies**: Use the VACUUM command to configure retention policies and specify how long to keep historical data before it is eligible for removal. This helps balance data retention needs and storage optimization.
* ### MERGE Command
    * **Data Synchronization**: Integrate updates from external data sources into the Delta table while maintaining consistency.
    * **Data Enrichment**: Apply changes and updates to existing data while inserting new records to ensure the table reflects the most current state of the data.

## Delta Table Use Cases and Applications
Delta tables offer robust features for managing and processing large-scale data, making them highly versatile across various use cases and applications. Here are some key use cases and applications of Delta tables:

* Delta Lake extends the capabilities of data lakes by adding transactional support, schema enforcement, and data quality features. It enables data lakes to handle large datasets efficiently and reliably.
* Delta tables are ideal for data warehousing environments where historical data needs to be stored, queried, and analyzed. They support ACID transactions, ensuring data integrity and consistency.

## Delta Tables vs. Delta Live Tables

Delta table | Delta Live tables
------------|------------------
Delta tables are a way of storing data in tables| Delta Live Tables enable you to explain the flow of data across these tables explicitly. Delta Live Tables is an explicit framework that can manage multiple delta tables by building them and keeping them updated. 
In essence, Delta Tables is an architecture of data tables. |On the other hand, Delta Live Tables is a framework of data pipelines.

## Features of Databricks Delta Table
Delta Live Table (DLT) is a framework that can be used for building reliable, maintainable, and testable data processing pipelines on Delta Lake. It simplifies ETL Development, automatic data testing, and deep visibility for monitoring as well as recovery of pipeline operation. To create a Databricks Delta Table, one can use an existing **Apache Spark SQL code** and change the written format from **parquet, CSV, or JSON to Delta**.

The Delta Lake consists of a transaction log that solely serves as a source of truth — **the central repository that tracks all changes made by users in a Databricks Delta Table**. The transaction log is the mechanism through which Delta Lake guarantees one of the ACID properties called Atomicity. It assures users whether an operation (like INSERT or UPDATE) performed on a Data Lake is either complete or incomplete.

Below are a few features offered by Databricks Delta Live Table:

- **Automate Data Pipeline**: Defines an end-to-end Data Pipeline by specifying Data Source, Transformation Logic, and Destination state of Data instead of manually combining complicated data processing jobs. Delta Live Table automatically maintains all data dependencies across the Pipeline and reuse ETL pipelines with independent Data Management. It can also run batch or streaming data while specifying incremental or complete computation for each Databricks Delta Table.
- **Automatic Testing**: Prevents bad data from flowing into tables through validation and integrity checks, it avoids Data Quality errors. It also allows you to monitor Data Quality trends to derive insight about required changes and the performance of data.
- **Automatic Error-Handling**: Reduces downtime and timestamp of Data Pipelines. Delta Live Table gains deeper visibility into Pipeline operation with tools that visually track operational statistics and data lineage. It also speeds up maintenance with single-click deployment and upgrades.

## More Delta things on Azure Databricks
Following are descriptions of other delta features included in Databricks.

### Delta Sharing
Delta Sharing is an **open standard for secure data sharing that allows organizations to share data regardless of the computing platform**.

### Delta Engine
Databricks has a **large data query optimizer that makes use of open-source Delta Lake technology**. The Delta engine improves the performance of Databricks SQL, Spark SQL, and DataFrame operations by shifting computation onto the data.

### Delta Lake Transaction Log (AKA DeltaLogs)
DeltaLogs is the only source that tracks all modifications made to the table by users and the method that ensures atomicity through Delta Lake. The transaction log is critical for understanding Delta Lake since it is the common pattern that runs through its most important features.

- ACID transactions
- Scalable metadata handling
- Time travel


# Databricks Photon Engine

Read blog : https://learn.microsoft.com/en-us/azure/databricks/clusters/photon 




# Delta Lake

Read blog : https://learn.microsoft.com/en-us/azure/databricks/delta/



# Data warehousing

Read blog : https://learn.microsoft.com/en-us/azure/databricks/sql/



# Data Lakehouse

Read blog : https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/



# Delta Live tables

Read blog : https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/



# Advancing in DLT

Video Link : https://youtu.be/0K_CLhwRHAM


Watch DEMO
# Structured Streaming
Read blog : https://learn.microsoft.com/en-us/azure/databricks/structured-streaming/


