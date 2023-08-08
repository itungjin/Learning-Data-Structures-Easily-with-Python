from ch06.linked_stack import LinkedStack
import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch06')


def copy_stack(a: LinkedStack, b: LinkedStack):
    b.pop_all()
    temp_stack = LinkedStack()
    while not a.is_empty():
        temp_stack.push(a.pop())
    while not temp_stack.is_empty():
        item = temp_stack.pop()
        a.push(item)
        b.push(item)
