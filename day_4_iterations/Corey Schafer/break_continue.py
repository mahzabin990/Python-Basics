nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        break # it means after getting 3 it won't iterate through the list anymore!
    print(num)

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!')
        continue # it means after getting 3 it will iterate through the list anymore!
    print(num)