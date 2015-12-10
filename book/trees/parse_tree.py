# -*- coding: utf-8 -*-

import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
LEFT_PAREN = '('
RIGHT_PAREN = ')'


def build_parse_tree(expression):
    tree = {}
    stack = [tree]
    node = tree
    for token in expression:
        if token == LEFT_PAREN:
            node['left'] = {}
            stack.append(node)
            node = node['left']
        elif token == RIGHT_PAREN:
            node = stack.pop()
        elif token in OPERATORS.keys():
            node['val'] = token
            node['right'] = {}
            stack.append(node)
            node = node['right']
        else:
            node['val'] = int(token)
            parent = stack.pop()
            node = parent
    return tree

"""

The four rules for building a parse tree are coded as the four clauses
of the `if` statement above. In each case you can see that the code implements
the rule.

Now that we have built a parse tree, we can write a function to evaluate it,
returning the numerical result. To write this function, we will make use of
the hierarchical nature of the tree to write an algorithm that evaluates a
parse tree by recursively evaluating each subtree.

A natural base case for recursive algorithms that operate on trees is to check
for a leaf node. In a parse tree, the leaf nodes will always be operands.
Since numerical objects like integers and floating points require no further
interpretation, the `evaluate` function can simply return the value stored in
the leaf node. The recursive step that moves the function toward the base case
is to call `evaluate` on both the left and the right children of the current
node. The recursive call effectively moves us down the tree, toward a leaf
node.

To put the results of the two recursive calls together, we can simply apply
the operator stored in the parent node to the results returned from evaluating
both children. In the example from above we see that the two children of the
root evaluate to themselves, namely 10 and 3. Applying the multiplication
operator gives us a final result of 30.

The code for a recursive `evaluate` function is shown below. First, we obtain
references to the left and the right children of the current node. If both the
left and right children evaluate to `None`, then we know that the current node
is really a leaf node. If the current node is not a leaf node, look up the
operator in the current node and apply it to the results from recursively
evaluating the left and right children.

To implement the arithmetic, we use a dictionary with the keys
`'+', '-', '*'`, and `'/'`. The values stored in the dictionary are
functions from Python’s operator module. The operator module provides us
with the functional versions of many commonly used operators. When we
look up an operator in the dictionary, the corresponding function object
is retrieved. Since the retrieved object is a function, we can call it
in the usual way `function(param1, param2)`. So the lookup
`OPERATORS['+'](2, 2)` is equivalent to `operator.add(2, 2)`.
"""


def evaluate(tree):
    try:
        operate = OPERATORS[tree['val']]
        return operate(evaluate(tree['left']), evaluate(tree['right']))
    except KeyError:
        # no left or no right, so is a leaf - our base case
        return tree['val']

"""

Finally, we will trace the `evaluate` function on the parse tree we created
above. When we first call `evaluate`, we pass the root of the entire tree as
the parameter `parse_tree`. Then since the left and right children exist, we
look up the operator in the root of the tree, which is `'+'`, and which maps
to the `operator.add` function. As usual for a Python function call, the first
thing Python does is to evaluate the parameters that are passed to the
function. In this case both parameters are recursive function calls to our
`evaluate` function. Using left-to-right evaluation, the first recursive call
goes to the left. In the first recursive call the `evaluate` function is given
the left subtree. We find that the node has no left or right children, so we
are in a leaf node. When we are in a leaf node we just return the value stored
in the leaf node as the result of the evaluation. In this case we return the
integer 3.

At this point we have one parameter evaluated for our top-level call to
`operator.add`. But we are not done yet. Continuing the left-to-right
evaluation of the parameters, we now make a recursive call to evaluate
the right child of the root. We find that the node has both a left and a
right child so we look up the operator stored in this node, `'*'`, and
call this function using the left and right children as the parameters.
At this point you can see that both recursive calls will be to leaf
nodes, which will evaluate to the integers four and five respectively.
With the two parameters evaluated, we return the result of
`operator.mul(4, 5)`. At this point we have evaluated the operands for
the top level `'+'` operator and all that is left to do is finish the
call to `operator.add(3, 20)`. The result of the evaluation of the entire
expression tree for $$(3 + (4 \times 5))$$ is 23.
"""
