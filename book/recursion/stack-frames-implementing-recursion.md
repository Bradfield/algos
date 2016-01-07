---
title: Stack Frames: Implementing Recursion
layout: default.html
collection: recursion
position: 5
---

Suppose that instead of concatenating the result of the recursive call
to `to_string` with the string from `CHAR_FROM_INT`, we modified our
algorithm to push the strings onto a stack prior to making the recursive
call. The code for this modified algorithm might look like:

```python
CHAR_FROM_INT = '0123456789ABCDEF'

def to_string(n,base):
    stack = []
    while n > 0:
        if n < base:
            stack.append(CHAR_FROM_INT[n])
        else:
            stack.append(CHAR_FROM_INT[n % base])
        n = n // base
    result = ''
    while stack:
        result = result + stack.pop()
    return result

to_string(1453,16)  # => 5AD
```

Each time we make a call to `to_string`, we push a character on the stack.
Returning to the previous example we can see that after the fourth call
to `to_string` the stack would look the diagram below.
Notice that now we can simply pop the characters off the stack and
concatenate them into the final result, `'1010'`.

![Strings placed on the stack during
conversion](figures/recursion-stack.png)

The previous example gives us some insight into how Python implements a
recursive function call. When a function is called in Python, a **stack
frame** is allocated to handle the local variables of the function. When
the function returns, the return value is left on top of the stack for
the calling function to access. The diagram below
illustrates the call stack after the return statement.

![Call stack generated from
to_string(10, 2)](figures/new-call-stack.png)

Notice that the call to `to_string(2 // 2, 2)` leaves a return value of `'1'`
on the stack. This return value is then used in place of the function
call (`to_string(1,2)`) in the expression `'1' + CHAR_FROM_INT[2 % 2]`, which
will leave the string `'10'` on the top of the stack. In this way, the
Python call stack takes the place of the stack we used explicitly in our algorithm above. In our list summing example, you can
think of the return value on the stack taking the place of an
accumulator variable.

The stack frames also provide a scope for the variables used by the
function. Even though we are calling the same function over and over,
each call creates a new scope for the variables that are local to the
function.
