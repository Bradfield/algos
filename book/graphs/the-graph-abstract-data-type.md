---
title: The Graph Abstract Data Type
layout: default.html
collection: graphs
position: 2
---

The graph abstract data type (ADT) is defined as follows:

-   `Graph()` creates a new, empty graph.
-   `add_vertex(vertex)` adds an instance of `Vertex` to the graph.
-   `add_edge(from_vertex, to_vertex)` Adds a new, directed edge to the graph
    that connects two vertices.
-   `add_edge(from_vertex, to_vertex, weight)` Adds a new, weighted, directed
    edge to the graph that connects two vertices.
-   `get_vertex(key)` finds the vertex in the graph named `key`.
-   `get_vertices()` returns the list of all vertices in the graph.
-   `in` returns `True` for a statement of the form `vertex in graph`,
    if the given vertex is in the graph, `False` otherwise.

Beginning with the formal definition for a graph there are several ways
we can implement the graph ADT in Python. We will see that there are
trade-offs in using different representations to implement the ADT
described above. There are two well-known implementations of a graph,
the **adjacency matrix** and the **adjacency list**. We will explain
both of these options, and then implement one as a Python class.
