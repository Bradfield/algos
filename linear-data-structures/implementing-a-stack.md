Implementing a Stack in Python
==============================

Now that we have clearly defined the stack as an abstract data type we
will turn our attention to using Python to implement the stack. Recall
that when we give an abstract data type a physical implementation we
refer to the implementation as a data structure.

As we described in Chapter 1, in Python, as in any object-oriented
programming language, the implementation of choice for an abstract data
type such as a stack is the creation of a new class. The stack
operations are implemented as methods. Further, to implement a stack,
which is a collection of elements, it makes sense to utilize the power
and simplicity of the primitive collections provided by Python. We will
use a list.

Recall that the list class in Python provides an ordered collection
mechanism and a set of methods. For example, if we have the list
\[2,5,3,6,7,4\], we need only to decide which end of the list will be
considered the top of the stack and which will be the base. Once that
decision is made, the operations can be implemented using the list
methods such as `append` and `pop`.

The following stack implementation
(ActiveCode 1 &lt;lst\_stackcode1&gt;) assumes that the end of the list
will hold the top element of the stack. As the stack grows (as `push`
operations occur), new items will be added on the end of the list. `pop`
operations will manipulate that same end.

Remember that nothing happens when we click the `run` button other than
the definition of the class. We must create a `Stack` object and then
use it. ActiveCode 2 &lt;lst\_stackcode1&gt; shows the `Stack` class in
action as we perform the sequence of operations from
Table 1 &lt;tbl\_stackops&gt;. Notice that the definition of the `Stack`
class is imported from the `pythonds` module.

> **note**
>
> The `pythonds` module contains implementations of all data structures
> discussed in this book. It is structured according to the sections:
> basic, trees, and graphs. The module can be downloaded from
> [pythonworks.org](http://www.pythonworks.org/pythonds).

It is important to note that we could have chosen to implement the stack
using a list where the top is at the beginning instead of at the end. In
this case, the previous `pop` and `append` methods would no longer work
and we would have to index position 0 (the first item in the list)
explicitly using `pop` and `insert`. The implementation is shown in
CodeLens 1 &lt;lst\_stackcode2&gt;.

This ability to change the physical implementation of an abstract data
type while maintaining the logical characteristics is an example of
abstraction at work. However, even though the stack will work either
way, if we consider the performance of the two implementations, there is
definitely a difference. Recall that the `append` and `pop()` operations
were both O(1). This means that the first implementation will perform
push and pop in constant time no matter how many items are on the stack.
The performance of the second implementation suffers in that the
`insert(0)` and `pop(0)` operations will both require O(n) for a stack
of size n. Clearly, even though the implementations are logically
equivalent, they would have very different timings when performing
benchmark testing.

> **Self Check**
>
> Write a function revstring(mystr) that uses a stack to reverse the
> characters in a string.
