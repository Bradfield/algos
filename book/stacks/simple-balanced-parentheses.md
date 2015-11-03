---
title: Simple Balanced Parentheses
layout: chapter.html
collection: stacks
position: 4
---

We now turn our attention to using stacks to solve real computer science
problems. You have no doubt written arithmetic expressions such as

$$(5+6)*(7+8)/(4+3)$$

where parentheses are used to order the performance of operations. You
may also have some experience programming in a language such as Lisp
with constructs like

```lisp
(defun square(n)
     (* n n))
```

This defines a function called `square` that will return the square of
its argument `n`. Lisp is notorious for using lots and lots of
parentheses.

In both of these examples, parentheses must appear in a balanced
fashion. *Balanced parentheses* means that each opening symbol has a
corresponding closing symbol and the pairs of parentheses are properly
nested. Consider the following correctly balanced strings of
parentheses:

    (()()()())

    (((())))

    (()((())()))

Compare those with the following, which are not balanced:

    ((((((())

    ()))

    (()()(()

The ability to differentiate between parentheses that are correctly
balanced and those that are unbalanced is an important part of
recognizing many programming language structures.

The challenge then is to write an algorithm that will read a string of
parentheses from left to right and decide whether the symbols are
balanced. To solve this problem we need to make an important
observation. As you process symbols from left to right, the most recent
opening parenthesis must match the next closing symbol. Also, the first opening symbol
processed may have to wait until the very last symbol for its match.
Closing symbols match opening symbols in the reverse order of their
appearance; they match from the inside out. This is a clue that stacks
can be used to solve the problem.

![Matching Parentheses](figures/simple-parity-check.png)

Once you agree that a stack is the appropriate data structure for
keeping the parentheses, the statement of the algorithm is
straightforward. Starting with an empty stack, process the parenthesis
strings from left to right. If a symbol is an opening parenthesis, push
it on the stack as a signal that a corresponding closing symbol needs to
appear later. If, on the other hand, a symbol is a closing parenthesis,
pop the stack. As long as it is possible to pop the stack to match every
closing symbol, the parentheses remain balanced. If at any time there is
no opening symbol on the stack to match a closing symbol, the string is
not balanced properly. At the end of the string, when all symbols have
been processed, the stack should be empty. The Python code to implement
this algorithm may look like this:

```python
OPENING = '('

def is_balanced(parentheses):
    stack = []
    for paren in parentheses:
        if paren == OPENING:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError:  # too many closing parens
                return False
    return len(stack) == 0  # false if too many opening parens

is_balanced('((()))')  # => True
is_balanced('(()')  # => False
is_balanced('())')  # => False
```

This function, `is_balanced`, returns a boolean result as to whether the string of parentheses is
balanced. If the
current symbol is `(`, then it is pushed on the stack. If it is `)` we attempt to pop from the stack. If the stack is empty at that point, we know that the parenthesis string is inbalanced with too many closing parens. Finally, as long as the expression is balanced and the stack has been completely cleaned off, the string
represents a correctly balanced sequence of parentheses.
