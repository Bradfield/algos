# -*- coding: utf-8 -*-
"""
Solution 1: Checking Off
------------------------

Our first solution to the anagram problem will check to see that each character
in the first string occurs in the second. If it is possible to "check off" each
character, then the two strings must be anagrams.

We can check off a character by replacing it with the special Python value
`None`. Since strings in Python are immutable, we need to convert the second
second string to a list. Each character from the first string will be checked
against the characters in this list and, if found, checked off by replacement.

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
To analyze this algorithm, note that each of the `n` characters in `s1` causes
an iteration of up to `n` characters in the list from `s2`. Each of the `n`
positions in the list will be visited once to match a character from `s1`.

So the number of visits becomes the sum of the integers from 1 to `n`. We
recognized earlier that this can be written as

$$
\sum_{i=1}^{n} i = \frac {n(n+1)}{2}
$$

$$
                 = \frac {1}{2}n^{2} + \frac {1}{2}n
$$

As $$n$$ gets larger, the $$n^{2}$$ term will dominate the $$n$$ term and the
$$\frac {1}{2}$$ constant can be ignored. Therefore, this solution is
$$O(n^{2})$$.

Solution 2: Sort and Compare
----------------------------

A second solution uses the fact that, even though `s1` and `s2` are different,
they are only anagrams if they consist of the same characters. If the strings
are anagrams, sorting them both alphabetically should produce the same string.

Below is a possible implementation using this strategy. We use the Python
builtin function `sorted` to return an iterable of the sorted characters for
each string, and `itertools.izip_longest` to iterate these sorted iterables
at the same time until the end of the longer string.
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
At first glance, you may be tempted to think that this algorithm is $$O(n)$$,
since there is only one iteration to compare `n` characters after sorting.
However, the two `sorted` method calls have their own costs: sorting is
typically either $$O(n^{2})$$ or $$O(n\log n)$$. Since both of these functions
dominate $$O(n)$$, this algorithm will have the same order of magnitude as that
of the sorting process.

Solution 3: Brute Force
-----------------------

A *brute force* technique for solving a problem typically tries to exhaust all
possibilities. We can apply this technique to the anagram problem by generating
a list of all possible strings using the characters from `s1`. If `s2` occurs
in that list, then `s1` and `s2` ar anagrams.

There is a difficulty with this approach, however: when generating all possible
strings from `s1`, there are $$n$$ possible first characters, $$n-1$$ possible
second characters, $$n-2$$ possible third characters, and so on. The total
number of candidate strings is $$n*(n-1)*(n-2)*...*3*2*1$$, which is $$n!$$.
Although some of the strings may be duplicates, the program cannot know this
ahead of time, so it will still generate $$n!$$ strings.

It turns out that $$n!$$ grows even faster than $$2^{n}$$ as *n* gets large.
If `s1` were 20 characters long, there would be $$20!$$ or
2,432,902,008,176,640,000 possible candidate strings. If we processed one
candidate every second, it would take 77,146,816,596 years to process the
entire list. This is probably not going to be a good solution.

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
