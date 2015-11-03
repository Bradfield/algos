---
title: What is a List?
layout: chapter.html
collection: lists
position: 1
---

Throughout the discussion of basic data structures, we have used Python lists to implement the abstract data types presented. Unfortunately, “list” is not the best name for this collection type, as we will soon see (a better name would be “array”).

When discussing the list _abstract data type_, we consider a list to be a collection of items where each item holds a relative position with respect to the others.

The members of a list are comonly refered to as nodes. When each node holds a reference to the next node in the list, we call this a singly linked list. When each node holds a reference to both the next and previous nodes in the list, we call this a doubly linked list.

For simplicity we will assume that lists cannot contain duplicate items. Again this is a point of departure from Python’s native list type.

In this section we will consider both unordered and ordered lists. As we will see, an ordered list is simply a list with additional functionality designed to maintain its constituent nodes in a particular order.
