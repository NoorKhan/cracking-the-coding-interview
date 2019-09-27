from linked_list import Node

node = Node('d')
node.next = Node('e')
node.next.next = Node('f')

def delete_middle_node(node):
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next

    node.print()

delete_middle_node(node)