def subsets(nums):
    res = [[]]
    for num in nums:
        res += [curr + [num] for curr in res]
    return res

# Example usage
nums = [1,2,3]
print("Output:", subsets(nums))
