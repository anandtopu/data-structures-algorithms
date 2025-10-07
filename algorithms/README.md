# Algorithms

This directory contains implementations of fundamental algorithms.

## Available Implementations

### Sorting Algorithms
- **Quick Sort** (`sorting/quick_sort.py`): O(n log n) average case, divide-and-conquer sorting
- **Merge Sort** (`sorting/merge_sort.py`): O(n log n) stable sorting algorithm

### Searching Algorithms
- **Binary Search** (`searching/binary_search.py`): O(log n) search in sorted arrays
  - Iterative and recursive implementations
  - First/last occurrence variants
  - Insert position finder

## Complexity Analysis

Each implementation includes detailed time and space complexity analysis:

### Sorting
| Algorithm  | Best       | Average    | Worst      | Space      | Stable |
|-----------|------------|------------|------------|------------|--------|
| Quick Sort | O(n log n) | O(n log n) | O(n²)      | O(log n)   | No     |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n)       | Yes    |

### Searching
| Algorithm     | Time Complexity | Space      | Requirement    |
|--------------|----------------|------------|----------------|
| Binary Search | O(log n)       | O(1)/O(log n) | Sorted array |

## Usage

Run any file directly to see examples and performance tests:
```bash
python3 algorithms/sorting/quick_sort.py
python3 algorithms/searching/binary_search.py
```

Run tests:
```bash
python3 -m pytest tests/test_algorithms.py -v
```
