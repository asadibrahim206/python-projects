import practise

print(practise.name)
#BEGINERS 

#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# num1 = 3
# num2 = 2

# if num1 * num2 < 1000:
#     print("the mulitiplication is : " ,num1 * num2)
# else: 
#     print("the sum is : ", num1 + num2)

#Exercise 2: Print the Sum of a Current Number and a Previous number


# prev_num = 0
# for num in range(10):
#     print(f"The current number is : {num} and the previous number is {prev_num} and the sum is : {num + prev_num}")
#     prev_num = num

# Exercise 3: Print characters present at an even index number

# string = input("ENTER AN STRING : ")

# for chr in range(len(string)):
#     if chr % 2 == 0:
#         print(string[chr])
#     else
#         print("noe even")

mydict = {'a': 100, 'b':200, 'c':300}

for item in mydict.items():
    print(item)