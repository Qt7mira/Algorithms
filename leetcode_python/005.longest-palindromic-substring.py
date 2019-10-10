#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.68%)
# Likes:    1317
# Dislikes: 0
# Total Accepted:    114.9K
# Total Submissions: 422.1K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        dp = {}
        max_value = 0

        if len(s) <= 1:
            return s

        for j in range(len(s)):
            for i in range(j + 1):
                # (j - i) <= 2 即只隔一个字母
                if s[i] == s[j] and ((j - i) <= 2 or dp[i + 1][j - 1]):
                    if i not in dp:
                        dp[i] = {}
                    if j not in dp[i]:
                        dp[i][j] = True

                else:
                    if i not in dp:
                        dp[i] = {}
                    if j not in dp[i]:
                        dp[i][j] = False

                if dp[i][j]:
                    if j - i + 1 > max_value:
                        max_value = j - i + 1
                        res = s[i: j + 1]

        return res


