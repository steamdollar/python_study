#
# 1. Understanding preocess in python
# process는 하나 이상의 thread에서 실행되는 컴퓨터 프로그램의 인스턴스로,
# program code와 그 행동을 포함한다.

# python은 global interpreter lock (GIL)을 가지고 있는데, GIL은
# 언어 인터프리터에서 사용되는 메커니즘으로, 스레드의  실행을 동기화해
# 동시에 하나의 스레드만 실행될 수 있도록 한다.
# 즉, 멀티 프로세서 환경에서도 python은 하나의 프로세서만 구동해 하나의 프로세스를 실행하며
# 특정 프로그램에서는 꽤 큰 제한 사항이 될 수 있다.

#
# 2. Creating and Managing Process in Python
# 파이썬의 멀티 프로세싱 모듈은 새로운 프로세스를 생성할 수 있게 한다.

import multiprocessing

# 새 프로세스에서 실행할 함수
def print_numbers():
    for i in range(10):
        print(i)

p = multiprocessing.Process(target=print_numbers)

# start process
p.start()

# wait for the process to finish
p.join()

print("All Done!")

#
# 3. inter-process communication in python
# 파이썬의 프로세스들은 메모리 공간을 공유하지 않아 직접 서로와 커뮤니케이션을 할 수 없다.
# 공유 메모리, 파이프를 사용해 서로와 상호작용해야 한다.
# 이 또한 multiprocessing module에서 기능을 제공함.

#
# 4. difference btw multi"threading" and multi"processing"
# 둘 다 멀티테스킹을 위한 기능이지만 다른 점이 많다.

# Thread : 동일 프로세스 안에서 동일한 메모리 공간을 공유하므로 스레드 간 상호작용이 빠르다.
# 하지만, GIL 때문에 process 하나에서는 동시에 하나의 thread만이 실행될 수 있으므로
# 멀티프로세스 시스템에서 멀티스레딩의 이점이 제한을 받는다.

# Process : 메모리 공간을 공유하지 않아 process간의 의사소통은 thread의 그것보다 느리다.
# 하지만 각 process는 자신의 interpreter와 메모리 공간을 가지므로, 다른 processor들에서 구동될 수 있고,
# 멀티프로세서 환경에서는 멀티 스레딩보다 더 효과적이다.

# 그래서 내가 하는 작업에 따라서 잘 선택하면 되는데,
# cpu-bound task (e.g. 수학적 계산)를 처리할 땐 멀티 프로세싱이,
# (GIL의 제약을 넘어 다른 cpu에서 동시에 돌아갈 수 있으므로)
# I/O bound task (e.g. downloading file from internet)에서는
# I/O operation이 완료되길 기다리는 동안 동시에 실행이 가능한 멀티 스레딩이 좋을 수 있다.

