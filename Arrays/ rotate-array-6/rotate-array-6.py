def rotate(nums, k):
    n = len(nums)
    k %= n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

# Example usage
nums = [1,2,3,4,5,6,7]
k = 3
print("Output:", rotate(nums, k))
