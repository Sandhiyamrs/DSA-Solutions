class MyCircularDeque:
    def __init__(self, k):
        self.k = k
        self.q = []

    def insertFront(self, value):
        if self.isFull():
            return False
        self.q.insert(0, value)
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.q.append(value)
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.q.pop(0)
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.q.pop()
        return True

    def getFront(self):
        return self.q[0] if not self.isEmpty() else -1

    def getRear(self):
        return self.q[-1] if not self.isEmpty() else -1

    def isEmpty(self):
        return len(self.q) == 0

    def isFull(self):
        return len(self.q) == self.k
