import numpy as np
# Aggregate function = summarise data and typically return a single value

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Actual Array")
print(array)
print("Sum of the array: ",np.sum(array))
print("Mean of the array: ",np.mean(array))
print("Standard deviation of the array: ",np.std(array))
print("Variance of the array: ",np.var(array))
print("Minimum element of the array: ",np.min(array))
print("Maximum element of the array: ",np.max(array))
