from typing import List


# 辅助函数
def backtracking(board: List[List[str]], word: str, visited: List[List[bool]], i: int, j: int, word_pos: int):
    if (i < 0 or i >= len(board) or j < 0 or j >= len(board[0])
            or visited[i][j] or board[i][j] != word[word_pos]):
        return False
    if word_pos == len(word) - 1:
        return True
    visited[i][j] = True  # 修改当前节点状态
    if (backtracking(board, word, visited, i + 1, j, word_pos + 1) or
            backtracking(board, word, visited, i - 1, j, word_pos + 1) or
            backtracking(board, word, visited, i, j + 1, word_pos + 1) or
            backtracking(board, word, visited, i, j - 1, word_pos + 1)):
        return True  # 递归子节点
    visited[i][j] = False  # 回改当前节点状态
    return False


# 主函数
def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    return any([
        backtracking(board, word, visited, i, j, 0)
        for i in range(m) for j in range(n)
    ])

word = "ABCCED"
board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]

print(exist(board,word))