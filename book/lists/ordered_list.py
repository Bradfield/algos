from unordered_list import Node, UnorderedList


class OrderedList(UnorderedList):
    """

As we consider the operations for the ordered list, we should note that
the `is_empty` and `size` methods can be implemented the same as with
unordered lists since they deal only with the number of nodes in the
list without regard to the actual item values. Likewise, the `remove`
method will work just fine since we still need to find the item and then
link around the node to remove it. The two remaining methods, `search`
and `add`, will require some modification.

The search of an unordered linked list required that we traverse the
nodes one at a time until we either find the item we are looking for or
run out of nodes (`None`). It turns out that the same approach would
actually work with the ordered list and in fact in the case where we
find the item it is exactly what we need. However, in the case where the
item is not in the list, we can take advantage of the ordering to stop
the search as soon as possible.

For example, the diagram below shows the ordered linked
list as a search is looking for the value 45. As we traverse, starting
at the head of the list, we first compare against 17. Since 17 is not
the item we are looking for, we move to the next node, in this case 26.
Again, this is not what we want, so we move on to 31 and then on to 54.
Now, at this point, something is different. Since 54 is not the item we
are looking for, our former strategy would be to move forward. However,
due to the fact that this is an ordered list, that will not be
necessary. Once the value in the node becomes greater than the item we
are searching for, the search can stop and return `False`. There is no
way the item could exist further out in the linked list.

![Searching an ordered linked
list](figures/ordered-list-search.png)

Below we provide an adaptation of the `search` method from our `UnorderedList`
class to take advantage of this optimization.

"""
    def search(self, item):
        current = self.head

        while current is not None:
            if current.value == item:
                return True
            if current.value > item:
                return False
            current = current.next

        return False
    """
The most significant method modification will take place in `add`.
Recall that for unordered lists, the `add` method could simply place a
new node at the head of the list. It was the easiest point of access.
Unfortunately, this will no longer work with ordered lists. It is now
necessary that we discover the specific place where a new item belongs
in the existing ordered list.

Assume we have the ordered list consisting of 17, 26, 54, 77, and 93 and
we want to add the value 31. The `add` method must decide that the new
item belongs between 26 and 54. Below we show
the setup that we need. As we explained earlier, we need to traverse the
linked list looking for the place where the new node will be added. We
know we have found that place when either we run out of nodes (`current`
becomes `None`) or the value of the current node becomes greater than
the item we wish to add. In our example, seeing the value 54 causes us
to stop.

![Adding an item to an ordered linked
list](figures/ordered-list-insert.png)

As we saw with unordered lists, it is necessary to have an additional
reference, again called `previous`, since `current` will not provide
access to the node that must be modified.

Once we have identified the position at which to add our new node, we
construct it and place it correctly, either as the new head of the node (if
`previous` is `None`) or between `previous` and `current` otherwise.

"""
    def add(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.value > item:
                break
            previous, current = current, current.next

        temp = Node(item)
        if previous is None:
            temp.next, self.head = self.head, temp
        else:
            temp.next, previous.next = current, temp
"""
We leave the remaining methods as exercises. You should
carefully consider whether the unordered implementations will work given
that the list is now ordered.
"""
