#Q1 - Count digits and letters separately
#Solution-
# text = "abvc13413adsf5234"
# count_digits= 0
# count_letters = 0 
# for i in text:
#     if i.isalpha():
#         count_letters = count_letters + 1
#     else:
#         count_digits = count_digits + 1
# print("The number of letters are: ", count_letters)
# print("The number of digits are: ", count_digits)







#Q2- Find all numbers greater than the average
#Solution-

# numbers = [10, 20 ,30, 40,50,60]
# average = sum(numbers) / len(numbers)
# for i in numbers:
#     if i > average:
#         print("The numbers are greater than the average are: ", i)



#Q3- Check if a string has all unique characters
#Solution- 
# text = "Hello wolrd "
# unique = True
# for ch in text:
#     if text.count(ch)> 1 :
#         unique = False 

# if unique:
#     print("All characters are unique")
# else:
#     print("All characters are not uniqe")








#Q4- Rotate a list by 1 position to the right 
#Solution- 

# numbers = [1,2,3,4,45,6,7,5,4]
# last = numbers[-1]
# new_list = [last]

# for i in range(len(numbers)-1):
#     new_list.append(numbers[i])
# print(new_list)





#Q5- Find the first non-repeating character
#Solution-
text = "adf aadsfasdf asdfjasd fjaldsf"
for ch  in text:
    if text.count(ch) == 1:
        print("First non repeating character is:", ch)
        break
