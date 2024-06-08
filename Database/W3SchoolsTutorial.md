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

Best Practice Tips:

* Do not need upper case for SELECT and other commands
  * Even column data is not case sensitive
* Some DBS need semi colons at the end
* In SELECT, separate columns with comma

### SELECT

* `SELECT col1, col2 FROM tableName`
* SELECT DISTINCT gets all unique values
* SELECT COUNT = Returns the number
  * ```SELECT COUNT(DISTINCT Country) FROM Customers``` not supported for Microsoft access DBs
  * ```SELECT COUNT (*) FROM Customers``` Gets all customers from table

## SQL Database

## SQL References

## SQL Examples

## Look Up later

* Why upper case by default
* Pro Tips and Hacks with DB information