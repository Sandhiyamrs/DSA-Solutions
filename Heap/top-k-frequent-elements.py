import heapq
from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
