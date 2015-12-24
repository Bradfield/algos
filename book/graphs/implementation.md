---
title: Implementation
layout: chapter.html
collection: graphs
position: 5
---

Using dictionaries, it is easy to implement the adjacency list in
Python. In our implementation of the Graph abstract data type we will
create two classes, `Graph`, which holds the master list of vertices,
and `Vertex`, which will represent each vertex in the graph.

Each `Vertex` uses a dictionary to keep track of the vertices to which
it is connected, and the weight of each edge. If we weren't concerned
with edge weights, we could use a set in place of a dictionary. This
dictionary is called `neighbors`.

In the code below, The `add_neighbor` method is used add a connection
from this vertex to another. The `get_connections` method returns all of
the vertices in the adjacency list, as represented by the `neighbors`
instance variable. The `get_weight` method returns the weight of the
edge from this vertex to the vertex passed as a parameter.

```python
class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]
```

The `Graph` class, shown below, contains a dictionary that maps vertex
names to vertex objects. `Graph` also provides methods for adding
vertices to a graph and connecting one vertex to another. The
`get_vertices` method returns the names of all of the vertices in the
graph. In addition, we have implemented the `__iter__` method to make it
easy to iterate over all the vertex objects in a particular graph.
Together, the two methods allow you to iterate over the vertices in a
graph by name, or by the objects themselves.


```python
class Graph(object):
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.verticies[from_key].add_neighbor(self.verticies[to_key], weight)

    def get_vertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())
```

Using the `Graph` and `Vertex` classes just defined, the following
Python session creates our example graph.. First we create six vertices
numbered 0 through 5. Then we display the vertex dictionary. Notice that
for each key 0 through 5 we have created an instance of a `Vertex`.
Next, we add the edges that connect the vertices together. Finally, a
nested loop verifies that each edge in the graph is properly stored.

```
>>> g = Graph()
>>> for i in range(6):
...     g.add_vertex(Vertex(i))
>>> g.verticies
{0: <adjGraph.Vertex instance at 0x41e18>,
 1: <adjGraph.Vertex instance at 0x7f2b0>,
 2: <adjGraph.Vertex instance at 0x7f288>,
 3: <adjGraph.Vertex instance at 0x7f350>,
 4: <adjGraph.Vertex instance at 0x7f328>,
 5: <adjGraph.Vertex instance at 0x7f300>}
>>> g.add_edge(0, 1, 5)
>>> g.add_edge(0, 5, 2)
>>> g.add_edge(1, 2, 4)
>>> g.add_edge(2, 3, 9)
>>> g.add_edge(3, 4, 7)
>>> g.add_edge(3, 5, 3)
>>> g.add_edge(4, 0, 1)
>>> g.add_edge(5, 4, 8)
>>> g.add_edge(5, 2, 1)
>>> for v in g:
...     for w in v.get_connections():
...         print('{} -> {}'.format(v.key, w.key))
...
0 -> 5
0 -> 1
1 -> 2
2 -> 3
3 -> 4
3 -> 5
4 -> 0
5 -> 4
5 -> 2
```
