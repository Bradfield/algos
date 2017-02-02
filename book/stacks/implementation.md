---
title: A Stack Implementation
layout: default.html
collection: stacks
position: 3
---

Now that we’ve clearly defined the stack as an abstract data type we’ll turn our attention to using Python to implement the stack. Recall that when we give an abstract data type a physical implementation we refer to the implementation as a data structure.

You may be wondering if a Python `list` “is” a stack. It’s more precise to say that a Python `list` “may be used as a” stack. That is to say, the implementation of `list` in Python provides methods that allow us to achieve the behavior of the stack abstract data type, for instance `.append()` allows us to push items to our stack.

In practice “use a Python list as a stack” is precisely what you’re likely to do, in other words you will define something like: `pancake_stack = []` then diligently use only the `append` and `pop` methods as well as `len(pancake_stack)` for the size, and `pancake_stack[-1]` to peek. Of course, a Python `list` permits much more than the behavior of a stack, notably accessing an item by index, and inserting and deleting items at any point by index.

As such, we ought to communicate as clearly as possible our intention to use this (concrete) data structure of a `list` as an abstract data type stack. Sometimes we can achieve this simply by naming it a stack. Other times, we may want to use a class to abstract away the implementation of the stack as a list, and only provide the behaviors that we require of a stack.

Such an abstraction is also illustrative of the distinction between concrete data structures and abstract data types, so we provide a possible implementation of a stack class here:

<!-- literate stacks/stack_right.py -->

It’s important to note that we could’ve chosen to implement the stack using a list where the top is at the beginning instead of at the end. In this case, instead of using `pop` and `append` as above, instead we’d pop from and insert into position 0 in the list. Here’s a possible implementation of that approach:

<!-- literate stacks/stack_left.py -->

This ability to change the physical implementation of an abstract data type while maintaining the logical characteristics is an example of abstraction at work. However, even though the stack will work either way, if we consider the performance of the two implementations, there’s definitely a difference. Recall that the `append` and `pop()` operations were both $$O(1)$$. This means that the first implementation will perform push and pop in constant time no matter how many items are on the stack. The performance of the second implementation suffers in that the `insert(0)` and `pop(0)` operations will both require $$O(n)$$ for a stack of size n. Clearly, even though the implementations are logically equivalent, they would have very different timings when performing benchmark testing.

Going forward, we’ll simply use Python `list`s directly as stacks, being careful to only use the stack-like behavior of the `list`.
