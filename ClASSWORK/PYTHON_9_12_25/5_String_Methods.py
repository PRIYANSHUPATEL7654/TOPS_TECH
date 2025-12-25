# 25/12/25

# Strings : Collection of objects, immutable (cannot be changed)

name = input("Enter the name : ")
print("Upper : ",name.upper())
print("Lower : ",name.lower())
print("Capitalize : ",name.capitalize())
print("Title : ",name.title())
print(f"Length(len) : {len(name)}")
print(f"Count : {name.count("p")}")
print(f"Count : {name.count("Pat",10)}") # Checks for Pat after/from 10th position
print(f"Split : {name.split()}")
print(f"Startswith : {name.startswith("P")}")
print(f"Replace : {name.replace("P","p")}")
print(f"Find : {name.find("P")}") # Only shows the first occurrence of the provided letter/word
print(f"Trim : {name.strip("Priy")}") # Strip can be called as trim
print(F"RTrim : {name.rstrip("tel")}")
print(F"LTrim : {name.lstrip("Pri")}")
lst=name.split()
print(f"{lst,len(lst)}")
lst_cities=['Ahmedabad','Baroda','Surat']
all_cities=",".join(lst_cities)
print("Join : ",all_cities)