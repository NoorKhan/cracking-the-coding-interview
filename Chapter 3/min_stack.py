from stack import Stack

class MinStack(Stack):
    def __init__(self):
        self.min_stack = Stack()
        super().__init__()

    def push(self, data):
        super().push(data)

        if self.min_stack.is_empty() or (not self.min_stack.is_empty() and data <= self.min_stack.peek()):
            self.min_stack.push(data)

    def pop(self):
        data = super().pop()

        if data == self.min_stack.peek():
            self.min_stack.pop()

        return data

    def min(self):
        return self.min_stack.peek()