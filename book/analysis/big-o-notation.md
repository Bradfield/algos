---
title: Big O Notation
collection: analysis
position: 2
layout: default.html
---

An algorithm is little more than a series of steps required to perform some task. If we treat each step as a basic unit of computation, then an algorithm’s execution time can be expressed as the *number of steps required to solve the problem*.

This abstraction is exactly what we need: it characterizes an algorithm’s efficiency in terms of execution time while remaining independent of any particular program or computer. Now we can take a closer look at those two summation algorithms we introduced last chapter.

Intuitively, we can see that the first algorithm (`sum_of_n`) is doing more work than the second (`arithmetic_sum`): some program steps are being repeated, and the program takes even longer if we increase the value of `n`. But we need to be more precise.

The most expensive unit of computation in `sum_of_n` is variable assignment. If we counted the number of assignment statements, we would have a worthy approximation of the algorithm's execution time: there's an initial assignment statement (`total = 0`) that is performed only once, followed by a loop that executes (`total += i`) a total of `n` times.

We can denote this more succinctly with function $$T$$, where $$T(n)=1+n$$.

The parameter $$n$$ is often referred to as the “size of the problem”, so we can read this as “$$T(n)$$ is the time it takes to solve a problem of size $$n$$, namely 1 + $$n$$ steps.”

For our summation functions, it makes sense to use the number of terms being summed to denote the size of the problem. Then, we can say that “The sum of the first 100,000 integers is a *bigger instance* of the summation problem than the sum of the first 1,000 integers.”

Based on that claim, it seems reasonable that the time required to solve the larger case would be greater than for the smaller case. “Seems reasonable” isn’t quite good enough, though; we need to _prove_ that the algorithm’s execution time depends on the size of the problem.

To do this, we’re going to stop worrying about the *exact* number of operations an algorithm performs and determine the dominant part of the $$T(n)$$ function. We can do this because, as the problem gets larger, some portion of the $$T(n)$$ function tends to overpower the rest; it’s this dominant portion that is ultimately most helpful for algorithm comparisons.

The *order of magnitude* function describes the part of $$T(n)$$ that increases fastest as the value of $$n$$ increases. “Order of magnitude function” is a bit of a mouthful, though, so we call it *big O*. We
write it as $$O(f(n))$$, where $$f(n)$$ is the dominant part of the original $$T(n)$$. This is called “Big O notation” and provides a useful approximation for the *actual* number of steps in a computation.

In the above example, we saw that $$T(n)=1+n$$. As $$n$$ gets larger, the constant 1 will become less significant to the final result. If we are simply looking for an approximation of $$T(n)$$, then we can drop the 1 and say that the running time is $$O(n)$$.

Let’s be clear, though: the 1 *is* important to $$T(n)$$ and can only be safely ignored when we are looking for an *approximation* of $$T(n)$$.

As another example, suppose that the exact number of steps in some algorithm is $$T(n)=5n^{2}+27n+1005$$. When $$n$$ is small (1 or 2), the constant 1005 seems to be the dominant part of the function. However, as $$n$$ gets larger, the term $$n^{2}$$ becomes enormous, dwarfing the other two terms in its contribution to the final result.

Again, for an *approximation* of $$T(n)$$ at large values of $$n$$, we can focus on $$5n^{2}$$ and ignore the other terms. Similarly, the coefficient $$5$$ becomes insignificant as $$n$$ gets larger. We would then say that the function $$T(n)$$ has an order of magnitude $$f(n)=n^{2}$$; more simply, the function $$T(n)$$ is $$O(n^{2})$$.

Although we don’t see this in the summation example, sometimes the performance of an algorithm depends on the problem’s **exact** data values rather than its size. For these kinds of algorithms, we need to characterize their performances as *worst case*, *best case*, or *average case*.

The worst case performance refers to a particular data set where the algorithm performs especially poorly, while the best case performance refers to a data set that the algorithm can process extremely fast. The average case, as you can probably infer, performs somewhere in between these two extremes. Understanding these distinctions can help prevent any one particular case from misleading us.

There are several common order of magnitude functions that will frequently appear as you study algorithms. These functions are listed below from lowest order of magnitude to highest. Knowing these goes a long way toward recognizing them in your own code.

f(n) | Name
--- | ---
$$1$$ | Constant
$$\log{n}$$ | Logarithmic
$$n$$ | Linear
$$n\log{n}$$ | Log Linear
$$n^{2}$$ | Quadratic
$$n^{3}$$ | Cubic
$$2^{n}$$ | Exponential

In order to decide which of these functions dominates a $$T(n)$$ function, we must see how it compares with the others as $$n$$ becomes larger. We’ve taken the liberty of graphing these functions together below.

![](figures/big-o-plot.png)

Notice that, when $$n$$ is small, the functions inhabit a similar area; it’s hard to tell which is dominant. However, as $$n$$ grows, they branch, making it easy for us to distinguish them.

As a final example, suppose that we have the fragment of Python code shown below. Although this program does nothing useful, it’s instructive to see how we can take actual code and analyze its performance.

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

To calculate $$T(n)$$ for this fragment, we need to count the assignment operations, which is easier if we group them logically.

The first group consists of three assignment statements, giving us the term **3**. The second group consists of three assignments in the nested iteration: **$$3n^{2}$$**. The third group has two assignments iterated $$n$$ times: **$$2n$$**. The fourth “group” is the last assignment statement, which is just the constant **1**.

Putting those all together: $$T(n)=3+3n^{2}+2n+1=3n^{2}+2n+4$$. By looking at the exponents, we can see that the $$n^{2}$$ term will be dominant, so this fragment of code is $$O(n^{2})$$. Remember that we can safely ignore all the terms and coefficients as $$n$$ grows larger.

The diagram below shows a few of the common big O functions as they compare with the $$T(n)$$ function discussed above.

![](figures/big-o-plot-2.png)

Note that $$T(n)$$ is initially larger than the cubic function but, as $$n$$ grows, $$T(n)$$ cannot compete with the rapid growth of the cubic function. Instead, it heads in the same direction as the quadratic function as $$n$$ continues to grow.
