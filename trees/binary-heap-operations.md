Binary Heap Operations
======================

The basic operations we will implement for our binary heap are as
follows:

-   `BinaryHeap()` creates a new, empty, binary heap.
-   `insert(k)` adds a new item to the heap.
-   `findMin()` returns the item with the minimum key value, leaving
    item in the heap.
-   `delMin()` returns the item with the minimum key value, removing the
    item from the heap.
-   `isEmpty()` returns true if the heap is empty, false otherwise.
-   `size()` returns the number of items in the heap.
-   `buildHeap(list)` builds a new heap from a list of keys.

ActiveCode 1 &lt;lst\_heap1&gt; demonstrates the use of some of the
binary heap methods. Notice that no matter the order that we add items
to the heap, the smallest is removed each time. We will now turn our
attention to creating an implementation for this idea.
