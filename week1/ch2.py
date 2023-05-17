# Data Structures and Control flow

# 1. Data structures
# 데이터를 저장하고 조작하는 data structures

# list : 배열
# 순서가 있고, 변할 수 있는 데이터 집합. [] 안에 데이터들을 ,로 구분해 넣는다.

ex_list = [1, 2, 3, "apple", "banana"]

# tuples : list와 비슷하지만 변경할 수는 없는 데이터 집합. () 안에 데이터들을 ,로 구분해 넣는다.

ex_tuple = ( 1, 2, 3, "apple", "banana")

# Dictionaries : 순서가 없는 데이터 집합. 각 데이터는 k-v 쌍으로 구성되어 있다. 변경 가능하고 ,로 데이터 쌍을 구분함.
ex_dic = {"name" : "Alice", "age" : 25, "address": "newyork"}

# Sets : 순서가 없는 unique item의 집합. 변경이 가능하고 ,로 구분
# 데이터 간 순서라는게 없고, 중복값이 불가능하다는 점에서 list와 구분 됨.
ex_set = {1, 2, 3, "apple", "banana", "apple"}
print(ex_set) # {1, 2, 3, 'banana', 'apple'} - 실행할때마다 다른 순서로 찍혀 나옴


##########

# 2. Control Flow
# 프로그램의 실행 순서를 조작한다.

# 조건문
# if, elif, else를 사용한다.
x = 10
if x > 0:
    print("x is positive")
elif x < 0 :
    print("x is negative")
else:
    print("x is zero")

# 반복문
# for, while을 사용한다.

# for loop - list 등을 사용해 범위 내에서 반복
for i in range(5):
    print(1)
    
# while loop - 조건이 true인 동안 반복
i = 0
while i < 5:
    print(i)
    i += 1
    
# loop control statements
# break, continue, pass

# break : 현재 반복을 끝내고 다음 코드 실행
# continue : 현재 반복을 생략하고, 다음 루프를 실행

# pass : 이건 좀 익숙하지가 않은데, 미래의 코드를 위한 placeholder라고 한다.
# pass statement가 실행되면 아무 일도 일어나지 않지만 빈 코드가 허용되지 않는 코드의 경우에도 에러 없이 넘어갈 수 있음.

# function w/o content
def my_function():
    pass
    
# class w/o content
class MyClass
    pass
    
# loop w/o code
for x in [0, 1, 2]:
    pass

# 위 세 가지 모두 pass 없이 그냥 비워두면 에러가 남.
# 딱히 기능적으로 필요한건 아니고, 사용자의 개발 과정에서의 편의성을 위한 기능

