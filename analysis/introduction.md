Introduction to Algorithm Analysis
===

Every software engineer will have a different answer to the question
“what makes one computer program better than another?” Some may focus
on the readability of the code, others on the engineering paradigms
used, others on “efficiency”, and so on.

When we put aside the language- or implementation-specific aspects of a
program and talk about the underlying _algorithm_, there are fewer
comparisons to be made. We concern ourselves here with comparing
algorithms based upon the amount of computing resources used, in other
words we want to be able to compare two algorithms and say that one is
better than the other because it is more economical in its use of
computing resources.

Typically, the two “computing resources” that we care about are space
(such as memory) and time. In different contexts, we may be willing to
compromise one more than another, for instance we may be willing for
a program to run longer so long as it doesn’t exceed a certain amount
of allocated space, or conversely we may be willing to use more memory
in order to reduce the running time of a program. As such we want a
vocabulary and method of analysis that allows us to discuss the usage
of space and time for any algorithm we encounter.

One way we _could_ measure the running time for a program is to do a
benchmark analysis. This would involve tracking the actual time required
for the program to compute its result.

In Python, we can benchmark a function by noting the starting time and
ending time with respect to the system we are using. In the `time`
module there is a function called `time` that will return the current
system clock time in seconds since some arbitrary starting point. By
calling this function twice, at the beginning and at the end, and then
computing the difference, we can get an exact number of seconds
(fractions in most cases) for execution.

Let us do so for a simple function computing the sum of a range of
integers:

```python
def sum_of_n(n):
    the_sum = 0
    for i in range(n + 1):
        the_sum = the_sum + i
    return the_sum
```

We can add our calls to `time.time` and return the difference in order
to measure the running time for each call in seconds, and return it
alongside our sum as a tuple:

```python
import time

def sum_of_n(n):
   start = time.time()

   the_sum = 0
   for i in range(n + 1):
      the_sum = the_sum + i

   end = time.time()

   return the_sum, end - start
```

If we perform 5 invocations of the function, each computing the sum of
the first 10,000 integers, we get something like the following:

```
>>> for i in range(5):
...     print('Sum is {}, required {:10.7f} seconds'.format(*sum_of_n(10000)))
Sum is 50005000, required  0.0018950 seconds
Sum is 50005000, required  0.0018620 seconds
Sum is 50005000, required  0.0019171 seconds
Sum is 50005000, required  0.0019162 seconds
Sum is 50005000, required  0.0019360 seconds
```

We discover that the time is fairly consistent and it takes on average
about 0.0019 seconds to execute that code. What if we run the function
adding the first 100,000 integers?

```
>>> for i in range(5):
...     print('Sum is {:d}, required {:10.7f} seconds'.format(sum_of_n(100000)))
Sum is 5000050000, required  0.0199420 seconds
Sum is 5000050000, required  0.0180972 seconds
Sum is 5000050000, required  0.0194821 seconds
Sum is 5000050000, required  0.0178988 seconds
Sum is 5000050000, required  0.0188949 seconds
```

Again, the time required for each run, although longer, is very
consistent, averaging about 10 times more seconds. For `n` equal to
1,000,000 we get:

```
>>> for i in range(5):
...     print('Sum is {}, required {:10.7f} seconds'.format(*sum_of_n(1000000)))
Sum is 500000500000, required  0.1948988 seconds
Sum is 500000500000, required  0.1850290 seconds
Sum is 500000500000, required  0.1809771 seconds
Sum is 500000500000, required  0.1729250 seconds
Sum is 500000500000, required  0.1646299 seconds
```

In this case, the average again turns out to be about 10 times the
previous.

Now consider the approach below, which shows a different
means of solving the summation problem. This function, `arithmetic_sum`, takes
advantage of a closed equation $$\sum_{i=1}^{n} i = \frac {(n)(n+1)}{2}$$
to compute the sum of the first `n` integers without iterating.

```python
def arithmetic_sum(n):
    return n * (n + 1) / 2
```

If we do the same benchmark measurement for `arithmetic_sum`, using five
different values for `n` (10,000, 100,000, 1,000,000, 10,000,000, and
100,000,000), we get the following results:

```
Sum is 50005000, required 0.00000095 seconds
Sum is 5000050000, required 0.00000191 seconds
Sum is 500000500000, required 0.00000095 seconds
Sum is 50000005000000, required 0.00000095 seconds
Sum is 5000000050000000, required 0.00000119 seconds
```

There are two important things to notice about this output. First, the
times recorded above are shorter than any of the previous examples.
Second, they are very consistent no matter what the value of `n`. It
appears that `arithmetic_sum` is hardly impacted by the number of integers
being added.

But what does this benchmark really tell us? Intuitively, we can see
that the iterative solutions seem to be doing more work since some
program steps are being repeated. This is likely the reason it is taking
longer. Also, the time required for the iterative solution seems to
increase as we increase the value of `n`. However, there is a problem.
If we ran the same function on a different computer or used a different
programming language, we would likely get different results. It could
take even longer to perform `arithmetic_sum` if the computer were older.

We need a better way to characterize these algorithms with respect to
execution time. The benchmark technique computes the actual time to
execute. It does not really provide us with a useful measurement,
because it is dependent on a particular machine, program, time of day,
compiler, and programming language. Instead, we would like to have a
characterization that is independent of the program or computer being
used. This measure would then be useful for judging the algorithm alone
and could be used to compare algorithms across implementations.
