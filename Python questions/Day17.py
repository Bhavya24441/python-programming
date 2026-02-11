#Question1: WAP to check whether a number is present in a list or not.
#Solution:
# n = int(input("Enter number of elements:"))
# lst=[]
# for i in range(n):
#     lst.append(int(input()))
# search = int(input("Enter number to serach: "))
# found = False

# for num in lst:
#     if num == search:
#         found == True
# if found:
#     print("number found in list")
# else:
#     print("number not found in list")


#Question2: Create a tuple and print elements at even index positions.
#Solution:
# n = int(input("Enter the number of elements: "))
# t = ()

# for i in range(n):
#     t = t + (input(),)
# print("Elements at even index postions: ")
# for i in range(0, n, 2):
#     print(t[i])







#Question3: WAP to merge two lists into a single list.
# #Solution:
# n1 = int(input("Enter number of elements in list: "))
# list1= []
# for i in range(n1):
#     list1.append(input())
# n2 = int(input("Enter the number of elements in list: "))
# list2 =[]
# for i in range(n2):
#     list2.append(input())
# merged_list = list1 + list2
# print("Merged list = ", merged_list)




#Question4: Create a dictionary of students and display total number of students.
# #Solution: 
# n = int(input("Enter the number of studets: "))
# students = {}
# for i in range(n):
#     name = input("Enter student name: ")
#     age = int(input("Enter age: "))
#     students[name]= age
# count = len(students)
# print("Total number of students= ",count)