---
title: Introduction to Lists
layout: default.html
collection: lists
position: 1
---

Throughout the discussion of basic data structures, we have used Python lists to implement the abstract data types presented. Unfortunately, “list” is not the best name for this collection type, as we will soon see (a better name would be “array”).

When discussing the list _abstract data type_, we consider a list to be a collection of items where each item holds a relative position with respect to the others.

The members of a list are commonly refered to as nodes. When each node holds a reference to the next node in the list, we call this a singly linked list. When each node holds a reference to both the next and previous nodes in the list, we call this a doubly linked list.

For simplicity we will assume that lists cannot contain duplicate items. Again this is a point of departure from Python’s native list type.

In this chapter we will consider both unordered and ordered lists. As we will see, an ordered list is simply a list with additional functionality designed to maintain its constituent nodes in a particular order.

The Unordered List Abstract Data Type
---

The structure of an unordered list, as described above, is a collection
of items where each item holds a relative position with respect to the
others. Some possible unordered list operations are given below.

-   `List()` creates a new list that is empty. It needs no parameters
    and returns an empty list.
-   `add(item)` adds a new item to the list. It needs the item and
    returns nothing. Assume the item is not already in the list.
-   `remove(item)` removes the item from the list. It needs the item and
    modifies the list. Assume the item is present in the list.
-   `search(item)` searches for the item in the list. It needs the item
    and returns a boolean value.
-   `is_empty()` tests to see whether the list is empty. It needs no
    parameters and returns a boolean value.
-   `size()` returns the number of items in the list. It needs no
    parameters and returns an integer.
-   `append(item)` adds a new item to the end of the list making it the
    last item in the collection. It needs the item and returns nothing.
    Assume the item is not already in the list.
-   `index(item)` returns the position of item in the list. It needs the
    item and returns the index. Assume the item is in the list.
-   `insert(pos, item)` adds a new item to the list at position pos. It
    needs the item and returns nothing. Assume the item is not already
    in the list and there are enough existing items to have
    position pos.
-   `pop()` removes and returns the last item in the list. It needs
    nothing and returns an item. Assume the list has at least one item.
-   `pop(pos)` removes and returns the item at position pos. It needs
    the position and returns the item. Assume the item is in the list.

The Ordered List
---

Later in this section we will also consider the ordered list, which is an
abstract data type identical to the unordered list described above, but with
the additional property that its items are maintained in a meaningful order.
For instance if we add the numbers 2, 3 and 1 to an ordered list, we would
expect to be able to access them as `1 -> 2 -> 3` or perhaps `3 -> 2 -> 1`
depending on whether that ordered list is designed to maintain an ascending
or descending order.
