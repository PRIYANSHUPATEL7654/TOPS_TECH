import re # regular expression
# msg = "Ahmedabad is a nice city.Ahmedabad has nice atmosphere"
# s = re.search(r"Ahmedabad",msg) # r means raw
# print(s)
# if s:
#     print("String is found")
# else:
#     print("String not found")

# s1 = re.findall(r"Ahmedabad",msg) # it finds all occurrences of the string
# print(s1)

# msg = "Ahmedabad is a nice city 1111111111.Ahmedabad has nice 2222222222 atmosphere"
# s = re.search(r"\d{10}",msg) # r means raw, d means digit
# print(s)

# s1 = re.findall(r"\d{10}",msg) # it finds all occurrences of the number with given length
# print(s1)

# s2 = re.match(r"\d{10}",msg) # it only finds whether the string we have given to search exists at the starting of the string
# print(s2)

# 26/2/26

# s3 = re.findall(r"\d+",msg) # it finds all occurrences of the number with any length 
# print(s3)

# str = "This is a new day"
# s4 = re.sub(r"new","beautiful",str) # it works for both digits and strings whereas replace only works for strings
# # s5 = re.sub(r"\d{10}","1234512345",msg)
# print(s4)

# str1 = " user user1 user2 3user3 user_psp"
# s6 = re.findall(r"user+\d",str1)
# print(s6)

# str1 = "this is my pc"
# ans = re.findall(r"[a-j]",str1)
# print(ans)

# email regex

str = "psp@gmail.com a@gmail.com b_1@gmail.in aaaa"
ans = re.findall(r"^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$",str)
print(ans)