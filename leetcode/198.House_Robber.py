
# def rob(nums):
#     n = len(nums)
#     dp = [0] * (n + 1)
#     dp[1] = nums[0]
#     for i in range(2, n + 1):
#         dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
#     return dp[n]

def rob(nums):
    pre_pre = pre = cur = 0
    for i in range(len(nums)):
        cur = max(pre, pre_pre + nums[i])
        pre_pre = pre
        pre = cur
    return cur

if __name__ == '__main__':
    nums = [2,7,9,3,1]
    print(rob(nums))
