from bidirect_node import BidirectNode


class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode('dummy', None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__num_items = 0

    def insert(self, i: int, new_item) -> None:
        if 0 <= i <= self.__num_items:
            prev = self.get_node(i-1)
            new_node = BidirectNode(new_item, prev, prev.next)
            prev.next = new_node
            new_node.next.prev = new_node
            self.__num_items += 1
        else:
            print("index", i, "out of bound in insert()")

    def append(self, new_item) -> None:
        prev = self.__head.prev
        new_node = BidirectNode(new_item, prev, self.__head)
        prev.next = new_node
        self.__head.prev = new_node
        self.__num_items += 1

    def pop(self, *args):
        if self.is_empty():
            return None

        if len(args) == 1:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__num_items - 1

        if 0 <= i < self.__num_items:
            curr = self.get_node(i)
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__num_items -= 1
            return curr.item
        else:
            return None

    def remove(self, x):
        curr = self.__find_node(x)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__num_items -= 1
            return x
        else:
            return None

    def get(self, *args):
        if self.is_empty():
            return None

        if len(args) == 1:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__num_items - 1

        if 0 <= i < self.__num_items:
            return self.get_node(i).item
        else:
            return None

    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return None

    def is_empty(self) -> bool:
        return self.__num_items == 0

    def size(self) -> int:
        return self.__num_items

    def clear(self):
        self.__head = BidirectNode('dummy', None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__num_items = 0

    def count(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt

    def extend(self, a):
        for element in a:
            self.append(element)

    def copy(self) -> 'CircularDoublyLinkedList':
        a = CircularDoublyLinkedList
        for element in self:
            a.append(element)
        return a

    def reverse(self) -> None:
        curr = self.__head
        for _ in range(self.__num_items + 1):
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)

    def __find_node(self, x) -> BidirectNode:
        curr = self.__head.next
        while curr != self.__head:
            if curr.item == x:
                return curr
            curr = curr.next
        return None

    def get_node(self, i: int) -> BidirectNode:
        curr = self.__head
        for _ in range(i+1):
            curr = curr.next
        return curr

    def print_list(self) -> None:
        for element in self:
            print(element, end=' ')
        print()

    def __iter__(self):
        return CircularDoublyLinkedListIterator(self)


class CircularDoublyLinkedListIterator:
    def __init__(self, alist: CircularDoublyLinkedList):
        self.__head = alist.get_node(-1)
        self.iter_position = self.__head.next

    def __next__(self):
        if self.iter_position == self.__head:
            raise StopIteration
        else:
            item = self.iter_position.item
            self.iter_position = self.iter_position.next
            return item
