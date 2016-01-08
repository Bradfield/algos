'use strict'

const _ = require('lodash')

const litpyMarker = /<!-- litpy (.+) -->/g

const removePragmas =
  content =>
    content.replace(/# -\*-.+-\*-\n/g, '')

const invert =
  content =>
    '```python\n' +
    content.replace(/"""\n([\s\S]+?)\n^"""/gm, '```\n$1\n```python') +
    '\n```'

const removeEmptyCodeBlocks =
  content =>
    content.replace(/```python\n+```/g, '')

const stripNewlinesInCodeBlocks =
  content =>
    content
      .replace(/```python\n+/g, '```python\n')
      .replace(/\n+```/g, '\n```')

const replacer =
  files =>
    (match, group) =>
      _.flow(
        removePragmas,
        invert,
        removeEmptyCodeBlocks,
        stripNewlinesInCodeBlocks
      )(files[group].contents.toString('utf8'))

const incorporateLiteratePython = files => {
  for (let path in files) {
    if (path.search('\.md$') !== -1) {
      const file = files[path]
      const replaced = file.contents.toString('utf8').replace(litpyMarker, replacer(files))
      file.contents = new Buffer(replaced, 'utf8')
    }
  }
}

module.exports = { incorporateLiteratePython }
