
# Clusters
Blog Link : https://learn.microsoft.com/en-us/azure/databricks/compute/

Azure Databricks compute **refers to the selection of computing resources available in the Azure Databricks workspace**. Users need access to compute to run data engineering, data science, and data analytics workloads, such as production ETL pipelines, streaming analytics, ad-hoc analytics, and machine learning.

Users can either connect to existing compute or create new compute if they have the proper permissions.

You can view the compute you have access to using the Compute section of the workspace:

![](https://learn.microsoft.com/en-us/azure/databricks/_static/images/compute/compute-page.png)

## Types of compute
These are the types of compute available in Azure Databricks:

1. **Serverless compute for notebooks**: On-demand, scalable compute used to execute SQL and Python code in notebooks.

2. **Serverless compute for jobs**: On-demand, scalable compute used to run your Databricks jobs without configuring and deploying infrastructure.

3. **All-Purpose compute**: Provisioned compute used to analyze data in notebooks. You can create, terminate, and restart this compute using the UI, CLI, or REST API.

4. **Job compute**: Provisioned compute used to run automated jobs. The Azure Databricks job scheduler automatically creates a job compute whenever a job is configured to run on new compute. The compute terminates when the job is complete. You cannot restart a job compute.

5. **Instance pools**: Compute with idle, ready-to-use instances, used to reduce start and autoscaling times. You can create this compute using the UI, CLI, or REST API.

6. **Serverless SQL warehouses**: On-demand elastic compute used to run SQL commands on data objects in the SQL editor or interactive notebooks. You can create SQL warehouses using the UI, CLI, or REST API.

7. **Classic SQL warehouses**: Used to run SQL commands on data objects in the SQL editor or interactive notebooks. You can create SQL warehouses using the UI, CLI, or REST API.

## Databricks Runtime
Databricks Runtime is the **set of core components that run on your compute**. The Databricks Runtime is a configurable setting in all-purpose of jobs compute but autoselected in SQL warehouses.

Each Databricks Runtime version includes updates that improve the usability, performance, and security of big data analytics. The Databricks Runtime on your compute adds many features, including:

* Delta Lake, a next-generation storage layer built on top of Apache Spark that provides ACID transactions, optimized layouts and indexes, and execution engine improvements for building data pipelines.
* Installed Java, Scala, Python, and R libraries.
* Ubuntu and its accompanying system libraries.
* GPU libraries for GPU-enabled clusters.
* Azure Databricks services that integrate with other components of the platform, such as notebooks, jobs, and cluster management.

## Runtime versioning
Databricks Runtime versions are released on a regular basis:

- Long Term Support versions are represented by an **LTS qualifier** (for example, 3.5 LTS). For each major release, we declare a “canonical” feature version, for which we provide three full years of support.    
- Major versions are represented by an increment to the version number that precedes the decimal point (the jump from 3.5 to 4.0, for example). They are released when there are major changes, some of which may not be backwards-compatible.
- Feature versions are represented by an increment to the version number that follows the decimal point (the jump from 3.4 to 3.5, for example). Each major release includes multiple feature releases. Feature releases are always backward compatible with previous releases within their major release.


# Notebooks
Blog link : https://learn.microsoft.com/en-us/azure/databricks/notebooks/

Notebooks are a common tool in data science and machine learning for developing code and presenting results. In Azure Databricks, notebooks are the primary tool for creating data science and machine learning workflows and collaborating with colleagues. Databricks notebooks provide real-time coauthoring in multiple languages, automatic versioning, and built-in data visualizations.

## How to import and run example notebooks
The Azure Databricks documentation includes many example notebooks that are intended to illustrate how to use Databricks capabilities. To import one of these notebooks into a Databricks workspace:

1. Click `Copy link for import` at the upper right of the notebook preview that appears on the page.

2. In the workspace browser, navigate to the location where you want to import the notebook.

3. Right-click the folder and select Import from the menu.

4. Click the URL radio button and paste the link you just copied in the field.
    ![](https://learn.microsoft.com/en-us/azure/databricks/_static/images/notebooks/import-nb-from-url.png)

5. Click Import. The notebook is imported and opens automatically in the workspace. Changes you make to the notebook are saved automatically.

6. To run the notebook, click `Run all` button at the top of the notebook. For more information about running notebooks and individual notebook cells

# Workflows
Blog Link : https://learn.microsoft.com/en-us/azure/databricks/jobs/

Databricks Workflows provides a **collection of tools that allow you to schedule and orchestrate data processing tasks on Azure Databricks**. You use Databricks Workflows to configure Databricks Jobs.

## What are Databricks jobs?
A Databricks job allows you to **configure tasks to run in a specified compute environment on a specified schedule**. Along with Delta Live Tables pipelines, jobs are the primary tool used on Azure Databricks to deploy data processing and ML logic into production.

Jobs can vary in complexity from a single task running a Databricks notebook to thousands of tasks running with conditional logic and dependencies.

## How can I configure and run jobs?
You can create and run a job using the Jobs UI, the Databricks CLI, or by invoking the Jobs API. You can repair and re-run a failed or canceled job using the UI or API. You can monitor job run results using the UI, CLI, API, and notifications (for example, email, webhook destination, or Slack notifications).

## What is the minimum configuration needed for a job?
All jobs on Azure Databricks require the following:

- Source code that contains logic to be run.
- A compute resource to run the logic. The compute resource can be serverless compute, classic jobs compute, or all-purpose compute. See Use Azure Databricks compute with your jobs.
- A specified schedule for when the job should be run or a manual trigger.
- A unique name.


## What is a task?
A task represents a unit of logic in a job. Tasks can range in complexity and include the following:

- A notebook
- A JAR
- A SQL query
- A DLT pipeline
- Another job
- Control flow tasks

You can control the execution order of tasks by specifying dependencies between them. You can configure tasks to run in sequence or parallel.

Jobs interact with state information and metadata of tasks, but task scope is isolated. You can use task values to share context between scheduled tasks.

## What control flow options are available for jobs?
When you configure jobs and tasks within jobs, you can customize settings that control how the entire job and individual tasks run.

### trigger types
You must specify a trigger type when you configure a job. You can choose from the following trigger types:

- Scheduled
- File arrival
- Continuous

You can also choose to manually trigger your job, but this is mostly reserved for specific use cases such as:

- You use an external orchestration tool for triggering jobs using REST API calls.
- You have a job that runs rarely that requires a human-in-the-loop for validation or resolving data quality issues.
- You are running a workload that only needs to be run once or a few times, such as a migration.


### Retries
Retries specifies how many times a particular job or task should be re-run if the job fails with an error message. Errors are often transient and resolved through restart, and some features on Azure Databricks such as schema evolution with Structured Streaming assume that you run jobs with retries in order to reset the environment and allow a workflow to proceed.

An option for configuring retries appears in the UI for supported contexts. These include the following:

- You can specify retries for an entire job, meaning the whole job restarts if any task fails.
- You can specify retries for a task, in which case the task restarts up to the specified number of times if it encounters an error.


When running in continuous trigger mode, Databricks automatically retries with exponential backoff. 

### Run if conditional tasks
You can use the Run if task type to specify conditionals for later tasks based on the outcome of other tasks. You add tasks to your job and specify upstream-dependent tasks. Based on the status of those tasks, you can configure one or more downstream tasks to run. Jobs support the following dependencies:

- All succeeded
- At least one succeeded
- None failed
- All done
- At least one failed
- All failed

### If/else conditional tasks
You can use the If/else task type to specify conditionals based on some value. 

Jobs support `taskValues` that you define within your logic and allow you to return the results of some computation or state from a task to the jobs environment. You can define If/else conditions against `taskValues`, job parameters, or dynamic values.

Azure Databricks supports the following operands for conditionals:

`==`
`!=`
`>`
`>=`
`<`
`<=`

### For each tasks
Use the `For each` task to run another task in a loop, passing a different set of parameters to each iteration of the task.

Adding the `For each` task to a job requires defining two tasks: The `For each` task and a nested task. The nested task is the task to run `for each` iteration of the `For each` task and is one of the standard Azure Databricks Jobs task types. Multiple methods are supported for passing parameters to the nested task.

### Duration threshold
You can specify a duration threshold to either send a warning or stop a task or job if a specified duration is exceeded. Examples of when you might want to configure this setting include the following:

- You have tasks that are prone to getting stuck in a hung state.
- You need to warn an engineer if an SLA for a workflow is exceeded.
- You want to fail a job configured with a large cluster to avoid unexpected costs.


### Concurrency
Most jobs are configured with the default concurrency of 1 concurrent job. This means that if a previous job run has not completed by the time a new job should be triggered, the next job run is skipped.

There are some use cases for increased concurrency, but most workloads do not require altering this setting.

## How can I monitor jobs?
You can **receive notifications when a job or task starts, completes, or fails**. You can send notifications to one or more email addresses or system destinations. 

System tables include a lakeflow schema where you can view records related to job activity in your account. 

You can also join the jobs system tables with billing tables to monitor the cost of jobs across your account. 

## Limitations
The following limitations exist:

- A workspace is limited to 1000 concurrent task runs. A `429 Too Many Requests` response is returned when you request a run that cannot start immediately.
- The number of jobs a workspace can create in an hour is limited to 10000 (includes “runs submit”). This limit also affects jobs created by the REST API and notebook workflows.
- A workspace can contain up to 12000 saved jobs.
- A job can contain up to 100 tasks.

## Can I manage workflows programmatically?

Databricks provides tools and APIs that allow you to schedule and orchestrate your workflows programmatically, including the following:

- Databricks CLI
- Databricks Asset Bundles
- Databricks extension for Visual Studio Code
- Databricks SDKs
- Jobs REST API

### Workflow orchestration with Apache AirFlow
You can use Apache Airflow to manage and schedule your data workflows. With Airflow, you define your workflow in a Python file, and Airflow manages scheduling and running the workflow.

### Workflow orchestration with Azure Data Factory
Azure Data Factory (ADF) is a cloud data integration service that lets you compose data storage, movement, and processing services into automated data pipelines. You can use ADF to orchestrate an Azure Databricks job as part of an ADF pipeline.

ADF also provides built-in support to run Databricks notebooks, Python scripts, or code packaged in JARs in an ADF pipeline.

# Jobs
Blog Link : https://kb.databricks.com/jobs/job-run-dash.html

# Job API
Blog Link : 


# Cluster API
Blog Link : 


# Rest API
Blog Link : 


# Libraries
Blog Link : 


# Repos
Blog Link : 


# DBFS
Blog Link : 


# Working with Files

# Migration

# Spark Monitoring

# Query Databases using JDBC

# Optimization & Performance