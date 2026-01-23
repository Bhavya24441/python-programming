#Bhavya Jain 590024441
# Question 1: Write a Python program to find the sum of all numbers in a list.
#Solution
# numbers = [10,20,30 ,40, 50]
# total_sum = sum(numbers)
# print("Sum of all the numbers in the list is:", total_sum)



# Question 2: Write a Python program to find the largest number in a list.
#Solution:
# numbers = [100, 150, 200, 250, 300]
# largest = max(numbers)
# print("The largest number in the list is:", largest)







#Question 3: Write a program to count the number of vowels in a string.

#Solution:

# String_name= "Hello world this is Bhavya Jain"
# vowels= "a","e","i","o","u","A","E","I","O","U"
# count = 0
# for char in String_name:
#     if char in vowels:
#         count = count + 1
# print ("Number of vowels in the string is:", count)






# Question 4: Count Odd Numbers in a List

#Solution: 

# numbers = [1,2,3,4,4,5,5,6,7,7,8,97,34,32,1324,245,35,6467,567,35,6234,5]
# odd_count = 0 
# for i in numbers:
#     if i% 2 !=0:
#         odd_count = odd_count +1
# print("The count of odd numbers in the list is:", odd_count)







# Question 6: Find Average of Numbers

#Solution:
# numbers= [10,20,345,4353,25,234,23,4312,4,1234,356,634]
# total = 0 
# count = 0 
# for i in numbers:
#     total = total +i 
#     count = count + 1
# average = total / count
# print("The average of the numbers in the list is:", average)





# Question 7: Print Numbers Divisible by 3
#Solution:
# numbers = [10,23,33,45,60,72,81,95,102,115,123,135, 3,9,12,14,15,116]
# for i in numbers:
#     if i%3==0:
#         print(i)





# Question 8 : Count Spaces in a String
#Solution:
# string = "Hello world   this    is question 8"
# count = 0
# for char in string:
#     if char == " ":
#         count = count + 1
# print("The number of spaces in the string is:", count)






# Question 9 : Replace Vowels with *
#Solution:
# string = "This string will have its vowerls replaced with *"
# vowels = "a","e","i","o","u","A","E","I","O","U"
# new_string = ""
# for char in string:
#     if char in vowels:
#         new_string = new_string + "*"
#     else:
#         new_string = new_string +char
# print("The new string is:", new_string)



# Question 10: Remove Duplicates from List
#Solution:
# numbers =[1111,2,222,4,4,5,6,7,7,7,7,8,8,6,5,5,4,3,2,1,1111]
# duplicates_removed =[]
# for i in numbers:
#     if i not in duplicates_removed:
#         duplicates_removed.append(i)
# print("List after removing duplicates:", duplicates_removed)