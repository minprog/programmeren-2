# Queue

Let's see what it means to define a useful *interface* for a class. To do this, our starting point is the **queue** data structure, which is often used to efficiently implement algorithms...

The goal of a queue is to be able to store items that you might retrieve later, in the order in which they were stored. As such, a queue supports two core operations:

- **enqueue**, which adds an item to the back of queue, waiting to be collected again
- **dequeue**, which removes an item from the front of the queue

![A visual description of the queue structure. It is a row of elements. One end is labeled 'back' and the other end 'front'. On the periphery near the back is another element, with an arrow pointing from that element to the back, labeled 'enqueue'. From the front an arrow points to a different element outside the queue. That arrow is labeled 'dequeue'.](wikipedia_queue.png){:style="max-width:300px"}  
<small>Image by [Vegpuff/Wikipedia](https://commons.wikimedia.org/wiki/File:Data_Queue.svg).</small>

Note our use of "front" and "back". The most important thing about queues is that elements are added to one end, while removing elements is done at the other end. This ensures that elements which are first into the queue, will also be removed first (this is often called first-in-first-out, or FIFO).

From the description you might understand that a queue is, in its essence, a list of items, but that it enables a very specific way of dealing with that data --- using the two core operations.

These two operations form the core *interface* of the queue data structure, which defines how it is supposed to be used.

{% next "Let's get started" %}


## Defining a class interface

Classes may be used to implement structures like queues. If we structure a class using the information in the previous section, it might look like this:

    class Queue:

        # add element to back of queue
        def enqueue(self, element):
            # TODO

        # remove element from front of queue
        def dequeue(self):
            # TODO

And when fully implemented (note the `TODO`s!) one would probably want to use the class like this:

    q = Queue()          # create new queue
    q.enqueue(3)         # add number 3 to back of queue
    q.enqueue(1)         # add number 1 to back of queue
    print(q.dequeue())   # prints first number "in", so 3

Before you go on, copy the class definition from above into the editor on the right. You can also copy the testing code.

We have now defined the *class interface* in Python. The class interface, consisting of two methods, prescribes how you could **use** the class by calling its methods. However, our interface does not have an implementation yet, so the testing code doesn't work.

{% next %}


## Choosing an internal representation

As we mentioned, a queue is similar to a list, yet with a different set of supported operations. Any queue-type object needs to have some data storage. We will use a standard Python list to build our class around. Each queue object will *contain* its own private list object.

To create an object that is internal to our queue objects, we should store and retrieve it using the `self` keyword:

    self._data = []

This line creates a new list and stores it in the object under the name `_data`. We chose to start the name with an underscore (`_`) to indicate that the variable is private to the object, and that one should not to write code to manipulate that variable from anywhere else but the code of the class itself.

Because each object needs such a list from the very beginning, the line above should be placed in the *object initializer*. That initializer could look like this:

    def __init__(self):
        self._data = []

Before you go on, add this method to the top of the `Queue` class definition.

Now, each time a new object is created using the `Queue()` syntax, it will also create an internal list, which is accessible from the class code using `self._data`.

{% next %}


## Enqueueing

Now that we have storage, it's time to implement `enqueue()`. Recall that items should be stored at one end, but removed at the other end of the queue. How could we do this using the standard Python list that we chose to use?

Python lists support a variety of operations for adding and removing items. [Have a look at the documentation](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types). You probably know `append()` to add an item to the "end" of a list. That seems a good starting point.

> Do make note, however, that in the image above, the "back" of the queue was pictured to the left, while you might imagine the "end" of a list being on the right. This is an implementation detail. It is not wrong per se, as long as you make sure that elements are enqueued and dequeued on opposite sides. Anyone writing code using the `Queue` class should not worry about data being on the left or the right, as long as the queue definition is adhered to.

Implement `enqueue()` to append the given element to the internal `_data` list.

{% next %}


## Dequeueing

Now that you have implemented this method, how should you implement `dequeue()`? As we have defined `enqueue()` to place items at the "end" of the list, we should be looking to **remove** items from the "start".

There's a catch! What use is it to remove elements from a queue if we can't do anything with those? The method should not only remove the element but also `return` it.

Take another look at the Python documentation for lists and see if you can find a method that you can use to remove elements from the start of a list (in other words: elements that are furthest from the end of the list).

Implement `dequeue()` to remove the frontmost element from the internal `_data` list and return it.

{% next %}


## Features

While `enqueue()` and `dequeue()` are quite essential for implementing the queue data structure, there are some additional features that may come in handy.

We now ask you to implement three of those operations as methods of the `Queue` class:

- **size**, which returns the number of elements "waiting" in the queue
- **peek**, which returns the frontmost element but does not remove it from the queue (yet)
- **empty**, which clears the queue, removing all elements

Implement these operations and add some testing code below to see if it all works well.

{% next %}


## Resume

Having implemented the queue class, you should notice what it *doesn't* support. You can't, for example, take a look at the second element of a queue, unless you remove the first one. And you definitely can't dequeue an element from the back of the queue.

The idea of a queue is used in many applications, but an important one is scheduling. Computers can administer many tasks that have to be performed, and when one task is done, another may be started. The list of open tasks is kept in a queue, ensuring that the oldest task is scheduled first.

All in all, a queue is a lot less flexible than a standard Python structure such as a list or a dictionary. So why use a queue at all? Because it provides a very simple to use *interface* for a very specific task. This makes the code that *uses* the queue much simpler to read. A programmer recognizes the queue structure with its enqueue and dequeue operations and immediately understands what's going on.

There are a few standard structures like queues that you might be aware of as a programming. One that you might have encountered before is the **stack**. You could look that one up on Wikipedia, for example, and try to implement its operations in a Python class. It is quite similar to a queue, yet very different in its behavior and its applications!

This was Queue!






