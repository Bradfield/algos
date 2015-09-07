The Binary Search
=================

It is possible to take greater advantage of the ordered list if we are
clever with our comparisons. In the sequential search, when we compare
against the first item, there are at most $n-1$ more items to look
through if the first item is not what we are looking for. Instead of
searching the list in sequence, a **binary search** will start by
examining the middle item. If that item is the one we are searching for,
we are done. If it is not the correct item, we can use the ordered
nature of the list to eliminate half of the remaining items. If the item
we are searching for is greater than the middle item, we know that the
entire lower half of the list as well as the middle item can be
eliminated from further consideration. The item, if it is in the list,
must be in the upper half.

We can then repeat the process with the upper half. Start at the middle
item and compare it against what we are looking for. Again, we either
find it or split the list in half, therefore eliminating another large
part of our possible search space. Figure 3 &lt;fig\_binsearch&gt; shows
how this algorithm can quickly find the value 54. The complete function
is shown in CodeLens 3 &lt;lst\_binarysearchpy&gt;.

![Figure 3: Binary Search of an Ordered List of
Integers](Figures/binsearch.png)

Before we move on to the analysis, we should note that this algorithm is
a great example of a divide and conquer strategy. Divide and conquer
means that we divide the problem into smaller pieces, solve the smaller
pieces in some way, and then reassemble the whole problem to get the
result. When we perform a binary search of a list, we first check the
middle item. If the item we are searching for is less than the middle
item, we can simply perform a binary search of the left half of the
original list. Likewise, if the item is greater, we can perform a binary
search of the right half. Either way, this is a recursive call to the
binary search function passing a smaller list.
CodeLens 4 &lt;lst\_recbinarysearch&gt; shows this recursive version.

Analysis of Binary Search
-------------------------

To analyze the binary search algorithm, we need to recall that each
comparison eliminates about half of the remaining items from
consideration. What is the maximum number of comparisons this algorithm
will require to check the entire list? If we start with *n* items, about
$\frac{n}{2}$ items will be left after the first comparison. After the
second comparison, there will be about $\frac{n}{4}$. Then
$\frac{n}{8}$, $\frac{n}{16}$, and so on. How many times can we split
the list? Table 3 &lt;tbl\_binaryanalysis&gt; helps us to see the
answer.

When we split the list enough times, we end up with a list that has just
one item. Either that is the item we are looking for or it is not.
Either way, we are done. The number of comparisons necessary to get to
this point is *i* where $\frac {n}{2^i} =1$. Solving for *i* gives us
$i=\log n$. The maximum number of comparisons is logarithmic with
respect to the number of items in the list. Therefore, the binary search
is $O(\log n)$.

One additional analysis issue needs to be addressed. In the recursive
solution shown above, the recursive call,

`binarySearch(alist[:midpoint],item)`

uses the slice operator to create the left half of the list that is then
passed to the next invocation (similarly for the right half as well).
The analysis that we did above assumed that the slice operator takes
constant time. However, we know that the slice operator in Python is
actually O(k). This means that the binary search using slice will not
perform in strict logarithmic time. Luckily this can be remedied by
passing the list along with the starting and ending indices. The indices
can be calculated as we did in Listing 3 &lt;lst\_binarysearchpy&gt;. We
leave this implementation as an exercise.

Even though a binary search is generally better than a sequential
search, it is important to note that for small values of *n*, the
additional cost of sorting is probably not worth it. In fact, we should
always consider whether it is cost effective to take on the extra work
of sorting to gain searching benefits. If we can sort once and then
search many times, the cost of the sort is not so significant. However,
for large lists, sorting even once can be so expensive that simply
performing a sequential search from the start may be the best choice.

> **Self Check**
