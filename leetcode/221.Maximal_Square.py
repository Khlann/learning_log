
from typing import List
def maximalSquare(matrix):
    m = len(matrix)
    n = len(matrix[0])
    # Bug fix: Correctly initialize the dp array
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return max([max(row) for row in dp]) ** 2

if __name__ == '__main__':
    # Note: The elements in the matrix should be strings '1' and '0'
    matrix = [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]
    print(maximalSquare(matrix))
