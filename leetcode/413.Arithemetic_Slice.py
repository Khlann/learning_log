def ars(nums):
    n = len(nums)
    dp = [0] * n
    for i in range(2, n):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            dp[i] = dp[i - 1] + 1
    return sum(dp)

if __name__ == '__main__':
    nums = [1,2,3,4]
    print(ars(nums))