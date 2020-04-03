from linked_list import LinkedList, Node

linked_list = LinkedList()
node_a = Node(1)
node_b = Node(2)
node_c = Node(3)
node_d = Node(4)
node_e = Node(5)

linked_list.append_node(node_a)
linked_list.append_node(node_b)
linked_list.append_node(node_c)
linked_list.append_node(node_d)
linked_list.append_node(node_e)
node_e.next = node_c

def find_loop_node(linked_list):
    nodes = set()

    current_node = linked_list.head
    while current_node is not None:
        if current_node in nodes:
            return current_node
        else:
            nodes.add(current_node)
            current_node = current_node.next

    return None

print(find_loop_node(linked_list).data)
