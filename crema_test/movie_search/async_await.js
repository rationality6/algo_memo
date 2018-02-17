const searchMovieDatas = async (TITLE, URI) => {
  const titleURI = URI + `search/?Title=${TITLE}`
  const body = await httpsGet(URI)
  return {
    movieTitles: body.data.map(x => x.Title),
    totalPage: body.total_pages,
    titleURI
  }
}

const promiseWrapForNextPages = async (URI, nextPage) => {
  URI = URI + `&page=${nextPage}`
  const body = await httpsGet(URI)
  const movies = body.data.map(x => x.Title)
  return movies
}

const solution = async (TITLE, URI) => {
  const resObj = await searchMovieDatas(TITLE, URI)
  const pageLength = resObj.totalPage
  let promiseJar = []

  // Into the jar
  for (let i = 2; i <= pageLength; i += 1) {
    promiseJar.push(promiseWrapForNextPages(resObj.titleURI, i))
  }

  // Concat and sorting
  const anotherMovieTitles = await Promise.all(promiseJar)
  const flattenArray = anotherMovieTitles.reduce((a, b) => a.concat(b))
  const resultSorted = resObj.movieTitles.concat(flattenArray).sort()
  console.log(resultSorted)
}

const queryURI = `https://jsonmock.hackerrank.com/api/movies/`

solution('spiderman', queryURI)
// solution('world', queryURI)
