# CLASSES & OBJECTS
# Class : It is a blue print, basically a structure but not an actual entity. It is a collection of object. Eg, person()
# Object : It is a real entity and a type of class. Eg, psp = person()
# init : It is like constructor in java. It is called automatically when an object is created.
# self : It refers to the current object.

class Person:
    # 1)
    def __init__(self):
        print("Inside init")

    def greet(self,name):
        print("Good morning",name)
    
    # 2)
    def __init__(self,name,age):
        self.nam = name
        self.ag = age

    def greet(self):
        print("Name :",self.nam)

    def displayDetails(self):
        print(self.nam,self.ag)

obj1 = Person("PSP",22)
obj1.greet()
obj1.displayDetails()

obj2 = Person("DSP",23)
obj2.greet()
obj2.displayDetails()

obj3 = Person("SBP",24)
obj4 = Person("JSPsss",25)
obj5 = Person("MBP",26)
lst_Person = [obj3,obj4,obj5]

for i in lst_Person:
    if len(i.nam)>5:
        i.greet()
        i.displayDetails()

class Book:
    def __init__(self,title,author,price,no_of_pg):
        self.title = title
        self.author = author
        self.price = price
        self.no_of_pg = no_of_pg
    
    def display(self):
        print("TITLE :",self.title,"\nAUTHOR :",self.author,"\nPRICE :",self.price,"\nNO OF PAGES :",self.no_of_pg)

b1 = Book("Rich Dad Poor Dad","Robert",1000,230)
b1.display()

b2 = Book("Rich Dad Poor Dad 2","Robert 2",1040,240)
b3 = Book("Rich Dad Poor Dad 3","Robert 3",1050,250)
lst_book = [b2,b3]
for i in lst_book:
    i.display()