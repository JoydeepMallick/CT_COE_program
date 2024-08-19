# Unity Catalog

Read blog : https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/
 
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


