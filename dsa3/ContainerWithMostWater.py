'''Problem Description

Given N non-negative integers A[0], A[1], ..., A[N-1] , where each represents a point at coordinate (i, A[i]).

N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water. You need to return this maximum area.

Note: You may not slant the container. It is guaranteed that the answer will fit in integer limits.

Problem Constraints
1 <= N <= 10^5

1 <= A[i] <= 10^5

Input Format

Single Argument representing a 1-D array A.

Output Format

Return single Integer denoting the maximum area you can obtain.
Example Input

Input 1:

A = [1, 5, 4, 3]
Input 2:

A = [1]
'''

class Solution:
    def maxArea(self, A):
        left = 0
        right = len(A) - 1
        max_area = 0

        # Move pointers toward each other
        while left < right:
            # Calculate area between left and right
            height = min(A[left], A[right])
            width = right - left
            area = height * width

            # Update max area
            max_area = max(max_area, area)

            # Move the pointer pointing to the shorter line
            if A[left] < A[right]:
                left += 1
            else:
                right -= 1

        return max_area

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)
        if n < 2:
            return 0
        left, right = 0, n - 1
        max_area = 0
        while left < right:
            area = min(A[left], A[right]) * (right - left)
            max_area = max(max_area, area)
            if A[left] < A[right]:
                left += 1
            else:
                right -= 1
        return max_area

'''Optimized Solution (Two-Pointer Technique)
Approach:
Use two pointers: one at the start (left) and one at the end (right).
Calculate area between left and right.
Move the pointer pointing to the shorter line, hoping to find a taller line that might increase the area.
Time Complexity:
O(n) — each element is visited at most once.
Space Complexity:
O(1) — no extra space used.
'''

class Solution:
    def maxArea_brute_force(self, A):
        max_area = 0
        n = len(A)

        # Try every pair of lines
        for i in range(n):
            for j in range(i + 1, n):
                # Calculate area between lines i and j
                height = min(A[i], A[j])
                width = j - i
                area = height * width

                # Update max area if needed
                max_area = max(max_area, area)

        return max_area
'''Brute-Force Solution
Approach:
Try every pair of lines (i, j) where i < j.
Calculate the area for each pair.
Track the maximum area found.
Time Complexity:
O(n²) — nested loops over all pairs.
Space Complexity:
O(1) — no extra space used.
'''