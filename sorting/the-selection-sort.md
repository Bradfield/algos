The Selection Sort
==================

The **selection sort** improves on the bubble sort by making only one
exchange for every pass through the list. In order to do this, a
selection sort looks for the largest value as it makes a pass and, after
completing the pass, places it in the proper location. As with a bubble
sort, after the first pass, the largest item is in the correct place.
After the second pass, the next largest is in place. This process
continues and requires $n-1$ passes to sort *n* items, since the final
item must be in place after the $(n-1)$ st pass.

Figure 3 shows the entire sorting process. On
each pass, the largest remaining item is selected and then placed in its
proper location. The first pass places 93, the second pass places 77,
the third places 55, and so on. The function is shown in
ActiveCode 1 &lt;lst\_selectionsortcode&gt;.

![Figure 3: `selectionSort`](figures/selectionsortnew.png)

You may see that the selection sort makes the same number of comparisons
as the bubble sort and is therefore also $O(n^{2})$. However, due to the
reduction in the number of exchanges, the selection sort typically
executes faster in benchmark studies. In fact, for our list, the bubble
sort makes 20 exchanges, while the selection sort makes only 8.
