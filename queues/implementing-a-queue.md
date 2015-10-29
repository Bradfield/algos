Implementing a Queue in Python
==============================

Just like with a stack, it is possible to “use a Python list as a queue”. Again, for the purpose of illustrating the narrow set of behaviors that define the queue abstract data type, we define a `Queue` class to expose only the desired the functionality of an internal list.

_Unlike_ with a stack, the performance implication of using a Python list as a queue is significant. The implementation shown below uses `insert(0, item)` to enqueue a new item, which will be an $$O(n)$$ operation.

```python

class Queue(object):
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)
```

In practice, many Python programmers will use the standard library’s `collections.deque` class to achieve $$O(1)$$ enqueues and dequeues. We will cover deques in depth in the next chapter; for now consider deques to be a combination of a stack and a queue, enabling $$O(1)$$ pushing and popping from both ends.
