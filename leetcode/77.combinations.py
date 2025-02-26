from typing import List


# 辅函数。
def backtracking(
        combinations: List[List[int]], pick: List[int], pos: int, n: int, k: int
):
    if len(pick) == k:
        combinations.append(pick[:])  # int为基本类型，可以浅拷贝
        return
    for i in range(pos, n + 1):
        pick.append(i)  # 修改当前节点状态
        backtracking(combinations, pick, i + 1, n, k)  # 递归子节点
        pick.pop()  # 回改当前节点状态


# 主函数。
def combine(n: int, k: int) -> List[List[int]]:
    combinations = []
    pick = []
    backtracking(combinations, pick, 1, n, k)
    return combinations

print(combine(4,2))