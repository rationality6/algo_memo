class TimesTable {
  constructor() {
    this.arr = [];
  }
  makeTimesTable(n, y) {
    const TTA = this.returnTimesTableArray(n, y);
    TTA.forEach((items, index) => {
      items.forEach((a, b) => {
        this.arr.push(a);
      });
    });
  }
  returnTimesTableArray(n, y) {
    return [...Array(n + 1).keys()].map(a => {
      return [...Array(y + 1).keys()].map(x => {
        return `${a} * ${x} = ${a * x}`;
      });
    });
  }
  printing() {
    return this.arr;
  }
}

t0 = new TimesTable();
t0.makeTimesTable(9, 9);
console.log(t0.printing());
