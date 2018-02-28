const fibo = n => {
  let arr = [];
  let a = 0;
  let b = 1;
  while (arr.length < n) {
    let temp = a;
    a = b;
    b = temp + b;
    arr.push(a);
  }
  return arr;
};

console.log(fibo(10));

const fibo = n => {
  if (n < 2) {
    return n;
  } else {
    return fibo(n - 1) + fibo(n - 2);
  }
};

let arr = [1, 2, 3];

const foobar = n => {
  return n
}
foobar("Hello world")
