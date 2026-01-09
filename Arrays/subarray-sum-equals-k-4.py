def subarraySum(nums, k):
    count = 0
    curr_sum = 0
    mp = {0: 1}

    for num in nums:
        curr_sum += num
        count += mp.get(curr_sum - k, 0)
        mp[curr_sum] = mp.get(curr_sum, 0) + 1

    return count
