function count() {
  // var i;
  for (let i = 1; i < 5; i += 1) {
    setTimeout(() => {
      console.log(i)
    }, i * 100)
  }
}
count()

function count() {
  var i;
  for (i = 1; i < 10; i += 1) {
    (function(countingNumber) {
      setTimeout(function)
    })
  }
}

function count() {
  var i
  for (i = 1; i < 10; i += 1) {
    (function(countingNumber) {
      setTimeout(function timer() {
        console.log(countingNumber);
      })
    })(i)
  }
}

count()

function foo() {
  if (true) {
    var color = 'blue';
  }
  console.log(color);
}
foo();

function foo() {
  let color
  if (true) {
    color = 'blue';
    console.log(color);
  }
  console.log(color);
}
foo();

const outter = () => {
  const data_in = "in!"
  const inner = () => {
    return data_in;
  }
  return inner
}
const result = outter()
console.log(result())
