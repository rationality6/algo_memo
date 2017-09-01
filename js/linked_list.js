const Node = function(data) {
  this.data = data;
  this.next = null;
};

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.numberOfValues = 0;
  }
  add(data) {
    const node = new Node(data);

    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.numberOfValues++;
  }
  remove(data) {
    let previous = this.head;
    let current = this.head;
  }
  traverse(fn) {
    let current = this.head;
    while(current){
      if(fn){
        fn(current)
      }
    }
  }
  length() {
    return this.numberOfValues;
  }
  print() {
    let string = "";
    let current = this.head;
    while (current) {
      string += `${current.data}`;
      current = current.next;
    }
    console.log(string.trim());
  }
}

const singlyLinkedList = new SinglyLinkedList();
singlyLinkedList.print();
singlyLinkedList.add(1);
singlyLinkedList.add(2);
singlyLinkedList.add(3);
singlyLinkedList.add(4);
singlyLinkedList.print();

if (!null) {
  console.log("foo");
}
