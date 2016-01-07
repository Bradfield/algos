---
title: Binary Search Trees
layout: default.html
collection: trees
position: 10
---

So far we have seen two different ways to implement the **map** abstract
data type—binary search on a list, and hash tables. In this section we
will consider the binary tree, which is the basis of another common
implementation of maps focused on efficient searching.

Before we look at the implementation, let’s review the interface
provided by the map ADT. Notice that this interface is very
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


Implementation
---

A binary search tree relies on the property that keys that are less than
the parent are found in the left subtree, and keys that are greater than
the parent are found in the right subtree. We will call this the **BST
property**. As we implement the `Map` interface as described above, the
BST property will guide our implementation. The diagram below
illustrates this property of a binary search tree, showing the keys
without any associated values. Notice that the property holds for each
parent and child. All of the keys in the left subtree are less than the
key in the root; all of the keys in the right subtree are greater than
the root.

![A simple binary search tree](figures/simple-binary-search-tree.png)

Now that you know what a binary search tree is, we will look at how a
binary search tree is constructed. The search tree above represents the nodes that exist after we
have inserted the following keys in the order:
$$70, 31, 93, 94, 14, 23, 73$$. Since 70 was the first key inserted into the
tree, it is the root. Next, 31 is less than 70, so it becomes the left
child of 70. Next, 93 is greater than 70, so it becomes the right child
of 70. Now we have two levels of the tree filled, so the next key is
going to be the left or right child of either 31 or 93. Since 94 is
greater than 70 and 93, it becomes the right child of 93. Similarly 14
is less than 70 and 31, so it becomes the left child of 31. 23 is also
less than 31, so it must be in the left subtree of 31. However, it is
greater than 14, so it becomes the right child of 14.

To implement the binary search tree, we will use the nodes and
references approach. While it would be possible in Python to implement
the tree using `dict`s as we have elsewhere in this chapter, doing so
presupposes that we have the very associative structure that we are
implementing!

Our implementation will use two classes: `TreeNode` to house the lower
level logic to construct and manipulate the tree itself, and
`BinarySearchTree` to hold a reference to the root node and provide a
map-like interface to the user.

<!-- litpy trees/binary_search_tree.py -->

Analysis
---

With the implementation of a binary search tree now complete, we will do
a quick analysis of the methods we have implemented. Let’s first look at
the `put` method. The limiting factor on its performance is the height
of the binary tree. Recall that the height
of a tree is the number of edges between the root and the deepest leaf
node. The height is the limiting factor because when we are searching
for the appropriate place to insert a node into the tree, we will need
to do at most one comparison at each level of the tree.

What is the height of a binary tree likely to be? The answer to this
question depends on how the keys are added to the tree. If the keys are
added in a random order, the height of the tree is going to be around
$$\log_2{n}$$ where $$n$$ is the number of nodes in the tree. This is
because if the keys are randomly distributed, around half of them will be
less than the root and half will be greater than the root. Remember that
in a binary tree there is one node at the root, two nodes in the next
level, and four at the next. The number of nodes at any particular level
is $$2^d$$ where $$d$$ is the depth of the level. The total number of nodes
in a perfectly balanced binary tree is $$2^{h+1}-1$$, where $$h$$ represents
the height of the tree.

A perfectly balanced tree has the same number of nodes in the left
subtree as it does in the right subtree. In a balanced binary tree, the worst-case
performance of `put` is $$O(\log_2{n})$$, where $$n$$ is the number of nodes
in the tree. Notice that this is the inverse relationship to the
calculation in the previous paragraph. So $$\log_2{n}$$ gives us the
height of the tree, and represents the maximum number of comparisons
that `put` will need to do as it searches for the proper place to insert
a new node.

Unfortunately it is possible to construct a search tree that has height
$$n$$ simply by inserting the keys in sorted order! An example of such a
tree is shown below. In this
case the performance of the `put` method is $$O(n)$$.

![A skewed binary search tree would give poor performance](figures/skewed-tree.png)

Now that you understand that the performance of the `put` method is
limited by the height of the tree, you can probably guess that other
methods, `get`, `in`, and `del`, are limited as well. Since `get` searches
the tree to find the key, in the worst case the tree is searched all the
way to the bottom and no key is found. At first glance `del` might seem
more complicated, since it may need to search for the successor before
the deletion operation can complete. But remember that the worst-case
scenario to find the successor is also just the height of the tree which
means that you would simply double the work. Since doubling is a
constant factor it does not change worst case
