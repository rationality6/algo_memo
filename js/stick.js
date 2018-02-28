const stick_price = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30];

const cutRod = (price, n) => {
  let r = [0];

  for (let j = 1; j <= n; j++) {
    let q = 0;

    for (let i = 1; i <= j; i++) {
      console.log(`${price[i]} + ${r[j - i]}`, price[i] + r[j - i]);
      q = Math.max(q, price[i] + r[j - i]);
    }

    // console.log(q, "q");
    r[j] = q;
  }
  // console.log(r, "r");
  // console.log(n, "n");
  return r[n];
};

// console.log(cutRod(stick_price, 0));
// console.log(cutRod(stick_price, 1));
// console.log(cutRod(stick_price, 2)); // 5
// console.log(cutRod(stick_price, 3)); // 8
console.log(cutRod(stick_price, 4)); // 10
// console.log(cutRod(stick_price, 7)); // 18


var value = 100;
var myObj = {
  value: 1,
  func1() {
    console.log(`func1's this.value: ${this.value}`);

    var func2 = function() {
      console.log(`func2's this.value ${this.value}`);
    }.bind(this);
    func2();
  }
};

myObj.func1();
