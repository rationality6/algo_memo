// Task 1
//
// Build a responsive web application to calculate simple and compound interest.
//
// 1. User should be able to select one of the 2 options - Simple or Compound interest.
// 2. Depending on the options chosen by the user, following fields should be shown: principal, rate of interest, time period, compound frequency(yearly, half yearly etc.)
// 3. User should be able to fill these fields
// 4. User should be to see the result when clicks the button - Result should include:
//
// a table that shows calculated interests and total amounts for each year
// At the bottom - Grand total of interest and amount for all the years
// Note - Write test cases
//
// Technology Stack:
//
// ReactJs, Redux

class Test {
  static assertEquals(answerFunc, answer) {
    console.log(Math.round(answerFunc, 3) === Math.round(answer, 3))
  }
  static it(test_log) {
    console.log(test_log);
  }
}

// principal, rate, time
const getInterest = (principal, rate, time) => {
  return principal + principal * rate * time
}

const getCompoundInterest = (principal, rate, compound, time) => {
  return principal * (1 + rate / compound) ** time
}

// console.log(getInterest(100, 0.1, 12))
console.log(getCompoundInterest(100, 0.1, 6, 12))

Test.it('STATIC TESTS')
// Test.assertEquals(getInterest(100, 0.1, 12), (100 + 100 * 0.1 * 12))
Test.assertEquals(getCompoundInterest(100, 0.1, 6, 12), (100 * (1 + 0.1 / 6) ** 12))

// test
// console.log(100 + 100 * 0.1 * 12);
console.log(100 * (1 + 0.1 / 12) ** 12 * 1);
console.log(100 * (1 + 0.1) ** (12 / 12));

console.log(100 * (1 + 0.1 / 1) ** (1 * (2/12)))

console.log(100 * (1 + (0.1 * (2/12))));
