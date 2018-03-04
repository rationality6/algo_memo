interface Person {
  firstName: string;
  lastName: string;
}

const greeter = (person: Person) => {
  return `Hello ${person.firstName}, ${person.lastName}`
}


console.log(greeter({ firstName: "hyun", lastName: "ahn" }))


class Student {
  fullName: string
  constructor(
    public firstName: string,
    public middleInitial: string,
    public lastName: string
  ) {
    this.fullName = firstName + " " + middleInitial + " " + lastName
  }
}

let user = new Student("Jane", "M.", "User")


let isDone: boolean = false

let decimal: number = 6
let hex: number = 0xf00d
let binary: number = 0b1010
let octal: number = 0o744

let color: string = "blue"
color = 'red'

let fullName: string = `Bob Bobbington`

let age: number = 37
let sentence: string = `Hello, my name is ${fullName}`
console.log(sentence)

// let list: number[] = [1, 2, 3]
let list: Array<number> = [1, 2, 3]
// console.log(list)
console.log(list)


function identity<T>(arg: T): T {
  return arg
}

let output = identity<string>("myString")

console.log(output)
