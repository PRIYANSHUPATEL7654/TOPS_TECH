USE ADVANCED_SQL;

CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments(dept_id)
);

CREATE TABLE Emp_Orders (
    order_id INT PRIMARY KEY,
    emp_id INT,
    amount INT,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
);

INSERT INTO Departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Sales');

INSERT INTO Employees VALUES
(101, 'Amit', 30000, 1),
(102, 'Neha', 40000, 2),
(103, 'Ravi', 35000, 2),
(104, 'Pooja', 25000, 3);

INSERT INTO Emp_Orders VALUES
(1, 101, 5000),
(2, 102, 8000),
(3, 102, 7000),
(4, 104, 4000);

-- Task 1: COUNT
-- Count total number of employees
Select count(*) from employees;

-- Task 2: SUM
-- Find total salary of all employees
select sum(salary) from employees;

-- Task 3: AVG
-- Find average salary of employees
select avg(salary) from employees;

-- Task 5: INNER JOIN
-- Show employee name with department name
select e.emp_name,d.dept_name from employees e inner join departments d on e.dept_id = d.dept_id;

-- Task 6: JOIN + SUM
-- Find total order amount handled by each employee
select e.emp_name, sum(eo.amount) from employees e left join emp_orders eo on e.emp_id = eo.emp_id group by e.emp_id;

-- Task 7: VIEW
-- Create a view showing employee name, department, and salary
create view emp_dept_salary as select e.emp_name, d.dept_name, e.salary from employees e,departments d where e.dept_id = d.dept_id;
select * from emp_dept_salary;

-- Task 8: PROCEDURE (Simple)
-- Create a procedure to show all employees
delimiter &&
create procedure employees_name()
begin
	select emp_name from employees;
end&&
call employees_name();

-- Task 9: PROCEDURE with PARAMETER
-- Procedure to get employees by department
delimiter &&
create procedure employees_name_by_dept(department_name varchar(10))
begin
	select e.emp_name from employees e, departments d where e.dept_id = d.dept_id and d.dept_name = department_name;
end&&

drop procedure employees_name_by_dept;

call employees_name_by_dept("IT");

-- Task 10: JOIN + AVG
-- Find average salary department-wise
select avg(e.salary),d.dept_name from employees e join departments d on d.dept_id = e.dept_id group by d.dept_id;