function Stack() {
  this.stack = [];
}

Stack.prototype.push = function(value) {
  this.stack.push(value);
};
Stack.prototype.pop = function() {
  return this.stack.pop();
};
Stack.prototype.peek = function() {
  return this.stack[this.stack.length - 1];
};
Stack.prototype.length = function() {
  return this.stack.length;
};
Stack.prototype.print = function() {
  console.log(this.stack.join(" "));
};

var stack0 = new Stack();

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

// last in first out lifo
