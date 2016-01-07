---
title: What is a Stack?
layout: default.html
collection: stacks
position: 1
---

We will begin our study of data structures by considering four simple
but very powerful concepts. Stacks, queues, deques, and lists are
examples of data collections whose items are ordered depending on how
they are added or removed. Once an item is added, it stays in that
position relative to the other elements that came before and came after
it. These are often referred to as *linear data structures*.

Linear structures can be thought of as having two ends, referred to
variously as “left” and “right”; “top” and “bottom”; or, “front” and
“rear”. The names given to the ends are not significant; what
distinguishes one linear structure from another is the location where
additions and removals may occur. For example, a structure might allow
new items to be added at only one end and removed at another; another
may allow addition or removal from either end.

These variations give rise to some of the most useful data structures in
computer science. They appear in many algorithms and can be used to
solve a variety of important problems.

Stacks
---

A *stack* is an ordered collection of items where the addition of new
items and the removal of existing items always takes place at the same
end. This end is commonly referred to as the “top.” The end opposite the
top is known as the “base.”

The base of the stack is significant since items stored in the stack
that are closer to the base represent those that have been in the stack
the longest. The most recently added item is the one that is in position
to be removed first. This ordering principle is sometimes called
*LIFO*, (last in, first out). It provides an ordering based on length
of time in the collection. Newer items are near the top, while older
items are near the base.

Many examples of stacks occur in everyday situations. Consider a stack
of plates on a table, where it is possible to add or remove plates only
to or from the top. Equivalently, imagine a stack of books on a desk.
The only book whose cover is visible is the one on top. To access others
in the stack, we need to remove the ones that are sitting on top of
them.

![A stack of books](figures/bookstack2.png)

Here is another stack, this one contains a number of primitive Python
data objects:

![A Stack of primitive Python objects](figures/primitive.png)

One of the most useful ideas related to stacks comes from the simple
observation that the order of insertion is the reverse of the order of
removal. Assume you start out with a clean desk. Now place books one at
a time on top of each other and consider what happens when you begin
removing books: the order that they are removed is exactly the reverse
of the order that they were placed. Stacks are fundamentally important,
as they can be used to reverse the order of items.

Below we show the Python data object stack as it was created and then
again as items are removed. Note the order of the objects.

![The reversal property of stacks](figures/simple-reversal.png)

Considering this reversal property, you can perhaps think of examples of
stacks that occur as you use your computer. For example, every web
browser has a Back button. As you navigate from web page to web page,
the URLs of those pages are placed on a stack. The current page that you
are viewing is on the top and the first page you looked at is at the
base. If you click on the Back button, you begin to move in reverse
order through the pages.
