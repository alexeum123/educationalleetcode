#twosum
def twoSum(nums, target):
    myDict = {}
    for i, val in enumerate(nums):
        if target-val in myDict:
           return myDict[target-val], i
        else:
           myDict[val] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
    

    