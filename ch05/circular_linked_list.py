from list_node import ListNode


class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", self.__tail)
        self.__num_items = 0

    def insert(self, i: int, new_item) -> None:
        if 0 <= i <= self.__num_items:
            prev = self.get_node(i-1)
            new_node = ListNode(new_item, prev.next)
            prev.next = new_node
            self.__num_items += 1
            if i == self.__num_items - 1:
                self.__tail = new_node
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
        
        if len(args) == 0 or args[0] == -1:
            index = self.__num_items - 1
        else:
            index = args[0]
        
        prev = self.get_node(index-1)
        curr = prev.next
        prev.next = curr.next
        if index == self.__num_items - 1:
            self.__tail = prev
        self.__num_items -= 1
        return curr.item
    
    def remove(self, x):
        prev, curr = self.__find_node(x)
        if curr != None:
            prev.next = curr.next
            self.__num_items -= 1
            if self.__tail == curr:
                self.__tail = prev
            return curr.item
        else:
            return None
    
    def get(self, *args):
        if self.is_empty():
            return None
        
        if len(args) == 0 or args[0] == -1:
            index = self.__num_items - 1
        else:
            index = args[0]
        
        if 0 <= index <= self.__num_items - 1:
            return self.get_node(index).item
        else:
            return None
    
    def index(self, x) -> int:
        cnt = 0
        curr = self.__tail


        while curr != self.__tail:
            if curr.item == x:
                return cnt
            else:
                curr = curr.next
                cnt += 1
        
        if curr.item == x:
            return cnt

        return None
    
    def is_empty(self) -> bool:
        return self.__num_items == 0

    def size(self) -> int:
        return self.__num_items
    
    def clear(self):
        self.__tail = ListNode("dummy", self.__tail)
        self.__num_items = 0
    
    def count(self, x) -> int:
        cnt = 0
        curr = self.__tail.next
        while curr != self.__tail:
            if curr.item == x:
                cnt += 1
            curr = curr.next
        if curr.item == x:
            cnt += 1
        return cnt
    
    def extend(self, a):
        for x in a:
            self.append(x)
    
    def copy(self) -> b'CircularLinkedList':

        
    

        