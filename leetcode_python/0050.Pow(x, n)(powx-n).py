#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (33.25%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    43.1K
# Total Submissions: 128.5K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
#
#
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
#
#
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
#
# 说明:
#
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
#
#
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:

        # 整体思路还是2分：2^11 = 1 * 2^1 * 2^2 * 2^8
        #                           11    5  2  1
        # 下面的位运算其实只是个花活，用 %2 和 /2 同样可以判断奇偶和除2

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            # 判断奇偶，n & 1 = True时为奇数
            if n & 1:
                res *= x
            x *= x
            n >>= 1

        return res

# @lc code=end
