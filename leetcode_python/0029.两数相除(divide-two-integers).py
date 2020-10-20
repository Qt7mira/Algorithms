#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#
# https://leetcode-cn.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (18.64%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 123.3K
# Testcase Example:  '10\n3'
#
# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
#
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
#
# 说明:
#
#
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 2^31 − 1。
#
#
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # 使用异或判断dividend和divisor的符号差别
        sign = int(dividend > 0) ^ int(divisor > 0)

        dividend = dividend if dividend >= 0 else -dividend
        divisor = divisor if divisor >= 0 else -divisor

        res = 0

        # 思路：使用位操作扩大divisor，节省计算时间
        while divisor <= dividend:
            temp = 1
            temp_d = divisor
            while temp_d << 1 <= dividend:
                if temp_d >= 1 << 31:
                    break
                temp = temp << 1
                temp_d = temp_d << 1

            dividend = dividend - temp_d
            res += temp

        # 题目要求的边界判断 [−2^31,  2^31 − 1]

        if sign == 1:
            res = max(-res, -(1 << 31))
        else:
            res = min(res, (1 << 31) - 1)

        return res

# @lc code=end

