function MyArray() {
  this.array = [];
}

MyArray.prototype.add = function(data) {
  this.array.push(data);
};

MyArray.prototype.remove = function(data) {
  this.array = this.array.filter(n => n !== data);
};

MyArray.prototype.search = function(data) {
  var foundIndex = this.array.indexOf(data);
  console.log("foundIndex", foundIndex);
  if (~foundIndex) {
    return foundIndex;
  }
};

MyArray.prototype.getAtIndex = function(index) {
  return this.array[index];
};

MyArray.prototype.length = function() {
  return this.array.length;
};

MyArray.prototype.print = function() {
  console.log(this.array.join(" "));
};

const array00 = new MyArray();

array00.add(1);
array00.add(2);
array00.add(3);
array00.add(4);
array00.print();
console.log(`search 3 gives index 2: ${array00.search(3)}`);
console.log(`getAtindex 2 gives 3: ${array00.getAtIndex(2)}`);
console.log(`length is 4: ${array00.length()}`)
array00.remove(3)
array00.print();
array00.add(5)
array00.add(5)
array00.print()
array00.remove(5)
array00.print()
