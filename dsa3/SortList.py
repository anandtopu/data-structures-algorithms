# Definition for singly-linked list.
'''How it works:

sortList is the main function that applies merge sort recursively.
getMiddle finds the midpoint of the list using the slow-fast pointer technique.
merge merges two sorted linked lists into one.
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        # Base case: if list is empty or has only one node
        if not A or not A.next:
            return A

        # Step 1: Split the list into two halves
        mid = self.getMiddle(A)
        right = mid.next
        mid.next = None  # Break the list into two halves

        # Step 2: Recursively sort both halves
        left_sorted = self.sortList(A)
        right_sorted = self.sortList(right)

        # Step 3: Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def getMiddle(self, head):
        # Initialize slow and fast pointers
        slow = head
        fast = head

        # Move fast by 2 steps and slow by 1 step
        # When fast reaches the end, slow will be at the middle
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, l1, l2):
        # Merge two sorted linked lists
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Append the remaining nodes
        tail.next = l1 if l1 else l2
        return dummy.next


'''Brute-force Strategy:

Traverse the linked list and store all node values in a Python list.
Sort the list using Python’s built-in sort() method.
Reconstruct the linked list from the sorted values.

This approach has a time complexity of O(n log n) due to the sorting step, but it uses O(n) extra space, which is not optimal compared to merge sort that works in-place.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        # Step 1: Extract values from the linked list
        values = []
        current = A
        while current:
            values.append(current.val)
            current = current.next

        # Step 2: Sort the values
        values.sort()

        # Step 3: Reconstruct the linked list from sorted values
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next

        return dummy.next
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(n) for storing values in a list

def merge(l1, l2):
    dummy = ListNode(0)
    head = dummy

    while (l1 and l2):
        # find the smaller node
        if (l1.val <= l2.val):
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next
    # add the remaining nodes
    head.next = l1 if l1 else l2
    return dummy.next


def sortL(head):
    if (head == None or head.next == None):
        return head
    pre, fast, slow = head, head, head

    # find the middle node
    while (fast and fast.next):
        pre = slow
        slow = slow.next
        fast = fast.next.next

    pre.next = None
    return merge(sortL(head), sortL(slow))


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        return sortL(A)
