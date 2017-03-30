---
title: The Big Picture
collection: analysis
position: 1
layout: default.html
---

What makes one computer program better than another?

Take a moment to answer this for yourself 🙂. If you were given two programs that solve the same problem, how would you decide which one to use?

<!-- concealed -->
The truth is there are many valid criteria, which are often in conflict.
<!-- /concealed -->

For instance, we typically want our program to be _correct_. In other words, we’d like the program’s output to match our expectations. Unfortunately, correctness is not always clear. For instance, what does it mean for Google to return the “correct” top 10 search results for your search query?

Good software engineers often want their code to be _readable_, _reusable_, _elegant_ or _testable_. These are admirable goals, but you may not be able to achieve them all at the same time. It’s also not entirely clear what something like “elegance” looks like, and we certainly haven’t been able to model it mathematically, so computer scientists haven’t given these aspects of programs much consideration 🤷‍.

Two factors that computer scientists _love_ to model mathematically, though, are how long a program will take to run, and how much space (typically, memory) it will use. We call these time and space efficiency, and they’ll be at the core of our study of algorithms.

Again we may need to trade these off against other concerns: algorithm A may be faster but use more memory than algorithm B. They might both be less elegant than algorithm C, in a context where elegance is the priority. We’ll be focusing on time and space because they happen to be both interesting and measurable, but please don’t go away thinking they’re always the most important factors. The only truly correct answer is: “it depends”.

Another aspect of “it depends”, even when we focus on just time or space, is the context in which the program runs. There is often a relationship between the inputs of a program and its running time or space usage. For instance if you `grep` over many large files, it will take longer than if you `grep` over fewer, smaller files. This relationship between inputs and behavior will be an important part of our analysis.

Beyond this, the exact and space that your program uses will also depend on many other factors. Can you think of at least three?

<!-- concealed -->
Here are some:

* How long it takes your computer to execute every instruction
* Your computer’s “Instruction Set Architecture”, for instance ARM or Intel x86
* How many cores of your machine the program uses
* What language your program is written in
* How your operating system chooses to schedule processes
* What other programs are running at the same time

&hellip; and so on.
<!-- /concealed -->

All of these are important factors for us software engineers, but to the computer scientist these are details that don’t speak to the core question of whether an algorithm is fast or slow. Sometimes we’d like to be able to ask: generally speaking, irrespective of whether a program is written in Fortran for the IBM 704 or in Python running on a shiny new Macbook, will it be more time and/or space efficient than an alternative? This is the crux of algorithm analysis.

<p class="crux">
Algorithm analysis is a way to compare the time and space efficiency of programs with respect to their possible inputs, but irrespective of other context.
</p>

In the real world, we measure the time used by a program in some unit of time, such as seconds. Similarly we measure space used in something like bytes. In analysis, this would be too specific. If we run a program and measure the time it takes to finish, this number would incorporate details like language choice and CPU speed. We will need new models and vocabulary in order to speak with the level of generality that we’re seeking.

Let’s explore this idea with an example.

Say I wanted to calculate the sum of the first n numbers, and I’m wondering how long this will take. Firstly, can you think of a simple algorithm to do the calculation? It should be a function that has n as a parameter, and returns the sum of the first n numbers. You don’t need to do anything fancy, but please do take the time to write out an algorithm and think about how long it will take to run on small or large inputs.

Here is a simple Python solution:

```python
def sum_to_n(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total
```

Will `sum_to_n` take longer to run given a larger n? Intuitively, the answer seems to be yes, as it will loop more times.

Will `sum_to_n` take the same amount of time to run each time it’s invoked with the same input? Intuitively the answer seems to be yes, since the same instructions are executed.

Let’s now add some code to time the execution:


```python
import time

def sum_to_n(n):
    # record start time
    start = time.time()

    # run the function's code
    total = 0
    for i in range(n + 1):
        total += i

    # record end time
    end = time.time()

    return total, end - start
```

Let’s say I ran this with `n=1000000` (1 million) and noticed that it took 0.11 seconds. What would you expect to see if I ran it five more times?

```
>>> output_template = '{}({}) = {:15d} ({:8.7f} seconds)'
>>> for _ in range(5):
...     print(output_template.format('sum_to_n', 1000000, *sum_to_n(1000000)))
```

```
sum_to_n(1000000) =    500000500000 (0.1209280 seconds)
sum_to_n(1000000) =    500000500000 (0.1107872 seconds)
sum_to_n(1000000) =    500000500000 (0.1187370 seconds)
sum_to_n(1000000) =    500000500000 (0.1210580 seconds)
sum_to_n(1000000) =    500000500000 (0.1230309 seconds)
```

Interestingly, it takes a slightly different amount of time on each invocation, due to the slightly different state of my computer and the Python virtual machine each time. These are differences that we’d like to ignore.

Now, what if we were to run it again with a range of different inputs, say 1 million, 2 million etc up to 9 million? What would you expect to see?

```
>>> for i in range(1, 10):
...     print(output_template.format('sum_to_n', i * 1000000, *sum_to_n(i * 1000000)))
```

```
sum_to_n(1000000) =    500000500000 (0.1198549 seconds)
sum_to_n(2000000) =   2000001000000 (0.2401729 seconds)
sum_to_n(3000000) =   4500001500000 (0.3838110 seconds)
sum_to_n(4000000) =   8000002000000 (0.4790699 seconds)
sum_to_n(5000000) =  12500002500000 (0.6189690 seconds)
sum_to_n(6000000) =  18000003000000 (0.6952291 seconds)
sum_to_n(7000000) =  24500003500000 (0.8431778 seconds)
sum_to_n(8000000) =  32000004000000 (0.9679160 seconds)
sum_to_n(9000000) =  40500004500000 (1.0458572 seconds)
```

Do you see the general relationship between between n and time elapsed? Is this what you expected? What would the relationship look like if you were to plot our different values of n on the x-axis and time elapsed on the y-axis?

[TODO chart]

It turns out that our simple strategy is not the most efficient. In fact there is a short formula that will give us the answer to our question without any looping. Can you determine (or perhaps remember) what it is? Here's a hint... try it with the numbers 1 to 6, and group 1 and 6, 2 and 5, and 3 and 4 together to notice that there are three pairs each individually totaling 7.

Mathematically, the formula is:

$$\sum_{i=1}^{n} i = \frac {n(n+1)}{2}$$

If you don’t quite understand why this formula gives us the right answer, take a moment to explore [one of these visual explanations](https://fr0ddy.github.io/math/visual-proofs/sum-of-first-n-natural-numbers.html).

How would we implement this as a Python function, again with our timing code?

```python
def arithmetic_sum(n):
    start = time.time()
    total = n * (n + 1) // 2
    end = time.time()
    return total, end - start
```

What do you expect to see if we run this with our range of inputs as we did with `sum_to_n`?

```
>>> for i in range(1, 10):
...     print(output_template.format('arithmetic_sum', i * 1000000, *arithmetic_sum(i * 1000000)))
```

```
arithmetic_sum(1000000) =    500000500000 (0.0000021 seconds)
arithmetic_sum(2000000) =   2000001000000 (0.0000029 seconds)
arithmetic_sum(3000000) =   4500001500000 (0.0000019 seconds)
arithmetic_sum(4000000) =   8000002000000 (0.0000019 seconds)
arithmetic_sum(5000000) =  12500002500000 (0.0000031 seconds)
arithmetic_sum(6000000) =  18000003000000 (0.0000021 seconds)
arithmetic_sum(7000000) =  24500003500000 (0.0000021 seconds)
arithmetic_sum(8000000) =  32000004000000 (0.0000029 seconds)
arithmetic_sum(9000000) =  40500004500000 (0.0000019 seconds)
```

Notice that our answers are all correct. Did you expect each calculation to take around the same amount of time? What would this look like if we were to again plot our range of n values on the x-axis and times to calculate on the y-axis?

[TODO graph]

Not to get too far ahead of ourselves, but we describe `sum_to_n` as “linear” or $$O(n)$$, and `arithmetic_sum` as “constant” or $$O(1)$$. Hopefully you can see why. Irrespective of the exact times that these functions take to execute, we can spot a general trend that, that the execution time for `sum_to_n` grows in proportion to n, whereas the execution time for `arithmetic_sum` remains constant. All else being equal, `arithmetic_sum` is the better algorithm due to its more efficient use of time.

In the following sections, we’ll apply a little more rigor to our reasoning, and develop a vocabulary for describing these time and space usage characteristics more generally.
