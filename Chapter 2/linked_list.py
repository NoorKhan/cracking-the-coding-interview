class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        print(self.data)
        if self.next is not None:
            print(self.next.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size = self.size + 1

    def append_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size = self.size + 1

    def remove(self, data):
        current_node = self.head
        if current_node is None:
            return False
        
        if current_node.data == data:
            self.head = current_node.next
            return True

        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return True
            else:
                current_node = current_node.next

        return False

    def print(self):
        if self.head is None:
            print("Empty list!")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, "-> ", end = "")
                current_node = current_node.next
            print(None)