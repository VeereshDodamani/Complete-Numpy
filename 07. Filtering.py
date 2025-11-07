# Filtering  = Refers to the process of selecting elements from an array that matches the condition

import numpy as np
ages = np.array([[23,19,22,20,25,18,16,56],[32,28,19,23,17,21,20,27]])

print("Teenagers")
teen = ages[ages<18]
print(teen)

print("Adults")
adults = ages[(ages>=18) & (ages<50)]
print(adults)

print("Seniors")
seniors = ages[(ages>50)]
print(seniors)

print("Even")
even = ages[(ages%2 == 0)]
print(even)

print("Odds")
odd = ages[(ages%2 == 1)]
print(odd)
print("\n")

print("Adults array")
adults = np.where(ages>=18,ages,-1)
print(adults)
