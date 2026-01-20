# 30/12/25

# Collection/Sequence : List, Set, Tuple, Dictionary
# List[] : Ordered, mutable collection that allows duplicate elements.
# Tuple() : Ordered, immutable collection that allows duplicate elements.
# Set{} : Unordered, mutable collection that does not allow duplicate elements.
# Dictionary{key:value} : Ordered, mutable collection that stores data in key–value pairs with unique keys.

# 1) LIST []

# Adding int values in list
list = [1,"int",2,3,4]
sum = 0
for i in list:
    if type(i) == int:
        sum += i
print(sum)

# Find length of each element in list
list = ["Ahmedabad","Surat","Baroda"]
for i in list:
        print(len(i))
length = []
for i in list:
    for j in range(len(list)):
        length[j] = len(i)
print(length)

# Find vowels in string
list1 = ["Ahmedabad","Surat","Baroda"]
count = 0
for i in list1:
    for j in i:
        if j in "aeiouAEIOU":
            count +=1
    print(count)
    count = 0

# Convert to upper case if the len of the list element is more than 5
str =["aaaaaaa","bbbbb","ccc"]
for i in str:
    if len(i) > 5:
        print(i.upper())

# Count number of strings which starts with letter "M" in list 
lst_name = ['abc','mno','pqr','mna']
count = 0
lst_M = []
for i in lst_name:
    if i.startswith('m'):
        count += 1 
        lst_M.append(i)
print(count," Strings : ",lst_M)

# 1/1/26

# List Methods
# Append & Extend
list_city = ['ahmedabad','surat','baroda']
list_city.append('rajkot')
print(list_city)

# Clear & delete
lst_num = [1,2,3,4,5]
lst_city = ['ahmedabad','surat','baroda','rajkot']

lst_num.clear() # it only clears data inlike del where the list is also deleted
del lst_city # it deletes the list along with its data
print(lst_num)
print(lst_city)

# Pop : It deletes the value/element at the index we give
lst_num.pop() # by default it deletes the last element/value from the list
lst_num.pop(2) # it deletes the element at index 2 (starts from 0)

# Remove : It deletes the value/element we tell it unlike pop in which we need to give the index at which the value needs to be removed
lst_num.remove(4) # it removes the first element 4 from the list, we always need to specify which element needs to be deleted

# Reverse : To reverse the whole list (last element becomes first and first becomes last)
lst_num.reverse() # it reverses the whole list

# Sort : It sorts the list in ascending order
lst_num.sort() # sorts in ascending order
lst_city.sort() # sorts in ascending order
lst_num.sort(reverse=True) # sorts in descending order
lst_city.sort(reverse =True) # sorts in descending order
lst_num.sort(key=len) # sorts according to length in ascending order
lst_city.sort(key=len) # sorts according to length in ascending order
lst_num.sort(key=len,reverse=True) # sorts according to length in descending order
lst_city.sort(key=len,reverse=True) # sorts according to length in descending order

list_city= ['ahmedabad','baroda','surat','rajkot']
print(max(list_city)) # it checks the second letter and the last one according to letters
print(min(list_city)) # it checks the second letter and the first one according to letters

list_letters= ['amreli','ahmedabad','baroda','chamannagar','dholakpur']
print(max(list_letters)) # it checks the second letter and the last one according to letters
print(min(list_letters)) # it checks the second letter and the first one according to letters

# Sorted : sorted vs sort
# Sum

# reverse a list without using reverse function
list_city_1 = ['ahmedabad','baroda','surat','rajkot']
print(len(list_city_1))
for i in range(len(list_city_1)-1,-1,-1):
    print(list_city_1[i])

# Zip : Combines 2 or more list and gives possible combined values
# eg : if a list 1 has 3 elements and list 2 has 2 elements then it will give 2 combined values
list_city_2 = ['Gandhinagar','Jaipur','Mumbai']
print(zip(list_city_1,list_city_2)) # returns object identity
print(list(zip(list_city_1,list_city_2))) # returns zipped value of both lists in list form
print(tuple(zip(list_city_1,list_city_2))) # returns zipped value of both lists in tuple form
print(set(zip(list_city_1,list_city_2))) # returns zipped value of both lists in set form
print(dict(zip(list_city_1,list_city_2))) # returns zipped value of both lists in dict form

# Unzip : It unzips the zipped values
list_city_3 = [('ahmedabad', 'Gandhinagar'), ('baroda', 'Jaipur'), ('surat', 'Mumbai')]
list_city_4 = (('ahmedabad', 'Gandhinagar'), ('baroda', 'Jaipur'), ('surat', 'Mumbai'))
list_city_5 = {('ahmedabad', 'Gandhinagar'), ('surat', 'Mumbai'), ('baroda', 'Jaipur')}
list_city_6 = {'ahmedabad': 'Gandhinagar', 'baroda': 'Jaipur'}

print(list(zip(*list_city_3)))
print(tuple(zip(*list_city_4)))
print(set(zip(*list_city_5)))
print(dict(zip(*list_city_6))) # it only unzips the keys letter wise and also in letters if there is any duplicate values it automatically removes it and does not show in output
list_city_7,list_city_8 = zip(*list_city_3)
print(list(list_city_7))
print(tuple(list_city_8))

# Comprehension : Comprehension is a short and clean way to create collections (like lists, sets, dictionaries) using a single line of code. 

list1 = ["ahmedabad","baroda","surat"]
ans = [i for i in list1 if len(i) <= 5] # only if condition
print(ans)
ans = [i if len(i) > 5 else " " for i in list1] # if else condition
print(ans)

# normal way :
ans=[]
for i in list1:
    if len(i) > 5:
        ans.append(i)
print(ans)

# Write a program to find a square of a number and store it into another list
list1 = [1,2,3,4]
ans = [i*i for i in list1 if i%2==0]
print(list1,ans)

# Write a program to convert the elements of list to upper case
list1 = ["ahmedabad","baroda","surat"]
ans = [i.upper() for i in list1]
print(ans)

# 2) TUPLE ()
# faster than list as it is immutable (it cannot be changed)
tuple_num = (1,22,333,4444,55555)
print(tuple_num[1:4]) # gives element from index 1 to 3 (4th is excluded)

# pairs
tuple_state_city = [('gujarat','gandhinagar'),('maharashtra','mumbai'),('rajasthan','jaipur')]
print(tuple_state_city[2])
print(tuple_state_city[2][1])

# 3/1/26

# 3) SET {}

# does not allow a duplicate value
lst = {} # it is by default a dictionary until we put values in set form
lst = {1,2,3,4,1} # now it is a set
print(lst)
lst.add(5)
print(lst)
lst1 = {1,2,3}
lst2 = {4,5,6,2,3,2}
print(lst1.union(lst2))

# 6/1/26

# Intersection
num1 = {1,2,3,4,5}
num2 = {11,22,33,44,55,2}
num3 = {2,5,6,4}
num4 = num1.intersection(num2)
num5 = num4.intersection(num3)
print(num5)

# Union
num6 = num1.union(num2)
print(num6)
num6 = num1 | num2 | num3 # another way of union
print(num6)

# 4) DICTIONARY {}

dict1 = {1 : "ONE",2 : "TWO",3 : "THREE"} # KEY : VALUE
# OR
dict1 = {
    1 : "ONE",
    2 : "TWO",
    3 : "THREE"}

dict1 = {1 : "ONE",2 : "TWO",3 : "THREE",2 : "FIVE", 4 : "FIVE"} # updates the value with same key
print(dict1)

dict2 = {"INDIA" : "DELHI", "USA" : "WASHINGTON", "RUSSIA" : "MOSCOW", "CANADA" : "OTTAWA"}
print(dict2["INDIA"])
print(dict2.keys())
print(dict2.values())
print(dict2.items())

print("KEYS")
for i in dict2.keys():
    print(i)

print("VALUES")
for i in dict2.values():
    print(i)

print("ITEMS")
for i,j in dict2.items():
    print(i,":",j)

print("FETCHING VALUES USING KEYS")
for i in dict2.keys():
    print(dict2[i])

# Store data of students like name, email, age, s_phone_no, marks
student_data = {"a@gmail.com" : ["A",20,1122334455,120],
                "b@gmail.com" : ["B",21,5544332211,150],
                "c@yahoo.com" : ["C",24,1234512345,180]}

for i,j in student_data.items():
    print(i,j)

for i,j in student_data.items():
    print(i)
    for k in j:
        print(k)

# 8/1/26

sum=0
for i in student_data.keys():
    sum+=student_data[i][3]
print(sum)

# 13/1/26

dict2 = {"INDIA" : "DELHI", "USA" : "WASHINGTON", "RUSSIA" : "MOSCOW", "CANADA" : "OTTAWA"}
print(dict2)

# Update : If there is a key matching in a dict then it will update its value or if there is no key in dict then it will add in it
dict2.update({"INDIA":"MUMBAI"})
print(dict2)

# Clear : It clears all the data from the dictionary
dict2.clear()
print(dict2)

# Copy
new_dict = dict2.copy()
print(new_dict)
print(id(dict2))
print(id(new_dict))

# Fromkeys : fromkeys() is a dictionary class method used to create a new dictionary from a sequence of keys, all having the same value.
lst = ["a","b",'c','d']
tup = ('a','b','c','d')
set1 = {"b","a","c"}
dict3 = dict.fromkeys(lst,2) # inserting list items as a key in dict, the second parameter will be the value of all keys
dict4 = dict.fromkeys(tup) # inserting tuple items as a key in dict, the second parameter will be the value of all keys
dict5 = dict.fromkeys(set1) # inserting set items as a key in dict, the second parameter will be the value of all keys
dict6 = dict.fromkeys("ABC",1) # inserting string characters as a key in dict, the second parameter will be the value of all keys
print(dict3)
print(dict4)
print(dict5)
print(dict6)

# Get : it will return the value of a input key
print(dict2.get("INDIA"))
print(dict2)

# Pop : It pops out the particular item of the key we give
print(dict2.pop("INDIA"))
print(dict2)

# Popitem : It removes the last key-value pair from the dictionary
print(dict2.popitem())
print(dict2)

# Setdefault : It is a dictionary method used to get the value of a key. If the key does not exist, it adds the key with a default value.
dict2.setdefault("SOUTH AFRICA","CAPE TOWN")
dict2["SOUTH AFRICA"] = "ABC" # This will update the value as ABC at the place where it was cape town before 
print(dict2)

# 13/1/26

# PEP : PYTHON ENHANCEMENT PROPOSAL