# 1. os module : 운영 체제의 기능을 사용, e.g. 파일 시스템 탐색, 환경 정보 프로세스 관리 등..

import os

# 현재 디렉토리 확인
print(os.getcwd())

# 현재 디렉토리의 파일과 폴더
print(os.listdir())

##

# 2. math module : 수학적 기능 제공
import math

# 제곱근 
print(math.sqrt(16))

# 코사인 값
print(math.cos(0))

##

# 3. datatime module : 날짜, 시간 관련 lib
import datetime

now = datetime.datetime.now()
print(now) 

##

# 4. random : 난수 생성
import random

print(random.randint(1,10))