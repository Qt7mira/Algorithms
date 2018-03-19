class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_dic = dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in nums_dic.keys():
                return [nums_dic[sub], index]
            else:
                nums_dic[value] = index
        return "no matched nums"


sol = Solution()
print(sol.twoSum([3, 2, 4], 6))
