#
# 1. Understanding Encapsulation
# 마찬가지로 OOP의 기본적인 개념중 하나이다.
# data, method를 wrap하는 것을 의미한다.
# > 변수와 method로의 접근을 제한하고, 데이터의 의도치 않은 수정을 방지할 수 있다.

#
# 2. Private & Protected Access Modifier
# 파이썬에서는 인스턴스를 private이나 protected로 설정하기 위해,
# __(private)나 _(protected)를 사용할 수 있다.

#
# 2-1. Protected members : subclass에서만 접근할 수 있는 요소
class Animal:
    def __init__(self, name, age):
        self._name = name
        # age를 protected class로 설정
        self._age = age

#        
# 2-2. private memebers : subclass를 포함한 외부에서 접근할 수 없다.
class Animal:
    def __init__(self, name, age):
        # name, age를 private class로 설정 
        self.__name = name
        self.__age = age

#         
# 3. Getters and Setters
# 이런 요소들에 접근하기 위해서는 getter, setter method를 사용한다.

# Getter : private한 요소의 값을 가져오기 위해 사용되는 method. get_ prefix를 붙여 사용한다.
# Setter : private한 요소의 값을 조작하기 위해 사용되는 method. set_ prefix를 붙여 사용한다.

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_age(self):
        return self.__age
        
    def set_age(self, age):
        if age > 0:
            self.__age = age