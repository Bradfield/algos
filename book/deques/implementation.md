---
title: A Deque Implementation
layout: default.html
collection: deques
position: 3
---

In practice, the most straightforward way to utilize a deque in Python will be to import `deque` from the `collections` module. For illustration purposes however, below we present a possible implementation of a deque using a Python list as the underlying concrete data type.

```python
class Deque(object):
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0,item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)
```

In `remove_front` we use the `pop` method to remove the last element from
the list. However, in `remove_rear`, the `pop(0)` method must remove the
first element of the list. Likewise, we need to use the `insert` method
in `add_rear` since the `append` method assumes the addition of
a new element to the end of the list.

You can see many similarities to Python code already described for
stacks and queues. You are also likely to observe that in this
implementation adding and removing items from the front is $$O(1)$$ whereas
adding and removing from the rear is $$O(n)$$. This is to be expected given
the common operations that appear for adding and removing items. Again,
the important thing is to be certain that we know where the front and
rear are assigned in the implementation.
