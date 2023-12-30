#product of array except self
def productExceptSelf(nums): #return list
    numLength = len(nums)
    result = [1] * numLength   #ex [1, 1, 1, 1, 1]
    
    for i in range(1, numLength):
        result[i] = result[i-1] * nums[i-1]      #[1, 1, 2, 6]
                                                 #accumulation of forward multiply to index
    accumulator = 1
    for i in range (numLength-1, 0, -1):
        accumulator *= nums[i]
        result[i-1] *= accumulator
    
    return result


nums = [1,2,3,4]
output = [24,12,8,6]
print(productExceptSelf(nums))