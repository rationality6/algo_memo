const https = require('https');

const httpsGet = (url) => {
  return new Promise(resolve => {
    https.get(url, res => {
      res.setEncoding('utf8')
      res.on('data', body => {
        body = JSON.parse(body)
        resolve(body)
      })
    })
  })
}

const getMovieTitles = async substr => {
  const url = `https://jsonmock.hackerrank.com/api/movies/search/?Title=${substr}`
  const body = await httpsGet(url)
  const movieTitles = body.data.map(x => x.Title)
  const totalPage = body.total_pages
  return [url, movieTitles, totalPage]
}

const promiseWrap = async (substr, nextPage) => {
  const url = substr + `&page=${nextPage}`
  const body = await httpsGet(url)
  const movies = body.data.map(x => x.Title)
  return movies
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

// solution('spiderman')
solution('world')
