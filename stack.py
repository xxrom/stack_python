# LIFO last in first out

class Stack:

  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return self.stack == []

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    data = self.stack[-1] # return last item
    del self.stack[-1]
    return data

  def peek(self):
    return self.stack[-1]

  def sizeStack(self):
    return len(self.stack)

stack = Stack()

stack.push(12)
stack.push(32)
stack.push(42)
print(stack.sizeStack()) # [12 , 32, 42]
print('pop ', stack.pop()) # 42
print('pop ', stack.pop()) # 32
print(stack.sizeStack()) # [12]
print('peek ', stack.peek())
print(stack.sizeStack()) # [12]
