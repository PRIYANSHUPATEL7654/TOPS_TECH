# 18/12/25
# Python control statements are commonly grouped as:
# Decision / Selection statements
# if
# if–else
# if–elif–else
# match–case

# Looping statements
# for
# while

# Jump statements
# break
# continue
# pass
# return

# 1) Match
# # match compares a value against different patterns and executes the block where the pattern matches.
day = int(input("Enter day(1-7) : "))
match day:
    case 1 : print("Monday")
    case 2 : print("Tuesday")
    case 3 : print("Wednesday")
    case 4 : print("Thursday")
    case 5 : print("Friday")
    case 6 : print("Saturday")
    case 7 : print("Sunday")
    case _ : print("Please enter valid day")

month = int(input("Enter month(1-12) : "))
a = [1,3,5,7,8,10,12]
b = [4,6,9,11]
if month in a:
    print("31 days")
elif month in b:
    print("30 days")
elif month == 2:
    print("28/29 days")
else:
    print("Please enter valid day")
# OR
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12 : print("31 days")
    case 2 : print("28/29 days")
    case 4 | 6 | 9 | 11 : print("30 days")
    case _ : print("Please enter valid day")
# OR
match month:
    case m if m in (1, 3, 5, 7, 8, 10, 12) : print("31 days")
    case 2 : print("28/29 days")
    case m if m in (4, 6, 9, 11) : print("30 days")
    case _ : print("Please enter valid day")

# 2) For
# (for i in range()) is for digits and (for i in ) is for strings
for a in range (10):
    print(f"{a}")
start = int(input("Enter starting position : "))
end = int(input("Enter ending position : "))

if(start < end):
    print("starting number should be lesser than ending position")

for a in range (start,end):
    print(f"Welcome user {a}")

for a in range(1,15,2):
    print(f"{a}")

for a in range(0,15,2):
    print(f"{a}")

for a in range(15,1,-2):
    print(f"{a}")

for a in range(15,0,-2):
    print(f"{a}")

start = int(input("Enter starting position : "))
end = int(input("Enter ending position : "))
increment = int(input("Enter increment : "))

if(start < end):
    print("starting number should be lesser than ending position")

for a in range (start,end,increment):
    print(f"Welcome user {a}")

# 20/12/25

# 3) While

i = 1
while i <= 10:
    print("Hello",i)
    i+=1

# Table : Printing table of any number
num = int(input("Enter the number for which you want whole table : "))
i = 1
if num%2 == 0:
    while i <= 10:
        print(f"{num} * {i} = ",num*i)
        i+=1
else:
    print("Number is not even")

num = int(input("enter the number for its table : "))
for i in range(1,11):
    print(num*i)

# MENU DRIVEN PROGRAMS

# 1. ADDITION
# 2. SUBTRACTION
# 3. MULTIPLICATION
# 4. DIVISION
# 5. EXIT

while True:
    choice = int(input("1. ADDITION\n2. SUBTRACTION\n3. MULTIPLICATION\n4. DIVISION\n5. EXIT\nEnter your choice from above options : "))

    match choice:
        case 1:
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            print(f"Addition of {num1} and {num2} is",num1+num2)
        case 2:
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            print(f"Subtraction of {num1} and {num2} is",num1-num2)
        case 3:
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            print(f"Multiplication of {num1} and {num2} is",num1*num2)
        case 4:
            num1 = int(input("Enter number 1 : "))
            num2 = int(input("Enter number 2 : "))
            print(f"Division of {num1} and {num2} is",num1/num2)
        case 5: break
        case _ :
            print("Invalid choice")

# 4) Break

i = 1
while i <= 10:
    print(i)
    if(i == 3):
        break
    i+=1

# 5) Continue

i=1
while i<=10:
    i+=1
    if(i==3):
        continue
    print(i)

# 6) Pass

# 23/12/25

# To check if a number is prime or not

num = int(input("Enter the number : "))
temp = 1
for i in range(2,num):
    if i % 2 == 0:
        temp = 1
        print(num,"is not a prime number")
        break
    else:
        temp = 0
if temp == 0:
    print(num,"is a prime number")

# print numbers are prime and not prime for 2 to 100 
for i in range(2,101):
    temp = 1
    for n in range (2,i):
        if i % 2 == 0:
            temp = 1
            print(i,"is not a prime number")
            break
        else:
            temp = 0
    if temp == 0:
        print(i,"is a prime number")

# print numbers are prime and not prime for 2 to 100 and count of total prime and not prime numbers
count_prime = 0
count_not_prime = 0
for i in range(2,101):
    temp = 1
    for n in range (2,i):
        if i % 2 == 0:
            temp = 1
            count_not_prime += 1
            print(i,"is not a prime number")
            break
        else:
            count_not_prime += 1
            temp = 0
    if temp == 0:
        print(i,"is a prime number")
print("total prime numbers : ",count_prime)
print("total not prime numbers : ",count_not_prime)