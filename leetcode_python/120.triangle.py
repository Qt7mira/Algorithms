#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (61.25%)
# Likes:    223
# Dislikes: 0
# Total Accepted:    23.8K
# Total Submissions: 38.5K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
#
# 例如，给定三角形：
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
# 说明：
#
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
#
#


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        # dp[i][j] 代表走到第i行, 第j行的最优解
        # 从下往上思考，dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        dp = {}

        # 初始化复制
        for i in range(len(triangle)):
            if i not in dp:
                dp[i] = {}
            for j in range(len(triangle[i])):
                dp[i][j] = 0

        n = len(triangle)

        # 最后一行，即新dp的第一行
        for j in range(len(triangle[n - 1])):
            dp[n - 1][j] = triangle[n - 1][j]

        # 倒序遍历
        for i in range(len(triangle) - 1)[::-1]:
            for j in range(len(triangle[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]
