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

const generateLinkGraph = (startingUrl, maxDepth) => {
  const graph = {}
  const queue = [[startingUrl, 0]]
  let pendingRequests = 0
  while (queue.length > 0 || pendingRequests > 0) {
    const [location, depth] = queue.shift()
    if (depth < maxDepth) {
      const addLinkForUrl = addLink(graph, location)
      pendingRequests += 1
      request({ url: location, headers }, (error, response, body) => {
        pendingRequests -= 1
        if (error) return
        parseLinks(body, url.parse(location).host)
        .forEach(link => {
          addLinkForUrl(link)
          traverse(link, depth - 1)
        })
      })
    }
  }
  return graph
}

// const generateLinkGraph = (startingUrl, depth) => {
//   const graph = { }
//
//   const traverse = (location, depth) => {
//     if (depth === 0) return
//     if (graph[location]) return
//     const addLinkForUrl = addLink(graph, location)
//
//     // TODO: handle redundant requests
//     request({ url: location, headers }, (error, response, body) => {
//       if (error) return
//       parseLinks(body, url.parse(location).host)
//       .forEach(link => {
//         addLinkForUrl(link)
//         traverse(link, depth - 1)
//       })
//     })
//   }
//
//   traverse(startingUrl, depth)
//
//   return graph
// }

const graph = generateLinkGraph('http://localhost:8000/graphs/strongly-connected-components/', 3)

// TODO: actually, just wait
setTimeout(() => {
  for (let key in graph) {
    graph[key] = Array.from(graph[key])
  }
  console.log(JSON.stringify(graph))
}, 50000)
