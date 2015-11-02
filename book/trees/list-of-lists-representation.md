---
title: List of Lists Representation
layout: chapter.html
collection: graphs
position: 1
---

One way to represent trees succinctly is as a list of lists. Consider that in a list of lists, each element has one and only one parent (up to the outermost list) so meets our expectation of a tree as a hierarchical structure with no cycles.

In a list of lists tree, we will store the value of the each node as the first element of
the list. The second element of the list will itself be a list that
represents the left subtree. The third element of the list will be
another list that represents the right subtree. To illustrate this
storage technique, let’s look at an example:

![A Small Tree](figures/smalltree.png)

```python
tree = [
    'a',  #root
    [
        'b',  # left subtree
        ['d' [], []],
        ['e' [], []]
    ],
    [
        'c',  # right subtree
        ['f' [], []],
        []
    ]
]
```

Notice that we can access subtrees of the list using standard list
indexing. The root of the tree is `tree[0]`, the left subtree of the
root is `tree[1]`, and the right subtree is `tree[2]`.
Below we illustrate creating a simple tree
using a list. Once the tree is constructed, we can access the root and
the left and right subtrees.

```python
tree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]

# the left subtree
tree[1]  # => ['b', ['d', [], []], ['e', [], []]]

# the right subtree
tree[2]  # => ['c', ['f', [], []], []]

# the root
tree[0]  # => 'a'
```

One very nice property of this list of
lists approach is that the structure of a list representing a subtree
adheres to the structure defined for a tree; the structure itself is
recursive! A subtree that has a root value and two empty lists is a leaf
node. Another nice feature of the list of lists approach is that it
generalizes to a tree that has many subtrees. In the case where the tree
is more than a binary tree, another subtree is just another list.

Let’s formalize this definition of the tree data structure by providing
some functions that make it easy for us to use lists as trees. Note that
we are not going to define a binary tree class. The functions we will
write will just help us manipulate a standard list as though we are
working with a tree.

```python
def make_binary_tree(r):
    return [r, [], []]
```

The `make_binary_tree` function simply constructs a list with a root node and
two empty sublists for the children. To add a left subtree to the root
of a tree, we need to insert a new list into the second position of the
root list. We must be careful. If the list already has something in the
second position, we need to keep track of it and push it down the tree
as the left child of the list we are adding. Here is the Python code for inserting a left child:


```python
def insert_left(root, child_val):
    subtree = root.pop(1)
    if len(subtree) > 1:
        root.insert(1, [child_val, subtree, []])
    else:
        root.insert(1, [child_val, [], []])
    return root
```

Notice that to insert a left child, we first obtain the (possibly empty)
list that corresponds to the current left child. We then add the new
left child, installing the old left child as the left child of the new
one. This allows us to splice a new node into the tree at any position.
The code for `insert_right` is similar to `insert_left` and is shown below:

```python
def insert_right(root, child_val):
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [child_val, [], subtree])
    else:
        root.insert(2, [child_val, [], []])
    return root
```

To round out this set of tree-making functions, let’s write a couple of access
functions for getting and setting the root value, as well as getting the
left or right subtrees. This way we can abstract away the fact that we use the positions in a list to represent values, left subtrees and right subtrees:

```python
def get_root_val(root):
    return root[0]

def set_root_val(root, new_val):
    root[0] = new_val

def get_left_child(root):
    return root[1]

def get_root_child(root):
    return root[2]
```

We can now use our `make_binary_tree` definition to build a tree and retrieve children of given nodes:

```python
root = make_binary_tree(3)
insert_left(root, 4)
insert_left(root, 5)
insert_right(root, 6)
insert_right(root, 7)
left = get_left_child(root)
left  # => [5, [4, [], []], []]

set_root_val(left, 9)
root  # => [3, [9, [4, [], []], []], [7, [], [6, [], []]]]

insert_left(left, 11)
root  # => [3, [9, [11, [4, [], []], []], []], [7, [], [6, [], []]]]
get_root_child(get_root_child(root))  # => [6, [], []]
```
