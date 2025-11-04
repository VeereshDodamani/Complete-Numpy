import numpy as np

# Scalar arithmetics
print("Scalar arithmetics")
array = np.array([1,2,3])
print("Actual Array")
print(array)
print("Adding 1")
print(array + 1)
print("Substracting 1")
print(array - 1)
print("Multiply by 2")
print(array * 2)
print("Divide by 4")
print(array / 4)


# Vectorised Math Function
print("Vectorised Math Function")
array = np.array([1.01,2.52,3.34])
print("Actual Array")
print(array)
print("Sqrt of the array")
print(np.sqrt(array))
print("Round off array")
print(np.round(array))
print("Round off array to floor")
print(np.floor(array))
print("Round off array to ceil")
print(np.ceil(array))
