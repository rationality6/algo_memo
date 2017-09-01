class Animal {
  speak() {
    return this;
  }
  static eat() {
    return this;
  }
}

let obj = new Animal();
console.log(obj.speak());
let speak = obj.speak;
console.log(speak())
console.log(Animal.eat(),'animal eat') // class Animal)
let eat = Animal.eat;
console.log(eat())


// unnamed
const Rectangle = class {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};

// named
const Rectangle = class Rectangle {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
};
