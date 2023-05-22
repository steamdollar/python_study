#
# 1. 람다 함수
# 작은 익명 함수라고 생각하면 된다.
# 매개 변수는 원하는 대로 받을 수 있지만 표현은 한 가지밖에 없음

# `lambda` args : expression

multiply = lambda x, y : x * y
print(multiply(5,6))


# map function
# js의 map과 동일하게 배열 (or tuple, ...)의 각 요소에 대해 함수를 적용함.

numbers = [1,2,3,4]
squared = map(lambda x : x ** 2, numbers)
print(list(squared))


# filter function
# 조건을 만족하는 요소만 담은 새 배열을 만듬

numbers = [1,2,3,4,5,6]
even_numbers = filter(lambda x : x % 2 == 0 , numbers)
print(list(even_numbers))

# reduce
# functools module의 함수로, 배열 안의 값들에 대해 순차적인 연산을 수행

from functools import reduce

numbers = [1,2,3,4]
product = reduce((lambda x, y : x * y), numbers)
print(product)

