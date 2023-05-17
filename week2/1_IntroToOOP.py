# 1. UnderStanding OOP

# OOP는 프로그래밍 패러다임으로, 프로그램을 구조화해 하나의 객체에 property와 behavior가 묶여있는 것을 의미한다.
# 코드 유지 관리가 쉬워짐.

# 2. classes and obj in python
# 파이썬에선 모든게 객체다. type() 을 사용해 객체의 타입을 확인할 수 있다.

# class는 객체의 청사진이라고 보면 됨.

class Dog:
    # __init__ : class로부터 obj가 생성될때 실행되는 함수, obj의 attribute를 초기화한다.
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print("woof!")

# Dog type instance(object) my_dog 생성
my_dog = Dog("Fido")

# attribute, method에 접근 가능
print(my_dog.name)
my_dog.bark()

# 3. class variable and instance variable
# 파이썬엔 두 가지 변수가 있다.

# class variable : class의 모든 인스턴스에게 공유되는 변수, 이를 바꾸면 모든 인스턴스의 해당 값이 변한다.
# instance varaible : class의 각 인스턴스들 각각이 가지고 있는 변수

class Dog:
    # class variable
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog("Fido", 3)
dog2 = Dog("Rex", 5)

Dog.species = "Canis lupus"
print(dog1.species)
print(dog2.species)

# 4. instance methods
# method는 class 내부에 정의된 함수로, 그 class의 인스턴스에만 호출될 수 있다.
# mtehod의 첫 파라미터는 항상 `self`이며, class의 인스턴스를 향한 reference가 된다.

def bark(self):
    print("woof!")

# method를 class 선언 이후 추가할 수도 있으나, 코드 관리가 어려워지므로 추천되는 방식은 아님    
Dog.bark = bark

dog1.bark()

# 5. self
# `self` keyword는 class의 instance method에 첫 번쨰 인수로 사용되는 convention이다.
# 이는 method가 호출되는 instance를 refer 한다.

class Person:
    # __init__, greeting 모두 self를 첫 번째 인수로 가짐
    def __init__(self, name):
        self.name = name
        
    def greeting(self):
        print(f"Hello, {self.name}")
        

lsj = Person("lsj")

# 인스턴스를 만들고 method 호출시, 파이썬이 자동으로 인스턴스를 method에 전달해줌
lsj.greeting() # 사실 greeting(lsj) 를 호출하는 것

