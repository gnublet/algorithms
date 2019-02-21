class Stack:
    def __init__(self):
        self.items = [] # list implementation of stack, not really much to do

    # check if Stack is empty
    def is_empty(self):
        return self.items == []

    # push an item to end
    def push(self, item):
        self.items.append(item)

    # pop an item off end
    def pop(self):
        self.items.pop()

    # print stack
    def print_stack(self):
        print(self.items)

def main():
    s = Stack()
    s.push(1)
    s.push('b')
    s.push('cc')
    s.print_stack()

main()
    