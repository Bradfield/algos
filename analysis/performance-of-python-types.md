Performance of Python Types
===========================

Now that you have a general idea of Big-O notation and the differences
between the different functions, our goal in this section is to tell you
about the Big-O performance for the operations on Python lists and
dictionaries. It is important for you to understand the efficiency of
these Python data structures because they are the building blocks we
will use as we implement other data structures in the remainder of the
book. In this section we will try to give you some intuitive understanding
of why the performance is what it is, but you will not fully appreciate
why this is the case until later chapters where we dive into the details
of how lists and dictionaries may be implemented.

Lists
---

The designers of Python had many choices to make when they implemented
the list data structure. Each of these choices could have an impact on
how fast list operations perform. To help them make the right choices
they looked at the ways that people would most commonly use the list
data structure and they optimized their implementation of a list so that
the most common operations were very fast. Of course they also tried to
make the less common operations fast, but when a tradeoff had to be made
the performance of a less common operation was often sacrificed in favor
of the more common operation.

Two common operations are indexing and assigning to an index position.
Both of these operations take the same amount of time no matter how
large the list becomes, because the values are simply assigned to or
retrieved from specific, known memory locations. As such, index lookup
and assignment on a list are both $$O(1)$$.

Another very common programming task is to grow a list. There are two
ways to create a longer list. You can use the append method or the
concatenation operator. The append method is $$O(1)$$, as the new value
is stored at a specific memory location that has already been allocated
for the array, much like index assignment. However, the
concatenation operator is $$O(k)$$ where $$k$$ is the size of the list that
is being concatenated, effectively because $$k$$ sequential assignment
operations must occur, equivalent to $$k$$ appends.

Popping from a list in Python is typically performed from its end, but
by passing an index (such as `0`) you can pop from a specific location.
The performance characteristics of the two are very different. When
`pop` is called on the end of the list it takes $$O(1)$$ but when pop is
called on the first element in the list or anywhere in the middle it is
$$O(n)$$. The reason for this lies in how Python chooses to implement
lists. When an item is taken from the front of the list, in Python’s
implementation, all the other elements in the list are shifted one
position closer to the beginning. This may seem silly to you now, but as
we explore an alternative list implementation in a later chapter, we
will see that this inefficiency is a concession that is made in order to
allow $$O(1)$$ index operations.

Much like popping from the start or middle of a list, inserting at an
index is $$O(n)$$ in Python, as every subsequent element must be shifted
one position closer to the end in order to accommodate the new element.
Deletion unsurprisingly behaves in the same way.

Iteration—somewhat intuitively—is $$O(n)$$. Iterating over $$n$$ items
requires $$n$$ steps. This also gives us an intuitive understanding of
why the `in` operator in Python is $$O(n)$$ when operating over a list—
effectively we must iterate over every element of the list to determine
if the element in question is contained therein.

The slice operations require some more thought. To access a slice `[a:b]`
of an array, we must iterate through every element between that at index
`a` and that at index `b`. As such slice access is $$O(k)$$ where $$k$$
is the number of elements in the slice. Deleting a slice is $$O(n)$$ for
the same reason that deleting a single element is—$$n$$ subsequent
elements must then be shifted toward the beginning of the list.

As mentioned previously, concatenation is $$O(k)$$ where $$k$$ is the
length of the concatenated list, due to an effective $$k$$ appends.
It follows that multiplying a list is $$O(nk)$$ as multiplication of
a $$k$$ length list $$n$$ times will involve $$k(n - 1)$$ appends, so
in the order of $$nk$$.

Reversing a list in $$O(n)$$ as each element must be repositioned.
Finally, as previously mentioned [sort in Python](http://svn.python.org/view/python/trunk/Objects/listsort.txt?revision=69846&view=markup) is $$O(n log n)$$, the
least intuitive of all of these outcomes, and [beyond the scope of this book](https://en.wikipedia.org/wiki/Timsort)
to demonstrate.

Below we provide a table of performance characteristics of Python list
operations, for future reference.


Operation  | Big-O Efficiency
--- | ---
index []    | $$O(1)$$
index assignment    | $$O(1)$$
append  | $$O(1)$$
pop()   | $$O(1)$$
pop(i)  | $$O(n)$$
insert(i, item)  | $$O(n)$$
del operator    | $$O(n)$$
iteration   | $$O(n)$$
contains (in)   | $$O(n)$$
get slice [x:y] | $$O(k)$$
del slice   | $$O(n)$$
reverse | $$O(n)$$
concatenate | $$O(k)$$
sort    | $$O(n log n)$$
multiply    | $$O(nk)$$


Dictionaries
---

The second major Python data structure is the dictionary. As you
probably recall, dictionaries differ from lists in that you can access
items in a dictionary by a key rather than a position. Later in this
book you will see that there are many ways to implement a dictionary.
The thing that is most important to notice right now is that the get
item and set item operations on a dictionary are $$O(1)$$. It is
difficult to provide an intuitive explanation for this without diving
into the implementation as we do later, except to say that a dictionary
is a structure created specifically for the purpose of setting and
retrieving values by key in constant time.

Another important dictionary operation is the contains operation.
Checking to see whether a key is in the dictionary or not is also $$O(1)$$.
This follows from the fact that getting an item from a dictionary is
itself $$O(1)$$.

Iterating over a dictionary is unsurprisingly $$O(n)$$, as is copying
the dictionary, as $$n$$ individual key/value pairs must be copied.

The efficiency of all dictionary operations is summarized in the table
below. One important side note on dictionary performance is that the
efficiencies we provide in the table are for average performance. In
some rare cases the contains, get item, and set item operations can
degenerate into $$O(n)$$ performance but we will get into that in a
later chapter when we talk about the different ways that a dictionary
could be implemented.

Operation  | Big-O Efficiency
--- | ---
copy   | $$O(n)$$
get item   | $$O(1)$$
set item   | $$O(1)$$
delete item| $$O(1)$$
contains (in)  | $$O(1)$$
iteration  | $$O(n)$$

Since Python is an evolving language, there are always changes going on
behind the scenes. The latest information on the performance of Python
data structures can be found on the Python website. As of this writing
the Python wiki has a nice time complexity page that can be found at the
[Time Complexity Wiki](http://wiki.python.org/moin/TimeComplexity).

