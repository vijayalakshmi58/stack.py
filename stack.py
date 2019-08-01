# stack.py
class Stack:
  def __init__(self):
    self.stack = []
  def add(self, department):
    if department not in self.stack:
      self.stack.append(department)
      return True
    else:
        return False
  def remove(self):
    if len(self.stack) <= 0:
      return ("No element in the Stack")
    else:
      return self.stack.pop()
  def peek(self):     
	    return self.stack[-1]
AStack = Stack()
AStack.add("IT")
AStack.add("ECE")
AStack.add("CSE")
print(AStack.remove())
AStack.add("EEE")
print(AStack.peek())
