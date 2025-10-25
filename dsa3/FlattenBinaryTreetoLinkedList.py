# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



# Preorder: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
# Inorder: 3 -> 2 -> 4 -> 1 -> 6 -> 5 -> 7
# Postorder: 3 -> 4 -> 2 -> 6 -> 7 ->


# Flattened: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
# '''
# Definition for a  binary tree node.
class Solution:
    def flatten(self, root):
        if not root:
            return None

        nodes = []

        def preorder(node):
            if not node:
                return
            nodes.append(node)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        for i in range(len(nodes) - 1):
            nodes[i].left = None
            nodes[i].right = nodes[i + 1]

        return root


class Solution2:
    def flatten(self, root):
        self.prev = None

        def helper(node):
            if not node:
                return
            helper(node.right)
            helper(node.left)

            node.right = self.prev
            node.left = None
            self.prev = node

        helper(root)
        return root