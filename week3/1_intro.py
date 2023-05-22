#
# 1. Understanding the Functional Programming Paradigm
# 함수형 프로그래밍은 state 변경이나 변경 가능 data를 피하고, 데이터 처리를 수학적인 함수로 취급하는 패러다임.
# 이 패러다임 안에서 함수는 다른 변수처럼 전달, 사용될 수 있다. (e.g. 람다 함수)

# apply_func는 숫자 두개와 함꼐 함수 하나를 파라미터로 받는다.
def apply_func(x, y, func):
    return func(x,y)

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

print(apply_fujnc(5,3, add))
print(apply_fujnc(5,3, subtract))

#
# 2. pure function
# pure function이란, 리턴값이 다른 문제 없이 오직 투입값에 의해서만 결정되는 것을 의미한다.
# = 주어진 input에 대해 항상 같은 값을 리턴

def pure_function(x):
    return 2 * x

print(pure_function(5)) # 10
print(pure_function(5)) # 10

#
# 3. 고차 함수
# 하나 이상의 함수를 인자값으로 받거나, 리턴하는 함수.
# 합성 함수와 비슷하다고 보면 됨..

#
# 4. Immutability and State
# 함수형 프로그래밍의 핵심 개념이 불변성임.
# 함수형 프로그래밍에서는 변화를 싫어해서 뭐든지간에 항상 일정하길 바란다.
# 그래서 생성 후 변하지 않는 데이터 구조나 타입을 사용하게 됨.

# 예시로 tuple은 immutable한데 반해 list는 mutable 함.
# 따라서 함수형에서는 tuple이 선호된다.

x = (1,2,3)
# x[0] = 0 # 으로 바꾸려고 하면 에러남
