create database psp;
USE psp;

create table employee (name varchar(20), id int,age int, salary int, dept varchar(20), mNo int, address varchar(40));
alter table employee add column hire_date date;