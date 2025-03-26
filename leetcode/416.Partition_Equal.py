def pe(list):
    nums_sum = sum(list)
    if nums_sum % 2 != 0:
        return False
    target, n = nums_sum // 2, len(list)
    dp = [[False for _ in range(target + 1)] for _ in range(n+1)]
    dp[0][0] = True
    for i in range(1,n+1):
        for j in range(target+1):
            if j < list[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-list[i-1]]
    return dp[-1][-1]

list = [1,5,11,5]
result = pe(list)
print(result)