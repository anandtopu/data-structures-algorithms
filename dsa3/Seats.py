class Solution:
    def seats(self, A: str) -> int:
        MOD = 10000003
        positions = [i for i, ch in enumerate(A) if ch == 'x']

        if not positions:
            return 0

        median_index = len(positions) // 2
        median_pos = positions[median_index]

        # Calculate total moves to bring everyone to the median-centered block
        moves = 0
        for i, pos in enumerate(positions):
            target = median_pos - (median_index - i)
            moves = (moves + abs(pos - target)) % MOD

        return moves