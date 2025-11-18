
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def iter_dfs(node):
            result = 0
            stk = [(1, [node, [0]])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, ret = params
                    if not node:
                        continue
                    ret1, ret2 = [0], [0]
                    stk.append((2, [node, ret1, ret2, ret]))
                    stk.append((1, [node.right, ret2]))
                    stk.append((1, [node.left, ret1]))
                elif step == 2:
                    node, ret1, ret2, ret = params
                    result = max(result, ret1[0]+ret2[0])
                    ret[0] = 1+max(ret1[0], ret2[0])
            return result

        return iter_dfs(root)

# Time:  O(n)
# Space: O(h)

'''Solution Explanation
This algorithm computes the diameter of a binary tree—the length of the longest path between any two nodes—using an iterative post-order DFS approach with an explicit stack.

Core Approach:
Instead of recursion, the solution uses a stack to simulate post-order traversal. For each node, it computes the heights of its left and right subtrees, then updates the maximum diameter found so far as the sum of these heights.

Key Concepts:

Post-order Traversal: Children are processed before the parent, ensuring subtree heights are available when needed.
Stack Simulation: Each stack entry includes a step indicator (to distinguish between pre- and post-processing) and mutable lists to pass computed heights up the stack.
Diameter Calculation: At each node, the sum of left and right subtree heights is considered as a candidate for the diameter.
Complexity:

Time: O(n), since each node is visited once.
Space: O(h), where h is the tree height, due to the stack.
This approach avoids recursion and efficiently computes the diameter in a single traversal.
'''