const https = require('https');

const getMovieTitles = substr => {
  return new Promise(resolve => {
    const url = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr
    https.get(url, res => {
      res.setEncoding('utf8')
      res.on('data', body => {
        body = JSON.parse(body)
        const movies = body.data.map(x => x.Title)
        const totalPage = body.total_pages
        resolve([substr, movies, totalPage])
      })
    })
  })
}

const promiseWrap = (substr, nextPage) => {
  return new Promise(resolve => {
    let url1 = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr + "&page=" + nextPage;
    https.get(url1, res => {
      res.setEncoding('utf8');
      res.on('data', body => {
        body = JSON.parse(body)
        const movies = body.data.map(x => x.Title)
        resolve(movies)
      })
    })
  })
}

const solution = async T => {
  const res0 = await getMovieTitles(T)
  const pageLength = res0[2]
  let promiseJar = []

  // Into jar
  for (let i = 1; i < pageLength; i += 1) {
    const numberRevise = i + 1
    promiseJar.push(promiseWrap(res0[0], numberRevise))
  }

  // Concat and sorting
  const res1 = await Promise.all(promiseJar)
  const flattenArray = res1.reduce((a, b) => a.concat(b))
  const resultSorted = res0[1].concat(flattenArray).sort()
  console.log(resultSorted)
}

solution('spiderman')
