from typing import List, Set
# 辅函数。
def dfs(isConnected: List[List[int]], city: int, visited: Set[int]):
    visited.add(city)
    for i in range(len(isConnected)):
        if isConnected[city][i] == 1 and i not in visited:
            dfs(isConnected, i, visited)
# 主函数。
def findCircleNum(isConnected: List[List[int]]) -> int:
    count = 0
    # 防止重复搜索已被搜索过的节点。
    visited = set()
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(isConnected, i, visited)
            count += 1
    return count

if __name__ == "__main__":
    grid =[[1,1,0],
           [1,1,0],
           [0,0,1]] 
    count = findCircleNum(grid)
    print(count)