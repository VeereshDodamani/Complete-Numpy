import numpy as np

# Broadcasting allows numpy to perform operations on arary
# with different shapes by virtually expanding dimensions
# so they can match the larger array's shape

# The dimensions have the same size
# or
# One of the dimension has a size of 1


array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])
print("Shape of both the arrays")
print(array1.shape)
print(array2.shape)
print("\n")

print("Multiplication of both arrays")
print(array1 * array2)

array3 = np.array([[1,2,3,4,5]])
array4 = np.array([[1],[2],[3],[4],[5]])
print("Shape of both the arrays")
print(array3.shape)
print(array4.shape)
print("\n")

print("Multiplication of both arrays")
print(array3 * array4)
