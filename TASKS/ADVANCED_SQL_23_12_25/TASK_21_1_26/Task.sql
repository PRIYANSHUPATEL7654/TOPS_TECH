USE ADVANCED_SQL;

CREATE TABLE CUSTOMER_DATA(
	customer_id varchar(10), 
    gender varchar(10), 
    age int, 
    payment_method varchar(15));
    
CREATE TABLE SALES_DATA(
	invoice_no varchar(10) primary key, 
    customer_id varchar(20), 
    category varchar(20), 
    quantity int, 
    price decimal(6,2), 
    invoice_date varchar(12), 
    shopping_mall varchar(40), foreign key(customer_id) references customer_data(customer_id));

SELECT customer_id, COUNT(*)
FROM customer_data
GROUP BY customer_id
HAVING COUNT(*) > 1; -- to check if there is any duplicate value or not so that i can make the column as primary key

ALTER TABLE customer_data
ADD PRIMARY KEY (customer_id);

UPDATE sales_data
SET invoice_date =
CASE
    WHEN invoice_date LIKE '%/%'
        THEN STR_TO_DATE(invoice_date, '%d/%m/%Y')
    WHEN invoice_date LIKE '%-%'
        THEN STR_TO_DATE(invoice_date, '%d-%m-%Y')
END; -- To convert all dates in single format acceptable in date datatype

Alter table sales_data modify invoice_date date;

-- 1. Display all records from the sales table.
select * from sales_data;

-- 2. Show only invoice_no, customer_id, and price.
select invoice_no, customer_id, price from sales_data;

-- 3. Find all sales where the category is Clothing.
select * from sales_data where category = "Clothing";

-- 4. List all unique product categories.
select distinct(category) from sales_data;

-- 5. Show all distinct shopping malls.
select distinct(shopping_mall) from sales_data;

-- 6. Find sales where quantity is greater than 3.
select * from sales_data where quantity > 3;

-- 7. Display records where price is greater than 2000.
select * from sales_data where price > 2000.00;

-- 8. Show all sales made in Kanyon mall.
select * from sales_data where shopping_mall = "Kanyon mall";

-- 9. Count total number of invoices.
select count(invoice_no) from sales_data;

-- 10. Count total number of customers.
select count(*) from customer_data;

-- 11. Display sales ordered by price (highest first).
select * from sales_data order by price desc;

-- 12. Display sales ordered by invoice_date (latest first).
select * from sales_data order by invoice_date desc;

-- 13. Find the minimum price from sales.
select min(price) from sales_data;

-- 14. Find the maximum quantity sold in a single invoice.
select max(quantity) from sales_data;

-- 15. Find the average price of all sales.
select avg(price) from sales_data;

-- 16. Find total revenue (quantity × price).
select sum(quantity*price) as "Total Revenue" from sales_data;

-- 17. Find total quantity sold across all sales.
select sum(quantity) from sales_data;

-- 18. Find total revenue per category.
select category,sum(quantity*price) as "Total Revenue" from sales_data group by category;

-- 19. Find average price per category.
select category,avg(price) from sales_data group by category;

-- 20. Find total quantity sold per shopping mall.
select shopping_mall,count(quantity) from sales_data group by shopping_mall;

-- 21. Count number of invoices per category.
select category,count(invoice_no) from sales_data group by category;

-- 22. Count number of invoices per shopping mall.
select shopping_mall,count(invoice_no) from sales_data group by shopping_mall;

-- 23. Find minimum and maximum price per category.
select category,max(price), min(price) from sales_data group by category;

-- 24. Find average quantity per shopping mall.
select shopping_mall,avg(quantity) from sales_data group by shopping_mall;

-- 25. Find total revenue per shopping mall.
select shopping_mall,sum(quantity*price) as "Total Revenue" from sales_data group by shopping_mall;

-- 26. Show categories with total revenue greater than 500,000.
select category,sum(quantity*price) as "Total Revenue" from sales_data group by category having sum(quantity*price) > 500000;

-- 27. Show shopping malls with more than 5,000 invoices.
select shopping_mall, count(invoice_no) from sales_data group by shopping_mall having count(invoice_no) > 5000;

-- 28. Find categories where average price is greater than 1,000.
select category, avg(price) from sales_data group by category having avg(price) > 1000;

-- 29. Find malls where total quantity sold is greater than 20,000.
select shopping_mall, count(quantity) from sales_data group by shopping_mall having count(quantity) > 20000;

-- 30. Show customers who have more than 5 invoices.
select customer_id, count(invoice_id) from sales_data group by customer_id having count(invoice_id) > 5;

-- 31. Find categories with more than 10,000 total quantity sold.
select category, sum(quantity) from sales_data group by category having sum(quantity) > 10000;

-- 32. Show malls where average quantity per invoice is greater than 3.
select shopping_mall, avg(quantity) from sales_data group by shopping_mall having avg(quantity) > 3;

-- 33. Find customers whose total spending is greater than 10,000.
select customer_id, sum(quantity*price) from sales_data group by customer_id having sum(quantity*price) > 10000;

-- 34. Show categories with minimum price greater than 500.
select category, min(price) from sales_data group by category having min(price) > 500;

-- 35. Show malls where total revenue is less than 100,000.
select shopping_mall, sum(quantity*price) from sales_data group by shopping_mall having sum(quantity*price) < 100000;

-- 36. Show all sales made in the year 2021.
select * from sales_data where year(invoice_date) = "2021";

-- 37. Show all sales made in the year 2022.
select * from sales_data where year(invoice_date) = "2021";

-- 38. Find total revenue per year.
select sum(quantity*price), year(invoice_date) from sales_data group by year(invoice_date) order by year(invoice_date);

-- 39. Find total revenue per month.
select sum(quantity*price), month(invoice_date) from sales_data group by month(invoice_date) order by month(invoice_date);

-- 40. Find the month with highest total revenue.
select sum(quantity*price), month(invoice_date) from sales_data group by month(invoice_date) order by sum(quantity*price) desc limit 1;

-- 41. Count number of invoices per year.
select count(*),year(invoice_date) from sales_data group by year(invoice_date) order by year(invoice_date) asc;

-- 42. Show sales made between two given dates.
select * from sales_data where invoice_date between "2021-2-12" and "2021-3-14" order by invoice_date asc;

-- 43. Find the top 5 highest priced invoices.
select invoice_no, price from sales_data order by price desc limit 5;

-- 44. Find the top 3 categories by total revenue.
select category, sum(quantity*price) as "total revenue" from sales_data group by category order by "total revenue" desc limit 3;

-- 45. Find the shopping mall with highest total revenue.
select shopping_mall, sum(quantity*price) as "total revenue" from sales_data group by shopping_mall order by "total revenue" desc limit 1;

-- 46. Find the category with highest average price.
select category, avg(price) from sales_data group by category order by avg(price) desc limit 1;

-- 47. Find customers who purchased from more than one category.
select customer_id from sales_data group by customer_id having count(distinct category) > 1;

-- 48. Find customers who purchased from more than one shopping mall.
select customer_id from sales_data group by customer_id having count(distinct shopping_mall) > 1;

-- 49. Find the invoice with highest total amount (quantity × price).
select invoice_no,sum(quantity*price) from sales_data group by invoice_no order by sum(quantity*price) desc limit 1;

-- 50. Rank shopping malls based on total revenue (highest to lowest).
select shopping_mall, sum(quantity*price), rank() over (order by sum(quantity*price) desc) as "Rank" from sales_data group by shopping_mall;