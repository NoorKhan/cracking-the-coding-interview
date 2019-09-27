class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            node = Node(data, None)
            node.next = node
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head)
            self.tail.next = node
            self.tail = node

        self.size = self.size + 1

    def print(self):
        if self.head is None:
            print("List is empty!")
        else:
            current_node = self.head
            while True:
                print(current_node.data, end=' -> ')
                current_node = current_node.next
                if current_node is self.head:
                    break

linked_list = CircularLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
print(linked_list.print())
            
    

   