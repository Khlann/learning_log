

# 辅助函数
def backtracking(solutions, board,
                 column, ldiag, rdiag, row):
    n = len(board)
    if row == n:
        solutions.append(["".join(row) for row in board])
        return
    for i in range(n):
        if column[i] or ldiag[n - row + i - 1] or rdiag[row + i]:
            continue
        # 修改当前节点状态
        board[row][i] = "Q"
        column[i] = ldiag[n - row + i - 1] = rdiag[row + i] = True
        # 递归子节点
        backtracking(solutions, board, column, ldiag, rdiag, row + 1)
        # 回改当前节点状态
        board[row][i] = "."
        column[i] = ldiag[n - row + i - 1] = rdiag[row + i] = False
    return solutions


# 主函数
def solveNQueens(n: int) -> List[List[str]]:
    solutions = []
    board = [["." for _ in range(n)] for _ in range(n)]
    column = [False] * n
    ldiag = [False] * (2 * n - 1)
    rdiag = [False] * (2 * n - 1)
    backtracking(solutions, board, column, ldiag, rdiag, 0)
    return solutions

n = 4
print(solveNQueens(n))