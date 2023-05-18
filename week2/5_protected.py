class Animal:
    def __init__(self, name, age):
        self._name = name
        self.__age = age
        
        def get_age(self):
            return self.__age
            

# protected member 에 접근하는 것은 가능
dog = Animal("Buddy", 5)
print(dog._name)

dog._name = "Rex"
print(dog._name)

# private인 age에 접근해 read, write 하는건 불가능
try:
    print(dog.__age)
except AttributeError:
    print("Cannot access __age")

try:
    dog.__age = 6
    print(dog.__age)
except AttributeError:
    print("cannot modify private member : __age")


# print(dog.get_age())