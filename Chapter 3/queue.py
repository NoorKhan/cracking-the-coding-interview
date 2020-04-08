class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, item):
        node = self.Node(item)

        if self.first is None:
            self.first = node
        
        if self.last is not None:
            self.last.next = node

        self.last = node

        self.size = self.size + 1

    def remove(self):
        if self.first is not None:
            data = self.first.data
            self.first = self.first.next

            if self.first is None:
                self.last = None

            self.size = self.size - 1

            return data

        return None

    def peek(self):
        if self.first is None:
            return None
        else:
            return self.first.data

    def is_empty(self):
        return self.first is None

    def print(self):
        if self.is_empty():
            print("Empty queue")

        current_node = self.first

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

queue = Queue()
queue.add(5)
queue.add(12)
queue.add(1)

queue.print()