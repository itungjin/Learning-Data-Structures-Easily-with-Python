from ..circular_doubly_linked_list import CircularDoublyLinkedList


def contains(alist: CircularDoublyLinkedList, x) -> bool:
    if alist.index(x):
        return True
    return False
