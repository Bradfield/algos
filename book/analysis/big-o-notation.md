---
title: Big O Notation
collection: analysis
position: 2
layout: default.html
---

An algorithm is little more than a series of operations (or steps) required to
perform some task. If we treat each step as a basic unit of computation, then
an algorithm’s execution time can be expressed as the *number of steps required
to solve the problem*.

This abstraction is exactly what we need: it characterizes an algorithm’s
efficiency in terms of execution time while remaining independent of any
particular program or computer.

How can we apply this abstraction to the summation algorithms shown earlier?

Looking back at our function `sum_of_n`, the most basic unit of computation
seems to be variable assignment so, if we count those, we could have a worthy
representation of the algorithm's execution time. There's an initial assignment
statement that is performed only once (`the_sum = 0`), followed by a loop that executes (`the_sum += i`) a total of `n` times.

We can denote this more elegantly with function $$T$$, where $$T(n) = 1 + n$$.

The parameter *n* is often referred to as the “size of the problem”, so we can
read this as “T(n) is the time it takes to solve a problem of size *n*,
namely 1 + *n* steps.”

For our summation functions, it makes sense to use the number of terms being
summed to denote the size of the problem. Then, we can say that “The sum of the
first 100,000 integers is a *bigger instance* of the summation problem than the
sum of the first 1,000 integers”.

Based on that claim, it seems reasonable that the time required to solve the
larger case would be greater than for the smaller case. “Seems reasonable” isn’t
quite good enough, though; we need to prove that the algorithm’s execution time
is dependent on the size of the problem.

To do this, we’re going to stop worrying about the *exact* number of operations
an algorithm performs and determine the dominant part of the $$T(n)$$ function.
We can do this because, as the problem gets larger, some portion of the $$T(n)$$
function tends to overpower the rest; it is this dominant portion that is
ultimately most helpful for algorithm comparisons.

The *order of magnitude* function describes the part of $$T(n)$$ that increases
fastest as the value of *n* increases. “Order of magnitude function” is a bit of
a mouthful, though, so we call it *big O* notation and write it as $$O(f(n))$$,
where $$f(n)$$ is the dominant part of the original $$T(n)$$. Big O notation provides a useful approximation for the *actual* number of steps in a
computation.

****

In the above example, $$T(n)=1+n$$. As *n* gets large, the constant 1 will
become less and less significant to the final result. If we are looking
for an approximation for $$T(n)$$, then we can drop the 1 and simply say
that the running time is $$O(n)$$. It is important to note that the 1 is
certainly significant for $$T(n)$$. However, as *n* gets large, our
approximation will be just as accurate without it.

As another example, suppose that for some algorithm, the exact number of
steps is $$T(n)=5n^{2}+27n+1005$$. When *n* is small, say 1 or 2, the
constant 1005 seems to be the dominant part of the function. However, as
*n* gets larger, the $$n^{2}$$ term becomes the most important. In fact,
when *n* is really large, the other two terms become insignificant in
the role that they play in determining the final result. Again, to
approximate $$T(n)$$ as *n* gets large, we can ignore the other terms and
focus on $$5n^{2}$$. In addition, the coefficient $$5$$ becomes
insignificant as *n* gets large. We would say then that the function
$$T(n)$$ has an order of magnitude $$f(n)=n^{2}$$, or simply that it is
$$O(n^{2})$$.

Although we do not see this in the summation example, sometimes the
performance of an algorithm depends on the exact values of the data
rather than simply the size of the problem. For these kinds of
algorithms we need to characterize their performance in terms of best
case, *worst case*, or *average case* performance. The worst case
performance refers to a particular data set where the algorithm performs
especially poorly. Whereas a different data set for the exact same
algorithm might have extraordinarily good performance. However, in most
cases the algorithm performs somewhere in between these two extremes
(average case). It is important for a computer scientist to understand
these distinctions so they are not misled by one particular case.

A number of very common order of magnitude functions will come up over
and over as you study algorithms. These are shown in
the table below. In order to decide which of these
functions is the dominant part of any $$T(n)$$ function, we must see how
they compare with one another as *n* gets large.

f(n) | Name
--- | ---
$$1$$ | Constant
$$log n$$ | Logarithmic
$$n$$ | Linear
$$n log n$$ | Log Linear
$$n^{2}$$ | Quadratic
$$n^{3}$$ | Cubic
$$2^{n}$$ | Exponential

Below we show graphs of the common functions
from the above table. Notice that when `n` is small, the
functions are not very well defined with respect to one another. It is
hard to tell which is dominant. However, as `n` grows, there is a
definite relationship and it is easy to see how they compare with one
another.

![Plot of common big O functions](figures/big-o-plot.png)

As a final example, suppose that we have the fragment of Python code
shown below. Although this program does
not really do anything, it is instructive to see how we can take actual
code and analyze performance.

```python
a = 5
b = 6
c = 10
for i in range(n):
   for j in range(n):
      x = i * i
      y = j * j
      z = i * j
for k in range(n):
   w = a * k + 45
   v = b * b
d = 33
```

The number of assignment operations is the sum of four terms. The first
term is the constant 3, representing the three assignment statements at
the start of the fragment. The second term is $$3n^{2}$$, since there are
three statements that are performed $$n^{2}$$ times due to the nested
iteration. The third term is $$2n$$, two statements iterated *n* times.
Finally, the fourth term is the constant 1, representing the final
assignment statement. This gives us $$T(n)=3+3n^{2}+2n+1=3n^{2}+2n+4$$. By
looking at the exponents, we can easily see that the $$n^{2}$$ term will
be dominant and therefore this fragment of code is $$O(n^{2})$$. Note that
all of the other terms as well as the coefficient on the dominant term
can be ignored as *n* grows larger.

![Comparing T(n) with common big O functions](figures/big-o-plot-2.png)

This diagram shows a few of the common big O
functions as they compare with the $$T(n)$$ function discussed above. Note
that $$T(n)$$ is initially larger than the cubic function. However, as n
grows, the cubic function quickly overtakes $$T(n)$$. It is easy to see
that $$T(n)$$ then follows the quadratic function as $$n$$ continues to
grow.

