from Stack import Stack, priority

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
