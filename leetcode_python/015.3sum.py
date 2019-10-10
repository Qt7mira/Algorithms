class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            print('index', i)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                m = nums[i] + nums[l] + nums[r]
                if m < 0:
                    l += 1
                elif m > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    # 为了防止输出相同的结果数组，当出现相同的数字，指针继续移动
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # 指针继续移动
                    l += 1
                    r -= 1
        return res


sol = Solution()
# print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([-2, 0, 0, 2, 2]))
