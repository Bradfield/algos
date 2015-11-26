# -*- coding: utf-8 -*-
"""
Solution 1: Checking Off
------------------------

Our first solution to the anagram problem will check to see that each
character in the first string actually occurs in the second. If it is
possible to “checkoff” each character, then the two strings must be
anagrams. Checking off a character will be accomplished by replacing it
with the special Python value `None`. However, since strings in Python
are immutable, the first step in the process will be to convert the
second string to a list. Each character from the first string can be
checked against the characters in the list and if found, checked off by
replacement. An implementation of this strategy may look like this:
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
To analyze this algorithm, we need to note that each of the `n`
characters in `s1` will cause an iteration through up to `n` characters
in the list from `s2`. Each of the `n` positions in the list will be
visited once to match a character from `s1`. The number of visits then
becomes the sum of the integers from 1 to `n`. We recognized earlier that
this can be written as

$$
\sum_{i=1}^{n} i = \frac {n(n+1)}{2}
$$

$$
                 = \frac {1}{2}n^{2} + \frac {1}{2}n
$$

As $$n$$ gets large, the $$n^{2}$$ term will dominate the $$n$$ term and the
$$\frac {1}{2}$$ can be ignored. Therefore, this solution is $$O(n^{2})$$.

Solution 2: Sort and Compare
----------------------------

Another solution to the anagram problem will make use of the fact that
even though `s1` and `s2` are different, they are anagrams only if they
consist of exactly the same characters. So, if we begin by sorting each
string alphabetically, from a to z, we will end up with the same string
if the original two strings are anagrams. Below is a possible
implementation of this strategy. We use the Python builtin function
`sorted` to return an iterable of the sorted characters in each string,
and `itertools.izip_longest` to iterate over one character from each of
the sorted strings at a time, all the way through to the end of the
longer string.
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
At first glance you may be tempted to think that this algorithm is
$$O(n)$$, since there is one simple iteration to compare the *n*
characters after the sorting process. However, the two calls to the
Python `sorted` method are not without their own cost. Sorting is
typically either $$O(n^{2})$$ or $$O(n\log n)$$, so the sorting
operations dominate the iteration. In the end, this algorithm will have
the same order of magnitude as that of the sorting process.

Solution 3: Brute Force
-----------------------

A *brute force* technique for solving a problem typically tries to
exhaust all possibilities. For the anagram detection problem, we can
simply generate a list of all possible strings using the characters from
`s1` and then see if `s2` occurs. However, there is a difficulty with
this approach. When generating all possible strings from `s1`, there are
$$n$$ possible first characters, $$n-1$$ possible characters for the second
position, $$n-2$$ for the third, and so on. The total number of candidate
strings is $$n*(n-1)*(n-2)*...*3*2*1$$, which is $$n!$$. Although some of
the strings may be duplicates, the program cannot know this ahead of
time and so it will still generate $$n!$$ different strings.

It turns out that $$n!$$ grows even faster than $$2^{n}$$ as *n* gets large.
In fact, if `s1` were 20 characters long, there would be
$$20!$$ or 2,432,902,008,176,640,000 possible candidate strings. If we
processed one possibility every second, it would still take us
77,146,816,596 years to go through the entire list. This is probably not
going to be a good solution.

Solution 4: Count and Compare
-----------------------------

Our final solution to the anagram problem takes advantage of the fact
that any two anagrams will have the same number of a’s, the same number
of b’s, the same number of c’s, and so on. In order to decide whether
two strings are anagrams, we will first count the number of times each
character occurs. Since there are 26 possible characters, we can use a
list of 26 counters, one for each possible character. Each time we see a
particular character, we will increment the counter at that position. In
the end, if the two lists of counters are identical, the strings must be
anagrams. Here is a possible implementation of the strategy:

"""


def anagram_count_compare(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for char in s1:
        pos = ord(char) - ord('a')
        c1[pos] = c1[pos] + 1

    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] = c2[pos] + 1

    for a, b in zip(c1, c2):
        if a != b:
            return False
    return True

anagram_count_compare('apple', 'pleap')  # => True
anagram_count_compare('apple', 'applf')  # => False

"""

Again, the solution has a number of iterations. However, unlike the
first solution, none of them are nested. The first two iterations used
to count the characters are both based on $$n$$. The third iteration,
comparing the two lists of counts, always takes 26 steps since there are
26 possible characters in the strings. Adding it all up gives us
$$T(n)=2n+26$$ steps. That is $$O(n)$$. We have found a linear order of
magnitude algorithm for solving this problem.

Those with greater familiarity with Python may note that the counting
strategy we implemented in `anagram_count_compare` could be much more
succinctly approached using `collections.Counter`, which constructs a
`dict`-like object mapping elements in an iterable to the number of
occurences of that element in a that iterable. In fact, the
implementation becomes _very_ succinct:
"""
from collections import Counter


def anagram_with_counter(s1, s2):
    return Counter(s1) == Counter(s2)

anagram_with_counter('apple', 'pleap')  # => True
anagram_with_counter('apple', 'applf')  # => False

"""

It is worth noting that `anagram_with_counter` is also $$O(n)$$, but
that it is impossible to determine this without understanding the
implementation of `collections.Counter`.

Before leaving this example, we need to say something about space
requirements. Although the last solution was able to run in linear time,
it could only do so by using additional storage to keep the two lists of
character counts. In other words, this algorithm sacrificed space in
order to gain time.

This is a common tradeoff. On many occasions you will need to make
decisions between time and space trade-offs. In this case, the amount of
extra space is not significant. However, if the underlying alphabet had
millions of characters, there would be more concern. As a software
engineer, when given a choice of algorithms, it will be up to you to
determine the best use of computing resources given a particular
problem.
"""
