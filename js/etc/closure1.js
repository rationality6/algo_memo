function foo() {
  var color = 'blue';
  function bar() {
    console.log(color);
  }
  bar();
}
foo();


function foo() {
  var color = 'blue';
  function bar() {
    console.log(color);
  }
  return bar;
}
const wrap = foo()
console.log(wrap());
