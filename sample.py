nums = [1,2,3,4]

#for loop values in a reversed list
for num in reversed(nums):
    print(num)

#enumerate on its own is not reversiblee
#must turn enumerate into a list
for i, num in reversed(list(enumerate(nums))):
    print(i, num)