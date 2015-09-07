Trees and Tree Algorithms
====

The tree is a very commonly encountered Abstract Data Type that allows us to represent hierarchical relationships with no cycles (we will see what “cycles” are momentarily).

It turns out that _many_ of the structures we encounter when writing software are hierarchical and without cycles. For instance, every file and directory within a file system is “inside” one and only one parent directory, up to the root directory. In an HTML document, every tag is inside one and only one parent tag, up to the root (`html`) tag.

It also turns out that that we can use trees to implement useful data structures like maps, and to do fast searches. We will cover some of the many use cases for trees in this chapter, as well as exploring algorithms to traverse through trees.
