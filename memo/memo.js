foo();
function foo() {
  console.log("hello");
}

var foo = function() {
  console.log("hello");
};
foo();

//Question 1:
function foo() {
  function bar() {
    console.log("hello");
  }

  return bar();

  function bar() {
    console.log("world");
  }
}
foo();

//Question 2:
function foo() {
  var bar = function() {
    console.log("hello");
  };
  return bar();
  var bar = function() {
    console.log("world");
  };
}
foo();
