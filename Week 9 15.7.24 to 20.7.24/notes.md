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







<br/><br/><br/><br/><br/><br/>

# Introduction to Apache Spark

Video link : https://youtu.be/9mN3N3aoF2w



<br/><br/><br/><br/><br/><br/>

# Set up Databricks Community

Read here : https://www.databricks.com/blog/2016/02/17/introducing-databricks-community-edition-apache-spark-for-all.html



<br/><br/><br/><br/><br/><br/>

# Apache spark installation

Read here : https://spark.apache.org/downloads.html



<br/><br/><br/><br/><br/><br/>

# Java installation

Read here : https://www.oracle.com/java/technologies/downloads/



<br/><br/><br/><br/><br/><br/>

# Apache spark & python installation

Read here : https://www.sundog-education.com/spark-python/



<br/><br/><br/><br/><br/><br/>

# Traditional Approach and its Limitation

Read here : https://www.geeksforgeeks.org/big-challenges-with-big-data/



<br/><br/><br/><br/><br/><br/>

# Hadoop

Read here : https://intellipaat.com/blog/top-big-data-challenges/


