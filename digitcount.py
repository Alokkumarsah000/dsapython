# no = 12345
# count = 0
# while no > 0:
#     count += 1
#     no = no // 10
# print("Number of digits:", count)

from math import *
no = 1453
count = int(log10(no)) + 1
print("Number of digits:", count)


# if iteration is depended on any number(in this case divided by 10) then its time complexity is o(logn(n))