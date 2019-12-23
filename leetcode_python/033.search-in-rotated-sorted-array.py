#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.09%)
# Likes:    361
# Dislikes: 0
# Total Accepted:    44.6K
# Total Submissions: 123.6K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # 先找到旋转节点，然后就是简单的有序数据找数了

        def find_rotated_index(l, r):
            rotated_index = 0

            # 不加等号是因为想要后面的那个元素的index
            while l < r:

                # +1 是因为想要后面的那个元素的index
                rotated_index = (l + r + 1) // 2
                if nums[rotated_index] > nums[l]:
                    l += 1
                else:
                    r -= 1

            return rotated_index

        def search_result(l, r):

            while l <= r:

                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid

                if target > nums[l]:
                    l += 1
                else:
                    r -= 1

            return -1

        length = len(nums)
        if length == 0:
            return -1
        if length == 1:
            return 0 if nums[0] == target else -1

        l = 0
        r = length - 1

        ind = find_rotated_index(l, r)
        print("id", ind)

        if nums[ind] <= target <= nums[r]:
            return search_result(ind, r)
        elif nums[l] <= target <= nums[ind - 1]:
            return search_result(l, ind - 1)
        else:
            return -1

# @lc code=end
