#
# 1. Class methods and Static methods
# classmethods, staticmethods는 파이썬에서 method의 분류이며, 인스턴스가 아닌 class에 소속된 method이다.

#
# 1-1. Class methods
# 개별 인스턴스가 아닌 class 자체에 묶인 method들이다.
# `self`에 대해 접근할 수 없으므로 인스턴스의 상태를 바꿀 수 없으며,
# 대신 class의 상태를 바꿀 수 있다.

# 다음처럼 @classmethod 데코레이터를 이용해 선언하고, 첫 인자로는 cls를 준다.

class MyClass:
    var = 10
    
    @classmethod
    def update_var(cls, new_val):
        cls.var = new_val
        
print(MyClass.var) # 10

MyClass.update_var(99)
print(MyClass.var) # 99

#
# 1-2. staticmethod
# 이건 instance, class에 작동하는 method가 아닌, 특정 파라미터를 처리해주는 함수.

class MyClass2:
    @staticmethod
    def add(a, b):
        return a+b
        
#
# 2. property Decorators
# property 데코레이터는 class에서 getter, setter, deleter를 생성하는 방법이다.
# method를 속성처럼 사용할 수가 있게 됨. > code를 더 가독성 좋고 'pythonic'하게 만든다는데, pythonic한게 뭐냐?

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'
        
    @full_name.setter
    def full_name(self, name):
        self._first_name, self._last_name = name.split()

#        
# 3. Magic or Dunder methods
# dunder = double underscore는 class에 특수한 method를 추가할 때 사용한다.
# __로 감싸져 있어서 그렇게 부름.

# __init__ : class의 인스턴스 초기화시 호출
# __str__ : 원하는 내용을 print
# __len__ : 인스턴스의 length를 리턴

class Dunders:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"MyClass instance : {self.name}"
    
    def __len__(self):
        return len(self.name)
        

prac=Dunders("lsj")

print(prac.name) # lsj
print(prac.__str__()) # lsj
print(prac.__len__()) # 3