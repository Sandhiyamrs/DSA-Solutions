from collections import deque

def max_sliding_window(nums, k):
    if not nums or k == 0:
        return []

    dq = deque()  # stores indices, decreasing values
    res = []

    for i, n in enumerate(nums):
        # remove indices out of window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # maintain decreasing order
        while dq and nums[dq[-1]] < n:
            dq.pop()
        dq.append(i)
        # append max once first window completed
        if i >= k - 1:
            res.append(nums[dq[0]])

    return res
