def subarray_sum(nums, k):
    count = 0
    curr = 0
    seen = {0: 1}  # prefix sum frequencies

    for n in nums:
        curr += n
        need = curr - k
        count += seen.get(need, 0)
        seen[curr] = seen.get(curr, 0) + 1

    return count
