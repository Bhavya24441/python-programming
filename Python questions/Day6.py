#Print all numbers greater than 50 from a given list
#Solution:  

# numbers = [10, 55, 23, 67, 89, 45, 32, 76]
# for i in numbers:
#     if i > 50:
#         print(i)





#Count how many numbers are divisible by 4
#Solution:

# numbers = [12, 16, 25, 40, 55, 64, 78, 80]
# count = 0 
# for i in numbers:
#     if i % 4 == 0:
#         count = count + 1
# print("Count of numbers divisible by 4:", count)






#Remove spaces from a given string
#Solution:
# string = " hello world "
# no_space_string = string.replace(" ", "")
# print("String without spaces:", no_space_string)







#Count uppercase and lowercase letters in a string
#Solution:
# string = " Hello worLd this is Bhavya jain "
# upper_count = 0
# lower_count = 0
# for char in string:
#     if char.isupper():
#         upper_count = upper_count + 1
#     elif char.islower():
#         lower_count = lower_count + 1
# print("Uppercase letters:", upper_count)
# print("Lowercase letters:", lower_count)







#Check if list is sorted in ascending order
#Solution:
# numbers = [1, 2, 3, 4, 5, 6]
# is_sorted = True 
# for i in range(len(numbers)-1):
#     if numbers[i] > numbers[i +1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("List is sorted in ascending order")
# else:
#     print("List is not sorted in ascending order")









# Find product of numbers
#Solution:

numbers = [1, 2, 3, 4, 5, 6,7,7,8]
product = 1
for i in numbers:
    product = product * i
print("Product of numbers:", product)