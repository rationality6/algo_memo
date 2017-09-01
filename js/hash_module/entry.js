import HashTable from "./hash";

const hashTable00 = new HashTable(3);
hashTable00.add("first", 1);
hashTable00.add("second", 2);
hashTable00.add("third", 3);
hashTable00.add("fourth", 4);
hashTable00.add("fifth", 5);
hashTable00.print();

import Human from "./human";

console.log([...Array(5).keys()].reduce((a, b) => a + b));
