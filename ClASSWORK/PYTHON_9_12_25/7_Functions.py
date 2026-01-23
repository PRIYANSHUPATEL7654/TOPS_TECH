# 17/1/26

# Normal function
# def greet():
#     print("have a nice day")

# Function with parameter
# def greet1(name):
#     print(f"have a good day {name}")

# greet()
# greet1("Priyanshu")

# Addition of numbers
# def add(no1,no2):
#     return no1+no2

# ans = add(1,3)
# print("Addition is :",ans)

# Factorial of number
# def factorial(num):
#     fact = 1
#     for i in range (1,num+1):
#         fact = fact * i
    
#     print(fact)

# factorial(5)

# 20/1/26

# def power(no1):
#     print(no1**2)

# power(10)

# def isEven(no1):
#     # return no1%2 # this returns the remainder
#     return no1%2==0 # this returns true or false

# print(isEven(10))

# MENU DRIVEN PROGRAM

# 1. FACTORIAL
# 2. ODD/EVEN
# 3. PALINDROME
# 4. EXIT

def fact(num1):
    fact = 1
    for i in range (1,num1+1):
        fact = fact * i
    return fact

def odd_even(num1):
    if num1%2==0:
        return "even"
    else:
        return "odd"

# def palindrome(str):
#     # for i in str[::-1]:
#     #     str1 += i
#     #     # print(i)
#     if str == str[::-1]:
#         return "is Palindrome"
#     else:
#         return "is not palindrome"
    
# OR

# def palindrome(str):
#     str1=""
#     for i in str[::-1]:
#         str1 += i
#     if str1 == str:
#         return "is Palindrome"
#     else:
#         return "is not palindrome"
    
# OR

def palindrome(str):
    
    for i in range (len(str)-1):
        length = len(str)-1
        if str[i] == str[length-i]:
            continue
        else:
            return "is not palindrome"
    return "is Palindrome"
   

# while True:
#     choice = int(input("1. FACTORIAL\n2. ODD/EVEN\n3. PALINDROME\n4. EXIT\nEnter your choice from above options : "))

#     match choice:
#         case 1:
#             num1 = int(input("Enter a number : "))
#             print(fact(num1))
#         case 2:
#             num1 = int(input("Enter number 1 : "))
#             print(odd_even(num1))
#         case 3:
#             str = input("Enter a string : ")
#             print(palindrome(str))
#         case 4: break
#         case _ :
#             print("Invalid choice")


# Parameters in functions : If we do not give value of parameter mentioned in function then default parameter value will be used. Default parameter should always be at last.

# def greet(msg="Have a nice day"): 
#     print(msg)

# greet("Have a good day")
# greet()

def stud_info(name, address = "Paldi",name1 = "PSP",age = 20):
    print(name,address,name1,age)

stud_info("a","Naranpura",19)
stud_info("a","Naranpura")
stud_info("a","abc")
stud_info("psp",name1 = "ads",age = 21) # If we do not want to give from any of the middle default parameter then we need to give other values during function call with a parameter(variable) name 

# *args : It is a variable argument in which if we do not know the number of arguments then we use this. It is in a tuple form.

def info(*args):
    print(args)

info("a")
info("a","b",10)
info("a","b",10,20)

# *kwargs : It is also a variable argument but it gives values in dictionary form.
# Eg : if we pass name = "A" then name will be key and "a" will be value.

def info1(**kwargs):
    print(kwargs)


info1(name = "ABC", age = 20)
# info1("abc") # It will give error

def info2(name,*args):
    print(name,args)

# The name value will be outside the tuple formed by args 
info2("PSP","P", 20)
info2("ABC") 

def info3(name,**kwargs):
    print(name,kwargs)

# The name value will be outside the dictionary formed by kwargs 
info3("PSP",address = "P",age = 20)

# 24/1/26

# Lambda : It is a function with no name and also known as anonymous function. It is simple function.
# Map : 
# Filter : 
# Reduce : 