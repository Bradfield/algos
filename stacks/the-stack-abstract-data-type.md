The Stack Abstract Data Type
============================

The stack abstract data type is an ordered collection of items where items are added to and removed from the end called the “top.” Stacks are ordered LIFO. The interface for a stack is:

-   `Stack()` creates a new stack that is empty
-   `push(item)` adds the given item to the top of the stack and returns nothing
-   `pop()` removes the top item from the stack and returns it
-   `peek()` returns the top item from the stack but does not remove it (the stack is not modified)
-   `is_empty()` tests to see whether the stack is empty and returns a boolean
-   `size()` returns the number of items on the stack as an integer

For example, if `s` is a stack that has been created and starts out
empty, then the below table shows the results of a
sequence of stack operations. Under stack contents, the top item is
listed at the far right.


Stack operation | Stack contents | Return value
--- | --- | ---
`s.is_empty()` | `[]` | `True`
`s.push(4)` | `[4]` |
`s.push('dog')` | `[4, 'dog']` |
`s.peek()` | `[4, 'dog']` | `'dog'`
`s.push(True)` | `[4, 'dog', True]` |
`s.size()` | `[4, 'dog', True]` | `3`
`s.is_empty()` | `[4, 'dog', True]` | `False`
`s.push(8.4)` | `[4, 'dog', True, 8.4]` |
`s.pop()` | `[4, 'dog', True]` | `8.4`
`s.pop()` | `[4, 'dog']` | `True`
`s.size()` | `[4, 'dog']` | `2`
