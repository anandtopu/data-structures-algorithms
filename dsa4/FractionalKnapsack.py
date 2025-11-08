'''
Problem Description

Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum total value that we can fit in the knapsack. If the maximum total value is ans, then return ⌊ans × 100⌋ , i.e., floor of (ans × 100).

NOTE:

You can break an item for maximizing the total value of the knapsack



Problem Constraints

1 <= N <= 105

1 <= A[i], B[i] <= 103

1 <= C <= 103




Input Format

First argument is an integer array A of size N denoting the values on N items.

Second argument is an integer array B of size N denoting the weights on N items.

Third argument is an integer C denoting the knapsack capacity.




Output Format

Return a single integer denoting the maximum total value of A such that sum of the weights of this subset is smaller than or equal to C.


'''

from decimal import Decimal, getcontext
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        getcontext().prec = 10  # Set precision
        items = sorted(zip(A, B), key=lambda x: Decimal(x[0]) / Decimal(x[1]), reverse=True)
        total_value = Decimal(0)
        remaining_capacity = Decimal(C)

        for value, weight in items:
            value = Decimal(value)
            weight = Decimal(weight)
            if remaining_capacity == 0:
                break
            if weight <= remaining_capacity:
                total_value += value
                remaining_capacity -= weight
            else:
                total_value += value * (remaining_capacity / weight)
                remaining_capacity = Decimal(0)

        return int(total_value * Decimal(100))

