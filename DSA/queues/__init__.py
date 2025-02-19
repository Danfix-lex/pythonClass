class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def enqueue(self, item):
        self.rear += 1
        self.queue.insert(self.rear, item)

    def dequeue(self):
        if not self.is_empty():
            item = self.queue[self.front]
            self.front += 1
            return item
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            return "Queue is empty"

    def is_empty(self):
        return self.front > self.rear

    def size(self):
        return self.rear - self.front + 1