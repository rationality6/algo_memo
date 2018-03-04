function loggingIdentity<T>(arg: Array<T>): Array<T> {
  console.log(arg.length)
  return arg;
}

// const foo = loggingIdentity<string>("fooo?")
// const foo = loggingIdentity("fooo?")

// console.log(foo)

// function loggingIdentity<T>(arg: T[]): T[] {
//     console.log(arg.length)
//     return arg;
// }


console.log(typeof (+"3"))

// let output = identity<string>("myString")

// console.log(output)

function identity(arg: number): number {
  return arg;
}
