"""
Dynamic Array Implementation
A resizable array that grows automatically when capacity is reached.

Time Complexity:
- Access: O(1)
- Append: O(1) amortized
- Insert: O(n)
- Delete: O(n)

Space Complexity: O(n)
"""


class DynamicArray:
    """A dynamic array implementation that resizes automatically."""
    
    def __init__(self, capacity=10):
        """Initialize the dynamic array with given capacity."""
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity
    
    def __len__(self):
        """Return the number of elements in the array."""
        return self.size
    
    def __getitem__(self, index):
        """Get element at given index."""
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        return self.array[index]
    
    def __setitem__(self, index, value):
        """Set element at given index."""
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        self.array[index] = value
    
    def append(self, value):
        """Add element to the end of the array."""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1
    
    def insert(self, index, value):
        """Insert element at given index."""
        if not 0 <= index <= self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        # Shift elements to the right
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        
        self.array[index] = value
        self.size += 1
    
    def delete(self, index):
        """Delete element at given index."""
        if not 0 <= index < self.size:
            raise IndexError("Index out of range")
        
        # Shift elements to the left
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size - 1] = None
        self.size -= 1
        
        # Shrink if needed
        if self.size > 0 and self.size == self.capacity // 4:
            self._resize(self.capacity // 2)
    
    def _resize(self, new_capacity):
        """Resize the internal array to new capacity."""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity
    
    def __str__(self):
        """String representation of the array."""
        return str([self.array[i] for i in range(self.size)])


if __name__ == "__main__":
    # Example usage
    arr = DynamicArray()
    
    print("Appending elements:")
    for i in range(5):
        arr.append(i * 10)
    print(f"Array: {arr}")
    print(f"Length: {len(arr)}")
    
    print("\nInserting element 99 at index 2:")
    arr.insert(2, 99)
    print(f"Array: {arr}")
    
    print("\nDeleting element at index 1:")
    arr.delete(1)
    print(f"Array: {arr}")
    
    print("\nAccessing elements:")
    print(f"Element at index 0: {arr[0]}")
    print(f"Element at index 2: {arr[2]}")
