# Copy selective tables with selective columns from one database to another

We can issue below command **for each table we want to copy** from old database to new database :-

```sql
USE SourceDatabase; 
GO

SELECT * INTO DestinationDatabase.dbo.DestinationTable 
FROM SourceDatabase.dbo.SourceTable; 
GO
```

We also have a `Copy Database wizard` of SSMS for the same by selecting needed tables only.