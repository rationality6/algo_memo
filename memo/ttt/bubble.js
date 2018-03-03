const swap = (a, b) => {}

const bubble_sort = L => {
  const length_list = L.length
  for (let i = length_list - 1; i > 0; i -= 1) {
    for (let j = 0; j < i; j += 1) {
      if (L[j + 1] < L[j]) {
        let temp = L[j]
        L[j] = L[j + 1]
        L[j + 1] = temp
      }
    }
  }
  return L
}

let array0 = [5, 4, 3, 2, 1]

console.log(bubble_sort(array0))
