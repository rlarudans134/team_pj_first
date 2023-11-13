import calc
import sys
from intopost import InToPost

# TODO
"""
1. Enter로 입력을 받는다.

2. 지원하는 연산은 더하기(+), 빼기(-), 곱하기(*)다.

3. 한 번의 입력에는 한 종류의 연산만 들어올 수 있다.

4. 사용자가 =를 입력하면 연산 결과를 출력한다.

5. 정수만 입력될 수 있다.

6. 2-5번의 입력 외에는 에러메세지를 출력한다.
"""

type_exeption = ["(", ")", "+", "-", "*"]
tmp = []

# End State define here: condition ==> "="
while True:
    user_input_exprssion = sys.stdin.readline().rstrip()

    # EOF detection here
    try:
        if user_input_exprssion[0] == "=":
            break
    except IndexError:
        print("EOF Error occured, Please try again")
        continue

    # Change user_input to list type
    user_input_exprssion = list(user_input_exprssion)

    # Change type of string to decimal, and also check condition 5. which in TODO.
    for idx in range(len(user_input_exprssion)):
        if user_input_exprssion[idx] not in type_exeption:
            try:
                user_input_exprssion[idx] = int(user_input_exprssion[idx])
            except ValueError:
                print("Please check your input, You can only type the int")
                break
    
    # Result about infix
    infix = user_input_exprssion

    # Call out InToPost function here
    InToPost(infix)

