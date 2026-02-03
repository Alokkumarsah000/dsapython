# what is hashing?
# restoring value into some data structure like list,dictionary or set and the fetching it is called hashing


num = [1,2,3,1,3,3,6,8,9,5]         # 1<=n<=10           10^8 ->may be 

no_to_look_after = [22,3,2,4,56,1]  # if we use two for loop its time complexity would be 10^16 which would exceed 10^8 causing time limit exceed problem


hash_map = [0]*11

for number in num:
    hash_map[number]+=1

for no in no_to_look_after:
    if no < 1 or no > 10:
        print(0)
    else:
        print(hash_map[no])


# time complexity 0(m+n)