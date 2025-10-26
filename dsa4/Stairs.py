'''v=Problem Description

You are climbing a staircase and it takes A steps to reach the top.


Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Return the number of distinct ways modulo 1000000007



Problem Constraints

1 <= A <= 105



Input Format

The first and the only argument contains an integer A, the number of steps.



Output Format

Return an integer, representing the number of ways to reach the top.



Example Input

Input 1:

 A = 2
Input 2:

 A = 3


Example Output

Output 1:

 2
Output 2:

 3'''
from re import A
MOD = 1000000007

class SolutionDP:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        if A <= 0:
            return 0
        if A == 1:
            return 1
        if A == 2:
            return 2

        prev1, prev2 = 1, 2
        for _ in range(3, A + 1):
            curr = (prev1 + prev2) % MOD
            prev1, prev2 = prev2, curr
        return prev2

class SolutionExponentiation:
    def climbStairs(self, A):
        MOD = 1000000007

        def multiply(mat1, mat2):
            return [
                [(mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]) % MOD,
                 (mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]) % MOD],
                [(mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]) % MOD,
                 (mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]) % MOD]
            ]

        def power(matrix, n):
            result = [[1, 0], [0, 1]]  # Identity matrix
            while n > 0:
                if n % 2 == 1:
                    result = multiply(result, matrix)
                matrix = multiply(matrix, matrix)
                n //= 2
            return result

        if A == 1:
            return 1
        if A == 2:
            return 2

        base = [[1, 1], [1, 0]]
        res = power(base, A - 2)

        # f(n) = res[0][0]*f(2) + res[0][1]*f(1)
        return (res[0][0] * 2 + res[0][1] * 1) % MOD