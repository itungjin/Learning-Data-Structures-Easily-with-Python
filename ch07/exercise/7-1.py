class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, x):
        self.__queue.insert(0, x)
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.__queue.pop()
    
    def front(self):
        if self.is_empty():
            return None
        else:
            return self.__queue[-1]
    
    def is_empty(self):
        return not self.__queue
    
    def dequeue_all(self):
        self.__queue.clear()