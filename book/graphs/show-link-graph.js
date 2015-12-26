d3.json('/graphs/link-graph-data.json', (error, data) => {
  var graph = {
    nodes: [],
    links: []
  }

  var positionOfNode = {}

  for (var key in data) {
    var targets = data[key]
    if (positionOfNode[key]) {
      var nodePosition = positionOfNode[key]
    } else {
      var nodePosition = positionOfNode[key] = graph.nodes.length
      graph.nodes.push({ name: key, group: 1 })
    }

    for (var targetIndex in targets) {
      var targetKey = targets[targetIndex]
      if (positionOfNode[targetKey]) {
        var targetPosition = positionOfNode[targetKey]
      } else {
        var targetPosition = positionOfNode[targetKey] = graph.nodes.length
        graph.nodes.push({ name: targetKey, group: 1 })
      }
      graph.links.push({ source: nodePosition, target: targetPosition, value: 1 })
    }
  }

 var width = 720,
     height = 500;

 var svg = d3.select('#link-graph')
     .attr('width', width)
     .attr('height', height)

 var tooltip = d3.select('body')
   .append('div')
   .style({
     position: 'absolute',
     'z-index': 10,
     visibility: 'hidden',
   })

 var force = d3.layout.force()
     .nodes(graph.nodes)
     .links(graph.links)
     .size([width, height])
     .linkStrength(0.1)
     .friction(0.9)
     .linkDistance(20)
     .charge(-300)
     .gravity(0.1)
     .theta(0.08)
     .alpha(0.1)
     .start();

 var link = svg.selectAll('.link')
     .data(graph.links)
     .enter().append('line')
     .attr('class', 'link')

 var node = svg.selectAll('.node')
     .data(graph.nodes)
     .enter().append('circle')
     .attr('class', 'node')
     .attr('r', 3)
     .on('mouseover', function (d) {
       tooltip.text(d.name)
       tooltip.style({
         visibility: 'visible',
         top: d.y + 'px',
         left: (d.x + 20) + 'px',
       })
     })
     .on('mouseout', function () {
       tooltip.style('visibility', 'hidden')
     })

 // TODO: pre-compute
var r = 3
  force.on('tick', function () {
    node.attr('cx', function (d) { return d.x = Math.max(r, Math.min(width - r, d.x)) })
        .attr('cy', function (d) { return d.y = Math.max(r, Math.min(height - r, d.y)) })

    link.attr('x1', function (d) { return d.source.x })
        .attr('y1', function (d) { return d.source.y })
        .attr('x2', function (d) { return d.target.x })
        .attr('y2', function (d) { return d.target.y })
  })
})
