from typing import List

# def maxAreaOfIsland(grid: List[List[int]]) -> int:
#     direction = [-1, 0, 1, 0, -1]
#     m, n, max_area = len(grid), len(grid[0]), 0
#     for i in range(m):
#         for j in range(n):
#             if grid[i][j] == 1:
#                 island = []
#                 local_area = 1
#                 grid[i][j] = 0
#                 island.append((i, j))
#                 while len(island) > 0:
#                     r, c = island.pop()
#                     for k in range(4):
#                         x, y = r + direction[k], c + direction[k + 1]
#                         if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
#                             local_area += 1
#                             grid[x][y] = 0
#                             island.append((x, y))
#                 max_area = max(max_area, local_area)
#     return max_area

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j]== 0:
        return 0
    grid[i][j] = 0
    return (1 + dfs(grid, i-1, j) + dfs(grid, i, j+1) + dfs(grid, i, j-1) + dfs(grid, i+1 ,j)) 

def maxAreaOfIsland(grid:List[List[int]]):
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_area = max(max_area,dfs(grid,i,j))
    return max_area


# 测试示例
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(maxAreaOfIsland(grid))