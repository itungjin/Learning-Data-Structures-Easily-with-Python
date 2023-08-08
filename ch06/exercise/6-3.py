from ch06.linked_stack import LinkedStack
import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch06')


def palindrome(string) -> bool:
    s = LinkedStack()
    i = 0
    while string[i] != '$':
        s.push(string[i])
        i += 1
    i += 1
    while i < len(string):
        if string[i] != s.pop():
            return False
        i += 1
    return True
