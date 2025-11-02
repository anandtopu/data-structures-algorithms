from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums_set = set(nums)
        while head and head.val in nums_set:
            head = head.next
        curr = head
        while curr and curr.next:
            if curr.next.val in nums_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head