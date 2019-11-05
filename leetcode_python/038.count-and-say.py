#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (52.04%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    49.6K
# Total Submissions: 94.2K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
#
# 注意：整数顺序将表示为一个字符串。
#
#
#
# 示例 1:
#
# 输入: 1
# 输出: "1"
#
#
# 示例 2:
#
# 输入: 4
# 输出: "1211"
#
#
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        res, new_res = "1", ""
        c, c_count = None, 0

        for i in range(1, n):
            for j in range(len(res)):
                if c:
                    if res[j] == res[j - 1]:
                        c_count += 1
                    else:
                        new_res += str(c_count) + str(c)
                        c = res[j]
                        c_count = 1
                else:
                    c = res[j]
                    c_count += 1
            new_res += str(c_count) + str(c)
            c, c_count = None, 0
            res = new_res
            new_res = ""
        return res

# @lc code=end


# 第二方案：使用内置函数groupby
# from itertools import groupby

# def countAndSay(n):
#     result = '1'
#     for i in range(1, n):
#         result = ''.join([str(len(list(g))) + k for k, g in groupby(result)])
#     return result
