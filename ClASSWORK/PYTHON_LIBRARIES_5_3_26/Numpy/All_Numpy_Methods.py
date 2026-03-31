import numpy as np
arr = np.array([10, 20, 30, 40])

print("NumPy Array:", arr)
print("Type:", type(arr))


print(np.random.rand(2,3)) # it creates uniform distribution positive values(it means that it creates random numbers without any pattern) in float and in 2*3 matrix. It ranges from 0 to 1.
print(np.random.randn(2,3)) # it creates normal distribution positive & negative values(it means that it creates random numbers either positive or negative in bell shaped curve where mean = 0 and std = 1. It means all values are centered around 0) in float and in 2*3 matrix. It ranges from -infinity to +infinity. It is used in machine learning instead of rand as it makes learning more accurate unlike rand where only positive values may not be accurate in learning and giving appropriate output.
print(np.random.randint(2,10,5)) # it gives an array of size 5 with random int values ranging from 2 to 10.
print(np.random.randint(2,10,(2,3))) # it creates a 2*3 matrix of random int values ranging from 2 to 10.
print(np.random.random(4)) # it creates an array of same type of values as in rand.
print(np.random.random((2,3))) # it is same as rand, the difference is there only in syntax as here the dimensions are given in tuple((2,3)) and in rand it is not given in tuple(2,3). The output in both will be same (the values are random so it may be different but both follows same rule).
print(np.random.choice([10,20,30,40])) # it gives random value from the given array.
print(np.random.choice([10,20,30,40],3)) # it gives 3 random value from the given array.
