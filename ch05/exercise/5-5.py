from typing import Tuple
from list_node import ListNode


class LinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__tail = self.__head

    def insert(self, i: int, new_item):
        prev = self.__head
        for _ in range(i):
            prev = prev.next
            if prev == None:
                print('index', i, 'out of bound in insert()')
                return None

        new_node = ListNode(new_item, prev.next)
        prev.next = new_node
        if prev == self.__tail:
            self.__tail = new_node

    def append(self, x):
        new_node = ListNode(x, None)
        self.__tail.next = new_node
        self.__tail = new_node

    def num_items1(self) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            curr = curr.next
            cnt += 1
        return cnt

    def num_items2(self, node: ListNode) -> int:
        if node == None:
            return 0
        else:
            return 1 + self.num_items2(node.next)
