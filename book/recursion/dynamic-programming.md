---
title: Dynamic Programming
layout: default.html
collection: recursion
position: 7
---

Dynamic programming is a powerful technique for solving a certain class
of problems, typically in a more efficient manner than the corresponding
recursive strategy. Specifically, when a problem consists of
“overlapping subproblems,” a recursive strategy may lead to redundant
computation. The corresponding dynamic programming strategy may
avoid such waste by addressing and solving the subproblems one at a time
in a manner without overlap.

This idea is difficult to understand in the abstract, so let’s consider
a couple of examples.

Firstly, let’s write a function to return the nth Fibonacci number: the nth
number in the sequence constructed by starting with $$0, 1$$ and calculating
subsequent numbers as the sum of the previous two numbers, like so:

$$0, 1, 1, 2, 3, 5, 8, 13, 21 ...$$

The Fibonacci sequence may be familiar enough to you that you are able
to take a “top down” approach: identifying the
recursive relationship simply by considering the definition of the
Fibonacci sequence. In other words, a “top down” approach considers the
statement “calculating subsequent numbers as the sum of the previous two
numbers” and recognizes the relationship $$f(n) = f(n-1) + f(n-2)$$.

With 0 and 1 as our base cases, this leads to an implementation in code that
looks very much like the mathematical definition of the sequence:

<!-- language python -->
```python
def fib(n):
    if n <= 1:
        return n  # base cases: return 0 or 1 if n is 0 or 1, respectively
    return fib(n - 1) + fib(n - 2)
```
<!-- /language -->

<!-- language javascript -->
```javascript
const fib = (n) => {
  if (n <= 1) return n
  return fib(n - 1) + fib(n - 2)
}
```
<!-- /language -->

This is a correct solution, but it poses a problem evident to those who run
`fib(50)` and wait for an answer. The running time of this implementation is
$$O(2^n)$$ due to a very large number of redundant recursive executions. When
we call `fib(n)` we recursively call `fib(n - 1)` and `fib(n - 2)` which
themselves call (i) `fib(n - 2)` and `fib(n - 3)`; and, (ii) `fib(n - 3)`
and `fib(n - 4)`, respectively.

We can see that there are some redundant calls,
and you may recognize that each of those redundant calls trigger trees of
further entirely redundant calls. This can be seen more clearly by drawing out
the call tree for `fib(5)`, as we do below:

<figure>
  <svg id="fib-5-call-tree" />
</figure>

<script>
drawTree('#fib-5-call-tree', {
  name: 'fib(5)',
  children: [
    {
      name: 'fib(4)',
      children: [
        {
          name: 'fib(3)',
          children: [
            {
              name: 'fib(2)',
              children: [
                { name: 'fib(1)' },
                { name: 'fib(0)' }
              ]
            },
            { name: 'fib(1)' }
          ]
        },
        {
          name: 'fib(2)',
          children: [
            { name: 'fib(1)' },
            { name: 'fib(0)' }
          ]
        },
      ]
    },
    {
      name: 'fib(3)',
      children: [
        {
          name: 'fib(2)',
          children: [
            { name: 'fib(1)' },
            { name: 'fib(0)' }
          ]
        },
        { name: 'fib(1)' }
      ]
    }
  ]
})
</script>

We can see that the entirety of the `fib(3)` subtree is duplicated below
the `fib(4)` subtree, and the `fib(2)` subtree occurs three times. As
`n` increases, the size of the redundant call subtrees increases
dramatically, while the number of unique calls only grows linearly.
Ideally we would only perform the calculations required, giving us $$0(n)$$
running time.

This is a good time to consider that the “top down” approach of
recursive problem solving has a counterpart, the unsurprising “bottom
up” approach of dynamic programming.

Applying dynamic programming to this problem, we ask ourselves “starting
with 0 and 1, how do we build up an answer to $$f(n)$$?” If `n` were 0
or 1, we could answer immediately. If it were 2, however, we would need
to add 0 and 1 to determine the answer: 1. If n were 3, we would
need to add the answer to $$f(2)$$, that we just determined, to the 1
that we previously determined, giving a total of 2. Following this strategy, we
obtain 3, 5, 8, etc., until we have reached the answer for our `n`.

At any point in time we only need to retain a memory of the previous two
calculations, and we never obtain the same sum twice.

An implementation of this strategy might look like:

<!-- language python -->
```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a
```
<!-- /language -->
<!-- language javascript -->
```javascript
const fib = (n) => {
  let a = 0
  let b = 1
  for (let i = 0; i < n; i++) {
    let temp = a
    a = a + b
    b = temp
  }
  return a
}
```
<!-- /language -->

With this implementation, we sacrifice some of the elegance and
readability of our recursive solution, but gain a much better $$O(n)$$
running time and $$O(1)$$ space cost.

Let’s now consider a problem where both the recursive and dynamic
programming approaches require a little more work to discover.

Given a lattice of height `H` and width `W`, how many unique shortest
paths exist from the top left corner to bottom right corner?

For instance, consider the lattice of height and width 2:

<figure>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge" d="M50 50 H100" />
    <path class="graph-edge" d="M100 50 H150" />
    <path class="graph-edge" d="M50 100 H100" />
    <path class="graph-edge" d="M100 100 H150" />
    <path class="graph-edge" d="M50 150 H100" />
    <path class="graph-edge" d="M100 150 H150" />
    <path class="graph-edge" d="M50 50 V100" />
    <path class="graph-edge" d="M50 100 V150" />
    <path class="graph-edge" d="M100 50 V100" />
    <path class="graph-edge" d="M100 100 V150" />
    <path class="graph-edge" d="M150 50 V100" />
    <path class="graph-edge" d="M150 100 V150" />
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
</figure>

We can see that the shortest path from top left to bottom right will
be of length 4, and that there are 6 unique paths of length 4:

<figure>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-emphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 150 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-emphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 150 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 V150"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-emphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 150 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 V150"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <br/>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 150 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 150 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 150 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="50" cy="150" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
</figure>

Exploring this problem, we realize that any shortest path must always
progress down and to the right—any path that progresses up or left
at any point has no chance of being “shortest”. Exploring further,
we note that by grouping those paths that start with a right step
(shown on the top line above) and those that start with a down step
(shown on the bottom line below), we can break this traversal problem
into subproblems.

Specifically, the total number of paths along a $$H \times W$$ lattice
is the sum of those along a $$(H - 1) \times W$$ lattice and a
$$H \times (W - 1)$$ lattice.

Continuing with our $$2 \times 2$$ example, the paths starting with a right step lead to the $$1 \times 2$$ subproblem with these three solutions:

<figure>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-emphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
  <svg height=200 width=200 version="1.1">
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 150 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 V150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 100 V150"/>
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="150" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="150" r="5" />
  </svg>
</figure>

Looking closely, we see this as a repetition of the right hand portion
of our first three solutions to the $$2 \times 2$$ problem.

Similarly, the paths starting downward on our $$2 \times 2$$ problem
lead to the $$2 \times 1$$ subproblem with the following three
solutions:

<figure>
   <svg height=150 width=200 version="1.1">
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-emphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
  </svg>
  <svg height=150 width=200 version="1.1">
    <path class="graph-edge graph-edge-emphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M150 50 V100"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
  </svg>
  <svg height=150 width=200 version="1.1">
    <path class="graph-edge graph-edge-emphasized" d="M50 50 H100"/>
    <path class="graph-edge graph-edge-emphasized" d="M100 50 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 100 H100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 100 H150"/>
    <path class="graph-edge graph-edge-deemphasized" d="M50 50 V100"/>
    <path class="graph-edge graph-edge-deemphasized" d="M100 50 V100"/>
    <path class="graph-edge graph-edge-emphasized" d="M150 50 V100"/>
    <circle class="graph-node" cx="50" cy="50" r="5" />
    <circle class="graph-node" cx="50" cy="100" r="5" />
    <circle class="graph-node" cx="100" cy="50" r="5" />
    <circle class="graph-node" cx="100" cy="100" r="5" />
    <circle class="graph-node" cx="150" cy="50" r="5" />
    <circle class="graph-node" cx="150" cy="100" r="5" />
  </svg>
</figure>

This time by looking closely we see that this is a repetition of the
bottom portion of our final three solutions to the $$2 \times 2$$
problem.

We can say then with some confidence that the total number of paths
along a $$H \times W$$ lattice is the sum of those along a $$(H - 1) \times W$$
lattice and a $$H \times (W - 1)$$ lattice. Thus by taking a top down
approach to explore the recursive nature of the problem, we’ve identified
a recursive relationship: `f(h, w) = f(h, w - 1) + f(w, h - 1)`.

Before we can write a recursive solution to the problem, we must also
recognize the base case: when the `h` or `w` of our subproblem
is `0`, we are dealing with a straight line, so the number of paths
is simply `1`.

Putting our base case and general case together, we obtain a succinct recursive
solution:

<!-- language python -->
<!-- literate recursion/lattice_traversal_recursive.py -->
<!-- /language -->

<!-- language javascript -->
```javascript
const numPaths = (height, width) => {
  if (height === 0 || width === 0) return 1
  return numPaths(height, width - 1) + numPaths(height - 1, width)
}
```
<!-- /language -->

Unfortunately, we find ourselves with another $$O(2^n)$$ solution
(where $$n = H + W$$) due
to redundant calls in our overlapping subproblems. For instance,
calculating `f(3, 2)` involves calculating `f(2, 2)` and `f(3, 1)`,
but then in calculating `f(2, 3)` we redundantly call `f(2, 2)` once
more.

Consider the call tree of <span data-language="python">`num_paths(2, 2)`</span><span data-language="javascript">`numPaths(2, 2)`</span> to convince yourself
that the running time is $$O(2^n)$$:

<figure>
  <svg id="lattice-2-2-call-tree" />
</figure>

<script>
drawTree('#lattice-2-2-call-tree', {
  name: 'f(2, 2)',
  children: [
    {
      name: 'f(2, 1)',
      children: [
        { name: 'f(2, 0)' },
        {
          name: 'f(1, 1)',
          children: [
            { name: 'f(1, 0)' },
            { name: 'f(0, 1)' }
          ]
        },
      ]
    },
    {
      name: 'f(1, 2)',
      children: [
        {
          name: 'f(1, 1)',
          children: [
            { name: 'f(1, 0)' },
            { name: 'f(0, 1)' }
          ]
        },
        { name: 'f(0, 2)' }
      ]
    },
  ]
})
</script>

Once again this should be a signal to us that we may be able to find
a faster solution by going bottom up, computing and storing the answer
to subproblems before we address the core problem.

After some exploration of the problem, you may come to recognize that in order
to calculate the number of unique paths to any point on the lattice, we must
solve the subproblems of the number of paths to each of the points to the left
and above the point in question. In turn, those subproblems can be solved if
we first answer the subproblems of the number of paths to each of the points
to the left and above _those_ points. The logical conclusion is that if we
start with the top leftmost point (which we can say can be reached in only 1
way) we can then iterate through every point of the lattice, row by row, and
calculate the paths to that point as the sum of the paths to the points above
and to the left, which by the nature of our iteration we have already calculated
precisely one time.

We can use a list of lists to store our computed values
as we proceed. For a $$H \times W$$ lattice, we can use a $$(H + 1) \times (W + 1)$$
list of lists, with each entry representing the number of paths that
one may take to arrive at that vertex. We may initialize the values to
1, as we know that there is only one way to arrive at a vertex on the
top or left edges. Then, iterating through each entry of each row, we
can determine the number of paths to that vertex by adding the number
of paths to the vertexes directly above and to the left. Finally, we
access the value computed in the last entry of the last row of our memo,
which represents the number of paths to traverse the entire lattice.

For instance, this is the memo that we will generate in the process of
computing `f(2, 2)` using this strategy:

```python
[
    [1, 1, 1],
    [1, 2, 3],
    [1, 3, 6]
]
```

Again we arrive at our answer 6.

This is what the memo looks like for `f(10, 10)`:

```python
[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66],
    [1, 4, 10, 20, 35, 56, 84, 120, 165, 220, 286],
    [1, 5, 15, 35, 70, 126, 210, 330, 495, 715, 1001],
    [1, 6, 21, 56, 126, 252, 462, 792, 1287, 2002, 3003],
    [1, 7, 28, 84, 210, 462, 924, 1716, 3003, 5005, 8008],
    [1, 8, 36, 120, 330, 792, 1716, 3432, 6435, 11440, 19448],
    [1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310, 43758],
    [1, 10, 55, 220, 715, 2002, 5005, 11440, 24310, 48620, 92378],
    [1, 11, 66, 286, 1001, 3003, 8008, 19448, 43758, 92378, 184756]
]
```

Below is a possible implementation of the dynamic programming strategy
we have discussed.

<!-- language python -->
<!-- literate recursion/lattice_traversal_dp.py -->
<!-- /language -->

<!-- language javascript -->
```javascript
const numPathsDp = (height, width) {
  const memo = Array.from(Array(height + 1)).map(
    () => Array.from(Array(width + 1)).map(() => 1)
  )
  for (let i = 1; i < memo.length; i++) {
    const row = memo[i]
    for (let j = 1; j < row.length; j++) {
      memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
    }
  }
  return memo[height][width]
}
```
<!-- /language -->

Both the time and space cost for this implementation are $$O(H \times W)$$,
compared to $$O(2^{H + W})$$ time and $$O(H + W)$$ space previously, making a big time difference as $$H$$
and $$W$$ increase.

If space is of particular concern, the space cost could be decreased to
$$O(W)$$ by retaining a memo of the prior row only. This is left as an
exercise for the reader.
