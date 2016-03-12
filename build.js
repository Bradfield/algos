'use strict'

const collections = require('metalsmith-collections')
const drafts = require('metalsmith-drafts')
const layouts = require('metalsmith-layouts')
const markdown = require('metalsmith-markdown')
const Metalsmith = require('metalsmith')
const permalinks = require('metalsmith-permalinks')

const { convertToKatex } = require('./katex-plugin')
const { incorporateLiterateCode } = require('./literate-code-plugin')
const { highlightCode } = require('./prism-plugin')
const { wrapFigures } = require('./captions-plugin')

process.env.SITE_ROOT = process.env.SITE_ROOT || '/'

const BUILD_DESTINATION = process.env.BUILD_DESTINATION || '/tmp/algos-book-dev-build'

const chapters = [
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
const collectionConfig = {}
const nextSection = {}
const previousSection = {}
chapters.forEach(([label, name], i) => {
  collectionConfig[label] = {
    sortBy: 'position',
    metadata: { name: name },
  }
  nextSection[label] = chapters[i + 1] ? chapters[i + 1][0] : null
  previousSection[label] = chapters[i - 1] ? chapters[i - 1][0] : null
})

const INDEX_PATH = 'index.html'

// UGH! fix this ugly hack around the fact that the collections plugin
// does not link previous/next between chapters
const bridgeLinksBetweenCollections =
  (files, metalsmith) => {
    for (let path in files) {
      // ignore non-html files
      if (path.search('\.html$') === -1) continue

      const file = files[path]
      // special case: link introduction to first section
      if (path === INDEX_PATH) {
        file.next = metalsmith._metadata.collections[chapters[0][0]][0]
        continue
      }

      if (file.collection.length === 1) {
        const collection = file.collection[0]
        if (file.next === undefined) {
          const nextCollection = nextSection[collection]
          if (nextCollection) {
            file.next = metalsmith._metadata.collections[nextCollection][0]
          }
        }
        if (file.previous === undefined) {
          const previousCollection = previousSection[collection]
          if (previousCollection) {
            const collection = metalsmith._metadata.collections[previousCollection]
            file.previous = collection[collection.length - 1]
          } else {
            // special case: link first section of first chapter back to intro
            file.previous = files[INDEX_PATH]
          }
        }
      }
    }
  }

const byPosition = (a, b) => a.position - b.position

const generateTableOfContents =
  (files, metalsmith) => {
    const metadata = metalsmith.metadata()
    metadata['tableOfContents'] = chapters.map(([label, name]) => {
      return {
        name: name,
        collection: (metadata[label] || []).sort(byPosition),
      }
    })
  }

console.log(`Building to ${BUILD_DESTINATION} ..`)

// const debugSingleFile =
//   (targetPath) =>
//     (files) => {
//       for (let path in files) {
//         if (path !== targetPath) delete files[path]
//       }
//     }

const EXCLUSION_FILE_PATTERNS = [
  '\.pyc$',
  '\.py$',
  '\.DS_STORE'
]

const removeNonPublicFiles =
  files => {
    for (let path in files) {
      for (let i in EXCLUSION_FILE_PATTERNS) {
        if (path.search(EXCLUSION_FILE_PATTERNS[i]) !== -1) {
          delete files[path]
          continue
        }
      }
    }
  }

if (!process.env.TEST) {
  Metalsmith(__dirname)
  .source('book')
  .destination(BUILD_DESTINATION)
  // .use(debugSingleFile('graphs/knights-tour.md'))
  .use(drafts())
  .use(incorporateLiterateCode)
  .use(convertToKatex)
  .use(highlightCode)
  .use(markdown({ tables: true }))
  .use(collections(collectionConfig))
  .use(bridgeLinksBetweenCollections)
  .use(wrapFigures)
  .use(removeNonPublicFiles)
  .use(permalinks())
  .use(generateTableOfContents)
  .use(layouts({ engine: 'ejs' }))
  .build(err => {
    console.log('Built')
    if (err) { throw err }
  })
}
