/*
It is important to note that we could have chosen to implement the stack
using an array where the top is at the beginning instead of at the end. In
this case, instead of using `pop` and `push` as above, instead we
would pop from and insert into position 0. Here is a possible
implementation of that approach:
*/

class Stack {
  constructor() {
    this._items = [];
  }

  is_empty() {
    return this._items.length == 0;
  }

  push(item) {
    this._items.splice(0, 0, item);
  }

  pop() {
    return this._items.splice(0, 1);
  }

  peek() {
    return self._items[0];
  }

  size() {
    return self._items.length;
  }
}

/*
This ability to change the physical implementation of an abstract data
type while maintaining the logical characteristics is an example of
abstraction at work. However, even though the stack will work either
way, if we consider the performance of the two implementations, there is
definitely a difference. Recall that the `push` and `pop()` operations
were both $$O(1)$$. This means that the first implementation will
perform push and pop in constant time no matter how many items are on
the stack. The performance of the second implementation suffers in that
all the `splice()` operations will require $$O(n)$$ for a
stack of size n. Clearly, even though the implementations are logically
equivalent, they would have very different timings when performing
benchmark testing.

Going forward, we will simply use JavaScript's `array`s directly as stacks,
being careful to only use the stack-like behavior of the `array`.
*/
