class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        if not A or not A.next:
            return A

        slow = A
        fast = A

        # Step 1: Detect loop using Floyd’s algorithm
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return A  # No loop

        # Step 2: Find the start of the loop
        slow = A
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Step 3: Find the node just before the start of the loop
        ptr = slow
        while ptr.next != slow:
            ptr = ptr.next

        # Step 4: Break the loop
        ptr.next = None

        return A