# Assignment

1. Create **4 notebooks** in Databricks that read from single table and inserts/updates data into **5 respective output Delta tables** 

2. Create an **orchestration notebook** that calls the other notebooks using `Dbutils` 

3. Create a **parallel orchestration notebook** that calls the 5 notebooks in parallel using concurrent notebook workflow 

4. Create **Jobs** for both the notebooks using Databricks Jobs API 

5. Schedule the jobs using **Jobs API**. Use **Clusters API** to create similar compute cluster for both. 

6. Compare **runtime of sequential and parallel jobs**

# Solution

Took help of <span style="color:red">ChatGPT</span>

### 1. Create 4 Notebooks in Databricks
Each notebook should read data from a single table and insert/update data into 5 respective output Delta tables. Here's a general structure for each notebook:

#### Notebook 1: `notebook_1`
- **Input**: Read data from `input_table`.
- **Output**: Insert/Update data into `output_table_1`.
- **Processing**: Implement any necessary transformations before inserting/updating.

#### Notebook 2: `notebook_2`
- **Input**: Read data from `input_table`.
- **Output**: Insert/Update data into `output_table_2`.
- **Processing**: Implement any necessary transformations before inserting/updating.

#### Notebook 3: `notebook_3`
- **Input**: Read data from `input_table`.
- **Output**: Insert/Update data into `output_table_3`.
- **Processing**: Implement any necessary transformations before inserting/updating.

#### Notebook 4: `notebook_4`
- **Input**: Read data from `input_table`.
- **Output**: Insert/Update data into `output_table_4`.
- **Processing**: Implement any necessary transformations before inserting/updating.

### 2. Create an Orchestration Notebook
This notebook will orchestrate the execution of the other four notebooks using `dbutils.notebook.run()`. The notebooks will be run sequentially:

#### Orchestration Notebook (Sequential)
- Use `dbutils.notebook.run("notebook_1", timeout_seconds)` to run the first notebook.
- Repeat the above step for `notebook_2`, `notebook_3`, and `notebook_4`.

### 3. Create a Parallel Orchestration Notebook
This notebook will orchestrate the execution of the other four notebooks in parallel using `concurrent.futures` or similar methods for parallel execution:

#### Orchestration Notebook (Parallel)
- Use `concurrent.futures` or `dbutils.notebook.run` with threading to execute the notebooks in parallel.
  
```python
from concurrent.futures import ThreadPoolExecutor

notebooks = ["notebook_1", "notebook_2", "notebook_3", "notebook_4"]

def run_notebook(notebook):
    return dbutils.notebook.run(notebook, 60)

with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(run_notebook, notebooks))
```

### 4. Create Jobs for Both Notebooks Using Databricks Jobs API
- **Job 1**: Create a job for the sequential orchestration notebook.
- **Job 2**: Create a job for the parallel orchestration notebook.

You can use the [Databricks Jobs API](https://docs.databricks.com/dev-tools/api/latest/jobs.html) to create these jobs.

### 5. Schedule the Jobs Using Jobs API
Schedule both jobs using the Jobs API, setting them to run at specific intervals or triggers.

### 6. Use Clusters API to Create Compute Clusters
Create similar clusters for both jobs using the [Databricks Clusters API](https://docs.databricks.com/dev-tools/api/latest/clusters.html).

### 7. Compare Runtime of Sequential and Parallel Jobs
- Run both jobs.
- Compare the runtime by checking the job execution history in Databricks or using the Databricks API to retrieve job runtimes.

### Steps to Implement:
1. **Set up the individual notebooks (`notebook_1`, `notebook_2`, etc.)** with the necessary logic.
2. **Create the orchestration notebooks** as described.
3. **Use the Databricks Jobs API** to create and schedule the jobs.
4. **Monitor and compare** the runtime of both jobs.
