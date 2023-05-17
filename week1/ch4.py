# Packages and Exception handling

# 1. UnderStanding Python Packages
# package는 파이썬의 module namespace를 구조화하는 방식
# 디렉토리는 __init__.py를 포함해 파이썬이 이를 패키지로
# 인식할 수 있도록 해주어야 한다.
# 내용물은 비워도 되지만 보통 패키지 초기화 코드를 넣어둔다.

# my_package/
# │
# ├── __init__.py
# ├── module1.py
# └── module2.py

# 이렇게 만든 패키지에서 모듈을 가져올 수 있다.
# from my_package import module1
# from my_package.module1 import my_function

# 2. exception Handling
# try-catch 가 아닌 try-except를 사용한다.

try:
    x = 1 / 0
except ZeroDivisionError:
    x = 0
    
# 여러 개의 예외 타입을 넣어 여러 가지 예외 처리를 해줄 수도 있음
try:
    x = 1/ 0
except (ZeroDivisionError, TypeError):
    x = 0

# finally까지 붙이면 에러 발생 여부에 무관하게 실행될 코드 블록을 생성
finally :
    print("finish calculation")

