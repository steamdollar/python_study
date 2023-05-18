# 1. Understanding Polymorphism
# 프로그래밍에서 polymorphism은 함수, 변수, 객체가 다양한 폼을 가질 수 있는 능력을 의미하는 
# OOP의 기본적인 개념이다.

# 다형성의 실전적인 적용은 
# 객체가 다양한 데이터 타입에 속하고, 다른 타입에 대한 동일한 이름을 가진 method 호출에 응답하는 능력이다.

# 2. Polymorphism with a Function and Objects
class Animal:
    def __init__(self, name):
        self.name = name
    
    # 하위 class따라 다른 값을 가질 것이므로 여기서는 pass로 값을 주지 않음
    def speak(self):
        pass

# Dog class는 Animal class를 상속받음
class Dog(Animal):
    def speak(self):
        return self.name + ' says Woof!'

class Cat(Animal):
    def speak(self):
        return self.name+ ' says meow!'

fido= Dog("Fido")
isis = Cat("isis")

print(fido.speak())
print(isis.speak())

# 어떤 타입 인스턴스든 받을 수 있는 함수를 만들 수도 있다.
def animal_speak(animal):
    print(animal.speak())
    
animal_speak(fido)
animal_speak(isis)

# 3. Polymorphism w/ inheritance
# 다형성은 상속과 밀접한 연관이 있다. 
# 예시에서 base class Animal로부터 Dog, Cat의 child class가 나왔는데,
# 각 child class들은 speak method를 Animal class로부터 상속받고, method를 override 한다.

# 각기 다른 타입의 animals 배열을 만들고 반복문으로 speak() method를 호출
# > 각 child는 각기 다른 반응을 보인다.
animals = [Dog("Fido"), Cat("isis")]

for animal in animals:
    print(animal.speak())