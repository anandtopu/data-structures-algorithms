'''

Example 1:

Input: digits = [1,2,3] Output: [1,2,4] Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1] Output: [4,3,2,2] Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9] Output: [1,0] Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Add one using carry starting from the least-significant digit.
        carry = 1
        n = len(digits)
        # Work in-place from the end
        for i in range(n - 1, -1, -1):
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
            # early exit if there's no carry
            if carry == 0:
                return digits

        # If there's still a carry after processing all digits,
        # insert it at the front (e.g. 999 -> 1000)
        if carry:
            digits.insert(0, carry)
        return digits


if __name__ == "__main__":
    # Quick manual tests using the examples from the docstring
    s = Solution()
    tests = [([1,2,3], [1,2,4]),
             ([4,3,2,1], [4,3,2,2]),
             ([9], [1,0]),
             ([9,9,9], [1,0,0,0]),
             ([0], [1])]

    for inp, expected in tests:
        out = s.plusOne(list(inp))
        print(f"in={inp} -> out={out} expected={expected} {'OK' if out==expected else 'FAIL'}")