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

        # 利用二分法，还设置了提前终止的条件
        # 但提交之后，发现还是相对比较慢……回头再想想
        length = len(nums)

        if length == 0:
            return [-1, -1]
        if length == 1:
            return [0, 0] if nums[0] == target else [-1, -1]

        l, r = 0, length - 1
        start, end = -1, -1

        while l <= r:

            print("l", l, nums[l], "r", r, nums[r])

            if nums[l] == target and start == -1:
                start = l
            if nums[r] == target and end == -1:
                end = r
            if end != -1 and start != -1:
                break

            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l += 1
            else:
                r -= 1

            print(l, r, start, end)

        return [start, end]
# @lc code=end

