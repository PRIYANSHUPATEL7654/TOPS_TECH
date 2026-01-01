# 25/12/25

# Strings : Collection of objects, immutable (cannot be changed)

# name = input("Enter the name : ")
# print("Upper : ",name.upper())
# print("Lower : ",name.lower())
# print("Capitalize : ",name.capitalize())
# print("Title : ",name.title())
# print(f"Length(len) : {len(name)}")
# print(f"Count : {name.count("p")}")
# print(f"Count : {name.count("Pat",10)}") # Checks for Pat after/from 10th position
# print(f"Split : {name.split()}")
# print(f"Startswith : {name.startswith("P")}")
# print(f"Replace : {name.replace("P","p")}")
# print(f"Find : {name.find("P")}") # Only shows the first occurrence of the provided letter/word
# print(f"Trim : {name.strip("Priy")}") # Strip can be called as trim
# print(F"RTrim : {name.rstrip("tel")}")
# print(F"LTrim : {name.lstrip("Pri")}")
# lst=name.split()
# print(f"{lst,len(lst)}")
# lst_cities=['Ahmedabad','Baroda','Surat']
# all_cities=",".join(lst_cities)
# print("Join : ",all_cities)

# name = input("Enter name : ")
# for i in name: # for printing the string
#     print(i)
# for i in range (len(name)): # for printing the string along with the string indexes
#     print(name[i],i)

# Slicing : can be positive or negative
# syntax : name[start:end:stop]

#positive slicing (check string from left to right acc to index)
# print(name[2:5]) # to print the string from 2nd position to 4th (5th letter will not be printed)
# print(name[:5]) # to print upto 4th position
# print(name[2:]) # to print from position 2 to end
# print(name[::2]) # to print alternate (even) positions starting from 0,2,4,....,end
# print(name[1::2]) # to print alternate (odd) positions starting from 1,3,5,....,end
# negative slicing (check string from right to left acc to index)
# print(name[-8:-2]) # to print from 2 to 8 position
# print(name[:-2])
# print(name[-8:])
# print(name[::-1])

str = "Priyanshu Patel" # output should be : eliyanshu patpr, eg2 : tops technologies - output : esps technologito
str1 = str[-2:]
str2 = str[2:(len(str)-2)]
str3 = str[0:2]
print(str,"\n",str1+str2+str3)