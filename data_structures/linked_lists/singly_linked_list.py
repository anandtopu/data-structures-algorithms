"""
Singly Linked List Implementation

Time Complexity:
- Access: O(n)
- Search: O(n)
- Insert at head: O(1)
- Insert at tail: O(1) with tail pointer
- Delete: O(n)

Space Complexity: O(n)
"""


class Node:
    """Node class for linked list."""
    
    def __init__(self, data):
        """Initialize a node with data."""
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        """Return the number of elements in the list."""
        return self.size
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.size == 0
    
    def append(self, data):
        """Add element to the end of the list."""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def prepend(self, data):
        """Add element to the beginning of the list."""
        new_node = Node(data)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
    
    def insert_after(self, prev_data, data):
        """Insert element after a node with given data."""
        current = self.head
        
        while current:
            if current.data == prev_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                
                if current == self.tail:
                    self.tail = new_node
                
                self.size += 1
                return True
            current = current.next
        
        return False
    
    def delete(self, data):
        """Delete first occurrence of element with given data."""
        if self.is_empty():
            return False
        
        # Delete head
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self.size -= 1
            return True
        
        # Delete other nodes
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        
        return False
    
    def search(self, data):
        """Search for element with given data."""
        current = self.head
        
        while current:
            if current.data == data:
                return True
            current = current.next
        
        return False
    
    def reverse(self):
        """Reverse the linked list in place."""
        prev = None
        current = self.head
        self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def __str__(self):
        """String representation of the list."""
        if self.is_empty():
            return "[]"
        
        elements = []
        current = self.head
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements)


if __name__ == "__main__":
    # Example usage
    ll = LinkedList()
    
    print("Appending elements:")
    for i in range(1, 6):
        ll.append(i * 10)
    print(f"List: {ll}")
    print(f"Length: {len(ll)}")
    
    print("\nPrepending element 5:")
    ll.prepend(5)
    print(f"List: {ll}")
    
    print("\nInserting 25 after 20:")
    ll.insert_after(20, 25)
    print(f"List: {ll}")
    
    print("\nSearching for 30:")
    print(f"Found: {ll.search(30)}")
    
    print("\nDeleting 20:")
    ll.delete(20)
    print(f"List: {ll}")
    
    print("\nReversing list:")
    ll.reverse()
    print(f"List: {ll}")
