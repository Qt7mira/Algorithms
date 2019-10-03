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
        for cg in zip(*strs):
            if len(set(cg)) > 1:
                return strs[0][:l]
            l += 1
        return strs[0][:l]


a = ['abc', 'abcd', 'ab', 'ab']
sol = Solution()
# print(sol.longestCommonPrefix(a))
print(sol.longestCommonPrefix2(a))
