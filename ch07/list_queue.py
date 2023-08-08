class ListQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.__queue[0]

    def is_empty(self) -> bool:
        return not self.__queue

    def deque_all(self):
        self.__queue.clear()

    def print_queue(self):
        print("Queue from front:", end=' ')
        print(*self.__queue)
