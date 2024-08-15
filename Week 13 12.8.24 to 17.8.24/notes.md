# Dataframe checkpoint
Video link : https://youtu.be/hgzSL8bnJFQ
![](./Screenshot%20(1049).png)
![](./Screenshot%20(1050).png)
![](./Screenshot%20(1051).png)
![](./Screenshot%20(1052).png)


See demo

# Introduction to Delta Lake
Video link : https://youtu.be/t6i6fQilAm8

![](./Screenshot%20(1053).png)
![](./Screenshot%20(1054).png)

Please read [this article](https://www.striim.com/blog/data-warehouse-vs-data-lake-vs-data-lakehouse-an-overview/)

### What Is a Data Warehouse?
A data warehouse is a **unified data repository for storing large amounts of information from multiple sources within an organization**. A data warehouse represents a single source of “data truth” in an organization and **serves as a core reporting and business analytics component**.

Typically, data warehouses store historical data by combining relational data sets from multiple sources, including application, business, and transactional data. Data warehouses extract data from multiple sources and transform and clean the data before loading it into the warehousing system to serve as a single source of data truth. Organizations invest in data warehouses because of their ability to quickly deliver business insights from across the organization.

Data warehouses enable business analysts, data engineers, and decision-makers to access data via BI tools, SQL clients, and other less advanced (i.e., non-data science) analytics applications.

![](https://media.striim.com/wp-content/uploads/2021/11/12093717/data-warehouse.png)


#### The benefits of a data warehouse


1. **Improving data standardization, quality, and consistency**: Organizations generate data from various sources, including sales, users, and transactional data. Data warehousing consolidates corporate data into a consistent, standardized format that can serve as a single source of data truth, giving the organization the confidence to rely on the data for business needs.

2. **Delivering enhanced business intelligence**: Data warehousing bridges the gap between voluminous raw data, often collected automatically as a matter of practice, and the curated data that offers insights. They serve as the data storage backbone for organizations, allowing them to answer complex questions about their data and use the answers to make informed business decisions.
3. **Increasing the power and speed of data analytics and business intelligence workloads**: Data warehouses speed up the time required to prepare and analyze data. Since the data warehouse’s data is consistent and accurate, they can effortlessly connect to data analytics and business intelligence tools. Data warehouses also cut down the time required to gather data and give teams the power to leverage data for reports, dashboards, and other analytics needs.

4. **Improving the overall decision-making process**: Data warehousing improves decision-making by providing a single repository of current and historical data. Decision-makers can evaluate risks, understand customers’ needs, and improve products and services by transforming data in data warehouses for accurate insights.
    
    For example, Walgreens migrated its inventory management data into Azure Synapse to enable supply chain analysts to query data and create visualizations using tools such as Microsoft Power BI. The move to a cloud data warehouse also decreased time-to-insights: previous-day reports are now available at the start of the business day, instead of hours later.

#### The disadvantages of a data warehouse


1. **Lack of data flexibility**: Although data warehouses perform well with structured data, they can struggle with semi-structured and unstructured data formats such as log analytics, streaming, and social media data. This makes it hard to recommend data warehouses for machine learning and artificial intelligence use cases.

2. **High implementation and maintenance costs**: Data warehouses can be expensive to implement and maintain. This article by Cooladata estimates the annual cost of an in-house data warehouse with one terabyte of storage and 100,000 queries per month to be $468,000. Additionally, the data warehouse is typically not static; it becomes outdated and requires regular maintenance, which can be costly.

### What Is a Data Lake?
A data lake is a **centralized, highly flexible storage repository that stores large amounts of structured and unstructured data in its raw, original, and unformatted form**. In contrast to **data warehouses, which store already “cleaned” relational data**, a data lake stores data using a flat architecture and object storage in its raw form. Data lakes are flexible, durable, and cost-effective and enable organizations to gain advanced insight from unstructured data, unlike data warehouses that struggle with data in this format.

**In data lakes, the schema or data is not defined when data is captured; instead, data is extracted, loaded, and transformed (ELT) for analysis purposes.** Data lakes allow for machine learning and predictive analytics using tools for various data types from IoT devices, social media, and streaming data.

![](https://media.striim.com/wp-content/uploads/2021/11/12093415/Data-Lake-pattern.png)

#### The benefits of a data lake

1. **Data consolidation**: Data lakes can store both structured and unstructured data to eliminate the need to store both data formats in different environments. They provide a central repository to store all types of organizational data.

2. **Data flexibility**: A significant benefit of data lakes is their flexibility; you can store data in any format or medium without the need to have a predefined schema. Allowing the data to remain in its native format allows for more data for analysis and caters to future data use cases.

3. **Cost savings**: Data lakes are less expensive than traditional data warehouses; they are designed to be stored on low-cost commodity hardware, like object storage, usually optimized for a lower cost per GB stored. For example, Amazon S3 standard object storage offers an unbelievable low price of $0.023 per GB for the first 50 TB/month.

4. **Support for a wide variety of data science and machine learning use cases**: Data in data lakes is stored in an open, raw format, making it easier to apply various machine and deep learning algorithms to process the data to produce meaningful insights.


#### The disadvantages of a data lake


1. **Poor performance for business intelligence and data analytics use cases:** If not properly managed, data lakes can become disorganized, making it hard to connect them with business intelligence and analytics tools. Also, a lack of consistent data structure and ACID (atomicity, consistency, isolation, and durability) transactional support can result in sub-optimal query performance when required for reporting and analytics use cases.

2. **Lack of data reliability and security**: Data lakes’ lack of data consistency makes it difficult to enforce data reliability and security. Because data lakes can accommodate all data formats, it might be challenging to implement proper data security and governance policies to cater to sensitive data types.

### What Is a Data Lakehouse? A Combined Approach
A data lakehouse is a **new, big-data storage architecture that combines the best features of both data warehouses and data lakes**. A data lakehouse enables a **single repository for all your data (structured, semi-structured, and unstructured) while enabling best-in-class machine learning, business intelligence, and streaming capabilities**.

Data lakehouses **usually start as data lakes containing all data types**; the data is then converted to **Delta Lake format** (an open-source storage layer that brings reliability to data lakes).**Delta lakes enable ACID transactional processes from traditional data warehouses on data lakes**.

#### The benefits of a data lakehouse


1. **Reduced data redundancy**: Data lakehouses reduce data duplication by providing a single all-purpose data storage platform to cater to all business data demands. Because of the advantages of the data warehouse and the data lake, most companies opt for a hybrid solution. However, this approach could lead to data duplication, which can be costly.

2. **Cost-effectiveness**: Data lakehouses implement the cost-effective storage features of data lakes by utilizing low-cost object storage options. Additionally, data lakehouses eliminate the costs and time of maintaining multiple data storage systems by providing a single solution.

3. **Support for a wider variety of workloads**: Data lakehouses provide direct access to some of the most widely used business intelligence tools (Tableau, PowerBI) to enable advanced analytics. Additionally, data lakehouses use open-data formats (such as Parquet) with APIs and machine learning libraries, including Python/R, making it straightforward for data scientists and machine learning engineers to utilize the data.

4. **Ease of data versioning, governance, and security**: Data lakehouse architecture enforces schema and data integrity making it easier to implement robust data security and governance mechanisms.

#### The disadvantages of a data lakehouse

The main disadvantage of a data lakehouse is **it’s still a relatively new and immature technology**. As such, it’s unclear whether it will live up to its promises. It may be years before data lakehouses can compete with mature big-data storage solutions. But with the current speed of modern innovation, it’s difficult to predict whether a new data storage solution could eventually usurp it.

![](./Screenshot%20(1055).png)

<table>
<tbody>
<tr>
<th style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""></th>
<th style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Data Warehouse</th>
<th style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Data Lake</th>
<th style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="">Data Lakehouse</th>
</tr>
<tr>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><strong>Storage Data Type</strong></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Works well with structured data</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Works well with semi-structured and unstructured data</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Can handle structured, semi-structured, and unstructured data</span></td>
</tr>
<tr>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><strong>Purpose</strong></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Optimal for data analytics and business intelligence (BI) use-cases</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Suitable for machine learning (ML) and artificial intelligence (AI) workloads</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Suitable for both data analytics and machine learning workloads</span></td>
</tr>
<tr>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><strong>Cost</strong></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Storage is costly and time-consuming</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Storage is cost-effective, fast, and flexible</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Storage is cost-effective, fast, and flexible</span></td>
</tr>
<tr>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); background: rgb(222, 234, 246); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #1d2021;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left="" data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor=""><strong>ACID Compliance</strong></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Records data in an ACID-compliant manner to ensure the highest levels of integrity</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">Non-ACID compliance: updates and deletes are complex operations</span></td>
<td style="padding: 6px; vertical-align: top; border: 1px solid rgb(221, 221, 221); --darkreader-inline-border-top: #363b3e; --darkreader-inline-border-right: #363b3e; --darkreader-inline-border-bottom: #363b3e; --darkreader-inline-border-left: #363b3e;" data-darkreader-inline-border-top="" data-darkreader-inline-border-right="" data-darkreader-inline-border-bottom="" data-darkreader-inline-border-left=""><span style="font-weight: 400;">ACID-compliant to ensure consistency as multiple parties concurrently read or write data</span></td>
</tr>
</tbody>
</table>

See demo

# Internal working mechanism
Video link : https://youtu.be/YmqkMZ4MxJg

![](./Screenshot%20(1057).png)
![](./Screenshot%20(1058).png)


### ⭐⭐⭐See demo from [this timestamp](https://youtu.be/YmqkMZ4MxJg?t=302)

# Solution architecture
Video link : https://youtu.be/Csoeu_ZtYkQ

![](./Screenshot%20(1059).png)


### ⭐⭐⭐See Demo Explanation

# Create Delta table
Video link : https://www.youtube.com/watch?v=RTIcUB_oi4E


#### Read this [article](https://delta.io/blog/2022-10-25-create-delta-lake-tables/)
Different ways of creation :-

## 1. Create a Delta Lake table with the PySpark API

<h3 style="color:yellow"> Please be mindful of the syntax😐, all the methods in PySpark api use camel case🐫🐪</h3>

```py
from pyspark.sql.types import *
dt1 = (
    DeltaTable.create(spark)
    .tableName("testTable1")
    .addColumn("c1", dataType="INT", nullable=False)
    .addColumn("c2", dataType=IntegerType(), generatedAlwaysAs="c1 + 1")
    .partitionedBy("c1")
    .execute()
)
```
This will create an empty Delta Lake table with `c1` and `c2` columns.

If the table already exists, the `create` method will error. To avoid this, you can use the `createIfNotExists` method instead.

Delta Lake’s fluent API provides an elegant way to create tables with PySpark code. The API also allows you to specify generated columns and properties.

Another example from video

* using `create` function 

![](./Screenshot%20(1060).png)

* Below image confirms that `property` and `location` column are optional.
Below  code uses `createIfNotExists` method

![](./Screenshot%20(1061).png)

* use `createOrReplace` function, it replaces old table with same name if exists in current location where this table gets saved.

![](./Screenshot%20(1062).png)

* we can directly write the `column_name` or write `database_name.column_name` where the default database is called `default`

![](./Screenshot%20(1063).png)

## 2. Create a Delta Lake table with SQL

```py
# table creation
spark.sql("""
  CREATE TABLE table2 (country STRING, continent STRING) USING delta
""")

# data insertion
spark.sql("""
  INSERT INTO table2 VALUES
      ('china', 'asia'),
      ('argentina', 'south america')
""")

# printing
spark.sql("SELECT * FROM table2").show()
```
Output
```
+---------+-------------+
|  country|    continent|
+---------+-------------+
|argentina|south america|
|    china|         asia|
+---------+-------------+
```
We can confirm that this table is a Delta Lake table with the following command:

```py
spark.sql("DESCRIBE DETAIL table2").select("format").show()
```
Output
```
+------+
|format|
+------+
| delta|
+------+
```
Example from video

### Just a little addition to SQL command at end is `...USING DELTA`

* Using SQL command `create table`

![](./Screenshot%20(1064).png)


* Using SQL command `create table if not exists`

![](./Screenshot%20(1066).png)

* Using SQL command `create or replace table`

![](./Screenshot%20(1067).png)

## 3. Create a Delta Lake Table from a DataFrame

We can write out a PySpark DataFrame to Delta Lake, thereby creating a Delta Lake table.

We start by creating a PySpark DataFrame with a few rows of data:

```py
columns = ["character", "franchise"]
data = [("link", "zelda"), ("king k rool", "donkey kong"), ("samus", "metroid")]
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(columns)

# check structure
df.show()
```
Output 
```
+-----------+-----------+
|  character|  franchise|
+-----------+-----------+
|       link|      zelda|
|king k rool|donkey kong|
|      samus|    metroid|
+-----------+-----------+
```

To write this DataFrame out as Parquet files and create a table (an operation you’re likely familiar with):

```py
df.write.format("parquet").saveAsTable("table1_as_parquet")
```

Creating a Delta Lake table uses almost identical syntax – it’s as easy as switching your format from "parquet" to "delta":

```py
df.write.format("delta").saveAsTable("table1")
```

We can run a command to confirm that the table is in fact a Delta Lake table:

```py
DeltaTable.isDeltaTable(spark, "spark-warehouse/table1") # True
```

And we can fetch the contents of this table via the PySpark API:

```py
spark.table("table1").show()
```
Output
```
+-----------+-----------+
|  character|  franchise|
+-----------+-----------+
|king k rool|donkey kong|
|      samus|    metroid|
|       link|      zelda|
+-----------+-----------+
```

Example from video

![](./Screenshot%20(1069).png)
![](./Screenshot%20(1070).png)

## 4. Create a Delta Lake table from CSV

Suppose you have the following `students1.csv` file:

```csv
student_name,graduation_year,major
someXXperson,2023,math
liXXyao,2025,physics
```

You can read this CSV file into a Spark DataFrame and write it out as a Delta Lake table using these commands:

```py
df = spark.read.option("header", True).csv("students1.csv")
df.write.format("delta").saveAsTable("students")
```
For a single CSV file, you don’t even need to use Spark: you can simply use `delta-rs`, which doesn’t have a Spark dependency, and create the Delta Lake from a Pandas DataFrame. 

If you have multiple CSV files, using PySpark is usually better because it can read multiple files in parallel.

Here’s how to create a Delta Lake table with multiple CSV files:

```py
df = spark.read.option("header", True).csv("path/with/csvs/")
df.write.format("delta").save("some/other/path")
```

## 5. Create a Delta Lake table from Parquet
You could follow a similar design pattern to convert Parquet files to a Delta Lake, reading them into a Spark DataFrame and then writing them out to a Delta Lake – but there’s an even easier approach.

Delta Lakes store data in Parquet files and metadata in a transaction log. When creating a Delta Lake from Parquet files, you don’t need to rewrite the data: you can perform an in-place operation and simply add the transaction log to the existing folder with the Parquet files. Here’s how to perform this operation:

```py
DeltaTable.convertToDelta(spark, "parquet.`tmp/lake1`")
```
Suppose you have the following Parquet files stored in tmp/lake1:

```
tmp/lake1
├── _SUCCESS
├── part-00000-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
├── part-00003-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
├── part-00006-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
└── part-00009-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
```
Here’s what the files will look like after they’ve been converted to a Delta Lake:

```
tmp/lake1
├── _SUCCESS
├── _delta_log
│   ├── 00000000000000000000.checkpoint.parquet
│   ├── 00000000000000000000.json
│   └── _last_checkpoint
├── part-00000-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
├── part-00003-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
├── part-00006-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
└── part-00009-1f1cc136-76ea-4185-84d6-54f7e758bfb7-c000.snappy.parquet
```


## Create a Delta Lake table from other technologies
The open nature of Delta Lake allows for a robust connector ecosystem. This means you can create a Delta Lake with a variety of other technologies. Here are some examples:

The `delta-rs` Python bindings let you create a Delta Lake from a pandas DataFrame.
**kafka-delta-ingest** is a highly efficient way to stream data from Kafka into a Delta Lake.
The connectors repo contains Delta Standalone, a Java library that doesn’t depend on Spark, which allows for Java-based connectors like **Hive** and **Flink**.

### ⭐⭐⭐See Demo
# Delta table instance
Video link : https://www.youtube.com/watch?v=DVUwIpIlNss

![](./Screenshot%20(1071).png) 
![](./Screenshot%20(1072).png) 

![](./Screenshot%20(1079).png)



First create a table and insert values

![](./Screenshot%20(1073).png) 

## Approach 1 : Using `forPath`
Viewing table and creating an instance

![](./Screenshot%20(1074).png) 

After delete operation

![](./Screenshot%20(1076).png) 

Table will look like 

![](./Screenshot%20(1078).png)

<span style="color:red"> **NOTE** </span>
Now **updated table from same instance** will look something like 

![](./Screenshot%20(1077).png) 

## Approach 2 : Using `forName`

![](./Screenshot%20(1080).png)

<span style="color:red"> **NOTE** </span>
In general all SQL commnands have a alternative here and can be used for example:-

![](./Screenshot%20(1081).png)
![](./Screenshot%20(1082).png)


### ⭐⭐⭐See video for sure

# SCD types
Video link : https://youtu.be/i5oM2bUyH0o


First lets create a DELTA table :

![](./Screenshot%20(1083).png)
![](./Screenshot%20(1084).png)



## 1. Merge(Upsert) using SparkSQL

In SparkSQL we need to set source and target as table in order to perform any SQL operations. 

![](./Screenshot%20(1087).png)
![](./Screenshot%20(1085).png)
![](./Screenshot%20(1089).png)

With some more examples we will do testing

![](./Screenshot%20(1091).png)
![](./Screenshot%20(1092).png)

Hence `source_view` contains 2 records now as shown above but delta table has only one record as shown below:

![](./Screenshot%20(1093).png)

## 2. Merge using PySpark
In order to merge using PySpark **we need to keep data in Dataframe format and not in Table format**.

![](./Screenshot%20(1096).png)
Now we create a delta dataframe

![](./Screenshot%20(1097).png)

Now we perform merge operations and see the update

![](./Screenshot%20(1098).png)
![](./Screenshot%20(1099).png)




### ⭐⭐⭐See Demo

# Audit log table
Video link : https://youtu.be/GhBlup-8JbE

![](./Screenshot%20(1100).png)

Assume below example

![](./Screenshot%20(1101).png)

When we perform following steps and following outputs is expected as shown below:

![](./Screenshot%20(1102).png)
![](./Screenshot%20(1103).png)

### ⭐⭐⭐See Demo from [current timestamp](https://youtu.be/GhBlup-8JbE?t=731)

Now we perform a real demo

![](./Screenshot%20(1104).png)

Now we create an instance of table 

![](./Screenshot%20(1105).png)

Now we create schema and also a source data frame.

![](./Screenshot%20(1106).png)
![](./Screenshot%20(1107).png)

Now we perform join operation

![](./Screenshot%20(1108).png)
![](./Screenshot%20(1109).png)

![](./Screenshot%20(1110).png)

![](./Screenshot%20(1111).png)

![](./Screenshot%20(1112).png)

![](./Screenshot%20(1113).png)

![](./Screenshot%20(1114).png)

![](./Screenshot%20(1115).png)

# SCD type 2
Video link : https://www.youtube.com/watch?v=GhBlup-8JbE

Lets assume an example 

![](./Screenshot%20(1116).png)
![](./Screenshot%20(1117).png)
![](./Screenshot%20(1118).png)

### ⭐⭐⭐See Demo from [current timestamp](https://youtu.be/GhBlup-8JbE?t=728)

Creating table

![](./Screenshot%20(1119).png)

Creating instance

![](./Screenshot%20(1121).png)

Now we create schema 

![](./Screenshot%20(1123).png)

then create a sample dataframe

![](./Screenshot%20(1122).png)

now we join 

![](./Screenshot%20(1124).png)
![](./Screenshot%20(1125).png)

![](./Screenshot%20(1126).png)

![](./Screenshot%20(1127).png)

![](./Screenshot%20(1128).png)

![](./Screenshot%20(1129).png)

![](./Screenshot%20(1130).png)

![](./Screenshot%20(1131).png)


# CDC
Read Blog : https://www.databricks.com/blog/2021/06/09/how-to-simplify-cdc-with-delta-lakes-change-data-feed.html 

We see CDC used in an **ingestion to analytics architecture called the medallion architecture**. The medallion architecture that takes raw data landed from source systems and refines the data through bronze, silver and gold tables. CDC and the medallion architecture provide multiple benefits to users since only changed or added data needs to be processed. In addition, the different tables in the architecture allow different personas, such as Data Scientists and BI Analysts, to use the correct up-to-date data for their needs. 

![](https://www.databricks.com/wp-content/uploads/2021/06/How-to-Simplify-CDC-with-Delta-Lakes-Change-Data-Feed-blog-image6.jpg)

### Why is the CDF feature needed?

Biggest issues before CDF
* Quality Control 
* Inefficiency 

After CDF biggest achievements
* Simplicity and convenience
* Efficiency



# Time travel
Video link : https://youtu.be/3av7ctZ1uoo

⭐⭐Read [mircrosoft blog](https://learn.microsoft.com/en-us/azure/databricks/delta/history)

Each operation that modifies a Delta Lake table creates a new table version. You can use history information to audit operations, rollback a table, or query a table at a specific point in time using **time travel**.

### Retrieve Delta table history
You can retrieve information including the operations, user, and timestamp for each write to a Delta table by running the `history` command. The operations are returned in reverse chronological order.

Table history retention is determined by the table setting `delta.logRetentionDuration`, which is 30 days by default.


```SQL
DESCRIBE HISTORY table_name       -- get the full history of the table

DESCRIBE HISTORY table_name LIMIT 1  -- get the last operation only
```


Assume following delta table:-

![](./Screenshot%20(1132).png)
![](./Screenshot%20(1133).png)

## Using table history command from SQL

![](./Screenshot%20(1134).png)

## Pyspark approaches

### Method 1 : PySpark - **`Timestamp + Table`**

![](./Screenshot%20(1135).png)

### Method 2 : PySpark - **`Version + Table`**

Here instead of `path` option we need to provide `load` option where the value is the location of table.

![](./Screenshot%20(1137).png)

### Method 3 : PySpark - **`Version + Path`**

Here instead of timstamp we need to provide the version number.

![](./Screenshot%20(1138).png)

### Method 4 : PySpark - **`Version + Table`**

![](./Screenshot%20(1139).png)


## SQL approaches

### Method 5 : SQL - **`Version + Table`**

![](./Screenshot%20(1140).png)

### Method 6 : SQL - **`Version + Path`**

![](./Screenshot%20(1141).png)

### Method 7 : SQL - **`Timestamp + Table`**

![](./Screenshot%20(1142).png)

### Method 8 : SQL - **`Timestamp + Path`**

![](./Screenshot%20(1143).png)








### ⭐⭐⭐See Demo from video

# Restore command
Video link : https://youtu.be/CHfP2UxZn1g



See Demo

# Optimize command
Video link : https://youtu.be/F9tc8EgIn3c



See Demo

# Vacuum command
Video link : https://youtu.be/G_RzisFeA5U



See Demo

# Z-Order command
Video link : https://youtu.be/89cInDvqXCY
 


See Demo

# Schmea Evolution
Video link : https://youtu.be/NOYL0yRoUeo



See Demo

