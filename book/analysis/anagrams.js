/*
Solution 1: Checking Off
------------------------

Our first solution to the anagram problem will check to see that each
character in the first string actually occurs in the second. If it is
possible to “checkoff” each character, then the two strings must be
anagrams. Checking off a character will be accomplished by replacing it
with the special JavaScript value `null`. However, since strings in JavaScript
are immutable, the first step in the process will be to convert the
second string to an array. Each character from the first string
can be checked against the characters in the list and if found, checked off by
replacement. An implementation of this strategy may look like this:
*/

function anagramCheckingOff (string1, string2) {
  if (string1.length !== string2.length) return false

  const string2ToCheckOff = string2.split('')

  for (let i = 0; i < string1.length; i++) {
    let letterFound = false
    for (let j = 0; j < string2ToCheckOff.length; j++) {
      if (string1[i] === string2ToCheckOff[j]) {
        string2ToCheckOff[j] = null
        letterFound = true
        break
      }
    }
    if (!letterFound) return false
  }

  return true
}

assert.equal(true, anagramCheckingOff('abcd', 'dcba'))
assert.equal(false, anagramCheckingOff('abcd', 'abcc'))

/*
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
even though `string1` and `string2` are different, they are anagrams only if
they consist of exactly the same characters. So, if we begin by sorting each
string alphabetically, from a to z, we will end up with the same string
if the original two strings are anagrams. Below is a possible
implementation of this strategy. First, we convert each string to an array using
the string method `split`, and then we use the array method `sort` which
lexographically sorts an array in place and then returns the array. Finally, we
loop through the first string, checking to make sure that both strings contain
the same letter at every index.
*/

function anagramSortAndCompare (string1, string2) {
  if (string1.length !== string2.length) return false

  const sortedString1 = string1.split('').sort()
  const sortedString2 = string2.split('').sort()

  for (let i = 0; i < sortedString1.length; i++) {
    if (sortedString1[i] !== sortedString2[i]) return false
  }

  return true
}

assert.equal(true, anagramSortAndCompare('abcde', 'edcba'))
assert.equal(false, anagramSortAndCompare('abcde', 'abcd'))

/*
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
array of 26 counters, one for each possible character. Each time we see a
particular character, we will increment the counter at that position. In
the end, if the two arrays of counters are identical, the strings must be
anagrams. Here is a possible implementation of the strategy:

*/

function anagramCountCompare (string1, string2) {

  function getLetterPosition (letter) {
    return letter.charCodeAt() - 'a'.charCodeAt()
  }

  // No "clean" way to prepopulate an array in JavaScript with 0's
  const string1LetterCounts = new Array(26)
  const string2LetterCounts = new Array(26)

  for (let i = 0; i < string1.length; i++) {
    const letterPosition = getLetterPosition(string1[i])
    if (!string1LetterCounts[letterPosition]) {
      string1LetterCounts[letterPosition] = 1
    } else {
      string1LetterCounts[letterPosition]++
    }
  }

  for (let i = 0; i < string2.length; i++) {
    const letterPosition = getLetterPosition(string2[i])
    if (!string2LetterCounts[letterPosition]) {
      string2LetterCounts[letterPosition] = 1
    } else {
      string2LetterCounts[letterPosition]++
    }
  }

  for (let i = 0; i < string1LetterCounts.length; i++) {
    if (string1LetterCounts[i] !== string2LetterCounts[i]) {
      return false
    }
  }

  return true
}

assert.equal(true, anagramCountCompare('apple', 'pleap'))
assert.equal(false, anagramCountCompare('apple', 'applf'))

/*
Again, the solution has a number of iterations. However, unlike the
first solution, none of them are nested. The first two iterations used
to count the characters are both based on $$n$$. The third iteration,
comparing the two lists of counts, always takes 26 steps since there are
26 possible characters in the strings. Adding it all up gives us
$$T(n)=2n+26$$ steps. That is $$O(n)$$. We have found a linear order of
magnitude algorithm for solving this problem.

Those with greater familiarity with JavaScript may note that the counting
strategy we implemented in `anagramCountCompare` could be much more
succinctly approached using the `reduce` method of arrays. Note that we are
required to add an additional check that the strings are of the same length
since our dictionary comparison loop will not account for string2 having
additional characters.
*/

function anagramCountCompareWithReduce (string1, string2) {

  function letterCountReducer (letterCounts, letter) {
    if (letterCounts[letter]) {
      letterCounts[letter]++
    } else {
      letterCounts[letter] = 0
    }
    return letterCounts
  }

  const string1LetterCounts = string1.split('').reduce(letterCountReducer, {})
  const string2LetterCounts = string2.split('').reduce(letterCountReducer, {})


  for (let letter in string1LetterCounts) {
    if (string1LetterCounts[letter] !== string2LetterCounts[letter]) {
      return false
    }
  }

  return string1.length === string2.length
}

assert.equal(true, anagramCountCompareWithReduce('apple', 'pleap'))
assert.equal(false, anagramCountCompareWithReduce('apple', 'applf'))

/*
It is worth noting that `anagramCounterCompareWithReduce` is also $$O(n)$$, but
that it is impossible to determine this without understanding the
implementation of `Array.reduce` method.

Before leaving this example, we need to say something about space
requirements. Although the last solution was able to run in linear time,
it could only do so by using additional storage to keep the two dictionaries of
character counts. In other words, this algorithm sacrificed space in
order to gain time.

This is a common tradeoff. On many occasions you will need to make
decisions between time and space trade-offs. In this case, the amount of
extra space is not significant. However, if the underlying alphabet had
millions of characters, there would be more concern. As a software
engineer, when given a choice of algorithms, it will be up to you to
determine the best use of computing resources given a particular
problem.
*/
