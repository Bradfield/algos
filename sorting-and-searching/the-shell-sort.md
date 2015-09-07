The Shell Sort
==============

The **shell sort**, sometimes called the “diminishing increment sort,”
improves on the insertion sort by breaking the original list into a
number of smaller sublists, each of which is sorted using an insertion
sort. The unique way that these sublists are chosen is the key to the
shell sort. Instead of breaking the list into sublists of contiguous
items, the shell sort uses an increment `i`, sometimes called the
**gap**, to create a sublist by choosing all items that are `i` items
apart.

This can be seen in Figure 6 &lt;fig\_incrementsA&gt;. This list has
nine items. If we use an increment of three, there are three sublists,
each of which can be sorted by an insertion sort. After completing these
sorts, we get the list shown in Figure 7 &lt;fig\_incrementsB&gt;.
Although this list is not completely sorted, something very interesting
has happened. By sorting the sublists, we have moved the items closer to
where they actually belong.

![Figure 6: A Shell Sort with Increments of
Three](Figures/shellsortA.png)

![Figure 7: A Shell Sort after Sorting Each
Sublist](Figures/shellsortB.png)

Figure 8 &lt;fig\_incrementsC&gt; shows a final insertion sort using an
increment of one; in other words, a standard insertion sort. Note that
by performing the earlier sublist sorts, we have now reduced the total
number of shifting operations necessary to put the list in its final
order. For this case, we need only four more shifts to complete the
process.

![Figure 8: ShellSort: A Final Insertion Sort with Increment of
1](Figures/shellsortC.png)

![Figure 9: Initial Sublists for a Shell Sort](Figures/shellsortD.png)

We said earlier that the way in which the increments are chosen is the
unique feature of the shell sort. The function shown in
ActiveCode 1 &lt;lst\_shell&gt; uses a different set of increments. In
this case, we begin with $\frac {n}{2}$ sublists. On the next pass,
$\frac {n}{4}$ sublists are sorted. Eventually, a single list is sorted
with the basic insertion sort. Figure 9 &lt;fig\_incrementsD&gt; shows
the first sublists for our example using this increment.

The following invocation of the `shellSort` function shows the partially
sorted lists after each increment, with the final sort being an
insertion sort with an increment of one.

At first glance you may think that a shell sort cannot be better than an
insertion sort, since it does a complete insertion sort as the last
step. It turns out, however, that this final insertion sort does not
need to do very many comparisons (or shifts) since the list has been
pre-sorted by earlier incremental insertion sorts, as described above.
In other words, each pass produces a list that is “more sorted” than the
previous one. This makes the final pass very efficient.

Although a general analysis of the shell sort is well beyond the scope
of this text, we can say that it tends to fall somewhere between $O(n)$
and $O(n^{2})$, based on the behavior described above. For the
increments shown in Listing 5 &lt;lst\_shell&gt;, the performance is
$O(n^{2})$. By changing the increment, for example using $2^{k}-1$ (1,
3, 7, 15, 31, and so on), a shell sort can perform at
$O(n^{\frac {3}{2}})$.

