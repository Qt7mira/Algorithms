#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (41.48%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 106.8K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
#
#
#
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        res = 0
        diff_value = 100 ** 100
        nums = sorted(nums)

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                m = nums[i] + nums[l] + nums[r]

                if m < target:
                    if (target - m) < diff_value:
                        diff_value = target - m
                        res = m
                    l += 1
                elif m > target:
                    if (m - target) < diff_value:
                        diff_value = m - target
                        res = m
                    r -= 1
                else:
                    return m

        return res
