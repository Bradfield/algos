/* eslint-disable no-unused-vars */

function isLeftNode (node) {
  return node.parent && node.parent.children && node.parent.children[0] === node
}

function isLeaf (node) {
  return !node.children
}

// TODO: this code could be less crappy overall

function drawTree (target, root) {
  const height = 270
  const width = 720
  const marginTop = 20

  let i = 0

  const tree = d3.layout.tree().size([height, width])

  const diagonal = d3.svg.diagonal()
   .projection(function (d) { return [d.x * 2.5, d.y] })

  const svg = d3.select(target)
   .attr('width', width)
   .attr('height', height + marginTop)
    .append('g')
    .attr('transform', 'translate(0,' + marginTop + ')')

  const nodes = tree.nodes(root).reverse()
  const links = tree.links(nodes)

  // Normalize for fixed-depth.
  nodes.forEach(function (d) { d.y = d.depth * 60 })

  // Declare the nodes
  const node = svg.selectAll('g.node')
   .data(nodes, function (d) { return d.id || (d.id = ++i) })

  // Enter the nodes.
  const nodeEnter = node.enter().append('g')
    .attr('class', 'graph-node')
    .attr('transform', function (d) {
      return 'translate(' + d.x * 2.5 + ',' + d.y + ')'
    })

  nodeEnter.append('circle').attr('r', 5)

  nodeEnter.append('text')
    .attr('x', function (d) {
      if (isLeaf(d)) return 0
      return isLeftNode(d) ? -10 : 10
    })
    .attr('y', function (d) {
      return isLeaf(d) ? 20 : 0
    })
    .attr('text-anchor', function (d) {
      if (isLeftNode(d)) return 'end'
      return isLeaf(d) ? 'middle' : 'start'
    })
    .text(function (d) { return d.name })

  // Declare the link
  svg.selectAll('path.link')
    .data(links, function (d) { return d.target.id })
    .enter().insert('path', 'g')
    .attr('class', 'graph-edge')
    .attr('d', diagonal)
}

function drawScatter (target, data, xLabel, yLabel, xDomain, yDomain) {

  const margin = {top: 20, right: 30, bottom: 30, left: 40},
      width = 720 - margin.left - margin.right,
      height = 240 - margin.top - margin.bottom

  const x = d3.scale.linear().range([0, width])
  const y = d3.scale.linear().range([height, 0])

  const xAxis = d3.svg.axis().scale(x).orient('bottom')
  const yAxis = d3.svg.axis().scale(y).orient('left')

  const svg = d3.select(target)
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
    .append('g')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')


  x.domain(xDomain || d3.extent(data, d => d.x)).nice()
  y.domain(yDomain || d3.extent(data, d => d.y)).nice()

  svg.append('g')
      .attr('class', 'x axis')
      .attr('transform', 'translate(0,' + height + ')')
      .call(xAxis)
    .append('text')
      .attr('class', 'label')
      .attr('x', width)
      .attr('y', -6)
      .style('text-anchor', 'end')
      .text(xLabel)

  svg.append('g')
      .attr('class', 'y axis')
      .call(yAxis)
    .append('text')
      .attr('class', 'label')
      .attr('transform', 'rotate(-90)')
      .attr('y', 6)
      .attr('dy', '.71em')
      .style('text-anchor', 'end')
      .text(yLabel)

  svg.selectAll('.dot')
      .data(data)
    .enter().append('circle')
      .attr('class', 'dot')
      .attr('r', 3.5)
      .attr('cx', d => x(d.x))
      .attr('cy', d => y(d.y))

}
