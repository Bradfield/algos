---
title: Performance of Python Types
collection: analysis
position: 4
layout: default.html
---

Now that you have a general idea of big O notation, our goal in this section
is to tell you about the big O performance for the most commonly-used
operations supported by Python lists and dictionaries. The efficiencies of
these data types are important because we use them to implement other abstract data structures in the remainder of this book.

This section is intended to give you some intuitive understanding of *why* the
performances are what they are, but you will not fully appreciate these reasons
until later, when we explore how lists and dictionaries may be implemented.

Keep in mind that there is a difference between the Python *language* and a
[Python implementation](https://wiki.python.org/moin/PythonImplementations).
Our discussion below assumes the use of the CPython implementation.

Lists
---

The designers of the Python list data type had many choices to make during
implementation. Each choice had an impact on how quickly the list could perform
operations. One decision they made was to optimize the list implementation for
commonly-used operations. This doesn't mean rarer operations are slow; it just
means that common operations got preference during situations where the
designers had to make a tradeoff.

Two common operations are indexing and assigning to an index position. In
Python lists, values are assigned to and retrieved from specific, known memory
locations. No matter how large the list is, then, index lookup and assignment
take a constant amount of time and are thus $$O(1)$$.

Another common programming need is to grow a list. There are two ways to do
this: you can use the `append` method or the concatenation operator (`+`).

The `append` method is “amortized” $$O(1)$$. In most cases, the memory required
to append a new value has already been allocated, which is strictly $$O(1)$$.
Once the C array underlying the list has been exhausted, it must be expanded in
order to accomodate further `append`s. This periodic expansion process is
linear relative to the size of the new array, which seems to contradict our
claim that `append`ing is $$O(1)$$.

However, the expansion rate is cleverly chosen to be three times the previous
size of the array; when we spread the expansion cost over each additional
`append` afforded by this extra space, the cost per `append` is $$O(1)$$ *on an
amortized basis*.

On the other hand, concatenation is $$O(k)$$, where $$k$$ is the size of the
concatenated list, since $$k$$ sequential assignment operations must occur.

Popping from a Python list is typically performed from its end but, by passing
an index, you can pop from a specific position. When `pop` is called from the
end, the operation is $$O(1)$$, while calling `pop` from anywhere else is
$$O(n)$$. Why the difference?

When an item is taken from the front of a Python list, all other elements in
the list are shifted one position closer to the beginning. This is an
unavoidable cost to allow $$O(1)$$ index lookup, which is the more common
operation.

For the same reasons, inserting at an index is $$O(n)$$; every subsequent
element must be shifted one position closer to the end to accomodate the new
element. Unsurprisingly, deletion behaves the same way.

Iteration is $$O(n)$$ because iterating over $$n$$ elements requires $$n$$
steps. This also explains why the `in` operator in Python is $$O(n)$$: to
determine whether an element is in a list, we must iterate over every element.

Slice operations require more thought. To access the slice `[a:b]` of a list,
we must iterate over every element between indices `a` and `b`. So, slice
access is $$O(k)$$, where $$k$$ is the size of the slice. Deleting a slice is
$$O(n)$$ for the same reason that deleting a single element is $$O(n)$$: $$n$$
subsequent elements must be shifted toward the list's beginning.

To understand list multiplication, remember that concatenation is $$O(k)$$,
where $$k$$ is the length of the concatenated list. It follows that multiplying
a list is $$O(nk)$$, since multiplying a $$k$$-sized list $$n$$ times will
require $$k(n - 1)$$ appends.

Reversing a list is $$O(n)$$ since we must reposition each element.

Finally (and least intuitively), [sorting in Python](http://svn.python.org/view/python/trunk/Objects/listsort.txt?revision=69846&view=markup)
is $$O(nlog n)$$ and [beyond the scope of this book](https://en.wikipedia.org/wiki/Timsort) to demonstrate.

For future reference, we have summarized the performance characteristics of
Python's list operations in the table below:

Operation  | Big O Efficiency
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

The second major Python data type is the dictionary. As you might recall,
dictionaries differ from lists in their ability to access items by key rather
than position. For now, the most important characteristic to note is that
“getting” and “setting” an item in a dictionary are both $$O(1)$$ operations.

We won't immediately attempt to provide an intuitive explanation for this, but
rest assured that we will dive into a discussion of dictionary implementations
later. For now, simply remember that dictionaries were created specifically for
the purpose of getting and setting values by key as fast as possible.

Another important dictionary operation is checking whether a key is present in
a dictionary. This “contains” operation is also $$O(1)$$ because checking for
a given key is implicit in getting an item from a dictionary, which is itself
$$O(1)$$.

Iterating over a dictionary is $$O(n)$$, as is copying the dictionary, since
$$n$$ key/value pairs must be copied.

We have summarized the efficencies of all dictionary operations in the table
below:

Operation  | Big O Efficiency
--- | ---
copy   | $$O(n)$$
get item   | $$O(1)$$
set item   | $$O(1)$$
delete item| $$O(1)$$
contains (in)  | $$O(1)$$
iteration  | $$O(n)$$

One important sidenote is that the efficiences provided in the above tables are
performances in the *average case*. In rare cases, “contains”, “get item” and
“set item” can degenerate into $$O(n)$$ performance but, again, we shall save
that discussion for when we talk about different ways of implementing a
dictionary.

---

Python is still an evolving language, so there are always changes going on
behind the scenes. The latest information on the performance of Python data
types can be found on the Python website. As of this writing, the Python wiki
has a nice time complexity page that can be found at the
[Time Complexity Wiki](http://wiki.python.org/moin/TimeComplexity).
