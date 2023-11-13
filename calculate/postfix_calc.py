from Stack import Stack

priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}

def postfix_calc(postfix):
    st = Stack()
    for cur in postfix:
        if cur in priority:
            operands1 = st.pop()
            operands2 = st.pop()
            if cur == '+':
                st.push(plus(operands1 + operands2))
            elif cur == '-':
                st.push(minus(operands1 + operands2))
            elif cur == '*':
                st.push(mul(operands1 + operands2))
            else:
                st.push(cur)
    return st.pop()
