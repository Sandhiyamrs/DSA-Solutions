def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

# Example usage
nums = [2,7,11,15]
target = 9
print("Output:", two_sum(nums, target))
