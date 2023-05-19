//
// 1. Class & object
// ts는 js와 같은듯 다름..
// 일단 당연히 property들의 type을 언급해줘야 함.

class Employee {
    name : string;
    age : number;
    
    constructor(name : string, age : number) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        console.log( `Hello my name is ${this.name}`)
    }
}

let emp = new Employee("John", 30)
emp.greet();


//
// 2. interface
// 코드와 코드 외부에서의 컨트랙트를 정의하는 방법이다.
// 인터페이스는 객체가 특정 구조에 맞는지를 검사하는데 사용된다.
// 변수의 특정 조합을 지정해 항상 함께 사용하도록 할 수 있음.

interface IStudent {
    name : string;
    id : number;
    display() : void;
}

class Student implements IStudent {
    name : string;
    id : number;
    
    constructor(name : string, id : number) {
        this.name = name;
        this.id = id
    }
    
    display() : void {
        console.log(`Student name : ${this.name} , StudentID : ${this.id}`)
    }
}


// Student Class는 IStudent employee를 implement해, 필요한 속성과 method가 전부 있는지 확인한다.
let stu: IStudent = new Student("lsj", 2014160141)
stu.display()


//
// 2. Inheritance
// 상속은 extends keyword를 사용한다.

class Manager extends Employee {
    department : string;
    
    constructor(name : string, age : number, department : string) {
        // 상속받은 class는 super를 이용해 처리
        super(name, age);
        
        // 그 외 고유 property들은 this를 이용
        this.department = department
    }
    
    manage() {
        console.log(`I manage the ${this.department} department`)
    }
}

let mgr = new Manager("Alice", 40, "HR")
mgr.manage()

//
// 3. Polymorphism
// 이 쪽도 큰 차이는 없다.

class Animal {
    name : string;
    
    constructor(name : string) {
        this.name = name
    }
    
    move() {
        console.log(`${this.name} is moving`)
    }
}

class Bird extends Animal {
    // move method를 override
    move() {
        console.log(`${this.name} is flying`)
    }
}

let bird : Animal = new Bird("Sparrow")
bird.move()

//
// 4. encapsulation
// access modifier `private`, `protected`, `public`을 이용해 encapsulation을 구현할 수 있다.

class Car {
    private name : string;
    private price : number
    
    constructor(name : string, price : number) {
        this.name = name;
        this.price = price
    }
    
    public greet() {
        console.log(`Hello, I am ${this.name}`)
    }
}

let mac = new Car("Benz", 1000);
emp.greet()
// console.log(emp.name) // err