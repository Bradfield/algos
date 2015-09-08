Algorithms and Data Structures with Python
===

The way we think about programming has undergone many changes in the
years since the first electronic computers required patch cables and
switches to convey instructions from human to machine. As is the case
with many aspects of society, changes in computing technology provide
computer scientists with a growing number of tools and platforms on
which to practice their craft. Advances such as faster processors,
high-speed networks, and large memory capacities have created a spiral
of complexity through which computer scientists must navigate.
Throughout all of this rapid evolution, a number of basic principles
have remained constant. The science of computing is concerned with using
computers to solve problems.

You have no doubt spent considerable time learning the basics of
problem-solving and hopefully feel confident in your ability to take a
problem statement and develop a solution. You have also learned that
writing computer programs is often hard. The complexity of large
problems and the corresponding complexity of the solutions can tend to
overshadow the fundamental ideas related to the problem-solving process.


Why Study Data Structures and Abstract Data Types?
---

To manage the complexity of problems and the problem-solving process,
computer scientists use abstractions to allow us to focus on the “big
picture” without getting lost in the details. By creating models of the
problem domain, we are able to utilize a better and more efficient
problem-solving process. These models allow us to describe the data that
our algorithms will manipulate in a much more consistent way with
respect to the problem itself.

An *abstract data type*, sometimes abbreviated *ADT*, is a logical description of how we view the data
and the operations that are allowed without regard to how they will be
implemented. This means that we are concerned only with what the data is
representing and not with how it will eventually be constructed. By
providing this level of abstraction, we are creating an
*encapsulation* around the data. The idea is that by encapsulating the
details of the implementation, we are hiding them from the user’s view.
This is called *information hiding*.

The implementation of an abstract data type, often referred to as a
*data structure*, will require that we provide a physical view of the
data using some collection of programming constructs and primitive data
types. As we discussed earlier, the separation of these two perspectives
will allow us to define the complex data models for our problems without
giving any indication as to the details of how the model will actually
be built. This provides an *implementation-independent* view of the
data. Since there will usually be many different ways to implement an
abstract data type, this implementation independence allows the
programmer to switch the details of the implementation without changing
the way the user of the data interacts with it. The user can remain
focused on the problem-solving process.


Why Study Algorithms?
---

Computer scientists learn by experience. We learn by seeing others solve
problems and by solving problems by ourselves. Being exposed to
different problem-solving techniques and seeing how different algorithms
are designed helps us to take on the next challenging problem that we
are given. By considering a number of different algorithms, we can begin
to develop pattern recognition so that the next time a similar problem
arises, we are better able to solve it.

Algorithms are often quite different from one another. Consider a function to calculate the square root of a number. It is entirely possible that there are
many different ways to implement the details to compute the square root. One algorithm may use many fewer resources than another. One
algorithm might take 10 times as long to return the result as the other.
We would like to have some way to compare these two solutions. Even
though they both work, one is perhaps “better” than the other. We might
suggest that one is more efficient or that one simply works faster or
uses less memory. As we study algorithms, we can learn analysis
techniques that allow us to compare and contrast solutions based solely
on their own characteristics, not the characteristics of the program or
computer used to implement them.

In the worst case scenario, we may have a problem that is intractable,
meaning that there is no algorithm that can solve the problem in a
realistic amount of time. It is important to be able to distinguish
between those problems that have solutions, those that do not, and those
where solutions exist but require too much time or other resources to
work reasonably.

There will often be trade-offs that we will need to identify and decide
upon. As computer scientists, in addition to our ability to solve
problems, we will also need to know and understand solution evaluation
techniques. In the end, there are often many ways to solve a problem.
Finding a solution and then deciding whether it is a good one are tasks
that we will do over and over again.


Assumed Knowledge
---

This book assumes intermediate knowledge of Python. If you encounter any unfamiliar Python usage, we encourage you to use [Learn Python the Hard Way](http://learnpythonthehardway.org/) or [Dive into Python](http://www.diveintopython.net/toc/index.html), both of which are excellent, free
