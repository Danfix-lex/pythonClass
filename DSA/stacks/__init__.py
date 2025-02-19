class Stack:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.top < self.capacity - 1:
            self.top += 1
            self.stack[self.top] = item
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.is_empty():
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return item
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            return "Stack is empty"

    def is_empty(self):
        return self.top == -1

    def size(self):
        return self.top + 1

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", stack.size())
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack size after pop:", stack.size())
print("Is stack empty?", stack.is_empty())