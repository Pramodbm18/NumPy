# NumPy Arrays Creation
# NumPy provides several functions to create arrays with specific patterns or values. Here are some common methods for creating NumPy arrays:
# 1. Using np.array() -> create an array from a list or tuple.
# 2. Using np.arange() -> create an array with a range of values.
# 3. Using np.linspace() -> create an array with evenly spaced values between a specified
# 4. Using np.logspace() -> create an array with logarithmically spaced values between a specified range.
# 5. Using np.zeros() -> create an array filled with zeros.
# 6. Using np.ones() -> create an array filled with ones.
# 7. Using np.full() -> create an array filled with a specified value.
# 8. Using np.empty() -> create an uninitialized array (values will be random).
# 9. Using np.random.rand() -> create an array with random floats between 0 and 1.
# 10. Using np.random.randn() -> create an array with random floats from a standard normal distribution.
# 11. Using np.random.randint() -> create an array with random integers within a specified range.

import numpy as np
range = np.arange(1,10)
print(range)
arr = np.linspace(0,1,5) #line space
print(arr)
ar = np.logspace(1,3,3) # logarithmic scal
print(ar)
# Zeros array full of zeros
arr = np.zeros(5)
print(arr)
arr = np.zeros([2,3])
print(arr) 
arr = np.ones([4,4], dtype=int) # array full of ones
print(arr)
arr = np.full(10,2) # -> create an array full of any value
print(arr)
arr = np.full([2,4],7) # [row, column], default value
print(arr)
arr = np.empty([2,3]) # Uninitialized array -> create an array without setting any values
print(arr)
arr = np.random.rand(2,3) # Random floats (0 to 1)
print(arr)
arr = np.random.randn(2,3) # random floats from standard normal distribution
print(arr)
arr = np.random.randint(10,100) # random integer
print(arr)
arr = np.random.randint(10,100, size = (3,4)) # create a random integer in matrix
print(arr)

#  NumPy Data Type and Type Casting

a = np.array([1,2,3,4,5])
print(a)
print(type(a))
lst = ["string",1,2,3,4.4,5]
arr = np.array(lst)
print(arr) 
arr = np.array([1,2,34,4,5]) # int64
print(arr.dtype)
arr = np.array([1,2,3.4,4,5]) # float64
print(arr.dtype)
arr = np.array(["1","2",34,4,5]) # string64
print(arr.dtype)
arr = np.array([1,2,34,4,5], dtype = np.float64) # float64
print(arr.dtype)
arr = np.array([1,2,34,4,5], dtype = np.float32) # float32
print(arr.dtype)
arr = np.array([1.2,2,3.4,4,5], dtype = np.int64) # int64
print(arr.dtype)
print(arr) # [1,2,3,4,5] create a integer lost a decimal values

# Type Costing -> astype()

arr = np.array([1,2,3])
print(arr.dtype) # int64
new_arr = arr.astype(np.float64) # this is convert integer to float 
print(new_arr.dtype) # float64 
new2_arr = new_arr.astype(np.int64) # This is convert float to integer
print(new2_arr.dtype) # int64

# Type casting errors:
try:
    arr = np.array(["1","2","hello"]) # This is not convert string to integer becuse int() with base 10
    arr2 = arr.astype(np.int64)
    print(arr2.dtype)
except Exception as e:
    print(f"Error : {e}") # Error : invalid literal for int() with base 10: np.str_('hello')

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr.ndim) # .ndim is a how many functions in array -> (2)
print(arr.shape) # .shape is a how many Row's and Column's -> (2 rows and 3 columns)
print(arr.size) # .size is a how many size in an array -> (6)
print(arr.itemsize) # .itemsize is a how much requred memory in an array -> (8)

# Array Reshaping -> Reshape, Ravel, Flatten

# Reshape
arr = np.array([1,2,3,4,5,6])
reshape = arr.reshape(3,2) # This is changing the data, and reshape. the array in 3 Row's and 2 Column's -> [[1 2] [3 4] [5 6]]
print(reshape)
reshape2 = reshape.reshape(2,3)# This is changing the data, and reshape. the array in 2 Row's and 3 Column's -> [[1 2 3] [4 5 6]]
print(reshape2)

# Ravel -> convert is 1D array
ravel = reshape2.ravel()
ravel [0] = 100
print(ravel)
print(reshape2)

# Flatten -> to 1D array
# -> return a copy of the array
flat = reshape2.flatten()
print(flat)
flat [0] = 1
print(flat)

# Arithmetic operations on Array

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a+b) # Addition
print(a-b) # Subtractor
print(a*b) # Multiplication
print(a/b) # Division
print(a//b) #floar division
print(b%a) # Modules -> remainder
print(a**2) # Exponent -> power

# Universal Function -> ufuncs
arr = np.array([1,4,9,16])
# Square root -> np.sqrt()
print(np.sqrt(arr))

# Exponential -> np.exp -> e^x -> x is any integer
print(np.exp([1,2]))

# Sine fuction -> np.sin
angles = np.array([0, np.pi/2,np.pi])
print(np.sin(angles))

# Indexing and slicing

a = [0,1,2,3,4,5,6]
print(a[0:4]) # slicing
print(a[::-1]) # reverse
print(a[-1]) # -ve indexing

# Multi dimentional slicing

matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(matrix[0:2]) # [[1 2 3]  [4 5 6]]
print(matrix[0:2, 0:2]) # [[1 2] [4 5]]

# Index Arrays -> Advanced Indexing
# np.take -> built in function to perform indexing and slicing
arr = np.array([10,20,30,40,50])
ind = [0,2]
print(np.take(arr,ind))

# Iterating with nditer()

arr = np.array([[1,2],[3,4]])
for x in np.nditer(arr):
    print(x,end=" ")

# Ndenumerate() -> both index + value

for ind, x in np.ndenumerate(arr):
    print(f"\n{ind}, {x}")

# Views vs Copies

arr = np.array([1,2,3,4,5])
view = arr[1:3]
print(view)
view [0] = 200
print(view)
print(arr)

# Copy
copy = arr[1:3].copy()
print(copy)
print(arr)

# Transpose of a Matrix
arr = np.array([[1,2],[3,4]])
print(arr) # This is orginal elements
print(arr.transpose()) # This is Transpose elements

# Swapaxes -> swap 2 specific axes in a matrix.
arr = np.array([[[1,2],[3,4]]])
print(arr.shape)
swap = np.swapaxes(arr,0,1)
print(swap.shape)

# Concatenation and Stacking in NumPy Arrays
# Concatenation
a = np.array([1,2])
b = np.array([3,4])
combine = np.concatenate((a,b))
print(combine)

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
print(np.vstack((arr1,arr2))) # Vertical stack
print(np.hstack((arr1,arr2))) # Horizental stack
print(np.stack((arr1,arr2), axis = 0))
print(np.stack((arr1,arr2), axis = 1))

# Splitting Arrays:

arr1 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr1)
print(np.split(arr1, 2)) # Split arrays in 2 paths

# Repeat Vs Tile in NumPy Arrays
arr = np.array([1,2,3])
print(np.repeat(arr,2)) # Each elements repeated twice
print(np.repeat(arr,3)) # Each elements repeated thrice

# tile -> repeat my whole array
print(np.tile(arr, 2))

# Aggregate Functions:
arr = np.array([1,2,3])
print(np.sum(arr))
print(np.mean(arr)) # Find the Mean value
print(np.median(arr)) # Find the Median value
print(np.std(arr)) # Find the standard diviation value
print(np.var(arr)) # Find the variance value
print(np.min(arr)) # Find the minimum value
print(np.max(arr)) # Find the maxmum value

print(matrix)
print(np.sum(matrix, axis = 1)) # Add row wise
print(np.sum(matrix, axis = 0)) # add column wise

# Cumulative Operations -> running total
print(arr) # [1,2,3]
print(np.cumsum(arr)) # [1,1+2=3,1+2+3=6] -> [1,3,6]
print(np.cumprod(arr)) # 1,1*2=2,1*2*3=6 -> [1,2,6]

# Where:
result = np.where(arr <2, "low","high")
print(result)

# argwhere: row-column positions for 2 arrays
arr = np.array([10,25,35,50])
print(np.argwhere(arr>20))

# Masking in Arrays
mask = np.logical_and(arr>15,arr<35)
print(mask)

print(matrix)
print(np.argwhere(matrix > 5))

# Broadcasting in NumPy Arrays
 
image = np.array([[200,150],[100,250]])
brightness = image + 50
print(image)
print(brightness)

# Vectorization:
# np.vectorize() -> convert a regular function to be applied on an array.

def square(x):
    return x*x
vfunc = np.vectorize(square)
arr = np.array([100,2,3,4,5,6])
print(arr)
print(vfunc(arr))

# Dealing with missing values.
# np.nan -> not a number.
a = np.array([1,2, np.nan,4])
# np.inf and -np.inf -> positive and negative infinites.
# np.isnan
# np.isinf
# np.isfinite
# --> These are the function sed to detect any values, infinite value or fnite value.

print(np.isnan(a))
b = np.array([1,np.nan,np.inf,10.2,40])
print(np.isinf(b))
new_b = np.nan_to_num(b) # Remove Nan / infinite values.
print(new_b)

