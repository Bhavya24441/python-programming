
#Question1: Check if string is palindrome
#Solution:
text = "madam"

reversed_text= text[::1]
if text == reversed_text:
    print("Plaindrome")
else:
    print("Not palindrome")




#Question2: Sum of all even numbers in a list
#Solution:
numbers = [1,2,3,4,5,6,7,8]
even_sum = 0
for num in numbers:
    if num %2 == 0:
        even_sum += num
print("Sum of even numbers = ", even_sum)


#Question3:Find Factorial of a Number (Using Loop)
#Solution: 

num = 5
fact = 1
for i in range(1, num +1):
    fact *= i
print("Factorial=", fact)


#Question5: Print Multiplication Table of a Number
#Solution:
num = 9
for i in range(1,11):
    result = num * i 
    print(num, "x", i, "=", result)