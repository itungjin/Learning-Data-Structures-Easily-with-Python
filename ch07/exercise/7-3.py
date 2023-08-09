import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch07')
from ch07.linked_queue import LinkedQueue

def copy_queue(a: LinkedQueue, b: LinkedQueue):
    temp = []
    while not a.is_empty():
        temp.append(a.dequeue())
    for i in range(len(temp)):
        a.enqueue(temp[i])
        b.enqueue(temp[i])
