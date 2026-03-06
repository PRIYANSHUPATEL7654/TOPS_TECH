# OOPS : Encapsulation, Inheritance, Polymorphism, Abstraction
# CLASSES & OBJECTS
# Class : It is a blue print, basically a structure but not an actual entity. It is a collection of object. Eg, person()
# Object : It is a real entity and a type of class. Eg, psp = person()
# init : It is like constructor in java. It is called automatically when an object is created.
# self : It refers to the current object.

# class Person:
#     # 1)
#     def __init__(self):
#         print("Inside init")

#     def greet(self,name):
#         print("Good morning",name)
    
#     # 2)
#     def __init__(self,name,age):
#         self.nam = name
#         self.ag = age

#     def greet(self):
#         print("Name :",self.nam)

#     def displayDetails(self):
#         print(self.nam,self.ag)

# obj1 = Person("PSP",22)
# obj1.greet()
# obj1.displayDetails()

# obj2 = Person("DSP",23)
# obj2.greet()
# obj2.displayDetails()

# obj3 = Person("SBP",24)
# obj4 = Person("JSPsss",25)
# obj5 = Person("MBP",26)
# lst_Person = [obj3,obj4,obj5]

# for i in lst_Person:
#     if len(i.nam)>5:
#         i.greet()
#         i.displayDetails()

# class Book:
#     def __init__(self,title,author,price,no_of_pg):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.no_of_pg = no_of_pg
    
#     def display(self):
#         print("TITLE :",self.title,"\nAUTHOR :",self.author,"\nPRICE :",self.price,"\nNO OF PAGES :",self.no_of_pg)

# b1 = Book("Rich Dad Poor Dad","Robert",1000,230)
# b1.display()

# b2 = Book("Rich Dad Poor Dad 2","Robert 2",1040,240)
# b3 = Book("Rich Dad Poor Dad 3","Robert 3",1050,250)
# lst_book = [b2,b3]
# for i in lst_book:
#     i.display()

# 14/2/26

# 1) ENCAPSULATION
# It means using data hiding to prevent security breach.

# class A:
#     def __init__(self,name,c_no):
#         self.name = name
#         self.__c_no = c_no # using double underscore(__) before variable name makes it private and it cannot be accessed outside the class
    
#     def display(self):
#         print(self.name,self.__c_no)

# a = A("PSP",123456)
# a.display()
# print(a.name)
# print(a.__c_no)

# class Bank:
#     def __init__(self,balance):
#         self.__balance = balance # private variable

#     def deposit(self,amount):
#         self.__balance += amount

#     def withdraw(self,with_amount):
#         if self.__balance < with_amount:
#             print("The withdraw amount is greater than the balance")
#         else:
#             self.__balance -= with_amount

#     def get_balance(self):
#         return self.__balance

# b1 = Bank(1000)
# print(b1.get_balance())
# b1.deposit(130)
# print(b1.get_balance())
# b1.withdraw(2500)
# print(b1.get_balance())

# 2) Inheritance

# Single Inheritance : A -> B
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name,self.age,end = " ")

# class Manager(Person):
#     def __init__(self, name, age,salary):
#         super().__init__(name, age)
#         self.salary = salary
    
#     def display(self):
#         super().display()
#         print(self.salary)

# e1 = Manager("ABC",22,22000)
# e1.display()

# Multilevel Inheritance : A -> B -> C
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name,self.age,end = " ")

# class Manager(Person):
#     def __init__(self, name, age, man_salary):
#         super().__init__(name, age)
#         self.man_salary = man_salary
    
#     def display(self):
#         super().display()
#         print(self.man_salary)

# class Employee(Manager):
#     def __init__(self, name, age, emp_salary):
#         super().__init__(name, age)
#         self.emp_salary = emp_salary
    
#     def display(self):
#         super().display()
#         print(self.emp_salary)

# e1 = Manager("ABC",22,22000)
# e1.display()
# e2 = Employee("Abc",23,10000)
# e2.display()

# Multiple Inheritance : A -> C, B -> C
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name,self.age,end = " ")

# class Manager:
#     def __init__(self, man_salary):
#         self.man_salary = man_salary
    
#     def display(self):
#         print(self.man_salary)

# class Employee(Person,Manager):
#     def __init__(self, name, age, man_salary, emp_salary):
#         super().__init__(name, age, man_salary)
#         self.emp_salary = emp_salary
    
#     def display(self):
#         super().display()
#         print(self.emp_salary)

# p1 = Person("ABC",22)
# p1.display()
# m1 = Manager(22000)
# m1.display()
# e2 = Employee("Abc",23,10000)
# e2.display()

# Heirarchical Inheritance : A -> B, A -> C
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(self.name,self.age,end = " ")

# class Manager(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
    
#     def display(self):
#         super().display()
#         print(self.salary)

# class Student(Person):
#     def __init__(self, name, age, marks):
#         super().__init__(name, age)
#         self.marks = marks
    
#     def display(self):
#         super().display()
#         print(self.marks)

# e1 = Manager("ABC",22,22000)
# e1.display()
# s1 = Student("ABC",22,50)
# s1.display()

# Hybrid Inheritance : Combination of any 2 or more inheritance from above 

# 3) Polymorphism : It is like Same name different work
# -> Types of polymorphism : 
# 1. Compile time : 1) Method overloading : It is not directly supported in python
#                   2) Operator overloading (operators like +,*)
# 2. Runtime :      1) Method overriding

# 1. Method overloading : It is not directly supported in python. But it can be achieved in following 3 ways :

# 1st way : Using Default Arguments (Simplest Way)

# In below code if b and c are not passed → default = 0
# So same method behaves differently
# class Calculator:

#     def add(self, a, b=0, c=0):
#         return a + b + c

# obj = Calculator()

# print(obj.add(5))         # 5
# print(obj.add(5, 10))     # 15
# print(obj.add(5, 10, 20)) # 35

# 2nd way : Using *args (Flexible Arguments)

# *args accepts any number of arguments.
# class Calculator:

#     def add(self, *args):
#         total = 0
#         for num in args:
#             total += num
#         return total

# obj = Calculator()

# print(obj.add(5))            # 5
# print(obj.add(5, 10))        # 15
# print(obj.add(1,2,3,4,5))    # 15

# 3rd way : Using Type Checking (Advanced Way)

# Behavior changes based on data type
# class Calculator:

#     def add(self, a, b):
#         if isinstance(a, str) and isinstance(b, str):
#             return a + b
#         elif isinstance(a, int) and isinstance(b, int):
#             return a + b
#         else:
#             return "Invalid types"

# obj = Calculator()

# print(obj.add(5,10))       # 15
# print(obj.add("Hi","Yo"))  # HiYo

# 2. Operator Overloading : In below example if i write p3 = p1+p2 then it will call __add__ method and if i write > instead of + then it will call __gt__ method . gt and add are special methods used in operator overloading.
# class point:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     # __str__ is a special method (also called a dunder method — double underscore method)
#     def __str__(self):
#         return f"{self.x} : {self.y}"

#     def __gt__(self,other):
#         if self.x > other.x:
#             return point(self.x,self.y)
#         else:
#             return point(other.x,other.y)

#     def __add__(self,other):
#         return point(self.x + other.x, self.y + other.y)


# p1 = point(12,14)
# p2 = point(1,31)
# p3 = point(2,23)

# # p3 = p1 > p2
# # after > sign in above line it automatically internally converts into p1.__gt__(p2)

# p4 = p1 + p2 + p3 # any number of object values can be added and it will give output correctly
# # after + sign in above line it automatically internally converts into p1.__add__(p2)

# print(p4)

# 3. Method Overriding : Same method name and same argument but in parent and child class.

# class car:
#     def speed(self):
#         print("Car")

# class sportscar(car):
#     def speed(self):
#         print("SportsCar")
    
# class sedan(car):
#     def speed(self):
#         print("SedanCar")

# obj1 = car()
# obj1.speed()
# obj2 = sportscar()
# obj2.speed()
# obj3 = sedan()
# obj3.speed()

# 4) Abstraction 
# Hiding implementation and showing only important details
# Abstract class : It has one or more abstract method. Its object cannot be created. Without abstract method, abstract class acts as normal class only.
# Abstract method : The abstract method of a class cannot be accessed by any class including child class. It only tells that method with same name should be made in the child class and ensures proper structure. A method an only be abstract if the class is abstract otherwise abstract method cannot be made.

from abc import ABC,abstractmethod
# class bank(ABC):
#     @abstractmethod
#     def calculateInterest(self):
#         pass
    
# class SBI(bank):
#     pass
#     # def calculateInterest(self):
#     #     return 0.5
    
# # class Axis(bank):
# #     def calculateInterest(self):
# #         return 1
    
# obj1 = bank() # any parent class with abstract method cannot have an object and creating one will always give error, and always call all other methods usingchild class object
# print(obj1.calculateInterest())
# obj2 = SBI()
# print(obj2.calculateInterest())
# obj3 = Axis()
# print(obj3.calculateInterest())

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class rectangle(shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
# class square(shape):
#     def __init__(self,length):
#         self.length = length
    
#     def area(self):
#         return self.length * self.length
    
# r = rectangle(5,3)
# print(r.area())
# r1 = square(15)
# print(r1.area())

# 24/2/26

# GENERATOR

# def my_generator():
#     for i in range(1,6):
#         yield i

# # Using the generator
# gen = my_generator()

# print(gen)
# for val in gen:
#     print(val)


# def my_generator():
#     for i in range(1,6):
#         print("in")
#         yield i

# # Using the generator
# gen = my_generator()

# print(gen)
# for val in gen:
#     print(val)

# def my_generator():
#     for i in range(1,6):
#         print("in")
#         yield i

# Using the generator
# gen = my_generator()

# print(gen)
# # for val in gen:
# #     print(val)

# print(gen.__next__())
# print(gen.__next__())
# print(gen.__next__())

# sq = (x = x*x for i in range (1,6))

# print(sq.__next__())
# print(sq.__next__())
# print(sq.__next__())
# for i in sq:
#     print(i)

# lst = [1,2,3,4,5]

# i = iter(lst)
# print(lst.__next__())
# print(lst.__next__())
# print(lst.__next__())
# print(lst.__next__())