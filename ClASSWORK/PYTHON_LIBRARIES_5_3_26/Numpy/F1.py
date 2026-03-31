import numpy as np

# 6/3/26
# lst1 = [1,3,2,5,4]
# set1 = {5,4,2,6,8,7,7}

# print(lst1)
# print(set1)

# add = []
# sub = []
# mul = []
# div = []

# for i in lst1:
#     add.append(i+2)
#     sub.append(i-2)
#     mul.append(i*2)
#     div.append(i/2)

# print(add,sub,mul,div)

# add1 = np.array(lst1)
# print(add1 + 2)

# sub1 = np.array(lst1)
# print(add1 - 2)

# mul1 = np.array(lst1)
# print(add1 * 2)

# div1 = np.array(lst1)
# print(add1 / 2)

# 7/3/26
# mat = [4][4]
# for i in mat:
#     for j in i:
#         print(j)

# matrix using numpy
# matrix = np.array([[1,2,3,4],[5,6,7,8]])
# print(matrix)

# array properties
# 1) shape : 2 * 4
# 2) ndim : here 2 dimensions
# 3) size : 2 * 4 = 6
# 4) dtype : here int

# print("Shape of array : ",matrix.shape)
# print("Shape of array : ",matrix.ndim)
# print("Shape of array : ",matrix.size)
# print("Shape of array : ",matrix.dtype)

# arr1 = np.arange(1,21)
# print(arr1)
# matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix1 * 10)
# print("Shape of array : ",matrix1.shape)
# print("Shape of array : ",matrix1.ndim)

# 10/3/26

# zeros_array = np.zeros((2,3))
# print(zeros_array)
# ones_array = np.ones((3,4))
# print(ones_array)
# range_array = np.arange(1,1000,2)
# print(range_array)

# 11/3/2026

# Mathematical Operations
# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)
# print(arr1 / arr2)

# Linspace
# arr = np.linspace(0,10,8)
# print(arr)
# arr = np.eye(3,5) # here 3 number of rows will be displayed from 5 * 5 matrix 
# print(arr)
# arr = np.identity(5)
# print(arr)

# array = np.arange(1,10)
# reshaped_arr = array.reshape(3,3)
# print(reshaped_arr)
# ravel_arr = reshaped_arr.ravel()
# print(ravel_arr)
# flatten_arr = reshaped_arr.flatten()
# print(flatten_arr)

# matrix = np.array([[1,2,3],[4,5,6]])

# print("Original:\n", matrix)
# print("Transpose using T:\n", matrix.T)
# print("Transpose using function:\n", np.transpose(matrix))

# np.random.seed(42)

# print("Uniform:\n", np.random.rand(2,2))
# print("Normal:\n", np.random.randn(2,2))
# print("Random Integers:\n", np.random.randint(1, 10, (2,3)))
# print("Random Choice:\n", np.random.choice([10,20,30], size=9))

# 13/3/26

# a = np.array([10,20,30])
# b = np.array([2,4,6])

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print("Floor division value : ",a // b)
# print("Power : ",a ** 2)
# print("Modulo(Remainder) : ",a % b)

# Operators
# a = np.array([5,10,15])
# print("Greater than 8 : ",a > 8) # It will give boolean values (true false)
# print("Greater than 8 : ",a[a > 8]) # It will give values acc to condition
# print("Equal to 10 : ",a == 10) # It will give boolean values (true false)
# print("Equal to 10 : ",a[a == 10]) # It will give values acc to condition

# Logical Operators
# and, or, not
# a = np.array([1,3,5,6])
# print("And Operator : ", np.logical_and(a>1, a<6))
# print("And Operator : ", a[np.logical_and(a>1, a<6)])

# print("Or Operator : ", np.logical_or(a>1, a<10))
# print("Or Operator : ", a[np.logical_or(a>1, a<10)])

# print("Not Operator : ", np.logical_not(a>1))
# print("Not Operator : ", a[np.logical_not(a>1)])

# a = np.array([[1,3,5],[1,3,5]])
# b = np.ones([1,2,3])
# print(a + b)

# a = np.array([1,3,5])
# print("Aggregate sum : ",np.sum(a))

# 14/3/26

# Mathematical and Statistical Functions
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# add1 = np.add(a,b)
# sub1 = np.subtract(a,b)
# mul1 = np.multiply(a,b)
# div1 = np.divide(b,a)
# power = np.power(b,a)
# mod1 = np.mod(a,b) # to find remainder
# sqrt1 = np.sqrt(b)
# expo = np.exp(b)
# log = np.log(a) # natural log
# log10 = np.log10(a) # log base 1o
# print(add1)
# print(sub1)
# print(mul1)
# print(div1)
# print(power)
# print(mod1)
# print(sqrt1)
# print(expo)
# print(log)
# print(log10)

# arr = np.array([1.4,2.6,3.5])
# print(np.round(arr))
# print(np.floor(arr))
# print(np.ceil(arr))

# Statistical functions : 
# data = np.array([10, 20, 30, 40, 50])
# print("Mean:", np.mean(data))
# print("Median:", np.median(data))
# print("Standard Deviation:", np.std(data))
# print("Variance:", np.var(data))
# print("Minimum:", np.min(data))
# print("Maximum:", np.max(data))
# print("Sum:", np.sum(data))
# print("Cumulative Sum:", np.cumsum(data))
# print("Product:", np.prod(data))
# print("90th Percentile:", np.percentile(data, 70))

# 16/3/26

# CONCATENATION
# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# c = np.array([[9,10],[11,12]])
# print("Concatenate axis=0:\n", np.concatenate((a,b,c),axis=0))
# print("Concatenate axis=1:\n", np.concatenate((a,b,c), axis=1))

# CONCATENATION USING FUNCTIONS
# print("vstack:\n", np.vstack((a,b,c)))
# print("hstack:\n", np.hstack((a,b,c)))
# print("dstack:\n", np.dstack((a,b,c)))

# Splitting
# a = np.arange(8)
# splt = np.split(a,4)
# arr_splt = np.array_split(a,3)

# print(splt)
# print(arr_splt)

# 17/3/26

# arr = np.array([0,12,14,10,16,18])
# print(np.sort(arr))
# print(np.argsort(arr))

# indices = np.where(arr > 15)
# print(indices)

# print(np.nonzero(arr)) 
# print(np.any(arr > 15))
# print(np.all(arr > 11))

# print(np.clip(arr,12,16))

# 20/3/26

# CASE STUDY :

prices = np.array([100,200,150,300,np.nan,250])

quantity = np.array([10,5,8,3,7,6])

print(np.isnan(prices))
avg_price = np.nanmean(prices)
print(avg_price)

prices = np.where(np.isnan(prices),avg_price,prices)
print(prices)

total_revenue = prices * quantity
print(total_revenue)

# highest selling product

print(np.argmax(total_revenue))
print(total_revenue[np.argmax(total_revenue)])