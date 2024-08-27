
# Clusters
Blog Link : 

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
Blog Link : 



# Jobs
Blog Link : 

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