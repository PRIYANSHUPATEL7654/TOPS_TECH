CREATE TABLE departments ( 
    dept_id INT PRIMARY KEY, 
    dept_name VARCHAR(50) 
); 
 
CREATE TABLE employees ( 
    emp_id INT PRIMARY KEY, 
    emp_name VARCHAR(50), 
    gender CHAR(1), 
    salary DECIMAL(10,2), 
    hire_date DATE, 
    dept_id INT, 
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id) 
); 
 
INSERT INTO departments VALUES 
(1, 'HR'), 
(2, 'Finance'), 
(3, 'Sales'), 
(4, 'IT'); 
 
INSERT INTO employees VALUES 
(101, 'Amit Sharma', 'M', 60000, '2021-03-12', 3), 
(102, 'Priya Singh', 'F', 75000, '2019-11-20', 2), 
(103, 'Ravi Patel', 'M', 55000, '2022-01-05', 3), 
(104, 'Neha Verma', 'F', 90000, '2018-07-15', 4), 
(105, 'Karan Mehta', 'M', 50000, '2023-04-10', 1), 
(106, 'Sneha Rao', 'F', 95000, '2020-05-25', 4); 

-- 1) Display all columns from the employees table
select * from employees;

-- 2) Show only employee names and their salaries
select emp_name,salary from employees;
 
-- 3) List all female employees
select emp_name from employees where gender = "F";
 
-- 4) Display the names of employees who work in the IT department
select emp_name from employees where dept_id = 4;
 
-- 5) Find employees whose salary is less than ₹60,000
-- List employees whose salary is between ₹55,000 and ₹90,000
select emp_name,salary from employees where salary < 60000;
select emp_name,salary from employees where salary between 55000 and 90000;
 
-- 6) Display all employees whose name starts with “N”
select emp_name from employees where emp_name like "N%";

-- 7) Show all employees whose name ends with “a”
select emp_name from employees where emp_name like "%A";

-- 8) Display employees who joined in the year 2023
select emp_name,hire_date from employees where hire_date like "2023%";

-- 9) List all male employees from the Sales department
select emp_name from employees where gender = "M" and dept_id = 3;

-- 10) Find all employees whose department ID is either 2 or 4
select emp_name from employees where dept_id = 2 or dept_id = 4;

-- 11) Show departments whose name starts with ‘S’
select dept_name from departments where dept_name like "S%";

-- 12) Count how many departments exist in the company 
select count(dept_name) from departments; 

-- 13) Sort departments alphabetically
select dept_name from departments order by dept_name asc;

-- 14) Show each employee’s name with their department name
select e.emp_name,d.dept_name from employees e join departments d on e.dept_id = d.dept_id;

-- 15) Display employee name, department name, and salary for all employees
select emp_name,dept_name,salary from employees e join departments d on e.dept_id = d.dept_id;

-- 16) Find the average salary of each department
select dept_name,avg(e.salary) from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name;

-- 17) Count total employees in each department
select count(emp_name),dept_name from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name;

-- OTHER TABLES
-- CREATE TABLE customers (
--     cust_id INT PRIMARY KEY,
--     cust_name VARCHAR(50),
--     city VARCHAR(50),
--     email VARCHAR(100),
--     join_date DATE
-- );

-- -- insert into 

-- CREATE TABLE products (
--     prod_id INT PRIMARY KEY,
--     prod_name VARCHAR(50),
--     category VARCHAR(30),
--     price DECIMAL(10,2),
--     stock INT
-- );

-- CREATE TABLE orders (
--     order_id INT PRIMARY KEY,
--     cust_id INT,
--     order_date DATE,
--     status VARCHAR(20),
--     FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
-- );

-- CREATE TABLE order_items (
--     order_item_id INT PRIMARY KEY,
--     order_id INT,
--     prod_id INT,
--     quantity INT,
--     FOREIGN KEY (order_id) REFERENCES orders(order_id),
--     FOREIGN KEY (prod_id) REFERENCES products(prod_id)
-- );

-- 1) Show all customers who live in Mumbai. 
-- 2) Display names of all products in the “Electronics” category. 
-- 3) List all orders that were delivered. 
-- 4) Find customers who joined after January 2023. 
-- 5) Display products whose price is greater than ₹10,000. 
-- 6) Show the total number of customers. 
-- 7) Display product names with their stock quantity. 
-- 8) List orders placed in August 2024. 
-- 9) Show customers whose name starts with “S”. 
-- 10) Display the cheapest product. 
-- 11) Count how many orders each customer has placed. 
-- 12) Find the total quantity of products ordered in each order. 
-- 13) Show each customer’s name and the total value of their delivered orders. 
-- 14) Display the most expensive product in each category. 
-- 15) Find customers who have never placed an order. 
-- 16) Show total sales (price × quantity) of each product. 
-- 17) List all products that have been ordered more than 2 times. 
-- 18) Find the total revenue generated in 2024. 
-- 19) Display all orders along with customer names and order status. 
-- 20) Show the number of “Delivered” vs “Cancelled” orders. 
-- 21) Find the top 3 customers with the highest total spending.
-- 22) Display the product categories ranked by total sales. 
-- 23) Find customers who have purchased both “Laptop” and “Headphones”. 
-- 24) Show products that were never ordered. 
-- 25) Find orders with multiple products from different categories. 
-- 26) Calculate each month’s total revenue and show a running total. 
-- 27) Display the average order value per customer. 
-- 28) Show the most frequently ordered product. 
-- 29) List customers who placed orders in at least 3 different months. 
-- 30) Find products that are out of stock or nearly out of stock (less than 10 units).