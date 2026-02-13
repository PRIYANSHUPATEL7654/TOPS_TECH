# 7/2/26

try:
    num = int(input("Enter a number : "))
    print(num/0)
except:
    print("Enter number only")

# 10/2/26

try:
    num = int(input("Enter a number : "))
    print(num/2)
    dic = {"name":"age"}
    print(dic["age"])
except ZeroDivisionError:
    print("Number cannot be divided by 0")
except ValueError:
    print("Input mismatch")
except:
    print("Exception")

import traceback
try:
    num = int(input("Enter a number : "))
    dic = {"name":"age"}
    # print(dic["age"])
# except:
#     traceback.print_exc()
except Exception as e:
    print(type(e).__name__,":",e)

# Custom Exception

class PasswordLength(Exception):
    pass # we can also apply some logic here
try:
    password = input("Enter password : ")
    if len(password)<8:
        raise PasswordLength
except PasswordLength:
    print("Exception : password must be greater than 8")

try:
    num = int(input("Enter a number : "))
    print(num/2)
except:
    print("Exception")
else:
    print("Else block")
finally:
    print("Finally block executed")