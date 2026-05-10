CREATE DATABASE ASSESSMENT;
USE ASSESSMENT;

CREATE TABLE country (
    id INT PRIMARY KEY,
    country_name VARCHAR(100),
    country_name_eng VARCHAR(100),
    country_code VARCHAR(10)
);

INSERT INTO country (id, country_name, country_name_eng, country_code) VALUES
(1, 'Deutschland', 'Germany', 'DEU'),
(2, 'Srbija', 'Serbia', 'SRB'),
(3, 'Hrvatska', 'Croatia', 'HRV'),
(4, 'United States of America', 'United States of America', 'USA'),
(5, 'Polska', 'Poland', 'POL'),
(6, 'Espana', 'Spain', 'ESP'),
(7, 'Rossiya', 'Russia', 'RUS');

CREATE TABLE city (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(50),
    lat DECIMAL(10,6),
    `long` DECIMAL(10,6),
    country_id INT,
    foreign key (country_id) references country(id)
);

INSERT INTO city (city_id, city_name, lat, `long`, country_id) VALUES
(1, 'Berlin', 52.520008, 13.404954, 1),
(2, 'Belgrade', 44.787197, 20.457273, 2),
(3, 'Zagreb', 45.815399, 15.966568, 3),
(4, 'New York', 40.730610, -73.935242, 4),
(5, 'Los Angeles', 34.052235, -118.243683, 4),
(6, 'Warsaw', 52.237049, 21.017532, 5);

CREATE TABLE customer (
    id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city_id INT,
    customer_address VARCHAR(100),
    next_call_date DATE,
    ts_inserted TIMESTAMP,
    foreign key (city_id) references city(city_id)
);

INSERT INTO customer (id, customer_name, city_id, customer_address, next_call_date, ts_inserted) VALUES
(1, 'Jewelry Store', 4, 'Long Street 120', '2020-01-21', '2020-01-09 14:01:20'),
(2, 'Bakery', 1, 'Kurfürstendamm 25', '2020-02-21', '2020-01-09 17:52:15'),
(3, 'Cafe', 1, 'Tauentzienstraße 44', '2020-01-21', '2020-01-10 08:02:49'),
(4, 'Restaurant', 3, 'Ulica lipa 15', '2020-01-21', '2020-01-10 09:20:21');

-- Task : 1 (join multiple tables using left join)
-- List all Countries and customers related to these countries. For each country displaying its name in English, the name of the city customer is located in as well as the name of the customer. Return even countries without related cities and customers. 
select country.country_name_eng, city.city_name, customer.customer_name from country
left join city on city.country_id = country.id
left join customer on customer.city_id = city.city_id;

-- Task : 2 (join multiple tables using both left and inner join)
-- Return the list of all countries that have pairs(exclude countries which are not referenced by any city). For such pairs return all customers.
-- Return even pairs of not having a single customer

select country.country_name_eng, city.city_name, customer.customer_name from country
inner join city on city.country_id = country.id
left join customer on customer.city_id = city.city_id;