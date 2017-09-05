const sumMatrix = (a, b) => {
  return a.map((c, d) => {
    console.log(c, "c");
    console.log(d, "d");
    return c.map((e, f) => {
      console.log(e, "e");
      console.log(f, "f");
      return e + b[d][f];
    });
  });
};

console.log(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]));
