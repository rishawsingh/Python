# Implementation of Circular Queue using linked lists
# https://en.wikipedia.org/wiki/Circular_buffer

from typing import Any


class CircularQueueLinkedList:
    """
    Circular FIFO list with the given capacity (default queue length : 6)

    >>> cq = CircularQueueLinkedList(2)
    >>> cq.enqueue('a')
    >>> cq.enqueue('b')
    >>> cq.enqueue('c')
    Traceback (most recent call last):
       ...
    Exception: Full Queue
    """

    def __init__(self, initial_capacity: int = 6) -> None:
        self.front = None
        self.rear = None
        self.create_linked_list(initial_capacity)

    def create_linked_list(self, initial_capacity: int) -> None:
        current_node = Node()
        self.front = current_node
        self.rear = current_node
        previous_node = current_node
        for i in range(1, initial_capacity):
            current_node = Node()
            previous_node.next = current_node
            current_node.prev = previous_node
            previous_node = current_node
        previous_node.next = self.front
        self.front.prev = previous_node

    def is_empty(self) -> bool:
        """
        Checks where the queue is empty or not
        >>> cq = CircularQueueLinkedList()
        >>> cq.is_empty()
        True
        >>> cq.enqueue('a')
        >>> cq.is_empty()
        False
        >>> cq.dequeue()
        'a'
        >>> cq.is_empty()
        True
        """
        return self.front == self.rear and self.front.data is None

    def first(self) -> Any:
        """
        Returns the first element of the queue
        >>> cq = CircularQueueLinkedList()
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('a')
        >>> cq.first()
        'a'
        >>> cq.dequeue()
        'a'
        >>> cq.first()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('b')
        >>> cq.enqueue('c')
        >>> cq.first()
        'b'
        """
        self.check_can_perform_operation()
        return self.front.data

    def enqueue(self, data: Any) -> None:
        """
        Saves data at the end of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.enqueue('a')
        >>> cq.enqueue('b')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        'b'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        self.check_is_full()
        if self.is_empty():
            self.rear.data = data
        else:
            self.rear = self.rear.next
            self.rear.data = data

    def dequeue(self) -> Any:
        """
        Removes and retrieves the first element of the queue

        >>> cq = CircularQueueLinkedList()
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        >>> cq.enqueue('a')
        >>> cq.dequeue()
        'a'
        >>> cq.dequeue()
        Traceback (most recent call last):
           ...
        Exception: Empty Queue
        """
        self.check_can_perform_operation()
        if self.front == self.rear:
            data = self.front.data
            self.front.data = None
            return data

        old_front = self.front
        self.front = old_front.next
        data = old_front.data
        old_front.data = None
        return data

    def check_can_perform_operation(self) -> None:
        if self.is_empty():
            raise Exception("Empty Queue")

    def check_is_full(self) -> None:
        if self.rear.next == self.front:
            raise Exception("Full Queue")


class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
        self.prev = None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
