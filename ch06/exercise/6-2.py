class ListStack:
    def __init__(self):
        self.__stack = []

    def push(self, x):
        self.__stack.insert(0, x)

    def pop(self):
        self.__stack.pop(0)

    def top(self):
        if self.is_empty():
            print("No element in stack")
            return None
        else:
            return self.__stack[0]

    def is_empty(self) -> bool:
        return not self.__stack

    def pop_all(self):
        self.__stack.clear()

    def print_stack(self):
        print("Stack: ")
        for i in range(len(self.__stack)):
            print(f'stack[{i}]: {self.__stack[i]}')
