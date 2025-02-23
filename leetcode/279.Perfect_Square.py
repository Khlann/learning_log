
import sys
import math

def numSquares(n):
    dp = [0] + [sys.maxsize] * n
    for i in range(1, n + 1):
        # Bug fix: import math and use math.floor and math.sqrt
        for j in range(1, int(math.floor(math.sqrt(i))) + 1):
            dp[i] = min(dp[i], dp[i - j * j] + 1)
    return dp[n]

if __name__ == '__main__':
    n = 9
    print(numSquares(n))