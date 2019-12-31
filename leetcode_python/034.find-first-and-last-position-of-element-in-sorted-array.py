#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (37.48%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    38.3K
# Total Submissions: 101.4K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # 新方法，用两次2分，分别找左右
        # 细节是魔鬼 T.T

        def find_l(nums, low, high):
            # 注意循环退出条件：带等号
            while low <= high:
                mid = low + ((high - low) >> 1)
                # 注意指针移动时，带 +1/-1，=mid可能会导致原地不动
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1

            return low

        def find_r(nums, low, high):
            while low <= high:
                mid = low + ((high - low) >> 1)
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        length = len(nums)
        start = find_l(nums, 0, length - 1)

        # nums 为空 或者 没有target
        if start == len(nums) or nums[start] != target:
            return [-1, -1]

        return [start, find_r(nums, 0, length - 1)]
# @lc code=end

