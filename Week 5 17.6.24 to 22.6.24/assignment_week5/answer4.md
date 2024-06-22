# Copy selective tables with selective columns from one database to another

# Copy all the tables from one database to another

First let import a sample database from Microsoft for testing:-

ref :- https://www.youtube.com/watch?v=Fc6pr2l9a-M&t=171s

File link :- https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms

#### I have used lightweight versions since they have less data and less volume to download

We can issue below command **for each table we want to copy** from old database to new database :-

```sql
USE SourceDatabase; 
GO

SELECT * INTO DestinationDatabase.dbo.DestinationTable 
FROM SourceDatabase.dbo.SourceTable; 
GO
```

We also have a `Copy Database wizard` of SSMS for the same.