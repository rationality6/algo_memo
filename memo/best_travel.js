class Test {
  assert_equals(anwser_func, anwser) {
    console.log(anwser_func === anwser)
  }
}

test = new Test()


const chooseBestSum = (t, k, ls) => {
  if (ls.length < 3)
    return null;
  let res = 0;

  function dfs(t, k, ls, start, path) {
    if (path.length == k) {
      let sum = path.reduce((a, b) => a + b, 0)
      if (sum <= t)
        res = Math.max(res, sum);
      return;
    }
    for (let i = start; i < ls.length; i++) {
      path.push(ls[i]);
      dfs(t, k, ls, i + 1, path);
      path.pop();
    }
  }
  dfs(t, k, ls, 0, []);
  return res === 0 ? null : res;
}

const xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

test.assert_equals(chooseBestSum(230, 4, xs), 230)
test.assert_equals(chooseBestSum(430, 5, xs), 430)
test.assert_equals(chooseBestSum(430, 8, xs), null)


[...Array(5).keys()].map(a => console.log(a))
