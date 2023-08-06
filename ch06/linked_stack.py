import sys
sys.path.append('/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append('/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch05')

from ch05.linked_list_basic import LinkedListBasic


class LinkedStack:
    def __init__(self):
        self.__list = LinkedListBasic()

    def push(self, x):
        self.__list.insert(0, x)

    def pop(self):
        return self.__list.pop(0)

    def top(self):
        if self.is_empty():
            return None
        else:
            return self.__list.get(0)

    def is_empty(self):
        return self.__list.is_empty()

    def pop_all(self):
        self.__list.clear()

    def print_stack(self):
        print("Stack from top:", end=' ')
        self.__list.print_list()
        print()
