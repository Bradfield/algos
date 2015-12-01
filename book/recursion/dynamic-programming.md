---
title: Dynamic Programming
layout: chapter.html
collection: recursion
position: 7
---

Dynamic programming is a powerful technique for solving a certain class of
problems, typically in a more efficient manner than the corresponding recursive
strategy. Specifically, when a problem consists of “overlapping subproblems”
a recursive strategy may lead to redundant computation whereas the corresponding
dynamic programming strategy may avoid such waste by addressing and solving the
subproblems one at a time in a manner without overlap.

This idea is difficult to understand in the abstract, so let’s consider a
couple of examples.

Firstly, let’s write a function to return the nth Fibonacci number, being the
nth number in the sequence constructed by starting with $$0, 1$$ and calculating
subsequent numbers as the sum of the previous two numbers, like so:

$$0, 1, 1, 2, 3, 5, 8, 13, 21 ...$$

The Fibonacci sequence may be familiar enough to you that you are able to take a
“top down” approach, namely that you can identify the recursive relationship
simply by considering the definition of the Fibonacci sequence. In other words,
a “top down” approach considers the statement “calculating subsequent numbers as
the sum of the previous two numbers” and recognizes the relationship
$$f(n) = f(n-1) + f(n-2)$$. With 0 and 1 as our base cases, this leads to a
straightforward implementation:

```python
def fib(n):
    if n <= 1:
        return n  # base cases: return 0 or 1 if n is 0 or 1 respectively
    return fib(n - 1) + fib(n - 2)
```

This is a correct solution, but it poses a problem evident to those who run
`fib(50)` and wait for an answer. The running time of this implementation is
$$O(2^n)$$ due to a very large number of redundant recursive executions. When
we call `fib(n)` we recursively call `fib(n - 1)` and `fib(n - 2)` which
themselves call (i) `fib(n - 2)` and `fib(n - 3)`; and, (ii) `fib(n - 3)`
and `fib(n - 4)` respectively. We can see that there are some redundant calls,
and you may recognize that each of those redundant calls trigger trees of
further entirely redundant calls. This can be seen more clearly by drawing out
the call tree for `fib(5)`, as we do below:

<svg id="fib-5-call-tree" />

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

We can see that the entirety of the `fib(3)` subtree is duplicated below the
`fib(4)` subtree, and the `fib(2)` subtree occurs three times. As `n` increases,
the size of the redundant call subtrees increases dramatically, whereas
the number of unique calls grows only linearly. Ideally we would do only the
calculations required, giving us $$0(n)$$ running time.

This is a good time to consider that the “top down” approach of recursive
problem solving has a counterpart, the unsurprising “bottom up” approach of
dynamic programming.

Applying dynamic programming to this problem, we ask ourselves “starting with
0 and 1, how do we build up an answer to $$f(n)$$?” If `n` were 0 or 1, we could
answer immediately. If it were 2 however, we would need to add 0 and 1 to
determine the answer to be 1. If n were 3, we would now need to add the answer
to $$f(2)$$ that we just determined to the 1 that we previously determined,
giving a total of 2. Doing this again, we obtain 3, 5, 8 etc until we have
reached the answer for our `n`. At any point in time we only need to retain
a memory of the previous to calculations, and we never do the same sum twice.

A straightforward implementation falls out of this strategy:

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a
    return a
```

With this implementation we sacrifice some of the elegance and readability of
our recursive solution, but gain a much better $$O(n)$$ running time and
$$O(1)$$ space cost.
