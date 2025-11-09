import numpy as np

rng = np.random.default_rng()
print("Random number generated: ",rng.integers(low=1, high=7))
print("Random matrix generated: \n",rng.integers(low=1, high=101, size=(3,2)))
print("\n")

print("Generate random number between 0-1:",np.random.uniform())
print("Generate random number between 0-1:\n",np.random.uniform(low=1, high=10, size=(2,2)))
print("\n")

rng = np.random.default_rng()
array = np.array([1,2,3,4,5])
print("Actual array: ",array)
rng.shuffle(array)
print(array)
