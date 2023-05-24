#
# 1. Understanding Decorators
# 함수나 class의 행동을 변경할 수 있게 해주는 도구이다.
# 영구적으로 함수를 변경하지 않고, 함수를 wrap해서 기능을 확장시킬 수 있음.

# python에서 함수는 일급 객체이므로 전달되어 매개 변수로 사용될 수 있다.
# 일급 객체 : 다음 특징을 가지는 모든 객체들
# 1. 모든 요소는 할당 명령문의 대상이 될 수 있다.
# 2. 모든 요소는 동일성 비교의 대상이 될 수 있다.
# 3. 모든 요소는 함수의 파라미터가 될 수 있다.
# 4. 모든 요소는 함수의 반환값이 될 수 있다.

def say_hello(name):
    return f"Hello {name}"

def to_my_chocolate_glaze(name):
    return "Hello Chocolate glaze"

def greet_bob(greeter_func):
    return greeter_func("bob")

print(greet_bob(say_hello))
print(greet_bob(to_my_chocolate_glaze))

#
# 2. Writing Decorators

def my_decorator(func):
    def wrapper():
        print("sth is happen before func is called")
        func()
        print("sth is happen after fun is called")
    return wrapper

def hello():
    print("Hello!")

# hello 함수를 데코레이터를 이용해 wrapper function으로 대체
hello = my_decorator(hello)

hello()

#
# 3. applying decorators
# 더 간결하게 표현하고 싶다면 @ 기호를 사용한다.

@my_decorator
def hello2():
    print("hello2")
    
hello2()

## 4. class decorators
# func가 아닌 class를 수정, 확장한다.

# class를 인수로 받아 property을 추가하는 decorator
def my_class_decorator(cls):
    cls.greeting = "hello"
    return cls
    
@my_class_decorator
class MyClass:
    pass
    
obj = MyClass()
print(obj.greeting)

#
# 5. decorators w/ parameters
# decorator도 인수를 받을 수 있다.

# repeat : n을 인수로 갖는 데코레이터 > 함수 실행의 반복 횟수 결정
def repeat(n):
    # repeat은 decorator를 리턴, decorator는 wrapper를 리턴
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                func(*args)
        return wrapper
    return decorator
    
@repeat(3)
def say_hello2(name):
    print(f"hello {name}")

say_hello2("Alice")