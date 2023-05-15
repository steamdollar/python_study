# 1. functions - reusable pieces of codes
# 호출될때만 실행되며, 파라미터를 받아 일정 과정을 거쳐 값을 반환

# 함수는 def를 이용해 정의한다.
# default parameter도 넣어줄 수 있음
def greet(name="world"):
    return "Hello, " + name

print(greet())
print(greet('Alice'))

# 가변 매개변수
# 함수가 받는 매개 변수의 갯수를 바꿀 수 있음

# *arg는 튜플 안의 모든 매개변수를 모아 함수를 반복 실행함
def print_args(*args):
    for i, arg in enumerate(args):
        print("Arg {} is : {}".format(1, arg))

print_args("Alice", "Bob", "Ched")

# 2. 람다 함수
# def 대신 lambda 키워드를 이용해 정의된다. 일반적으로 길지 않고 다시 사용하지 않을 함수에 사용한다.

multiply = lambda x, y : x * y + y
print(multiply(2,3))

# 3. recursion
# 자신의 body 내에서 자신을 호출하는 함수
def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n-1)
        
print(factorial(5))

# 4. import function
import example

example.greet("Elicia")

# module import에도 여러 가지 방법이 있다.

# import module_name : 모듈 전체를 import 할 때, ( 위 example 의 경우)

# import math
# print(math.sqrt(16))

##

# from module_name import function_name : module에서 특정 함수만 가져오고 싶을때, 이 경우 앞에 module.을 붙이고 함수를 호출하지 않고
# 바로 함수명만 써주면 된다.

# from math import sqrt
# print(sqrt(16))

##

# import module_name as alias : 모듈 전체를 가져와 alias를 줄 때
import math as m
print(m.sqrt(16))

# 5. python 표준 lib 탐구
# python_lib.py 참조