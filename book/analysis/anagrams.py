# -*- coding: utf-8 -*-
"""
Solution 1: Checking Off
------------------------

Our first solution to the anagram problem will check whether each character in the first string occurs in the second. As we perform these checks, we’ll “check off” characters. If we can check off each character, then the two strings must be anagrams.

We can check off a character by replacing it with the special Python value `None`. Since strings in Python are immutable, we need to convert the second string to a list. Each character from the first string will be checked against the characters in this list and, if found, checked off by replacement.

An implementation of this strategy might look like this:
"""
def anagram_checking_off(s1, s2):
    if len(s1) != len(s2):
        return False

    to_check_off = list(s2)

    for char in s1:
        for i, other_char in enumerate(to_check_off):
            if char == other_char:
                to_check_off[i] = None
                break
        else:
            return False

    return True

anagram_checking_off('abcd', 'dcba')  # => True
anagram_checking_off('abcd', 'abcc')  # => False

"""
To analyze this algorithm, note that each of the $$n$$ characters in `s1` causes an iteration of up to $$n$$ characters in the list from `s2`. Each of the $$n$$ positions in the list will be visited once to match a character from `s1`.

So the number of visits becomes the sum of the integers from 1 to $$n$$. We recognized earlier that this can be written as

$$
\sum_{i=1}^{n} i = \frac {n(n+1)}{2} = \frac {1}{2}n^{2} + \frac {1}{2}n
$$

As $$n$$ gets larger, the $$n^{2}$$ term will dominate the $$n$$ term and the $$\frac {1}{2}$$ constant can be ignored. Therefore, this solution is $$O(n^{2})$$.

Solution 2: Sort and Compare
----------------------------

A second solution uses the fact that, even though `s1` and `s2` are different, they are only anagrams if they consist of the same characters. If the strings are anagrams, sorting them both alphabetically should produce the same string.

First, we use the Python builtin function `sorted` to return an iterable of sorted characters for each string. Then, we use `itertools.izip_longest` to iterate over the sorted characters of both strings until the end of the longer string.

Here is a possible implementation using this strategy:
"""
from itertools import izip_longest


def anagram_sort_and_compare(s1, s2):
    for a, b in izip_longest(sorted(s1), sorted(s2)):
        if a != b:
            return False
    return True

anagram_sort_and_compare('abcde', 'edcba')  # => True
anagram_sort_and_compare('abcde', 'abcd')  # => False

"""
At first glance, this algorithm seems like it’s $$O(n)$$, since there’s only one iteration to compare $$n$$ characters after sorting. However, the two `sorted` method calls have their own cost, typically $$O(n\log n)$$. Since that function dominates $$O(n)$$, this algorithm will also be $$O(n\log n)$$.

Solution 3: Brute Force
-----------------------

A *brute force* technique for solving a problem typically tries to exhaust all possibilities. We can apply this technique to the anagram problem by generating a list of all possible strings using the characters from `s1`. If `s2` occurs in that list, then `s1` and `s2` are anagrams.

There’s a problem with this approach, though: when generating all possible strings from `s1`, there are $$n$$ possible first characters, $$n-1$$ possible second characters, $$n-2$$ possible third characters, and so on. The total number of candidate strings is $$n*(n-1)*(n-2)*...*3*2*1$$, which is $$n!$$. Although some of the strings may be duplicates, the program won’t know that and will still generate $$n!$$ strings.

It turns out that $$n!$$ grows even faster than $$2^{n}$$ as *n* gets large. If `s1` were 20 characters long, there would be $$20!$$ or
2,432,902,008,176,640,000 possible candidate strings. If we processed one candidate every second, it would take 77,146,816,596 years to process the entire list. This is probably not going to be a good solution.

Solution 4: Count and Compare
-----------------------------

Our final solution uses the fact that any two anagrams have the same number of a’s, the same number of b’s, the same number of c’s, and so on. First, we generate character counts for each string. If these counts match, the two strings are anagrams.

Since there are 26 possible characters, we can use a list of 26 counters for each string. Each time we see a particular character, we’ll increment the counter at that character’s position. If the two lists are identical at the end, the strings must be anagrams.

Here is a possible implementation of this strategy:
"""
def anagram_count_compare(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for char in s1:
        pos = ord(char) - ord('a')
        c1[pos] += 1

    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] += 1

    for a, b in zip(c1, c2):
        if a != b:
            return False
    return True

anagram_count_compare('apple', 'pleap')  # => True
anagram_count_compare('apple', 'applf')  # => False

"""
Again, the solution has many iterations. However, unlike the first solution, none of them are nested. The first two iterations count characters and are $$O(n)$$. The third iteration always takes 26 steps since there are 26 possible characters. Adding everything gives $$T(n)=2n+26$$ steps, which is $$O(n)$$. We have found a linear order of magnitude algorithm for solving this problem.

This implementation could be written more succinctly by using `collections.Counter`, which constructs a `dict`-like object mapping elements in an iterable to the number of occurrences of that element in the iterable. Behold:
"""
from collections import Counter


def anagram_with_counter(s1, s2):
    return Counter(s1) == Counter(s2)

anagram_with_counter('apple', 'pleap')  # => True
anagram_with_counter('apple', 'applf')  # => False

"""
Note that `anagram_with_counter` is also $$O(n)$$, but we only know this because we understand the implementation of `collections.Counter`.

One final thought about space requirements: although the last solution was able to run in linear time, it only did so by using additional storage for the two lists of character counts. In other words, this algorithm sacrificed space in order to gain time.

This is a common tradeoff. In this case, the amount of extra space isn’t significant; however, if the underlying alphabet had millions of characters, there would be more cause for concern.

On many occasions, you’ll need to choose between time and space. When given a choice of algorithms, it’s up to you as a software engineer to determine the best use of computing resources for a given problem.
"""
