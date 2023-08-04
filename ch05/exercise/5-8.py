from ..list_node import ListNode


def are_in_same_linked_list(node1: ListNode, node2: ListNode) -> bool:
    start, end = node1, node2
    while start != None:
        if start == end:
            return True
        start = start.next

    start, end = node2, node1
    while start != None:
        if start == end:
            return True
        start = start.next

    return False
