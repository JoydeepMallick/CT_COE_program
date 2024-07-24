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




# Write dataframe into CSV file
Video link : https://youtu.be/SQfTHPvzlEI





# Read json File in to dataframe
Video link : https://youtu.be/HdfQWt3DgW0




# Write dataframe into json file
Video link : 





# Read parquet file in to dataframe
Video link : 





# Write dataframe into parquet
Video link : 





# show() in pyspark
Video link : 





# withColumn() in pyspark
Video link : 





# withColumnRenamed() in pyspark
Video link : 





# StructType() & StructField()
Video link : 





# explode(),split(),array_contains,array() functions
Video link : 





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




