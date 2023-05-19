//
// 1. interface
// 코드와 코드 외부에서의 컨트랙트를 정의하는 방법이다.
// 인터페이스는 객체가 특정 구조에 맞는지를 검사하는데 사용된다.
// 변수의 특정 조합을 지정해 항상 함께 사용하도록 할 수 있음.

interface IStudent {
    name : string;
    id : number;
    display() : void;
}

// Student Class는 IStudent employee를 implement해, 필요한 속성과 method가 전부 있는지 확인한다.
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

let stu: IStudent = new Student("lsj", 2014160141)
stu.display()

//
// 2. Access Modifier : public, private, protected
// public : 어디서나 접근할 수 있는 맴버 (디폴트)
// private : 그들이 정의된 class 내에서만 접근할 수 있는 맴버.
// protected : class와 그 subclass에서 접근할 수 있다.

class Employee {
    public name : string;
    private id : number;
    protected age : number;
    
    constructor(name : string, id : number, age : number) {
        this.name = name;
        this.id = id;
        this.age = age;
    }   
}

class Manager extends Employee {
    display() : void {
        // public, protected는 manager class에서 접근할 수 있음
        console.log(`name : ${this.name}, Age : ${this.age}`)
        
        // private인 id property는 subclass Manager에서 접근할 수 없음
        // console.log(`id : ${this.id}`)
    }
}

//
// 3. Static Properties and Methods
// Static members는 class의 instance가 아닌 class에 귀속되어 있다.
// class name을 직접 이용해 접근할 수 있다. (인스턴스를 생성하지 않고도)

class Person {
    static job : string = "WhiteHand"
    
    static getJob() {
        return this.job
    }
}

console.log(Person.job)
console.log(Person.getJob())

//
// 4. Abstract Classes
// 다른 class를 유도할 수 있는 base classes인데, 직접 인스턴스화가 되지는 않는다.
// member들을 위한 implementation을 위한 세부 사항을 포함하고 있고,
// `abstract` keyword가 abstract class와 method를 정의하는데 사용된다.

abstract class Employer {
    name : string;
    
    constructor(name : string) {
        this.name = name;
    }
    
    abstract display() : void;
}

// employer class를 상속받은 Managers class가 
// Employer에서 정의된 display method를 구현한다.
class Managers extends Employer {
    display() : void {
        console.log(`Manager Name : ${this.name}`)
    }
}

let mgr = new Managers("John Conner")
mgr.display()


//
// 5. Generics 
// 컴포넌트가 어떤 데이터 타입이든 받아서 작동할 수 있게 해줌,.
// 하나의 data type에 묶인걸 풀어주는 역할.
// 함수, 클래스, 인터페이스 모두에 사용할 수 있다.

class Collection<T> {
    private items : T[] = [];
    
    addItem(item : T) : void {
        this.items.push(item)
    }
    
    getItems() : T[] {
        return this.items;
    }
}

let numCollection = new Collection<number>();
numCollection.addItem(1)
numCollection.addItem(2)

console.log(numCollection.getItems()) // [1, 2]

let strCollection= new Collection<string>();
strCollection.addItem("aaa")
strCollection.addItem("bbb")

console.log(strCollection.getItems()) // [aaa, bbb]