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
CREATE TABLE customers (
    cust_id INT PRIMARY KEY,
    cust_name VARCHAR(50),
    city VARCHAR(50),
    email VARCHAR(100),
    join_date DATE
);

INSERT INTO customers (cust_id, cust_name, city, email, join_date) VALUES
(1, 'Aarav Shah', 'Mumbai', 'aarav@example.com', '2023-02-10'),
(2, 'Simran Kaur', 'Delhi', 'simran@example.com', '2023-03-14'),
(3, 'Suresh Gupta', 'Mumbai', 'suresh@example.com', '2024-01-05'),
(4, 'Priya Patel', 'Ahmedabad', 'priya@example.com', '2022-12-20'),
(5, 'Rahul Verma', 'Pune', 'rahul@example.com', '2024-08-10'),
(6, 'Sneha Reddy', 'Hyderabad', 'sneha@example.com', '2023-11-22'),
(7, 'Krish Nair', 'Kochi', 'krish@example.com', '2024-04-01'),
(8, 'Rohan Mehta', 'Surat', 'rohan@example.com', '2023-07-15'),
(9, 'Nisha Dubey', 'Indore', 'nisha@example.com', '2024-02-28'),
(10, 'Vikas Sharma', 'Jaipur', 'vikas@example.com', '2023-01-02');

CREATE TABLE products (
    prod_id INT PRIMARY KEY,
    prod_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock INT
);

INSERT INTO products (prod_id, prod_name, category, price, stock) VALUES
(101, 'Laptop', 'Electronics', 55000, 12),
(102, 'Headphones', 'Electronics', 1500, 40),
(103, 'Office Chair', 'Furniture', 7000, 5),
(104, 'Running Shoes', 'Footwear', 3500, 20),
(105, 'Smartphone', 'Electronics', 25000, 15),
(106, 'Backpack', 'Bags', 1200, 50),
(107, 'Keyboard', 'Electronics', 900, 30),
(108, 'Water Bottle', 'Kitchen', 300, 100),
(109, 'Bluetooth Speaker', 'Electronics', 2000, 7),
(110, 'Wrist Watch', 'Fashion', 3000, 0);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    cust_id INT,
    order_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (cust_id) REFERENCES customers(cust_id)
);

INSERT INTO orders (order_id, cust_id, order_date, status) VALUES
(2001, 1, '2024-08-05', 'Delivered'),
(2002, 1, '2024-06-11', 'Pending'),
(2003, 2, '2024-08-10', 'Cancelled'),
(2004, 3, '2024-01-15', 'Delivered'),
(2005, 4, '2024-03-22', 'Delivered'),
(2006, 5, '2024-08-30', 'Delivered'),
(2007, 6, '2024-04-09', 'Pending'),
(2008, 7, '2024-02-28', 'Cancelled'),
(2009, 8, '2024-05-18', 'Delivered'),
(2010, 9, '2024-07-07', 'Delivered');

SET SQL_SAFE_UPDATES = 0; -- 0 MEANS OFF AND 1 MEANS ON

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    prod_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (prod_id) REFERENCES products(prod_id)
);

INSERT INTO order_items (order_item_id, order_id, prod_id, quantity) VALUES
(1, 2001, 101, 1),     -- Laptop
(2, 2001, 102, 2),     -- Headphones
(3, 2002, 106, 1),     -- Backpack
(4, 2003, 103, 1),     -- Chair
(5, 2004, 101, 1),     -- Laptop
(6, 2005, 104, 2),     -- Shoes
(7, 2006, 109, 1),     -- Speaker
(8, 2006, 102, 1),     -- Headphones
(9, 2007, 108, 3),     -- Water bottle
(10, 2008, 107, 1),    -- Keyboard
(11, 2009, 102, 1),    -- Headphones
(12, 2010, 105, 1),    -- Smartphone
(13, 2010, 102, 3);    -- Headphones

-- 1) Show all customers who live in Mumbai. 
select cust_name, city from customers where city = "mumbai";

-- 2) Display names of all products in the “Electronics” category. 
select prod_name,category from products where category = "electronics";

-- 3) List all orders that were delivered. 
select order_id,status from orders where status = "delivered";

-- 4) Find customers who joined after January 2023.
select cust_name,join_date from customers where join_date > "2023-01-31";

-- 5) Display products whose price is greater than ₹10,000.
select prod_name, price from products where price > "10000";

-- 6) Show the total number of customers. 
select count(*) from customers;

-- 7) Display product names with their stock quantity
select prod_name, stock from products;
 
-- 8) List orders placed in August 2024.
select order_id,order_date from orders where order_date between "2024-08-01" and "2024-08-31";

-- 9) Show customers whose name starts with “S”. 
select cust_name from customers where cust_name like "s%";

-- 10) Display the cheapest product.
select prod_name,price from products where price = (select min(price) from products);

-- 11) Count how many orders each customer has placed.
select cust_name ,count(order_id) from customers,orders where customers.cust_id=orders.cust_id group by orders.cust_id;

-- 12) Find the total quantity of products ordered in each order.
select order_items.order_id,sum(order_items.quantity) from order_items group by order_items.order_id;
 
-- 13) Show each customer’s name and the total value of their delivered orders.
select c.cust_name, sum(p.price * oi.quantity) as total_value from customers c 
join orders o on o.cust_id = c.cust_id
join order_items oi on oi.order_id = o.order_id
join products p on p.prod_id = oi.prod_id
where o.status = "Delivered" group by c.cust_name; 

-- 14) Display the most expensive product in each category.
select prod_name, p.category, price from products p where price = (select max(price) from products where category = p.category);
 
-- 15) Find customers who have never placed an order.
select c.cust_id, cust_name from customers c where c.cust_id not in (select cust_id from orders);

-- 16) Show total sales (price × quantity) of each product. 
select p.prod_name, SUM(p.price * oi.quantity) as total_sales from products p,order_items oi where p.prod_id = oi.prod_id group by p.prod_id;

-- 17) List all products that have been ordered more than 2 times.
select prod_id,count(prod_id) from order_items group by prod_id having count(prod_id) > 2;

-- 18) Find the total revenue generated in 2024.
SELECT SUM(p.price * oi.quantity) AS total_revenue_2024
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON p.prod_id = oi.prod_id
WHERE YEAR(o.order_date) = 2024;

-- 19) Display all orders along with customer names and order status. 
SELECT o.order_id, c.cust_name, o.status
FROM orders o
JOIN customers c ON o.cust_id = c.cust_id;

-- 20) Show the number of “Delivered” vs “Cancelled” orders. 
SELECT status, COUNT(*) AS total_orders
FROM orders
GROUP BY status;

-- 21) Find the top 3 customers with the highest total spending.
SELECT c.cust_name, SUM(p.price * oi.quantity) AS total_spent
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.prod_id = p.prod_id
WHERE o.status = 'Delivered'
GROUP BY c.cust_name
ORDER BY total_spent DESC
LIMIT 3;

-- 22) Display the product categories ranked by total sales.
SELECT p.category, SUM(p.price * oi.quantity) AS total_sales
FROM products p
JOIN order_items oi ON p.prod_id = oi.prod_id
GROUP BY p.category
ORDER BY total_sales DESC;

-- 23) Find customers who have purchased both “Laptop” and “Headphones”.
SELECT c.cust_name
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
JOIN order_items oi ON o.order_id = oi.order_id
WHERE oi.prod_id IN (101, 102)
GROUP BY c.cust_name
HAVING COUNT(DISTINCT oi.prod_id) = 2;

-- 24) Show products that were never ordered.
SELECT p.prod_id, p.prod_name FROM products p LEFT JOIN order_items oi ON p.prod_id = oi.prod_id WHERE oi.prod_id IS NULL;

-- 25) Find orders with multiple products from different categories. 
SELECT o.order_id
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON p.prod_id = oi.prod_id
GROUP BY o.order_id
HAVING COUNT(DISTINCT p.category) > 1;

-- 26) Calculate each month’s total revenue and show a running total. 
SELECT
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    SUM(p.price * oi.quantity) AS monthly_revenue,
    SUM(SUM(p.price * oi.quantity)) OVER (ORDER BY DATE_FORMAT(o.order_date, '%Y-%m')) AS running_total
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY DATE_FORMAT(o.order_date, '%Y-%m');

-- 27) Display the average order value per customer. 
SELECT c.cust_name,
       AVG(order_total) AS avg_order_value
FROM (
    SELECT o.order_id, o.cust_id, SUM(p.price * oi.quantity) AS order_total
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.prod_id = p.prod_id
    GROUP BY o.order_id
) AS totals
JOIN customers c ON totals.cust_id = c.cust_id
GROUP BY c.cust_name;

-- 28) Show the most frequently ordered product. 
SELECT p.prod_name, COUNT(*) AS times_ordered
FROM order_items oi
JOIN products p ON oi.prod_id = p.prod_id
GROUP BY p.prod_name
ORDER BY times_ordered DESC
LIMIT 1;

-- 29) List customers who placed orders in at least 3 different months.
SELECT c.cust_name
FROM customers c
JOIN orders o ON c.cust_id = o.cust_id
GROUP BY c.cust_name
HAVING COUNT(DISTINCT MONTH(o.order_date)) >= 3;
 
-- 30) Find products that are out of stock or nearly out of stock (less than 10 units).
SELECT prod_name, stock
FROM products
WHERE stock < 10;
