#
# 1. Understanding Generators and the yield keyword
# generator는 함수의 특수한 타입으로, iterator를 반환한다.
# 정의는 다른 함수와 동일하게 하지만, 일련의 값들을 생성해야 할 때는 
# return 대신 yield를 사용한다.

# 이는 덩치 큰 데이터 집합을 다룰 때 유용한데, 다른 접근 방식을 통해 iterator를 생성하는데 사용된다.
# 제너레이터를 사용하면 모든 것을 미리 저장하는 대신 진행하면서 생성할 수 있다.

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator
gen = simple_generator()

# generator는 `next` method를 이용해 사용할 수 있다.
# next method를 호출하면 generator는 마지막에 멈춘 곳부터 재개되며, 다음 `yield`까지 진행한다.
# 더 이상 `yield`가 없다면 `StopIteration` 예외가 발동하며, 모든 값이 생성되었다는 것을 알려준다.
print(next(gen))
print(next(gen))
print(next(gen))

# 한 번 더 호출하려고 하면 StopIteration이 뜨면서 에러가 남
# print(next(gen)) 

#
# 2. Writing generators
# 파이썬의 제네레이터는 활용 범위가 매우 넓다.
# 좀 더 복잡한 예시로 피보나치 수열도 만들 수 있음.

def fibonacci():
    a, b = 0, 1
    
    # 이론적으로 무한 반복문
    while True:
        yield a
        a, b  = b, a + b
        

fib = fibonacci()
# yielded vlaue는 next의 리턴값으로 들어옴
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# 중요한건 각 호출 사이에 일정한 state를 유지하는 것.
# 또, next를 호출해서 값이 바뀐다면 이전 값은 다시 사용할 수 없다.

#
# 4. Generator Expressions
# 짧은 표현으로 generator를 생성하는 syntax에 대해 알아보자.

gen2 = (x**2 for x in range(10))

# 이는 아래 함수와 동일
def gen22():
    for x in range(10):
        yield x**2

# 이렇게 제네레이터에서 반복적으로 값을 뽑아내는 것도 가능하다.
g = gen22()
for val in g:
    print(val)
    
#
# 5. using generators w/ Data pipilines
# generator는 데이터 프로세싱 작업에서 매우 유용하다.
# generator를 여럿 사용해 데이터 처리 파이프라인을 구축해
# 가독성 좋고 메모리도 효율적으로 쓰는 코드를 짤 수 있다. 

# file을 열어 line 별로 읽는 함수
def read_file(filename):
    """A generator to rad lines from a file."""
    with open(filename) as f:
        for line in f:
            yield line.strip()
            
def filter_lines(lines, keyword):
    """A generator to filter lines based on a keyword."""
    for line in lines:
        if keyword in line:
            yield line
            

filename = "example.txt"

lines = read_file(filename)
filtered_lines = filter_lines(lines, "important")

# read_file, filter_lines는 한 번에 한 줄 읽고, 그걸 반복해 처음부터 끝까지 읽게 됨.
for line in filtered_lines:
    print(line)
    
#
# 6. generator-based coroutines
# coroutine은 비동기 작업들을 관리한다. 
# generator 함수는 다른 작업이 작동할 때 잠시 멈출 수 있음. (`yield` 키워드 사용)

#
# 7. sending data to generator
# `yield` 키워드를 사용하면 generator도 데이터를 받아 coroutine 비슷하게 동작할 수 있다.
# generator의 send method를 이용해 data를 generator에 넣는다.

def echo():
    while True:
        received = yield
        print(received)
        
e = echo()
# 우선 한 번 실행해서, generator가 yield에서 멈춰있도록 해야함
next(e) 

# data를 받으면 print하고 다시 반복문 처음으로 돌아가 yield에서 멈춤
e.send("say hello")

# 반복
e.send("to my chocolate glaze")