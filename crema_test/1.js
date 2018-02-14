const https = require('https');

const httpsGet = URI => {
  return new Promise(resolve => {
    https.get(URI, res => {
      res.setEncoding('utf8')
      let chunk = []
      res.on('data', body => {
        chunk += body
      })
      res.on('end', () => resolve(JSON.parse(chunk)));
    })
  })
}

const _range = (START, END) => {
  let jar = []
  for (let i = START; i < END; i += 1) {
    jar.push(i)
  }
  return jar
}

const queryURI = `https://jsonmock.hackerrank.com/api/movies/`

const solution = (TITLE, URI) => {
  const titleURI = URI + `search/?Title=${TITLE}`
  return httpsGet(titleURI)
    .then(i => {
      return {
        o: Promise.resolve(i),
        totalPages: i.total_pages,
      }
    })
    .then(({o,totalPages}) => {
      return [o, ..._range(2, totalPages + 1).map(p => {
        const withPageURI = titleURI + `&page=${p}`
        return httpsGet(withPageURI)
      })]
    })
    .then(j => Promise.all(j))
    .then(k => [].concat(...k.map(k => k.data)))
    .then(l => l.map(l => l.Title).sort())
}


solution('spiderman', queryURI)
  .then(console.log)


// const searchMovieDatas = async (TITLE, URI) => {
//   const titleURI = URI + `search/?Title=${TITLE}`
//   const body = await httpsGet(URI)
//   return {
//     movieTitles: body.data.map(x => x.Title),
//     totalPage: body.total_pages,
//     titleURI
//   }
// }
//
// const promiseWrapForNextPages = async (URI, nextPage) => {
//   URI = URI + `&page=${nextPage}`
//   const body = await httpsGet(URI)
//   const movies = body.data.map(x => x.Title)
//   return movies
// }
//
// const solution = async (TITLE, URI) => {
//   const resObj = await searchMovieDatas(TITLE, URI)
//   const pageLength = resObj.totalPage
//   let promiseJar = []
//
//   // Into the jar
//   for (let i = 2; i <= pageLength; i += 1) {
//     promiseJar.push(promiseWrapForNextPages(resObj.titleURI, i))
//   }
//
//   // Concat and sorting
//   const anotherMovieTitles = await Promise.all(promiseJar)
//   const flattenArray = anotherMovieTitles.reduce((a, b) => a.concat(b))
//   const resultSorted = resObj.movieTitles.concat(flattenArray).sort()
//   console.log(resultSorted)
// }
//
// const queryURI = `https://jsonmock.hackerrank.com/api/movies/`
//
// solution('spiderman', queryURI)
// // solution('world', queryURI)
