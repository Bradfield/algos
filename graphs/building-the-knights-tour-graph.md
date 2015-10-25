Building the Knight’s Tour Graph
================================

To represent the knight’s tour problem as a graph we will use the
following two ideas: Each square on the chessboard can be represented as
a node in the graph.

To build the full graph for an n-by-n board we can use the Python
function shown below. The `build_knight_graph` function makes one pass
over the entire board. At each square on the board the
`build_knight_graph` function calls a helper, `generate_legal_moves`, to
create a list of legal moves for that position on the board. All legal
moves are then converted into edges in the graph.

```python
from prior_section import Graph

def build_knight_graph(board_size):
    graph = Graph()
    for row in range(board_size):
        for col in range(board_size):
            for to_row, to_col in legal_moves_from(row, col, board_size):
                graph.add_edge((row, col), (to_row, to_col))
    return graph

```

The `legal_moves_from` generator below takes the position of the
knight on the board and yields any of the eight possible moves that are still on the board.

```python
MOVE_OFFSETS = (
              (-1, -2), ( 1, -2),
    (-2, -1),                     ( 2, -1),
    (-2,  1),                     ( 2,  1),
              (-1,  2), ( 1,  2),
)


def legal_moves_from(row, col, board_size):
    for row_offset, col_offset in MOVE_OFFSETS:
        move_row, move_col = row + row_offset, col + col_offset
        if 0 <= move_row < board_size and 0 <= move_col < board_size:
            yield move_row, move_col
```
The illustration below shows the complete graph of possible
moves on an eight-by-eight board. There are exactly 336 edges in the
graph. Notice that the vertices corresponding to the edges of the board
have fewer connections (legal moves) than the vertices in the middle of
the board. Once again we can see how sparse the graph is. If the graph
was fully connected there would be 4,096 edges. Since there are only 336
edges, the adjacency matrix would be only 8.2 percent full.

![All Legal Moves for a Knight on an 8x8 Chessboard](figures/knights-tour-legal-moves.png)
