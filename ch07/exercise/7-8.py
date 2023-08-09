class Deque:
    def __init__(self):
        self.__deque = []
    
    def enqueue(self, x):
        self.__deque.append(x)
    
    def dequeue(self):
        return self.__deque.pop(0)

    def enqueue_front(self, x):
        self.__deque.insert(0, x)
    
    def dequeue_tail(self):
        return self.__deque.pop()

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.__deque[0]
    
    def is_empty(self):
        return not self.__deque

    def deque_all(self):
        self.__deque.clear()
    
    def print_queue(self):
        print("Deque from front:", end=' ')
        print(*self.__deque)
    