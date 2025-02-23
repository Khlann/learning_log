
def wordBreak(s, wordDict):
    n = len(s)
    dp = [True] + [False] * n
    for i in range(1, n+1):
        for word in wordDict:
            if i >= len(word) and s[i-len(word):i] == word:
                dp[i] = dp[i-len(word)]
            if dp[i]:
                break
    return dp[n]
if __name__ == '__main__':
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(wordBreak(s, wordDict))