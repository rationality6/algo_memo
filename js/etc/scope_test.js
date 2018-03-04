function foo() {
  let color
  if (true) {
    let color = 'blue'
    console.log(color)
  }
  console.log(color)
}

foo()

let x = 'global'

const foo = () => {
  let x = 'local'
  return bar()
}

const bar = () => {
  console.log(x)
}

const a = foo()
console.log(a);
bar()

///
const foo = () => {
  let x = 'local'
  const bar = () => {
    console.log(x)
  }
  return bar
}

const a = foo()
console.log(a());
///

let globalColor = 'red'
function foo() {
  let fooColor = 'blue';
  function bar() {
    let barColor = 'yellow'
    console.log(barColor)
    console.log(fooColor)
    console.log(globalColor)
  }
  bar()
}
foo()

var color = 'red';
function foo() {
  var color = 'blue'; // 2
  function bar() {
    console.log(color); // 1
  }
  return bar;
}
var baz = foo(); // 3
baz(); // 4

function foo() {
  if (true) {
    var color = 'blue'
  }
  console.log(color)
}
foo()
