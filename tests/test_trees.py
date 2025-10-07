"""
Unit tests for tree data structures
Run with: python3 -m pytest tests/
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.trees.binary_search_tree import BinarySearchTree


class TestBinarySearchTree:
    """Test cases for Binary Search Tree."""
    
    def test_insert_search(self):
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        
        for val in values:
            bst.insert(val)
        
        for val in values:
            assert bst.search(val)
        
        assert not bst.search(25)
        assert not bst.search(100)
    
    def test_inorder_traversal(self):
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        
        for val in values:
            bst.insert(val)
        
        # Inorder should give sorted values
        assert bst.inorder_traversal() == [20, 30, 40, 50, 60, 70, 80]
    
    def test_delete_leaf(self):
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40]
        
        for val in values:
            bst.insert(val)
        
        bst.delete(20)
        assert not bst.search(20)
        assert bst.inorder_traversal() == [30, 40, 50, 70]
    
    def test_delete_one_child(self):
        bst = BinarySearchTree()
        values = [50, 30, 70, 60]
        
        for val in values:
            bst.insert(val)
        
        bst.delete(70)
        assert not bst.search(70)
        assert bst.inorder_traversal() == [30, 50, 60]
    
    def test_delete_two_children(self):
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        
        for val in values:
            bst.insert(val)
        
        bst.delete(30)
        assert not bst.search(30)
        assert bst.inorder_traversal() == [20, 40, 50, 60, 70, 80]
    
    def test_height(self):
        bst = BinarySearchTree()
        assert bst.height() == 0
        
        bst.insert(50)
        assert bst.height() == 1
        
        bst.insert(30)
        bst.insert(70)
        assert bst.height() == 2
    
    def test_is_valid_bst(self):
        bst = BinarySearchTree()
        values = [50, 30, 70, 20, 40, 60, 80]
        
        for val in values:
            bst.insert(val)
        
        assert bst.is_valid_bst()
