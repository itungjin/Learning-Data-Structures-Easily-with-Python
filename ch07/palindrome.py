import sys
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python')
sys.path.append(
    '/Volumes/CT1000MX 500SSD1/Codes/Learning-Data-Structures-Easily-with-Python/ch06')
from ch06.list_stack import ListStack
from list_queue import ListQueue

def is_palindrome(A) -> bool:
    s = ListStack(); q = ListQueue()
    for i in range(len(A)):
        s.push(A[i]); q.enqueue(A[i])
    while not q.is_empty() and s.pop() == q.dequeue():
        pass
    if q.is_empty():
        return True
    else:
        return False

def main():
    print("Palindrome Check!")
    str = "lioninoil"
    t = is_palindrome(str)
    print(str, "is Palindrome?:", t)

if __name__ == "__main__":
    main()