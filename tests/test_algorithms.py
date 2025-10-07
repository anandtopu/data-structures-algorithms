"""
Unit tests for algorithms
Run with: python3 -m pytest tests/
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.searching.binary_search import (
    binary_search_iterative,
    binary_search_recursive,
    binary_search_first_occurrence,
    binary_search_last_occurrence
)


class TestQuickSort:
    """Test cases for Quick Sort."""
    
    def test_basic_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = quick_sort(arr.copy())
        assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_empty_array(self):
        arr = []
        sorted_arr = quick_sort(arr.copy())
        assert sorted_arr == []
    
    def test_single_element(self):
        arr = [1]
        sorted_arr = quick_sort(arr.copy())
        assert sorted_arr == [1]
    
    def test_duplicates(self):
        arr = [3, 3, 3, 3]
        sorted_arr = quick_sort(arr.copy())
        assert sorted_arr == [3, 3, 3, 3]
    
    def test_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = quick_sort(arr.copy())
        assert sorted_arr == [1, 2, 3, 4, 5]


class TestMergeSort:
    """Test cases for Merge Sort."""
    
    def test_basic_sort(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorted_arr = merge_sort(arr)
        assert sorted_arr == [11, 12, 22, 25, 34, 64, 90]
    
    def test_empty_array(self):
        arr = []
        sorted_arr = merge_sort(arr)
        assert sorted_arr == []
    
    def test_single_element(self):
        arr = [1]
        sorted_arr = merge_sort(arr)
        assert sorted_arr == [1]
    
    def test_duplicates(self):
        arr = [3, 3, 3, 3]
        sorted_arr = merge_sort(arr)
        assert sorted_arr == [3, 3, 3, 3]


class TestBinarySearch:
    """Test cases for Binary Search."""
    
    def test_iterative_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        assert binary_search_iterative(arr, 7) == 3
        assert binary_search_iterative(arr, 1) == 0
        assert binary_search_iterative(arr, 15) == 7
    
    def test_iterative_not_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        assert binary_search_iterative(arr, 4) == -1
        assert binary_search_iterative(arr, 0) == -1
        assert binary_search_iterative(arr, 20) == -1
    
    def test_recursive_found(self):
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        assert binary_search_recursive(arr, 7) == 3
        assert binary_search_recursive(arr, 1) == 0
    
    def test_first_occurrence(self):
        arr = [1, 2, 2, 2, 3, 4, 4, 5]
        assert binary_search_first_occurrence(arr, 2) == 1
        assert binary_search_first_occurrence(arr, 4) == 5
    
    def test_last_occurrence(self):
        arr = [1, 2, 2, 2, 3, 4, 4, 5]
        assert binary_search_last_occurrence(arr, 2) == 3
        assert binary_search_last_occurrence(arr, 4) == 6
    
    def test_empty_array(self):
        arr = []
        assert binary_search_iterative(arr, 1) == -1
        assert binary_search_recursive(arr, 1) == -1
