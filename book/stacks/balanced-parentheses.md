---
title: Balanced Parentheses
layout: default.html
collection: stacks
position: 4
---

We now turn our attention to using stacks to solve real computer science problems. You’ve no doubt written arithmetic expressions such as

$$(5+6)\times(7+8)/(4+3)$$

where parentheses are used to order the performance of operations. You may also have some experience programming in a language such as Lisp with constructs like

```lisp
(defun square(n)
     (* n n))
```

This defines a function called `square` that will return the square of its argument `n`. Lisp is notorious for using lots and lots of parentheses.

In both of these examples, parentheses must appear in a balanced fashion. *Balanced parentheses* means that each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested. Consider the following correctly balanced strings of parentheses:

    (()()()())

    (((())))

    (()((())()))

Compare those with the following, which aren’t balanced:

    ((((((())

    ()))

    (()()(()

The ability to differentiate between parentheses that are correctly balanced and those that are unbalanced is an important part of recognizing many programming language structures.

The challenge then is to write an algorithm that will read a string of parentheses from left to right and decide whether the symbols are balanced. To solve this problem we need to make an important observation. As you process symbols from left to right, the most recent opening parenthesis must match the next closing symbol. Also, the first opening symbol processed may have to wait until the very last symbol for its match. Closing symbols match opening symbols in the reverse order of their appearance; they match from the inside out. This is a clue that stacks can be used to solve the problem.

![Matching parentheses](figures/simple-parity-check.png)

Once you agree that a stack is the appropriate data structure for keeping the parentheses, the statement of the algorithm is straightforward. Starting with an empty stack, process the parenthesis strings from left to right. If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. If, on the other hand, a symbol is a closing parenthesis, pop the stack. As long as it’s possible to pop the stack to match every closing symbol, the parentheses remain balanced. If at any time there’s no opening symbol on the stack to match a closing symbol, the string is not balanced properly. At the end of the string, when all symbols have been processed, the stack should be empty. The Python code to implement this algorithm may look like this:

<!-- literate stacks/balanced_parentheses.py -->

This function, `is_balanced`, returns a boolean result as to whether the string of parentheses is balanced. If the current symbol is `(`, then it’s pushed on the stack. If it is `)` we attempt to pop from the stack. If the stack is empty at that point, we know that the parenthesis string is imbalanced with too many closing parens. Finally, as long as the expression is balanced and the stack has been completely cleaned off, the string represents a correctly balanced sequence of parentheses.

Balanced Symbols: A General Case
---

The balanced parentheses problem shown above is a specific case of a more general situation that arises in many programming languages. The general problem of balancing and nesting different kinds of opening and closing symbols occurs frequently. For example, in Python square brackets, `[` and `]`, are used for lists; curly braces, `{` and `}`, are used for dictionaries; and parentheses, `(` and `)`, are used for tuples and arithmetic expressions. It’s possible to mix symbols as long as each maintains its own open and close relationship. Strings of symbols such as

    { { ( [ ] [ ] ) } ( ) }

    [ [ { { ( ( ) ) } } ] ]

    [ ] [ ] [ ] ( ) { }

are properly balanced in that not only does each opening symbol have a corresponding closing symbol, but the types of symbols match as well.

Compare those with the following strings that are not balanced:

    ( [ ) ]

    ( ( ( ) ] ) )

    [ { ( ) ]

The simple parentheses checker from the previous section can easily be extended to handle these new types of symbols. Recall that each opening symbol is simply pushed on the stack to wait for the matching closing symbol to appear later in the sequence. When a closing symbol does appear, the only difference is that we must check to be sure that it correctly matches the type of the opening symbol on top of the stack. If the two symbols don’t match, the string isn’t balanced. Once again, if the entire string is processed and nothing is left on the stack, the string is correctly balanced.

The Python program to implement this is shown below. The only change is that we use a dictionary to ensure that symbols popped from the stack correctly match our expectations of pairing with the symbol being considered at the time.

<!-- literate stacks/balanced_symbols.py -->

These two examples show that stacks are very important data structures for the processing of language constructs in computer science. Almost any notation you can think of has some type of nested symbol that must be matched in a balanced order. There are a number of other important uses for stacks in computer science. We’ll continue to explore them in the next sections.
