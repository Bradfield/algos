const collections = require('metalsmith-collections')
const layouts = require('metalsmith-layouts')
const markdown = require('metalsmith-markdown')
const Metalsmith = require('metalsmith')
const permalinks = require('metalsmith-permalinks')

const BUILD_DESTINATION = '/Users/ozan/tmp/algos-book-dev-build'

console.log(`Building to ${BUILD_DESTINATION} ..`)


const sections = [
  ['analysis', 'Analysis'],
  ['stacks', 'Stacks'],
  ['queues', 'Queues'],
  ['deques', 'Deques'],
  ['lists', 'Lists'],
  ['recursion', 'Recursion'],
  ['searching', 'Searching'],
  ['trees', 'Trees'],
  ['graphs', 'Graphs'],
]
const collectionConfig = new Map(
  sections.map(([label, name]) => [label, {
    sortBy: 'position',
    metadata: { name: name },
  }])
)

const byPosition = (a, b) => a.position - b.position

const generateTableOfContents = (files, metalsmith) => {
  const metadata = metalsmith.metadata()
  metadata['index'] = sections.map(([label, name]) => {
    return {
      sectionName: name,
      collection: (metadata[label] || []).sort(byPosition),
    }
  })
}


Metalsmith(__dirname)
.source('book')
.destination(BUILD_DESTINATION)
.use(collections(collectionConfig))
.use(markdown({ tables: true }))
.use(permalinks())
.use(generateTableOfContents)
.use(layouts({ engine: 'handlebars' }))
.build(err => {
  console.log('Built')
  if (err) { throw err }
})
