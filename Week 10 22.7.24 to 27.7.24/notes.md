### Entire playlist for PySpark

https://www.youtube.com/watch?v=6MaZoOgJa84&list=PLMWaZteqtEaJFiJ2FyIKK0YEuXwQ9YIS_

⭐Please read about Apache Spark and Big data and why it came into existence from Week 9 before this.


# What is Pyspark
video link : https://youtu.be/6MaZoOgJa84

PySpark is an interface for Apache Spark in Python. It not only allows you to write spark applications using Python APIs, but also provides the PySpark shell for interactively analyzing your data in distributed environment. 

PySpark supports most Spark features such as **SparkSQL, DataFrame, Streaming, MLib (Machine Learning) and spark core**.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSePnamTescIkx7Ip9UQFcn-1XqHS3shqrtSQ&s)


# Create dataframe
video link : https://youtu.be/mIAIQI5rMY8

DataFrame is **distributed collection of data organized into named columns**.

Conceptually equivalent to tables in relational database.

⭐⭐see demo in video
![](./Screenshot%20(912).png)

### ⭐⭐[read stackoverflow](https://stackoverflow.com/questions/57959759/manually-create-a-pyspark-dataframe) and [official pyspark doc](https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.SparkSession.createDataFrame.html) to know about dataframe creation

```py
df = spark.createDataFrame(
    [
        (1, "foo"),  # create your data here, be consistent in the types.
        (2, "bar"),
    ],
    ["id", "label"]  # add your column names here
)

df.printSchema() # kind of like desc in sql
```
Output
```
root
 |-- id: long (nullable = true)
 |-- label: string (nullable = true)
```

```py
df.show()
```
Output
```
+---+-----+                                                                 
| id|label|
+---+-----+
|  1|  foo|
|  2|  bar|
+---+-----+
```

### Basic syntax
```py
SparkSession.createDataFrame(
    data, 
    schema=None, 
    samplingRatio=None, 
    verifySchema=True)
```
### Parameters
1. `data` : **RDD or iterable**

    an **RDD** of any kind of SQL data representation(e.g. Row, tuple, int, boolean, etc.), or list, or pandas.DataFrame.

2. `schema` : `pyspark.sql.types.DataType`, `str` or `list`, **optional**
    
    a `pyspark.sql.types.DataType` or a datatype string or a list of column names, default is None. 
    
    The data type string format equals to `pyspark.sql.types.DataType.simpleString`, except that top level struct type can omit the `struct<>` and atomic types use `typeName()` as their format, e.g. use byte instead of `tinyint` for `pyspark.sql.types.ByteType`. 
    
    We can also use `int` as a short name for `pyspark.sql.types.IntegerType`.

3. `samplingRatio`: `float`, **optional**

    the sample ratio of rows used for inferring

4. `verifySchema` : `bool`, **optional**

    verify data types of every row against schema. Enabled by default.

### Returns
    DataFrame

### Defining DataFrame Schema with StructField and StructType

⭐⭐[read gfg blog here](https://www.geeksforgeeks.org/defining-dataframe-schema-with-structfield-and-structtype/)

### Create dataframe with dictionary

⭐⭐[Read gfg](https://www.geeksforgeeks.org/create-pyspark-dataframe-from-dictionary/)

# Read CSV File in to dataframe
video link : https://youtu.be/lRkIQMRXcYw

Use `csv("path")` or `format("csv").load("path")` of DataFrameReader, you can read a CSV file into a PySpark Dataframe.
![](./Screenshot%20(913).png)

⭐⭐see demo


# Write dataframe into CSV file
Video link : https://youtu.be/SQfTHPvzlEI

### ⭐⭐[read this](https://sparkbyexamples.com/pyspark/pyspark-write-dataframe-to-csv-file/) and [this](https://www.deeplearningnerds.com/pyspark-write-dataframe-to-csv-file/)

In PySpark you can save (write/extract) a DataFrame to a CSV file on disk by using `dataframeObj.write.csv("path")`, using this you can also write DataFrame to AWS S3, Azure Blob, HDFS, or any PySpark supported file systems.

### Write PySpark DataFrame to CSV File
we would like to write the already created PySpark DataFrame to a CSV file. The file should have the following attributes:

- File should include a header with the column names.
- Columns of the file should be separated with semi-colon ;.
- Existing file should be overwritten.
- File path should be "data/frameworks.csv".

We can do this in two different ways.

#### 1. using csv()
    
To do this, we first create a `DataFrameWriter` instance with `df.write`. Afterwards, we use the `csv()` method in combination with the `option()` method and the `mode()` method of `DataFrameWriter`:
```py
df.write.option("header",True) \
    .option("delimiter",";") \
    .mode("overwrite") \
    .csv("data/frameworks.csv")
```
#### 2. using format("csv").save()
Now, we consider another option to write the PySpark DataFrame to a CSV file.

First, we create a `DataFrameWriter` instance with `df.write`. Afterwards, we use the `save()` method in combination with the `format()` method, the `option()` method and the `mode()` method of `DataFrameWriter`:
```py
df.write.option("header",True) \
    .option("delimiter",";") \
    .format("csv") \
    .mode("overwrite") \
    .save("data/frameworks.csv")
```

# Read json File in to dataframe
Video link : https://youtu.be/HdfQWt3DgW0

![](./Screenshot%20(914).png)
![](./Screenshot%20(915).png)
![](./Screenshot%20(916).png)

### ⭐⭐See video


# Write dataframe into json file
Video link : https://youtu.be/U0iwA473r1c?si=olEYeZxAEFQJvnq9

Use `DataFrameWriter` object to write PySpark DataFrame to a CSV file.

```py
df.write.json(path='dbfs:/FileStore/data/jsonemps')
```

### ⭐⭐see demo in video

# Read parquet file in to dataframe
Video link : https://youtu.be/VeeJuNsTjmg?si=VyOokrKOlbwpUR7f

![](./Screenshot%20(917).png)
![](./Screenshot%20(918).png)

### ⭐⭐see demo in video

# Write dataframe into parquet
Video link : https://youtu.be/Ck8pEx6WafQ?si=TideguMq8SmSPFYs 

![](./Screenshot%20(919).png)
![](./Screenshot%20(920).png)

### ⭐⭐see demo in video

# show() in pyspark
Video link : https://youtu.be/9VhitO4KFv0

`show()` displays contents of the table.

![](./Screenshot%20(921).png)

### ⭐⭐see demo in video

# withColumn() in pyspark
Video link : https://youtu.be/RgGT7LfHBQs

![](./Screenshot%20(922).png)

### ⭐⭐see demo in video

# withColumnRenamed() in pyspark
Video link : https://youtu.be/z2_ajv_aY2Y

used to rename column name in dataframe.

![](./Screenshot%20(923).png)

### ⭐⭐see demo in video

# StructType() & StructField()
Video link : https://youtu.be/D0Xoyd7rpV0?si=0Gn6TOF7GU-Y8ijN



### ⭐⭐see demo in video

# explode(),split(),array_contains,array() functions
Video link : 



### ⭐⭐see demo in video

# Maptype
Video link : 





# row() class in pyspark
Video link : 





# when() & otherwise() functions
Video link : 





# filter() & where() functions
Video link : 





# alias(),asc(),desc()
Video link : 





# distinct()& dropDuplicates()
Video link : 





# orderBy() & sort()
Video link : 





# union& unionAll()
Video link : 





# groupBy()
Video link : 





# groupBy() agg
Video link : 





# UnionByName()
Video link : 





# select()
Video link : 





# joins part 1
Video link : 





# joins part 2
Video link : 





# pivot
Video link : 





# unpivot
Video link : 





# fill()& fillna()
Video link : 





# collect()
Video link : 





# createOrReplaceTempView()
Video link : 





# UDF
Video link : 





# partitionBy()
Video link : 





# convert RDD to dataframe
Video link : 





# Timestamp Functions
Video link : 





# Window Functions
Video link : 




