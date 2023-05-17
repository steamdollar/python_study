# File I/O & Context managers

# Part 1. File I/O
# 파일들을 조작하기 위한 기본적 함수와 method using file object

# Writing to a file
with open("text.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("asdfggh\n")

# w for the write mode

with open("text.txt", "a") as f:
    f.write("Hello again.")
    
# a for the append mode

# Reading a file
with open("text.txt", "r") as f:
    # print(f.read())
    lines = f.readlines()
    
    # r for the read mode
    
lines.remove("asdfggh\n")
# 여기까지만 하면 파일에 반영되지 않는다.
# 수정된 데이터를 다시 file에 넣어줘야 함.

with open('text.txt', 'w') as file:
    for line in lines:
        file.write(line)    


# cf) r+ for read+write mode도 있다.


# Part2. Context Managers
# `with` keyword와 함께 conjunction에 사용될 method를 결정하는 object

# context manager protocol은 __enter__, __exit__ method로 이루어져 있다.
# with block이 실행되면 __enter__ method가 실행되고,
# with block이 끝날 때 __exit__ method가 실행된다.
# 보통 실행 직후 바로 clean up 되어야할 작업들과 함께 사용한다. (파일 닫기 같은..)

# ManagedFile class가 context manager로 
# context에 들어올때 파일을 열고, (__enter__)
# 나갈 때 파일을 닫는다. (__exit__)

class ManagedFile:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__ (self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile("text.txt") as f:
    print(f.read())
