// 
// 1. Concept
// JSON 형식으로 데이터를 저장하는 컨테이너
// k - v 형식으로 이루어져 있고, key는 string (property name), value는 뭐든 올 수 있음

let person = {
    name : "John",
    age : 20
}

console.log(person.name) // John

// 
// 2. Prototype-based Inheritance
// 일반적인 OOP 언어와는 조금 다르다. 
// JS는 class-based model보다는 prototype-based model에 기반하고 있음

// JS의 각 객체들은 전부 다른 객체, 자신의 prototype과 링크되어 있다.
// 만약 객체에 없는 property에 접근하려 할 경우, 
// JS는 이 링크를 이용해 프로토타입 객체에서 이를 찾으려고 한다.
// 이를 'prototypal inheritance' 라고 함.

let animal = {
    eats : true
}

let rabbit = {
    jumps : true
}

rabbit.__proto__ = animal;

console.log(rabbit.eats) // true

//
// 3. Defining Classes in JS (ES6)
// js는 ES6부터 class 키워드를 도입하기 시작했음


// Person은 class
class Person {
    
    // constructor는 class로부터 객체를 생성, 초기화하는 특수한 method
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    // PEerson 객체가 사용할 수 있는 method
    greet() {
        console.log(`Hello, I am ${this.name}`)
    }
}

// class가 정의되었다면 new 키워드를 사용해 그에 속하는 인스턴스를 생성할 수 있다.

let lsj = new Person("lsj", 30)
lsj.greet()

//
// 5. Methods and Properties
// class 내부에서 함수는 method, 변수는 properties 라고 부른다.

class Car {
    constructor(brand) {
        this.carname = brand;
    }
    
    present() {
        return "I have a " + this.carname;
    }
}

let mycar = new Car("Ford")
console.log(mycar.present())

//
// 6. Getter and Setters
// api 등을 만들 때 data를 보호하기 위해 사용한다. 
// 직접 property를 조작하지 않고, method를 통해 조작함

class User {
    constructor(name) {
        this._name = name
        // 언더바는 backing field (private) 를 생성하기 위해 사용된다.
    }
    
    get name () {
        return this._name
    }
    
    set name(value) {
        if(value.length < 4) {
            console.log("Name is too short")
            return
        }
        this._name = value
    }
}

let user = new User("Trump")
console.log(user.name)

user.name = "Biden"
console.log(user.name)

user.name = "Jo"

//
// 7. Static methods and properties
// static method는 class의 모든 인스턴스에 적용되는 mehtod이다.
// class 자체에서 정의되며, 일반적으로 utility function에 활용된다.

class Helper {
    static log(message) {
        console.log(message)
    }
}

Helper.log("this is static method!")

//
// 8. Inheritance and Polymorphism in ES6 classes
// 존재하는 class로부터 새로운 class를 만들 때 사용하는 핵심 개념이 된다.

class Animal {
    constructor(name) {
        this.name = name
    }
    
    speak() {
        console.log(this.name + ' makes a noise')
    }
}

// Dog class는 Animal로 부터 derive 됨.
class Dog extends Animal {
    // Animal의 speak method를 override, showing polymorphism
    speak() {
        console.log(this.name + ' barks.')
    }
}

let dog = new Dog("Rex")
dog.speak()

//
// 9. encapsulation
// 숨겨진 데이터에 접근할 수 있는 방식. 객체의 data에 직접 접근하는 것을 막고,
// class의 method를 통해 접근할 수 있도록 한다.
// 보통 closure와 IIFE(즉발 함수)를 이용해 구현함

let Employee = (function() {
    let privateData = {}
    
    function Employee(name, age) {
        privateData[this.id = Math.random()] = {
            name : name,
            age : age
        }
    }
    
    Employee.prototype.getName = function (){
        return privateData[this.id].name
    }
    
    Employee.prototype.getAge = function () {
        return privateData[this.id].age
    }
    
    return Employee
})()

let emp = new Employee("John", 30)
console.log(emp.getName())
console.log(emp.getAge())