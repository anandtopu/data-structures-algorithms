"""
Quick Sort Implementation

Time Complexity:
- Best/Average: O(n log n)
- Worst: O(n²) - when pivot is always smallest/largest
- Can be improved with random pivot selection

Space Complexity: O(log n) - for recursion stack

Algorithm:
1. Choose a pivot element
2. Partition array so elements < pivot are on left, > pivot on right
3. Recursively sort left and right partitions
"""


def quick_sort(arr, low=0, high=None):
    """
    Sort array using Quick Sort algorithm.
    
    Args:
        arr: List to be sorted
        low: Starting index
        high: Ending index
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high)
        
        # Recursively sort left and right partitions
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Partition array using last element as pivot.
    
    Returns index of pivot after partitioning.
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_optimized(arr, low=0, high=None):
    """
    Optimized Quick Sort with random pivot selection.
    """
    import random
    
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Choose random pivot and swap with last element
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        
        # Partition and sort
        pivot_idx = partition(arr, low, high)
        quick_sort_optimized(arr, low, pivot_idx - 1)
        quick_sort_optimized(arr, pivot_idx + 1, high)
    
    return arr


if __name__ == "__main__":
    # Example usage
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    print("=== Quick Sort ===\n")
    
    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = quick_sort(arr.copy())
        print(f"Original: {original}")
        print(f"Sorted:   {sorted_arr}")
        print()
    
    # Performance test
    import random
    import time
    
    print("=== Performance Test ===")
    sizes = [100, 1000, 5000]
    
    for size in sizes:
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        start = time.time()
        quick_sort(arr.copy())
        duration = time.time() - start
        
        print(f"Size: {size:5d}, Time: {duration:.6f} seconds")
