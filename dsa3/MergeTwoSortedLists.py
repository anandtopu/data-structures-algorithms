# Definition for singly-linked list.

'''Brute-Force Approach
🔧 Algorithm:

Traverse both lists and collect all values into a Python list.
Sort the combined list using Python’s built-in sort() (O(n log n)).
Reconstruct a new linked list from the sorted values.

'''
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : head node of linked list
	# @return the head node in the linked list
	def mergeTwoLists(self, A, B):
        values = []
        while A:
            values.append(A.val)
            A = A.next
        while B:
            values.append(B.val)
            B = B.next

        values.sort()

        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

'''⏱️ Time Complexity:

Traversal: O(n + m)
Sorting: O((n + m) log(n + m))
Reconstruction: O(n + m)

📦 Space Complexity:

O(n + m) for storing values
O(n + m) for new nodes

⚠️ Downsides:

Not memory-efficient (creates new nodes).
Doesn’t reuse existing nodes.
Not optimal for large lists.'''

class Solution:
    def mergeTwoLists(self, A, B):
        dummy = ListNode(0)
        tail = dummy

        while A and B:
            if A.val <= B.val:
                tail.next = A
                A = A.next
            else:
                tail.next = B
                B = B.next
            tail = tail.next

        tail.next = A if A else B
        return dummy.next
'''Optimized Approach (In-Place Merge)
🔧 Algorithm:

Use two pointers to traverse both lists.
Compare current nodes of A and B.
Append the smaller node to the result list.
Move the pointer forward in the list from which the node was taken.
When one list is exhausted, append the remaining nodes from the other list.'''

''' Time Complexity:

O(n + m) — each node is visited once.

📦 Space Complexity:

O(1) — no extra space used (in-place merge).

✅ Advantages:

Efficient for large lists.
Reuses existing nodes.
No extra memory allocation.'''