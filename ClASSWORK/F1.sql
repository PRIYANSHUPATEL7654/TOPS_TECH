create database psp;
USE psp;

-- DDL - data defination language (create, alter, drop)
-- DML - data manipulation language (insert, update) 
-- DQL - data query language ()
-- DCL - data control language (grant, revoke)
CREATE TABLE STUDENT (stu_id int, stu_name varchar(20), mNo int);
alter table student add column email_id varchar(30);
alter table student modify email_id (40);
alter table student drop email_id;