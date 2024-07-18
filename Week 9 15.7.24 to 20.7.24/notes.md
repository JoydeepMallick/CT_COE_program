# What is Big Data

Video link : https://youtu.be/zez2Tv-bcXY

From [Wikipedia](https://en.wikipedia.org/wiki/Big_data)
Big data primarily refers to data sets that are too large or complex to be dealt with by traditional data-processing application software.

![](https://media.licdn.com/dms/image/D4D12AQFNUAdgaoK2zQ/article-cover_image-shrink_600_2000/0/1692816749106?e=2147483647&v=beta&t=iVpvOcBQmvYllV--CopadMhBsmyGEC85qb5jMtNFaxE)

**Some argue that it has been around since the early 1990s, crediting American computer scientist John R Mashey, considered the 'father of big data', for making it popular. Others believe it was a term coined in 2005 by Roger Mougalas and the O'Reilly Media group.**

### Sources of Big Data
These data come from many sources like

- **Social networking sites**: Facebook, Google, LinkedIn all these sites generates huge amount of data on a day to day basis as they have billions of users worldwide.
- **E-commerce site**: Sites like Amazon, Flipkart, Alibaba generates huge amount of logs from which users buying trends can be traced.
- **Weather Station**: All the weather station and satellite gives very huge data which are stored and manipulated to forecast weather.
- **Telecom company**: Telecom giants like Airtel, Vodafone study the user trends and accordingly publish their plans and for this they store the data of its million users.
- **Share Market**: Stock exchange across the world generates huge amount of data through its daily transaction.

## 5 V's of Big Data

![](data:image/jpeg;base64,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)

<span style="color:red">**NOTE** : some say [6 Vs](https://www.geeksforgeeks.org/5-vs-of-big-data/) some say [7 Vs](https://dsstream.com/7-vs-of-big-data-what-are-they-and-why-are-they-so-important/) so read the links here also.</span>

### ⭐⭐⭐Read this good [article on medium](https://medium.com/analytics-vidhya/the-5-vs-of-big-data-2758bfcc51d)

Essentially 5 important V's needed :-

### 1. Volume
Volume is a huge amount of data.

To determine the value of data, size of data plays a very crucial role. **If the volume of data is very large, then it is actually considered as a ‘Big Data’**. This means whether a particular data can actually be considered as a Big Data or not, is dependent upon the volume of data.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzkP5KIJXF17VHswVYH9NnWQ_ixdBzdx8xiw&s)

### 2. Velocity 
The **speed at which the data is created and how fast it moves**.

There is a massive and continuous flow of data. This determines the potential of data that how fast the data is generated and processed to meet the demands.

Sampling data can help in dealing with the issue like ‘velocity’.


### 3. Variety
It **refers to nature of data that is structured, semi-structured and unstructured data**.

It also refers to **heterogeneous sources**.

Variety is basically the arrival of data from new sources that are both inside and outside of an enterprise. It can be structured, semi-structured and unstructured.
- **Structured data**: This data is basically an organized data. It generally refers to data that has defined the length and format of data.
- **Semi- Structured data**: This data is basically a semi-organised data. It is generally a form of data that do not conform to the formal structure of data. Log files are the examples of this type of data.
- **Unstructured data**: This data basically refers to unorganized data. It generally refers to data that doesn’t fit neatly into the traditional row and column structure of the relational database. Texts, pictures, videos etc. are the examples of unstructured data which can’t be stored in the form of rows and columns.

![](https://miro.medium.com/v2/resize:fit:1400/1*8QDJDlRmlb3Zo5gupANH5Q.jpeg)

### 4. Veracity

It refers to **inconsistencies and uncertainty in data**, that is data which is available can sometimes get messy and quality and accuracy are difficult to control.

**Big Data is also variable because of the multitude of data dimensions resulting from multiple disparate data types and sources**.

![](https://miro.medium.com/v2/resize:fit:1400/0*C8lyVlqjWAxKnpQg)

#### READ [medium blog](https://medium.com/sciforce/data-veracity-a-new-key-to-big-data-38e110391c7d)

### 5. Value

The bulk of Data having no Value is of no good to the company, unless you turn it into something useful.

Data in itself is of no use or importance but **it needs to be converted into something valuable to extract Information**.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwmQieFR8E60wKVg3DzHC0-fTB0jiE140sNA&s)

## Big data as a opportunity

From **movies recommendation of Netflix**, **product recommendation of amazon**, **flipkart to youtube video recommendation** all is based on analyzing and developing algorithsm based on our views, comments, reviews, watch hours and this data is actually very big data not some small data when to be thought of.

![alt text](<Screenshot (884).png>)

### Example of Walmart,

When the **Hurricane Sandy was about to hit New Jersey in USA**, then <span style="color:yellow">Walmart</span> used the big data analytics to profit from it. **   **. Upon detailed anaysis they found that **people tend to buy emergency stuff like flashlights, lifejackets and interestingly people also buy a lot of strawberry poptarts**. 

![](https://itdoesnttastelikechicken.com/wp-content/uploads/2014/03/vegan-strawberry-pop-tarts.jpg)
😁Pran jai par Strawberry poptart na jai!

So walmart stuffed their stores at that time with all emoergency stuff and strawberry poptarts and sold all of them and earned a  lot of profit during that time.


### Example of IBM,

Earlier electric meter records were collected in intervals of one month but now with smart and new meters they were collected in interval of 15 minutes. This generated huge amounts of data.

![alt text](<Screenshot (885).png>)

They used this data to analyze and find out current problems.

![alt text](<Screenshot (886).png>)

Upon anayzing they found out that during certains times users require more energy causing load on supply.  To balance it pricing was made based on peak-hours costing more encouraging heavy industrial machinery to be used in off-peak times reducing load on supply.

![alt text](<Screenshot (887).png>)

IBM implemented the smart meter solution as shown in following image🔽

![alt text](<Screenshot (888).png>)

### ONCOR uses IBM Smart meter solution

It helped identify peak outages and avoid such situations by manipulating prices during peak hours encouraging people to use electricity for heavy usage during off peak times to save money.

This also helped **company emerge as one of the major energy savers** in the country and also **reduced people's bills by 25%**.

![alt text](<Screenshot (889).png>)

## Problems with Big Data

### 1. Storing exponentially huge growing data sets

⚠ Statistics of video is too old

Rather Read [here](https://explodingtopics.com/blog/data-generated-per-day)

- Approximately 402.74 million terabytes of data are created each day
- Around 147 zettabytes of data will be generated this year
- 181 zettabytes of data will be generated in 2025
- Videos account for over half of internet data traffic
- The US has over 2,700 data centers

### 2. Processing the data having complex structure

Big data can be a mixture of various forms and kinds of data and extracting exact meaning from each type of data is tedious.

![alt text](<Screenshot (890).png>)

### 3. Processing huge amounts of data faster

![alt text](<Screenshot (891).png>)

### 4. Data Quality
the accuracy, relevance, and completeness of the data—is another common pain point. Human decision-making and machine learning require ample and reliable data, but larger datasets are more likely to contain inaccuracies, incomplete records, errors, and duplicates. Not correcting quality issues leads to ill-informed decisions and lost revenue.

Before analyzing big data, it must be run through automated cleansing tools that check for and correct duplicates, anomalies, missing information, and other errors. Setting specific data quality standards and measuring these benchmarks regularly will also help by highlighting where data collection and cleansing techniques must change.

### 5. Ethical Issues
Big data also comes with some ethical concerns. Gathering that much information means increased likelihood of personally identifiable information being part of it. In addition to questions about user privacy, biases in data can lead to biased AI that carries human prejudices even further.

To avoid ethical concerns, businesses should form a data ethics committee or at least have a regular ethical review process to review data collection and usage policies and ensure the company doesn’t infringe on people’s privacy. Scrubbing data of identifying factors like race, gender, and sexuality will also help remove bias-prone information from the equation.

### 6. Lack Of Experience
Technical issues may be the easiest challenges to recognize, but user-side challenges deserve attention too—and one of the biggest is a lack of big data experience. Making sense of big data and managing its supporting infrastructure requires a skillset lacking in many organizations. There’s a nationwide shortage of jobseekers with the skills being sought by enterprises, and it’s not getting any better.

## Hadoop🐘

According to [Wikipedia](https://en.wikipedia.org/wiki/Apache_Hadoop),

Apache Hadoop is a collection of open-source software utilities that facilitates **using a network of many computers to solve problems involving massive amounts of data and computation**. It provides a software framework for distributed storage and processing of big data using the MapReduce programming model.

### History

Apache Software Foundation is the developers of Hadoop, and it’s co-founders are **Doug Cutting** and **Mike Cafarella**. **It’s co-founder Doug Cutting named it on his son’s toy elephant**. In October 2003 the first paper release was Google File System. In January 2006, MapReduce development started on the Apache Nutch which consisted of around 6000 lines coding for it and around 5000 lines coding for HDFS. In April 2006 Hadoop 0.1.0 was released.

![](https://alchetron.com/cdn/doug-cutting-1c09e78b-fa6d-4b1e-af24-2b2c8f5fcc7-resize-750.jpg)

Doug Cutting with Hadoop elephant toy


### ⭐⭐Read [medium blog](https://medium.com/cdapio/the-need-for-abstraction-in-hadoop-b004b822f6ff)

### Hadoop has two main components:
1. **HDFS (Hadoop Distributed File System)**: This is the **storage component** of Hadoop, which allows for the storage of large amounts of data across multiple machines. It is designed to work with commodity hardware, which makes it cost-effective.
2. **YARN (Yet Another Resource Negotiator)**: This is the **resource management component** of Hadoop, which manages the allocation of resources (such as CPU and memory) for processing the data stored in HDFS.

Hadoop also includes several additional modules that provide additional functionality, such as **Hive (a SQL-like query language), Pig (a high-level platform for creating MapReduce programs), and HBase (a non-relational, distributed database)**.

Hadoop is commonly used in big data scenarios such as data warehousing, business intelligence, and machine learning. It’s also used for data processing, data analysis, and data mining. It enables the distributed processing of large data sets across clusters of computers using a simple programming model.

### Hadoop Distributed File System

It has **distributed file system** known as HDFS and this HDFS **splits files into blocks and sends them across various nodes in form of large clusters**. Also in case of a node failure, the system operates and data transfer takes place between the nodes which are facilitated by HDFS.

![alt text](<Screenshot (892).png>)
It kind of master-slave architecture. The master node contains metadata about the slave nodes containing information like :-

- how data is stored in different Data nodes
- which datanode contains what data
- which datanodes stored replicated data for failure control

.... so on.

This solves various problems:-

### 1. Storing large data of multiple small storage systems

Assume I have 1 TB of big data now we can store it into multiple 256 GB or any smaller than 1 TB of storages in different nodes/ computers by breaking them into pieces as required. This wont force us to get a node of 1TB to store the data.

![alt text](<Screenshot (893).png>)

### 2. Storing different kinds of data is easy

We can now store different forms of data more easily since **HDFS does not perform any schema validation during dumping data and also allows write once read many (WORM)**.

![alt text](<Screenshot (894).png>)

### 3. Processing Data Faster

In master slave architecture processing can take place in individual nodes instead of a single node storing all data and processing all data and processing them all at once. Hence parallel processing is employed which is faster and efficient.

Chunks of output from all slave node is then combined at master node to provide user the output.

![alt text](<Screenshot (895).png>)


### Hadoop ecosystem

⭐⭐Read [gfg](https://www.geeksforgeeks.org/hadoop-ecosystem/) and [databricks blog](https://www.databricks.com/glossary/hadoop-ecosystem)

Apache Hadoop ecosystem **refers to the various components of the Apache Hadoop software library**; it includes open source projects as well as a complete range of complementary tools. Some of the most well-known tools of the Hadoop ecosystem include HDFS, Hive, Pig, YARN, MapReduce, Spark, HBase, Oozie, Sqoop, Zookeeper, etc. Here are the major Hadoop ecosystem components that are used frequently by developers.

![](https://www.edureka.co/blog/wp-content/uploads/2016/10/HADOOP-ECOSYSTEM-Edureka.png)

####  What is HDFS?
Hadoop Distributed File System (HDFS), is one of the largest Apache projects and primary storage system of Hadoop. It employs a NameNode and DataNode architecture. It is a distributed file system able to store large files running over the cluster of commodity hardware

#### What is Hive?
Hive is an ETL and Data warehousing tool used to query or analyze large datasets stored within the Hadoop ecosystem. Hive has three main functions: data summarization, query, and analysis of unstructured and semi-structured data in Hadoop. It features a SQL-like interface, HQL language that works similar to SQL and automatically translates queries into MapReduce jobs.

#### What is Apache Pig?
This is a high-level scripting language used to execute queries for larger datasets that are used within Hadoop. Pig's simple SQL-like scripting language is known as Pig Latin and its main objective is to perform the required operations and arrange the final output in the desired format.

#### What is MapReduce?

![](https://www.databricks.com/sites/default/files/inline-images/map-reduce.png)

This is another data processing layer of Hadoop. It has the capability to process large structured and unstructured data as well as to manage very large data files in parallel by dividing the job into a set of independent tasks (sub-job).

#### What is YARN?
**YARN stands for Yet Another Resource Negotiator**, but it's commonly referred to by the acronym alone. It is one of the core components in open source Apache Hadoop suitable for resource management. It is responsible for managing workloads, monitoring, and security controls implementation. It also allocates system resources to the various applications running in a Hadoop cluster while assigning which tasks should be executed by each cluster nodes. YARN has two main components:

- Resource Manager
- Node Manager

#### What is Apache Spark?

![](https://www.databricks.com/sites/default/files/inline-images/spark.png)

Apache Spark is a fast, in-memory data processing engine suitable for use in a wide range of circumstances. Spark can be deployed in several ways, it features Java, Python, Scala, and R programming languages, and supports SQL, streaming data, machine learning, and graph processing, which can be used together in an application.



![alt text](<Screenshot (896).png>)


Following are the components that collectively form a Hadoop ecosystem: 
<ul>
<li value="1"><b><strong>HDFS: </strong></b><span>Hadoop Distributed File System</span></li>
<li value="2"><b><strong>YARN:</strong></b><span> Yet Another Resource Negotiator</span></li>
<li value="3"><b><strong>MapReduce:</strong></b><span> Programming based Data Processing</span></li>
<li value="4"><b><strong>Spark:</strong></b><span> In-Memory data processing</span></li>
<li value="5"><b><strong>PIG, HIVE:</strong></b><span> Query based processing of data services</span></li>
<li value="6"><b><strong>HBase: </strong></b><span>NoSQL Database</span></li>
<li value="7"><b><strong>Mahout, Spark MLLib:</strong></b><span> </span><a href="https://www.geeksforgeeks.org/machine-learning/"><span>Machine Learning </span></a><span>algorithm libraries</span></li>
<li value="8"><b><strong>Solar, Lucene:</strong></b><span> Searching and Indexing</span></li>
<li value="9"><b><strong>Zookeeper:</strong></b><span> Managing cluster</span></li>
<li value="10"><b><strong>Oozie:</strong></b><span> Job Scheduling</span></li>
</ul>

![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/HadoopEcosystem-min.png)

### Advantages and Disadvantages

⭐⭐Read [gfg](https://www.geeksforgeeks.org/hadoop-an-introduction/)





<br/><br/><br/><br/><br/><br/>

# Introduction to Apache Spark

Video link : https://youtu.be/9mN3N3aoF2w

⭐⭐Read [amazon awws blog](https://aws.amazon.com/what-is/apache-spark/)  

**Apache Spark is an open-source, distributed processing system used for big data workloads**. It utilizes in-memory caching, and optimized query execution for fast analytic queries against data of any size. **It provides development APIs in Java, Scala, Python and R, and supports code reuse across multiple workloads—batch processing, interactive queries, real-time analytics, machine learning, and graph processing**. You’ll find it used by organizations from any industry, including at FINRA, Yelp, Zillow, DataXu, Urban Institute, and CrowdStrike.

![](https://www.databricks.com/en-website-assets/static/5e953f5a26d3e6b7949bff788ef5a2af/largest-open-source-apache-spark1679038543.png)

### History
Apache Spark started in 2009 as a research project at UC Berkley’s AMPLab, a collaboration involving students, researchers, and faculty, focused on data-intensive application domains. The goal of Spark was to create a new framework, optimized for fast iterative processing like machine learning, and interactive data analysis, while retaining the scalability, and fault tolerance of Hadoop MapReduce. The first paper entitled, “Spark: Cluster Computing with Working Sets” was published in June 2010, and Spark was open sourced under a BSD license. In June, 2013, Spark entered incubation status at the Apache Software Foundation (ASF), and established as an Apache Top-Level Project in February, 2014. Spark can run standalone, on Apache Mesos, or most frequently on Apache Hadoop.

### How does Apache Spark work?
**Hadoop MapReduce is a programming model for processing big data sets with a parallel, distributed algorithm**. Developers can write massively parallelized operators, without having to worry about work distribution, and fault tolerance. However, **a challenge to MapReduce is the sequential multi-step process it takes to run a job. With each step, MapReduce reads data from the cluster, performs operations, and writes the results back to HDFS. Because each step requires a disk read, and write, MapReduce jobs are slower due to the latency of disk I/O**.

**Spark was created to address the limitations to MapReduce, by doing processing in-memory, reducing the number of steps in a job, and by reusing data across multiple parallel operations**. With Spark, **only one-step is needed where data is read into memory, operations performed, and the results written back—resulting in a much faster execution**. Spark also reuses data by using an in-memory cache to greatly speed up machine learning algorithms that repeatedly call a function on the same dataset. Data re-use is accomplished through the creation of DataFrames, an abstraction over Resilient Distributed Dataset (RDD), which is a collection of objects that is cached in memory, and reused in multiple Spark operations. This dramatically lowers the latency making Spark multiple times faster than MapReduce, especially when doing machine learning, and interactive analytics.

### Apache Spark vs. Apache Hadoop
Outside of the differences in the design of Spark and Hadoop MapReduce, **many organizations have found these big data frameworks to be complimentary, using them together to solve a broader business challenge**.

Hadoop is an **open source framework that has the Hadoop Distributed File System (HDFS) as storage**, YARN as a way of managing computing resources used by different applications, and an implementation of the MapReduce programming model as an execution engine. **In a typical Hadoop implementation, different execution engines are also deployed such as Spark, Tez, and Presto**.

Spark is an open source framework focused on interactive query, machine learning, and real-time workloads.**It does not have its own storage system, but runs analytics on other storage systems like HDFS, or other popular stores like Amazon Redshift, Amazon S3, Couchbase, Cassandra, and others**. Spark on Hadoop leverages YARN to share a common cluster and dataset as other Hadoop engines, ensuring consistent levels of service, and response.

### Why Apache Spark came into Picture?

⭐⭐See this [video](https://youtu.be/v_uodKAywXA?t=119) 

<span style="color:red">2 main issues with hadoop </span>

- Hadoop relied **storing data on harddisks** which made storing and fetching and writing data much much slower.
![](https://qph.cf2.quoracdn.net/main-qimg-c89c960f0bcdda9658e8363ae447cf3e-pjlq)

- Hadoop's processing model particularly *MapReduce* is inherently batch-oriented. In this model, data is processed in **large chunks or batches**. This means a job must complete processing of a batch before it can move on to the next batch. This introduces latency nad system needs to wait for the entire batch to complete before the next job can start.

Hence a more **real time data processing system** was needed.

### Apache Spark addresses the issues of Hadoop

- Spark supports both batch and stream processing, making it more versatile for different types of data processing needs.

- It introduced powerful concept of **Resilient Distributed Datasets (RDDs)** : RDDs are **immutable collections of objects that can be processed in parallel across a cluster**. They support fault tolerance and in-memory computation, which significantly improve performance and reliability.

- **Spark's ability to perform in-memory computations** is one of its major advantages. By storing intermediate data in memory, Spark avoids the I/O overhead associated with writing to and reading from disk, which is typical in Hadoop's MapReduce. This results in significant performance improvements, especially for iterative algorithms that need to repeatedly access the same data.

- **For simple ETL tasks, the speedup might be closer to 10x, whereas for iterative tasks, it could indeed approach or exceed 100x😱 than Hadoop.**

## Main components of Apache Spark

⭐⭐Read [gfg](https://www.geeksforgeeks.org/components-of-apache-spark/)

![](https://media.geeksforgeeks.org/wp-content/uploads/20200616181455/spark2.png)

### 1. Spark Core
All the functionalities being provided by Apache Spark are built on the highest of the **Spark Core**. It delivers speed by providing in-memory computation capability. Spark Core is the foundation of parallel and distributed processing of giant dataset. **It is the main backbone of the essential I/O functionalities and significant in programming and observing the role of the spark cluster. It holds all the components related to scheduling, distributing and monitoring jobs on a cluster, Task dispatching, Fault recovery.**

 The functionalities of this component are:
- It contains the basic functionality of spark. (Task scheduling, memory management, fault recovery, interacting with storage systems).
- Home to API that defines RDDs.

### 2. Spark SQL Structured data
The Spark SQL component is **built above the spark core and used to provide the structured processing on the data**. It provides standard access to a range of data sources. **It includes Hive, JSON, and JDBC. It supports querying data either via SQL or via the hive language**. 
- This also works to access structured and semi-structured information. 
- It also provides powerful, interactive, analytical application across both streaming and historical data. 

Spark SQL could be a new module in the spark that integrates the relative process with the spark with programming API. 

The main functionality of this module is:
- It is a Spark package for working with structured data.
- It Supports many sources of data including hive tablets, parquet, json.
- It allows the developers to intermix SQK with programmatic data manipulation supported by RDDs in python, scala and java.

### 3. Spark Streaming
Spark streaming **permits ascendible, high-throughput, fault-tolerant stream process of live knowledge streams**. Spark can access data from a source like a flume, TCP socket. It will operate different algorithms in which it receives the data in a file system, database and live dashboard. **Spark uses Micro-batching for real-time streaming**. 

<span style="color:yellow">Micro-batching is a technique that permits a method or a task to treat a stream as a sequence of little batches of information.</span> 

Hence **spark streaming groups the live data into small batches. It delivers it to the batch system for processing**. 

The functionality of this module is:
- Enables processing of live streams of data like log files generated by production web services.
- The API’s defined in this module are quite similar to spark core RDD API’s.


### 4. Mllib Machine Learning
MLlib in spark is a **scalable Machine learning library that contains various machine learning algorithms**. The motive behind MLlib creation is to make the implementation of machine learning simple. **It contains machine learning libraries and the implementation of various algorithms. For example, clustering, regression, classification and collaborative filtering**.

### 5. GraphX graph processing
It is an **API for graphs and graph parallel execution**. There is network analytics in which we store the data. Clustering, classification, traversal, searching, and pathfinding is also possible in the graph. 
- It generally optimizes how we can represent vertex and edges in a graph. 
- GraphX also optimizes how we can represent vertex and edges when they are primitive data types. 

To support graph computation, it supports fundamental operations like subgraph, joins vertices, and aggregate messages as well as an optimized variant of the Pregel API.



<br/><br/><br/><br/><br/><br/>

# Set up Databricks Community

Read here : https://www.databricks.com/blog/2016/02/17/introducing-databricks-community-edition-apache-spark-for-all.html

## Whis is Databricks?

According to [wikipedia](https://en.wikipedia.org/wiki/Databricks),

Databricks, Inc. is a **global data, analytics and artificial intelligence company** founded by the original creators of Apache Spark. **The company provides a cloud-based platform to help enterprises build, scale, and govern data and AI, including generative AI and other machine learning models**.

Databricks is used for building, testing, and deploying machine learning and analytics applications to help achieve better business outcomes.

Databricks integrates with cloud services like **Azure, GCP, AWS**.

## Difference between Databricks and Azure Databricks

Read this [reddit post](https://www.reddit.com/r/dataengineering/comments/v4a7gr/what_is_the_difference_between_azure_databricks/) and [microsoft community forum](https://techcommunity.microsoft.com/t5/analytics-on-azure/data-bricks-in-azure-vs-aws/m-p/1776174)

Databricks is available on all major platforms like Azure, Aws, and Google cloud.

<span style="color:yellow">
The main thing is databricks is available on aws and google cloud as third party service.
</br></br>
But on Azure it is available as first party service meaning you have a unified billing.
</span>

Azure databricks is using the same thing from databricks but just provides you a unified billing platform where all your databricks and storage cost are coming from Azure.

**At a high level, Azure Databricks is a first party service on Azure. What that means is that it's more than a partnership- there are deep integrations between Azure services and Azure Databricks.** Examples of what this entails:

- **Azure Key Vault Secret Stores in Databricks** - Users can work with secrets they have access to, without the secrets ever being exposed to the end user
- **Azure Active Directory Support** - User credentials on Azure used to authenticate to Azure Databricks, and data in Azure Data Lake Storage accessed through those credentials 'passed through' from Azure Databricks. This allows teams to configure permissions on files to users and groups, and Azure Databricks authenticates the rest
- **Top level integration with Azure Data Factory**, allowing scheduling of notebooks as jobs in a data estate
- **Integrating easily with other Azure Data Services (Cosmos DB, Synapse) through service endpoints on private networks**

As a general rule, the integrations to the rest of the Azure platform are deeper on Azure Databricks, compared to how even Databricks on AWS integrates with other AWS services. Overall, this builds a more seamless and streamlined experience for building out your data estate with Databricks.

## 🔥🔥Which one is free to use🤔

**Community edition with limited features is free to use**

### ⭐⭐⭐READ THIS : https://databricks.com/try-databricks


### <span style="color:red">Please note that Free Trial is different from community edition hence please read the above link before signing up</span>

If you sign up for free trial it ends in 14 days but community edition does not

### Read databricks own article  
https://www.databricks.com/product/faq/community-edition

As mentioned 

`
The Databricks Community Edition access is not time-limited and users will not incur AWS costs for their cluster usage.
`

<br/><br/><br/><br/><br/><br/>

# Apache spark installation

Read here : https://spark.apache.org/downloads.html



<br/><br/><br/><br/><br/><br/>

# Java installation

Read here : https://www.oracle.com/java/technologies/downloads/

Installed JDK 18 already before. 


<br/><br/><br/><br/><br/><br/>

# Apache spark & python installation

Read here : https://www.sundog-education.com/spark-python/



<br/><br/><br/><br/><br/><br/>

# Traditional Approach and its Limitation

Read here : https://www.geeksforgeeks.org/big-challenges-with-big-data/

<div class="text" style="height: auto; overflow: unset; mask-image: none;">
                                                                <p>The challenges in <a href="https://www.geeksforgeeks.org/world-big-data/" rel="noopener" target="_blank"><strong>Big Data</strong></a> are the real implementation hurdles. These require immediate attention and need to be handled because if not handled then the failure of the technology may take place which can also lead to some unpleasant result. Big data challenges include the storing, analyzing the extremely large and fast-growing data.</p>
<p><strong>Some of the Big Data challenges are:</strong></p>
<ol>
<li><strong><em>Sharing and Accessing Data: </em></strong>
<ul>
<li>Perhaps the most frequent challenge in big data efforts is the inaccessibility of data sets from external sources.</li>
<li> Sharing data can cause substantial challenges.</li>
<li> It include the need for inter and intra- institutional legal documents.</li>
<li> Accessing data from public repositories leads to multiple difficulties.</li>
<li>It is necessary for the data to be available in an accurate, complete and timely manner because if data in the companies information system is to be used to make accurate decisions in time then it becomes necessary for data to be available in this manner.</li>
</ul>
</li>
<p><br></p>
<li><strong><em>Privacy and Security:</em></strong>
<ul>
<li>It is another most important challenge with Big Data. This challenge includes sensitive, conceptual, technical as well as legal significance.</li>
<li>Most of the organizations are unable to maintain regular checks due to large amounts of data generation. However, it should be necessary to perform security checks and observation in real time because it is most beneficial.</li>
<li>There is some information of a person which when combined with external large data may lead to some facts of a person which may be secretive and he might not want the owner to know this information about that person.</li>
<li>Some of the organization collects information of the people in order to add value to their business. This is done by making insights into their lives that they’re unaware of.</li>
</ul>
</li>
<p><br></p>
<li><strong><em>Analytical Challenges: </em></strong>
<ul>
<li>There are some huge analytical challenges in big data which arise some main challenges questions like how to deal with a problem if data volume gets too large?</li>
<li>Or how to find out the important data points?</li>
<li>Or how to use data to the best advantage?</li>
<li>These large amount of data on which these type of analysis is to be done can be structured (organized data), semi-structured (Semi-organized data) or unstructured (unorganized data). There are two techniques through which decision making can be done:
<ul>
<li>Either incorporate massive data volumes in the analysis.</li>
<li>Or determine upfront which Big data is relevant.</li>
</ul>
</li></ul>
</li>
<p><br></p>
<li><strong><em>Technical challenges:</em></strong>
<ul>
<li><strong>Quality of data:</strong>
<ul>
<li>When there is a collection of a large amount of data and storage of this data, it comes at a cost. Big companies, business leaders and IT leaders always want large data storage.</li>
<li>For better results and conclusions, Big data rather than having irrelevant data, focuses on quality data storage.</li>
<li>This further arise a question that how it can be ensured that data is relevant, how much data would be enough for decision making and whether the stored data is accurate or not.</li>
</ul>
</li>
<li><strong>Fault tolerance:</strong>
<ul>
<li>Fault tolerance is another technical challenge and fault tolerance computing is extremely hard, involving intricate algorithms.</li>
<li>Nowadays some of the new technologies like cloud computing and big data always intended that whenever the failure occurs the damage done should be within the acceptable threshold that is the whole task should not begin from the scratch.</li>
</ul>
</li>
<li><strong>Scalability:</strong>
<ul>
<li>Big data projects can grow and evolve rapidly. The scalability issue of Big Data has lead towards cloud computing.</li>
<li>It leads to various challenges like how to run and execute various jobs so that goal of each workload can be achieved cost-effectively.</li>
<li>It also requires dealing with the system failures in an efficient manner. This leads to a big question again that what kinds of storage devices are to be used.</li>
</ul>
</li>
</ul>
</li></ol>
<div hidead="MID"></div><br><div id="AP_G4GR_6"></div>

<br/><br/><br/><br/><br/><br/>

# Hadoop

Read here : https://intellipaat.com/blog/top-big-data-challenges/

## Challenges with Big data and remedies

### 1. Data Growth
One of the most pressing Big Data challenges is storage. Data is growing exponentially with time, and with that, enterprises are struggling to store large amounts of data. Much of this data is extracted from images, audio, documents, text files, etc., that are unstructured and not in databases. It is difficult to extract and analyze all unstructured data. These issues are a part of Big Data infrastructure challenges.

#### Solution:
 Dealing with rapid data growth can be facilitated through converged and hyper-converged infrastructure and software-defined storage. Additionally, compression, tiering, and deduplication can reduce space consumption as well as cut storage costs. Enterprises also use tools such as Big Data Analytics software, Hadoop and NoSQL databases, Spark, AI, Machine Learning, BI applications, etc., to deal with this issue.


### 2. Real-time Insights
Data sets are a treasure trove of insights. However, data sets are of no value if no real-time insights are drawn from them. Now, some may define real-time as instantaneous while others may consider it as the time taken between data extraction and analysis. However, the core idea is to generate actionable insights to bring about efficiency in result-oriented tasks such as:

- Establishing new avenues for innovation and disruption
- Speeding up the process of service deployment
- Cutting costs through operational cost efficiencies
- New product launches and service offerings
- Encouraging a data-driven culture
#### Solution: 
One of the Big Data challenges is the generation of timely reports and insights. To achieve that, enterprises are looking to invest in ETL and analytics tools with real-time capabilities to have a level playing field with competitors in the market.


### 3. Data Validation
Data validation on a Big Data scale can be rather difficult. An organization can get similar sets of data from different sources but the data from these sources may not always be similar. Getting the data to agree with each other and looking out for accuracy, usability, and security fall under a process called data governance. According to a 2016 survey by AtScale, the fastest-growing concern was data governance.

#### Solution:
 Tackling Big Data management challenges and data governance can be complex with all the policy changes combined with technology. Special teams are assigned to handle data governance and invest in ad-hoc data management solutions that ensure data accuracy.


### 4. Data Security
Security can be one of the most daunting Big Data challenges especially for organizations that have sensitive company data or have access to a lot of personal user information. Vulnerable data is an attractive target for cyberattacks and malicious hackers.

When it comes to data security, most organizations believe that they have the right security protocols in place that are sufficient for their data repositories. Only a few organizations invest in additional measures exclusive to Big Data such as identity and access authority, data encryption, data segregation, etc. Often, organizations are more immersed in activities involving data storage and analysis. Data security is usually put on the back burner, which is not a wise move at all as unprotected data can fast become a serious problem. Stolen records can cost an organization millions.

#### Solution: 
The following are the ways how an enterprise can tackle the security challenges of Big Data:

- Recruiting more cybersecurity professionals
- Data encryption and segregation
- Identity and access authorization control
- Endpoint security
- Real-time monitoring
- Using Big Data security tools such as IBM Guardium

### 5. Big Data Skills
Running Big Data tools requires expertise that is possessed by data scientists, data engineers, and data analysts. They have the skills to handle Big Data challenges and come up with valuable insights for the company they work in. The problem is not the demand but the lack of such skills that, in turn, becomes a challenge. Big Data salaries have drastically increased over the years. According to ZipRecruiter, as of January 2021, the average annual compensation offered to Big Data Specialists in the United States is US$107,892. Although organizations are spending on recruiting professionals with such skills, organizations are also investing in training their existing staff as well.

#### Solution:
 Data professionals are not able to keep up with the rate data handling tools are evolving. Hence, organizations invest in AI- or ML-powered data analytics solutions. This allows even non-experts to easily run tools with basic knowledge. This way, companies can cut recruitment costs and achieve Big Data goals.

 ### 6. Increasing Salaries of Skilled Big Data Professionals
Big Data salaries have increased significantly. According to the 2017 Robert Half Technology Salary Guide, big data engineers have salaries between US$135,000 and US$196,000 on average. while data scientists earn around US$116,000 to US$163, 500. BI analysts make around US$118,000 to US$138,750 annually.

#### Solution: 
To deal with the shortage of talent, organizations have had to increase their budgets as well as the efforts to recruit and retain. Therefore, these organizations are training their current staff members in an attempt to have the skills from within the company.

Some are also looking to technology like analytics solutions that have self-service as well as machine learning capabilities. These solutions are designed to be used by professionals without extensive knowledge in data science. In this way, it is possible to achieve big data goals without spending on big data experts.


### 7. Resistance to Big Data Adoption
It is not only about the technological challenges of conventional systems in Big Data but also about the resistance that is faced by Big Data adoption. While many want to introduce data-driven culture in their organizations, only a few are able to adopt it successfully. Why is it a challenge? It is observed to be because of three major reasons:

- Business resistance due to lack of understanding
- Lack of organizational alignment
- Lack of middle management understanding and adoption

Primarily, due to the lack of understanding of Big Data, organizations fail in their initiatives to adopt Big Data. Most employees are unaware of what data is, let alone have any idea of its importance. If employees do not understand the importance of Big Data, they may not follow the correct procedures or protocols that are necessary for handling Big Data and, as a result, introduce unseen setbacks.

#### Solution: 
Introducing Big Data can bring about a tremendous change in any organization, which can be difficult. Workshops, seminars, and training programs are a great way to introduce employees at all levels to the world of Big Data. Decision-making will improve with strong leadership that knows how to capitalize on the opportunities provided by Big Data. Thus, the challenges associated with Big Data’s adoption and implementation are still continuing to hamper the organizations’ progress.

## Big Data Risks in Other Sectors

### 1. Big Data Challenges in Healthcare
Here are some of the challenges in healthcare analytics platform:

- Efficiency of diagnoses
- Prescribing preventive medicine
- Providing medical results in a digital form
- Using predictive analysis to identify patterns
- Real-time monitoring
- Developing data exchange and interoperability architecture for personalized patient care
- Developing AI-based analytical platform for the integration of multi-sourced data
- Predictive and prescriptive modeling platform to minimize the semantic gap for an accurate diagnosis


### 2. Big Data Challenges in Security Management
- Fake data generation
- Granular access control
- Challenges in data security in systems
- Data provenance
- Real-time data security


### 3. Big Data Challenges in Hadoop-Data Lake Migration
Migration from Hadoop can happen due to a variety of reasons. Below are some of the common reasons why migration becomes a challenge:

- Poor data scalability and reliability
- Blocked projects
- Cost of time and resource
- Runtime quality issues
- Unsupportive service


### 4. Big Data Challenges in Cloud Security Governance
Some of the challenges in cloud security governance are:-

- Performance management
- Cost management
- Security issues
- Governance/control

