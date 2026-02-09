# print number from 1 to n using parameter recursion

# number = int(input("enter a number: "))

# def listingFunction(number, n):
#     if number == 0:
#         return
#     print(number)
#     listingFunction(number-1, n)


# listingFunction(20, 20)


def listingFuncion(i, n):
    if i>10:
        return
    print(i)
    listingFuncion(i+1, n)


listingFuncion(1, 10)