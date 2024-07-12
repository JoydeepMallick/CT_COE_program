# ASSIGNMENT 1

Load NYC taxi data to DataLake/Blob_Storage/DataBricks and extract the data through dataframe in the notebook. 

Perform Following **Queries using PySpark**. 

**Query 1.** - Add a column named as ""`Revenue`"" into dataframe which is the sum of the below columns '`Fare_amount`','`Extra`','`MTA_tax`','`Improvement_surcharge`','`Tip_amount`','`Tolls_amount`','`Total_amount`' 

**Query 2.** - Increasing count of total passengers in New York City by area 

**Query 3.** - Realtime Average fare/total earning amount earned by 2 vendors 

**Query 4.** - Moving Count of payments made by each payment mode 

**Query 5.** - Highest two gaining vendor's on a particular date with no of passenger and total distance by cab 

**Query 6.** - Most no of passenger between a route of two location. 

**Query 7.** - Get top pickup locations with most passengers in last 5/10 seconds."


### Resources :
http://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml 

Choose `Trip sheet data -> 2018 -> January -> yellow` 

Type https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv




# Solution

## <span style="color:red">**NOTE**</span>

The provided [link](https://www.nyc.gov/html/tlc/html/about/trip_record_data.shtml) for the trip_record shows

```
Taxi & Limousine Commission has recently redesigned its website and this page has moved. Please update your bookmark to:

https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

You will be redirected in 5 seconds, or click on the link above.
```

### The actual link (🤔Probably) to download can be [found here](https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2018-01.parquet)

The second link for [yellow_tripdata_2020-01.csv](https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv) shows permission denied as follows :-

```xml
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<Error>
<Code>AccessDenied</Code>
<Message>Access Denied</Message>
<RequestId>WPZX6J4XDJNWK8YN</RequestId>
<HostId>x3zXQTO6jLgQg4Q232lwGnmIeYCksbGLCzPcXqKKGHxm3TDKguWcS65zd6g9q54LgPe2y/OId8E=</HostId>
</Error>
```
 
## Steps to approach the problem

