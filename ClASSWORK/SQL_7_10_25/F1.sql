create database psp;
USE psp;

-- DDL - data defination language (create, alter, drop)
-- DML - data manipulation language (insert, update) 
-- DQL - data query language (select,update)
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

-- DQL - data query language (select,update)
update student_table set roll_no = 3 where student_name = "C";
delete from student_table where roll_no = 9;
select roll_no as "roll_num",student_name from student_table where roll_no > 3;
select * from student_table where roll_no >3 and age < 22;
select * from student_table where age between 19 and 22;

-- 18/11/2025
CREATE TABLE DEPARTMENT (
	dept_id decimal primary key,
    dept_name varchar(20));

create table employee_ (
	e_id int primary key auto_increment,
	ename varchar(20),
    city varchar(20),
    salary decimal(7,2),
    email varchar(20),
    dept_id decimal,
    foreign key (dept_id) references DEPARTMENT(dept_id));
    
insert into department 
values 
(1,"Production"),
(2,"HR"),
(3,"IT"),
(4,"networking");

INSERT INTO employee_ (ename, city, salary, email, dept_id)
VALUES
('Aarav', 'Ahmedabad', 52000.00, 'aarav@ex.com', 1),
('Riya', 'Mumbai', 61000.00, 'riya@ex.com', 2),
('Neel', 'Delhi', 45000.00, 'neel@ex.com', 3),
('Sanya', 'Bangalore', 75000.00, 'sanya@ex.com', 4),
('Arjun', 'Pune', 68000.00, 'arjun@ex.com', 1),
('Diya', 'Jaipur', 47000.00, 'diya@ex.com', 2),
('Karan', 'Surat', 54000.00, 'karan@ex.com', 3),
('Isha', 'Hyderabad', 72000.00, 'isha@ex.com', 4),
('Rohan', 'Kolkata', 39000.00, 'rohan@ex.com', 1),
('Mira', 'Chennai', 83000.00, 'mira@ex.com', 2),
('Vihan', 'Ahmedabad', 56000.00, 'vihan@ex.com', 3),
('Priya', 'Pune', 60000.00, 'priya@ex.com', 4),
('Dev', 'Delhi', 71000.00, 'dev@ex.com', 1),
('Harsh', 'Surat', 43000.00, 'harsh@ex.com', 2),
('Nidhi', 'Mumbai', 90000.00, 'nidhi@ex.com', 3),
('Tanvi', 'Indore', 48000.00, 'tanvi@ex.com', 4),
('Laksh', 'Noida', 65000.00, 'laksh@ex.com', 1),
('Anaya', 'Ahmedabad', 70000.00, 'anaya@ex.com', 2),
('Kabir', 'Bhopal', 51000.00, 'kabir@ex.com', 3),
('Shruti', 'Jaipur', 82000.00, 'shruti@ex.com', 4);
    
describe employee_;
select * from employee_;

SET SQL_SAFE_UPDATES = 1; -- 0 MEANS OFF AND 1 MEANS ON
update employee_ set salary = 30000 where e_id = 25;

-- 20/11/2025

-- Display employee name and city from employee table 
select ename, city from employee_;

-- Display employee name and city from employee table 
select ename as Employee_Name, city as "City of Employee" from employee_;

-- Fetch only those details of employees who got more than 20000 salary
select * from employee_ where salary > 70000;

-- Fetch only those details of employees who got more than 20000 salary and leaves in hyderabad
select * from employee_ where salary > 70000 and city = "hyderabad";

-- Fetch only those details of employees who got more than 20000 salary or leaves in hyderabad
select * from employee_ where salary > 70000 or city = "hyderabad";

-- Fetch only those details of employees who got more than 20000 salary and less than 70000 salary
select ename, city, salary from employee_ where salary between 20000 and 70000;

-- Fetch employees who live in surat and ahmedabad
select * from employee_ where city in ("surat","ahmedabad");

-- Fetch employees whose salary is 10000 and 20000 salary
select ename, salary from employee_ where salary in (52000,45000);

-- Display name of employees whose name starts with R
select * from employee_ where ename like "R%";
-- Note : We use meta characters ( % , _ ) when using like

-- Display name of employees whose name ends with A
select * from employee_ where ename like "%A";

-- Display name of employees whose name starts with R and ends with A
select * from employee_ where ename like "r%a";

-- Display name of employees whose name length is 5 (use  underscore char 5 times)
select * from employee_ where ename like "_____";

-- Display name of employees whose name length is 5 and second letter is A 
select * from employee_ where ename like "__n__";

-- Display name of employees whose name contains second last letter y 
select * from employee_ where ename like "%y_";