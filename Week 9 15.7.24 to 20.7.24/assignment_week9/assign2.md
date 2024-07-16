# ASSIGNMENT 2

1. Create different parquet files for each date between 2018-01-01 and 2020-23-10. Name of the parquet file should follow the nomenclature '`TSK_YYYYMMDD.parquet`' 

2. Load all parquets under different folders in Data Lake basis their Year-Month. Ex : File `TSK_20190201` should be loaded to folder '`201902`' 

3. Create a read function in Databricks that takes 2 dates and reads from ADLS only those parquet files that are lying between that date range. Create a single dataframe out of all the read parquets

# SOLUTION


