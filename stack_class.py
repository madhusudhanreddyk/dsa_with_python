from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,key):
        self.container.append(key)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)
s = Stack()
s.push("We")
s.push("will")
s.push("conquere")
s.push("COVI-19")
s.pop()
print(s.peek())
print(s.is_empty())
print(s.size())
print(s.container)
