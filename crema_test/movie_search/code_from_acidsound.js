// A code from Acidsound
const _range = (start,end)=> {
  let range=[];
  for (let i=start; i<end; i++) range.push(i);
  return range;
};

const Fetch = (uri)=>
  new Promise((resolve, reject)=>
    require('https').get(uri, res=>{
      let chunk="";
      res.setEncoding('utf8');
      res.on('data', body => chunk+=body);
      res.on('end', ()=> resolve(JSON.parse(chunk)));
    })
  );

const queryURI = "https://jsonmock.hackerrank.com/api/movies/search/?Title=";

const getMovieTitles = (subject)=>
  Fetch(`${queryURI}${subject}`)
  .then(o=>({o: Promise.resolve(o), pages: o.total_pages}))

  .then(({o,pages})=>[o, ..._range(2, pages + 1).map(v=>
    Fetch(`${queryURI}${subject}&page=${v}`)
  )])
  .then(o=>Promise.all(o))
  // .then(o=>[].concat(...o.map(o=>o.data))) // flatten
  // .then(o=>o.map(o=>o.Title))
  // .then(o=>o.sort());

getMovieTitles('spiderman')
  .then(console.log);
