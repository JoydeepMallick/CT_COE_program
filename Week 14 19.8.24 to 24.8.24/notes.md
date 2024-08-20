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

Video Link : https://youtu.be/DEDcJ3R54mo


Watch DEMO
# Data Sharing

Read blog : https://learn.microsoft.com/en-us/azure/databricks/data-sharing/



# Delta Table

Read blog : https://hevodata.com/learn/databricks-delta-tables/ 



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


