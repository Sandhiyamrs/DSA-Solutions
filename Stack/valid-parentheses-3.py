def is_valid(s):
    stack = []
    match = {')':'(', ']':'[', '}':'{'}

    for ch in s:
        if ch in match.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()

    return not stack
