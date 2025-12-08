def longestPalindrome(s):
    if not s:
        return ""
    start = end = 0
    for i in range(len(s)):
        for j in [0,1]:
            left, right = i, i+j
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start = left + 1
                end = right - 1
    return s[start:end+1]

# Example usage
s = "babad"
print("Output:", longestPalindrome(s))
