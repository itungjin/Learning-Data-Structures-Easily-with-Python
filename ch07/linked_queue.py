import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch05')
from ch05.circular_linked_list import CircularLinkedList

class LinkedQueue:
    def __init__(self):
        self.__queue = CircularLinkedList()

    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        return self.__queue.get(0)

    def is_empty(self) -> bool:
        return self.__queue.is_empty()

    def dequeue_all(self):
        self.__queue.clear()

    def print_queue(self):
        print("Queue from front:", end=' ')
        self.__queue.print_list()
