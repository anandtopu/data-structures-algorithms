import heapq


class Solution:
    def solve(self, A):
        if len(A) == 1:
            return 0
        # Validate constraints
        if not isinstance(A, list):
            raise ValueError("Input must be a list of integers.")

        n = len(A)
        if n < 1 or n > 100000:
            raise ValueError("Array length must be between 1 and 100000.")

        for length in A:
            if not isinstance(length, int):
                raise ValueError("All elements must be integers.")
            if length < 1 or length > 1000:
                raise ValueError("Each rope length must be between 1 and 1000.")

        # Main logic using min-heap
        heapq.heapify(A)
        total_cost = 0

        while len(A) > 1:
            first = heapq.heappop(A)
            second = heapq.heappop(A)
            cost = first + second
            total_cost += cost
            heapq.heappush(A, cost)

        return total_cost

class Solution:
    def solve(self, A):
        # Validate input
        if not isinstance(A, list) or len(A) < 1 or len(A) > 100000:
            raise ValueError("Array length must be between 1 and 100000.")
        for length in A:
            if not isinstance(length, int) or length < 1 or length > 1000:
                raise ValueError("Each rope length must be between 1 and 1000.")

        # Sort the array
        A.sort()
        total_cost = 0

        while len(A) > 1:
            # Combine two smallest ropes
            first = A.pop(0)
            second = A.pop(0)
            cost = first + second
            total_cost += cost

            # Insert the new rope back in sorted order
            # This is O(n) because list insertion is costly
            from bisect import insort
            insort(A, cost)

        return total_cost


import heapq

def min_cost_to_connect_ropes(A):
    heapq.heapify(A)
    total_cost = 0

    while len(A) > 1:
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        cost = first + second
        total_cost += cost
        heapq.heappush(A, cost)

    return total_cost



def solve(self, A):
    def helper(start, end):
        if start == end:
            return (0, A[start])  # No cost, single rope length

        mid = (start + end) // 2
        left_cost, left_length = helper(start, mid)
        right_cost, right_length = helper(mid + 1, end)

        merge_cost = left_length + right_length
        total_cost = left_cost + right_cost + merge_cost

        return (total_cost, merge_cost)

    total_cost, _ = helper(0, len(A) - 1)
    return total_cost
