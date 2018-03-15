function test() {
  var i;
  console.log(i)
  for (i = 0; i < 5; i++) {
    console.log(i)
  }
  console.log(i)
}
test()

console.log(add(2, 3))

console.log(add(3, 4))

function add(x, y) {
  return x + y
}
