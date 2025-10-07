"""
Unit tests for data structures
Run with: python3 -m pytest tests/
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.arrays.dynamic_array import DynamicArray
from data_structures.linked_lists.singly_linked_list import LinkedList
from data_structures.stacks.stack import Stack, is_balanced_parentheses
from data_structures.queues.queue import Queue, CircularQueue


class TestDynamicArray:
    """Test cases for Dynamic Array."""
    
    def test_append(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        assert len(arr) == 2
        assert arr[0] == 1
        assert arr[1] == 2
    
    def test_insert(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(3)
        arr.insert(1, 2)
        assert len(arr) == 3
        assert arr[0] == 1
        assert arr[1] == 2
        assert arr[2] == 3
    
    def test_delete(self):
        arr = DynamicArray()
        arr.append(1)
        arr.append(2)
        arr.append(3)
        arr.delete(1)
        assert len(arr) == 2
        assert arr[0] == 1
        assert arr[1] == 3


class TestLinkedList:
    """Test cases for Linked List."""
    
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert len(ll) == 2
        assert ll.search(1)
        assert ll.search(2)
    
    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        assert len(ll) == 2
    
    def test_delete(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(1)
        assert len(ll) == 1
        assert not ll.search(1)
        assert ll.search(2)
    
    def test_reverse(self):
        ll = LinkedList()
        for i in range(1, 4):
            ll.append(i)
        ll.reverse()
        # After reverse: 3 -> 2 -> 1
        assert ll.head.data == 3
        assert ll.tail.data == 1


class TestStack:
    """Test cases for Stack."""
    
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()
    
    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert stack.size() == 2
    
    def test_balanced_parentheses(self):
        assert is_balanced_parentheses("(())")
        assert is_balanced_parentheses("{[()]}")
        assert not is_balanced_parentheses("(()")
        assert not is_balanced_parentheses("{[(])}")


class TestQueue:
    """Test cases for Queue."""
    
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.is_empty()
    
    def test_front(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        assert q.front() == 1
        assert q.size() == 2


class TestCircularQueue:
    """Test cases for Circular Queue."""
    
    def test_enqueue_dequeue(self):
        cq = CircularQueue(3)
        cq.enqueue(1)
        cq.enqueue(2)
        assert cq.dequeue() == 1
        cq.enqueue(3)
        cq.enqueue(4)
        assert cq.size() == 3
    
    def test_full(self):
        cq = CircularQueue(2)
        cq.enqueue(1)
        cq.enqueue(2)
        assert cq.is_full()
