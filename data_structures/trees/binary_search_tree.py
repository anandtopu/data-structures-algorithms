"""
Binary Search Tree (BST) Implementation

Time Complexity:
- Search/Insert/Delete: O(h) where h is height
  - Best/Average: O(log n) for balanced tree
  - Worst: O(n) for skewed tree

Space Complexity: O(n)
"""


class TreeNode:
    """Node class for binary search tree."""
    
    def __init__(self, value):
        """Initialize a tree node."""
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree implementation."""
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None
    
    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper method to insert value recursively."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        """Search for a value in the BST."""
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        """Helper method to search recursively."""
        if node is None:
            return False
        
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def delete(self, value):
        """Delete a value from the BST."""
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        """Helper method to delete value recursively."""
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to delete found
            # Case 1: No children
            if node.left is None and node.right is None:
                return None
            
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Two children
            # Find minimum in right subtree
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursive(node.right, min_node.value)
        
        return node
    
    def _find_min(self, node):
        """Find node with minimum value in subtree."""
        while node.left is not None:
            node = node.left
        return node
    
    def inorder_traversal(self):
        """Inorder traversal (left, root, right) - returns sorted values."""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """Helper method for inorder traversal."""
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self):
        """Preorder traversal (root, left, right)."""
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        """Helper method for preorder traversal."""
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self):
        """Postorder traversal (left, right, root)."""
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        """Helper method for postorder traversal."""
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def height(self):
        """Get height of the tree."""
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        """Helper method to calculate height."""
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), 
                      self._height_recursive(node.right))
    
    def is_valid_bst(self):
        """Check if tree is a valid BST."""
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_recursive(self, node, min_val, max_val):
        """Helper method to validate BST."""
        if node is None:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False
        
        return (self._is_valid_bst_recursive(node.left, min_val, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_val))


if __name__ == "__main__":
    # Example usage
    bst = BinarySearchTree()
    
    print("Inserting values: 50, 30, 70, 20, 40, 60, 80")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    
    print("\nTraversals:")
    print(f"Inorder (sorted):   {bst.inorder_traversal()}")
    print(f"Preorder:           {bst.preorder_traversal()}")
    print(f"Postorder:          {bst.postorder_traversal()}")
    
    print(f"\nHeight of tree: {bst.height()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    
    print("\nSearching:")
    for val in [40, 25, 80, 100]:
        print(f"  {val}: {'Found' if bst.search(val) else 'Not found'}")
    
    print("\nDeleting 30:")
    bst.delete(30)
    print(f"Inorder after deletion: {bst.inorder_traversal()}")
    
    print("\nDeleting 50:")
    bst.delete(50)
    print(f"Inorder after deletion: {bst.inorder_traversal()}")
