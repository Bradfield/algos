/*
Now that we have clearly defined the stack as an abstract data type we
will turn our attention to using JavaScript to implement the stack. Recall
that when we give an abstract data type a physical implementation we
refer to the implementation as a data structure.

You may be wondering if a JavaScript `array` “is” a stack. It is more precise
to say that a JavaScript `array` “may be used as a” stack. That is to say,
the implementation of `array` in JavaScript provides methods that allow us to
achieve the behavior of the stack abstract data type, for instance
`.push()` allows us to push items to our stack.

In practice “use a JavaScript list as a stack” is precisely what you are
likely to do, in other words you will define something like:
`let pancake_stack = []` then diligently use only the `push` and `pop`
methods as well as `pancake_stack.length` for the size, and
`pancake_stack[pancake_stack.length - 1]` to peek. Of course, a JavaScript
`array` permits much more than the behavior of a stack, notably accessing an
item by index, and inserting and deleting items at any point by index.

As such, we ought to communicate as clearly as possible our intention to
use this (concrete) data structure of a `array` as an abstract data type
stack. Sometimes we can achieve this simply by naming it a stack. Other
times, we may want to use a class to abstract away the implementation of
the stack as an array, and only provide the behaviors that we require of a
stack.

Such an abstraction is also illustrative of the distinction between
concrete data structures and abstract data types, so we provide a
possible implementation of a stack class here:
*/

class Stack {
  constructor() {
    this._items = [];
  }

  is_empty() {
    return this._items.length == 0;
  }

  push(item) {
    this._items.push(item);
  }

  pop() {
    return this._items.pop(item);
  }

  peek() {
    return this._items[self._items.length - 1];
  }

  size() {
    return this._items.length;
  }
}
