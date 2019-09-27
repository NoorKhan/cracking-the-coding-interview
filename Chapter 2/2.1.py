class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
                print(current_node.data)
                current_node = current_node.next

def remove_duplicates(linked_list):
    data_set = set()

    previous_node = linked_list.head
    current_node = previous_node.next
    data_set.add(previous_node.data)
    
    while current_node is not None:
        if current_node.data in data_set:
            previous_node.next = current_node.next        
        else:
            data_set.add(current_node.data)
            previous_node = current_node

        current_node = current_node.next
    
linked_list = LinkedList()
linked_list.append("z")
linked_list.append("a")
linked_list.append("a")
linked_list.append("a")
linked_list.append("a")
linked_list.append("b")
linked_list.append("b")
linked_list.append("c")
linked_list.append("cat")
linked_list.append("c")
linked_list.append("z")
linked_list.append("z")
linked_list.append("z")
linked_list.append("bc")
remove_duplicates(linked_list)
linked_list.print()