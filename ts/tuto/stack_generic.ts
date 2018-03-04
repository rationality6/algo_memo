class Stack {
  private foobar: string = "foo"
  private data: any[] = [];
  private foobar1: string = "bar"
  contructor() { }
  push(item: any): void {
    this.data.push(item);
  }
  pop(): any {
    return this.data.pop();
  }
}

const stack0 = new Stack()

class NumberStack extends Stack {
  constructor() {
    super()
  }
  push(item: number): void {
    super.push(item)
  }
  pop(): number {
    return super.pop()
  }
}

const ns = new NumberStack()
console.log(ns)
ns.push(1)
ns.push(2)
ns.push(3)
console.log(ns)


class StackGeneric<T> {
  private data: T[] = []
  constructor() {
  }
  push(item: T): void {
    this.data.push(item)
  }
  pop(): T {
    return this.data.pop()
  }
}

const numberStack = new StackGeneric<number>()
const stringStack = new StackGeneric<string>()
numberStack.push(1)
numberStack.push(2)
// numberStack.push('c')
stringStack.push('a')
stringStack.push('b')
// stringStack.push(3)
// stringStack.push('?' as any)
console.log(numberStack)
console.log(stringStack)
