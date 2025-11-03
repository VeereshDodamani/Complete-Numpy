import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(array)
print("\n")

# array[start:end:step]
print("Accessing first row")
print(array[0])

print("Accessing last row")
print(array[-1])
print("\n")

print("Using start:end command")
# Last element is exclusive, not included
print("Accessing 0:3")
print(array[0:3])
print("Accessing 1:4")
print(array[1:4])
print("\n")

print("Using start:end:step command")
# Step means skip at rotation
print(array[0:4:2]) # 2 means skip the 2nd row which comes
