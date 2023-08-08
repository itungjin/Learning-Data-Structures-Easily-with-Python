from list_stack import ListStack

def reverse(str):
    st = ListStack()
    for char in str:
        st.push(char)
    out = ""
    while not st.is_empty():
        out += st.pop()
    return out

def main():
    input = "Test Seq 12345"
    answer = reverse(input)
    print("Input string:", input)
    print("Reversed string:", answer)

if __name__ == "__main__":
    main()