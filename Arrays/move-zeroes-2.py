def moveZeroes(nums):
    idx = 0
    for num in nums:
        if num != 0:
            nums[idx] = num
            idx += 1
    for i in range(idx, len(nums)):
        nums[i] = 0
