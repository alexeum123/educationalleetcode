#find minimum in rotated sorted array

# def findRotations(nums): #returns int
#     for i in range(len(nums)):
#         if nums[0] <= nums[-1]:
#             return len(nums)
#         elif nums[i] <= nums[i-1]:
#             return i

# nums = [4,5,6,7,0,1,2]
# print(findRotations(nums))




# import math

# def findMin(nums): #returns int
#     #crunch method binary sort

#     l = 0 #first index
#     r = len(nums)-1 #last available index

#     #crunch with a loop, not recursion
#     while l<r:
#         m = (l + r) //2
#         if nums[m] <= nums[r]:   #midpoint valid order,
#             r = m                #scoot r left
       
#         else:                    #midpoint invalid order,
#             l = m+1              #scoot l right

#     return nums[l]               #moment of crossover   


def findMin(nums):
    l = 0
    r = len(nums)-1

    while l<r:
        m = (l+r)//2
        if nums[m]<=nums[r]:
            r = m
        else: 
            l = m+1
    
    return nums[l]


nums = [4,5,6,7,0,1,2]
print(findMin(nums))





