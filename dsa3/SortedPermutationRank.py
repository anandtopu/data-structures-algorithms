'''Problem Description

Given a string A. Find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Note: The answer might not fit in an integer, so return your answer % 1000003



Problem Constraints

1 <= |A| <= 1000



Input Format

First argument is a string A.



Output Format

Return an integer denoting the rank of the given string.



Example Input

Input 1:

A = "acb"
Input 2:

A = "a"


Example Output

Output 1:

2
Output 2:

1


Example Explanation

Explanation 1:

Given A = "acb".
The order permutations with letters 'a', 'c', and 'b' :
abc
acb
bac
bca
cab
cba
So, the rank of A is 2.
Explanation 2:

Given A = "a".
Rank is clearly 1.'''


class Solution:
	# @param A : string
	# @return an integer
	def findRank(self, A):
        MOD = 1000003
        N = len(A)
        fact = [1] * (N + 1)
        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD
        rank = 1
        unused = list(A)
        for i in range(N):
            unused.sort()
            cnt = sum(1 for c in unused if c < A[i])
            rank = (rank + cnt * fact[N - 1 - i]) % MOD
            unused.remove(A[i])
        return rank