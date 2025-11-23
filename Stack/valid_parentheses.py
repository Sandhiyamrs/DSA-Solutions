def is_valid(s):
    stack = []
    pair = {')':'(', '}':'{', ']':'['}

    for ch in s:
        if ch in pair:
            if not stack or stack.pop() != pair[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
