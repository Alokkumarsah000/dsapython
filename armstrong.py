# an armstrong number (also known as narcissistic number) is a number that is equals to the sum of 
# its digit each raised to the power of the number of digit

# 153-> 1^3+ 5^3+ 3^3 = 153 then armstrong number 

number = 153

result = number

number_of_digit = len(str(number))

total = 0

while number > 0:
    last_digit = number % 10
    total = total + (last_digit**number_of_digit)
    number = number // 10

print("armstrong number") if total == result else print('Not armstrong number')