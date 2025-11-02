from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for d in digits:
            num = num * 10 + d
        num += 1
        return [int(x) for x in str(num)]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits

