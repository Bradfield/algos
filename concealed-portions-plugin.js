

const addConcealmentMarkers = (files) => {
  for (let path in files) {
    if (path.search('\.html$') === -1) continue

    const file = files[path]
    const replaced =
      file.contents.toString('utf8')
        .replace(/<!-- concealed -->/g, '<div class="concealed">')
        .replace(/<!-- \/concealed -->/g, '</div>')

      file.contents = new Buffer(replaced, 'utf8')
  }
}

module.exports = { addConcealmentMarkers }
