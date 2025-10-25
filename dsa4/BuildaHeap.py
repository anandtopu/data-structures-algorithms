class Solution:
    # @param A: list of integers
    # @return: a list representing the binary min heap
    def build_heap(self, A: list[int] | None) -> list[int]:
        """
        Build a binary min-heap from list A in-place and return it.

        Edge cases handled:
        - A is None -> returns empty list.
        - A is not a list -> raises TypeError.
        - Empty or single-element lists -> returned as-is.

        Approach:
        - Bottom-up heap construction: call sift-down (heapify) from the last
          non-leaf node up to the root. This is O(n).
        - Use an iterative sift-down to avoid recursion depth limits.

        Dry-run example:
        - A = [3, 2, 1]
        - n = 3, start i = n//2 - 1 = 0
        - heapify(0):
            left = 1 (2), right = 2 (1) -> smallest = 2
            swap A[0] and A[2] -> [1, 2, 3]
            no further children -> done
        - Result: [1, 2, 3]
        """
        if A is None:
            return []

        if not isinstance(A, list):
            raise TypeError("build_heap expects a list or None")

        n = len(A)
        if n <= 1:
            # Empty or single-element list is already a valid heap
            return A

        def heapify(i: int, n: int):
            """Iterative sift-down: ensure subtree rooted at i is a min-heap."""
            while True:
                smallest = i
                left = 2 * i + 1
                right = 2 * i + 2

                # Compare with left child
                if left < n and A[left] < A[smallest]:
                    smallest = left
                # Compare with right child
                if right < n and A[right] < A[smallest]:
                    smallest = right

                if smallest == i:
                    # Current node is in correct position
                    break

                # Swap current node with the smallest child and continue
                A[i], A[smallest] = A[smallest], A[i]
                i = smallest

        # Build heap: start from the last non-leaf node down to the root
        for i in range(n // 2 - 1, -1, -1):
            heapify(i, n)

        return A