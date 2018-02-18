const axios = require('/Users/codepawn/github/algo_memo/crema_test/with_axios/node_modules/axios/lib/axios.js')

const queryURI = `https://jsonmock.hackerrank.com/api/movies/`

const _range = (S, E) => [...Array(E - S).keys()].map(s => s + S)

const solution = (TITLE, URI) => {
  const titleURI = URI + `search/?Title=${TITLE}`
  return axios.get(titleURI)
    .then(i => {
      return {
        o:Promise.resolve(i),
        totalPages: i.data.total_pages,
      }
    })
    .then(({o,totalPages}) => {
      return [o, ..._range(2, totalPages + 1).map(p => {
        const withPageURI = titleURI + `&page=${p}`
        return axios.get(withPageURI)
      })]
    })
    .then(j => Promise.all(j))
    .then(j => j.map((x)=>x.data))
    .then(k => [].concat(...k.map(k => k.data)))
    .then(l => l.map(l => l.Title).sort())
}

solution('spiderman', queryURI)
  .then(console.log)
