print("0 Dimensional Array")
array = np.array('A')
print(np.ndim(array))

print("1 Dimensional Array")
array = np.array(['A','B','C','D','E'])
print(np.ndim(array))

print("2 Dimensional Array")
array = np.array([['A','B','C','D','E'],['F','G','H','I','J']])
print(np.ndim(array))
print(np.shape(array))
print("\n")

print("Accessing element with index")
print(array[0][3]) # Different ways to access element
print(array[1,3])

print(array[0,0]+array[1,1])
