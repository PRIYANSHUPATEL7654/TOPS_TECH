# File : Open -> Read -> Write -> Close

# open
file = open("PYTHON_THEORY.txt")
print(file)

# read
# read : reads whole file
# readline : reads a particular line
# readlines : reads multiple lines
data = file.read()
print(data)

data1 = file.readline() # returns first line from a file
data2 = file.readlines() # returns the whole content from the file in list form line wise
data3 = file.readline() # returns first line from a file
print(data1)
print(data2)
print(data3)

# Print the content of file using readline
while True:
    data = file.readline()
    print(data)
    if not data:
        break

# Print the content of file using readlines in separate lines without making list
data2 = file.readlines()
for i in data2:
    print(i)

# Tell : It gives the number of characters in a file
print("Starting position : ",file.tell())
data2 = file.readlines()
print(data2)
print("Ending position : ",file.tell())

# Seek : It gives the number of characters of file but using seek it will start from a specific position
file.seek(25)
print("Starting position : ",file.tell())
data2 = file.readlines()
print(data2)
print("Ending position : ",file.tell())

# Write : To write something in a file 
file = open("text.txt","w")
text = "Hello again" 
file.write(text)
file.close()

# Append in existing content
file = open("10_File_Handling\\text1.txt","a") # here by writing a we give permission of appending in the existing content in file
text = "Helloji" 
file.write(text)
file.close()

# Writelines : We can use it when we want to write a list in a file
file = open("10_File_Handling\\text1.txt","a") # here by writing a we give permission of appending in the existing content in file
text = ["Helloji","1\n","2","3"] 
file.writelines(text)
file.close()

# Read from one file and write into another
file1 = open("10_File_Handling\\text1.txt")
data = file1.read()
file2 = open("10_File_Handling\\text2.txt","w")
text = data
file2.write(text)
file2.close()

# 7/2/26

# With : It handles the file opening and closing automatically so it will open file to read or write for whatever the task is and close the file after whether the task is finished or there is an error.
with open("10_File_Handling\\text1.txt") as file1:
    data = file1.read()
file2 = open("10_File_Handling\\text2.txt","w")
text = data
file2.write(text)

#JSON file handling : Java Script Object Notation

import json
user_data = {}

user_data["name"] = input("Enter your name : ")
user_data["age"] = int(input("Enter your age : "))
user_data["city"] = input("Enter your city : ")

user_data1 = ({"a":"b","c":"d"},{"e":"f","g":"h"}) # using [] or () brackets does not matter as it will always be stored in [] form
# user_data2 = {"i":"j","k":"l"},{"l":"m","n":"o"} 
with open("10_File_Handling\\user_data.json","w") as file1:
    # write the dictionary (here user_data) to the file in json format
    json.dump(user_data1,file1,indent=4)

user_data=[]
with open("10_File_Handling\\user_data.json","r") as file:
    user_data = json.load(file)
print(user_data)

for i in user_data:
    print(i)