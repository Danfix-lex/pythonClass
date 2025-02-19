class TupleStack:
    def __init__(self):
        self.stack = ()

    def push(self, item):
        self.stack = self.stack + (item,)

    def pop(self):
        if not self.is_empty():
            popped_item = self.stack[-1]
            self.stack = self.stack[:-1]
            return popped_item
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        count = 0
        for _ in self.stack:
            count += 1
        return count