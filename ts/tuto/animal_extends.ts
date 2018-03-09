class Animal {
  public name: string
  constructor(
    theName: string
  ) { this.name = theName }
}

class Rhino extends Animal {
  constructor() {
    super("Rhino?")
  }
}

class Employee {
  private name: string
  constructor(
    theName: string
  ) {
    this.name = theName
  }
}

let animal = new Animal("Goat")
let rhino = new Rhino()

console.log(animal)
console.log(rhino)
