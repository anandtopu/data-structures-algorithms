# Definition for a  binary tree node
# class TreeNode:
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# python
from collections import defaultdict, deque

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def verticalOrderTraversal(self, A):
        if not A:
            return []

        hd_map = defaultdict(list)
        queue = deque([(A, 0)])  # (node, horizontal distance)

        while queue:
            node, hd = queue.popleft()
            hd_map[hd].append(node.val)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        sorted_hd_keys = sorted(hd_map.keys())
        return [hd_map[hd] for hd in sorted_hd_keys]
