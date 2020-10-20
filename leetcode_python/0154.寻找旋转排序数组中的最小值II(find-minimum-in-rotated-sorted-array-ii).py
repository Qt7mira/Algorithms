#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (45.01%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 24.5K
# Testcase Example:  '[1,3,5]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。
#
# 示例 1：
#
# 输入: [1,3,5]
# 输出: 1
#
# 示例 2：
#
# 输入: [2,2,2,0,1]
# 输出: 0
#
# 说明：
#
#
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        low, high = 0, len(nums) - 1

        while low < high:
            mid = low + ((high - low) >> 1)
            print(low, high, mid)

            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            # [1, 0, 1, 1, 1] 在 low = 0, high = 4, mid = 2 时，无法判断 mid 在哪个排序区间中。
            else:
                # 预防[1, 1, 3, 1]的case
                # lc能够ac只是因为此时的high与最后的low的值相同
                # 但返回low的并不是旋转点
                if nums[high - 1] > nums[high]:
                    return nums[high]
                high -= 1

        return nums[low]

# @lc code=end

