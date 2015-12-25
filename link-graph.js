'use strict'

const jsdom = require('jsdom').jsdom
const request = require('request')
const url = require('url')

const headers = {
  'Accept': 'text/html',
}

const addLink = (graph, prior) =>
  (link) => {
    graph[prior] = graph[prior] || new Set()
    graph[prior].add(link)
  }

const parseLinks = (markup, host) =>
  Array.from(jsdom(markup).getElementsByTagName('a'))
  .map(a => a.href)
  .map(href => href.slice(0, 4) === 'http' ? href : `http://${host}${href}`)

const generateLinkGraph = (startingUrl, depth) => {
  const graph = { }

  const traverse = (location, depth) => {
    if (depth === 0) return
    if (graph[location]) return
    const addLinkForUrl = addLink(graph, location)
    console.log('traversing', location)
    request({ url: location, headers }, (error, response, body) => {
      if (error) return
      parseLinks(body, url.parse(location).host)
      .forEach(link => {
        addLinkForUrl(link)
        traverse(link, depth - 1)
      })
    })
  }

  traverse(startingUrl, depth)

  return graph
}

const graph = generateLinkGraph('https://www.wikipedia.org', 3)

setTimeout(() => console.log(graph), 20000)
