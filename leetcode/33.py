def search(nums, target): #return int
    l = 0
    r = len(nums) -1

    while l<r:
        m = (l+r)//2
        if nums[m] == target:
            return m

        if nums[m] <= nums[r]:
            r = m
        else:
            l = m+1

    return -1

nums = [8, 4,5,6,7,0,1,2]
print(search(nums, 8))



