# 30/12/25

# Collection/Sequence : List, Set, Tuple, Dictionary
# List : Ordered, mutable collection that allows duplicate elements.
# Tuple : Ordered, immutable collection that allows duplicate elements.
# Set : Unordered, mutable collection that does not allow duplicate elements.
# Dictionary : Ordered, mutable collection that stores data in key–value pairs with unique keys.

# 1) LIST

# Adding int values in list
# list = [1,"int",2,3,4]
# sum = 0
# for i in list:
#     if type(i) == int:
#         sum += i
# print(sum)

# Find length of each element in list
# list = ["Ahmedabad","Surat","Baroda"]
# for i in list:
#         print(len(i))
# length = []
# for i in list:
#     for j in range(len(list)):
#         length[j] = len(i)
# print(length)

# Find vowels in string
# list1 = ["Ahmedabad","Surat","Baroda"]
# count = 0
# for i in list1:
#     for j in i:
#         if j in "aeiouAEIOU":
#             count +=1
#     print(count)
#     count = 0

# Convert to upper case if the len of the list element is more than 5
# str =["aaaaaaa","bbbbb","ccc"]
# for i in str:
#     if len(i) > 5:
#         print(i.upper())

# Count number of strings which starts with letter "M" in list 
# lst_name = ['abc','mno','pqr','mna']
# count = 0
# lst_M = []
# for i in lst_name:
#     if i.startswith('m'):
#         count += 1 
#         lst_M.append(i)
# print(count," Strings : ",lst_M)

# 1/1/26

# List Methods
# Append & Extend
# list_city = ['ahmedabad','surat','baroda']
# list_city.append('rajkot')
# print(list_city)

# Clear & delete
# lst_num = [1,2,3,4,5]
# lst_city = ['ahmedabad','surat','baroda','rajkot']

# lst_num.clear() # it only clears data inlike del where the list is also deleted
# del lst_city # it deletes the list along with its data
# print(lst_num)
# print(lst_city)

# Pop : It deletes the value/element at the index we give
# lst_num.pop() # by default it deletes the last element/value from the list
# lst_num.pop(2) # it deletes the element at index 2 (starts from 0)

# Remove : It deletes the value/element we tell it unlike pop in which we need to give the index at which the value needs to be removed
# lst_num.remove(4) # it removes the first element 4 from the list, we always need to specify which element needs to be deleted

# Reverse : To reverse the whole list (last element becomes first and first becomes last)
# lst_num.reverse() # it reverses the whole list

# Sort : It sorts the list in ascending order
# lst_num.sort() # sorts in ascending order
# lst_city.sort() # sorts in ascending order
# lst_num.sort(reverse=True) # sorts in descending order
# lst_city.sort(reverse =True) # sorts in descending order
# lst_num.sort(key=len) # sorts according to length in ascending order
# lst_city.sort(key=len) # sorts according to length in ascending order
# lst_num.sort(key=len,reverse=True) # sorts according to length in descending order
# lst_city.sort(key=len,reverse=True) # sorts according to length in descending order

# list_city= ['ahmedabad','baroda','surat','rajkot']
# print(max(list_city)) # it checks the second letter and the last one according to letters
# print(min(list_city)) # it checks the second letter and the first one according to letters

# list_letters= ['amreli','ahmedabad','baroda','chamannagar','dholakpur']
# print(max(list_letters)) # it checks the second letter and the last one according to letters
# print(min(list_letters)) # it checks the second letter and the first one according to letters

# Sorted : sorted vs sort
# Sum

# 2) TUPLE
# faster than list as it is immutable (it cannot be changed)
tuple_num = (1,22,333,4444,55555)
print(tuple_num[1:4]) # gives element from index 1 to 3 (4th is excluded)

# pairs
tuple_state_city = [('gujarat','gandhinagar'),('maharashtra','mumbai'),('rajasthan','jaipur')]
print(tuple_state_city[2])
print(tuple_state_city[2][1])