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
-- 5) Foreign key : reference to another table(if a table A has id and if another table B also has id then one id is primary key and another is made foreign key to connect both)
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

SET SQL_SAFE_UPDATES = 0; -- 0 MEANS OFF AND 1 MEANS ON
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
select ename, salary from employee_ where salary in (52000,22000);

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

-- 22/11/25

-- Display the records ascending to city 
select * from employee_ order by city,ename;

-- Dsiplay the recored decending wise ename 
select * from employee_ order by ename desc;

-- Display employee details with department name 

select employee_.dept_id,ename,city,email,dept_name from employee_,department  
where department.dept_id=employee_.dept_id;


-- Dsiplay maximum salary from employee master
select max(salary) from employee_;

-- Display Average and maxium of salary 
select avg(salary) as 'Average salary',max(salary) as 'maximum salary' from employee_;

-- Display how many employees 
select count(*) from employee_;

-- Left Join 
select ename,email,salary,employee_.dept_id from employee_ left join department on
employee_.dept_id=department.dept_id;

-- right join
select ename,email,salary,employee_.dept_id from employee_ right join department on
employee_.dept_id=department.dept_id;

-- Display sum of s	alary in each department 

select dept_name,sum(salary) from employee_, department where department.dept_id=employee_.dept_id
group by employee_.dept_id;

-- Find max salary in each department
select dept_name,max(salary) from employee_, department where department.dept_id=employee_.dept_id
group by employee_.dept_id;


update employee_ set salary=12000 where e_id= 25;

select * from employee_ ;

-- 25/11/25

-- having clause
-- fetch records whose dept have more than 2 emp
select dept_name, count(*) from employee_, department where department.dept_id = employee_.dept_id group by department.dept_id having count(*) <= 2;

-- sub queries
select ename,salary from employee_ where salary > (select avg(salary) from employee_) order by ename;

-- select ename,salary,dept_name from employee_,department where salary > (select avg(salary) from employee_ where department.dept_id = employee_.dept_id) group by department.dept_id;

-- 27/11/25

    
insert into department 
values 
(5,"higher networking");

-- fetch dept in which there is no employee
select dept_id,dept_name from department where dept_id not in (select dept_id from employee_);

-- fetch dept which has more than 2 employees
select d.dept_id,dept_name from department d,employee_ where 2 < (select count(*) from employee_ where d.dept_id = employee_.dept_id group by employee_.dept_id);

-- view
-- 29/11/25
select concat(ename," ",city) as name_city from employee_;

select upper(city) from employee_;

select replace(ename,"Aarav","aarush") from employee_;

select substring(ename,1,5) from employee_;

select * from student;
alter table student add birth_date date;

insert into student values(1,"PSP",111111,"p@gmail.com","2001-12-12"),
(2,"SSP",222222,"s@gmail.com","2002-10-13"),
(3,"DSP",112121,"d@gmail.com","2003-08-14");

select month(birth_date) from student;

insert into student values(4,"ASP",112221,"a@gmail.com",curdate());

select * from employee_;

select ceil(salary) from employee_;

select floor(salary) from employee_;

select power(salary,0.5) from employee_;

Delimiter $$
create function get_full_name(emp_name varchar(20), emp_surname varchar(20))
returns varchar(50)
deterministic
begin
	return concat(emp_name," ",emp_surname);
end$$

select get_full_name(ename,salary) as name_city from employee_;

-- 2/12/25

Delimiter &&
create function getTotalDeptSalary(deptid int) 
returns int
reads sql data
begin
	declare total_salary int;
    select sum(salary) into total_salary from employee_ where dept_id = deptid;
	return total_salary;
end&&

select getTotalDeptSalary(2);
select sum(salary) from employee_ group by dept_id;

Delimiter &&
create function calculateSalaryWithDA(salary1 decimal(7,2), incre decimal(4,2))
returns decimal(8,5)
deterministic
begin
	declare incre_salary decimal(8,5);
    set incre_salary = salary1 + (salary1 * incre);
    return incre_salary;
end&&

 drop function calculateSalaryWithDA;
    
select calculateSalaryWithDA(salary,0.5) from employee_;

select * from employee_
Delimiter &&
create procedure GetEmployeesByDepartment(d_name varchar(20))
begin
	select ename,city,salary from employee_, department where employee_.dept_id = department.dept_id and dept_name = d_name;
end&&
    
drop procedure GetEmployeesByDepartment;

call GetEmployeesByDepartment("Networking");

-- 4/12/25

Delimiter &&
create function calculateSalaryWithDAHRA(salary1 decimal(7,2), incre decimal(4,2),HRA decimal(4,2))
returns decimal(8,5)
deterministic
begin
	declare incre_salary decimal(8,5);
    set incre_salary = salary1 + (salary1 * incre) + (salary1 * HRA);
    return incre_salary;
end&&

 drop function calculateSalaryWithDAHRA;
    
select calculateSalaryWithDAHRA(salary,0.5,0.2) from employee_;

-- get total employees by department using procedure
delimiter &&
create procedure GetTotalEmpByDepartment(dept_name varchar(20), out total_emp int)
begin
	select count(e_id) into total_emp from employee_ e, department d 
	where e.dept_id = d.dept_id
	and d.dept_name = dept_name group by d.dept_id;
end&&

select * from employee_;
drop procedure GetTotalEmpByDepartment;

call GetTotalEmpByDepartment("IT", @total_employees);
select @total_employees;

-- insert values using procedure
delimiter &&
create procedure insertValues(dept_id int, dept_name varchar(20))
begin
	insert into department values (dept_id,dept_name);
end&&

select * from department;

call insertValues(11,"Products");

-- 6/12/25

-- TRIGGERS : SQL triggers are stored procedures that automatically execute in response to certain events in a specific table or view in a database
create table employee_backup(eid int, insert_date date)

delimiter &&
create trigger emp_insert_record
after insert 
on employee_
for each row
begin
	insert into employee_backup values (new.e_id,now());
end&&

select * from employee_;

insert into employee_ values ('Aarvi', 'Ahmedabad', 50000.20, 'aarvi@ex.com', 3);

create table employee_backup2 (ename varchar(20), city varchar(20), currentdate date);

delimiter &&
create trigger emp_delete_record
before delete
on employee_
for each row
begin
	insert into employee_backup2 values (old.ename, old.city, now());
end&&

select * from employee_backup2;

delete from employee_ where ename = "Riya";

delimiter &&
create trigger inserted
after insert
on employee_
for each row
begin
	insert into employee_backup3(message)
    values ("Inserted Successfully");
end&&

drop trigger inserted;

delimiter &&
create trigger deleted
after delete
on employee_
for each row
begin
	insert into employee_backup3(message)
    values ("Deleted Successfully");
end&&

drop trigger deleted;

create table employee_backup3 (message varchar(50), currentdate date);

insert into employee_ values (101,'Ravi', 'Ahmedabad', 60000.20, 'ravi@ex.com', 4);

delete from employee_ where ename = "Ravi";

select * from employee_backup3;

-- 9/12/25

-- if/else
select ename, salary, 
if(salary > 80000, "Good Salary", 
	if(salary > 50000,"Average Salary", "Low Salary")) 
from employee_;

-- if salary is greater than 50000 leave it as it is otherwise update the salary by adding 10000 in it.
-- update employee_ set salary = if(salary > 50000,salary,salary + 10000);