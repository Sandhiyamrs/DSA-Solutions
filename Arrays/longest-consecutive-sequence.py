def longestConsecutive(nums):
    s = set(nums)
    longest = 0

    for num in s:
        if num - 1 not in s:
            curr = num
            streak = 1
            while curr + 1 in s:
                curr += 1
                streak += 1
            longest = max(longest, streak)

    return longest
