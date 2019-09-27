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

    def find(self, data):
        if self.head is None:
            return None
        else:
            current_node = self.head
            while True:
                if current_node.data == data:
                    return current_node
                
                current_node = current_node.next
                if current_node is self.head:
                    break

        return None

def is_rotated_substring(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        linked_list = CircularLinkedList()
        for c in s1:
            linked_list.append(c)

        first_character = s2[0]
        node = linked_list.find(first_character)

        if node is None:
            return False
        else:
            for c in s2[1:]:
                if node.next.data == c:
                    node = node.next
                else:
                    return False

        return True

print(is_rotated_substring("dabc", "abcd"))