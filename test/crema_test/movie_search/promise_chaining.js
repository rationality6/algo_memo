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
      console.log(o);
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
