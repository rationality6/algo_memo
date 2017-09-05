export class Human {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  say() {
    console.log(`${this.name} ${this.age}`);
  }
}

const hyun = new Human("Hyun", 30);
