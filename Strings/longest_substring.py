def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        longest = max(longest, right - left + 1)
    return longest
