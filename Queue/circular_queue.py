class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.q = [-1]*k
        self.front = self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front
