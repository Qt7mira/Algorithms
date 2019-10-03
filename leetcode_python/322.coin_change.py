#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (34.66%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 68.1K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1:
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2:
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 说明:
# 你可以认为每种硬币的数量是无限的。
#
#


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i] 在金额为i时的最优解
        # 假设coin有1，2，5，7，10
        # dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 5], dp[i - 7], dp[i - 10]) + 1
        # dp[i] = get_min(dp[i - coin[j]]) + 1

        dp = {}
        if coins is None or len(coins) == 0:
            return -1

        if amount < 0:
            return -1

        if amount == 0:
            return 0

        dp[0] = 0

        for i in range(1, amount + 1):
            if i in coins:
                dp[i] = 1
            else:
                dp[i] = -1

        for i in range(amount + 1):
            for coin in coins:
                if i - coin > 0 and dp[i - coin] != -1:
                    if dp[i] == -1 or dp[i] > dp[i - coin] + 1:
                        dp[i] = dp[i - coin] + 1

        return dp.get(amount, 0)


