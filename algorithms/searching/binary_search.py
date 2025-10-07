"""
Binary Search Implementation

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive

Requirement: Array must be sorted
"""


def binary_search_iterative(arr, target):
    """
    Iterative binary search implementation.
    
    Args:
        arr: Sorted list to search in
        target: Element to search for
    
    Returns:
        Index of target if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive binary search implementation.
    
    Args:
        arr: Sorted list to search in
        target: Element to search for
        left: Left boundary
        right: Right boundary
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_first_occurrence(arr, target):
    """
    Find first occurrence of target in sorted array with duplicates.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching in left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_last_occurrence(arr, target):
    """
    Find last occurrence of target in sorted array with duplicates.
    """
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching in right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def binary_search_insert_position(arr, target):
    """
    Find position where target should be inserted to maintain sorted order.
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


if __name__ == "__main__":
    # Example usage
    print("=== Binary Search ===\n")
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"Array: {arr}\n")
    
    targets = [7, 15, 1, 19, 20, 0]
    
    print("Iterative Search:")
    for target in targets:
        idx = binary_search_iterative(arr, target)
        if idx != -1:
            print(f"  {target} found at index {idx}")
        else:
            print(f"  {target} not found")
    
    print("\nRecursive Search:")
    for target in targets:
        idx = binary_search_recursive(arr, target)
        if idx != -1:
            print(f"  {target} found at index {idx}")
        else:
            print(f"  {target} not found")
    
    # Test with duplicates
    print("\n=== Search with Duplicates ===\n")
    arr_dup = [1, 2, 2, 2, 3, 4, 4, 5]
    print(f"Array: {arr_dup}")
    
    target = 2
    first = binary_search_first_occurrence(arr_dup, target)
    last = binary_search_last_occurrence(arr_dup, target)
    print(f"First occurrence of {target}: index {first}")
    print(f"Last occurrence of {target}: index {last}")
    
    target = 4
    first = binary_search_first_occurrence(arr_dup, target)
    last = binary_search_last_occurrence(arr_dup, target)
    print(f"First occurrence of {target}: index {first}")
    print(f"Last occurrence of {target}: index {last}")
    
    # Test insert position
    print("\n=== Insert Position ===\n")
    arr_insert = [1, 3, 5, 7, 9]
    print(f"Array: {arr_insert}")
    
    for target in [0, 2, 4, 6, 10]:
        pos = binary_search_insert_position(arr_insert, target)
        print(f"Insert {target} at position {pos}")
