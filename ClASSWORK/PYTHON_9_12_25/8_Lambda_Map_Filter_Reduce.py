# 1) LAMBDA 

add = lambda num1,num2 : num1+num2
print(add(10,20))

sq = lambda num : num**2
print(sq(10))

up_str = lambda name:name.upper()
print(up_str("Priyanshu"))

even_or_add = lambda num : "even" if num%2==0 else "odd"
print(even_or_add(90))

max = lambda num1,num2 : f"{num1} is greater" if num1 > num2 else f"{num2} is greater"
print(max(90,20))

lst = [1,2,3,4]

sq_ans =[]
for i in lst:
    sq_ans.append(sq(i))
print(sq_ans)


lst_names = ['priyanshu','akshar','jil']
up_ans =[]
for i in lst_names:
    up_ans.append(i.upper())
print(up_ans)

def sq(num):
    ans = num**2
    return ans

# 2) MAP

num_list = [1,2,3]
sq_list = list(map(sq,num_list))
print(sq_list)

def str_up(str):
    ans = str.upper

lst_names = ['priyanshu','akshar','jil']
upper_name = list(map(str.upper,lst_names))
print(upper_name)

# 27/1/26

lst_num = [1,2,3,4]
pow_num = [2,2,2,3]
lst_ans1 = []

for i in range(len(lst_num)):
    # lst_ans1.append(lst_num[i]**pow_num[i])
    # OR
    lst_ans1.append(pow(lst_num[i],pow_num[i]))

print(lst_ans1)

# # OR

lst_ans2 = list(map(pow,lst_num,pow_num))
print(lst_ans2)

# Convert celsius list to fahrenheit list

lst_cel = [0,2,-40,10]
lst_fah = list(map(lambda num: (9/5)*num+32,lst_cel))
print(lst_fah)

# 29/1/26

# If number is even then find square of the number

def checkEven(num):
    if num%2==0:
        return num
    
def sq(num):
    return num*num

lst = [1,2,3,4,5,6]
lst_even = list(filter(checkEven,lst)) # executed in double line
lst_ans = list(map(sq,lst_even))

lst_ans = list(map(sq,list(filter(checkEven,lst)))) # executed in single line

print(lst_ans)

# The above task can also be done using lambda function as below

lst = [1,2,3,4,5,6,7]

lst_even = list(filter(lambda num:num%2==0,lst))
lst_ans = list(map(lambda num:num*num,lst_even))
print(lst_even,lst_ans)

# # REDUCE

from functools import reduce

def add(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

lst = [1,2,3,4]
ans1 = reduce(add,lst)
print(ans1)

ans2 = reduce(mul,lst)
print(ans2)

# find the sum of squares of all even numbers

lst = [1,2,3,4,5,6]
lst_even = list(filter(lambda num:num%2==0,lst))
lst_sq = list(filter(lambda num:num*num,lst_even))
lst_add = list(filter(lst_sq))
print(lst_add)