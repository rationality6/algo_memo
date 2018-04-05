const randomBoolean = () => 0 === (Math.floor(Math.random() * 1))

const mockObj = {
  img: "",
  name: "동대문엽기떡볶이",
  location: "강남점",
  address: "서울시 강남구 대치동 890-47",
  like: randomBoolean()
}

let popularPlaces = []


for (let i = 0, len = 3; i < len; i += 1) {
  popularPlaces.push(mockObj)
}

console.log(popularPlaces);

console.log("foo")
