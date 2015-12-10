
function isLeftNode (node) {
  return node.parent && node.parent.children && node.parent.children[0] == node
}

function isLeaf (node) {
  return !node.children
}

// TODO: this code could be less crappy overall

function drawTree (target, root) {
  var height = 270
  var width = 720
  var marginTop = 20

  var i = 0

  var tree = d3.layout.tree().size([height, width])

  var diagonal = d3.svg.diagonal()
   .projection(function (d) { return [d.x * 2.5, d.y] })

  var svg = d3.select(target)
   .attr('width', width)
   .attr('height', height + marginTop)
    .append('g')
    .attr('transform', 'translate(0,' + marginTop + ')')

  var nodes = tree.nodes(root).reverse()
  var links = tree.links(nodes)

  // Normalize for fixed-depth.
  nodes.forEach(function(d) { d.y = d.depth * 60 })

  // Declare the nodes
  var node = svg.selectAll('g.node')
   .data(nodes, function(d) { return d.id || (d.id = ++i) })

  // Enter the nodes.
  var nodeEnter = node.enter().append('g')
    .attr('class', 'graph-node')
    .attr('transform', function(d) {
      return 'translate(' + d.x * 2.5 + ',' + d.y + ')'
    })

  nodeEnter.append('circle').attr('r', 5)

  nodeEnter.append('text')
    .attr('x', function(d) {
      if (isLeaf(d)) return 0
      return isLeftNode(d) ? -10 : 10
    })
    .attr('y', function(d) {
      return isLeaf(d) ? 20 : 0
    })
    .attr('text-anchor', function(d) {
      if (isLeftNode(d)) return 'end'
      return isLeaf(d) ? 'middle' : 'start'
    })
    .text(function(d) { return d.name })

  // Declare the link
  svg.selectAll('path.link')
    .data(links, function(d) { return d.target.id })
    .enter().insert('path', 'g')
    .attr('class', 'graph-edge')
    .attr('d', diagonal)

}
