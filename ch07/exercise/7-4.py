import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch07')
from ch07.list_queue import ListQueue

def push(a: ListQueue, x):
    b = ListQueue()
    b.enqueue(x)
    while not a.is_empty():
        b.enqueue(a.dequeue())
    while not b.is_empty():
        a.enqueue(a.dequeue())

def pop(a: ListQueue):
    b = ListQueue()
    while True:
        temp = a.dequeue()
        if not a.is_empty():
            b.enqueue(temp)
        else:
            break
    while not b.is_empty():
        a.enqueue(b.dequeue())
    return temp
