class Solution:
    # @param A : list of integers (weights)
    # @param B : integer (capacity)
    # @return an integer
    def minRides(self, A, B):
        A.sort()
        left, right = 0, len(A) - 1
        rides = 0

        while left <= right:
            if A[left] + A[right] <= B:
                left += 1  # pair lightest with heaviest
            right -= 1
            rides += 1

        return rides