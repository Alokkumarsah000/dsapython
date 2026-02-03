# what is recursion?
# when a function calls itself then it is called recursion

# two types of recursion -> head and tail recursion

# example of head recursion
count = 0

# def printingname(count):
#     if count == 4:
#         return
#     print("hello i am sinister")
#     count +=1
#     printingname(count)

# printingname(count)


# example of tail recursion

def printingame(count):
    if count ==4:
        return
    count +=1
    printingame(count)
    print("hello thanos")

printingame(count)