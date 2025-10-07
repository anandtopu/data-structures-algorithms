"""
Merge Sort Implementation

Time Complexity:
- Best/Average/Worst: O(n log n)
- Stable sort algorithm

Space Complexity: O(n) - requires additional space for merging

Algorithm:
1. Divide array into two halves
2. Recursively sort each half
3. Merge the two sorted halves
"""


def merge_sort(arr):
    """
    Sort array using Merge Sort algorithm.
    
    Args:
        arr: List to be sorted
    
    Returns:
        Sorted list
    """
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Combine
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Args:
        left: First sorted list
        right: Second sorted list
    
    Returns:
        Merged sorted list
    """
    result = []
    i = j = 0
    
    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort_inplace(arr, low=0, high=None):
    """
    In-place Merge Sort implementation.
    Modifies the original array.
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        mid = (low + high) // 2
        
        merge_sort_inplace(arr, low, mid)
        merge_sort_inplace(arr, mid + 1, high)
        merge_inplace(arr, low, mid, high)
    
    return arr


def merge_inplace(arr, low, mid, high):
    """Merge two sorted subarrays in place."""
    # Create temporary arrays
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    
    i = j = 0
    k = low
    
    # Merge back to original array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


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
    
    print("=== Merge Sort ===\n")
    
    for arr in test_arrays:
        original = arr.copy()
        sorted_arr = merge_sort(arr)
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
        merge_sort(arr)
        duration = time.time() - start
        
        print(f"Size: {size:5d}, Time: {duration:.6f} seconds")
