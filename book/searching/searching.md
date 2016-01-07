---
title: Searching
layout: default.html
collection: searching
position: 1
---

In this section we will study searching. Searching is the algorithmic process of finding a particular item in a collection of items. A search typically answers either `True` or `False` as to whether the item is present. On occasion it may be modified to return where the item is found. For our purposes here, we will simply concern ourselves with the question of membership.

In Python, there is a very easy way to ask whether an item is in a list of items. We use the `in` operator.

```python
>>> 15 in [3, 5, 2, 4, 1]
False
>>> 3 in [3, 5, 2, 4, 1]
True
```

Given the ease of _conducting_ a search in Python, you may wonder what the purpose is of studying search as an algorithms problem. The answer is that the underlying process used to enable a search is important to understand as it arises elsewhere, such as in data structures designed for fast search, and particular in databases.

It turns out that there are many different ways to search for an item in a collection. We focus here on the difference between two such ways—sequential search and binary search.
