#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (61.74%)
# Likes:    301
# Dislikes: 0
# Total Accepted:    44.2K
# Total Submissions: 70.9K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy

        # 注意终止条件，判断下一个和下下个不为None
        while curr.next and curr.next.next:
            a, b = curr.next, curr.next.next
            curr.next, a.next = b, b.next
            b.next = a
            curr = curr.next.next

        return dummy.next

# @lc code=end

