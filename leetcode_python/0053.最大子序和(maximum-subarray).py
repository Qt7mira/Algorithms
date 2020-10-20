#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (46.94%)
# Likes:    1264
# Dislikes: 0
# Total Accepted:    103.1K
# Total Submissions: 216.7K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
#


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if dp[i - 1] > 0: dp[i] = dp[i - 1] + nums[i]
        # else: dp[i] = nums[i]
        # so: dp[i] = max(dp[i - 1] + nums[i], nums[i])

        if nums is None or len(nums) == 0:
            return 0

        n = len(nums)
        dp = {}

        dp[0] = nums[0]
        res = dp[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(res, dp[i])

        return res





