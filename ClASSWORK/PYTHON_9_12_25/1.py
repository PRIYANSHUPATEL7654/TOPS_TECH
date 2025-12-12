# 9/12/25

# WAYS OF WRITING MULTIPLE PRINT STATEMENTS
# print("Hello World","Good Morning")
# #or
# print("statement1", end = " - ")
# print("Hello Everyone")
# #or
# print('statement2','- hello everyone and','good morning',sep=" * ")

# TAKING INPUT AND PRINTING THE INPUT
# name = input("Enter name : ")
# print(F"Your name is {name}")

# Addition of 2 numbers
# num1 = int(input("Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# # print("ADDITION OF",num1,"and",num2,"IS : ",num1+num2)
# # OR
# print(f"ADDITION OF {num1} and {num2} IS : ",num1+num2)

# Enter name, age, marks
# age = input("Enter your age : ")
# marks = input("Enter your marks : ")
# print(f"Name : {name}, Age : {age}, Marks : {marks}")

# 11/12/25

# percentage = float(input("enter percentage : "))
# print(percentage * 100)
# print(type(percentage))

# Operators : 
# 1) Arithmetic : +,-,*,/,//,** 
# 2) Relational : >, <, >=, <=, ==, !=
# 3) Logical :  and, or, not
# 4) Assignment : =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=
# 5) Membership : in, not in
# 6) Identity : is, is not
# 7) Bitwise : &, |, ^, ~, <<
# 8) Ternary : if....else

# 1) Arithmetic
# print(1+2)  # ADD
# print(4-2)  # SUBTRACT
# print(4*2)  # MULTIPLY
# print(2**4) # 2 POWER 4 (2 RAISE TO 4)
# print(5/2)  # DIVIDE
# print(5//2) # FLOOR VALUE OF DIVISION
# print(5%2)  # REMAINDER

a = 10
b = 3
# ADD = a + b
# SUB = a - b
# MUL = a * b
# DIV = a / b
# REM = a % b
# POWER = a ** b
# FLOOR = a // b
# print("ADDITION OF",a,"AND",b,"IS :",ADD)
# print("SUBTRACTION OF",a,"AND",b,"IS :",SUB)
# print("MULTIPLICATION OF",a,"AND",b,"IS :",MUL)
# print("DIVISION OF",a,"AND",b,"IS :",DIV)
# print("REMAINDER WHEN",a,"DIVIDE BY",b," IS :",REM)
# print(b,"TIMES",a,"IS :",POWER)
# print("FLOOR VALUE OF",a,"DIVIDE BY",b,"IS :",FLOOR)

# 2) Relational
print(f"{a} > {b} is ",a>b)
print(f"{a} < {b} is ",a<b)
print(f"{a} >= {b} is ",a>=b)
print(f"{a} <= {b} is ",a<=b)
print(f"{a} == {b} is ",a==b)
print(f"{a} != {b} is ",a!=b)