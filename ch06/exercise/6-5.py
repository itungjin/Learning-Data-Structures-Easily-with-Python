from ch06.linked_stack import LinkedStack
import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch06')


def paren_balance(s: str) -> bool:
    stack = LinkedStack()
    for char in s:
        if char == '(':
            stack.push('(')
        elif char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()
    if stack.is_empty():
        return True
    else:
        return False
