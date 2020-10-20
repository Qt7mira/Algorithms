#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (31.28%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    50.2K
# Total Submissions: 159.5K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
#
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        res = 0

        # case："a "
        s = s.strip()

        for c in s:
            if c != " ":
                res += 1
            else:
                res = 0
        return res

# @lc code=end

