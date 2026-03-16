# 1. Write a python program to sum of the first n positive integers.

n = int(input("Enter a number : "))
addition = 0
if n > 0:
    for i in range(n+1):
        addition+=i
print(addition)

# 2. Write a Python program to count occurrences of a substring in a string.

s = "applessss"
subs = "s"
count = s.count(subs)
print(count)

# 3. Write a Python program to count the occurrences of each word in a given sentence.

sen = "hi how are are you you . hi i i am fine"
list = sen.split()
print(list)
for i in set(list):
    if list.count(i) > 1:
        print(f"{i} =",list.count(i))

# 4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

str = "Priyanshu Patel" # output should be : eliyanshu patpr, eg2 : tops technologies - output : esps technologito
str1 = str[-2:]
str2 = str[2:(len(str)-2)]
str3 = str[0:2]
print(str,"\n",str1+str2+str3)

# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged.

str = 'priyanshu'
if len(str) >= 3:
    if str.endswith('ing'):
        str += 'ly'
        print(str)
    else:
        str += "ing"
        print(str)
else:
    print(str)

# 6. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

str = "prinotabcpooraaaa"
not_index = str.find("not")
poor_index = str.find("poor")
if not_index !=-1 and poor_index !=-1 and not_index < poor_index:
    str1 = str.replace(str[not_index:poor_index + 4],"good")
    print(str1)
else:
    print(str)

# 7. Program to find Greatest Common Divisor of two numbers. For example, the GCD of 20 and 28 is 4 and the GCD of 98 and 56 is 14.

no1 = 20
no2 = 28

while no2 != 0:
    no1, no2 = no2, no1 % no2

print("GCD is : ", no1)

# 8. Write a Python program to check whether a list contains a sublist.

def is_sublist(main_list,sub_list):
    n = len(sub_list)
    m = len(main_list)

    for i in range(m-n+1):
        if(main_list[i:i+n]) == sub_list:
           return True
    return False
    
main_list = [1,2,3,4]
sub_list = [2,3]

print(is_sublist(main_list,sub_list))

# 9. Write a Python program to find the second smallest number in a list.

num_list = [4,5,3,6]
num_list.sort()
print(num_list[1])

# 10. Write a Python program to get unique values from a list.

num_list = [1,1,2,3,1,4,1,5,1,6,1]
unique_list =[]

for i in num_list:
    if num_list.count(i) >= 1 and i not in unique_list:
        unique_list.append(i)

print(sorted(unique_list))

# OR

num_list = [1,1,1,1,1,1,1,1,1]

i = 0
while i < len(num_list):
    if num_list.count(num_list[i]) > 1:
        num_list.pop(i)
    else:
        i += 1

print(sorted(num_list))

# 11. Write a Python program to unzip a list of tuples into individual lists.

lst = [(1,2),(2,3),(3,4)]
print(list(zip(*lst)))

# 12. Write a Python program to convert a list of tuples into a dictionary

lst = [(1,2),(2,3),(3,4)]
print(dict(lst))

# 13. Write a Python program to sort a dictionary (ascending /descending) by value.

dict1 = {1: 3, 2: 2, 3: 4}
print(sorted(dict1.values())) # In ascending order
print(sorted(dict1.values(),reverse=True)) # In descending order

# 14. Write a Python program to find the highest 3 values in a dictionary

dict1 = {1: 3, 2: 2, 3: 10, 4: 5, 5: 7, 6: 8}
dict_values = sorted(dict1.values(),reverse=True)

for i in range(3):
    print(dict_values[i])

# 15. Given a number n, write a python program to make and print the list of Fibonacci series up to n. Input : n=7 Hint : first 7 numbers in the series Expected output :
# First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(7):
    print(i , " - ",fibonacci(i))

# 16. Counting the frequencies in a list using a dictionary in Python. 
# Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
# Expected output : 1 : 5 , 2 : 4 , 3 : 3 , 4 : 3 , 5 : 2

lst = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
dct1 = {}
for i in lst:
    if i not in dct1.keys():
        dct1[i] = lst.count(i)
print(dict(sorted(dct1.items())),end=" ")

# 17. Write a python program using function to find the sum of odd series and even series
# Odd series: 1^2/ 1! +3^2/ 3! + 5^2/ 5!+……n
# Even series: 2^2/ 2! + 4^2/ 4! + 6^2/ 6!+……n

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def odd_series(n):
    s = 0
    for i in range(1, n+1, 2):   # 1,3,5...
        s = s + (i**2) / factorial(i)
    return s


def even_series(n):
    s = 0
    for i in range(2, n+1, 2):   # 2,4,6...
        s = s + (i**2) / factorial(i)
    return s


n = int(input("Enter the number of values to find sum of : "))

print("Sum of Odd Series =", odd_series(n))
print("Sum of Even Series =", even_series(n))

# 18. Python Program to Find Factorial of Number Using Recursion

def fact(no):
    if no == 0 or no == 1:
        return no
    else:
        return no * fact(no-1)

num = int(input("Enter a number to find factorial for : "))
print(fact(num))

# 19. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def list1(lst):
    tup = set(lst) # because set removes all duplicate values from the list while printing
    return tup

lst = [1,3,2,4,3,5,4]
print(list1(lst))

# 20. Mini project :
# Problem Statement : Password Generator
# Make a program to generate a strong password using the input given by the user. To generate a password, randomly take some words from the user input and then include numbers, special characters and capital letters to generate the password. Also, keep a check that password length is more than 8 characters.
# Note: Include Exception handling wherever required. Also, make a ‘User’ class and store the details like user id, name and password of each user as a tuple.

import random
import string

class User:

    def __init__(self, user_id, name, password):
        self.details = (user_id, name, password)

    def display(self):
        print("User Details:", self.details)


def generate_password(words):

    word_list = words.split()

    if len(word_list) < 2:
        raise ValueError("Enter at least two words to generate password")

    w1 = random.choice(word_list)
    w2 = random.choice(word_list)

    number = str(random.randint(10,99))
    special = random.choice("@#$%&")

    password = w1.capitalize() + w2 + special + number

    if len(password) < 8:
        raise ValueError("Generated password is less than 8 characters")

    return password


try:

    user_id = int(input("Enter User ID: "))
    name = input("Enter Name: ")
    words = input("Enter some words: ")

    password = generate_password(words)

    print("Generated Password:", password)

    user = User(user_id, name, password)
    user.display()

except Exception as e:
    print(type(e).__name__,":",e)