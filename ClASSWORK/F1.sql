create database psp;
USE psp;

-- DDL - data defination language (create, alter, drop)
-- DML - data manipulation language (insert, update) 
-- DQL - data query language ()
-- DCL - data control language (grant, revoke)
CREATE TABLE STUDENT (stu_id int, stu_name varchar(20), mNo int);
alter table student add column email_id varchar(30);
-- alter table student modify email_id (40);
-- alter table student drop email_id;

describe student; -- to show table with all details
select * from student; -- to show all the values of the table

-- constraints (condition)
-- 1) Primary key : uniquely identified column (can only be one in the entire table)
-- 2) Unique key : same as primary key but can be more than one in the entire table
-- 3) Not null : must have some value
-- 4) Check : check the values (age<18)
-- 5) Foreign key : reference to another table(if a table A has id and if another table B also has id then)
-- 6) Default : sets a default value

create table department(dept_id int primary key auto_increment, dept_name varchar(20));

create table employee(emp_id int primary key,emp_name varchar(20),salary decimal (6,2),dept_id int, foreign key (dept_id) references department(dept_id));

DROP table department,employee;

create table student_table(roll_no int primary key auto_increment , student_name varchar(50) not null,age int check(age>18), contact_no int unique key, city varchar(50) default "Ahmedabad");

insert into student_table
(student_name, age, contact_no, city)
values
("G",22,213131314,"naranpura");

update student_table set roll_no = 3 where student_name = "C";

select * from student_table;