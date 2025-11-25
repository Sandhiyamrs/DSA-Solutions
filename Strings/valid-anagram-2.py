def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
