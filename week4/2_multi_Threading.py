#
# 1. Understanding Threads
# 멀티 스레딩이 뭔지는 다 아니까 넘어가고,
# 파이썬에 global interpreter lock (GIL)은 인터프리터에서
# 한 번에 하나의 스레드만 실행할 수 있도록 허용한다는 점에 유의한다.
# 즉, 멀티프로세스 시스템에서도 파이썬 스레드는 서로 다른 코어에서 실제 병렬로 실행되는게 아니라,
# 인터프리터가 스레드를 빠르게 스위칭해서 그렇게 보이는 것.

#
# 2. Creating and Managing Threads
# 새로운 스레드를 생성하기 위해서는 Thread 객체를 인스턴스화하고, start method를 호출한다.


import threading

def print_numbers():
    for i in range(10):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# thread 시작
thread1.start()
thread2.start()

# thread 종료 대기
thread1.join()
thread2.join()

print('thread 1, 2 done')

#
# 3. thread간 동기화
# 종종 복수의 스레드의 작업을 동기화해야할 때가 있다.
# threading 모듈에서 이 기능도 지원한다.

# Lock : 가장 간단한 형식의 동기화. 동 시간에 하나의 thread만이 접근할 수 있음.
# 다른 스레드가 lock을 한 데이터에 접근하려려면 lock이 release되길 기다려야 함.

# RLock : reentrant lock (재진입) 동일 thread에 의해 여러 번 획득할 수 있는 동기화 방식.

# Semaphore : 동시에 특정 갯수의 리소스만 리소스에 접근할수 있도록 하는 lock

# Event : 이 이벤트는 내부 플래그를 나타내며, 
# 스레드는 플래그가 설정될 때까지 기다리거나 
# 플래그를 직접 설정하거나 지울 수 있는 간단한 동기화 객체

# Condition : 한 스레드가 조건 변경을 알리는 동안 다른 스레드가 해당 조건이 실현될 때까지 
# 기다릴 수 있도록 하는 고급 형태의 이벤트 객체

lock = threading.Lock()

def print_numbers2():
    lock.acquire()
    for i in range(10):
        print(i)
    lock.release()

def print_letters2():
    lock.acquire()
    for letter in 'zyxwvutsrq':
        print(letter)
    lock.release()
    
thread3 = threading.Thread(target=print_numbers2)
thread4 = threading.Thread(target=print_letters2)

thread3.start()
thread4.start()

thread3.join()
thread4.join()

print('thread 3, 4 done')