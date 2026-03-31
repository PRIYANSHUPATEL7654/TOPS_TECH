import numpy as np
import random
# 14/3/26
# Numpy_2.ipynb
# 1. Create two arrays: a = [5, 10, 15] b = [1, 2, 3] Perform element-wise addition and multiplication.
# a = np.array([5, 10, 15] )
# b = np.array([1, 2, 3])
# print("Addition : ",a+b)
# print("Addition : ",np.sum(a+b)) # it gives sum of sum of 2 array elements
# print("Multiplication : ",a*b)

# 2. Given array: arr = [4, 8, 12, 16] Extract elements greater than 10.
# arr = np.array([4, 8, 12, 16])
# print(arr[arr > 10])

# 3. Create a 2×3 array of ones and add 5 to every element using broadcasting.
# arr = np.ones((2,3))
# print(arr + 5)

# 4. Given array: arr = [10, 20, 30, 40] Compute:
# -> Mean
# arr = np.array([10,20,30,40])
# print(arr.mean())
# # -> Sum
# print(arr.sum())
# # -> Maximum
# print(arr.max())

# 5. Convert 45 degrees into radians and compute its sine value.
# 6. Create two arrays: a = [2, 4, 6, 8] b = [1, 2, 3, 4] Perform floor division and modulus operations.
# a = np.array([2, 4, 7, 8])
# b = np.array([1, 2, 3, 4])
# print((a//b))
# print((a%b))

# 7. Generate a 3×3 random integer matrix between 1 and 20. Find its standard deviation and variance.
# a = np.random.randint(1,20,(3,3))
# print(a)
# print(np.std(a))
# print(np.var(a))

# 8. Create an array from 1 to 9 and reshape it into 3×3. Compute cumulative sum (cumsum).
# a = np.arange(1,10)
# print(a.reshape(3,3))
# print(np.cumsum(a))

# 9. Create array: arr = [-3, -1, 0, 1, 3] Apply:
# -> Square
# arr = np.array([-3, -1, 0, 1, 3])
# print(np.square(arr)) # or print(arr**2)
# # -> Square root (only valid values)
# print(np.sqrt(arr[arr >= 0]))

# 10. Using logical operations: Given array: arr = [5, 10, 15, 20, 25] Extract values between 10 and 20 inclusive.
# arr = np.array([5,10,15,20,25])
# print(arr[np.logical_and(arr >= 10,arr <= 20)])

# 11. Create a 3×4 matrix using np.arange(). Add a 1D array [10, 20, 30, 40] using broadcasting.
# arr = np.arange(1,13).reshape(3,4)
# arr1 = np.array([10,20,30,40])
# print(arr + arr1)

# 12. Generate 1000 random numbers from normal distribution. Compute:
# # -> Mean
# a = np.arange(1,1001)
# print(np.mean(a))
# # -> Standard deviation
# print(np.std(a))
# # -> 95th percentile
# print(np.percentile(a,95))

# 13. Create two matrices: A (2×3) and B (3×2). Transpose A and verify its shape.
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1,2],[3,4],[5,6]])
# print(np.transpose(a))

# 14. Create array: arr = [1, 2, 3, 4] Compute:
# # -> Exponential of each element
# arr = np.array([1,2,3,4])
# print(np.exp(arr))
# # -> Natural log
# print(np.log(arr))
# # -> Log base 10
# print(np.log10(arr))

# 15. Create array: arr = [1.2, 2.5, 3.7, 4.1] Apply:
# # -> round()
# arr = np.array([1.2, 2.5, 3.7, 4.1])
# print(np.round(arr))
# # -> floor()
# print(np.floor(arr))
# # -> ceil() Explain differences based on output.
# print(np.ceil(arr))

# 17/3/26
# Numpy_3.ipynb
# 1. Create an array from 1 to 15. Split it into 5 equal parts.
# a = np.arange(1,16)
# print(np.split(a,5))

# 2. Create an array from 1 to 11. Split it into 4 parts using array_split().
# a = np.arange(1,12)
# print(np.array_split(a,4))

# 3. Given: arr = np.array([10, 20, 30, 40, 50]). Insert 25 at index 2.
# arr = np.array([10, 20, 30, 40, 50])
# print(np.insert(arr,2,25))

# 4. Given: arr = np.array([[1,2], [3,4]]) Insert a new row [5,6] at index 1.
# arr = np.array([[1,2], [3,4]])
# print(np.insert(arr,1,[5,6],axis = 0))

# 5. Given: arr = np.array([5, 10, 15]). Append 20 and 25 at the end.
# arr = np.array([5, 10, 15])
# print(np.append(arr,20))
# print(np.append(arr,25))

# 6. Given: arr = np.array([[1,2], [3,4]]). Append column [7,8] to this array.
# arr = np.array([[1,2], [3,4]])
# # newdata = np.array([[7,0],[8,0]]) # to add rows
# newdata = np.array([[7],[8]]) # to add column
# print(np.append(arr, newdata, axis=1))

# 7. Given: arr = np.array([100, 200, 300, 400, 500]) Delete:
# # -> a) Element at index 3
# arr = np.array([100, 200, 300, 400, 500])
# print(np.delete(arr,3))
# # -> b) First two elements
# print(np.delete(arr,(0,1)))

# 8. Given: arr = np.array([[1,2], [3,4], [5,6]]). Delete the second row.
# arr = np.array([[1,2], [3,4], [5,6]])
# print(np.delete(arr,1,axis=0))

# 9. Create: arr = np.array([1,2,3,4]). Create:
# -> view_arr using view()
# arr = np.array([1,2,3,4])
# view_arr = arr.view()
# print(view_arr)
# # -> copy_arr using copy()
# copy_arr = arr.copy()
# print(copy_arr)
# # Modify arr[0] = 999
# arr[0] = 999
# print(arr)
# print(view_arr)
# print(copy_arr)
# Print all three arrays. Explain what happened.
# when modified arr, it also got modified in view_arr as it share same memory with the original array, and copy_arr is a copy of original arr so any changes made to original array does not affect the original one.

# 10. Create array from 1 to 6. Reshape it into 2×3 matrix. Change element at position (0,1) to 100.
# arr = np.arange(1,7).reshape(2,3)
# print(arr)
# arr[0,1] = 100
# print(arr)

# 11. Given: arr = np.array([[1,2,3], [4,5,6]]). Apply:
# arr = np.array([[1,2,3], [4,5,6]])
# print(arr)
# # -> flatten()
# f_arr = arr.flatten()
# print(f_arr)
# # -> ravel()
# r_arr = arr.ravel()
# print(r_arr)
# # Modify first element of both results. Observe difference.
# f_arr[0] = 10
# r_arr[0] = 20
# print(f_arr)
# print(r_arr)
# print(arr)
# Ravel is the view of the original array as the original also gets changed on changing r_arr(ravel arr), whereas flatten is the copy of the original array so any change done in it f_arr(flatten arr) does not change original array.

# 12. Create array from 1 to 12. Split into 3 equal parts. Delete last element from each part. Combine all remaining elements into a single array.
# arr = np.arange(1,13)
# a = np.split(arr,3)
# print(a)
# updated_arr = np.delete(a,[3],axis = 1)
# print(updated_arr)
# print(updated_arr.flatten())

# 17/3/26
# Numpy_3.ipynb
# 1. Create a 4*4 matrix using np.arange(1,17).
# -> Extract the second row.
# a = np.arange(1,17).reshape(4,4)
# print(a[1]) # or print(a[1,:])
# # -> Extract the last column.
# print(a[:,3])
# # -> Compute the mean of the entire matrix.
# print(np.mean(a))

# 2. Create array: arr = [5, 10, 15, 20, 25, 30]
# arr = np.array([5, 10, 15, 20, 25, 30])
# # -> Extract elements greater than 10 AND less than 30.
# print(arr[np.logical_and(arr<30,arr>10)])
# # -> Find their cumulative sum.
# print(np.cumsum(arr[np.logical_and(arr<30,arr>10)]))

# 3. Generate 10 random integers between 1 and 50.
# arr = np.random.randint(1,51,10)
# print(arr)
# # -> Sort them.
# print(np.sort(arr))
# # -> Return indices that would sort the original array.
# print(np.argsort(arr))
# # -> Find the 75th percentile.
# print(np.percentile(arr,75))

# 4. Create two 2*3 matrices.
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[10,20,30],[40,50,60]])
# -> Concatenate them row-wise.
# con = np.concatenate(a+b)
# print(con)
# # -> Then split the result into 2 equal parts.
# print(np.split(con,2))

# 5. Create array: arr = [1, 2, 2, 3, 4, 4, 5]
# arr = np.array([1, 2, 2, 3, 4, 4, 5])
# # -> Remove duplicate values.
# uni = np.unique(arr)
# print(uni)
# # -> Reverse the array using slicing.
# print(uni[::-1])
# # -> Compute standard deviation.
# print(np.std(uni))

# 6. Create a 5*5 matrix using np.arange(1,26).
# a = np.arange(1,26).reshape(5,5)
# # -> Extract all elements greater than 10 and less than 20.
# b = a[np.logical_and(a<20,a>10)]
# print(b)
# # -> Replace those values with 0 using boolean indexing.
# c = 0
# # -> Compute total sum of modified matrix.
# print(np.sum(c))

# 7. Generate 1000 random numbers from normal distribution.
# a = np.random.randn(1000)
# print(a)
# # -> Compute mean and standard deviation.
# print(np.mean(a))
# print(np.std(a))
# # -> Clip values between -1 and 1.
# b = np.clip(a,-1,1)
# print(b)
# # -> Count how many values were clipped.
# count = np.sum(a != b)
# print(count)

# 8. Create array: arr = [10, 20, np.nan, 40, 50, np.nan]
arr = np.array([10, 20, np.nan, 40, 50, np.nan])
# -> Compute mean ignoring NaN.
# -> Replace NaN values with 0.
# -> Compute new mean.

# 9. Create two matrices: A (3*3) using np.arange(), B (3*3) random integers between 1 and 10.
# a = np.arange(1,10).reshape(3,3)
# b = np.random.randint(1,10,9).reshape(3,3)
# print(a)
# print(b)
# # -> Perform element-wise multiplication.
# c = a*b
# print(c)
# # -> Compute 90th percentile of result.
# d = np.percentile(c,90)
# print(d)
# # -> Transpose the result.
# print(np.transpose(c))

# 10. Create array: arr = np.arange(1,21)
# -> Reshape into 4×5 matrix.
# arr = np.arange(1,21).reshape(4,5)
# print(arr)
# # -> Extract elements divisible by both 2 and 3.
# print(arr[np.logical_and(arr%2==0,arr%3==0)])
# # -> Insert value 999 at index 2.
# print(np.insert(arr,2,999))
# # -> Delete last element.
# print(np.delete(arr,-1))
# # -> Verify whether all remaining values are positive.
# print(np.all(arr[arr>=0]))