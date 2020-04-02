from linked_list import LinkedList

linked_list = LinkedList()
linked_list.append(7)
linked_list.append(1)
linked_list.append(6)
linked_list.print()

linked_list2 = LinkedList()
linked_list2.append(5)
linked_list2.append(9)
linked_list2.append(2)
linked_list2.print()

def sum_lists(linked_list, linked_list2, forward = False):
    def get_list_value(linked_list):
        sum = 0
        current_node = linked_list.head
        index = 0
        while current_node is not None:
            if forward:
                sum += current_node.data * 10 ** (linked_list.size - 1 - index)
            else:
                sum += current_node.data * 10 ** index
            current_node = current_node.next
            index += 1

        return sum

    return get_list_value(linked_list) + get_list_value(linked_list2)

print(sum_lists(linked_list, linked_list2))
# for the forward case use the size instance variable on the linked_list class.
# this can be done other ways
print(sum_lists(linked_list, linked_list2, True))

