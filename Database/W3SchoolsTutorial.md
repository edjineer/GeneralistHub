# SQL Tutorial Notes

(Link) [https://www.w3schools.com/sql/]
(Master Link to more Resources than I'll ever have time to use) [https://www.reddit.com/r/SQL/comments/ujql3d/what_are_the_best_resourcesways_to_learn_advanced/]

## SQL Tutorial

History Tidbits:

* SQL = Structured Query Language
* Original peoples = Donald Chamberlain, Raymond Boyce, Edgar Codd
* Original Company = IBM
* There is a version of the standard regularly released
* Well known data = Northwind sample DB

Infrastructure

* RDBMS = Relational Database Management System
  * Basis for SQL.
  * Uses tables to describe data
  * Tables have fields = columns
  * Rows = records
* Server Side Scripting Language like PHP or ASP
* HTML/CSS to style the data

Best Practice Syntax Tips:

* Do not need upper case for SELECT and other commands
  * Even column data is not case sensitive
* Some DBS need semi colons at the end
* In SELECT, separate columns with comma
* Use single quotes for text values, but do not use quotes for numbers
* If a value is null, then it cant work with < > =, but can use IS NULL or IS NOT NULL
* If you forget the WHERE in an UPDATE, it applies to all
* If using top, make sure syntax includes the * wildcard
* Dates are sandwiched with a # (#07/31/1996#)

## Common Commands

### SELECT

* `SELECT col1, col2 FROM tableName`
* SELECT DISTINCT gets all unique values
* SELECT COUNT = Returns the number
  * ```SELECT COUNT(DISTINCT Country) FROM Customers;``` not supported for Microsoft access DBs
  * ```SELECT COUNT (*) FROM Customers;``` Gets all customers from table
  * ```SELECT COUNT (*) AS DistinctCountries FROM (SELECT DISTINCT Country FROM Customers);``` Workaround

### WHERE

* A clause used for filtering records
* ```SELECT col,col FROM table_name WHERE condition(x='y', or x=4);```
* Can use =, >, <, <=, >=, <> is not equal, != is also not equal, BETWEEN, LIKE, IN:  to filter the search
  * ```SELECT * FROM Customers WHERE CustomerID IN (10, 20);``` IN is for when matches in a list
  * ```SELECT * FROM Customers WHERE CustomerId LIKE 's%';``` Starts with S
* Testing for NULL
  * If a value is null, then it cant work with < > =, but can use IS NULL or IS NOT NULL

### ORDER BY

Sorts results in ascending or descending order

* ```SELECT * FROM table ORDER BY col ASC|DESC```
  * ```SELECT * FROM Customers WHERE Country LIKE 'd%' ORDER BY Country ASC;```
* Can use multiple columns, but first one will order first

### AND and OR

* WHERE can contain many AND operators or OR operators
* Incorporate Parenthesis to ensure correct ordering
  * ```SELECT * FROM Customers WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');```

### NOT

* Can be around WHERE, or LIKE, BETWEEN, IN etc
* ```SELECT col FROM table WHERE NOT condition```

### INSERT INTO

* 2 Options
  * ```INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);``` For cols and values 
  * ```INSERT INTO table_name VALUES (value1, value2, value3, ...);```
  * Can also do multiple new records at once: INSERT INTO table_name (col, col, col) VALUES (val1, val2, val3), (val1a, val2a, val3a), etc;
* Any columns not specified will be marked as "null" in the new record

### UPDATE

* ```UPDATE tablename SET column=val, column=val WHERE condition```
* NOTE: If you omit the WHERE, then it happens EVERYWHERE

### DELETE

* ```DELETE FROM table WHERE condition```
* If you omit WHERE, then all records are deleted
* To delete a table, use ```DROP TABLE table;```

### TOP

* USed to specify a set number of records to return
* ```SELECT TOP 3 * FROM Customers;```
* Nice feature that's syntax/term varies across SQL implementations
* Can be used with percent too!
  * ```SELECT TOP 50 PERCENT * FROM  Customers;``` Make sure to include the *

## Aggregates

* Aggregates ignore nulls
* Usually used with GROUP BY

### MIN and MAX

* ```SELECT MIN(Price) FROM Products;```
  * ```SELECT * FROM Customers WHERE PostalCode=(SELECT MAX(PostalCode) FROM Customers);```
* Returns as a single value
* Can make it return with a description:
  * ```SELECT MIN(Price) AS SmallestPrice FROM Products;```
* Can use it with Group BY
  * ```SELECT MIN(Price) AS SmallestPrice, CategoryID FROM Products GROUP BY CategoryID;```

### COUNT

* ```SELECT COUNT(column_name) FROM table_name WHERE condition;```
* Ignore Dubplicates with DISTINCT

### AS

* Acts as an Alias for singly returned values
* ```SELECT COUNT(*) AS [Number of records] FROM Products;```

### SUM

* ```SELECT SUM(*) FROM table WHERE condition;```
* Can also add in an expression SELECT SUM (Quantity*10) FROM table

### AVG

* ```SELECT AVG(column_name) FROM table_name WHERE condition;```

### LIKE

* Pattern Matches 
* 2 Wildcards: % for zero one or multiple chars, or _ for one single character
* Can make contains: ```SELECT * FROM Customers WHERE CustomerName LIKE '%al%';```
* At least 3 chars in length: ```SELECT * FROM Customers WHERE CustomerName LIKE '___%'```
* If no wildcards, then string has to be exact result

### IN

* ```SELECT * FROM Customers WHERE Country IN ('Germany', 'France', 'UK');```

### BETWEEN

* ```SELECT * FROM Products WHERE Price BETWEEN 10 AND 20;```

## SQL Database

## SQL References

## SQL Examples

## Look Up later

* Why upper case by default
* Pro Tips and Hacks with DB information
* LIKE with WHERE: what can follow?
* How different flavors of SQL work, what about NoSQL from a high level? GraphQL?
* What if you want capitals to count in LIKE? By default they do not right now
