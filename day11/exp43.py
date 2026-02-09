# Create a NumPy array and find the second largest element.
import numpy as np 
arr = np.array([10,45,20,8,30])
largest = arr[0]
second_largest = arr[0]
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest element: ", second_largest)