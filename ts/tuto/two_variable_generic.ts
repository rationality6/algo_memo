function toPair(a: any, b: any): [any, any] {
  return [a, b]
}

console.log(toPair(3, 4))

function topair_generic<T, U>(a: T, b: U): [T, U] {
  return [a, b]
}

console.log()
