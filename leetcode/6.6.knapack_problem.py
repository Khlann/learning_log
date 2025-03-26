def knapack_problem(weight, value, n, w):
    dp = [[0 for _ in range(w + 1)] for _ in range(n+1)]
    for i in range(1, n+1):
        weight_i = weight[i-1]
        value_i = value[i-1]
        for j in range(1,w+1):
            if j >= weight_i:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight_i] + value_i)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]

weights_example = [2, 3, 1, 4]
values_example = [3, 4, 2, 5]
n_example = len(weights_example)
w_example = 6
print(knapack_problem(weights_example, values_example, n_example, w_example))