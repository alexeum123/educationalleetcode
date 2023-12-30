#maximum product subarray

def maxProduct(nums): #return int
  dp = [0] * len(nums)
  dp[0] = nums[0] #if array of 1, that is its max

  for i in range(1, len(nums)):
    dp[i] = max(dp[i-1]* nums[i], nums[i])

    return max(dp)


# nums = [2,3,-2,4]
nums = [-2,0,-1]
print(maxProduct(nums))