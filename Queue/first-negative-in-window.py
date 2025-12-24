from collections import deque

def firstNegativeInWindow(arr, k):
    q = deque()
    res = []

    for i in range(len(arr)):
        if arr[i] < 0:
            q.append(i)

        if q and q[0] <= i - k:
            q.popleft()

        if i >= k - 1:
            res.append(arr[q[0]] if q else 0)

    return res
