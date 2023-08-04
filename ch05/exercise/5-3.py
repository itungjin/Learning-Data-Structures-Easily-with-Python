from list_node import ListNode


class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__num_items = 0

    def __get_node(self, i: int) -> ListNode:
        curr = self.__head
        for _ in range(i+1):
            curr = curr.next
        return curr

    def insert(self, i: int, new_item):
        if i >= 0 and i <= self.__num_items:
            prev = self.__get_node(i-1)
            new_node = ListNode(new_item, prev.next)
            prev.next = new_node
            self.__num_items += 1
        else:
            print('index', i, ": out of bound in insert()")

    def append(self, new_item):
        prev = self.__get_node(self.__num_items - 1)
        new_node = ListNode(new_item, prev.next)
        prev.next = new_node
        self.__num_items += 1

    def pop(self, i: int):
        if i >= 0 and i <= self.__num_items - 1:
            prev = self.__get_node(i-1)
            curr = prev.next
            prev.next = curr.next
            self.__num_items -= 1
            return curr.item
        else:
            return None

    def __find_node(self, x) -> tuple[ListNode, ListNode]:
        prev = self.__head
        curr = prev.next
        while curr != None:
            if curr == x:
                return (prev, curr)
            else:
                prev = curr
                curr = curr.next
        return (None, None)

    def remove(self, x):
        prev, curr = self.__find_node(x)
        if curr != None:
            prev.next = curr.next
            self.__num_items -= 1
            return x
        else:
            return None

    def get(self, i: int):
        if self.is_empty():
            return None
        elif 0 <= i <= self.__num_items - 1:
            return self.__get_node(i).item
        else:
            return None

    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__num_items):
            if curr.item == x:
                return index
            else:
                curr = curr.next
        return None

    def is_empty(self) -> bool:
        return self.__num_items == 0

    def size(self) -> int:
        return self.__num_items

    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__num_items = 0

    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        return cnt

    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))

    def copy(self):
        new_linked_list = LinkedListBasic()
        for index in range(self.__num_items):
            new_linked_list.append(self.get(index))
        return new_linked_list

        # new_linked_list = LinkedListBasic()
        # new_linked_list.extend(self)
        # return new_linked_list

    def reverse(self):
        temp_linked_list = LinkedListBasic()
        for index in range(self.__num_items):
            temp_linked_list.insert(0, self.get(index))

        # temp_linked_list = self.copy()

        self.clear()
        for index in range(temp_linked_list.size()):
            self.append(temp_linked_list.get(index))

    def sort(self) -> None:
        temp_list = []
        for index in range(self.__num_items):
            temp_list.append(self.get(index))
        temp_list.sort()
        self.clear()
        for item in temp_list:
            self.append(item)

    def print_list(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item, end=' ')
            curr = curr.next
        print()

    def print_interval(self, i: int, j: int):
        curr = self.__get_node(i)
        for _ in range(i, j):
            print(curr.item)
            curr = curr.next
