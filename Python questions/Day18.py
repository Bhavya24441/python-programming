#Question1 : WAP to count how many strings in a list have length greater than 4.

#Solution: 
# n = int(input("Enter number of words: "))
# lst = [input() for i in range(n)]
# count = 0
# for word in lst:
#     if len(word)> 4:
#         count +=1
# print("Words with lenght greater than 4 = ", count)




#Question2: Create a tuple and print all elements in uppercase.
# #Solution: 
# n = int(input("Enter the number of elements: "))
# t = tuple(input() for i in range(n))
# print("Elements in uppercase: ")
# for item in t:
#     print(item.upper())



#Question3 :WAP to create a list of numbers and print only odd numbers from it.
#Solution:
# n = int(input("Enter the number of elements: "))
# lst = [int(input()) for i in range(n)]
# print("Odd numbers are:")
# for num in lst:
#     if num % 2 !=0:
#         print(num)

#Question4: Create a dictionary of city names and their populations. Display the city with the highest population.
#Solution:
# n = int(input("Enter the number of cities: "))
# cities = {}
# for i in range(n):
#     name = input("Enter city name: ")
#     pop  = int(input("Enter population: "))
#     cities[name] = pop
# max_city = max(cities, key=cities.get)
# print("City with highest population=", max_city)