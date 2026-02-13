def checkEven(num):
    if num%2==0:
        return num
    
def checkPositive(num):
    if num>0:
        return "positive"
    
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

class C1:
    def __init__(self):
        pass

    def display(self):
        print("Inside display")

# MATH,OS,SYS,RANDOM,DATETIME