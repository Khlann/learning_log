from typing import List
direction = [-1, 0, 1, 0, -1]

def dfs(heights: List[List[int]], can_reach: List[List[int]], r: int, c: int):
    if can_reach[r][c]:
        return
    can_reach[r][c]=True
    for i in range(4):
        x, y = r + direction[i], c + direction[i+1]
        if (x >= 0 and x< len(heights) and y >= 0 and y < len(heights[0]) and heights[x][y] >= heights[r][c]):
            dfs(heights, can_reach, x, y)

def pacificAltantic(heights: List[List[int]]):
    m, n = len(heights), len(heights[0])
    can_reach_p  = [[False for _ in range(n)]for _ in range(m)]
    can_reach_a  = [[False for _ in range(n)]for _ in range(m)]
    for i in range(m):
        dfs(heights, can_reach_p, i, 0)
        dfs(heights, can_reach_a, i, n-1)
    for j in range(n):
        dfs(heights, can_reach_p, 0, j)
        dfs(heights, can_reach_a, m-1, j)
    return[
        [i,j] for i in range(m) for j in range(n)
        if can_reach_p[i][j] and can_reach_a[i][j]
    ]
    
grid = [[1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
]

print(pacificAltantic(grid))