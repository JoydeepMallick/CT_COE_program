# SQL server basics

[read me](https://www.sqlservertutorial.net/sql-server-basics/)

# Constraints in SQL

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

# All inbuilt functions in SQL

🌟🌟🌟[Read here in detail](https://www.w3schools.com/sqL/sql_ref_sqlserver.asp)


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

## SQL Server String Functions

[read more](https://www.sqlservertutorial.net/sql-server-string-functions/)

<table>
<thead>
    <tr><th>Function</th><th>Description</th></tr>
</thead>
<tbody>
    <tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-ascii-function/">ASCII</a></td><td>Return the ASCII code value of a character</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-char-function/">CHAR</a></td><td>Convert an ASCII value to a character</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-charindex-function/">CHARINDEX</a></td><td>Search for a substring inside a string starting from a specified location and return the position of the substring.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-concat-function/">CONCAT</a></td><td>Join two or more strings into one string</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-concat_ws-function/">CONCAT_WS</a></td><td>Concatenate multiple strings with a separator into a single string</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-difference-function/">DIFFERENCE</a></td><td>Compare the SOUNDEX() values of two strings</td></tr><tr><td>FORMAT</td><td>Return a value formatted with the specified format and optional culture</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-left-function/">LEFT</a></td><td>Extract a given a number of characters from a character string starting from the left</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-len-function/">LEN</a></td><td>Return a number of characters of a character string</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-lower-function/">LOWER</a></td><td>Convert a string to lowercase</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-ltrim-function/">LTRIM</a></td><td>Return a new string from a specified string after removing all leading blanks</td></tr><tr><td>NCHAR</td><td>Return the Unicode character with the specified integer code, as defined by the Unicode standard</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-patindex-function/">PATINDEX</a></td><td>Returns the starting position of the first occurrence of a pattern in a string.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-quotename-function/">QUOTENAME</a></td><td>Returns a Unicode string with the delimiters added to make the input string a valid delimited identifier</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-replace-function/">REPLACE</a></td><td>Replace all occurrences of a substring, within a string, with another substring</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-replicate-function/">REPLICATE</a></td><td>Return a string repeated a specified number of times</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-reverse-function/">REVERSE</a></td><td>Return the reverse order of a character string</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-right-function/">RIGHT</a></td><td>Extract a given a number of characters from a character string starting from the right</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-rtrim-function/">RTRIM</a></td><td>Return a new string from a specified string after removing all trailing blanks</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-soundex-function/">SOUNDEX</a></td><td>Return a four-character (SOUNDEX) code of a string based on how it is spoken</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-space-function/">SPACE</a></td><td>Returns a string of repeated spaces.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-str-function/">STR</a></td><td>Returns character data converted from numeric data.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-string_agg-function/">STRING_AGG</a></td><td>Concatenate rows of strings with a specified separator into a new string</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-string_escape-function/">STRING_ESCAPE</a></td><td>Escapes special characters in a string and returns a new string with escaped characters</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-string_split-function/">STRING_SPLIT</a></td><td>A table-valued function that splits a string into rows of substrings based on a specified separator.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-stuff-function/">STUFF</a></td><td>Delete a part of a string and then insert another substring into the string starting at a specified position.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-substring-function/">SUBSTRING</a></td><td>Extract a substring within a string starting from a specified location with a specified length</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-translate-function/">TRANSLATE</a></td><td>Replace several single-characters, one-to-one translation in one operation.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-trim-function/">TRIM</a></td><td>Return a&nbsp;new string from a specified string after removing all leading and trailing blanks</td></tr><tr><td>UNICODE</td><td>Returns the integer value, as defined by the Unicode standard, of a character.</td></tr><tr><td><a href="https://www.sqlservertutorial.net/sql-server-string-functions/sql-server-upper-function/">UPPER</a></td><td>Convert a string to uppercase</td></tr>
</tbody>
</table>

## SQL math functions

<table class="ws-table-all notranslate">
<tbody><tr>
<th style="width:25%">Function</th>
<th>Description</th>
</tr>
<tr>
<td><a href="func_sqlserver_abs.asp">ABS</a></td>
<td>Returns the absolute value of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_acos.asp">ACOS</a></td>
<td>Returns the arc cosine of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_asin.asp">ASIN</a></td>
<td>Returns the arc sine of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_atan.asp">ATAN</a></td>
<td>Returns the arc tangent of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_atn2.asp">ATN2</a></td>
<td>Returns the arc tangent of two numbers</td>
</tr>
<tr>
<td><a href="func_sqlserver_avg.asp">AVG</a></td>
<td>Returns the average value of an expression</td>
</tr>
<tr>
<td><a href="func_sqlserver_ceiling.asp">CEILING</a></td>
<td>Returns the smallest integer value that is &gt;= a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_count.asp">COUNT</a></td>
<td>Returns the number of records returned by a select query</td>
</tr>
<tr>
<td><a href="func_sqlserver_cos.asp">COS</a></td>
<td>Returns the cosine of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_cot.asp">COT</a></td>
<td>Returns the cotangent of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_degrees.asp">DEGREES</a></td>
<td>Converts a value in radians to degrees</td>
</tr>
<tr>
<td><a href="func_sqlserver_exp.asp">EXP</a></td>
<td>Returns e raised to the power of a specified number</td>
</tr>
<tr>
<td><a href="func_sqlserver_floor.asp">FLOOR</a></td>
<td>Returns the largest integer value that is &lt;= to a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_log.asp">LOG</a></td>
<td>Returns the natural logarithm of a number, or the logarithm of a number to a 
specified base</td>
</tr>
<tr>
<td><a href="func_sqlserver_log10.asp">LOG10</a></td>
<td>Returns the natural logarithm of a number to base 10</td>
</tr>
<tr>
<td><a href="func_sqlserver_max.asp">MAX</a></td>
<td>Returns the maximum value in a set of values</td>
</tr>
<tr>
<td><a href="func_sqlserver_min.asp">MIN</a></td>
<td>Returns the minimum value in a set of values</td>
</tr>
<tr>
<td><a href="func_sqlserver_pi.asp">PI</a></td>
<td>Returns the value of PI</td>
</tr>
<tr>
<td><a href="func_sqlserver_power.asp">POWER</a></td>
<td>Returns the value of a number raised to the power of another number</td>
</tr>
<tr>
<td><a href="func_sqlserver_radians.asp">RADIANS</a></td>
<td>Converts a degree value into radians</td>
</tr>
<tr>
<td><a href="func_sqlserver_rand.asp">RAND</a></td>
<td>Returns a random number</td>
</tr>
<tr>
<td><a href="func_sqlserver_round.asp">ROUND</a></td>
<td>Rounds a number to a specified number of decimal places</td>
</tr>
<tr>
<td><a href="func_sqlserver_sign.asp">SIGN</a></td>
<td>Returns the sign of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_sin.asp">SIN</a></td>
<td>Returns the sine of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_sqrt.asp">SQRT</a></td>
<td>Returns the square root of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_square.asp">SQUARE</a></td>
<td>Returns the square of a number</td>
</tr>
<tr>
<td><a href="func_sqlserver_sum.asp">SUM</a></td>
<td>Calculates the sum of a set of values</td>
</tr>
<tr>
<td><a href="func_sqlserver_tan.asp">TAN</a></td>
<td>Returns the tangent of a number</td>
</tr>
</tbody></table>



# SQL server GROUP BY


⭐⭐⭐[Read more in detail](https://www.sqlservertutorial.net/sql-server-basics/sql-server-group-by/)

The GROUP BY clause allows you to arrange the rows of a query in groups. The groups are determined by the columns that you specify in the GROUP BY clause.

Syntax
```sql
SELECT
    select_list
FROM
    table_name
GROUP BY
    column_name1,
    column_name2 ,...;
```

Assume following table:-

<img src="https://www.sqlservertutorial.net/wp-content/uploads/SQL-Server-GROUP-BY-clause.png" width="400" height="300" />



the following query returns the number of orders placed by the customer by year:

```sql
SELECT
    customer_id,
    YEAR (order_date) order_year,
    COUNT (order_id) order_placed
FROM
    sales.orders
WHERE
    customer_id IN (1, 2)
GROUP BY
    customer_id,
    YEAR (order_date)
ORDER BY
    customer_id; 
```
Output:-

<img src="https://www.sqlservertutorial.net/wp-content/uploads/SQL-Server-GROUP-BY-clause-expression-example.png"  width="400" height="300">


## Group By rollup

⭐⭐⭐[read me](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver16#group-by-rollup) and [readme](https://www.sqltutorial.org/sql-rollup/)

**The ROLLUP is an extension of the GROUP BY clause.** 

Creates a group for each combination of column expressions. In addition, it "rolls up" the results into subtotals and grand totals. To do this, it moves from right to left decreasing the number of column expressions over which it creates groups and the aggregation(s).

The **column order affects the ROLLUP output** and can affect the number of rows in the result set.

For example, `GROUP BY ROLLUP (col1, col2, col3, col4)` creates groups for each combination of column expressions in the following lists.

- col1, col2, col3, col4
- col1, col2, col3, NULL
- col1, col2, NULL, NULL
- col1, NULL, NULL, NULL
- NULL, NULL, NULL, NULL --This is the grand total


```sql
-- Oracle, Microsoft SQL Server, and PostgreSQL syntax
SELECT 
    c1, c2, aggregate_function(c3)
FROM
    table
GROUP BY ROLLUP (c1, c2);


-- mysql syntax
SELECT 
    c1, c2, aggregate_function(c3)
FROM
    table_name
GROUP BY c1, c2 WITH ROLLUP;
```
example table:-
|Country	|Region	|Sales|
|-----------|-------|-----|
|Canada	|Alberta	|100|
|Canada	|British Columbia	|200|
|Canada	|British Columbia	|300|
|United States	|Montana	|100|

```sql
-- normal group by
SELECT Country, Region, SUM(sales) AS TotalSales
FROM Sales
GROUP BY Country, Region;
```
Output 

|Country|	Region|	TotalSales|
|-------|---------|-----------|
|Canada	|Alberta|	100|
Canada	|British Columbia|	500|
|United States	|Montana|	100|

```sql
-- group by with extension of roll up
SELECT Country, Region, SUM(Sales) AS TotalSales
FROM Sales
GROUP BY ROLLUP (Country, Region);
```
Output :-

|Country|	Region|	TotalSales|
|-------|---------|-----------|
|Canada	|Alberta	|100|
|Canada	|British Columbia|	500|
|Canada	|NULL	|600|
|United States	|Montana	|100|
|United States	|NULL	|100|
|NULL	|NULL	|700|

## Group by cube
[readme](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver16#group-by-cube--) and [readme](https://www.mssqltips.com/sqlservertip/6315/group-by-in-sql-server-with-cube-rollup-and-grouping-sets-examples/)

GROUP BY CUBE creates groups for **all possible combinations of columns**. For `GROUP BY CUBE (a, b)` the results has groups for unique values of
- (a, b)
- (NULL, b)
- (a, NULL)
- (NULL, NULL).

```sql
SELECT Country, Region, SUM(Sales) AS TotalSales
FROM Sales
GROUP BY CUBE (Country, Region);
```
Output :-
|Country|	Region|	TotalSales|
|-------|---------|-----------|
|Canada|	Alberta|	100|
|NULL|	Alberta|	100|
|Canada|	British Columbia|	500|
|NULL|	British Columbia|	500|
|United States|	Montana|	100|
|NULL|	Montana|	100|
|NULL|	NULL|	700|
|Canada|	NULL|	600|
|United States|	NULL|	100|

## Group by sets
[read](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-group-by-transact-sql?view=sql-server-ver16#group-by-grouping-sets--)

The GROUPING SETS option gives you the ability to combine multiple GROUP BY clauses into one GROUP BY clause. **The results are the equivalent of UNION ALL of the specified groups.**

For example, `GROUP BY ROLLUP (Country, Region)` and `GROUP BY GROUPING SETS ( ROLLUP (Country, Region) )` return the same results.

When GROUPING SETS has two or more elements, the results are a union of the elements. This example returns the union of the ROLLUP and CUBE results for Country and Region.

```sql
SELECT Country, Region, SUM(Sales) AS TotalSales
FROM Sales
GROUP BY GROUPING SETS ( ROLLUP (Country, Region), CUBE (Country, Region) );

-- this below query gives same result as above
SELECT Country, Region, SUM(Sales) AS TotalSales
FROM Sales
GROUP BY ROLLUP (Country, Region)
UNION ALL
SELECT Country, Region, SUM(Sales) AS TotalSales
FROM Sales
GROUP BY CUBE (Country, Region);
```
SQL does not consolidate duplicate groups generated for a GROUPING SETS list. For example, in `GROUP BY ( (), CUBE (Country, Region) )`, both elements return a row for the grand total and both rows will be listed in the results.


## GROUP BY ()
Specifies the empty group, which generates the grand total. This is useful as one of the elements of a GROUPING SET. 

For example, this statement gives the total sales for each country/region and then gives the grand-total for all countries/regions.

```sql
SELECT Country, SUM(Sales) AS TotalSales
FROM Sales
GROUP BY GROUPING SETS ( Country, () );
```


# JOINS in SQL

⭐⭐⭐[Read more](https://www.sqlshack.com/sql-join-overview-and-tutorial/)

A SQL Join is a special form of generating a meaningful data by combining multiple tables relate to each other using a “Key”.

The various SQL join types are as follows :-

1. SQL inner join
    - Equi join
    - Non-equi join (Theta join)
2. SQL outer join
    - SQL left join or left outer join
    - SQL right join or right outer join
    - SQL full join or full outer join
3. SQL cross join
4. SQL self join

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-249a.png)

**Note:** <span style="color:yellow">The keyword outer is optional.</span> It means you can specify the keyword “outer” or not makes no difference to the query execution.

## SQL inner join

The simplest and most common form of a join is the SQL inner join the default of the SQL join types used in most database management systems. It’s the **default SQL join** you get when you use the join keyword by itself.

The result of the SQL inner join includes rows from both the tables where the join conditions are met.

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-253a.png)

```sql
SELECT ColumnList from LeftTable L
INNER join  RightTable R
ON L.Column=R.Column
```

### EQUI join 
An equi join is the most common form of SQL inner join used in practice. If the join contains an equality operator e.g. =, then it’s an equi-join.

```sql
SELECT DISTINCT A.StateProvinceID,S.Name
FROM Person.Address A
inner join Person.StateProvince S
On A.StateProvinceID=S.StateProvinceID
```

### Theta join (Non-equi join)

In general, this a Theta join used to specify operators or conditions (the `ON` clause in SQL). In practice, this is a rarely used SQL join types. In most cases, the join will use a non-equality condition e.g. >

```sql
SELECT p1.FirstName, p2. FirstName             
FROM PErson.Person p1                                          
INNER join PErson.Person p2                                     
ON len(p1.FirstName) > len(p2.FirstName);
```

## SQL self join
A SQL Self join is a mechanism of joining a table to itself. You would use a self join when you wanted to create a result set joining records in the table with some other records from the same table.

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-259a.png)

```sql
SELECT e.ename, e.empno, m.ename as manager, e.mgr
FROM
    emp e, emp m
WHERE e.mgr = m.empno
```

## SQL cross join
A CROSS join returns all rows for all possible combinations of two tables. It generates all the rows from the left table which is then combined with all the rows from the right table. This type of join is also known as a Cartesian product(A*B).

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-261a.png)

```sql
SELECT e.BusinessEntityID, d.Name AS Department  
FROM HumanResources.Employee AS e  
CROSS join HumanResources.Department AS d
```

## SQL outer join
On joining tables with a SQL inner join, the output returns only matching rows from both the tables. When using a SQL outer join, not only it will list the matching rows, it will also list the unmatched rows from the other tables.

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-263a.png)

### SQL left outer join 

will return all the records from the left table in the join clause, regardless of matching records in the right table. The left SQL outer join includes rows where the condition is met plus all the rows from the table on the left where the condition is not met. Fields from the right table with no match will be displayed as null values.

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-264a.png)

Syntax:
```sql
SELECT ColumnList from LeftTable L
LEFT join  RightTable R
ON L.Column=R.Column
Where R.Column is NULL
```

### Right outer join 
will return all the records in the right table in the join clause, regardless of matching records in the left table. Using the right SQL outer join includes all the rows from the table on the right. The right SQL outer join is considered a special case and many databases don’t support right joins. Generally, a SQL right join can be rewritten as a SQL left join by simply changing the order of the tables in the query. In this instance, fields from the left table with no match will display null values

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-266a.png)

Syntax:
```sql
SELECT ColumnList from LeftTable L
RIGHT join  RightTable R
ON L.Column=R.Column
Where L.Column is NULL
```

### SQL outer join

will return all the rows in both tables. When rows don’t have a match in one of the tables, the field will display a null value. A full SQL outer join combines the effects of the SQL left joins and SQL right joins. Many databases do not support the implementation of full SQL outer joins

![](https://www.sqlshack.com/wp-content/uploads/2018/09/word-image-268a.png)

Syntax:
```sql
SELECT ColumnList from LeftTable L
FULL OUTER join  RightTable R
ON L.Column=R.Column
```

# Advanced JOINS in SQL

[Read here](https://visualizeright.com/2019/03/15/joins-and-advanced-joins/)

# Union and Union ALL

[read](https://www.sqlshack.com/sql-union-vs-union-all-in-sql-server/)

## SQL Union Operator Overview
 We use the SQL Union operator to combine two or more Select statement result set.

The syntax for the SQL Union operator
```sql
SELECT column1, Column2 ...Column (N) FROM tableA
UNION
SELECT column1, Column2 ...Column (N) FROM tableB;
```

We need to take care of following points to write a query with the SQL Union Operator.

- Both the Select statement must have the same number of columns
- Columns in both the Select statement must have compatible data types
- Column Order must also match in both the Select statement
- We can define Group By and Having clause with each Select statement. It is not possible to use them with the result set
- We cannot use Order By clause with individual Select statement. - We can use it with result set generated from the Union of both Select statements

Assume following example

```sql
-- Table A having values 1,2,3,4
CREATE TABLE TableA(
    ID INT
);
 Go
INSERT INTO TableA
VALUES(1),(2),(3),(4);

-- Table B having values 3,4,5,6
CREATE TABLE TableB(
    ID INT
);
 Go
INSERT INTO TableB
VALUES(3),(4),(5),(6);

-- If we use SQL Union operator between these two tables

SELECT ID
  FROM TableA
UNION
SELECT ID
  FROM TableB;
```
We get the following output.

<img src="https://www.sqlshack.com/wp-content/uploads/2019/04/sql-union-vs-union-all-sql-union-operator.png" height=230 width=900>

## SQL Union All Operator Overview
The SQL Union All operator combines the result of two or more Select statement similar to a SQL Union operator with a difference. **The only difference is that it does not remove any duplicate rows from the output of the Select statement.**

The syntax for SQL Union All operator
```sql
SELECT column1, Column2 ...Column (N) FROM tableA
Union All
SELECT column1, Column2 ...Column (N) FROM tableB;
```
Let us rerun the previous examples with SQL Union All operator.
```sql
SELECT ID
  FROM TableA
UNION All
SELECT ID
  FROM TableB;
```
<img src= "https://www.sqlshack.com/wp-content/uploads/2019/04/sql-union-all-operator.png">

**If the tables do not have any overlapping rows, SQL Union All output is similar to SQL Union operator.**

## SQL Union Vs Union All Operator
Union|Union All 
-----|---------
It combines the result set from multiple tables with eliminating the duplicate records | It combines the result set from multiple tables without eliminating the duplicate records
It performs a distinct on the result set. |It does not perform distinct on the result set
We need to specify Union operator|We need to specify Union All Operator
SQL Union All gives better performance in query execution in comparison to SQL Union|It gives better performance in comparison with SQL Union Operator

