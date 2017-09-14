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

const ex = [5, 2, 4, 7, 6, 1, 3, 8];
console.log(mergeSort(ex));
