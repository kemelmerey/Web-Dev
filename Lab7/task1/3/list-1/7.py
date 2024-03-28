def max_end3(nums):
    n = len(nums)-1
    x = nums[0]
    if nums[0] > nums[n]:
        x = nums[0]
    else:
        x = nums[n]
    
    for i in range(3):
        nums[i] = x
        
    return nums
    