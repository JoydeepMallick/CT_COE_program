# ASSIGNMENT 1

1. Load any Random Customer dataset 

2. Identify duplicate customers basis Name and Address 

3. Assign Master ID to matching customers 

4. Write back table enriched with Master ID back to Azure SQL

# SOLUTION

Here's a step-by-step guide to solving this assignment using Azure Databricks and PySpark:

## Step 1: Loading a Random Customer Dataset
For this example, we'll use a CSV file [`customer_dataset.csv`](./customer_dataset.csv).

#### a. log in to databricks community and press this
![](./Screenshot%20(902).png)

#### b. Upload file
![](./Screenshot%20(903).png)

#### c. Create new notebook
![](./Screenshot%20(904).png)

#### d. type in the following in first block
```python
# Load dataset into a DataFrame
customer_df = spark.read.csv('/FileStore/tables/customer_dataset.csv', header=True, inferSchema=True)
customer_df.show()
```
#### e. Press on run, it prompts to attach compute resources
![](./Screenshot%20(905).png)

#### f. The output for my dataset is as follows:-
```sql
(3) Spark Jobs
Job 0 

View
(Stages: 1/1)

Job 1 

View
(Stages: 1/1)

Job 2 

View
(Stages: 1/1)

 
customer_df:pyspark.sql.dataframe.DataFrame = [CustomerID: integer, Name: string ... 2 more fields]
+----------+-------------+-------------+--------------------+
|CustomerID|         Name|      Address|               Email|
+----------+-------------+-------------+--------------------+
|         1|     John Doe|   123 Elm St|    john@example.com|
|         2|   Jane Smith|   456 Oak St|    jane@example.com|
|         3|  Alice Brown|  789 Pine St|   alice@example.com|
|         4|Charlie Black| 234 Maple St| charlie@example.com|
|         5|    Eve White| 567 Birch St|     eve@example.com|
|         6|     John Doe|   123 Elm St|   john2@example.com|
|         7|   Jane Smith|   456 Oak St|   jane2@example.com|
|         8|  Alice Brown|  789 Pine St|  alice2@example.com|
|         9|Charlie Black| 234 Maple St|charlie2@example.com|
|        10|    Eve White| 567 Birch St|    eve2@example.com|
|        11|Michael Green| 890 Cedar St| michael@example.com|
|        12|   Sarah Blue|678 Spruce St|   sarah@example.com|
|        13|Michael Green| 890 Cedar St|michael2@example.com|
|        14| Laura Purple|345 Poplar St|   laura@example.com|
|        15| Laura Purple|345 Poplar St|  laura2@example.com|
|        16|     John Doe|   123 Elm St|   john3@example.com|
|        17|   Jane Smith|   456 Oak St|   jane3@example.com|
|        18|  Alice Brown|  789 Pine St|  alice3@example.com|
|        19|Charlie Black| 234 Maple St|charlie3@example.com|
|        20|    Eve White| 567 Birch St|    eve3@example.com|
+----------+-------------+-------------+--------------------+
only showing top 20 rows
```
![](./Screenshot%20(906).png)







## Step 2: Identify Duplicate Customers Based on Name and Address
Next, identify duplicate customers by checking for duplicates in the `Name` and `Address` columns.

```python
from pyspark.sql.functions import col, concat, lit

# Create a composite key by combining Name and Address
customer_df = customer_df.withColumn('CompositeKey', concat(col('Name'), lit('_'), col('Address')))

# Find duplicates
window_spec = Window.partitionBy('CompositeKey').orderBy('CustomerID')
customer_df = customer_df.withColumn('DuplicateRank', row_number().over(window_spec))
duplicates_df = customer_df.filter(col('DuplicateRank') > 1)
duplicates_df.show()
```

### Step 3: Assign Master ID to Matching Customers
Assign a unique Master ID to each group of duplicate customers.

```python
# Assign Master ID
master_id_df = duplicates_df.withColumn('MasterID', row_number().over(Window.orderBy(monotonically_increasing_id())))
master_id_df = master_id_df.select('CompositeKey', 'MasterID').distinct()

# Join MasterID back to the original DataFrame
enriched_customer_df = customer_df.join(master_id_df, 'CompositeKey', 'left')
enriched_customer_df.show()
```

### Step 4: Write Enriched Table Back to Azure SQL
**NOTE** : 😐 Could not perform this step due to no account in Azure. ChatGPT just gave me insights



Finally, write the enriched DataFrame back to Azure SQL.

```python
# Configure Azure SQL database connection
server_name = "jdbc:sqlserver://<server_name>.database.windows.net"
database_name = "<database_name>"
url = server_name + ";" + "databaseName=" + database_name + ";"
table_name = "EnrichedCustomerTable"
username = "<your_username>"
password = "<your_password>"

# Write DataFrame to Azure SQL
enriched_customer_df.write \
    .format("jdbc") \
    .mode("overwrite") \
    .option("url", url) \
    .option("dbtable", table_name) \
    .option("user", username) \
    .option("password", password) \
    .save()
```
