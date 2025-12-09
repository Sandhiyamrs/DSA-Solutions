def single_number(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

# Example usage
nums = [4,1,2,1,2]
print("Output:", single_number(nums))
