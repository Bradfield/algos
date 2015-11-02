---
title: Summary of Map ADT Implementations
layout: chapter.html
collection: graphs
position: 1
---

Over the past few sections we have looked at several data structures
that can be used to implement the map abstract data type. A binary
Search on a list, a hash table, a binary search tree, and a balanced
binary search tree. To conclude this section, let’s summarize the
performance of each data structure for the key operations defined by the
map ADT.

operation |  Sorted List | Hash Table  | Binary Search Tree | AVL Tree
--- | --- | --- | --- | ---
`put` | $$O(n)$$    | $$O(1)$$   | $$O(n)$$   | $$O(log2n)$$
`get` | $$O(log2n)$$    | $$O(1)$$   | $$O(n)$$   | $$O(log2n)$$
`in`  | $$O(log2n)$$    | $$O(1)$$   | $$O(n)$$   | $$O(log2n)$$
`del` | $$O(n)$$)   | $$O(1)$$   | $$O(n)$$   | $$O(log2n)$$
