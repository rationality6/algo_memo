const fibo = n => {
  arr = [];
  a = 0;
  b = 1;
  while (arr.length < n) {
    temp = a;
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

arr = [1, 2, 3];
