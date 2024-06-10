## SQL server basics

[read me](https://www.sqlservertutorial.net/sql-server-basics/)

## Constraints in SQL

<span style="color:red">**The syntax is of SQL server.**</span>

[Read me](https://www.sqlshack.com/commonly-used-sql-server-constraints-not-null-unique-primary-key/) and also[ read me](https://www.sqlshack.com/commonly-used-sql-server-constraints-foreign-key-check-default/)

Constraints in SQL Server are predefined rules and restrictions that are enforced in a single column or multiple columns, regarding the values allowed in the columns, to maintain the integrity, accuracy, and reliability of that column’s data.

Constraints in SQL Server are **predefined rules and restrictions that are enforced in a single column or multiple columns**, regarding the values allowed in the columns, to maintain the integrity, accuracy, and reliability of that column’s data.

There are six main constraints that are commonly used in SQL Server that we will describe deeply with examples within this article and the next one. These constraints are:

- SQL NOT NULL
- UNIQUE
- PRIMARY KEY
- FOREIGN KEY
- CHECK
- DEFAULT

### NOT NULL Constraint in SQL

By default, the columns are able to hold NULL values. A NOT NULL constraint in SQL is used to prevent inserting NULL values into the specified column, considering it as a not accepted value for that column

```sql
CREATE TABLE ConstraintDemo1
(
    ID INT NOT NULL,
    Name VARCHAR(50) NULL
)
```
Now trying something like 
```sql
 INSERT INTO ConstraintDemo1 ([NAME]) VALUES ('Fadi')
 ```
 will return error since default NULL not allowed in ID.

In order to convert a premade table with this constraint we can do 
```sql
ALTER TABLE ConstraintDemo1 ALTER COLUMN [Name] VARCHAR(50) NOT NULL
```

#### NOTE:
This will only work if the values already present in name are not null else error. to correct this do this :-

```sql
UPDATE ConstraintDemo1 SET [Name]='' WHERE [Name] IS NULL
/*You may update all values from null to required values*/
ALTER TABLE ConstraintDemo1 ALTER COLUMN [Name] VARCHAR(50) NOT NULL
```

### UNIQUE Constraints in SQL

The UNIQUE constraint in SQL is used to ensure that no duplicate values will be inserted into a specific column or combination of columns that are participating in the UNIQUE constraint and not part of the PRIMARY KEY.

```sql
CREATE TABLE ConstraintDemo2
(
     ID INT UNIQUE,
   Name VARCHAR(50) NULL
)
```

To add unique constraints to already created table
```sql
ALTER TABLE ConstraintDemo2 ADD CONSTRAINT UQ__Constrai UNIQUE (ID)
GO
```
To remove unique constraint from a table
```sql
ALTER TABLE ConstraintDemo2 DROP CONSTRAINT [UQ__Constrai__3214EC26B928E528]
```

In case of problems try to modify non unique i.e. repeated values

### SQL PRIMARY KEY Constraint

The PRIMARY KEY constraint consists of one column or multiple columns with values that uniquely identify each row in the table.

The SQL PRIMARY KEY constraint combines between the UNIQUE and SQL NOT NULL constraints, where the column or set of columns that are participating in the PRIMARY KEY cannot accept a NULL value.

```sql
CREATE TABLE ConstraintDemo3
(
     ID INT PRIMARY KEY,
   Name VARCHAR(50) NULL
)
```

to drop primary key
```sql
ALTER TABLE ConstraintDemo3
DROP CONSTRAINT PK__Constrai__3214EC27E0BEB1C4;
```

to add primary key
```sql
ALTER TABLE ConstraintDemo3
ADD PRIMARY KEY (ID);
```

### FOREIGN KEY Constraint

A Foreign Key is a database key that is used to link two tables together. The FOREIGN KEY constraint identifies the relationships between the database tables by referencing a column, or set of columns, in the Child table that contains the foreign key, to the PRIMARY KEY column or set of columns, in the Parent table.
```sql
CREATE TABLE ConstraintDemoParent
(
    ID INT PRIMARY KEY,
    Name VARCHAR(50) NULL
)

CREATE TABLE ConstraintDemoChild
(
    CID INT PRIMARY KEY,
	ID INT FOREIGN KEY REFERENCES ConstraintDemoParent(ID)
)
```

To drop constraint
```sql
ALTER TABLE ConstraintDemoChild
DROP CONSTRAINT  FK__ConstraintDe__ID__0B91BA14;
```

to add constraint
```sql
ALTER TABLE ConstraintDemoChild
ADD CONSTRAINT FK__ConstraintDe__ID
FOREIGN KEY (ID) REFERENCES ConstraintDemoParent(ID);
```

### CHECK Constraint

A CHECK constraint is defined on a column or set of columns to limit the range of values, that can be inserted into these columns, using a predefined condition.

Defining the CHECK constraint condition is somehow similar to writing the WHERE clause of a query, using the different comparison operators, such as AND, OR, BETWEEN, IN, LIKE and IS NULL to write its Boolean expression that will return TRUE, FALSE or UNKNOWN. The CHECK constraint will return UNKNOWN value when a NULL value is present in the condition. The CHECK constraint is used mainly to enforce the domain integrity by limiting the inserted values to the ones that follow the defined values, range or format rules.

```sql
CREATE TABLE ConstraintDemo4
(
     ID INT PRIMARY KEY,
	    Name VARCHAR(50) NULL,
	    Salary INT CHECK (Salary>0)
)
```

to drop constraint :-
```sql
ALTER TABLE ConstraintDemo4
DROP CONSTRAINT  CK__Constrain__Salar__0F624AF8;
```

to add constraint :-
```sql
ALTER TABLE ConstraintDemo4
ADD CONSTRAINT CK__Constrain__Salar
CHECK (Salary>0);
```

### DEFAULT Constraint

A DEFAULT constraint is used to provide a default column value for the inserted rows if no value is specified for that column in the INSERT statement. The Default constraint helps in maintaining the domain integrity by providing proper values for the column, in case the user does not provide a value for it. The default value can be a constant value, a system function value or NULL.

```sql
CREATE TABLE ConstraintDemo5
(
        ID INT PRIMARY KEY,
	    Name VARCHAR(50) NULL,
	    EmployeeDate DATETIME NOT NULL DEFAULT GETDATE()
)
```

to drop constraint :-
```sql
ALTER TABLE ConstraintDemo5
DROP CONSTRAINT  DF__Constrain__Emplo__1332DBDC;
```

to add constraint :-
```sql
ALTER TABLE ConstraintDemo5
Add Constraint DF__Constrain__Emplo  DEFAULT (GETDATE()) FOR EmployeeDate
```

# All concepts related to date time

[Read me](https://www.mssqltips.com/sqlservertip/5993/sql-server-date-and-time-functions-with-examples/)

## SQL Server `SYSDATETIME`, `SYSDATETIMEOFFSET` and `SYSUTCDATETIME` Functions

SQL Server High Precision Date and Time Functions have a scale of 7 and are:

- `SYSDATETIME` – returns the date and time of the machine the SQL Server is running on
- `SYSDATETIMEOFFSET` – returns the date and time of the machine the SQL Server is running on plus the offset from UTC
- `SYSUTCDATETIME` - returns the date and time of the machine the SQL Server is running on as UTC


| SQL Server T-SQL  Syntax |Date Function	| Result |
|-------------------------|----------|-------------|
| `SELECT SYSDATETIME() AS 'DateAndTime'; -- return datetime2(7)`	| DateAndTime|	2019-03-08 10:24:34.4377944 |
| `SELECT SYSDATETIMEOFFSET() AS 'DateAndTime+Offset'; -- datetimeoffset(7)` |	DateAndTime+Offset |	2019-03-08 10:24:34.4377944 -05:00|
| `SELECT SYSUTCDATETIME() AS 'DateAndTimeInUtc'; -- returns datetime2(7)`| DateAndTimeInUtc |	2019-03-08 15:24:34.4377944 |

### SQL Server `CURRENT_TIMESTAMP`, `GETDATE()` and `GETUTCDATE()` Functions

SQL Server Lesser Precision Data and Time Functions have a scale of 3 and are:

- `CURRENT_TIMESTAMP` - returns the date and time of the machine the SQL Server is running on
- `GETDATE()` - returns the date and time of the machine the SQL Server is running on
- `GETUTCDATE()` - returns the date and time of the machine the SQL Server is running on as UTC


| SQL Server T-SQL Syntax                      | Date Function       | Result                         |
|----------------------------------------------|---------------------|--------------------------------|
| `SELECT CURRENT_TIMESTAMP AS 'DateAndTime';` | DateAndTime         | 2019-03-08 10:28:23.643        |
| `SELECT GETDATE() AS 'DateAndTime';`         | DateAndTime         | 2019-03-08 10:28:23.643        |
| `SELECT GETUTCDATE() AS 'DateAndTimeUtc';`   | DateAndTimeUtc      | 2019-03-08 15:28:23.643        |


## SQL Server DATENAME Function
DATENAME – Returns a string corresponding to the datepart specified for the given date as shown in the following table

| SQL Server T-SQL Syntax                                                | Date Function | Result          |
|------------------------------------------------------------------------|---------------|-----------------|
| `SELECT DATENAME(YEAR, GETDATE()) AS 'Year';`                          | Year          | 2019            |
| `SELECT DATENAME(QUARTER, GETDATE()) AS 'Quarter';`                    | Quarter       | 1               |
| `SELECT DATENAME(MONTH, GETDATE()) AS 'Month';`                        | Month         | March           |
| `SELECT DATENAME(DAYOFYEAR, GETDATE()) AS 'DayOfYear';`                | DayOfYear     | 67              |
| `SELECT DATENAME(DAY, GETDATE()) AS 'Day';`                            | Day           | 8               |
| `SELECT DATENAME(WEEK, GETDATE()) AS 'Week';`                          | Week          | 10              |
| `SELECT DATENAME(WEEKDAY, GETDATE()) AS 'WeekDay';`                    | WeekDay       | Friday          |
| `SELECT DATENAME(HOUR, GETDATE()) AS 'Hour';`                          | Hour          | 11              |
| `SELECT DATENAME(MINUTE, GETDATE()) AS 'Minute';`                      | Minute        | 25              |
| `SELECT DATENAME(SECOND, GETDATE()) AS 'Second';`                      | Second        | 44              |
| `SELECT DATENAME(MILLISECOND, GETDATE()) AS 'MilliSecond';`            | MilliSecond   | 426             |
| `SELECT DATENAME(MICROSECOND, GETDATE()) AS 'MicroSecond';`            | MicroSecond   | 426666          |
| `SELECT DATENAME(NANOSECOND, GETDATE()) AS 'NanoSecond';`              | NanoSecond    | 426666666       |
| `SELECT DATENAME(ISO_WEEK, GETDATE()) AS 'Week';`                      | Week          | 10              |


## SQL Server DATEPART Function
`DATEPART` – returns an integer corresponding to the datepart specified
| SQL Server T-SQL Syntax                                           | Date Function | Result    |
|-------------------------------------------------------------------|---------------|-----------|
| `SELECT DATEPART(YEAR, GETDATE()) AS 'Year';`                     | Year          | 2019      |
| `SELECT DATEPART(QUARTER, GETDATE()) AS 'Quarter';`               | Quarter       | 1         |
| `SELECT DATEPART(MONTH, GETDATE()) AS 'Month';`                   | Month         | 3         |
| `SELECT DATEPART(DAYOFYEAR, GETDATE()) AS 'DayOfYear';`           | DayOfYear     | 67        |
| `SELECT DATEPART(DAY, GETDATE()) AS 'Day';`                       | Day           | 8         |
| `SELECT DATEPART(WEEK, GETDATE()) AS 'Week';`                     | Week          | 10        |
| `SELECT DATEPART(WEEKDAY, GETDATE()) AS 'WeekDay';`               | WeekDay       | 6         |
| `SELECT DATEPART(HOUR, GETDATE()) AS 'Hour';`                     | Hour          | 10        |
| `SELECT DATEPART(MINUTE, GETDATE()) AS 'Minute';`                 | Minute        | 36        |
| `SELECT DATEPART(SECOND, GETDATE()) AS 'Second';`                 | Second        | 14        |
| `SELECT DATEPART(MILLISECOND, GETDATE()) AS 'MilliSecond';`       | MilliSecond   | 43        |
| `SELECT DATEPART(MICROSECOND, GETDATE()) AS 'MicroSecond';`       | MicroSecond   | 43333     |
| `SELECT DATEPART(NANOSECOND, GETDATE()) AS 'NanoSecond';`         | NanoSecond    | 43333333  |
| `SELECT DATEPART(ISO_WEEK, GETDATE()) AS 'Week';`                 | Week          | 10        |


## SQL Server DAY, MONTH and YEAR Functions
- `DAY` – returns an integer corresponding to the day specified
- `MONTH`– returns an integer corresponding to the month specified
- `YEAR`– returns an integer corresponding to the year specified

| SQL Server T-SQL Syntax                          | Date Function | Result |
|--------------------------------------------------|---------------|--------|
| `SELECT DAY(GETDATE()) AS 'Day';`                | DAY           | 8      |
| `SELECT MONTH(GETDATE()) AS 'Month';`            | MONTH         | 3      |
| `SELECT YEAR(GETDATE()) AS 'Year';`              | YEAR          | 2019   |

## SQL Server DATEFROMPARTS, DATETIME2FROMPARTS, DATETIMEFROMPARTS, DATETIMEOFFSETFROMPARTS, SMALLDATETIMEFROMPARTS and  TIMEFROMPARTS Functions

- `DATEFROMPARTS` – returns a date from the date specified
- `DATETIME2FROMPARTS` – returns a datetime2 from part specified
- `DATETIMEFROMPARTS` – returns a datetime from part specified
- `DATETIMEOFFSETFROMPARTS` - returns a datetimeoffset from part specified
- `SMALLDATETIMEFROMPARTS` - returns a smalldatetime from part specified
- `TIMEFROMPARTS` - returns a time from part specified

| SQL Server T-SQL Syntax                                      | Date Function  | Result                   |
|--------------------------------------------------------------|----------------|--------------------------|
| `SELECT DATEFROMPARTS(2019,1,1) AS 'Date';`                  | Date           | 2019-01-01               |
| `SELECT DATETIME2FROMPARTS(2019,1,1,6,0,0,0,1) AS 'DateTime2';` | DateTime2      | 2019-01-01 06:00:00.0    |
| `SELECT DATETIMEFROMPARTS(2019,1,1,6,0,0,0) AS 'DateTime';`  | DateTime       | 2019-01-01 06:00:00.000  |
| `SELECT DATETIMEOFFSETFROMPARTS(2019,1,1,6,0,0,0,0,0,0) AS 'Offset';` | Offset         | 2019-01-01 06:00:00 +00:00 |
| `SELECT SMALLDATETIMEFROMPARTS(2019,1,1,6,0) AS 'SmallDateTime';` | SmallDateTime  | 2019-01-01 06:00:00      |
| `SELECT TIMEFROMPARTS(6,0,0,0,0) AS 'Time';`                 | Time           | 06:00:00                 |


## SQL Server DATEDIFF and DATEDIFF_BIG Functions

- `DATEDIFF` - returns the number of date or time datepart boundaries crossed between specified dates as an int
- `DATEDIFF_BIG` - returns the number of date or time datepart boundaries crossed between specified dates as a bigint

|SQL Server T-SQL Syntax|	Date Function|	Result|
|-----------------------|-------|-------|
|`SELECT DATEDIFF(DAY, 2019-31-01, 2019-01-01) AS 'DateDif'`|	DateDif|	30|
|`SELECT DATEDIFF_BIG(DAY, 2019-31-01, 2019-01-01) AS 'DateDifBig'`|	DateDifBig	|30|


## SQL Server DATEADD, EOMONTH, SWITCHOFFSET and TODATETIMEOFFSET Functions

- `DATEADD` - returns datepart with added interval as a datetime
- `EOMONTH` – returns last day of month of offset as type of start_date
- `SWITCHOFFSET` - returns date and time offset and time zone offset
- `TODATETIMEOFFSET` - returns date and time with time zone offset

| SQL Server T-SQL Syntax                                         | Date Function        | Result                               |
|-----------------------------------------------------------------|----------------------|--------------------------------------|
| `SELECT DATEADD(DAY,1,GETDATE()) AS 'DatePlus1';`               | DatePlus1            | 2019-03-09 10:38:21.710              |
| `SELECT EOMONTH(GETDATE(),1) AS 'LastDayOfNextMonth';`          | LastDayOfNextMonth   | 2019-04-30                           |
| `SELECT SWITCHOFFSET(GETDATE(), -6) AS 'NowMinus6';`            | NowMinus6            | 2019-03-08 12:40:22.540 -00:06       |
| `SELECT TODATETIMEOFFSET(GETDATE(), -2) AS 'Offset';`           | Offset               | 2019-03-08 12:46:22.540 -00:02       |


## SQL Server ISDATE Function to Validate Date and Time Values
ISDATE – returns int - Returns 1 if a valid datetime type and 0 if not


| SQL Server T-SQL Syntax |	Date Function |	Result |
|-------------------------|-------|-----|
| `SELECT ISDATE(GETDATE()) AS 'IsDate';`|	IsDate|	1|
|`SELECT ISDATE(NULL) AS 'IsDate';`|	IsDate|	0|

