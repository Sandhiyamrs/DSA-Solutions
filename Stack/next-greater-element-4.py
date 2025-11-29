def next_greater_element(nums):
    res = [-1] * len(nums)
    stack = []  # indexes of decreasing elements

    for i, val in enumerate(nums):
        while stack and nums[stack[-1]] < val:
            idx = stack.pop()
            res[idx] = val
        stack.append(i)

    return res
