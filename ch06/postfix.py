from list_stack import ListStack


def evaluate(p: str):
    s = ListStack()
    digit_previously = False

    for i in range(len(p)):
        char = p[i]
        if char.isdigit():
            if digit_previously:
                char = 10 * s.pop() + int(char)
                s.push(char)
            else:
                s.push(int(char))
                digit_previously = True
        elif is_operator(char):
            s.push(operation(s.pop(), s.pop(), char))
            digit_previously = False
        else:
            digit_previously = False

    return s.pop()


def is_operator(ch) -> bool:
    return ch == '+' or ch == '-' or ch == '*' or ch == '/'


def operation(opr2: int, opr1: int, ch) -> int:
    return {'+': opr1+opr2, '-': opr1-opr2, '*': opr1*opr2, '/': opr1//opr2}[ch]


def main():
    postfix = "700 3 47 + 6 * - 4 /"
    print("Input string:", postfix)
    answer = evaluate(postfix)
    print("Answer:", answer)
    print(ord('0'), ord('9'))


if __name__ == "__main__":
    main()
