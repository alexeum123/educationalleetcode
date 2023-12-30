#maximum subarray

def maxSubArray(nums): #return int
    dp = [0] * len(nums)      
    dp[0] = nums[0]

    for i, val in enumerate(nums):
        dp[i] = max(val, dp[i-1] + val)
    
    return max(dp)

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
print(maxSubArray(nums))


            

  