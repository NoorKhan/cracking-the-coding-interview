from stack import Stack

class SetOfStacks:
    def __init__(self, threshold):
        self.stacks = [Stack()]
        self.threshold = threshold

    def push(self, data):
        if self.stacks[-1].size == self.threshold:
            stack = Stack()
            stack.push(data)
            self.stacks.append(stack)
        else:
            self.stacks[-1].push(data)

    def pop(self):
        current_stack = self.stacks[-1]
        current_stack.pop()
        
        if current_stack.size == 0:
            self.stacks.pop()

    def print(self):
        i = 1
        for stack in self.stacks:
            print('stack #: ', i)
            stack.print()
            i = i + 1

