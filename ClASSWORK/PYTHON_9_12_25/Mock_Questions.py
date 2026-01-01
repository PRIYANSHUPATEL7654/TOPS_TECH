lst= [1,2,3]
for _ in lst:
    print("in pass")
    pass

print("hello"*5)
a=10
c = a
d = 10
lst1 = [1,2,3]
lst2 = [1,2,3]
lst3 = lst1
print(id(lst1))
print(id(lst2))
print(id(lst3))
print(f"{lst1 is lst2} - {lst1 == lst2}")
print(f"{lst3 is lst1}")
print(id(a))
print(id(d))
print(f"{a is d} - {a == d}")
print(f"{c is a}")

e = -10
result = "Positive" if e > 0 else "Negative" 
print(result)
city = ["a","b","c"]
for lst in city:
    print(lst)
    if lst == "a":
        break
else:
    print("else")