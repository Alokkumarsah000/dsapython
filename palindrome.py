# A palindrome is a word, phrase, number that reads the same backward as forward.
# Examples of palindromes: madam, racecar, 121, 12321

# check whether a given number is palindrome or not
number = 1221

original = number

lastDigit = 0
result = 0
# remaining_number = 0
while number > 0:
    lastDigit = number % 10
    result = (result * 10) + lastDigit
    number = number // 10
# if reversedNumber == number:
#     print("PALINDROME NUMBER")
# else:
#     print("NO PALINDROME NUMBER")
print("palindrome") if result == original else print("not palindrome")
