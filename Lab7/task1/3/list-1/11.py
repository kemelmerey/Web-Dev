def sum2(nums):
    res = 0
    n = len(nums)
    if n == 1:
        res = nums[0]
    elif n >= 2:
        res = nums[0] + nums[1]
        
    return res
