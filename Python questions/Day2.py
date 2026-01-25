#Bhavya Jain 590024441
# Question 1: Count numbers greater than 10 in a list
#Solution:

# numbers = [54,5634,2345,24,545,64,35,1,1,324,5,6544,5672,5423,4]
# count = 0
# for i in numbers:
#     if i> 10:
        
#         count = count + 1
# print("The count of numbers greater than 10 in the list is:", count)

 






#Question 2 : Find sum of only even numbers in a list
#Solution:
# numbers= [1,2,3,4,4,56,7,7,8,8,9,97,234,2,341,341,45,36,364,67,2,2,2,2,6]
# even_sum = 0
# for i in numbers:
#     if i % 2 == 0:
#         even_sum = even_sum +i

# print("The sum of even numbers in the list is:", even_sum)










#Question 3: Count vowels and consonants in a string
#Solution:
# string= "Hello world this is Bhavya Jain"
# count_constants = 0
# count_vowels =0
# vowels= "a","e","i","o","u","A","E","I","O","U"
# for char in string:
#     if char in vowels:
#         count_vowels = count_vowels +1
    
#     else:
#         count_constants = count_constants +1

# print("The count of vowels in the string is:", count_vowels)
# print("The count of consonants in the string is:", count_constants)








#Question 5: Remove vowels from a string
#Solution:
# string = "quick brown fox jumps over the lazy dog"
# vowels= "a","e","i","o","u","A","E","I","O","U"
# new_string= ""
# for char in string:
#     if char not in vowels:
#         new_string = new_string + char

# print("String after removing vowels is:", new_string)








#Question 6: Find second largest number in a list
#Solution:
# numbers = [10,20,345,4353,25,234,23,4312,4,1234,356,634]
# largest_number = max(numbers)
# print("The largest number in the list is:", largest_number)



#Question 7: Count frequency of each number (dictionary)

#Solution:
# numbers = [1,2,3,4,4,5,5,6,7,7,8,97,34,32,1324,245,35,6467,567,35,6234,5]
# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1
# print("Frequency of each number in the list is:", frequency)









#Question 8: Reverse each word in a sentence

#Solution:
# string = "Hello world this is Bhavya Jain"
# words = string.split()
# reversed_words = []
# for char in words:
#     reversed_words.append(char[::-1])
# reversed_string = ' '.join(reversed_words)
# print("String with each word reversed is:", reversed_string)







# Question 9: Check if two strings are anagrams
#Solution:
# string_1 = "Hello world thsi is bhayva jain"
# string_2= "jain bhavya is this world Hello"
# if sorted(string_1) == sorted(string_2):
#     print("The two strings are anagrams.")
# else:
#     print("The two strings are not anagrams.")












#Question 10 : Count how many words start with a vowel 

#Solution:
# string = "Apple and everyhing is a fruit but i dont knwo that a is a vowel"
# count = 0 
# vowels= "a","e","i","o","u","A","E","I","O","U"
# words = string.split()
# for char in words:
#     if char[0] in vowels:
#         count = count + 1
# print("The count of words starting with a vowel is:", count)
