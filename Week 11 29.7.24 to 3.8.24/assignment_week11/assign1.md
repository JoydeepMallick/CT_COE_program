# Assignment

Refer to the table CustomerDim Implement SCD Type-2 on the `CustomerDim table`. Initially it has got few records.

You need to create an insert trigger with the name `trg_dim` on the table `CustomerDim` that performs the necessary operation and maintains the data as maintained in SCD Type-2.

Initially Table Has the Following Records:

| CustomerID | CustomerName  | Address     | EffectiveStartDate | EffectiveEndDate | IsCurrent |
| ---------- | ------------- | ----------- | ------------------ | ---------------- | --------- |
| 1          | John Doe      | 123 Main St | 2023-01-01         | 9999-12-31       | 1         |
| 2          | Alice Johnson | 456 Elm St  | 2023-01-01         | 9999-12-31       | 1         |
| 3          | Bob Smith     | 789 Oak St  | 2023-01-01         | 9999-12-31       | 1         |

After Creating the Trigger, you have to insert the following records in the CustomerDim table:

| CustomerID | CustomerName  | Address |
| ---------- | ------------- | ------- |
| 1          | John Doe      | Ajmer   |
| 4          | David Richard | Mumbai  |
| 3          | Bob Smith     | Chennai |
| 5          | Eva Dsouza    | Mumbai  |

When the records are inserted, the value in the `EffectiveStartDate` column, `EffectiveEndDate` column and `IsCurrent` column should be updated accordingly.

The `EffectiveStartDate` column for the newly inserted records should have the current date.

You are required to update the `EffectiveEndDate` with one day before that of the new `EffectiveStartDate` for the historical records.

Refer the sample output given below:

**Sample Output**:

| CustomerID | CustomerName | Address     | EffectiveStartDate | EffectiveEndDate | IsCurrent |
| ---------- | ------------ | ----------- | ------------------ | ---------------- | --------- |
| 1          | John Doe     | 123 Main St | 2023-01-01         | 2023-09-10       | 0         |
| 1          | John Doe     | Ajmer       | 2023-09-11         | 9999-12-31       | 1         |

#### Please keep object names and column names exactly same as mentioned in the question.

# Solution

<span style="color:red">took help of chatGPT, unsure about SCD and not related to current week's learning</span>

To implement SCD Type-2 using an insert trigger in SQL:

### Step 1: Create the CustomerDim Table

First, create the table `CustomerDim` with the initial records.

```sql
CREATE TABLE CustomerDim (
    CustomerID INT,
    CustomerName VARCHAR(255),
    Address VARCHAR(255),
    EffectiveStartDate DATE,
    EffectiveEndDate DATE,
    IsCurrent BIT
);

INSERT INTO CustomerDim (CustomerID, CustomerName, Address, EffectiveStartDate, EffectiveEndDate, IsCurrent)
VALUES
(1, 'John Doe', '123 Main St', '2023-01-01', '9999-12-31', 1),
(2, 'Alice Johnson', '456 Elm St', '2023-01-01', '9999-12-31', 1),
(3, 'Bob Smith', '789 Oak St', '2023-01-01', '9999-12-31', 1);
```

### Step 2: Create the Insert Trigger

Create an insert trigger `trg_dim` on the `CustomerDim` table to handle the SCD Type-2 updates.

```sql
CREATE TRIGGER trg_dim
ON CustomerDim
INSTEAD OF INSERT
AS
BEGIN
    DECLARE @CurrentDate DATE = CAST(GETDATE() AS DATE);

    -- Loop through each inserted record
    DECLARE cur CURSOR FOR
    SELECT CustomerID, CustomerName, Address
    FROM inserted;

    DECLARE @CustomerID INT;
    DECLARE @CustomerName VARCHAR(255);
    DECLARE @Address VARCHAR(255);

    OPEN cur;
    FETCH NEXT FROM cur INTO @CustomerID, @CustomerName, @Address;

    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Check if the customer already exists and has a different address
        IF EXISTS (
            SELECT 1
            FROM CustomerDim
            WHERE CustomerID = @CustomerID AND Address <> @Address AND IsCurrent = 1
        )
        BEGIN
            -- Update the existing record's EffectiveEndDate and IsCurrent
            UPDATE CustomerDim
            SET EffectiveEndDate = DATEADD(DAY, -1, @CurrentDate),
                IsCurrent = 0
            WHERE CustomerID = @CustomerID AND IsCurrent = 1;

            -- Insert the new record with the current date as EffectiveStartDate
            INSERT INTO CustomerDim (CustomerID, CustomerName, Address, EffectiveStartDate, EffectiveEndDate, IsCurrent)
            VALUES (@CustomerID, @CustomerName, @Address, @CurrentDate, '9999-12-31', 1);
        END
        ELSE
        BEGIN
            -- Insert the new record if the customer does not exist or address is the same
            INSERT INTO CustomerDim (CustomerID, CustomerName, Address, EffectiveStartDate, EffectiveEndDate, IsCurrent)
            VALUES (@CustomerID, @CustomerName, @Address, @CurrentDate, '9999-12-31', 1);
        END

        FETCH NEXT FROM cur INTO @CustomerID, @CustomerName, @Address;
    END

    CLOSE cur;
    DEALLOCATE cur;
END;
```

### Step 3: Insert the New Records

Insert the new records into the `CustomerDim` table to test the trigger.

```sql
INSERT INTO CustomerDim (CustomerID, CustomerName, Address)
VALUES
(1, 'John Doe', 'Ajmer'),
(4, 'David Richard', 'Mumbai'),
(3, 'Bob Smith', 'Chennai'),
(5, 'Eva Dsouza', 'Mumbai');
```

### Step 4: Verify the Results

Check the `CustomerDim` table to ensure the records have been updated according to the SCD Type-2 logic.

```sql
SELECT * FROM CustomerDim ORDER BY CustomerID, EffectiveStartDate;
```

The output should look like this (assuming the current date is 2023-09-11):

```
CustomerID | CustomerName  | Address     | EffectiveStartDate | EffectiveEndDate | IsCurrent
-----------|---------------|-------------|--------------------|------------------|----------
1          | John Doe      | 123 Main St | 2023-01-01         | 2023-09-10       | 0
1          | John Doe      | Ajmer       | 2023-09-11         | 9999-12-31       | 1
2          | Alice Johnson | 456 Elm St  | 2023-01-01         | 9999-12-31       | 1
3          | Bob Smith     | 789 Oak St  | 2023-01-01         | 2023-09-10       | 0
3          | Bob Smith     | Chennai     | 2023-09-11         | 9999-12-31       | 1
4          | David Richard | Mumbai      | 2023-09-11         | 9999-12-31       | 1
5          | Eva Dsouza    | Mumbai      | 2023-09-11         | 9999-12-31       | 1
```


