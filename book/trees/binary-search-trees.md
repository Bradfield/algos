---
title: Binary Search Trees
layout: chapter.html
collection: trees
position: 10
---

We have already seen two different ways to get key-value pairs in a
collection. Recall that these collections implement the **map** abstract
data type. The two implementations of a map ADT we discussed were binary
search on a list and hash tables. In this section we will study **binary
search trees** as yet another way to map from a key to a value. In this
case we are not interested in the exact placement of items in the tree,
but we are interested in using the binary tree structure to provide for
efficient searching.

Before we look at the implementation, let’s review the interface
provided by the map ADT. You will notice that this interface is very
similar to the Python dictionary.

-   `Map()` Create a new, empty map.
-   `put(key, val)` Add a new key-value pair to the map. If the key is
    already in the map then replace the old value with the new value.
-   `get(key)` Given a key, return the value stored in the map or
    `None` otherwise.
-   `del` Delete the key-value pair from the map using a statement of
    the form `del map[key]`.
-   `len()` Return the number of key-value pairs stored in the map.
-   `in` Return `True` for a statement of the form `key in map`, if the
    given key is in the map.

