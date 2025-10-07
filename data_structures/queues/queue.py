"""
Queue Implementation using List

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(n) - due to list.pop(0)
- Front: O(1)

Space Complexity: O(n)

Note: For better performance, use collections.deque
"""


class Queue:
    """Queue implementation using Python list."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return front item from queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]
    
    def size(self):
        """Return number of items in queue."""
        return len(self.items)
    
    def __str__(self):
        """String representation of queue."""
        return str(self.items)


class CircularQueue:
    """Circular queue implementation using fixed-size array."""
    
    def __init__(self, capacity):
        """Initialize circular queue with given capacity."""
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front_idx = 0
        self.rear_idx = -1
        self.count = 0
    
    def is_empty(self):
        """Check if queue is empty."""
        return self.count == 0
    
    def is_full(self):
        """Check if queue is full."""
        return self.count == self.capacity
    
    def enqueue(self, item):
        """Add item to rear of queue."""
        if self.is_full():
            raise OverflowError("Queue is full")
        
        self.rear_idx = (self.rear_idx + 1) % self.capacity
        self.queue[self.rear_idx] = item
        self.count += 1
    
    def dequeue(self):
        """Remove and return front item from queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        
        item = self.queue[self.front_idx]
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.count -= 1
        return item
    
    def front(self):
        """Return front item without removing it."""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.queue[self.front_idx]
    
    def size(self):
        """Return number of items in queue."""
        return self.count
    
    def __str__(self):
        """String representation of queue."""
        if self.is_empty():
            return "[]"
        
        items = []
        idx = self.front_idx
        for _ in range(self.count):
            items.append(str(self.queue[idx]))
            idx = (idx + 1) % self.capacity
        
        return "[" + ", ".join(items) + "]"


if __name__ == "__main__":
    # Example usage - Simple Queue
    print("=== Simple Queue ===")
    q = Queue()
    
    print("Enqueuing elements:")
    for i in range(1, 6):
        q.enqueue(i * 10)
    print(f"Queue: {q}")
    print(f"Size: {q.size()}")
    
    print("\nFront element:")
    print(f"Front: {q.front()}")
    
    print("\nDequeuing elements:")
    print(f"Dequeued: {q.dequeue()}")
    print(f"Queue: {q}")
    
    # Example usage - Circular Queue
    print("\n=== Circular Queue ===")
    cq = CircularQueue(5)
    
    print("Enqueuing elements:")
    for i in range(1, 6):
        cq.enqueue(i * 10)
    print(f"Circular Queue: {cq}")
    
    print("\nDequeue and enqueue:")
    print(f"Dequeued: {cq.dequeue()}")
    print(f"Dequeued: {cq.dequeue()}")
    cq.enqueue(60)
    cq.enqueue(70)
    print(f"Circular Queue: {cq}")
