import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from stack import Stack
import calc

print("연동 테스트파일입니다.")
print("1.+,-,* 테스트를 위한 두개의 숫자 입력")


a = int(input())
b = int(input())
c = calc.plus(a,b)
d = calc.minus(a,b)
f = calc.multi(a,b)
print(c,d,f)


test_data = list(input("스택을 이용해 연산 숫서 결정하기위한 함수 테스팅 입력 예) (2+3)*4:" ))
infix = calc.Operands(test_data)
postfix = Stack.InToPost(infix)
print(Stack.InToPost(infix))