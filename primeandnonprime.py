# composite number -> a number greater than 1 and has more than 2 factors[that is 1 and number itself] 
# is called prime number
from math import sqrt
number = int(input("Enter a number : "))

# half_of_number = number//2

if number <= 1:
    print("neither prime nor composite number.")

is_prime = True

for x in range(2, int(sqrt(number))+1):
    if number % x == 0:
        is_prime = False
        break
if is_prime:
    print("prime number")
else:
    print("compostie number")




# number = int(input("Enter any number: "))

# result = []

# for i in range(1, int(sqrt(number)+1)):
#     if number % i == 0:
#         result.append(i)
#         if number // i != i:
#             result.append(number // i )


# print(sorted(result))

# time complexity -> 0(nlogn) + o(sqrt(n))