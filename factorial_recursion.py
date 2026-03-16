# factorial of number 5 is ie 5! = 5*4*3*2*1 = 120

# number = int(input("Enter a number: "))
# factorial = 1

# if number < 0:
#     print("there is no factorial of number less than 0")

# elif number == 0 or number == 1:
#     print("The factorial of number is 1")

# else:
#     for i in range(1, number+1):
#         factorial*=i
#     print(f"The factorial of number {number} is {factorial}")

# code for factorial using recursion

number = int(input("Enter a number: "))

def factorial(number):
    if number<0:
        print("There is no factorial of number less than 0")
    elif number == 0 or number ==1:
        return 1
    else:
        return number*factorial(number-1)

print(f"The factorial of number {number} is {factorial(number)}")

# time complexity o(n)
# space complexity 0(n) stack space