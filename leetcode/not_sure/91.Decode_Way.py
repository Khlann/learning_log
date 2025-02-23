def numDecodings(s):
    n = len(s)
    prev = ord(s[0])- ord('0')
    if prev == 0:
        return 0
    if n == 1:
        return 1
    dp = [1]*(n+1)
    for i in range(2,n+1):
        cur = ord(s[i-1])-ord('0')
        if (prev == 0 or prev > 2) and cur == 0:
            return 0
        if 0 < prev < 2 or (prev == 2 and cur <= 6):
            if cur == 0:
                dp[i] = dp [i-2]
            else:
                dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]
        prev = cur
    return dp[n]

if __name__ == '__main__':
    s = "226"
    print(numDecodings(s))