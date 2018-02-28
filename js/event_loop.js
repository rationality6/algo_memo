function test1() {
  console.log("test1")
  test2()
}

function test2() {
  let timer = setTimeout(function() {
    console.log("test2");
  }, 0);
  test3()
}

function test3() {
  console.log("test3");
}

test1()

function getX() {
  console.log(x);
  var x = 100
  console.log(x);
}
getX()

foo()
var foo = function() {
  console.log("Hello");
}

function outer() {
  var name = `closure`;
  function inner() {
    return name
  }
  return inner()
}
console.log(outer())

var name = `Warning`;
function outer() {
  var name = `closure`;
  function inner() {
    console.log(name);
  }
  return inner()
}
var callFunc = outer();
callFunc();

const outer = n => {
  const name = "Bory"
  const inner = () => {
    return name
  }
  return inner
}
const strip = outer()
console.log(strip())

var myObject = {
  name: 'foo',
  sayName: function() {
    console.log(this);
  }
}
myObject.sayName();
// console> Object {name: "foo"}
