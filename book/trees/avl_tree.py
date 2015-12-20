# -*- coding: utf-8 -*-

"""
We will implement the AVL tree as a subclass of `BinarySearchTree`.
To begin, we will override the `_put` method and write a new
`update_balance` helper method. These methods are shown below. You
will notice that the definition for `_put` is exactly the same as in
simple binary search trees except for the additions of the calls to
`update_balance`.
"""

from binary_search_tree import BinarySearchTree, TreeNode


class AVLTreeNode(TreeNode):
    def __init__(self, *args, **kwargs):
        super(AVLTreeNode, self).__init__(*args, **kwargs)
        self.balance_factor = 0


class AVLTree(BinarySearchTree):

    TreeNodeClass = AVLTreeNode

    def _put(self, key, val, node):
        if key < node.key:
            if node.left:
                self._put(key, val, node.left)
            else:
                node.left = self.TreeNodeClass(key, val, parent=node)
                self.update_balance(node.left)
        else:
            if node.right:
                self._put(key, val, node.right)
            else:
                node.right = self.TreeNodeClass(key, val, parent=node)
                self.update_balance(node.right)

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)
    """

The new `update_balance` method is where most of the work is done. This
implements the recursive procedure we just described. The
`update_balance` method first checks to see if the current node is out of
balance enough to require rebalancing. If that is the case
then the rebalancing is done and no further updating to parents is
required. If the current node does not require rebalancing then the
balance factor of the parent is adjusted. If the balance factor of the
parent is non-zero then the algorithm continues to work its way up the
tree toward the root by recursively calling `update_balance` on the
parent.

When a rebalancing of the tree is necessary, how do we do it? Efficient
rebalancing is the key to making the AVL Tree work well without
sacrificing performance. In order to bring an AVL Tree back into balance
we will perform one or more **rotations** on the tree.

To understand what a rotation is let us look at a very simple example.
Consider the tree in the left half of the illustration below.
This tree is out of balance with a balance factor of -2. To bring this
tree into balance we will use a left rotation around the subtree rooted
at node A.

![Transforming an unbalanced tree using a left
rotation](figures/simple-unbalanced.png)

To perform a left rotation we essentially do the following:

-   Promote the right child (B) to be the root of the subtree.
-   Move the old root (A) to be the left child of the new root.
-   If new root (B) already had a left child then make it the right
    child of the new left child (A). Note: Since the new root (B) was
    the right child of A the right child of A is guaranteed to be empty
    at this point. This allows us to add a new node as the right child
    without any further consideration.

While this procedure is fairly easy in concept, the details of the code
are a bit tricky since we need to move things around in just the right
order so that all properties of a Binary Search Tree are preserved.
Furthermore we need to make sure to update all of the parent pointers
appropriately.

Let’s look at a slightly more complicated tree to illustrate the right
rotation. The left side of the illustration below shows a tree
that is left-heavy and with a balance factor of 2 at the root. To
perform a right rotation we essentially do the following:

-   Promote the left child (C) to be the root of the subtree.
-   Move the old root (E) to be the right child of the new root.
-   If the new root(C) already had a right child (D) then make it the
    left child of the new right child (E). Note: Since the new root (C)
    was the left child of E, the left child of E is guaranteed to be
    empty at this point. This allows us to add a new node as the left
    child without any further consideration.

![Transforming an unbalanced tree using a right
rotation](figures/rotate-right.png)

Now that you have seen the rotations and have the basic idea of how a
rotation works let us look at the code below for both the left
rotations. First we create a temporary variable to keep track of the new
root of the subtree. As we said before the new root is the right child
of the previous root. Now that a reference to the right child has been
stored in this temporary variable we replace the right child of the old
root with the left child of the new.

The next step is to adjust the parent pointers of the two nodes. If
`new_root` has a left child then the new parent of the left child becomes
the old root. The parent of the new root is set to the parent of the old
root. If the old root was the root of the entire tree then we must set
the root of the tree to point to this new root. Otherwise, if the old
root is a left child then we change the parent of the left child to
point to the new root; otherwise we change the parent of the right child
to point to the new root. Finally we set the parent of
the old root to be the new root. This is a lot of complicated
bookkeeping, so we encourage you to trace through this function while
looking at the diagram above.

"""
    def rotate_left(self, rotation_root):
        new_root = rotation_root.right
        rotation_root.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = rotation_root
        new_root.parent = rotation_root.parent
        if not rotation_root.parent:
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left = new_root
            else:
                rotation_root.parent.right = new_root
        new_root.left = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = \
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = \
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)

    def rotate_right(self, rotation_root):
        new_root = rotation_root.left
        rotation_root.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = rotation_root
        new_root.parent = rotation_root.parent
        if not rotation_root.parent:
            self.root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right = new_root
            else:
                rotation_root.parent.left = new_root
        new_root.right = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = \
            rotation_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = \
            new_root.balance_factor + 1 + max(rotation_root.balance_factor, 0)

    """

The last two lines require some explanation. In these lines we
update the balance factors of the old and the new root. Since all the
other moves are moving entire subtrees around the balance factors of all
other nodes are unaffected by the rotation. But how can we update the
balance factors without completely recalculating the heights of the new
subtrees? The following derivation should convince you that these lines
are correct.

![A left rotation](figures/balance-factor-derivation.png)

Above we see a left rotation. B and D are the
pivotal nodes and A, C, E are their subtrees. Let $$h_x$$ denote the
height of a particular subtree rooted at node $$x$$. By definition we know
the following:

$$newBal(B) = h_A - h_C$$

$$oldBal(B) = h_A - h_D$$

But we know that the old height of D can also be given by $$1 +
max(h_C,h_E)$$, that is, the height of D is one more than the maximum
height of its two children. Remember that $$h_c$$ and $$h_E$$ hav not
changed. So, let us substitute that in to the second equation, which
gives us

$$oldBal(B) = h_A - (1 + max(h_C,h_E))$$

and then subtract the two equations. The following steps do the
subtraction and use some algebra to simplify the equation for
$$newBal(B)$$.

$$newBal(B) - oldBal(B) = h_A - h_C - (h_A - (1 + max(h_C,h_E)))$$

$$newBal(B) - oldBal(B) = h_A - h_C - h_A + (1 + max(h_C,h_E))$$

$$newBal(B) - oldBal(B) = h_A  - h_A + 1 + max(h_C,h_E) - h_C $$

$$newBal(B) - oldBal(B) =  1 + max(h_C,h_E) - h_C$$

Next we will move $$oldBal(B)$$ to the right hand side of the equation and
make use of the fact that $$max(a,b)-c = max(a-c, b-c)$$.

$$newBal(B) = oldBal(B) + 1 + max(h_C - h_C ,h_E - h_C)$$

But, $$h_E - h_C$$ is the same as $$-oldBal(D)$$. So we can use another
identity that says $$max(-a,-b) = -min(a,b)$$. So we can finish our
derivation of $$newBal(B)$$ with the following steps:

$$newBal(B) = oldBal(B) + 1 + max(0 , -oldBal(D))$$

$$newBal(B) = oldBal(B) + 1 - min(0 , oldBal(D))$$

Now we have all of the parts in terms that we readily know. If we
remember that B is `rotation_root` and D is `new_root` then we can see this
corresponds exactly to the statement on the penulitmate line, or:

```python
rotation_root.balance_factor = \
    rotation_root.balance_factor + 1 - min(0, new_root.balance_factor)
```

A similar derivation gives us the equation for the updated node D, as
well as the balance factors after a right rotation. We leave these as
exercises for you.

Now you might think that we are done. We know how to do our left and
right rotations, and we know when we should do a left or right rotation,
but take a look at the diagram below. Since node A has a
balance factor of -2 we should do a left rotation. But, what happens
when we do the left rotation around A?

![An unbalanced tree that is more difficult to
balance](figures/hard-unbalanced.png)

The diagram below shows us that after the left rotation we
are now out of balance the other way. If we do a right rotation to
correct the situation we are right back where we started.

![After a left rotation, the tree is out of balance in the other
direction](figures/bad-rotatation.png)

To correct this problem we must use the following set of rules:

-   If a subtree needs a left rotation to bring it into balance, first
    check the balance factor of the right child. If the right child is
    left heavy then do a right rotation on right child, followed by the
    original left rotation.
-   If a subtree needs a right rotation to bring it into balance, first
    check the balance factor of the left child. If the left child is
    right heavy then do a left rotation on the left child, followed by
    the original right rotation.

The diagram below shows how these rules solve the dilemma
we encountered above. Starting with a right rotation around
node C puts the tree in a position where the left rotation around A
brings the entire subtree back into balance.

![A right rotation followed by a left rotation](figures/rotate-left-right.png)

The code that implements these rules can be found in our `rebalance`
method, which is shown below. Rule number
1 from above is implemented by the `if` statement starting on line 2.
Rule number 2 is implemented by the `elif` statement starting on line 8.

"""

    def rebalance(self, node):
        if node.balance_factor < 0 and node.right:
            if node.right.balance_factor > 0:
                self.rotate_right(node.right)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balance_factor > 0 and node.left:
            if node.left.balance_factor < 0:
                self.rotate_left(node.left)
                self.rotate_right(node)
            else:
                self.rotate_right(node)
