#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (45.96%)
# Likes:    595
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 62K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        max_left, max_right = 0, 0

        # 不管两边，而是找最高，每次计算1单位宽的储水量
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                res += (max_left - height[l]) * 1
                l += 1
            else:
                max_right = max(max_right, height[r])
                res += (max_right - height[r]) * 1
                r -= 1

        return res


