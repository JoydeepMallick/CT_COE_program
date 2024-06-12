SET @index := -1; -- 0 BASED INDEXING

SELECT ROUND(AVG(LAT_N), 4)
FROM (
    SELECT @index:=@index + 1 AS IND, LAT_N 
    FROM STATION 
    ORDER BY LAT_N 
) AS INDEXLAT 
WHERE IND = ((SELECT COUNT(*) FROM STATION) / 2) 
   OR IND = (((SELECT COUNT(*) FROM STATION) - 1) / 2); -- 499/2 = 249 and 498/2 = 249 AND will work for even indices , -1 since we have 0 based indexing 


/* Improved version of above */
SET @index := 0; -- 1 BASED INDEXING

SELECT ROUND(AVG(LAT_N), 4)
FROM (
    SELECT @index:=@index + 1 AS IND, LAT_N 
    FROM STATION 
    ORDER BY LAT_N 
) AS INDEXLAT 
WHERE IND = ((SELECT COUNT(*) FROM STATION) / 2) 
   OR IND = (((SELECT COUNT(*) FROM STATION) + 1) / 2); -- this the real median formula which works for both odd and even elements because of a simple fact that division in sql returns just integer portion.

/* Further improved version of above where we smartly use index variable

i.e. after fill up of table INDEXLAT our final value of index will be the last index filled.

Hence no of rows in INDEXLAT = index(if 1 based indexing) or (index+1)(if 0 based indexing)

so avoid counting rows again

*/

SET @index := 0; -- 1 BASED INDEXING

SELECT ROUND(AVG(LAT_N), 4) FROM (
    SELECT @index:=@index + 1 AS IND, LAT_N 
    FROM STATION 
    ORDER BY LAT_N 
) AS INDEXLAT 
WHERE INDEXLAT.IND IN ( (@index)/ 2, (@index+1) /2  ); 
