interface IPerson {
  name: string
  sayHello(): void
}

class Person implements IPerson {
  constructor(public name: string) { }
  sayHello() {
    console.log(`Hello ${this.name}`)
  }

}

function greeter(person: IPerson): void {
  person.sayHello();
}

const me = new Person('Lee')
greeter(me)