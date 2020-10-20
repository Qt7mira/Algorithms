#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (71.51%)
# Likes:    551
# Dislikes: 0
# Total Accepted:    43.5K
# Total Submissions: 60.6K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 递归

        def helper(res, s, l, r):

            # 右括号比左括号多，肯定不对
            if l > r:
                return
            if l == 0 and r == 0:
                res.append(s)
            if l > 0:
                helper(res, s + "(", l - 1, r)
            if r > 0:
                helper(res, s + ")", l, r - 1)

        res = []
        if n == 0:
            return res
        helper(res, "", n, n)
        return res


