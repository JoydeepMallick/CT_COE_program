# ASSIGNMENT 1

1. Load any Random Customer dataset 

2. Identify duplicate customers basis Name and Address 

3. Assign Master ID to matching customers 

4. Write back table enriched with Master ID back to Azure SQL

# SOLUTION

Here's a step-by-step guide to solving this assignment using Azure Databricks and PySpark:

### Step 1: Load a Random Customer Dataset
First, load a sample dataset into Databricks. For this example, we'll use a CSV file containing customer data.

```python
# Load dataset into a DataFrame
customer_df = spark.read.csv('/path/to/customer_dataset.csv', header=True, inferSchema=True)
customer_df.show()
```

### Step 2: Identify Duplicate Customers Based on Name and Address
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

### Summary of the Steps:

1. **Load Data**: Load a random customer dataset into a DataFrame.
2. **Identify Duplicates**: Use a composite key (combination of Name and Address) to identify duplicate customers.
3. **Assign Master ID**: Assign a unique Master ID to each group of duplicate customers.
4. **Write to Azure SQL**: Save the enriched DataFrame with Master IDs back to an Azure SQL database.

This workflow ensures that duplicate customers are identified and assigned a unique Master ID, and the enriched data is stored back in Azure SQL for further use.