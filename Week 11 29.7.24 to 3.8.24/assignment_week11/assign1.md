# Assignment 

Refer to the table CustomerDim Implement SCD Type-2 on the `CustomerDim table`. Initially it has got few records. 

You need to create an insert trigger with the name `trg_dim` on the table `CustomerDim` that performs the necessary operation and maintains the data as maintained in SCD Type-2. 

Initially Table Has the Following Records: 

CustomerID | CustomerName | Address | EffectiveStartDate | EffectiveEndDate |IsCurrent
-----------|--------------|---------|-----------|-----------|-----------
 1 |John Doe| 123 Main St |2023-01-01 |9999-12-31 |1 
 2 |Alice Johnson |456 Elm St |2023-01-01 |9999-12-31| 1
3 |Bob Smith |789 Oak St |2023-01-01 |9999-12-31 |1 


After Creating the Trigger, you have to insert the following records in the CustomerDim table:

CustomerID |CustomerName |Address 
-----------|-------------|-------
1 |John Doe |Ajmer 
4 |David Richard |Mumbai 
3 |Bob Smith |Chennai 
5 |Eva Dsouza |Mumbai

When the records are inserted, the value in the `EffectiveStartDate` column, `EffectiveEndDate` column and `IsCurrent` column should be updated accordingly. 

The `EffectiveStartDate` column for the newly inserted records should have the current date. 

You are required to update the `EffectiveEndDate` with one day before that of the new `EffectiveStartDate` for the historical records. 

Refer the sample output given below: 

**Sample Output**: 

CustomerID |CustomerName |Address| EffectiveStartDate |EffectiveEndDate |IsCurrent
-----------|-------------|---------|------------|-----------|------------
1 |John Doe |123 Main St |2023-01-01 |2023-09-10 |0 
1 |John Doe |Ajmer |2023-09-11 |9999-12-31 |1

 #### Please keep object names and column names exactly same as mentioned in the question.


 # Solution

 