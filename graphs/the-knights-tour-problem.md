The Knight’s Tour Problem
=========================

The “[knight’s tour](https://en.wikipedia.org/wiki/Knight%27s_tour)” is
a classic problem in graph theory, first posed over 1,000 years ago and
pondered by legendary mathematicians including Leonhard Euler before
finally being solved in 1823. We will use the knight's tour problem to
illustrate a second common graph algorithm called depth first search.

The knight’s tour puzzle is played on a chess board with a single chess
piece, the knight. The object of the puzzle is to find a sequence of
moves that allow the knight to visit every square on the board exactly
once, like so:

![One possible knight's tour](figures/knights-tour.gif)

One such sequence is called a “tour.” The upper bound on the
number of possible legal tours for an eight-by-eight chessboard is known
to be $$1.305 \times 10^{35}$$; however, there are even more possible
dead ends. Clearly this is a problem that requires some real brains,
some real computing power, or both.

Once again we will solve the problem using two main steps:

-   Represent the legal moves of a knight on a chessboard as a graph.
-   Use a graph algorithm to find a path of length
    $$rows \times columns - 1$$ where every vertex on the graph is visited
    exactly once.
