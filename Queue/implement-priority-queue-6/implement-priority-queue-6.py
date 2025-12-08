import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))

    def pop(self):
        return heapq.heappop(self.heap)[1] if self.heap else None

    def peek(self):
        return self.heap[0][1] if self.heap else None

# Example usage
pq = PriorityQueue()
pq.insert("Task1", 2)
pq.insert("Task2", 5)
print("Peek Output:", pq.peek())
print("Pop Output:", pq.pop())
print("Pop Output:", pq.pop())
