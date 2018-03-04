// function makeThreeTimer() {
//   var count = 0;
//   return function() {
//     if (count < 3) {
//       console.log("doing work");
//       count++;
//     } else {
//       throw new Error("No more work");
//     }
//   };
// }
// var threeTimer = makeThreeTimer();
// threeTimer(); // logs 'doing work' (count gets incremented)
// threeTimer(); // logs 'doing work' (count gets incremented)
// threeTimer(); // logs 'doing work' (count gets incremented)
// threeTimer(); // throws an error
// threeTimer.count; // returns undefined

class Person {
  constructor(name) {
    this.name = name;
  }
  static getName() {
    console.log(`${this.name}`);
  }
}
Person.getName();
setTimeout(Person.getName, 1000);
