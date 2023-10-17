# This is a project on SQL BY ALX SE

SQL FILE TO BE TESTED
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

#TASK0
Write a script that lists all databases of your MySQL server.

#TASK1
Write a script that creates the database hbtn_0c_0 in your MySQL server.
If the database hbtn_0c_0 already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

#TASK2
Write a script that deletes the database hbtn_0c_0 in your MySQL server.
If the database hbtn_0c_0 doesn’t exist, your script should not fail
You are not allowed to use the SELECT or SHOW statements

#TASK3
Write a script that lists all the tables of a database in your MySQL server.
The database name will be passed as argument of mysql command (in the following example: mysql is the name of the database)

#TASK4
Write a script that creates a table called first_table in the current database in your MySQL server.
first_table description:
id INT
name VARCHAR(256)
The database name will be passed as an argument of the mysql command
If the table first_table already exists, your script should not fail
You are not allowed to use the SELECT or SHOW statements

#TASK5
Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
The database name will be passed as an argument of the mysql command
You are not allowed to use the DESCRIBE or EXPLAIN statements

#TASK6
Write a script that lists all rows of the table first_table from the database hbtn_0c_0 in your MySQL server.
All fields should be printed
The database name will be passed as an argument of the mysql command
