"""
Now that we have clearly defined the stack as an abstract data type we
will turn our attention to using Python to implement the stack. Recall
that when we give an abstract data type a physical implementation we
refer to the implementation as a data structure.

You may be wondering if a Python `list` “is” a stack. It is more precise
to say that a Python `list` “may be used as a” stack. That is to say,
the implementation of `list` in Python provides methods that allow us to
achieve the behavior of the stack abstract data type, for instance
`.append()` allows us to push items to our stack.

In practice “use a Python list as a stack” is precisely what you are
likely to do, in other words you will define something like:
`pancake_stack = []` then diligently use only the `append` and `pop`
methods as well as `len(pancake_stack)` for the size, and
`pancake_stack[-1]` to peek. Of course, a Python `list` permits much
more than the behavior of a stack, notably accessing an item by index,
and inserting and deleting items at any point by index.

As such, we ought to communicate as clearly as possible our intention to
use this (concrete) data structure of a `list` as an abstract data type
stack. Sometimes we can achieve this simply by naming it a stack. Other
times, we may want to use a class to abstract away the implementation of
the stack as a list, and only provide the behaviors that we require of a
stack.

Such an abstraction is also illustrative of the distinction between
concrete data structures and abstract data types, so we provide a
possible implementation of a stack class here:
"""

class Stack(object):

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)
