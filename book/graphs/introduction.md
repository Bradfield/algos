---
title: Introduction to Graphs
layout: default.html
collection: graphs
position: 1
---

In this chapter we will study graphs. Graphs are a more general
structure than the trees we studied in the last chapter; in fact you can
think of a tree as a special kind of graph. Graphs can be used to
represent many interesting things about our world, including systems of
roads, airline flights from city to city, how the Internet is connected,
or even the sequence of classes you must take to complete a major in
computer science. We will see in this chapter that once we have a good
representation for a problem, we can use some standard graph algorithms
to solve what otherwise might seem to be a very difficult problem.

Below we introduce some definitions that will allow us to talk precisely
about graphs throughout the chapter.

**Vertex**

A vertex (also called a “node”) is a fundamental part of a graph. It
can have a name, which we will call the “key.” A vertex may also
have additional information, which we will call the “payload.”

**Edge**

An edge is another fundamental part of a graph. An edge connects two
vertices to show that there is a relationship between them. Edges may be
one-way or two-way. If the edges in a graph are all one-way, we say that
the graph is a **directed graph**, or a **digraph**.

**Weight**

Edges may be weighted to show that there is a cost to go from one vertex
to another. For example in a graph of roads that connect one city to
another, the weight on the edge might represent the distance between the
two cities.

With those definitions in hand we can formally define a graph. A graph
can be represented by $$G$$ where $$G =(V,E)$$. For the graph $$G$$,
$$V$$ is a set of vertices and $$E$$ is a set of edges. Each edge is a
tuple $$(v,w)$$ where $$w,v \in V$$. We can add a third component to the
edge tuple to represent a weight. A subgraph $$s$$ is a set of edges
$$e$$ and vertices $$v$$ such that $$e \subset E$$ and $$v \subset V$$.

The diagram below shows another example of a simple weighted digraph.
Formally we can represent this graph as the set of six vertices:

$$V = \left\{ V0,V1,V2,V3,V4,V5 \right\}$$

and the set of nine edges:

$$E = \left\{ \begin{array}{l}(v0,v1,5), (v1,v2,4), (v2,v3,9), (v3,v4,7), (v4,v0,1), \\
             (v0,v5,2),(v5,v4,8),(v3,v5,3),(v5,v2,1)
             \end{array} \right\}$$

![A simple example of a directed graph](figures/digraph.png)

The example above helps illustrate two other key graph terms:

**Path**

A path in a graph is a sequence of vertices that are connected by edges.
Formally we would define a path as $$w_1, w_2, ..., w_n$$ such that
$$(w_i, w_{i+1}) \in E$$ for all $$1 \le i \le n-1$$. The unweighted
path length is the number of edges in the path, specifically $$n-1$$.
The weighted path length is the sum of the weights of all the edges in
the path. For example in the above graph the path from $$V3$$ to $$V1$$
is the sequence of vertices $$(V3,V4,V0,V1)$$. The edges are
$$\left\{(v3,v4,7),(v4,v0,1),(v0,v1,5) \right\}$$.

**Cycle**

A cycle in a directed graph is a path that starts and ends at the same
vertex. For example, in the above graph the path $$(V5,V2,V3,V5)$$ is a
cycle. A graph with no cycles is called an **acyclic graph**. A directed
graph with no cycles is called a **directed acyclic graph** or a
**DAG**. We will see that we can solve several important problems if the
problem can be represented as a DAG.

The Graph Abstract Data Type
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
