const get_shuffled_arr = arr => {
  let clone = arr.slice()
  for (let i = 0, len = clone.length - 1; i < len; i += 1) {
    const ran = Math.round(Math.random() * arr.length)
    const temp = clone[i]
    clone[i] = clone[ran]
    clone[ran] = temp
  }
  return clone
}

const merge = (left, right) => {
  let result = [];
  while (left.length && right.length) {
    if (left[0] <= right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  while (left.length) result.push(left.shift());
  while (right.length) result.push(right.shift());
  return result;
};

const mergeSort = array => {
  if (array.length < 2) return array;
  const pivot = Math.floor(array.length / 2);
  let left = array.slice(0, pivot);
  let right = array.slice(pivot, array.length);
  return merge(mergeSort(left), mergeSort(right));
};

// const ex = [5, 2, 4, 7, 6, 1, 3, 8, 9];
const arr0 = [...Array(10).keys()]
const random_arr0 = get_shuffled_arr(arr0)
console.log(random_arr0);
console.log(mergeSort(random_arr0));
