# 1. Write a python program to sum of the first n positive integers.
# n = int(input("Enter a number : "))
# addition = 0
# if n > 0:
#     for i in range(n+1):
#         addition+=i
# print(addition)

# 2. Write a Python program to count occurrences of a substring in a string.
# s = "applessss"
# subs = "s"
# count = s.count(subs)
# print(count)

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

# 5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead If the string length of the given string is less than 3, leave it unchanged