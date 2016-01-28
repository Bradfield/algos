---
title: Introduction to Queues
layout: default.html
collection: queues
position: 1
---

A queue is an ordered collection of items where the addition of new
items happens at one end, called the “rear,” and the removal of existing
items occurs at the other end, commonly called the “front.” As an
element enters the queue it starts at the rear and makes its way toward
the front, waiting until that time when it is the next element to be
removed.

The most recently added item in the queue must wait at the end of the
collection. The item that has been in the collection the longest is at
the front. This ordering principle is sometimes called **FIFO**,
**first-in first-out**. It is also known as “first-come first-served.”

The simplest example of a queue is the typical line that we all
participate in from time to time. We wait in a line for a movie, we wait
in the check-out line at a grocery store, and we wait in the cafeteria
line (so that we can pop the tray stack). Well-behaved lines, or queues,
are very restrictive in that they have only one way in and only one way
out. There is no jumping in the middle and no leaving before you have
waited the necessary amount of time to get to the front.

![A queue of Python data objects](figures/basic-queue.png)

Queues are a very prevalent model for data flow in real life. Consider
an office with 30 computers networked with a single printer. When
somebody wants to print, their print tasks “get in line” with all the
other printing tasks that are waiting. The first task in is the next to
be completed. If you are last in line, you must wait for all the other
tasks to print ahead of you.

Operating systems also use a number of different queues to control
processes within a computer. The scheduling of what gets done next is
typically based on a queuing algorithm that tries to execute programs as
quickly as possible and serve as many users as it can. Also, as we type,
sometimes keystrokes get ahead of the characters that appear on the
screen. This is due to the computer doing other work at that moment. The
keystrokes are being placed in a queue-like buffer so that they can
eventually be displayed on the screen in the proper order.

The Queue Abstract Data Type
---

A queue is structured  as an ordered collection of items which are added
at one end, called the “rear,” and removed from the other end, called
the “front.” The queue operations are:

-   `Queue()` creates a new queue that is empty. It needs no parameters
    and returns an empty queue.
-   `enqueue(item)` adds a new item to the rear of the queue. It needs
    the item and returns nothing.
-   `dequeue()` removes the front item from the queue. It needs no
    parameters and returns the item. The queue is modified.
-   `is_empty()` tests to see whether the queue is empty. It needs no
    parameters and returns a boolean value.
-   `size()` returns the number of items in the queue. It needs no
    parameters and returns an integer.

As an example, if we assume that `q` is a queue that has been created
and is currently empty, then the table below shows
the results of a sequence of queue operations. The queue contents are
shown such that the front is on the right. 4 was the first item enqueued
so it is the first item returned by dequeue.

Queue Operation | Queue Contents | Return Value
--- | --- | ---
`q.is_empty()` | `[]` | `True`
`q.enqueue(4)` |    `[4]` |
`q.enqueue('dog')` |    `['dog', 4]` |
`q.enqueue(True)` | `[True, 'dog', 4]` |
`q.size()` |    `[True, 'dog', 4]` | `3`
`q.is_empty()` | `[True, 'dog', 4]` | `False`
`q.enqueue(8.4)` |  `[8.4, True, 'dog', 4]` |
`q.dequeue()` | `[8.4, True, 'dog']`  |  `4`
`q.dequeue()` | `[8.4, True]` | `'dog'`
`q.size()` |    `[8.4, True]` | `2`
