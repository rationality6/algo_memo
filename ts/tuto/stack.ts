class Stack {
  private data: any[] = [];
  contructor() { }
  push(item: any): void {
    this.data.push(item);
  }
  pop(): any {
    return this.data.pop();
  }
}

const stack0 = new Stack()

// stack0.push(1)
// stack0.push(2)
// stack0.push(3)
// stack0.push(4)
// console.log(stack0)
//
// console.log(stack0.pop())
// console.log(stack0.pop())
// console.log(stack0.pop())
// console.log(stack0.pop())
//
// console.log(stack0)

class Stack_generic<T>{
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


const stack_generic = new Stack_generic()
