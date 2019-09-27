from linked_list import LinkedList

def kth_to_last(linked_list, k):
    nodes = []

    current_head = linked_list.head
    while current_head is not None:
        nodes.append(current_head)
        current_head = current_head.next
    
    print(nodes[len(nodes) - k - 1].data)

linked_list = LinkedList()
linked_list.append("z")
linked_list.append("a")
linked_list.append("b")
linked_list.append("c")

kth_to_last(linked_list, 1)