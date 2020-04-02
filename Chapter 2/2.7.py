from linked_list import LinkedList, Node

node1 = Node(1)

linked_list = LinkedList()
linked_list.append("a")
linked_list.append("b")
linked_list.append("c")
linked_list.append_node(node1)
linked_list.print()

linked_list2 = LinkedList()
linked_list2.append_node(node1)
linked_list2.append("d")
linked_list2.append("e")

def find_intersection(linked_list1, linked_list2):
    if linked_list1.size == 0 or linked_list2.size == 0:
        return None

    current_list = linked_list1 
    other_list = linked_list2
    if linked_list1.size < linked_list2.size: 
        current_list = linked_list2
        other_list = linked_list1

    set_of_nodes = set()

    current_head = current_list.head
    while current_head is not None:
        set_of_nodes.add(current_head)
        current_head = current_head.next

    current_head = other_list.head
    while current_head is not None:
        if current_head in set_of_nodes:
            return current_head

        current_head = current_head.next

    return None

print(node1)
print(find_intersection(linked_list, linked_list2))
