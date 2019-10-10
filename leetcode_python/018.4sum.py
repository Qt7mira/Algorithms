#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (36.03%)
# Likes:    279
# Dislikes: 0
# Total Accepted:    32.7K
# Total Submissions: 91K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []

        if len(nums) == 0:
            return res

        nums = sorted(nums)

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            new_target = target - nums[i]
            for j in range(i + 1, len(nums) - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, len(nums) - 1

                while l < r:
                    m = nums[j] + nums[l] + nums[r]

                    if m < new_target:
                        l += 1
                    elif m > new_target:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        while l < r and nums[l] == nums[l + 1]:
                            l += 1

                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        l += 1
                        r -= 1

        return res
