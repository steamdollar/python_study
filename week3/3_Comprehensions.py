#
# Comprehensions는 하나 이상의 iterator로부터 데이터 구조를 생성하는 방식이다.
# loop, 조건 검사 등을 짧은 코드로 할 수 있게 해줌.

#
# 1. list comprehensions
# list를 생성하는 간결한 방법. [] 안에 활용할 배열과 함께 for, in을 사용한다.

numbers = [1,2,3,4,5]
squares = [n ** 2 for n in numbers]
print(squares)

#
# 2. Dictionary comprehensions
# list와 동일하게 dictionary들도 간단한 표현식을 사용해 만들 수 있다.

squares2 = { n : n**2 for n in numbers }
print(squares2)

#
# 3. set comprehensions
# set도 마찬가지. set은 중복된 값을 허용하지 않으므로, 이를 알아서 걸러줌.

numbers2 = [1,2,2,3,4,4,5,5,6,6]

unique_squares = { n **2 for n in numbers2 }
print(unique_squares)