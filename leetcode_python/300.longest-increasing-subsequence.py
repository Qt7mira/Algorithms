#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.93%)
# Likes:    307
# Dislikes: 0
# Total Accepted:    30.3K
# Total Submissions: 70K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp[i]代表以nums[i]为结尾的最大上升子序列
        # 是O(n2)

        # 如果想O(nlogn)的话，应该是对dp进行二分查找
        # dp[i]代表长度为i+1的上升子序列的最小可能取值

        if nums is None or len(nums) == 0:
            return 0

        # 初始化dp
        dp = [1] * len(nums)
        for i in range(1, len(nums)):

            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

