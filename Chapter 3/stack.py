class Stack:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None
        self.size = 0

    def pop(self):
        if self.top is not None:
            current_top_data = self.top.data
            self.top = self.top.next

            self.size = self.size - 1

            return current_top_data
        else:
            return None
    
    def push(self, data):
        node = self.Node(data)
        node.next = self.top
        self.top = node

        self.size = self.size + 1

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.size == 0

    def print(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
