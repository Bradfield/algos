'use strict'

const imgTag = /<img .*? alt="([\s\S]*?)".*?>/g

const figureWithCaption = (match, group) => `
  <figure>
    ${match}
    <figcaption>${group}</figcaption>
  </figure>`

const wrapFigures = files => {
  for (let path in files) {
    if (path.search('\.html$') !== -1) {
      const file = files[path]
      const replaced = file.contents.toString('utf8').replace(imgTag, figureWithCaption)
      file.contents = new Buffer(replaced, 'utf8')
    }
  }
}

module.exports = { wrapFigures }
