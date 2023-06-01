#
# 1. NumPy (numerical Python)
# array에 관련된 라이브러리, 선형 대수, 퓨리에 변환 등에 사용되는 함수들도 가지고 있다.
# python에서 NumPy array가 list보다 많이 사용됨.

# 동일 타입으로 packing 되어있는 배열이고, 여러 벡터나 행렬 등의 기능을 사용할 수 있고, 코드 짜기도 편함.

list1 = [1,2,3,4]
list2 = [5,6,7,8]
product = [a*b for a, b in zip(list1, list2)]


import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
product = arr1 * arr2

#
# 2. Creating NumPy Arrays
# NumPy에서 array를 생성하는 몇 가지 방법이 있다.

# From a python list or tuple : list를 바로 convert해서 array를 생성
arr3 = np.array([1,2,3])
print(arr3)

arr32 = np.array([[1,2,3], [4,5,6]])
print(arr32)

# numpy array를 생성하는 함수 사용 (e.g. arange, linspace, ...)
arr4 = np.arange(10)
print(arr4)

# 0, 1을 이 둘을 포함해 8등분
arr42 = np.linspace(0,1,8)
print(arr42)

#
# 3. Basic Operations
# NumPy에서 기본 수학 연산은 배열에서 요소 단위로 작동하며, 
# 연산자 오버로드와 숫자 모듈의 함수로 모두 사용할 수 있다.

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

# elementwise calculation (요소 별 사칙연산)
print(x + y)
print(np.add(x, y))

print(x-y)
print(np.subtract(x,y))

print(np.multiply(x, y))

print(np.divide(x, y))

# 루트
print(np.sqrt(x))

#
# 4. indexing & slicing

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# slicing을 이용, 특정 위치의 subarray를 추출한다.

b = a[:2, 1:3]
# 첫 두 개 row와 2,3번째 column을 추출
#
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

print(b)
#[[2 3] [6 7]]

print(a[0, 1]) 
# 2

# a의 slice인 b도 a와 동일한 메모리를 참조하므로 b를 바꾸면 a도 바뀐다.
b[0, 0] = 77
print(a[0,1])
# 77