#
# 1. understanding Inheritance
# inheritance는 존재하는 class를 직접 변형하지 않고, 취해서 새로운 class를 만드는 방법이다.
# 새로 만든 class는 derived class (child class), 원래 있던 class를 base clss(parent class)라고 부름.
# 코드 재활용성을 높혀주고, class를 변형하지 않고 새롱운 것들을 추가할 수 있게 해줌.

# Parent Classes and Child Classes
# python에서는 child class를 생성할 때 parent class를 인수로 줄 수 있음.

# parant class Animal
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating")

# child class dog

# __init__ 함수, eat 함수를 상속받음.
class Dog(Animal):
    
    # dog class만의 함수 bark 정의
    def bark(self):
        print(f"{self.name} is barking")
        
dog = Dog("fido")

dog.eat()
dog.bark()

#
# 2. Overriding Methods
# 가끔 parnet class로부터 받은 method가 child에는 적절하지 않은 경우 child class에서 이를 override 할 수 있다.

class Bird(Animal):
    def eat(self):
        print(f"{self.name} is pecking at a seed")
        
bird = Bird("Polly")
bird.eat()

