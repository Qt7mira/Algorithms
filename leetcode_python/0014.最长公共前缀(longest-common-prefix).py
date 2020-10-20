#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.48%)
# Likes:    706
# Dislikes: 0
# Total Accepted:    126.1K
# Total Submissions: 362.1K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        prefix = strs[0]
        for one_str in strs[1:]:
            i = 0
            while i < len(one_str) and i < len(prefix) and prefix[i] == one_str[i]:
                i += 1
            prefix = prefix[:i]
            print(prefix)
        return prefix

    """an answer using zip"""

    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        l = 0
        for i in zip(*strs):
            if len(set(i)) > 1:
                return strs[0][:l]
            l += 1
        return strs[0][:l]
