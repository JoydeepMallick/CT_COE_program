# SQL Server stored procedures

[read more](https://www.sqlshack.com/sql-server-stored-procedures-for-beginners/)


SQL Server stored procedure is a batch of statements grouped as a logical unit and stored in the database. The stored procedure accepts the parameters and executes the T-SQL statements in the procedure, returns the result set if any.

## Benefits of using a stored procedure
1. **It can be easily modified**: We can easily modify the code inside the stored procedure **without the need to restart or deploying the application**. For example, If the T-SQL queries are written in the application and if we need to change the logic, we must change the code in the application and re-deploy it. **SQL Server Stored procedures eliminate such challenges by storing the code in the database**. So, when we want to change the logic inside the procedure we can just do it by simple `ALTER PROCEDURE` statement.

2. **Reduced network traffic**: When we use stored procedures instead of writing T-SQL queries at the application level, **only the procedure name is passed over the network instead of the whole T-SQL code.**

3. **Reusable**: Stored procedures can be executed by multiple users or multiple client applications without the need of writing the code again.

4. **Security**: Stored procedures reduce the threat by **eliminating direct access to the tables**. we can also encrypt the stored procedures while creating them so that source code inside the stored procedure is not visible. Use third-party tools like *ApexSQL Decrypt* to decrypt the encrypted stored procedures.

5. **Performance**: The SQL Server stored procedure when executed **for the first time creates a plan and stores it in the buffer pool so that the plan can be reused when it executes next time**.

## Creating a simple stored procedure

Assume following tables :-

**Product**
ProductID INT| ProductName VARCHAR(100)
-------------|------------------------
680          |'HL Road Frame - Black, 58'
706          |'HL Road Frame - Red, 58'
707          |'Sport-100 Helmet, Red'

**ProductDescription**
ProductID INT| ProductDescription VARCHAR(800)
-------------|--------------------------------
680          |'Replacement mountain wheel for entry-level rider.'
706          |'Sturdy alloy features a quick-release hub.'
707          |'Aerodynamic rims for smooth riding.'

We will create a simple stored procedure that joins two tables and returns the result set as shown in the following example.
```sql
CREATE PROCEDURE GetProductDesc
AS
BEGIN
SET NOCOUNT ON
 
SELECT P.ProductID,P.ProductName,PD.ProductDescription  FROM 
Product P
INNER JOIN ProductDescription PD ON P.ProductID=PD.ProductID
 
END
```
We can use `EXEC ProcedureName` to execute stored procedures. When we execute the procedure GetProductDesc, the result set looks like below.

![](https://www.sqlshack.com/wp-content/uploads/2019/07/result-set-of-a-sql-server-stored-procedure.png)

## Creating a stored procedure with parameters

Let us create a SQL Server stored procedure that accepts the input parameters and processes the records based on the input parameter.

Following is the example of a stored procedure that accepts the parameter.

```sql
CREATE PROCEDURE GetProductDesc_withparameters
(@PID INT)
AS
BEGIN
SET NOCOUNT ON
 
SELECT P.ProductID,P.ProductName,PD.ProductDescription  FROM 
Product P
INNER JOIN ProductDescription PD ON P.ProductID=PD.ProductID
WHERE P.ProductID=@PID
 
END
```
```sql
EXEC GetProductDesc_withparameters 706
```
While executing the stored procedure we need to pass the input parameter. Please refer to the below image for the result set.

![](https://www.sqlshack.com/wp-content/uploads/2019/07/sql-server-stored-procedure-with-parameters.png)


## Creating a stored procedure with default parameters values

Following is the example of a stored procedure with default parameter values.

```sql
CREATE PROCEDURE GetProductDesc_withDefaultparameters
(@PID INT =706)
AS
BEGIN
SET NOCOUNT ON
 
SELECT P.ProductID,P.ProductName,PD.ProductDescription  FROM 
Product P
INNER JOIN ProductDescription PD ON P.ProductID=PD.ProductID
WHERE P.ProductID=@PID
 
END
```
When we execute the above procedure without passing the parameter value, the default value 706 will be used. But when executed passing the value, the default value will be ignored and the passed value will be considered as a parameter.

![](https://www.sqlshack.com/wp-content/uploads/2019/07/sql-server-stored-procedures-with-default-paramete.png)



## Creating a stored procedure with an output parameter
Below is the example of a stored procedure with an output parameter. The following example retrieves the EmpID which is an auto identity column when a new employee is inserted.

```sql
CREATE TABLE Employee (EmpID int identity(1,1),EmpName varchar(500))
```
```sql
CREATE PROCEDURE ins_NewEmp_with_outputparamaters
(@Ename varchar(50),
@EId int output)
AS
BEGIN
SET NOCOUNT ON
 
INSERT INTO Employee (EmpName) VALUES (@Ename)
 
SELECT @EId= SCOPE_IDENTITY()
 
END
```

Executing the stored procedures with output parameters is bit different. We must declare the variable to store the value returned by the output parameter.
```sql
declare @EmpID INT
 
EXEC ins_NewEmp_with_outputparamaters 'Andrew', @EmpID OUTPUT
 
SELECT @EmpID
```

![](https://www.sqlshack.com/wp-content/uploads/2019/07/sql-server-stored-procedures-with-default-paramete-1.png)

![](https://www.sqlshack.com/wp-content/uploads/2019/07/inserted-records-in-the-table.png)

## Creating an encrypted stored procedure
We can hide the source code in the stored procedure by creating the procedure with the “`ENCRYPTION`” option.

Following is the example of an encrypted stored procedure.

```sql
CREATE PROCEDURE GetEmployees
WITH ENCRYPTION
AS
BEGIN
SET NOCOUNT ON 
 
SELECT EmpID,EmpName from Employee
END
```

When we try to view the code of the SQL Server stored procedure using sp_helptext, it returns “`The text for object ‘GetEmployees’ is encrypted.`”
![](https://www.sqlshack.com/wp-content/uploads/2019/07/encrypted-sql-server-stored-procedures.png)

When you try to script the encrypted stored procedure from SQL Server management studio, it throws an error as below.

![](https://www.sqlshack.com/wp-content/uploads/2019/07/encrypted-sql-server-stored-procedures-1.png)

## Creating a temporary procedure
Like the temporary table, we can create temporary procedures as well. There are two types of temporary procedures, one is a local temporary stored procedure and another one is a global temporary procedure.

These procedures are created in the **tempdb database.**

### Local temporary SQL Server stored procedures:
These are created with `#` as prefix and can be accessed only in the session where it created. **This procedure is automatically dropped when the connection is closed.**

Following is the example of creating a local temporary procedure.
```sql
CREATE PROCEDURE #Temp
AS
BEGIN
PRINT 'Local temp procedure'
END
```

### Global temporary SQL Server stored procedure: 
These procedures are created with `##` as prefix and can be accessed on the other sessions as well. This procedure is automatically dropped when the connection which is used to create the procedure is closed.

Below is the example of creating a global temporary procedure.
```sql
CREATE PROCEDURE ##TEMP
AS
BEGIN
PRINT 'Global temp procedure'
END
```

## Modifying the stored procedure
Use the `ALTER PROCEDURE` statement to modify the existing stored procedure. Following is the example of modifying the existing procedure.
```sql
ALTER PROCEDURE GetProductDesc
AS
BEGIN
SET NOCOUNT ON
 
SELECT P.ProductID,P.ProductName,PD.ProductDescription  FROM 
Product P
INNER JOIN ProductDescription PD ON P.ProductID=PD.ProductID
 
END
```

## Renaming the stored procedure
To rename a stored procedure using T-SQL, use system stored procedure sp_rename. Following is the example that renames the procedure “GetProductDesc” to a new name “GetProductDesc_new”.
```sql
sp_rename 'GetProductDesc','GetProductDesc_new'
```
![alt text](https://www.sqlshack.com/wp-content/uploads/2019/07/renaming-a-sql-server-stored-procedure.png)


# SQL Server User-defined Functions

[read here](https://www.sqlservertutorial.net/sql-server-user-defined-functions/)

The SQL Server user-defined functions help you simplify your development by encapsulating complex business logic and make them available for reuse in every query.

- [User-defined scalar functions](https://www.sqlservertutorial.net/sql-server-user-defined-functions/sql-server-scalar-functions/) – cover the user-defined scalar functions that allow you to encapsulate complex formula or business logic and reuse them in every query.

- [Table variables](https://www.sqlservertutorial.net/sql-server-user-defined-functions/sql-server-table-variables/) – learn how to use table variables as a return value of user-defined functions.
- [Table-valued functions](https://www.sqlservertutorial.net/sql-server-user-defined-functions/sql-server-table-valued-functions/) – introduce you to inline table-valued function and multi-statement table-valued function to develop user-defined functions that return data of table types.
- [Removing user-defined functions](https://www.sqlservertutorial.net/sql-server-user-defined-functions/sql-server-drop-function/) – learn how to drop one or more existing user-defined functions from the database.

## SQL Server Scalar Functions
SQL Server scalar function **takes one or more parameters and returns a single value**.

The scalar functions help you simplify your code. For example, you may have a complex calculation that appears in many queries. Instead of including the formula in every query, you can create a scalar function that encapsulates the formula and uses it in each query.

### Creating a scalar function
To create a scalar function, you use the CREATE FUNCTION statement as follows:

```sql
CREATE FUNCTION [schema_name.]function_name (parameter_list)
RETURNS data_type AS
BEGIN
    statements
    RETURN value
END
```

In this syntax:

- First, specify the name of the function after the `CREATE FUNCTION` keywords. The schema name is optional. **If you don’t explicitly specify it, SQL Server uses `dbo` by default**.
- Second, specify a list of parameters surrounded by parentheses after the function name.
- Third, specify the data type of the return value in the `RETURNS` statement.
- Finally, include a `RETURN` statement to return a value inside the body of the function.

The following example creates a function that calculates the net sales based on the quantity, list price, and discount:
```sql
CREATE FUNCTION sales.udfNetSale(
    @quantity INT,
    @list_price DEC(10,2),
    @discount DEC(4,2)
)
RETURNS DEC(10,2)
AS 
BEGIN
    RETURN @quantity * @list_price * (1 - @discount);
END;
```

### Calling a scalar function
You call a scalar function like a built-in function. For example, the following statement demonstrates how to call the udfNetSale function:
```sql
SELECT 
    sales.udfNetSale(10,100,0.1) net_sale;
```
Here is the output:

![](https://www.sqlservertutorial.net/wp-content/uploads/SQL-Server-Scalar-Function-example.png)


The following example illustrates how to use the sales.udfNetSale function to get the net sales of the sales orders in the order_items table:
```sql
SELECT 
    order_id, 
    SUM(sales.udfNetSale(quantity, list_price, discount)) net_amount
FROM 
    sales.order_items
GROUP BY 
    order_id
ORDER BY
    net_amount DESC;
```
### Modifying a scalar function
To modify a scalar function, you use the `ALTER` instead of the `CREATE` keyword. The rest statements remain the same:
```sql
ALTER FUNCTION [schema_name.]function_name (parameter_list)
    RETURN data_type AS
    BEGIN
        statements
        RETURN value
    END
```
Note that you can use the `CREATE OR ALTER` statement to create a user-defined function if it does not exist or to modify an existing scalar function:
```sql
CREATE OR ALTER FUNCTION [schema_name.]function_name (parameter_list)
        RETURN data_type AS
        BEGIN
            statements
            RETURN value
        END
```
### Removing a scalar function
To remove an existing scalar function, you use the DROP FUNCTION statement:
```sql
DROP FUNCTION [schema_name.]function_name;
```
For example, to remove the sales.udfNetSale function, you use the following statement:
```sql
DROP FUNCTION sales.udfNetSale;
```

### SQL Server scalar function notes
The following are some key takeaway of the scalar functions:

- Scalar functions can be used almost anywhere in T-SQL statements.
- Scalar functions accept one or more parameters but return only one value, therefore, they must include a RETURN statement.
- Scalar functions can use logic such as IF blocks or WHILE loops.
- Scalar functions cannot update data. They can access data but this is not a good practice.
- Scalar functions can call other functions.

## SQL Server Table Variables
Table variables are kinds of variables that allow you to hold rows of data, which are similar to temporary tables.

### How to declare table variables
To declare a table variable, you use the `DECLARE` statement as follows:
```sql
DECLARE @table_variable_name TABLE (
    column_list
);
```
### The scope of table variables
Similar to local variables, table variables are **out of scope at the end of the batch**.

<span style="color:yellow">If you define a table variable in a stored procedure or user-defined function, the table variable will no longer exist after the stored procedure or user-defined function exits. </span>

### Table variable example
For example, the following statement declares a table variable named @product_table which consists of three columns: product_name, brand_id, and list_price:
```sql
DECLARE @product_table TABLE (
    product_name VARCHAR(MAX) NOT NULL,
    brand_id INT NOT NULL,
    list_price DEC(11,2) NOT NULL
);
```
### Inserting data into the table variables
Once declared, the table variable is empty. You can insert rows into the table variables using the `INSERT` statement:
```sql
INSERT INTO @product_table
SELECT
    product_name,
    brand_id,
    list_price
FROM
    production.products
WHERE
    category_id = 1;
```

### Querying data from the table variables
Similar to a temporary table, you can query data from the table variables using the `SELECT` statement:
```sql
SELECT
    *
FROM
    @product_table;
```

**Note** that you need to execute the whole batch or you will get an error:
```sql
DECLARE @product_table TABLE (
    product_name VARCHAR(MAX) NOT NULL,
    brand_id INT NOT NULL,
    list_price DEC(11,2) NOT NULL
);

INSERT INTO @product_table
SELECT
    product_name,
    brand_id,
    list_price
FROM
    production.products
WHERE
    category_id = 1;

SELECT
    *
FROM
    @product_table;
GO
```

### Restrictions on table variables
1. First, you have to **define the structure of the table variable during the declaration**. Unlike a regular or temporary table, **you cannot alter the structure of the table variables after they are declared**.

2. Second, statistics help the query optimizer to come up with a good query’s execution plan. Unfortunately, **table variables do not contain statistics. Therefore, you should use table variables to hold a small number of rows**.

3. Third, **you cannot use the table variable as an input or output parameter like other data types**. However, you can return a table variable from a user-defined function

4. Fourth, **you cannot create non-clustered indexes for table variables**. However, starting with SQL Server 2014, memory-optimized table variables are available with the introduction of the new In-Memory OLTP that allows you to add non-clustered indexes as part of table variable’s declaration.

5. Fifth, **if you are using a table variable with a join, you need to alias the table in order to execute the query**. For example:
```sql
SELECT
    brand_name,
    product_name,
    list_price
FROM
    brands b
INNER JOIN @product_table pt 
    ON p.brand_id = pt.brand_id;
```

### Performance of table variables
- Using table variables in a stored procedure results in fewer recompilations than using a temporary table.

- In addition, a table variable use fewer resources than a temporary table with less locking and logging overhead.

- Similar to the temporary table, the table variables do live in the tempdb database, not in the memory.

## SQL Server Table-valued Functions
A table-valued function is a user-defined function that **returns data of a table type**. The return type of a table-valued function is a table, therefore, you can use the table-valued function just like you would use a table.

### Creating a table-valued function
The following statement example creates a table-valued function that returns a list of products including product name, model year and the list price for a specific model year:
```sql
CREATE FUNCTION udfProductInYear (
    @model_year INT
)
RETURNS TABLE
AS
RETURN
    SELECT 
        product_name,
        model_year,
        list_price
    FROM
        production.products
    WHERE
        model_year = @model_year;
```
The syntax is similar to the one that creates a user-defined function.
### Executing a table-valued function
To execute a table-valued function, you use it in the FROM clause of the SELECT statement:
```sql
SELECT 
    * 
FROM 
    udfProductInYear(2017);
```

### Modifying a table-valued function
To modify a table-valued function, you use the `ALTER` instead of `CREATE` keyword. The rest of the script is the same.

For example, the following statement modifies the udfProductInYear by changing the existing parameter and adding one more parameter:
```sql
ALTER FUNCTION udfProductInYear (
    @start_year INT,
    @end_year INT
)
RETURNS TABLE
AS
RETURN
    SELECT 
        product_name,
        model_year,
        list_price
    FROM
        production.products
    WHERE
        model_year BETWEEN @start_year AND @end_year
```

### Multi-statement table-valued functions (MSTVF)
A multi-statement table-valued function or MSTVF is a table-valued function that **returns the result of multiple statements.**

The multi-statement-table-valued function is very useful because **you can execute multiple queries within the function and aggregate results into the returned table**.

To define a multi-statement table-valued function, you use a table variable as the return value. Inside the function, you execute one or more queries and insert data into this table variable.

The following udfContacts() function combines staffs and customers into a single contact list:
```sql
CREATE FUNCTION udfContacts()
    RETURNS @contacts TABLE (
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(255),
        phone VARCHAR(25),
        contact_type VARCHAR(20)
    )
AS
BEGIN
    INSERT INTO @contacts
    SELECT 
        first_name, 
        last_name, 
        email, 
        phone,
        'Staff'
    FROM
        sales.staffs;

    INSERT INTO @contacts
    SELECT 
        first_name, 
        last_name, 
        email, 
        phone,
        'Customer'
    FROM
        sales.customers;
    RETURN;
END;
```
The following statement illustrates how to execute a multi-statement table-valued function udfContacts:
```sql
SELECT 
    * 
FROM
    udfContacts();
```

### When to use table-valued functions
**We typically use table-valued functions as parameterized views**. In comparison with stored procedures, the table-valued functions are more flexible because we can use them wherever tables are used.

## SQL Server DROP FUNCTION

To remove an existing user-defined function created by the CREATE FUNCTION statement, you use the `DROP FUNCTION` statement as follows:
```sql
DROP FUNCTION [ IF EXISTS ] [ schema_name. ] function_name;
```

In this syntax:

- `IF EXISTS` : 
The `IF EXISTS` option a**llows you to drop the function only if it exists**. **Otherwise, the statement does nothing**. If you attempt to remove a non-existing function without specifying the IF EXISTS option, you will get an error.

- `schema_name` : 
The `schema_name` **specifies the name of the schema to which the user-defined function which you wish to remove belongs**. The schema name is optional.

- `function_name` :
The `function_name` is the name of the function that you want to remove.

**Notes**

- If the function that you want to remove is referenced by views or other functions created using the WITH `SCHEMABINDING` option, the `DROP FUNCTION` will fail.

- In addition, if there are constraints like `CHECK` or `DEFAULT` and computed columns that refer to the function, the `DROP FUNCTION` statement **will also fail**.

To drop multiple user-defined functions, you specify a comma-separated list of function names in after the `DROP FUNCTION` clause as follows:
```sql
DROP FUNCTION [IF EXISTS] 
    schema_name.function_name1, 
    schema_name.function_name2,
    ...;
```

### SQL Server DROP FUNCTION – a simple example
The following example creates a function that calculates discount amount from quantity, list price, and discount percentage:

```sql
CREATE FUNCTION sales.udf_get_discount_amount (
    @quantity INT,
    @list_price DEC(10,2),
    @discount DEC(4,2) 
)
RETURNS DEC(10,2) 
AS 
BEGIN
    RETURN @quantity * @list_price * @discount
END
```
To drop the sales.udf_get_discount_amount function, you use the following statement:
```sql
DROP FUNCTION IF EXISTS sales.udf_get_discount_amount;
```


### SQL Server DROP FUNCTION with SCHEMABINDING example
The following example recreates the function sales.udf_get_discount_amountusing the` WITH SCHEMABINDING` option:

```sql
CREATE FUNCTION sales.udf_get_discount_amount (
    @quantity INT,
    @list_price DEC(10,2),
    @discount DEC(4,2) 
)
RETURNS DEC(10,2) 
WITH SCHEMABINDING
AS 
BEGIN
    RETURN @quantity * @list_price * @discount
END
```

And the following statement creates a view that uses the sales.udf_get_discount_amount function:

```sql
CREATE VIEW sales.discounts
WITH SCHEMABINDING
AS
SELECT
    order_id,
    SUM(sales.udf_get_discount_amount(
        quantity,
        list_price,
        discount
    )) AS discount_amount
FROM
    sales.order_items i
GROUP BY
    order_id;
```


Now, if you try to remove the sales.udf_get_discount_amount function, you will get an error:
```sql
DROP FUNCTION sales.udf_get_discount_amount;
```
SQL Server returns the following **error**:
```sql
Cannot DROP FUNCTION 'sales.udf_get_discount_amount' because it is being referenced by object 'discounts'.
```


If you want to remove the function, you must drop the sales.discounts view first:
```sql
DROP VIEW sales.discounts;
```
And then drop the function;
```sql
DROP FUNCTION sales.udf_get_discount_amount;
```

# SQL Server Temporary Tables

[read here](https://www.sqlservertutorial.net/sql-server-basics/sql-server-temporary-tables/)

Temporary tables are tables that exist temporarily on the SQL Server.

The temporary tables are useful for storing the immediate result sets that are accessed multiple times.

## Creating temporary tables
SQL Server provided two ways to create temporary tables via `SELECT INTO` and `CREATE TABLE` statements.

### Create temporary tables using SELECT INTO statement
The first way to create a temporary table is to use the `SELECT INTO` statement as shown below:
```sql
SELECT 
    select_list
INTO 
    temporary_table
FROM 
    table_name
....
```

The name of the temporary table starts with a hash symbol (`#`). For example, the following statement creates a temporary table using the `SELECT INTO` statement:
```sql
SELECT
    product_name,
    list_price
INTO #trek_products --- temporary table
FROM
    production.products
WHERE
    brand_id = 9;
```

Once you execute the statement, you can find the temporary table name created in the system database named `tempdb`, which can be accessed via the *SQL Server Management Studio* using the following path `System Databases > tempdb > Temporary Tables` as shown in the following picture:


![](https://www.sqlservertutorial.net/wp-content/uploads/SQL-Server-Temporary-Tables-Example.png)
As you can see clearly from the picture, the **temporary table also consists of a sequence of numbers as a postfix**. **This is a unique identifier for the temporary table**. Because multiple database connections can create temporary tables with the same name, SQL Server automatically appends this unique number at the end of the temporary table name to differentiate between the temporary tables.

### Create temporary tables using CREATE TABLE statement
The second way to create a temporary table is to use the `CREATE TABLE` statement:
```sql
CREATE TABLE #haro_products (
    product_name VARCHAR(MAX),
    list_price DEC(10,2)
);
```
This statement has the same syntax as creating a regular table. However, the name of the temporary table starts with a hash symbol (`#`)

After creating the temporary table, you can insert data into this table as a regular table:
```sql
INSERT INTO #haro_products
SELECT
    product_name,
    list_price
FROM 
    production.products
WHERE
    brand_id = 2;
```
Of course, you can query data against it within the current session:
```sql
SELECT
    *
FROM
    #haro_products;
```

<span style="color:yellow">However, if you open another connection and try the query above query, you will get the following error</span>:
```sql
Invalid object name '#haro_products'.
```

**This is because the temporary tables are only accessible within the session that created them**.


## Global temporary tables
Sometimes, you may want to create a temporary table **that is accessible across connections**. In this case, you can use global temporary tables.

Unlike a temporary table, the name of a global temporary table starts with a double hash symbol (`##`).

The following statements first create a global temporary table named ##heller_products and then populate data from the production.products table into this table:
```sql
CREATE TABLE ##heller_products (
    product_name VARCHAR(MAX),
    list_price DEC(10,2)
);

INSERT INTO ##heller_products
SELECT
    product_name,
    list_price
FROM 
    production.products
WHERE
    brand_id = 3;
```

Now, you can access the ##heller_products table from any session.

## Dropping temporary tables

### Automatic removal
- **SQL Server drops a temporary table automatically when you close the connection that created it.**

- **SQL Server drops a global temporary table once the connection that created it closed and the queries against this table from other connections completes.**

### Manual Deletion
From the connection in which the temporary table created, you can manually remove the temporary table by using the `DROP TABLE` statement:
```sql
DROP TABLE ##table_name;
```

# Index in SQL Server

<iframe width="560" height="315" src="https://www.youtube.com/embed/i_FwqzYMUvk?si=GCa1rj0-svWPLSY_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
