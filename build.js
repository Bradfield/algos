import collections from 'metalsmith-collections'
import drafts from 'metalsmith-drafts'
import layouts from 'metalsmith-layouts'
import markdown from 'metalsmith-markdown'
import Metalsmith from 'metalsmith'
import permalinks from 'metalsmith-permalinks'

import { convertToKatex } from './katex-plugin'
import { highlightCode } from './prism-plugin'
import { wrapFigures } from './captions-plugin'

const BUILD_DESTINATION = '/Users/ozan/tmp/algos-book-dev-build'

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
  metadata['tableOfContents'] = sections.map(([label, name]) => {
    return {
      sectionName: name,
      collection: (metadata[label] || []).sort(byPosition),
    }
  })
}

console.log(`Building to ${BUILD_DESTINATION} ..`)


const debugSingleFile = (targetPath) =>
  (files) => {
    for (let path in files) {
      if (path !== targetPath) delete files[path]
    }
  }


Metalsmith(__dirname)
.source('book')
.destination(BUILD_DESTINATION)
// .use(debugSingleFile('stacks/implementing-a-stack.md'))
.use(drafts())
.use(convertToKatex)
.use(highlightCode)
.use(collections(collectionConfig))
.use(markdown({ tables: true }))
.use(wrapFigures)
.use(permalinks())
.use(generateTableOfContents)
.use(layouts({ engine: 'ejs' }))
.build(err => {
  console.log('Built')
  if (err) { throw err }
})
