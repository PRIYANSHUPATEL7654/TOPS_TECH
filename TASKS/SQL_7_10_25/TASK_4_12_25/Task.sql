USE PSP;

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

-- Get order count by customer name
delimiter &&
create procedure orderCountByCustName(IN customer_name varchar(20))
begin
	select c.cust_name, count(o.order_id) from customers c
    join orders o on c.cust_id = o.cust_id
    where c.cust_name = customer_name 
    group by c.cust_name;
end&&

drop procedure orderCountByCustName;

call orderCountByCustName("Aarav Shah");

-- Insert into customers and display result Successfully 
delimiter &&
create procedure insertCust()
begin
	INSERT INTO customers VALUES (11, 'Aarav Patel', 'Ahmedabad', 'aarav2@example.com', '2024-02-10');
    select "Customer Added Successfully" as message;
end&&

call insertCust;
select * from customers;