def twoSum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        if target - num in mp:
            return [mp[target - num], i]
        mp[num] = i
