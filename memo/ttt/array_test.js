const burger = {
  eat: () => {
    console.log(this);
  },
  eat_func: function() {
    console.log(this);
  }
}

// burger.eat()
burger.eat()

const sugar = n => {
  return n
}

console.log(sugar('foo'))
