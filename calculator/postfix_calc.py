import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from stack import Stack
from calc import plus, minus, multi, priority

def Postfix_calc(postfix):
    st = Stack.Stack()
    for cur in postfix:
        if cur in priority:
            operands1 = st.pop()
            operands2 = st.pop()
            if cur == '+':
                st.push(plus(operands1, operands2))
            elif cur == '-':
                st.push(minus(operands1, operands2))
            elif cur == '*':
                st.push(multi(operands1, operands2))
        else:
            st.push(cur)
    return st.pop()
