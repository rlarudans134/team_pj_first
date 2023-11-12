# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.top = None
#     def push(self, data):
#         node = Node(data)
#         if self.top is None:
#             self.top = node
#         else:
#             node.next = self.top
#             self.top = node
#     def pop(self):
#         if self.top is None:
#             return None
#         node = self.top
#         self.top = node.next
#         return node.data



class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}
def InToPost(infix):
  s = Stack()
  postfix = []
  for i in infix:
    if i == '(':
      s.push(i)
    elif i == ')':
      while s.top() != '(':
        postfix.append(s.pop())
      s.pop()
    elif i in priority:
      while not s.isEmpty():
        if priority[s.top()] >= priority[i]:
          postfix.append(s.pop())
        else:
          break
      s.push(i)
    else:
      postfix.append(i)
  while not s.isEmpty():
    postfix.append(s.pop())

  return postfix