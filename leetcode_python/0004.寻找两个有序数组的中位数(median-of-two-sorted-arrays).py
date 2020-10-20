#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.85%)
# Likes:    1557
# Dislikes: 0
# Total Accepted:    93.9K
# Total Submissions: 260.9K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            # return findMedianSortedArrays(nums2, nums1)
            nums1, nums2 = nums2, nums1

        if len(nums1) == 0:
            if len(nums2) % 2 == 0:
                return (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            else:
                return nums2[len(nums2) // 2]

        length = len(nums1) + len(nums2)
        cut1, cut2 = 0, 0
        cut_l, cut_r = 0, len(nums1)

        if len(nums1) == 0:
            min_value, max_value = min(nums2) - 1, max(nums2) + 1
        elif len(nums2) == 0:
            min_value, max_value = min(nums1) - 1, max(nums1) + 1
        else:
            min_value, max_value = min(min(nums1), min(nums2)) - 1, max(max(nums1), max(nums2)) + 1

        # min_value, max_value = - 100 * 100, 100 * 100

        while cut1 < len(nums1):
            cut1 = int((cut_r - cut_l) / 2 + cut_l)
            cut2 = int(length / 2 - cut1)

            L1 = min_value if cut1 == 0 else nums1[cut1 - 1]
            L2 = min_value if cut2 == 0 else nums2[cut2 - 1]
            R1 = max_value if cut1 == len(nums1) else nums1[cut1]
            R2 = max_value if cut2 == len(nums2) else nums2[cut2]

            if L1 > R2:
                cut_r = cut1 - 1
            elif L2 > R1:
                cut_l = cut1 + 1
            else:
                # right pos
                if length % 2 == 0:
                    L1 = max(L1, L2)
                    R1 = min(R1, R2)
                    return (L1 + R1) / 2
                else:
                    return min(R1, R2)
        return -1


