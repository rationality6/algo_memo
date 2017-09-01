class Stack {
  constructor() {
    this.stack = [];
  }
  push(val) {
    this.stack.push(val);
  }
  pop() {
    this.stack.pop();
  }
  peek() {
    return this.stack[this.stack.length - 1];
  }
  length() {
    return this.stack.length;
  }
  print() {
    console.log(this.stack.join(" "));
  }
}

let stack0 = new Stack();
stack0.push(1);
stack0.push(2);
stack0.push(3);
stack0.print();
console.log("length is 3:", stack0.length());
console.log("peek is 3:", stack0.peek());
console.log("pop is 3:", stack0.pop());
stack0.print();
console.log("pop is 2:", stack0.pop());
console.log("length is 1:", stack0.length());
console.log("pop is 1:", stack0.pop());
stack0.print();
console.log("peek is undefined:", stack0.peek());
console.log("pop is undefined:", stack0.pop());
