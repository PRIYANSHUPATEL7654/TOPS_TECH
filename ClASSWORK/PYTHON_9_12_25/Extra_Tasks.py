# 1) Find Ared of circle (pi*radius*radius).
# note : pi = 3.14 , radius=accept float value from user

# pi = 3.14
# radius = float(input("Enter radius (in decimal) : "))
# area = pi*radius*radius
# print("Area of Circle : ",area)

# 2) Find maximum number using max function.

# a = [1,3,4,2,5]
# print(max(a))

# 3) Find maximum number using ternary operator.

# a = 1; b = 3; c = 2

# if a > b:
#     if a > c:
#         print(f"{a} is greatest")
#     else:
#         print(f"{c} is greatest")
# else:
#     if b > c:
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")

# 4) Find simple Interest . SI=(P*T*R)/100

# p = int(input("Enter principal amount : "))
# t = int(input("Enter time (in yrs) : "))
# r = int(input("Enter rate of interest (in %) : "))
# SI = (p*t*r)/100
# print("Simple interest : ",SI)

# 5) Find Compound Interest. Amount = P(1 + R/100) t  Compound Interest = A - P

# p = int(input("Enter principal amount : "))
# t = int(input("Enter time (in yrs) : "))
# r = int(input("Enter rate of interest (in %) : "))
# a = p*(1 + (r/100))*t
# print(a)
# CI = a - p
# print("Compund interest : ",CI)

# 6) Print ASCII number into letter. e.g input - 65 output 'A' , input - 56 output- 8

# ord() → character ➝ ASCII value
# chr() → ASCII value ➝ character
# num = int(input("Enter number : "))
# ascii_char = input("Enter letter : ")
# print(chr(num),ord(ascii_char))

# 7) Convert Binary to Decimal(Use int()) e.g input - 11011 and output - 27

# int("1011", 2)    # Binary → Decimal
# int("17", 8)      # Octal → Decimal
# int("123", 10)    # Decimal → Decimal
# int("1A", 16)     # Hexadecimal → Decimal

# binary = input("Enter binary number : ")
# decimal = int(binary,2)
# print(decimal)

# 8) Convert temperature, degrees Fahrenheit to degrees Celsius and vice versa. C = (5/9) * (F - 32) &  F = C * 9/5 + 32

# c_ = int(input("Enter temp in celsius : "))
# f_ = int(input("enter temp in fahrenheit : "))
# c = (5/9)*(f_ - 32)
# f = c_ * 9/5 + 32
# print(f"Temp for {c_} degree celsius is {f} in degree fahrenheit /n Temp for {f_} degree fahreheit is {c} in degree celsius")

# 9) Print multiplication table of given number e.g 5 output 5*1=5 ..... 5*10 = 50

# num = int(input("enter the number for its table : "))
# for i in range(1,11):
#     print(num*i)

# 10) Print no. of days in given list of Months e.g ['April','February','May'] output April - 30 Days February - 28 or 29 days,May 31 Days

# month = int(input("Enter month(1-12) : "))
# match month:
#     case 1 | 3 | 5 | 7 | 8 | 10 | 12 : print("31 days")
#     case 2 : print("28/29 days")
#     case 4 | 6 | 9 | 11 : print("30 days")
#     case _ : print("Please enter valid day")

# 11) Print no of digits and letters in String.Accept String from user. E.g string="H1Visa" Digits = 1 and letters=5

# s = input("Enter a string : ")
# digits = 0
# letters = 0
# for ch in s:
#     if ch.isdigit():
#         digits+=1
#     elif ch.isalpha():
#         letters+=1
# print(f"{digits} digits and {letters} letters are there in given input")

# 12) Accept and print number until user enter 0 (use while)

# user = int(input("Enter the number : "))

# while user != 0:
#     print(user)
#     user = int(input("Enter the number : "))
    
# 13) Count number of digits in given number (e.g number=23456 o/p digits=5)

# num = 23456
# count = len(str(num))
# print(count)

# 14) Print list of items iteratively e.g lst_grade = ['A','B','C'] 
# output = A
# B
# C

# lst_grade = ['A','B','C']
# for i in lst_grade:
#     print(i)

# 15) Print list of items iteratively among with type of data e.g lst_collection = ['A',True,234,45.76] 
# output = A - chr
# True - bool
# 234 - int
# 45.76 - float

# lst_collection = ['A',True,234,45.76]
# for i in lst_collection:
#     print(i," - ",type(i))

# 16) Print even numbers fall between 2 given numbers E.g user enter 10 20 
# output 12,14,16,18

# a = int(input("Enter the starting number : "))
# b = int(input("Enter the ending number : "))
# for i in range(a+1,b):
#     if (i % 2 == 0):
#         print(i)

# 17) Write a program to display number names of entered number e.g number="345" output = Three Four Five

# number = "345"
# for i in number:
#     if i == '0':
#         print("Zero",end=" ")
#     elif i == '1':
#         print("One",end=" ")
#     elif i == '2':
#         print("Two",end=" ")
#     elif i == '3':
#         print("Three",end=" ")
#     elif i == '4':
#         print("Four",end=" ")
#     elif i == '5':
#         print("Five",end=" ")
#     elif i == '6':
#         print("Six",end=" ")
#     elif i == '7':
#         print("Seven",end=" ")
#     elif i == '8':
#         print("Eight",end=" ")
#     elif i == '9':
#         print("Nine",end=" ")
#     else:
#         continue

# 18) Write a program to write series 1/1! + 1/2! + 1/3! + 1/4! ....1/number!

# number = int(input("Enter the number : "))
# j = 1
# result = 0
# for i in range(1,number):
#     j *= i
#     result += (1/j)
# print(result)

# 19) Write a program to display numbers which are divisible by 13 from given range.

# a = int(input("Enter the starting number : "))
# b = int(input("Enter the ending number : "))

# for i in range(a,b):
#     if i%13==0:
#         print(i)

# 20) Print even numbers from given range without using % .

# a = int(input("Enter the even starting number : "))
# b = int(input("Enter the ending number : "))

# for i in range (a,b,2):
#     print(i)

# 21) Print Pattern 
# 1     
# 1    0
# 1    0    1
# 1    0    1    0

# num = int(input("Enter the number of lines : "))
# for i in range (1,num+1):
#     for j in range (1,i+1):
#         if j%2 == 0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()

# 22) Print Pattern 
# A     
# A    B
# A    B    C
# A    B    C    D

# num = int(input("Enter the number of lines : "))
# for i in range (num):
#     a = 65
#     for j in range(i+1):
#         print(chr(a),end=" ")
#         a+=1
#     print()
        

# 23) Print Pattern 
# 1
# 2  2
# 3  3  3
# 4  4  4  4

# num = int(input("Enter the number of lines : "))
# for i in range (1,num+1):
#     for j in range (1,i+1):
#         print(i,end=" ")
#     print()

# 24) Print Pattern 
# 1
# 1  2
# 2  3  4
# 4  5  6  7
# 7  8  9  10

# num = int(input("Enter the number of lines : "))
# for i in range (1,num+1):
#     for j in range (1,i+1):
#         print(j,end=" ")
#     print()

# 25) Print Pattern
# ****
# ***
# **
# *

# num = int(input("Enter the number of lines : "))
# for i in range (num,0,-1):
#     for j in range (i):
#         print("*",end=" ")
#     print()

# 26) Print Pattern
#       *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *

# n = 10
# for i in range(1, n+1):
#     print(" " * (2*(n-i)),end = "")
#     # First star
#     print("*", end="")

#     if i > 1:
#         for j in range(i,1,-1):
#             print(" " * 3,end = "")
#             print("*",end ="")
    
#     print()

# for i in range(n - 1, 0, -1):
#     # Leading spaces
#     print(" " * (2*(n-i)), end="")
    
#     # First star
#     print("*", end="")
    
#     # Inner spaces
#     if i > 1:
#         for j in range(i,1,-1):
#             print(" " * 3,end = "")
#             print("*",end ="")
    
#     print()

# 27) Print Pattern
#    *
#   * *
#  *   *
# *     *
#  *   *
#   * *
#    *

# n = 4  # Change this value to make it bigger/smaller

# # Upper half (including middle row)
# for i in range(1, n + 1):
#     # Leading spaces
#     print(" " * (n - i), end="")
    
#     # First star
#     print("*", end="")
    
#     # Inner spaces (only if not the first row)
#     if i > 1:
#         print(" " * (2 * i - 3), end="")
#         # Second star
#         print("*", end="")
    
#     print()  # new line

# # Lower half (excluding the middle row — start from n-1 down to 1)
# for i in range(n - 1, 0, -1):
#     # Leading spaces
#     print(" " * (n - i), end="")
    
#     # First star
#     print("*", end="")
    
#     # Inner spaces
#     if i > 1:
#         print(" " * (2 * i - 3), end="")
#         # Second star
#         print("*", end="")
    
#     print()  # new line