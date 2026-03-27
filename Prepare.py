# list = [
#  [78,82,90],
#  [65,70,72],
#  [88,91,85]
# ]

# print(list[1][2])



# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# for row in matrix:
#     for element in row:
#         print(element)




# records = [(101,"Aman",78),(102,"Neha",91),(103,"Raj",65)]
# for roll,name,marks in students:
#     if roll == 102:
#         print(name)





# records = {
# 101: {"name":"Aman","marks":78},
# 102: {"name":"Neha","marks":91}
# }

# for each in records:
#     if each == 101:
#         print(records[each])



# list = [1,2,3,4,5,6,7,8,9,10]
# result = [x*x for x in list ]
# print(result)



# result = [x for x in range(1,21) if x%2==0]
# print(result)


# words = ["python","ai","data","science"]
# result = [len(word) for word in words if len(word)>3]

# print(result)

# nums = [1,2,2,3,4,4,5]
# print(len(set(nums)))

# nums = [1,1,2,3,3,4,4,5]
# print(set(nums))


# l= "Education"
# for ch in l:
#     if ch in "aeiouAEIOU":
#         print(ch)



# words = ["apple","sky","orange"]
# count = 0 
# for word in words:  
#     for ch in words:
#         if ch in "aeiouAEIOU":
#             count = count +1
# print(count)


# capial = "Hello PYTHON World"
# for ch in capial:
#     if ch.isupper():
#         print(ch)




# l = "apple|banana|mango"
# result = l.split("|")
# print(result)


# list = [1,2,3]
# list[0]=4
# print(list)

# string= "Hellow world"
# string[0]= "Hi"
# print(string)



# def normalize_text(s):
#     s = s.lower().split()
#     cleaned = ""

#     for s in normalize_text(s):
#         if s.isalnum() or ch == " ":
#             cleaned+=ch
#         else:
#             cleaned+= " "

#     tokens = cleaned.split()
#     return tokens 



# def normalize_tokens(s):
#     s = s.lower().split()
#     cleaned = ""

#     for s in normalize_tokens(s):
#         if s.isalnum() or ch =" ":
#             cleaned += ch
#         else:
#             cleaned =""
#     tokens = cleaned.split()
#     return tokens



# nums = [10,20,30,40,50]
# print(nums[0])
# print(nums[-1])
# print(nums[2])


# nums = [1,2,3,4,5]
# print(nums[::-1])


# nums = [1,2,3,4,5]
# nums.reverse()
# print(nums)


# num = int(input("Enter a number"))
# sum = 0 
# temp =num 
# while temp>0:
#     digit = temp%10
#     sum =sum+ digit**3
#     temp = temp//10
# if sum == num:
#     print("adf")
# else:
#     print("not ")




# nums = [153,370,123,407,89]
# sum = 0 
# temp = sum
# while temp>0:
#     digit = temp%10
#     sum = sum + digit**3
#     temp = temp//10
# if sum == nums:
#     print("Armstrong number")
# else:
#     print("Not a armstorng number")


















# nums = [153,370,123,407,89]
# for num in nums:
#     sum = 0
#     temp = sum
# while temp> 0 :
#     digit = temp % 10
#     sum = sum + digit**3
#     temp = temp//10
# if sum == nums:




# result = lambda x: x*x 
# print(result(5))



# result = lambda x: x %10
# print(result(59))


# nums = [1,2,3,4,5] 
# result = list(map(lambda x: x*x, nums))
# print(result)


# li = ["python","ai","data"]
# result=list(map(lambda x : x.upper(), li))
# print(result)


# li = [3,12,7,20,5]
# result = list(filter(lambda x: x >10, li))
# print(result)



# li = [5,-2,7,-1,3,200]
# for ch in li:
#     if ch>0 and ch<101:
#         print(ch)




# record = "101,Aman,78,A"
# roll, name,marks,seciton = records.split(",")
# result = {
#     int(roll): {
#         "name" = name
#         "marks" = marks
#         "seciton" = section

#     }
# }

# print(result)

# records = ["101,Aman,78,A","102,Neha,91,B"]
# roll, name,marks, seciton= records.split(",")
# result={
#     int(roll)= {
#         name
#     }
#     int(roll)



l = "asdfasfh aspdhfpas dhf"
count = 0
for ch in l:
    if set(ch):
        count = count +1
print(count)