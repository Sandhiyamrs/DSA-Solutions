from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)

# Example usage
s = "listen"
t = "silent"
print("Output:", is_anagram(s,t))
