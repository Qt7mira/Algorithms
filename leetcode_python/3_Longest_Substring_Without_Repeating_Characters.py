class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = 0
        ans = 0
        d = {}

        for index, value in enumerate(s):
            if value in d:
                start = max(start, d[value] + 1)
            d[value] = index
            ans = max(ans, index - start + 1)
            print(start, d, ans)
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
