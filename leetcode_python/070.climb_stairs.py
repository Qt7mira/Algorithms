#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (46.50%)
# Likes:    593
# Dislikes: 0
# Total Accepted:    70.8K
# Total Submissions: 152.3K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#
#


class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归思想，超时
        # if n == 1 or n == 2:
        #     return n

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # 动态规划
        dp = {}
        dp[1] = 1
        dp[2] = 2

        # range里不是range(3, n)
        # 避免range(3, 3)的情况，同时range(3, n)也到不了n
        for i in range(3, n + 1):
            dp[i] = dp.get(i - 1, 0) + dp.get(i - 2, 0)

        return dp[n]
