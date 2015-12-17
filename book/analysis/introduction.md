---
title: Introduction to Algorithm Analysis
collection: analysis
position: 1
layout: chapter.html
---

What makes one computer program better than another?

The answer depends on the criteria we use: code readability, engineering
paradigms, and efficiency are a few possible metrics by which we we could
measure a program's quality.

Let's set aside aspects of a program that are specific to language or
implementation and instead focus on the underlying _algorithm_. Doing this
limits the number of factors we have to consider and enables us to make bold
statements like "Tesla's algorithm is better than Edison's algorithm because
because it uses computing resources more efficiently."

Typically, the two “computing resources” that we care about are *space* and
*time*. We usually replace "space" with "memory" because humans are
narcissistic and like comparing computers to their brains.

Depending on the situation, we may be willing to sacrifice one resource
if it means getting more of the other; for instance, we might be fine with a
program running longer as long as it doesn't exceed a certain amount of space.
Or maybe we're comfortable using more memory so the program can run faster.

But, in order to talk intelligently about space/time for algorithms we
encounter, we'll need both a vocabulary and a method of analysis. Let's
tackle the method of analysis first.

One way we _could_ measure the running time for a program is to do a
benchmark analysis. This would involve tracking the actual time required
for the program to compute its result.

Let's try this for a simple function computing the sum of a range of integers:

```python
import time

def sum_of_n(n):
    # record start time
    start = time.time()

    # run the function's code
    the_sum = 0
    for i in range(n + 1):
        the_sum += i

    # record end time
    end = time.time()

    return the_sum, end - start
```

If we perform 5 invocations of the function, each computing the sum of
the first 10,000 integers, we get something like the following:

```
>>> for i in range(5):
...     print('Sum is {}, required {:10.7f} seconds'.format(sum_of_n(10000)))
Sum is 50005000, required  0.0018950 seconds
Sum is 50005000, required  0.0018620 seconds
Sum is 50005000, required  0.0019171 seconds
Sum is 50005000, required  0.0019162 seconds
Sum is 50005000, required  0.0019360 seconds
```

Seems like the running time is fairly consistent and takes an average of
0.0019 seconds to perform the actual calculation. What if we repeat this
process for the first 100,000 integers?

```
>>> for i in range(5):
...     print('Sum is {:d}, required {:10.7f} seconds'.format(sum_of_n(100000)))
Sum is 5000050000, required  0.0199420 seconds
Sum is 5000050000, required  0.0180972 seconds
Sum is 5000050000, required  0.0194821 seconds
Sum is 5000050000, required  0.0178988 seconds
Sum is 5000050000, required  0.0188949 seconds
```

Again, the time required for each run, although longer, is very consistent,
averaging about 0.019 seconds. For `n` equal to 1,000,000 we get:

```
>>> for i in range(5):
...     print('Sum is {}, required {:10.7f} seconds'.format(*sum_of_n(1000000)))
Sum is 500000500000, required  0.1948988 seconds
Sum is 500000500000, required  0.1850290 seconds
Sum is 500000500000, required  0.1809771 seconds
Sum is 500000500000, required  0.1729250 seconds
Sum is 500000500000, required  0.1646299 seconds
```

Not only does the pattern still hold, but there appears to be a correlation
between the _size_ of the input and the _time_ needed to process that input.
Every time we increase `n` by some factor, the run time increases by the same
factor. Nasty; I certainly don't have time to wait around for the sum of the
first 100,000,000,000,000,000 integers (220 days).

Good thing there's another way to solve this problem, and here it is, in
glorious mathematical notation!

$$\sum_{i=1}^{n} i = \frac {(n)(n+1)}{2}$$

We've taken the liberty of turning this formula into a new function below;
note the lack of iteration:

```python
def arithmetic_sum(n):
    return n * (n + 1) / 2
```

If we do our performance experiment with `arithmetic_sum` using five
different values for `n` (10,000, 100,000, 1,000,000, 10,000,000, and
100,000,000), we get the following results:

```
Sum is 50005000, required 0.00000095 seconds
Sum is 5000050000, required 0.00000191 seconds
Sum is 500000500000, required 0.00000095 seconds
Sum is 50000005000000, required 0.00000095 seconds
Sum is 5000000050000000, required 0.00000119 seconds
```

There are a couple things to notice about this output.

First, the run times we're seeing for `arithmetic_sum` are much shorter than
any times for `sum_of_n`. Second, the run times are consistent and don't seem
to be dependent on the value of `n`.

But what does this benchmark *really* tell us?

Intuitively, we can see that the iterative program seems to be doing more work;
some program steps are being repeated, so the program takes longer. Also, the
iterative program takes more time to finish if we increase the value of `n`.
But these conclusions are misleading.

If we ran the same function on a different computer or used a different
programming language, we would likely get different results. It could take
much longer to perform `arithmetic_sum` if the computer were older.

The benchmark technique computes the _actual_ time to execute, but this isn't
really a useful measurement; this "time" is dependent on a list of sources,
including the programming language, compiler, OS, machine, and time of day.

We need a more abstract way to characterize these algorithms with respect to
their execution times, one that is independent of the program or computer
being used. This measure could be used to judge the algorithm alone and to
compare algorithms across implementations.
