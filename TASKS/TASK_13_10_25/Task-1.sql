-- in psp database

create table dept(dept_id int primary key auto_increment, dept_name varchar(20));

create table emp(emp_id int primary key,emp_name varchar(20),salary decimal (6,2),dept_id int, foreign key (dept_id) references dept(dept_id));

alter table emp modify salary decimal (8,2);

insert into dept (dept_id, dept_name) values (101,"Human Resources");
insert into dept 
(dept_name)
values
("Finance"),
("Info Tech"),
("Marketing");

insert into emp
(emp_id, emp_name, salary, dept_id)
values
(1, "Aarav Mehta",100000.20,101),
(2,"Priya Sharma",200000.40,105),
(3,"Rohan Patel",205000.80,106),
(4,"Neha Singh",300000.40,107),
(5,"Karan Desai",400000.40,101),
(6,"Sneha Joshi",500000.40,105),
(7,"Vivek Nair",600000.40,106),
(8,"Aisha Shah",660000.40,107),
(9,"Rahul Verma",200000.40,101),
(10,"Ananya Iyer",200000.40,105),
(11,"Devansh Shah",204000.40,106),
(12,"Isha Trivedi",206000.40,107),
(13,"Manav Reddy",204000.00,101),
(14,"Kavya Patel",203000.40,105),
(15,"Arjun Malhotra",420000.40,106),
(16,"Meera Das",520000.00,107),
(17,"Nikhil Chatterjee",602000.40,101),
(18,"Tanya Kapoor",720000.80,105),
(19,"Aditya Ghosh",320000.90,106),
(20,"Simran Kaur",500000,107);

select * from dept;
select * from emp;