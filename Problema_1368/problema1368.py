from collections import deque

class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dq = deque()
        dq.append((0, 0, 0))
        visited = [[False] * n for _ in range(m)]
        
        while dq:
            x, y, cost = dq.popleft()
            if visited[x][y]:
                continue
            visited[x][y] = True
            if x == m - 1 and y == n - 1:
                return cost
            for idx, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[x][y] == idx + 1:
                        dq.appendleft((nx, ny, cost))
                    else:
                        dq.append((nx, ny, cost + 1))
