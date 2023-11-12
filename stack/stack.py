class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = node.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None



priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}
def InToPost(infix):
  s = Stack()
  postfix = []
  for i in infix:
    if i == '(':
      s.push(i)
    elif i == ')':
      while s.peek() != '(':
        postfix.append(s.pop())
      s.pop()
    elif i in priority:
      while not s.is_empty():
        if priority[s.peek()] >= priority[i]:
          postfix.append(s.pop())
        else:
          break
      s.push(i)
    else:
      postfix.append(i)
  while not s.is_empty():
    postfix.append(s.pop())

  return postfix
