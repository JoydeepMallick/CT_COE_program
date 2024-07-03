# ASSIGNMENT 1

Let's suppose you have 3 different types of file 
1) `CUST_MSTR_20191112.csv` 
2) `master_child_export-20191112.csv` 
3) `H_ECOM_ORDER.csv` 

All these files will be in the data lake container You have to fetch all three types of files into their respective folders. 

**Note**: There could be multiple files on all 3 types for different dates for example `CUST_MSTR_20191112.csv` and `CUST_MSTR_20191113.csv `

1) For the "`CUST_MSTR`" starting name of the file You have to create an additional column for a date that will fetch the data value from the filename and put it into an additional column Date format: 2019-11-12 and load it into the "`CUST_MSTR`" table 
2) For the "`master_child_export`" starting name of the file You have to create two additional columns date and date key which will fetch the data from the filename and put it into the additional columns. 
    - Date format: 2019-11-12 
    - DateKey format: 20191112 

    and load it into the "`master_child`" table 
3) for the "`H_ECOM_ORDER`" type of file you have to load it into the database as it is. and load it into "`H_ECOM_Orders`" table **Note**: This process will work on truncate load on a daily basis


**Resources :**
https://drive.google.com/drive/folders/1jtasnqX7BnmPfDKEWx2WBmDlN20el1AE?usp=drive_link
