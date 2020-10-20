#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.49%)
# Likes:    752
# Dislikes: 0
# Total Accepted:    170.6K
# Total Submissions: 301.6K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
#
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        p = len(str(int)) // 2

        if str(x)[0:p] == str(x)[::-1][0:p]:
            return True

        return False


class Solution:
    def isPalindrome(self, x):
        """
        判断x是否是回文
        :type x: int
        :rtype: bool
        
        思路：取后半部分反转后与前半部分比较
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revNumber = 0
        # 原始数字小于倒数时，表示已经处理了一半的数字位数
        while x > revNumber:
            revNumber = revNumber * 10 + x % 10
            x //= 10

        print(revNumber)
        print(x)
        return x == revNumber or x == revNumber // 10

    # 判断字符串是个回文
    def isPalindrome2(self, my_str):
        return my_str == my_str[::-1]


