# SQL Crash Course

## Basics

[SQL Fundamentals](https://www.youtube.com/watch?v=3s0lFtUrhSQ)

* DBMS = Database management system (SQLite)
* Relational Database: data into tables(entity) of rows(record) and columns(attribute)
* CRUD Operations
  * Create = INSERT
  * Retrieve = SELECT
  * Update = Update
  * Delete = Delete
  * JOIN = Combine rows from 2 or more tables based on a related column:
    * INNER JOIN
    * LEFT JOIN
    * RIGHT JOIN
    * FULL JOIN
* Data Types = Int, VarChar, Date, and Boolean
* Constraints
  * PRIMARY KEY = ensures uniquness of columns value
  * FOREIGN KEY = maintains referential integrity between two tables
  * NOT NULL = ensure col has a value
  * UNIQUE = ensures unifwq values in a columns
* Indexes
  * Speed is everything for DB retrievals
* Aggregates
  * SUM
  * MIN/MAX
  * COUNT
  * AVG
* GROUP BY usually used with Aggregates to group data based on specific columns
  * Used with Sum or Count for summary results
* ORDER BY = sort in ascending or descending order
* Subquery
  * AKA Inner Query, or Nested Query. Query embedded in another query
  * Used as a filter or condition on a main query
  * Used with () in a query after WHERE
* Views
  * USed like a table
* Transactions
  * Operation treated as a single unit. All succeed, or all fail
  * ACID
    * Atomicity
    * Consistency
    * Isolation
    * Durability
* Normalization
  * Organize Data to eliminate redundancy and improve integrity.
  * Define relationships between tabless
* Stored Procedures
  * Improve Performance and Security
* Triggers
  * Database objects that automatically execute in response to specific events
  * For data consistency and integrity
  * OR REPLACE
  * BEFORE / AFTER/ INSTEAD OF
  * Events can trigger (Insert, Update, Delete)
  * Has Begin and End

Revisit: JOIN, Group By, ORDER BY, Views, Transactions, Subqueries, Triggers, Stored PRocedures, 

## Complex

https://www.youtube.com/watch?v=Vy8NRI24aXg

* Look at the question, what do you need? Queries, Sub queries, outer joints?
* Get code working
