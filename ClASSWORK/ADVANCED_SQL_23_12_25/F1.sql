CREATE DATABASE ADVANCED_SQL;
USE ADVANCED_SQL;

SET SQL_SAFE_UPDATES = 0; -- 0 MEANS OFF AND 1 MEANS ON

CREATE TABLE student_details (
    sid INT primary key AUTO_INCREMENT,
    sname VARCHAR(20),
    fees DECIMAL(7,2),
    course VARCHAR(20),
    education VARCHAR(10),
    address VARCHAR(20)
);

-- drop table student_details;

INSERT INTO student_details 
(sname,fees,course,education,address)
values
('Amit', 45000.00, 'Java', 'BSc', 'Ahmedabad'),
('Neha', 52000.50, 'Python', 'BCA', 'Surat'),
('Rahul', 60000.00, 'DataSci', 'BTech', 'Vadodara'),
('Priya', 48000.75, 'WebDev', 'BSc', 'Rajkot'),
('Karan', 55000.00, 'Java', 'MCA', 'Gandhinagar'),
('Anjali', 47000.00, 'Python', 'BSc', 'Bhavnagar'),
('Vikas', 62000.00, 'AI', 'BTech', 'Ahmedabad'),
('Pooja', 50000.00, 'ML', 'MSc', 'Surat'),
('Rohan', 53000.00, 'Java', 'BCA', 'Vadodara'),
('Sneha', 49000.00, 'WebDev', 'BSc', 'Rajkot'),
('Arjun', 65000.00, 'DataSci', 'MTech', 'Ahmedabad'),
('Nisha', 46000.00, 'Python', 'BSc', 'Surat'),
('Sahil', 58000.00, 'Java', 'BTech', 'Vadodara'),
('Kriti', 51000.00, 'ML', 'MCA', 'Rajkot'),
('Manoj', 54000.00, 'WebDev', 'BCA', 'Gandhinagar'),
('Isha', 49500.00, 'Python', 'BSc', 'Ahmedabad'),
('Dev', 61000.00, 'AI', 'BTech', 'Surat'),
('Mehul', 57000.00, 'Java', 'MSc', 'Vadodara'),
('Riya', 48500.00, 'WebDev', 'BCA', 'Rajkot'),
('Harsh', 63000.00, 'DataSci', 'MTech', 'Ahmedabad');

select * from student_details;

Delete from student_details where sid=2;
update student_details set sname = "Harsh", course = "Python", education="MTech" where sid = 18;

-- 26/12/25

-- View is a virtual table form of the original table
CREATE VIEW course_java as select * from student_details where course = "java";

select * from course_java;

select max(fees) from student_details;
select min(fees) from student_details;

select * from student_details order by SName DESC;

-- 30/12/25

CREATE table cust(
	cid int primary key AUTO_INCREMENT,
    cname varchar(20),
    cadd varchar(60),
    cmob int
);

create table product(
	pid int primary key AUTO_INCREMENT,
    pname varchar(50)
);

create table orders(
    oid int PRIMARY key AUTO_INCREMENT,
    odetail varchar(60),
    custid int,
    productid int,
    foreign key (custid) REFERENCES cust(cid),
    foreign key (productid) REFERENCES product(pid)
);

INSERT INTO cust (cname, cadd, cmob) VALUES
('Rahul Sharma', 'Ahmedabad', 987654321),
('Neha Patel', 'Vadodara', 912345678),
('Amit Verma', 'Surat', 998877665),
('Priya Singh', 'Rajkot', 909090909),
('Karan Mehta', 'Gandhinagar', 955566677);

INSERT INTO product (pname) VALUES
('Laptop'),
('Mobile Phone'),
('Headphones'),
('Smart Watch'),
('Keyboard');

INSERT INTO orders (odetail, custid, productid) VALUES
('Laptop purchase order', 1, 1),
('Mobile phone order', 2, 2),
('Headphones online order', 3, 3),
('Smart watch gift order', 4, 4),
('Keyboard office order', 5, 5);

SELECT * FROM CUST;
SELECT * FROM PRODUCT;


select cust.cname,cust.cadd,cust.cid,orders.productid,orders.oid from cust left join orders on cust.cid = orders.custid -- LEFT JOIN
union -- LEFT JOIN + RIGHT = FULL JOIN
select cust.cname,cust.cadd,cust.cid,orders.productid,orders.oid from cust right join orders on cust.cid = orders.custid; -- RIGHT JOIN

create index test on cust(cname);
show index from cust;

create unique index testing on cust(cname,cadd);
show index from cust;

-- 1/1/26

-- CROSS JOIN : table A * table B - ALL UNIQUE VALUES FROM TABLE A AND B

select c.cname, o.odetail from cust c 
cross join orders o;

CREATE TABLE product_details(
	product varchar(20),
    size varchar(10),
    color varchar(10)
);

-- 6/1/26
-- STRINGS
-- methods : upper, lower, length, concat, reverse, replace, trim, ltrim, rtrim, substring
select * from cust;
select caddress, upper(caddress) as upper_case from cust;
select caddress, lower(caddress) as lower_case from cust;
select caddress, length(caddress) as length from cust;
select concat(caddress," - ",cmobile) as concat_data from cust;
select caddress,reverse(caddress) as reverse_data from cust;
select caddress,replace(caddress,"CG Road","SG Highway") as replaced_data from cust;
select caddress,trim(caddress) as trimmed_data from cust;
select trim("   xyz    ");
select caddress,ltrim(caddress) as left_trimmed_data from cust;
select caddress,rtrim(caddress) as right_trimmed_data from cust;
select caddress,substring(caddress,1,4) as substring_data from cust; -- here the index starts from 1 and if we have written 4 then it will include 4th char unlike python where it is not included
select caddress,substring(caddress,4) as substring_data from cust;

-- 7/1/26

-- TRIGGER : Automatically executes before/after insert/update/delete as per we make it. SQL triggers are stored procedures that automatically execute in response to certain events in a specific table or view in a database.
create table sales (sid int primary key auto_increment, amount int);
create table message (msg varchar(20));

-- after - insert
DELIMITER $$
CREATE trigger sales_msg
after insert on sales
for each row
begin
	insert into message values ("message received");
end $$

insert into sales(amount) values (10000);
select * from sales;
select * from message;

-- after - update
DELIMITER $$
CREATE trigger sales_msg_update
after update on sales
for each row
begin
	insert into message values ("message updated");
end $$

update sales set amount = 11000 where sid = 1;
select * from sales;
select * from message;

-- after - delete
DELIMITER $$
CREATE trigger sales_msg_delete
after delete on sales
for each row
begin
	insert into message values ("message deleted");
end $$

delete from sales where sid = 1;
select * from sales;
select * from message;

show triggers;

-- 9/1/26

-- Date Function 
create table test (id int auto_increment, name varchar(20), visit_date Date, primary key (id));

insert into test (name, visit_date) values
('a','2025-12-12'),
('b','2025-11-13'),
('c','2025-10-14'),
('d','2025-9-15'),
('e','2025-8-16');

select date(now()); -- to print current date
select now(); -- to print current date and current time

select name, year(visit_date) as year, month(visit_date) as month, day(visit_date) as day from test; -- to print year,month and day in different columns.

-- 19/1/26

create table trans_roll_commit (acc_id INT auto_increment primary key,name varchar(20), balance int);
delete from trans_roll_commit;
insert into trans_roll_commit (name, balance) values ('A',1000),('B',2000),('C',25000);

select * from  trans_roll_commit;

START TRANSACTION;
update trans_roll_commit set balance = balance - 300 where acc_id = 5;

savepoint sp;
update trans_roll_commit set balance = balance - 200 where acc_id = 5;

savepoint sp1;
update trans_roll_commit set balance = balance - 2000 where acc_id = 5;

rollback to sp;
rollback to sp1;
 commit;

create table stud_marks(id int primary key, name varchar(20), sub varchar(10), marks int);
delete from stud_marks;
insert into stud_marks(id, name, sub, marks) values (1,'xyz','sci',50),(2,'xyz','sci',60),(3,'mnm','maths',40),(4,'mnm','maths',60),(5,'sss','ds',70),(6,'sss','ds',80);

select name, sum(marks) from stud_marks group by name having sum(marks) > 100;
select sub, avg(marks) from stud_marks group by sub having avg(marks) > 50;
select name, sum(marks) from stud_marks where marks > 40 group by name having sum(marks) > 100;

select name, sum(marks),
case
	when sum(marks) >= 150 then "A"
	when sum(marks) >= 110 then "B"
	else "fail"
end as grade
from stud_marks
group by name;

-- 23/1/26 
-- data inserted using python in vscode 
select * from stud_marks;

CREATE TABLE EMPS (id int auto_increment primary key,name varchar(5), dept varchar(10),salary int);

drop table emps;
insert into EMPS 
(name,salary,dept) 
values 
("A",20000,"HR"),
("B",30000,"IT"),
("C",40000,"SALES"),
("D",50000,"SALES"),
("E",60000,"SALES"),
("F",55000,"IT"),
("G",50000,"HR");

-- 16/4/26
-- Window Function 
select *,
rank() over(partition by dept order by salary desc) as mydept
from emps;

-- select dept, max(salary) from emps group by dept; 

select * from emps;

-- 22/4/26
select name,salary, rank() over (order by salary desc) as t from emps; -- if there are same values then the rank will be same and after that the number of values which were repeated will be skipped and next value will be given, eg, if there are two same values and the rank there was 3 then it will be 3 then 3 and then directly 5
select name,salary, dense_rank() over (order by salary desc) as t from emps; -- if there are same values then the rank will be same and after that the number of values which were repeated will not be skipped and next value will be given, eg, if there are two same values and the rank there was 3 then it will be 3 then 3 and then 4 unlike in rank where it becomes 5
select name,salary, row_number() over (order by salary desc) as t from emps; -- in this even if there are same values the number will be given unique only
select name,salary, row_number() over (partition by dept order by salary desc) as t from emps;