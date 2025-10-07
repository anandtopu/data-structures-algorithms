'''
Problem Description

Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.






If the answer does not exist return an array with a single integer "-1".

First sub-array means the sub-array for which starting index in minimum.








Problem Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 109
1 <= B <= 109



Input Format

The first argument given is the integer array A.

The second argument given is integer B.



Output Format

Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single integer "-1".



Example Input

Input 1:

 A = [1, 2, 3, 4, 5]
 B = 5
Input 2:

 A = [5, 10, 20, 100, 105]
 B = 110
'''
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # Initialize two pointers for the sliding window
        l = 0
        r = 0
        current_sum = 0

        # Traverse the array using the right pointer
        while r < len(A):
            # If the current element equals B, return it as a single-element subarray
            if A[r] == B:
                return [A[r]]

            # If current sum equals B, break to return the subarray
            if current_sum == B:
                break

            # If current sum exceeds B, shrink the window from the left
            elif current_sum > B:
                current_sum -= A[l]
                l += 1

            # Otherwise, expand the window to the right
            else:
                current_sum += A[r]
                r += 1

        # After loop, check if a valid subarray was found
        if l < r and current_sum == B:
            return A[l:r]
        else:
            return [-1]

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve_brute_force(self, A, B):
        # Try every possible subarray starting from index i
        for i in range(len(A)):
            current_sum = 0
            # Expand subarray from i to j
            for j in range(i, len(A)):
                current_sum += A[j]
                # If sum matches B, return the subarray
                if current_sum == B:
                    return A[i:j+1]
                # If sum exceeds B, break early
                elif current_sum > B:
                    break
        # If no subarray found, return [-1]
        return [-1]

'''
Brute Force: TC O(n²) SC O(1) Checks all subarrays
Optimized (Sliding Window) TC O(n) SC O(1) Works only for positive integers
'''
# Below solution works for both positive and negative integers

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        # Dictionary to store prefix sums and their earliest index
        prefix_sum_map = {}
        current_sum = 0

        for i in range(len(A)):
            current_sum += A[i]

            # Case 1: Subarray starts from index 0
            if current_sum == B:
                return A[0:i+1]

            # Case 2: Subarray found between indices (prefix_sum_map[current_sum - B] + 1) to i
            if (current_sum - B) in prefix_sum_map:
                start_index = prefix_sum_map[current_sum - B] + 1
                return A[start_index:i+1]

            # Store the current prefix sum if not already present
            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i

        # If no subarray found
        return [-1]