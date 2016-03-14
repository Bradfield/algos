/*
Quick and dirty literate coding style for multiple
languages.

To use, in a markdown file reference a code sample as:

  <!-- literate graphs/example.py -->

Placeholders of this form in any markdown file will
be replaced with the contents of the referenced file,
following two rules:

  1. Anything in a block comment will be concatenated
    to the markdown, for further processing; and,
  2. Anything _not_ in a block comment will be wrapped
    with markdown tags indicating that it is a section
    of code to be formatted in <pre><code></code></pre>
    tags and syntax highlighted further down the
    pipeline.

For instance, a Python literate program like so:

  """
  A **comment**
  """
  def foo(): pass

Will be converted to the following markdown in the
calling file:

  A **comment**

  ```python
  def foo(): pass
  ```
*/

'use strict'

const assert = require('assert')
const _ = require('lodash')


const placeholders = /<!-- literate (.+) -->/g


const languages = {
  py: {
    blockComment: /"""\n([\s\S]+?)\n^"""/gm,
    pragmas: /^# -\*-.+-\*-\n/g,
    syntax: 'python',
  },
  js: {
    blockComment: /\/\*\n([\s\S]+?)\n^\*\//gm,
    pragmas: /^'use strict';?\n/g,
    syntax: 'javascript',
  }
}


const removePragmas = (config, content) =>
  content.replace(config.pragmas, '')


const invert = (config, content) =>
  '```' + config.syntax + '\n' +
  content.replace(config.blockComment, '```\n$1\n```' + config.syntax) +
  '\n```'


const removeEmptyCodeBlocks = (config, content) => {
  const emptyBlocks = new RegExp('```' + config.syntax + '\n+```', 'g')
  return content.replace(emptyBlocks, '')
}


const stripNewlinesInCodeBlocks = (config, content) => {
  const multipeNewlines = new RegExp('```' + config.syntax + '\n+', 'g')
  return content
    .replace(multipeNewlines, '```' + config.syntax + '\n')
    .replace(/\n+```/g, '\n```')
}


const conversionSteps = (config) =>
  ([
    removePragmas,
    invert,
    removeEmptyCodeBlocks,
    stripNewlinesInCodeBlocks
  ].map(f => _.partial(f, config)))


const converted = (steps, fileContent) =>
   _.flow.apply(null, steps)(fileContent)


// Return a function which when called with `replace`
// returns the markdown form of the referenced literate
// code
const replacePlaceholders = (files) =>
  (m, targetFilename) => {
    const ext = targetFilename.split('.')[1]
    const fileContent = files[targetFilename].contents.toString('utf8')
    const config = languages[ext]
    const steps = conversionSteps(config)

    return converted(steps, fileContent)
  }


// For each markdown file, find placeholders and replace
// with the converted form of the referenced files
const incorporateLiterateCode = (files) => {
  const replacer = replacePlaceholders(files)
  for (let path in files) {
    if (path.search('\.md$') === -1) continue

    const file = files[path]
    const fileContent = file.contents.toString('utf8')
    const replaced = fileContent.replace(placeholders, replacer)

    // Unfortunately, the contract is that we mutate the existing
    // file.contents
    file.contents = new Buffer(replaced, 'utf8')
  }
}

module.exports = { incorporateLiterateCode }


/* TESTS */

const test = () => {
  // Most of the literate code plugin is plumbing; the
  // important thing to test is the conversion from
  // literate form to markdown, as it uses a series
  // of fiddly rexexp

  const convertPython = _.partial(converted, conversionSteps(languages.py))
  const convertJS = _.partial(converted, conversionSteps(languages.js))

  assert.equal(convertPython(`
"""
A comment with _markdown_
"""
def foo_bar_baz():
    pass
`),
    `
A comment with _markdown_
\`\`\`python
def foo_bar_baz():
    pass
\`\`\``)

  assert.equal(convertJS(`
/*
A comment with _markdown_
*/
const foo = () => {}
`),
    `
A comment with _markdown_
\`\`\`javascript
const foo = () => {}
\`\`\``)

}

if (process.env.TEST) test()


