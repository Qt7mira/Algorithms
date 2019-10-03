#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (62.28%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    34.1K
# Total Submissions: 54.6K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#
#


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        # dp[i][j]即在i,j位置时的最小总和
        # dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        row = len(grid)
        col = len(grid[0])

        # 初始化
        dp = []
        for i in range(row):
            dp.append([0] * col)
        dp[0][0] = grid[0][0]

        # 第一行：dp[0][j] = dp[0][j - 1] + grid[0][j]
        for j in range(1, col):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 第一列：dp[i][0] = dp[i - 1][0] + grid[i][0]
        for i in range(1, row):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
            for j in range(1, col):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[row - 1][col - 1]


