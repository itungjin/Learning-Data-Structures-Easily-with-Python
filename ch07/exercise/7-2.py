import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch07')
from ch07.list_queue import ListQueue


def is_element(string: str):
    q = ListQueue()
    i = 0
    while string[i] != '$':
        q.enqueue(string[i])
        i += 1
    i += 1
    while not q.is_empty() and i < len(string):
        if string[i] != q.dequeue():
            return False
        i += 1
    if q.is_empty() and i == len(string):
        return True
    else:
        return False