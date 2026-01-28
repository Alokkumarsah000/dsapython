# how to store frequency in dictionary in python

# nums = [1,2,3,3,2,1,3,3,2,5,1]   ->   {1: 3, 2: 3, 3: 4, 5: 1}

# nums = [1,2,3,2,1,2,4,2,5]

# store_in_dict = dict()

# for i in range(0, len(nums)):
#     if nums[i]  in store_in_dict: # o(1)
#         store_in_dict[nums[i]] +=1 # o(1)
#     else:
#         store_in_dict[nums[i]] = 1 

# print(store_in_dict)

# time complexity = o(n)


nums = [1,2,3,2,2,1,3,4,2,3,2,4]

no = len(nums)

hash_map = dict()

for i in range(0, no):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) +1

print(hash_map)