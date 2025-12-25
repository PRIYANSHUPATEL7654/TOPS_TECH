num = int(input("Enter a number : "))
for i in range(num):
    for j in range(i):
        print("*",end=" ")
    print()
# output : 
# * 
# * * 
# * * * 
# * * * * 

num = int(input("Enter a number : "))
for i in range(num):
    for j in range(num,i,-1):
        print("*",end=" ")
    print()
# output : 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

num = int(input("Enter a number : "))
for i in range(num):
    for j in range(num,i,-1):
        print(f"{i}",end=" ")
    print(".")
# output : 
# 0 0 0 0 0 .
# 1 1 1 1 .
# 2 2 2 .
# 3 3 .
# 4 .

num = int(input("Enter a number : "))
for i in range(num):
    for j in range(i):
        print(f"{j+1}",end=" ")
    print()
# output : 
# 1
# 1 2
# 1 2 3
# 1 2 3 4

num = int(input("Enter a number : "))
for i in range(num,1,-1):
    for j in range(1,i):
        print(f"{j}",end=" ")
    print()
# output : 
# 1 2 3 4
# 1 2 3
# 1 2
# 1

num = int(input("Enter a number : "))
for i in range(num):
    for j in range(i):
        print(f"{i}",end=" ")
    print()
# output : 
# 1
# 2 2 
# 3 3 3
# 4 4 4 4

num = int(input("Enter a number : "))
count = 0
for i in range(1,num):
    if i%2!=0:
        for j in range(i-count):
            print(i,end=" ")
        print()
    else:
        count+=1
        continue
# output : 
# 1 
# 3 3                  i=3 , j=2 , count= i-j = 1
# 5 5 5                i=5 , j=3 , count= i-j = 2
# 7 7 7 7              i=7 , j=4 , count= i-j = 3
# 9 9 9 9 9            i=9 , j=5 , count= i-j = 4

num = int(input("Enter a number : "))
k = 1
for i in range(num):
    for j in range(i+1):
        print(k,end=" ")
    k+=2
    print()
# output : 
# 1 
# 3 3                  
# 5 5 5                
# 7 7 7 7              
# 9 9 9 9 9 

num = int(input("Enter a number : "))
k = 1
for i in range(num):
    for j in range(i+1):
        print(k,end=" ")
        k+=2
    print()
# output :
# 1
# 3 5
# 7 9 11
# 13 15 17 19
# 21 23 25 27 29