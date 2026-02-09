# Create a NumPy array and count how many elements are even and odd.
import numpy as np 
arr = np.array([1,2,3,4,5,6])
even_count = 0
odd_count =0
for num in arr:
    if num % 2 == 0:
        even_count +=1
    else:
        odd_count += 1
print("Even numbers: ", even_count)
print("Odd numbers: ", odd_count)