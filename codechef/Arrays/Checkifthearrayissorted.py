'''Check if the array is sorted
Given an array nums, return true if the array was initially sorted in non-decreasing order and then rotated any number of times (including zero). Otherwise, return false.

Rotation means that some suffix of the array is moved to the front.
Duplicates are allowed in the array.
Note:
If A is the original sorted array and it is rotated right by k positions, the resulting array B satisfies:
B[(i+k) mod A.length]=A[i]
B[(i+k)modA.length]=A[i]
for every valid index i.
1 2 3 4 5 is a sorted array and 2 3 4 5 1 is also a sorted array but after 4 rotations.
Constraints
1 ≤ nums.length ≤ 100
1≤nums.length≤100
1 ≤ nums [ i] ≤ 100
1≤nums[i]≤100'''
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                cnt += 1

        return cnt <= 1