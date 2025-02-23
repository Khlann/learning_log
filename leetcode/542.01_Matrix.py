import sys
def updateMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[sys.maxsize] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] !=0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1,dp[i][j - 1] + 1)
            else:
                dp[i][j] = 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if matrix[i][j]!=0:
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
    return dp

if __name__ == '__main__':
    matrix = [[1,0,1],[1,1,1],[1,1,1]]
    print(updateMatrix(matrix))