List of Lists Representation
============================

In a tree represented by a list of lists, we will begin with Python’s
list data structure and write the functions defined above. Although
writing the interface as a set of operations on a list is a bit
different from the other abstract data types we have implemented, it is
interesting to do so because it provides us with a simple recursive data
structure that we can look at and examine directly. In a list of lists
tree, we will store the value of the root node as the first element of
the list. The second element of the list will itself be a list that
represents the left subtree. The third element of the list will be
another list that represents the right subtree. To illustrate this
storage technique, let’s look at an example.
Figure 1 &lt;fig\_smalltree&gt; shows a simple tree and the
corresponding list implementation.

![Figure 1: A Small Tree](Figures/smalltree.png)

    myTree = ['a',   #root
          ['b',  #left subtree
           ['d' [], []],
           ['e' [], []] ],  
          ['c',  #right subtree
           ['f' [], []],
           [] ]  
         ]           

Notice that we can access subtrees of the list using standard list
indexing. The root of the tree is `myTree[0]`, the left subtree of the
root is `myTree[1]`, and the right subtree is `myTree[2]`.
ActiveCode 1 &lt;lst\_treelist1&gt; illustrates creating a simple tree
using a list. Once the tree is constructed, we can access the root and
the left and right subtrees. One very nice property of this list of
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

:

    def BinaryTree(r):
        return [r, [], []]    

The `BinaryTree` function simply constructs a list with a root node and
two empty sublists for the children. To add a left subtree to the root
of a tree, we need to insert a new list into the second position of the
root list. We must be careful. If the list already has something in the
second position, we need to keep track of it and push it down the tree
as the left child of the list we are adding.
Listing 1 &lt;lst\_linsleft&gt; shows the Python code for inserting a
left child.

**Listing 1**

    def insertLeft(root,newBranch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1,[newBranch,t,[]])
        else:
            root.insert(1,[newBranch, [], []])
        return root

Notice that to insert a left child, we first obtain the (possibly empty)
list that corresponds to the current left child. We then add the new
left child, installing the old left child as the left child of the new
one. This allows us to splice a new node into the tree at any position.
The code for `insertRight` is similar to `insertLeft` and is shown in
Listing 2 &lt;lst\_linsright&gt;.

**Listing 2**

    def insertRight(root,newBranch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2,[newBranch,[],t])
        else:
            root.insert(2,[newBranch,[],[]])
        return root

To round out this set of tree-making functions(see
Listing 3 &lt;lst\_treeacc&gt;), let’s write a couple of access
functions for getting and setting the root value, as well as getting the
left or right subtrees.

**Listing 3**

:

    def getRootVal(root):
        return root[0]

    def setRootVal(root,newVal):
        root[0] = newVal

    def getLeftChild(root):
        return root[1]

    def getRightChild(root):
        return root[2]

ActiveCode 2 &lt;lst\_bintreetry&gt; exercises the tree functions we
have just written. You should try it out for yourself. One of the
exercises asks you to draw the tree structure resulting from this set of
calls.

> **Self Check**
>
> Write a function `buildTree` that returns a tree using the list of
> lists functions that looks like this:
>
> ![image](Figures/tree_ex.png)
