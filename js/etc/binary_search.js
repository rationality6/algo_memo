class Test {
  static assertEquals(a, b) {
    console.log(a == b);
  }
}

//Char Count: X
function z(l) {
  let c = 0
  let h = l
  while (1 <= h) {
    h = h / 2
    c += 1
  }
  return c
}


Test.assertEquals(z(1), 1);
Test.assertEquals(z(2), 2);
Test.assertEquals(z(4), 3);
Test.assertEquals(z(999), 10);
Test.assertEquals(z(1000), 10);



// describe("function z", function() {
//   it("should exist", function() {
//     Test.expect(!!z, "function z does not exist");
//   });
//
//   it("should calculate the correct answer", function() {
//     Test.assertEquals(z(1), 1);
//     Test.assertEquals(z(2), 2);
//     Test.assertEquals(z(4), 3);
//     Test.assertEquals(z(999), 10);
//     Test.assertEquals(z(1000), 10);
//   });
//
//   it("should be <=100 characters", function() {
//     var len = z.toString().length;
//     if (len <= 100) {
//       console.log("z is " + len + " characters long.  Don't forget to add a comment!");
//       Test.expect(true);
//     } else {
//       Test.expect(false, "z is more than 100 characters");
//     }
//   });
// });
