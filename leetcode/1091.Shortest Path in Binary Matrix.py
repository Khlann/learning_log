import collections
from typing import List


def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    if grid[0][0] == 1:
        return -1
    m, n = len(grid), len(grid[0])
    dist = 0
    q = collections.deque()
    q.append((0, 0))
    grid[0][0] = -1
    while q:
        size = len(q)
        dist += 1
        for _ in range(size):
            r, c = q.popleft()
            if r == m - 1 and c == n - 1:
                return dist
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    x, y = r + dx, c + dy
                    if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] != 0:
                        continue
                    grid[x][y] = -1
                    q.append((x, y))
    return -1

input = [[0,0,1],
         [1,1,0],
         [1,1,0]]

print(shortestPathBinaryMatrix(input))