// 문제
// "ab2v9bc13j5jf4jv21" => 9^2 + 13^2 + 5^2 + 21^2 = 716
// 찾을수있는 가능한 패턴
// 1.숫자를 추출한다
// 2.짝수를 제외한 숫자들을 제곱한뒤 더한다

class Test {
  static assertEquals(a, b) {
    console.log(a === b);
  }
}

const secretString = "ab2v9bc13j5jf4jv21"

const findPattern = L => L.match(/\d+/g).filter(x => x % 2 !== 0).map(y => Math.pow(y, 2)).reduce((a, b) => a + b)

const result = findPattern(secretString)
const answerCalResult = (Math.pow(9, 2) + Math.pow(13, 2) + Math.pow(5, 2) + Math.pow(21, 2))
Test.assertEquals(result, answerCalResult)
