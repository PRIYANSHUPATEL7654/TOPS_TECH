# 11/12/25

# Operators : 
# 1) Arithmetic : +,-,*,/,//,** 
# 2) Relational : >, <, >=, <=, ==, !=
# 3) Logical :  and, or, not
# 4) Assignment : =, +=, -=, *=, /=, //=, %=, **=, &=, |=, ^=
# 5) Membership : in, not in
# 6) Identity : is, is not
# 7) Bitwise : &, |, ^, ~, <<
# 8) Ternary : if..elif..else ...(including nested)

# 1) Arithmetic
print(1+2)  # ADD
print(4-2)  # SUBTRACT
print(4*2)  # MULTIPLY
print(2**4) # 2 POWER 4 (2 RAISE TO 4)
print(5/2)  # DIVIDE
print(5//2) # FLOOR VALUE OF DIVISION
print(5%2)  # REMAINDER

a = 10
b = 3
ADD = a + b
SUB = a - b
MUL = a * b
DIV = a / b
REM = a % b
POWER = a ** b
FLOOR = a // b
print("ADDITION OF",a,"AND",b,"IS :",ADD)
print("SUBTRACTION OF",a,"AND",b,"IS :",SUB)
print("MULTIPLICATION OF",a,"AND",b,"IS :",MUL)
print("DIVISION OF",a,"AND",b,"IS :",DIV)
print("REMAINDER WHEN",a,"DIVIDE BY",b," IS :",REM)
print(b,"TIMES",a,"IS :",POWER)
print("FLOOR VALUE OF",a,"DIVIDE BY",b,"IS :",FLOOR)

# 2) Relational
print(f"{a} > {b} is ",a>b)
print(f"{a} < {b} is ",a<b)
print(f"{a} >= {b} is ",a>=b)
print(f"{a} <= {b} is ",a<=b)
print(f"{a} == {b} is ",a==b)
print(f"{a} != {b} is ",a!=b)

# 3) Logical
print(f"{a>b and a>9}")
if(a>9 and b<3):
    print("And worked")
elif(a<10 or b>4):
    print("Or worked")
elif(not (a>9 and b<4)):
    print("Not worked")
else:
    print("Nothing worked")

# 4) Assignment
a += b
print(a)
a -= b
print(a)
a /= b
print(a)
a *= b
print(a)
a //= b
print(a)
a **= b
print(a)

# 5) Membership
cities = ["a","b","c"]
print("d" in cities)

name = "priyanshu"
print("an" in name)

tasks = ["cooking","mopping","cleaning"]
user = input("Enter task to be checked : ")
print(user in tasks)

# 16/12/25

# 6) Identity
# for int variables it stores in same memory so it will not work for it, but in list it stores in different memory therefore it will work for it.
c = a
d = 10
lst1 = [1,2,3]
lst2 = [1,2,3]
lst3 = lst1
print(id(lst1))
print(id(lst2))
print(id(lst3))
print(f"{lst1 is lst2} - {lst1 == lst2}")
print(f"{lst3 is lst1}")
print(id(a))
print(id(d))
print(f"{a is d} - {a == d}")
print(f"{c is a}") # or a is c both are same

# 8) Ternary
e = 10
if e > 0:
    print(f"{e} is positive")
elif e == 0:
    print(f"{e} is equal to 0")
else:
    print(f"{e} is negative")

age = 20
if age >= 0 and age <= 2:
    print("infant")
elif age > 2 and age <= 18:
    print("minor")
elif age > 18 and age <= 50:
    print("adult")
elif age > 50 and age <= 70:
    print("senior")
elif age > 70:
    print("super senior")
else:
    print(f"{age} is not valid age")

# Lab Task
num = int(input("Enter number : "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# 18/12/25

# nested if
age = int(input("Enter age : "))
weight = int(input("Enter weight : "))
if age >= 18 :
    if weight > 70 :
        print("You can donate blood")
    else:
        print("Weight is less than requirement")
else:
    print("You are under age")