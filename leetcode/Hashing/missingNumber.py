from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor_all = 0
        xor_nums = 0
        n = len(nums)

        for i in range(n + 1):
            xor_all ^= i
        for num in nums:
            xor_nums ^= num

        return xor_all ^ xor_nums

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in num_set:
                return i
# Time Complexity: O(N)
# Space Complexity: O(N)