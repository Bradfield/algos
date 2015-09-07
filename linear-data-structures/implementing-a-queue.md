Implementing a Queue in Python
==============================

It is again appropriate to create a new class for the implementation of
the abstract data type queue. As before, we will use the power and
simplicity of the list collection to build the internal representation
of the queue.

We need to decide which end of the list to use as the rear and which to
use as the front. The implementation shown in
Listing 1 &lt;lst\_queuecode&gt; assumes that the rear is at position 0
in the list. This allows us to use the `insert` function on lists to add
new elements to the rear of the queue. The `pop` operation can be used
to remove the front element (the last element of the list). Recall that
this also means that enqueue will be O(n) and dequeue will be O(1).

**Listing 1**

    class Queue:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def enqueue(self, item):
            self.items.insert(0,item)

        def dequeue(self):
            return self.items.pop()

        def size(self):
            return len(self.items)

CodeLens 1 shows the `Queue` class in action as we perform the sequence
of operations from Table 1 &lt;tbl\_queueoperations&gt;.

Further manipulation of this queue would give the following results:

    >>> q.size()
    3
    >>> q.isEmpty()
    False
    >>> q.enqueue(8.4)
    >>> q.dequeue()
    4
    >>> q.dequeue()
    'dog'
    >>> q.size()
    2

> **Self Check**
