from typing import Tuple
from list_node import ListNode


class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__num_items = 0

    def insert(self, i: int, new_item) -> None:
        if 0 <= i <= self.__num_items:
            prev = self.get_node(i-1)
            new_node = ListNode(new_item, prev.next)
            prev.next = new_node
            if prev == self.__tail:
                self.__tail = new_node
            self.__num_items += 1
        else:
            print("index", i, ": out of bound in insert()")

    def append(self, new_item) -> None:
        new_node = ListNode(new_item, self.__tail.next)
        self.__tail.next = new_node
        self.__tail = new_node
        self.__num_items += 1

    def pop(self, *args):
        if self.is_empty():
            return None

        if len(args) == 0:
            i = self.__num_items
        else:
            if args[0] == -1:
                i = self.__num_items
            else:
                i = args[0]
        if 0 <= i < self.__num_items:
            prev = self.get_node(i-1)
            curr = prev.next
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
            self.__num_items -= 1
            return curr.item
        else:
            return None

    def remove(self, x):
        prev, curr = self.__find_node(x)
        if curr != None:
            prev.next = curr.next
            if curr == self.__tail:
                self.__tail = prev
            self.__num_items -= 1
            return x
        else:
            return None

    def get(self, *args):
        if self.is_empty():
            return None

        if len(args) == 0:
            i = self.__num_items
        else:
            if args[0] == -1:
                i = self.__num_items
            else:
                i = args[0]
        if 0 <= i < self.__num_items:
            curr = self.get_node(i)
            return curr.item
        else:
            return None

    def index(self, x) -> int:
        count = 0
        for element in self:
            if element == x:
                return count
            count += 1
        return None

    def is_empty(self) -> bool:
        return self.__num_items == 0

    def size(self) -> int:
        return self.__num_items

    def clear(self):
        self.__tail = ListNode('dummy', None)
        self.__tail.next = self.__tail
        self.__num_items = 0

    def count(self, x) -> int:
        count = 0
        for element in self:
            if element == x:
                count += 1

        return count

    def extend(self, a):
        for x in a:
            self.append(x)

    def copy(self) -> 'CircularLinkedList':
        new_list = CircularLinkedList()
        for element in self:
            new_list.append(element)
        return new_list

    def reverse(self) -> None:
        __head = self.__tail.next

        prev = __head
        curr = prev.next
        next = curr.next

        curr.next = prev
        __head.next = self.__tail
        self.__tail = curr

        while next != __head:
            prev = curr
            curr = next
            next = next.next
            curr.next = prev

    def sort(self) -> None:
        temp = []
        for element in self:
            temp.append(element)
        temp.sort()
        self.clear()
        for element in temp:
            self.append(element)

    def __find_node(self, x) -> Tuple[ListNode, ListNode]:
        prev = self.__tail.next
        curr = prev.next

        while curr != self.__tail.next:
            if curr.item == x:
                return prev, curr
            prev, curr = curr, curr.next

        return None, None

    def get_node(self, i: int) -> ListNode:
        curr = self.__tail.next

        for _ in range(i+1):
            curr = curr.next

        return curr

    def print_list(self) -> None:
        for element in self:
            print(element, end=' ')
        print()

    def __iter__(self):
        return CircularLinkedListIterator(self)

    def print_interval(self, i: int, j: int):
        curr = self.get_node(i)

        for _ in range(i, j):
            print(curr.item)
            curr = curr.next


class CircularLinkedListIterator:
    def __init__(self, alist: CircularLinkedList):
        self.__head = alist.get_node(-1)
        self.iter_position = self.__head.next

    def __next__(self):
        if self.iter_position == self.__head:
            raise StopIteration
        else:
            item = self.iter_position.item
            self.iter_position = self.iter_position.next
            return item
