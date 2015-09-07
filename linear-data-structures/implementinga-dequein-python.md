Implementing a Deque in Python
==============================

As we have done in previous sections, we will create a new class for the
implementation of the abstract data type deque. Again, the Python list
will provide a very nice set of methods upon which to build the details
of the deque. Our implementation (Listing 1 &lt;lst\_dequecode&gt;) will
assume that the rear of the deque is at position 0 in the list.

**Listing 1**

    class Deque:
        def __init__(self):
            self.items = []

        def isEmpty(self):
            return self.items == []

        def addFront(self, item):
            self.items.append(item)

        def addRear(self, item):
            self.items.insert(0,item)

        def removeFront(self):
            return self.items.pop()

        def removeRear(self):
            return self.items.pop(0)

        def size(self):
            return len(self.items)

In `removeFront` we use the `pop` method to remove the last element from
the list. However, in `removeRear`, the `pop(0)` method must remove the
first element of the list. Likewise, we need to use the `insert` method
(line 12) in `addRear` since the `append` method assumes the addition of
a new element to the end of the list.

CodeLens 1 shows the `Deque` class in action as we perform the sequence
of operations from Table 1 &lt;tbl\_dequeoperations&gt;.

You can see many similarities to Python code already described for
stacks and queues. You are also likely to observe that in this
implementation adding and removing items from the front is O(1) whereas
adding and removing from the rear is O(n). This is to be expected given
the common operations that appear for adding and removing items. Again,
the important thing is to be certain that we know where the front and
rear are assigned in the implementation.
