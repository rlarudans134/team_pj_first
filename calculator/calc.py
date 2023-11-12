import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from stack import Stack

def plus(a,b):
  try:
    result = a + b
    return result
  except:
    print(f"더하기 에러 발생")
    return None

def minus(a,b):
  try:
    result = a - b
    return result
  except:
    print(f"빼기 에러 발생")
    return None

def multi(a,b):
  try:
    result = a * b
    return result
  except:
    print(f"곱하기 에러 발생")
    return None
#
def Operands(infix):
  numbers = list('0123456789.')
  recognized = []

  i = 0
  while i < len(infix):
    j = 1
    if infix[i] in numbers:
      while i + j < len(infix):
        if infix[i + j] in numbers:
          j += 1
        else:
          break
      recognized.append(''.join(infix[i:i + j]))
      i += j
    else:
      recognized.append(infix[i])
      i += 1
  return recognized

# def InToPost(infix):
#   s = stack.Stack()
#   postfix = []
#   for i in infix:
#     if i == '(':
#       s.push(i)
#     elif i == ')':
#       while s.top() != '(':
#         postfix.append(s.pop())
#       s.pop()
#     elif i in priority:
#       while not s.isEmpty():
#         if priority[s.top()] >= priority[i]:
#           postfix.append(s.pop())
#         else:
#           break
#       s.push(i)
#     else:
#       postfix.append(i)
#   while not s.isEmpty():
#     postfix.append(s.pop())
#
#   return postfix
#
###InToPost()기능 중 일부 기능 calc.py내에서 제대로 작동하지않아######
###stack.py로 이동 후에 정상 작동함을 확인#####
