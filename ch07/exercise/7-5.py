import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch06')
from ch06.linked_stack import LinkedStack

def enqueue(a: LinkedStack, x):
    b = LinkedStack()
    while not a.is_empty():
        b.push(a.pop())
    b.push(x)
    while not b.is_empty():
        a.push(b.pop())

def dequeue(a: LinkedStack):
    b = LinkedStack()
    while True:
        temp = a.pop()
        if not a.is_empty():
            b.push(temp)
        else:
            break
    while not b.is_empty():
        a.push(b.pop())
    return temp