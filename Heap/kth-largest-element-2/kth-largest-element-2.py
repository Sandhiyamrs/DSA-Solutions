import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example usage
nums = [3,2,1,5,6,4]
k = 2
print("Output:", kth_largest(nums, k))
