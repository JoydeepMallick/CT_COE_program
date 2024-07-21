# ASSIGNMENT 1

1. Load any Random Customer dataset 

2. Identify duplicate customers basis Name and Address 

3. Assign Master ID to matching customers 

4. Write back table enriched with Master ID back to Azure SQL

# SOLUTION

### 🔗[Link to ipynb file](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3873506874890165/3075800649314905/2284474567993444/latest.html) (valid for 6 months, published on 20.7.24)

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
from pyspark.sql.functions import col, count

# group by name and address and count occurences
duplicates_df = customer_df.groupBy("Name", "Address").count().filter(col("count") > 1)
duplicates_df.show()
```
output
```sql

from pyspark.sql.functions import col, count

# group by name and address and count occurences
duplicates_df = customer_df.groupBy("Name", "Address").count().filter(col("count") > 1)
duplicates_df.show()
(2) Spark Jobs
Job 3 

View
(Stages: 1/1)

Job 4 

View
(Stages: 1/1, 1 skipped)

 
duplicates_df:pyspark.sql.dataframe.DataFrame
Name:string
Address:string
count:long
+-------------+--------------+-----+
|         Name|       Address|count|
+-------------+--------------+-----+
|Michael Green|  890 Cedar St|    5|
|    Eve White|  567 Birch St|    3|
|   Sarah Blue| 678 Spruce St|    2|
|Charlie Black|  234 Maple St|    3|
| Laura Purple| 345 Poplar St|    4|
|    David Red|901 Hickory St|    2|
|     John Doe|    123 Elm St|    3|
|  Alice Brown|   789 Pine St|    3|
|  Anna Yellow| 345 Poplar St|    2|
|   Jane Smith|    456 Oak St|    3|
+-------------+--------------+-----+

```
![](./Screenshot%20(907).png)


## Step 3: Assign Master ID to Matching Customers
Assign a unique Master ID to each group of duplicate customers.

---
### 🤔What is Master ID actually?

ChatGPT explains it nicely🤗

In the context of **data deduplication**, a **Master ID** is an identifier assigned to a group of duplicate records to signify that they belong to the same entity. It essentially serves to consolidate or "master" duplicate entries into a single, identifiable record.

### Why Use a Master ID?

1. **Identification of Unique Entities**: By assigning the same Master ID to duplicates, you can easily identify which records refer to the same entity.
2. **Data Consistency**: It helps maintain data consistency by ensuring that all duplicates are associated with a single, consistent identifier.
3. **Simplified Analysis**: It simplifies data analysis and reporting by allowing you to aggregate data based on unique entities rather than dealing with multiple duplicate records.

### Example

Consider the following dataset:

| CustomerID | Name       | Address       | Email              |
|------------|------------|---------------|--------------------|
| 1          | John Doe   | 123 Elm St    | john@example.com   |
| 2          | Jane Smith | 456 Oak St    | jane@example.com   |
| 3          | John Doe   | 123 Elm St    | john2@example.com  |
| 4          | Alice Brown| 789 Pine St   | alice@example.com  |
| 5          | John Doe   | 123 Elm St    | john3@example.com  |

After identifying duplicates and assigning a Master ID, the dataset might look like this:

| CustomerID | Name       | Address       | Email              | MasterID |
|------------|------------|---------------|--------------------|----------|
| 1          | John Doe   | 123 Elm St    | john@example.com   | 1        |
| 2          | Jane Smith | 456 Oak St    | jane@example.com   | 2        |
| 3          | John Doe   | 123 Elm St    | john2@example.com  | 1        |
| 4          | Alice Brown| 789 Pine St   | alice@example.com  | 4        |
| 5          | John Doe   | 123 Elm St    | john3@example.com  | 1        |

Here, all records for "John Doe" living at "123 Elm St" are assigned the same Master ID, indicating they are duplicates of the same customer.


Try googling:-
- creating unique identifiers for duplicates in Apache Spark
- creating unique identifiers for duplicates in Apache Spark

Read [stackoverflow](https://stackoverflow.com/a/36408554) and [databricks community post](https://community.databricks.com/t5/data-engineering/generate-group-id-for-similar-deduplicate-values-of-a-dataframe/td-p/21060).


---

Actual answer to our question :-
```python
from pyspark.sql.functions import col, concat_ws, row_number, monotonically_increasing_id
from pyspark.sql import Window

# Initialize Spark session (if not already initialized), some website mention its automatically created when we open a notebook
spark = SparkSession.builder \
    .appName("CustomerDeduplication") \
    .getOrCreate()

# Load dataset into a DataFrame
customer_df = spark.read.csv('/FileStore/tables/customer_dataset.csv', header=True, inferSchema=True)

# Replace null values if any in Name and Address columns with empty strings
customer_df = customer_df.fillna({'Name': '', 'Address': ''})

# Create a CompositeKey column by concatenating Name and Address
customer_df_modified = customer_df.withColumn("CompositeKey", concat_ws(' ', col("Name"), col("Address")))
print("Added Composite key :")
customer_df_modified.show()

# Use dense_rank to assign the same MasterID to duplicates
windowSpec = Window.partitionBy("CompositeKey").orderBy(monotonically_increasing_id())
master_id_df = customer_df_modified.withColumn("MasterID", row_number().over(windowSpec))


print("Below are 2 variations of outputs with Master ID columns : ")
# Select relevant columns
result_df = master_id_df.select("CustomerID", "Name", "Address", "MasterID")
result_df.show()

# Merge the MasterID back into the original dataset
merged_df = customer_df_modified.join(result_df.select("CustomerID", "MasterID"), on="CustomerID", how="left")
merged_df.show()

```
Output
```sql
customer_df:pyspark.sql.dataframe.DataFrame = [CustomerID: integer, Name: string ... 2 more fields]
customer_df_modified:pyspark.sql.dataframe.DataFrame = [CustomerID: integer, Name: string ... 3 more fields]
master_id_df:pyspark.sql.dataframe.DataFrame = [CustomerID: integer, Name: string ... 4 more fields]
result_df:pyspark.sql.dataframe.DataFrame = [CustomerID: integer, Name: string ... 2 more fields]
merged_df:pyspark.sql.dataframe.DataFrame = [CustomerID: integer, Name: string ... 4 more fields]
Added Composite key :
+----------+-------------+-------------+--------------------+--------------------+
|CustomerID|         Name|      Address|               Email|        CompositeKey|
+----------+-------------+-------------+--------------------+--------------------+
|         1|     John Doe|   123 Elm St|    john@example.com| John Doe 123 Elm St|
|         2|   Jane Smith|   456 Oak St|    jane@example.com|Jane Smith 456 Oa...|
|         3|  Alice Brown|  789 Pine St|   alice@example.com|Alice Brown 789 P...|
|         4|Charlie Black| 234 Maple St| charlie@example.com|Charlie Black 234...|
|         5|    Eve White| 567 Birch St|     eve@example.com|Eve White 567 Bir...|
|         6|     John Doe|   123 Elm St|   john2@example.com| John Doe 123 Elm St|
|         7|   Jane Smith|   456 Oak St|   jane2@example.com|Jane Smith 456 Oa...|
|         8|  Alice Brown|  789 Pine St|  alice2@example.com|Alice Brown 789 P...|
|         9|Charlie Black| 234 Maple St|charlie2@example.com|Charlie Black 234...|
|        10|    Eve White| 567 Birch St|    eve2@example.com|Eve White 567 Bir...|
|        11|Michael Green| 890 Cedar St| michael@example.com|Michael Green 890...|
|        12|   Sarah Blue|678 Spruce St|   sarah@example.com|Sarah Blue 678 Sp...|
|        13|Michael Green| 890 Cedar St|michael2@example.com|Michael Green 890...|
|        14| Laura Purple|345 Poplar St|   laura@example.com|Laura Purple 345 ...|
|        15| Laura Purple|345 Poplar St|  laura2@example.com|Laura Purple 345 ...|
|        16|     John Doe|   123 Elm St|   john3@example.com| John Doe 123 Elm St|
|        17|   Jane Smith|   456 Oak St|   jane3@example.com|Jane Smith 456 Oa...|
|        18|  Alice Brown|  789 Pine St|  alice3@example.com|Alice Brown 789 P...|
|        19|Charlie Black| 234 Maple St|charlie3@example.com|Charlie Black 234...|
|        20|    Eve White| 567 Birch St|    eve3@example.com|Eve White 567 Bir...|
+----------+-------------+-------------+--------------------+--------------------+
only showing top 20 rows

Below are 2 variations of outputs with Master ID columns : 
+----------+-------------+--------------+--------+
|CustomerID|         Name|       Address|MasterID|
+----------+-------------+--------------+--------+
|         3|  Alice Brown|   789 Pine St|       1|
|         8|  Alice Brown|   789 Pine St|       2|
|        18|  Alice Brown|   789 Pine St|       3|
|        28|  Anna Yellow| 345 Poplar St|       1|
|        29|  Anna Yellow| 345 Poplar St|       2|
|         4|Charlie Black|  234 Maple St|       1|
|         9|Charlie Black|  234 Maple St|       2|
|        19|Charlie Black|  234 Maple St|       3|
|        26|    David Red|901 Hickory St|       1|
|        27|    David Red|901 Hickory St|       2|
|         5|    Eve White|  567 Birch St|       1|
|        10|    Eve White|  567 Birch St|       2|
|        20|    Eve White|  567 Birch St|       3|
|         2|   Jane Smith|    456 Oak St|       1|
|         7|   Jane Smith|    456 Oak St|       2|
|        17|   Jane Smith|    456 Oak St|       3|
|         1|     John Doe|    123 Elm St|       1|
|         6|     John Doe|    123 Elm St|       2|
|        16|     John Doe|    123 Elm St|       3|
|        14| Laura Purple| 345 Poplar St|       1|
+----------+-------------+--------------+--------+
only showing top 20 rows

+----------+-------------+-------------+--------------------+--------------------+--------+
|CustomerID|         Name|      Address|               Email|        CompositeKey|MasterID|
+----------+-------------+-------------+--------------------+--------------------+--------+
|         1|     John Doe|   123 Elm St|    john@example.com| John Doe 123 Elm St|       1|
|         2|   Jane Smith|   456 Oak St|    jane@example.com|Jane Smith 456 Oa...|       1|
|         3|  Alice Brown|  789 Pine St|   alice@example.com|Alice Brown 789 P...|       1|
|         4|Charlie Black| 234 Maple St| charlie@example.com|Charlie Black 234...|       1|
|         5|    Eve White| 567 Birch St|     eve@example.com|Eve White 567 Bir...|       1|
|         6|     John Doe|   123 Elm St|   john2@example.com| John Doe 123 Elm St|       2|
|         7|   Jane Smith|   456 Oak St|   jane2@example.com|Jane Smith 456 Oa...|       2|
|         8|  Alice Brown|  789 Pine St|  alice2@example.com|Alice Brown 789 P...|       2|
|         9|Charlie Black| 234 Maple St|charlie2@example.com|Charlie Black 234...|       2|
|        10|    Eve White| 567 Birch St|    eve2@example.com|Eve White 567 Bir...|       2|
|        11|Michael Green| 890 Cedar St| michael@example.com|Michael Green 890...|       1|
|        12|   Sarah Blue|678 Spruce St|   sarah@example.com|Sarah Blue 678 Sp...|       1|
|        13|Michael Green| 890 Cedar St|michael2@example.com|Michael Green 890...|       2|
|        14| Laura Purple|345 Poplar St|   laura@example.com|Laura Purple 345 ...|       1|
|        15| Laura Purple|345 Poplar St|  laura2@example.com|Laura Purple 345 ...|       2|
|        16|     John Doe|   123 Elm St|   john3@example.com| John Doe 123 Elm St|       3|
|        17|   Jane Smith|   456 Oak St|   jane3@example.com|Jane Smith 456 Oa...|       3|
|        18|  Alice Brown|  789 Pine St|  alice3@example.com|Alice Brown 789 P...|       3|
|        19|Charlie Black| 234 Maple St|charlie3@example.com|Charlie Black 234...|       3|
|        20|    Eve White| 567 Birch St|    eve3@example.com|Eve White 567 Bir...|       3|
+----------+-------------+-------------+--------------------+--------------------+--------+
only showing top 20 rows
```


## Step 4: Write Enriched Table Back to Azure SQL
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
