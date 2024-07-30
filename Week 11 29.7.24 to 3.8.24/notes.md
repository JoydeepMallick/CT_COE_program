
### 🌟🌟🌟 Please watch the entire [playlist for databricks](https://www.youtube.com/playlist?list=PLMWaZteqtEaKi4WAePWtCSQCfQpvBT2U1)
<br/>

# Introduction to Azure Databricks
Video link : https://youtu.be/bO7Xad1gOFQ

**Azure Databricks** is **Apache Spark based anaytics platform** optimized for microsoft Azure cloud services platform.

![](https://www.sqlshack.com/wp-content/uploads/2020/03/azure-databricks-integration-with-other-services-.png)

### ⭐⭐read [this blog](https://www.sqlshack.com/a-beginners-guide-to-azure-databricks/)

Azure Databricks provides us one click setup, streamlined workflows, and interactive workspace that enables collaboration between data scientists, data engineers and business analysts.

![](./Screenshot%20(965).png)
![](./Screenshot%20(964).png)

Example : Companies providing a service or product always record customer feedback, collect info, and others which is unstructured also called the big data and then analyse the data with tools like databricks to make meaning out of it and then analyze the market risk of launching a new service or product and improve opon it.

* The processing of big data here is done using apache spark.

* Azure implemented Apache Spark within their ecosystem integrating it which is  **Azure Databricks**



#### ⭐⭐see demo

# Create Azure Databricks workspace using Azure portal
Video link : https://www.youtube.com/watch?v=S3lI9cpaUy8

<span style="color:yellow">😢😢😢Sad Prerequisites, no cracked approach found till now!!!</span>

![](./Screenshot%20(966).png)



#### ⭐⭐see demo

# Create Databricks community edition account
Video link : https://ct-lms-coe-frontend-dev.azurewebsites.net/learn/Data%20Engineering001

Databricks community edition is lifetime <span style="color:green">free databricks service with limited functions good for learning and experimenting.</span>

### We will use this since Azure Databricks is completely paid service with no free trial😢😢😢

Databricks when integrated with any cloud hosting provider like Azure, AWS, GCP ..... will be paid so avoid it if money is a issue.

#### <account of databricks is alredy made earlier, see previous weeks>

#### ⭐⭐see demo

# Workspace in Azure Databricks
Video link : https://www.youtube.com/watch?v=OUVUiVbI2UU


An Azure Databricks Workspace is an environment for accessing all the Azure Databricks assets.

Workspace organises below objects into folders :-
- Notebooks
- Libraries
- Experiments

We can manage the workspace using Workspace UI, the Databricks CLI, and the databricks Rest API.

<p style="color:yellow">
In the workspace UI we can get help by clicking ? icon on top right hand corner.
</p>
<p style="color:yellow">
The shortcut link displays keyboard shortcuts for working with notebooks.
</p>

#### ⭐⭐see demo

# Working with spark jobs in databricks
Video link : https://www.youtube.com/watch?v=9p4Evw7EzTw

## Create and Run a spark job

**Cluster** is a set of computational resources and configurations on which we can run workloads.

**Notebook** is a web based interface to a document that contains runnable code, visualizations and narrative text.



#### ⭐⭐see demo

# Azure Databricks architecture
Video link : https://www.youtube.com/watch?v=hpK0QaZSyEc

Azure Databricks is structured to enable secure cross functional team collaboration while keeping a significant amount of backend services managed by Azure  Databricks so we can stay focused on our data science, data analytics, and data engineering tasks.

Azure databricks operated on **<span style="color:yellow">control plane</span>** and **<span style="color:yellow">data plane</span>**.

* The **control plane** includes the backend services that Azure Databricks manages in its own Azure account. Notebook commands and many other workspace configurations are stored in the control plane and encrypted in the rest.

* The **data plane** is managed by our Azure account and is where our data resides. This is also where the data is processed.

### Read [microsoft docs](https://learn.microsoft.com/en-us/azure/databricks/getting-started/overview) and also [read this](https://www.bluetab.net/en/databricks-on-azure-an-architecture-perspective-part-1/)

![](https://learn.microsoft.com/en-us/azure/databricks/_static/images/getting-started/architecture-azure.png)

![](https://www.graphable.ai/wp-content/uploads/2023/10/databricks_06-1024x962.png)

![](https://www.bluetab.net/wp-content/uploads/2022/02/image10.png)

#### ⭐⭐see demo

# Databricks utilities
Video link : https://www.youtube.com/watch?v=nThRHMgbIVw

Databricks utlities (`dbutils`) makes it easy to perform powerful combination of tasks.

* to parameterise notebooks
* to chain notebooks
* to work with secrets

`dbutils` is available in Python, R and Scala notesbooks.

### List available utilities

To list available utilities with a short description for each utility, run `dbutils.help()` for python or scala.
```py
dbutils.help()
```

### List available commands for utility

To list available commands for an utility with a short desciption of each command, run `.help()` after the programmatic name for the utility.

```py
dbutils.fs.help()
```

To display help for a command run `help("<Command Name>")`.
```py
dbutils.fs.help("cp")
```



#### ⭐⭐see demo

# DBFS
Video link : https://youtu.be/_eTkax-Yj0k

Databricks Filesystem (DBFS) is a distributed file system mounted into an Azure Databricks workspace and available on Azure Databricks cluster. DBFS is an abstraction on top of scalable object storage.

The default storage location in DBFS is known as the <span style="color:yellow">DBFS root.</span>

* `/FileStore` : Imported data files, generated plots, and uploaded libraries

* `/databricks-datasets` : Sample public datasets

* `/databricks-results` : Files generated by downloading the full result of a query.




#### ⭐⭐see demo


# Widgets
Video link : https://youtu.be/JpcjbjDelfI

The Widgets utility allows you to parameterize notebooks.

Commands :-
`combobox`, `dropdown`, `get`, `getArguement`, `multiselect`, `remove`, `removeAll`, `text`

### Read [this databricks doc](https://docs.databricks.com/en/notebooks/widgets.html)

#### ⭐⭐see demo

There are 4 types of widgets:

 - `text`: Input a value in a text box.

- `dropdown`: Select a value from a list of provided values.

- `combobox`: Combination of text and dropdown. Select a value from a provided list or input one in the text box.

- `multiselect`: Select one or more values from a list of provided values.

# run() command of notebook

Video link : https://youtu.be/n53pCPqymK8

### `dbutils.notebook.run()`

- The notebook utility helps to chain notebooks and act on their results.

    Commands : `exit`, `run`

- Runs a notebook and returns it exit value.


#### ⭐⭐see demo

# exit() command of notebook
Video link : https://youtu.be/sg_GNfaBMEk

### `dbutils.notebook.exit()`

- The notebook utility helps to chain notebooks and act on their results.

    Commands : `exit`, `run`

- Exits a notebook with a value.

- Below cells after `exit()` command will get skipped.

#### ⭐⭐see demo

# creating mount point

Video link : https://youtu.be/XeyXd4KbIhI

Mount the specified source directory into DBFS at the specified mount point.

```py
dbutils.fs.mount(
    source= "wasbs://<container-name>@<storage-account-name>.blob.core.windows.net",
    mount_point="/mnt/<mount-name>",
    extra_config={
        "fs.azure.account.key.<storage-account-name>.blob.core.windows.net" : "Accountkey"
    }
)
```

#### ⭐⭐see demo

# Mount azure blob storage to azure databricks

Video link : https://youtu.be/8YL8T0kw75M

We can mount Azure Blob Storage either by using Account Key or By using SAS key.

```py
dbutils.fs.mount(
    source= "wasbs://<container-name>@<storage-account-name>.blob.core.windows.net",
    mount_point="/mnt/<mount-name>",
    extra_config={
        "<conf-key>" : "Accountkey"
    }
)
```
In case of :-

- Account key, `<conf-key>` is \
`fs.azure.account.key.<storage-account-name>.blob.core.windows.net`

- SAS key, `<conf-key>` is \
`fs.azure.sas.<container-name>.<storage-account-name>.blob.core.windows.net`



#### ⭐⭐see demo

# Mounts & refreshMounts
Video link : https://youtu.be/2jo0LfhD6Qk

### mounts command (`dbutils.fs.mounts`)

    Displays information about what is currently mounted within DBFS.

### refreshMounts command (`dbutils.fs.refreshMounts`)

    Forces all machines in cluster to refresh their mount cache, ensuring they receive the most recent information.



#### ⭐⭐see demo

# Update mount point

Video link : https://www.youtube.com/watch?v=YyjjFXYGnNA

Similar to `dbutils.fs.mounts` command, but updates an existing mount point instead of creating a new one. Returns an error if the mount point is not present.

#### ⭐⭐see demo

# Secret scope overview

Video link : https://www.youtube.com/watch?v=c0t5CRK95cs

Managing secrets begin with creating a secret scope. A secret scope is collection of secrets indentified by a name. A workspace is limited to a maximum of 100 secret scopes.

There are 2 types of secret scopes
1. Azure Key Vault-backed scopes
2. Datbricks-backed scopes 

### 1. Azure Key Vault-backed scopes

To reference secrets stored in an Azure Key Vault, we can create a secret scope backed by Azure Key Vault.

### 2. Datbricks-backed scopes 

A databricks-backed secret scope is stored in (backed by) an encrypted database owned and managed by Azure Databricks.  

#### ⭐⭐see demo

# Secrets utility
Video link : https://youtu.be/694AXxvREkg

### `dbutils.secrets`

The secret utility allows us to store and access sensitive credential information without making them visible in notebooks.

Commands : `get`, `getBytes`, `list`, `listScopes`



#### ⭐⭐see demo

# Access ADLS Gen 2 
Video link : https://youtu.be/h_mbpd0oqOE

Steps to access ADLS gen2:-

1. Create secret scope and secret
2. Set configuration for spark session using account key
3. Access storage

```py
spark.conf.set(
    "fs.azure.account.key.<storage-account-name>.dfs.core.windows.net",
    dbutils.secrets.get(
        scope="<scope-name>",
        key="<storage-account-access-key-name>"
    )
)
```

#### ⭐⭐see demo
