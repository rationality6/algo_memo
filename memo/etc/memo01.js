function test1() {
  var a = 1;
  console.log(a);
  if (true) {
    var a;
    console.log(a, "a");
    a = 2;
  }
  console.log(a);
}

test1();

Array.prototype.myMethod = function() {
  for (i = 0; i < this.length; i++) {
    this[i] = this[i].toUpperCase();
  }
};
var my_array = ["one", "two", "Three", "Four"];
my_array.myMethod();
console.log(my_array);

let result = [];
for (let i = 0, len = 10; i < len; i += 1) {
  result.push(()=>i)
}
console.log(result[1]());
