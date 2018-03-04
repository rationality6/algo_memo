class Frequncy {
  constructor() {
    this.result = "";
  }
  logic(input) {
    let obj = {};
    const splitedInput = input.split("");
    const sortedInput = splitedInput.sort();
    sortedInput.forEach((a, b) => (obj[a] = 0));
    for (let z = 0, len = sortedInput.length; z < len; z += 1) {
      for (let i in obj) {
        if (i === sortedInput[z]) {
          obj[i]++;
        }
      }
    }
    for (let i in obj) {
      this.result += `${i}${obj[i]}`;
    }
  }
  print() {
    return this.result;
  }
}

const frequncy0 = new Frequncy();

const example = "babdc";

frequncy0.logic(example);

console.log(frequncy0.print())
// assign a1b2c1d1, a1b2c1d1
