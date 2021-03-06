#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (34.27%)
# Likes:    79
# Dislikes: 0
# Total Accepted:    15K
# Total Submissions: 43.3K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
# 进阶:
#
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def find_rotated(nums, low, high):

            while low < high:
                mid = low + ((high - low) >> 1)

                if nums[mid] > nums[high]:
                    low = mid + 1
                elif nums[mid] < nums[high]:
                    high = mid
                else:
                    if nums[high - 1] > nums[high]:
                        return high
                    high -= 1

            return low

        def find_target(nums, low, high, target):

            while low <= high:

                mid = low + ((high - low) >> 1)

                if nums[mid] == target:
                    return True

                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        length = len(nums)
        if length == 0:
            return False
        if length == 1:
            return True if nums[0] == target else False

        rotated_index = find_rotated(nums, 0, length - 1)

        if nums[rotated_index] <= target <= nums[-1]:
            return find_target(nums, rotated_index, length - 1, target)
        elif nums[0] <= target <= nums[rotated_index - 1]:
            return find_target(nums, 0, rotated_index, target)
        else:
            return False

# @lc code=end

