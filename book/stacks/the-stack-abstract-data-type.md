---
title: The Stack Abstract Data Type
layout: chapter.html
collection: stacks
position: 2
---

An *abstract data type*, sometimes abbreviated *ADT*, is a logical
description of how we view the data and the operations that are allowed
without regard to how they will be implemented. This means that we are
concerned only with what the data is representing and not with how it
will eventually be constructed. By providing this level of abstraction,
we are creating an *encapsulation* around the data. The idea is that by
encapsulating the details of the implementation, we are hiding them from
the user’s view. This is called *information hiding*.

The implementation of an abstract data type, often referred to as a
*data structure*, will require that we provide a physical view of the
data using some collection of programming constructs and primitive data
types. The separation of these two perspectives will allow us to define
the complex data models for our problems without giving any indication
as to the details of how the model will actually be built. This provides
an *implementation-independent* view of the data. Since there will
usually be many different ways to implement an abstract data type, this
implementation independence allows the programmer to switch the details
of the implementation without changing the way the user of the data
interacts with it. The user can remain focused on the problem-solving
process.

The stack abstract data type is an ordered collection of items where
items are added to and removed from the end called the “top.” The
interface for a stack is:

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
