function node(val, left = EMPTY, right = EMPTY) {
  this.val = val
  this.left = left
  this.right = right
}

node.prototype[Symbol.iterator] = function* iterator() {
  yield* this.left
  yield this.val
  yield* this.right
}

console.log(node)

function* generator0(n) {
  for (let i = 0; i < n; i++) {
    yield i
  }
}

const gen = generator0(5)
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
console.log(gen.next())
