'use strict'


const addLanguageMarkers = (files) => {
  for (let path in files) {
    if (path.search('\.html$') === -1) continue

    const file = files[path]
    const replaced =
      file.contents.toString('utf8')
        .replace(/<!-- language (\w+) -->/g, '<div data-language="$1">')
        .replace(/<!-- \/language -->/g, '</div>')

      file.contents = new Buffer(replaced, 'utf8')
  }
}

module.exports = { addLanguageMarkers }
