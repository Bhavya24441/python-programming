# #Question1: Find Second Smallest Number in a List
# #Solution:
# numbers = [8,3,5,1,9]

# unique_numbers = list(set(numbers))
# unique_numbers.sort()

# print("Second smallest =", unique_numbers)

# #Question2:Check if Two Strings are Rotations of Each Other
# #Solution:
# s1= "abcde"
# s2= "cdeab"

# if len(s1)== len(s2):
#     combined = s1 +s2

#     if s2 in combined:
#         print("Rotation")
#     else:
#         print("Not Rotation")
# else:
#     print("Not rotation")





# #Question3:Count Frequency of Each Character (Using Dictionary)
# #Solution:
# text = "banana"
# freq = {}
# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch]= 1
# print(freq)



# #Question4: Find Missing Number in a Sequence
# #Solution:
# numbers = [1,2,4,5]
# n = len(numbers) + 1
# expected_sum = n* (n+1)/2
# actual_sum = sum(numbers)
# missing = expected_sum - actual_sum
# print("Missing number = ", missing)