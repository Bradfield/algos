---
title: Implementing an Unordered List
layout: default.html
collection: lists
position: 3
---

In order to implement an unordered list, we will construct what is
commonly known as a **linked list**. Recall that we need to be sure that
we can maintain the relative positioning of the items. However, there is
no requirement that we maintain that positioning in contiguous memory.
For example, consider the collection of items shown below. It appears that these values have been
placed randomly.

![Items not constrained in their physical
placement](figures/random-items.png)

If we can maintain some explicit information in each
item, namely the location of the next item, then the relative position of each item
can be expressed by simply following the link from one item to the next:

![Relative positions maintained by explicit
links](figures/explicit-links.png)

It is important to note that the location of the first item of the list
must be explicitly specified. Once we know where the first item is, the
first item can tell us where the second is, and so on. The external
reference is often referred to as the **head** of the list. Similarly,
the last item needs to know that there is no next item.

<!-- literate lists/unordered_list.py -->
