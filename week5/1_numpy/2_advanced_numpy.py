#
# 1. Random Module in NumPy
# 난수 생성 함수

import numpy as np

# generate 3 * 3 numpy array (요소는 전부 랜덤값)
random_array = np.random.rand(3,3)
print(random_array)

#
# 2. Array Manipulation
# 배열을 조작할 수 있는 함수들이 있다.

array = np.array([1,2,3,4,5,6])
new_array = array.reshape(3,2)
print(new_array)
# [[1 2] [3 4] [5 6]]

#
# 3. broadcasting
# numpy가 산술 연산 수행시 여러 형식이 다른 array와 작업할 수 있게 해줌.

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([2, 2, 2])

c = a + b 
print(c)
# [[3 4 5] [6 7 8] [9 10 11]]

#
# 4. Working w/ mathmatical Functions
# 배열에 적용될 수 있는 다양한 수학적 연산들

a = np.array([1, 4, 9])

# square root
b = np.sqrt(a)
print(b)

# exponential
c = np.exp(a)
print(c)