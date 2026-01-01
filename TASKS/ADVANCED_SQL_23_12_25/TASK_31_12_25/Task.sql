USE ADVANCED_SQL;

CREATE TABLE students ( 
student_id INT PRIMARY KEY, 
name VARCHAR(50), 
city VARCHAR(50), 
age INT 
); 
CREATE TABLE courses ( 
course_id INT PRIMARY KEY, 
course_name VARCHAR(50), 
fees INT 
); 
CREATE TABLE enrollments ( 
enroll_id INT PRIMARY KEY, 
student_id INT, 
course_id INT, 
enroll_date DATE, 
FOREIGN KEY (student_id) REFERENCES students(student_id), 
FOREIGN KEY (course_id) REFERENCES courses(course_id) 
); 

INSERT INTO students 
VALUES 
(1,'Rahul','Ahmedabad',21), 
(2,'Priya','Surat',22), 
(3,'Amit','Vadodara',20), 
(4,'Neha','Ahmedabad',23); 

INSERT INTO courses 
VALUES 
(101,'Java',15000), 
(102,'Python',12000), 
(103,'Web Development',10000); 

INSERT INTO enrollments 
VALUES 
(1,1,101,'2024-01-10'), 
(2,2,102,'2024-01-12'), 
(3,3,101,'2024-01-15'), 
(4,1,103,'2024-01-20'); 

-- Inner Join 
-- Display student name, course name, and enrollment date. 
select s.name,c.course_name,e.enroll_date from enrollments e 
join students s on e.student_id = s.student_id 
join courses c on e.course_id = c.course_id;

-- Left Join
-- Display all students with their enrolled course names. Show NULL if a student is not enrolled. 
select s.name,c.course_name from students s 
left join enrollments e on e.student_id = s.student_id 
left join courses c on e.course_id = c.course_id;

-- Right Join
-- Display all courses and students enrolled in them. 
select c.course_name,s.name from students s 
right join enrollments e on e.student_id = s.student_id 
right join courses c on e.course_id = c.course_id;

-- Join + Where
-- Display students who are enrolled in the Java course.
select c.course_name,s.name from students s 
right join enrollments e on e.student_id = s.student_id 
right join courses c on e.course_id = c.course_id where course_name = "Java";

-- View
-- Create a view named student_course_view that shows student name, city, course name, and fees.
create view student_course_view as select s.name,s.city,c.course_name,c.fees from students s 
join enrollments e on e.student_id = s.student_id 
join courses c on e.course_id = c.course_id;

select * from student_course_view;
-- drop view student_course_view;

-- Select from view
-- Fetch all records from student_course_view where city = 'Ahmedabad'.
select * from student_course_view where city = "Ahmedabad";

-- Update through view
-- Update city to 'Gandhinagar' for student Rahul using the view. 
SET SQL_SAFE_UPDATES = 0; -- 0 MEANS OFF AND 1 MEANS ON
update student_course_view set city = "Gandhinagar" where city = "Ahmedabad"and name = "Rahul";
select * from student_course_view;

-- Create index
-- Create an index on city column of students table. 
create index index_city on students(city);
show index from students;
drop index index_city on students;

-- Composite index
-- Create a composite index on student_id and course_id in enrollments table. 
create index index_student_course on enrollments(student_id,course_id);
show index from enrollments;

-- Performance check
-- Use EXPLAIN to analyze the query that fetches students from Ahmedabad. 
-- Concept : Index + Explain
explain select * from students where city = "Ahmedabad";