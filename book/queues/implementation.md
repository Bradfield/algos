---
title: A Queue Implementation
layout: default.html
collection: queues
position: 3
---

Just like with a stack, it is possible to “use a Python list as a queue”. Again, for the purpose of illustrating the narrow set of behaviors that define the queue abstract data type, we define a `Queue` class to expose only the desired the functionality of an internal list.

_Unlike_ with a stack, the performance implication of using a Python list as a queue is significant. The implementation shown below uses `insert(0, item)` to enqueue a new item, which will be an $$O(n)$$ operation.

<!-- literate queues/queue.py -->

In practice, many Python programmers will use the standard library’s `collections.deque` class to achieve $$O(1)$$ enqueues and dequeues. We will cover deques in depth in the next chapter; for now consider deques to be a combination of a stack and a queue, enabling $$O(1)$$ pushing and popping from both ends.
