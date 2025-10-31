
import heapq

class Solution:
    def solve(self, A, B, C):
        n, m = len(A), len(A[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        dist = [[float('inf')] * m for _ in range(n)]
        heap = [(0, B[0], B[1])]
        dist[B[0]][B[1]] = 0

        while heap:
            d, x, y = heapq.heappop(heap)
            if [x, y] == C:
                return d
            for dx, dy in directions:
                nx, ny, steps = x, y, 0
                # Roll until hitting a wall
                while 0 <= nx + dx < n and 0 <= ny + dy < m and A[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                    steps += 1
                if dist[nx][ny] > d + steps:
                    dist[nx][ny] = d + steps
                    heapq.heappush(heap, (dist[nx][ny], nx, ny))

        return -1
