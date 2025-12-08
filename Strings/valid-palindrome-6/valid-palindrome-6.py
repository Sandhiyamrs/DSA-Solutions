def isPalindrome(s):
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]

# Example usage
s = "A man, a plan, a canal: Panama"
print("Output:", isPalindrome(s))
