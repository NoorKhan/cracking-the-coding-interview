from linked_list import LinkedList, Node

linked_list = LinkedList()
linked_list.append(7)
linked_list.append(1)
linked_list.append(6)

def is_linked_list_palindrome(linked_list):
    reversed_linked_list = LinkedList()

    current_node = linked_list.head
    while current_node is not None:
        current_head = reversed_linked_list.head
        reversed_linked_list.head = Node(current_node.data)
        reversed_linked_list.head.next = current_head
        
        current_node = current_node.next

    current_node = linked_list.head
    current_reversed_node = reversed_linked_list.head
    while current_node is not None:
        if current_node.data != current_reversed_node.data:
            return False
        
        current_node = current_node.next
        current_reversed_node = current_reversed_node.next

    return True

print(is_linked_list_palindrome(linked_list))

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(1)
linked_list.append(1)

print(is_linked_list_palindrome(linked_list))

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(1)

print(is_linked_list_palindrome(linked_list))

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(2)
linked_list.append(1)

print(is_linked_list_palindrome(linked_list))