---
title: The Map Abstract Data Type
layout: default.html
collection: searching
position: 5
--

One of the most useful Python collections is the dictionary. Recall that
a dictionary is an associative data type where you can store key–data
pairs. The key is used to look up the associated data value. We often
refer to this idea as a **map**.

In this section, we effectively re-implement a simplified version of the the Python `dict` type to illustrate the hashing concepts we have been exploring.

The map abstract data type is defined as follows. The structure is an
unordered collection of associations between a key and a data value. The
keys in a map are all unique so that there is a one-to-one relationship
between a key and a value. The operations are given below.

-   `Map()` Create a new, empty map. It returns an empty map collection.
-   `put(key, val)` Add a new key-value pair to the map. If the key is
    already in the map then replace the old value with the new value.
-   `get(key)` Given a key, return the value stored in the map or
    `None` otherwise.
-   `del` Delete the key-value pair from the map using a statement of
    the form `del map[key]`.
-   `len()` Return the number of key-value pairs stored in the map.
-   `in` Return `True` for a statement of the form `key in map`, if the
    given key is in the map, `False` otherwise.

One of the great benefits of a dictionary is the fact that given a key,
we can look up the associated data value very quickly. In order to
provide this fast look up capability, we need an implementation that
supports an efficient search. We could use a list with sequential or
binary search but it would be even better to use a hash table as
described above since looking up an item in a hash table can approach
$$O(1)$$ performance.

Below we use two lists to
create a `HashTable` class that implements the Map abstract data type.
One list, called `slots`, will hold the key items and a parallel list,
called `data`, will hold the data values. When we look up a key, the
corresponding position in the data list will hold the associated data
value. We will treat the key list as a hash table using the ideas
presented earlier. Note that the initial size for the hash table has
been chosen to be 11. Although this is arbitrary, it is important that
the size be a prime number so that the collision resolution algorithm
can be as efficient as possible.

```python
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
```

`self.hash` implements the simple remainder method. The collision
resolution technique is linear probing with a “plus 1” rehash method.
The `put` method
assumes that there will eventually be an empty slot unless the key is
already present in the `self.slots`. It computes the original hash value
and if that slot is not empty, iterates the `rehash` method until an
empty slot occurs. If a nonempty slot already contains the key, the old
data value is replaced with the new data value.

```python

def put(self,key,data):
    hash_value = self.hash(key, len(self.slots))

    if self.slots[hash_value] is None:  # empty, so just set
        self.slots[hash_value] = key
        self.data[hash_value] = data
        return

    if self.slots[hash_value] == key:  # matches key, so just replace
        self.data[hash_value] = data
        return

    # otherwise, reshash until empty or matches key
    next_slot = self.rehash(hash_value, len(self.slots))
    while self.slots[next_slot] not in (None, key):
        next_slot = self.rehash(next_slot, len(self.slots))

    if self.slots[next_slot] == None:
        self.slots[next_slot] = key
        self.data[next_slot] = data
    else:
        self.data[next_slot] = data

def hash(self, key, size):
    return key % size

def rehash(self, oldhash, size):
    return (oldhash + 1) % size
```

Likewise, the `get` function (below) begins by computing the
initial hash value. If the value is not in the initial slot, `rehash` is
used to locate the next possible position. Notice we
guarantee that the search will terminate by checking to make sure that
we have not returned to the initial slot. If that happens, we have
exhausted all possible slots and the item must not be present.

The final methods of the `HashTable` class provide additional dictionary
functionality. We overload the \_\_getitem\_\_ and \_\_setitem\_\_
methods to allow access using`[]`. This means that once a `HashTable`
has been created, the familiar index operator will be available. We
leave the remaining methods as exercises.


```python
def get(self,key):
    starting_slot = self.hash(key, len(self.slots))

    position = starting_slot
    while self.slots[position] is not None:
        if self.slots[position] == key:
            return self.data[position]
        position = self.rehash(position, len(self.slots))
        if position == starting_slot:
            return None
    return None

def __getitem__(self, key):
    return self.get(key)

def __setitem__(self, key, data):
    self.put(key, data)
```

The following session shows the `HashTable` class in action. First we
will create a hash table and store some items with integer keys and
string data values.

```python
>>> H = HashTable()
>>> H[54] = 'cat'
>>> H[26] = 'dog'
>>> H[93] = 'lion'
>>> H[17] = 'tiger'
>>> H[77] = 'bird'
>>> H[31] = 'cow'
>>> H[44] = 'goat'
>>> H[55] = 'pig'
>>> H[20] = 'chicken'
>>> H.slots
[77, 44, 55, 20, 26, 93, 17, None, None, 31, 54]
>>> H.data
['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
```

Next we will access and modify some items in the hash table. Note that
the value for the key 20 is being replaced.

```python
>>> H[20]
'chicken'
>>> H[17]
'tiger'
>>> H[20] = 'duck'
>>> H[20]
'duck'
>>> H.data
['bird', 'goat', 'pig', 'duck', 'dog', 'lion', 'tiger', None, None, 'cow', 'cat']
>> H[99]
None
```
