---
title: Implementing an Ordered List
layout: default.html
collection: lists
position: 5
---

In order to implement the ordered list, we must remember that the relative
positions of the items are based on some underlying characteristic. The
ordered list of integers given above (17, 26, 31, 54, 77, and 93) can be
represented by a linked structure as shown below. Again, the node and link
structure is ideal for representing the relative positioning of the items.

![An ordered linked list](figures/ordered-list.png)

To implement the `OrderedList` class, we will use the same technique as
seen previously with unordered lists. We will subclass `UnorderedList` and
leave the `__init__` method intact as once again, an empty list will be
denoted by a `head` reference to `None`.

<!-- literate lists/ordered_list.py -->

Analysis of Linked Lists
------------------------

To analyze the complexity of the linked list operations, we need to
consider whether they require traversal. Consider a linked list that has
*n* nodes. The `is_empty` method is $$O(1)$$ since it requires one step to
check the head reference for `None`. `size`, on the other hand, will
always require $$n$$ steps since there is no way to know how many nodes
are in the linked list without traversing from head to end. Therefore,
`length` is $$O(n)$$. Adding an item to an unordered list will always be
$$O(1)$$ since we simply place the new node at the head of the linked list.
However, `search` and `remove`, as well as `add` for an ordered list,
all require the traversal process. Although on average they may need to
traverse only half of the nodes, these methods are all $$O(n)$$ since in
the worst case each will process every node in the list.

You may also have noticed that the performance of this implementation
differs from the actual performance given earlier for Python lists. This
suggests that linked lists are not the way Python lists are implemented.
The actual implementation of a Python list is based on the notion of an
array. We discuss this in depth later.
