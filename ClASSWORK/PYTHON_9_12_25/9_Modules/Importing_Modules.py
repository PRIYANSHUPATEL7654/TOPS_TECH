# 3/2/26
import Modules as m

# ans = m.fact(5)
# print(ans)

from Modules import fact,checkEven

# ans = checkEven(4)
# print(ans)

import random
# ans = random.randint(1,10)
# print(ans)

import math
# ans = math.factorial(5)
# print(ans)

import datetime
# Classes in datetime : date(only date), time(only time), datetime(date and time together), timedelta(date/time difference)
print(datetime.date.today())
print(datetime.datetime.now())
curr_year = datetime.datetime.now()
print(curr_year.year,curr_year.month,curr_year.day)
print(curr_year.hour,curr_year.minute,curr_year.second)
print(datetime.datetime.now().strftime("%d-%m-%y")) # small y gives only last 2 digit of year like 26 and big y gives full year like 2026
print(datetime.datetime.now().strftime("%H:%M:%S"))
print(datetime.datetime.now().strftime("%d-%b-%y")) # b gives month name instead of number and rest remains same

import os
# print(os.getcwd()) # Gives current working directory
# print(os.listdir(".")) # Gives names of all files in list form from the current directory
# print(os.listdir("./Modules")) # Gives names of all files in list form from the given directory
# mkdir, rmdir, rename, remove
# print(os.process_cpu_count())

import sys
# access command line arguments : the parameters passed at runtime
print(sys.argv) # it helps pass parameters at runtime in cli
# python 10_Importing_Modules PSP 10 ABC XYZ # Run this in cli, it will give output of this values in list form
# sys.exit()
print(sys.version)
print(sys.path)