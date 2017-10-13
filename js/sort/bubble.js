const bubble_sort = arr => {
  let clone = arr.slice()
  for (let i = clone.length - 1; i > 0; i -= 1) {
    for (let z = 0; z < i; z += 1) {
      if (clone[z] > clone[z + 1]) {
        let temp = clone[z]
        clone[z] = clone[z + 1]
        clone[z + 1] = temp
      }
    }
  }
  return clone
}

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

const arr0 = [...Array(10).keys()]
const random_arr0 = get_shuffled_arr(arr0)
console.log(random_arr0);
console.log(bubble_sort(random_arr0));
