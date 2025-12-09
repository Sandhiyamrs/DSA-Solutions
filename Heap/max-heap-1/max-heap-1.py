import heapq

def max_heapify(nums):
    max_heap = [-n for n in nums]  # invert values to use min-heap as max-heap
    heapq.heapify(max_heap)
    sorted_nums = [-heapq.heappop(max_heap) for _ in range(len(nums))]
    return sorted_nums

# Example usage
nums = [3,1,4,1,5,9,2]
print("Output:", max_heapify(nums))
