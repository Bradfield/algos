---
title: What is a Stack?
layout: chapter.html
collection: stacks
position: 1
---

We will begin our study of data structures by considering four simple
but very powerful concepts. Stacks, queues, deques, and lists are
examples of data collections whose items are ordered depending on how
they are added or removed. Once an item is added, it stays in that
position relative to the other elements that came before and came after
it. Collections such as these are often referred to as *linear data
structures*.

Linear structures can be thought of as having two ends. Sometimes these
ends are referred to as the “left” and the “right” or in some cases the
“front” and the “rear.” You could also call them the “top” and the
“bottom.” The names given to the ends are not significant. What
distinguishes one linear structure from another is the way in which
items are added and removed, in particular the location where these
additions and removals occur. For example, a structure might allow new
items to be added at only one end. Some structures might allow items to
be removed from either end.

These variations give rise to some of the most useful data structures in
computer science. They appear in many algorithms and can be used to
solve a variety of important problems.

Stacks
---

A *stack* is an ordered
collection of items where the addition of new items and the removal of
existing items always takes place at the same end. This end is commonly
referred to as the “top.” The end opposite the top is known as the
“base.”

The base of the stack is significant since items stored in the stack
that are closer to the base represent those that have been in the stack
the longest. The most recently added item is the one that is in position
to be removed first. This ordering principle is sometimes called
*LIFO*, (last in, first out). It provides an ordering based on length
of time in the collection. Newer items are near the top, while older
items are near the base.

Many examples of stacks occur in everyday situations. Almost any
cafeteria has a stack of trays or plates where you take the one at the
top, uncovering a new tray or plate for the next customer in line.
Imagine a stack of books on a desk.
The only book whose cover is visible is the one on top. To access others
in the stack, we need to remove the ones that are sitting on top of
them.

![A stack of books](figures/bookstack2.png)

Here is another stack, this one contains a number of primitive Python data objects:

![A Stack of primitive Python objects](figures/primitive.png)

One of the most useful ideas related to stacks comes from the simple
observation of items as they are added and then removed. Assume you
start out with a clean desktop. Now place books one at a time on top of
each other. You are constructing a stack. Consider what happens when you
begin removing books. The order that they are removed is exactly the
reverse of the order that they were placed. Stacks are fundamentally
important, as they can be used to reverse the order of items. The order
of insertion is the reverse of the order of removal.
Below we show the Python data object stack as it
was created and then again as items are removed. Note the order of the
objects.

![The reversal property of stacks](figures/simple-reversal.png)

Considering this reversal property, you can perhaps think of examples of
stacks that occur as you use your computer. For example, every web
browser has a Back button. As you navigate from web page to web page,
those pages are placed on a stack (actually it is the URLs that are
going on the stack). The current page that you are viewing is on the top
and the first page you looked at is at the base. If you click on the
Back button, you begin to move in reverse order through the pages.
