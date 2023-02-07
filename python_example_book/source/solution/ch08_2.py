class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())