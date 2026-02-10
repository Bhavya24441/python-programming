#1.WAP to count the number of vowels in a given string using a list.
#Solution:
text = input("Enter a string: ")
vowels = ['a','e','i','o','u']
count = 0
for ch in text.lower():
    if ch in vowels:
        count +=1
print("Number of vowels=", count)



#2.Create a tuple and find the sum of all elements.
#Solution:
n = int(input("Enter number of elements: "))
t = ()
for i in range(n):
    t = t + (int(input()))
total = 0
for num in t:
    total += num
print("Sum of elements= ",total)


#3.WAP to find the frequency of each element in a list.
#Solution:
n = int(input("Enter the number of elements: "))
lst =[]
for i in range(n):
    lst.append(input())
freq = {}
for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print("Element frequency: ")
for item in freq:
    print(item, ":", freq[item])






#4.Create a dictionary of employees and display employees working in a given departments.
#Solution:
n = int(input("Enter number of employees: "))
emp = {}
for i in range(n):
    name = input("Enter employee name: ")
    dept = input("Enter department: ")
    emp[name] = dept
search = input("Enter department to search: ")
print("Employees in", search, "department: ")
for name in emp:
    if emp[name] == search:
        print(name)