from typing import List

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A: int) -> List[int]:
        # Step 1: Sieve of Eratosthenes
        if A < 2:
            return []
        is_prime = [True] * (A + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(A ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, A + 1, i):
                    is_prime[j] = False

        # Step 2: Find the first valid pair
        for i in range(2, A // 2 + 1):
            if is_prime[i] and is_prime[A - i]:
                return [i, A - i]
        return []