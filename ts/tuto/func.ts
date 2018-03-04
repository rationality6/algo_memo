function first(arr: any[]): any {
  return arr[0]
}
function first_generic<T>(arr: T[]): T {
  return arr[0]
}


first_generic<number>([1, 2, 3])
console.log(first_generic)
