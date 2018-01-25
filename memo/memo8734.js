const data0 = [
  {
    "main_genre": "미상",
    "nation": "홍콩",
    "running_time": null,
    "title": "상재아심",
    "year": "2001",
    "poster": "http://cdn.watcha.net/p/b54c96d745b617936d3f.jpg"
  }, {
    "main_genre": "미상",
    "nation": "프랑스",
    "running_time": 60,
    "title": "본 누벨",
    "year": "2001",
    "poster": "http://cdn.watcha.net/p/67361f75cc1da1a7586f.jpg"
  }
]

// console.log(data0)
for (let i = 0, len = data0.length; i < len; i += 1) {
  const me = data0[i]
  console.log(data0.indexOf(me))
}
