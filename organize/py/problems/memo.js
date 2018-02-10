let state = {
  title: "j"
}

// let state = {
//   title: "",
//   id: 2
// }

const {title} = state
const id = 3
console.log({title, id})

console.log()

const a = 3
let value = a === null
  ? 0
  : a
console.log(value);

const p = 1000
const arr0 = [1200, 2400, 3600]
const addAmountToInterest = (arr, p) => arr.map(x => x + p)
console.log(addAmountToInterest(arr0, p))

const v = {
  a: [1, 2, 3]
}

console.log(v.a[4]) {
  "threeYearInterests" : [
    10.000000000000014, 20, 30
  ],
  "threeYearInterestsAndAmount" : [
    110.00000000000001, 120, 130
  ],
  "totalAmount" : 102
}

  {
    "threeYearInterests": [
      10, 21, 33
    ],
    "threeYearInterestsAndAmount": [
      110, 121, 133
    ],
    "totalAmount": 102
  }



let a = [1,2,3]
const b = [1,2,3]
console.log(a===b);
a = b
console.log(a===b);
