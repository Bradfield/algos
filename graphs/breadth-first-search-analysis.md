Breadth First Search Analysis
=============================

Before we continue with other graph algorithms let us analyze the run
time performance of the breadth first search algorithm. The first thing
to observe is that the while loop is executed, at most, one time for
each vertex in the graph $|V|$. You can see that this is true because a
vertex must be white before it can be examined and added to the queue.
This gives us $O(V)$ for the while loop. The for loop, which is nested
inside the while is executed at most once for each edge in the graph,
$|E|$. The reason is that every vertex is dequeued at most once and we
examine an edge from node $u$ to node $v$ only when node $u$ is
dequeued. This gives us $O(E)$ for the for loop. combining the two loops
gives us $O(V + E)$.

Of course doing the breadth first search is only part of the task.
Following the links from the starting node to the goal node is the other
part of the task. The worst case for this would be if the graph was a
single long chain. In this case traversing through all of the vertices
would be $O(V)$. The normal case is going to be some fraction of $|V|$
but we would still write $O(V)$.

Finally, at least for this problem, there is the time required to build
the initial graph. We leave the analysis of the `buildGraph` function as
an exercise for you.
